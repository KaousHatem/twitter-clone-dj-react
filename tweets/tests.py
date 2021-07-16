from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from .models import Tweet

# Create your tests here.

User = get_user_model()

class TweetTestCase(TestCase):
	"""docstring for TweetTestCase"""
	def setUp(self):
		self.user = User.objects.create_user(username="cfe", password="password2")
		self.userb = User.objects.create_user(username="cfe1", password="password1")
		Tweet.objects.create(content="my first tweet",user=self.user)
		Tweet.objects.create(content="my first tweet",user=self.user)
		Tweet.objects.create(content="my first tweet",user=self.userb)
		self.currentCount = Tweet.objects.all().count()

	def test_tweet_created(self):
		tweet_obj = Tweet.objects.create(content="my second tweet",user=self.user)
		self.assertEqual(tweet_obj.id, 4)
		self.assertEqual(tweet_obj.user, self.user)

	def get_client(self):
		client = APIClient()
		client.login(username=self.user.username, password='password2')
		return client

	

	def test_tweet_list(self):
		client = self.get_client()
		response = client.get('/api/tweets/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 3)

	def test_tweet_related_name(self):
		user = self.user
		self.assertEqual(user.tweets.count(), 2)



	def test_action_like(self):
		client = self.get_client()
		response = client.post('/api/tweets/action/',{"id": 1,"action": "like"})
		self.assertEqual(response.status_code, 200)
		like_count = response.json().get('likes')
		self.assertEqual(like_count, 1)
		user = self.user
		my_like_instances_count = user.tweetlike_set.count()
		self.assertEqual(my_like_instances_count, 1)
		my_related_likes = user.tweet_user.count()
		self.assertEqual(my_like_instances_count, my_related_likes)
		
		
	def test_action_unlike(self):
		client = self.get_client()
		response = client.post('/api/tweets/action/',{"id": 2,"action": "like"})
		self.assertEqual(response.status_code, 200)
		response = client.post('/api/tweets/action/',{"id": 2,"action": "unlike"})
		self.assertEqual(response.status_code, 200)
		like_count = response.json().get('likes')
		self.assertEqual(like_count, 0)
		

	def test_action_retweet(self):
		client = self.get_client()
		currentCount = self.currentCount
		response = client.post('/api/tweets/action/',{"id": 2,"action": "retweet"})
		self.assertEqual(response.status_code, 201)
		data = response.json()
		retweet_id = data.get('id')
		self.assertNotEqual(retweet_id, 2)
		self.assertEqual(retweet_id, currentCount+1)
		

	def test_tweet_create_api_view(self):
		request_data = {'content': "this is my view tweet"}
		client = self.get_client()
		response = client.post('/api/tweets/create/',request_data)
		self.assertEqual(response.status_code, 201)
		response_data = response.json()
		retweet_id = response_data.get('id')
		self.assertEqual(retweet_id, self.currentCount+1)

	def test_tweet_detail_api_view(self):
		client = self.get_client()
		response = client.get("/api/tweets/1/")
		self.assertEqual(response.status_code, 200)
		data = response.json()
		_id = data.get("id")
		self.assertEqual(_id, 1)

	def test_tweet_delete_api_view(self):
		client = self.get_client()
		response = client.delete("/api/tweets/1/delete/")
		self.assertEqual(response.status_code, 200)
		response = client.delete("/api/tweets/1/delete/")
		self.assertEqual(response.status_code, 404)

		response_incorrect_owner = client.delete("/api/tweets/3/delete/")
		self.assertEqual(response_incorrect_owner.status_code, 401)
		
