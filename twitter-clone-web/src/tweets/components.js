
import React, {useEffect, useState} from 'react';
import {apiTweetList,apiTweetCreate} from './lookup'

export function TweetComponent(props) {
  const [newTweets, setNewTweets] = useState([])
  const textAreaRef = React.createRef() 

  const handleBackendUpdate = (response,status) => {
    // backend api handler
    let tempNewTweets = [...newTweets]
    if (status === 201){
      tempNewTweets.unshift({response})
      setNewTweets(tempNewTweets)
    } else {
      alert("An error occured please try again")
    }
  }

  const handleSubmit = (event) => {
    // backend api request
    event.preventDefault()
    const newValue = textAreaRef.current.value
    apiTweetCreate(newValue,handleBackendUpdate)
    
    textAreaRef.current.value = ''
  }
  return <div className={props.className}> 
    <div className="col-12 mb-3">
      <form onSubmit={handleSubmit}>
        <textarea ref={textAreaRef} required={true} className="form-control" name="tweet" id="">
          
        </textarea>
        <button type="submit" className="btn btn-primary my-3" >Tweet</button>    
      </form>
    </div>
    {<TweetsList newTweets={newTweets} />}
  </div>
}



export function TweetsList(props){
  const [tweetsInit, setTweetsInit] = useState([])
  const [tweets, setTweets] = useState([])
  const [tweetsDidSet, setTweetsDidSet] = useState(false)

  useEffect(() => {

    const final = [...props.newTweets].concat(tweetsInit)
    if (final.length !== tweets.length){
      setTweets(final)
      console.log(final)
    }
  },[props.newTweets,tweets,tweetsInit])

  useEffect(() => {
    if (tweetsDidSet === false) {
      // do my lookup
      const handleTweetListLookup = (response,status) => {
        if (status === 200){
          setTweetsInit(response)
          setTweetsDidSet(true)
        }
        
      }
      apiTweetList(handleTweetListLookup)
    }
  }, [tweetsInit,tweetsDidSet,setTweetsDidSet])

  return tweets.map((item,index) =>{
    return <Tweet tweet={item} key={`${index}-{item.id}`} className="my-5 py-5 border bg-white text-dark"/>
  })
}

export function ActionBtn(props) {
  const {tweet, action} = props
  const [likes,setLikes] = useState(tweet.likes ? tweet.likes : 0)
  const [userLiked, setUserLiked] = useState(false)
  const className = props.className ? props.className : 'btn btn-primary'
  const actionDisplay = action.display ? action.display : 'Action'
  
  const handleClick = (event) => {
  	event.preventDefault()
  	if (action.type === 'like'){
  		if (userLiked === true){
  			setUserLiked(false)
  			setLikes(likes - 1)
  		}else {
  			setUserLiked(true)
  			setLikes(tweet.likes + 1)
  		}
  		
  	}
  }
  const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
  return <button className={className} onClick={handleClick}>{display}</button>

}

export function Tweet(props) {
  const {tweet} = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return <div className={className}>
    <p>{tweet.id} - {tweet.content}</p>
    <div className='btn btn-group'>
      <ActionBtn tweet={tweet} action={{type:"like",display:"Likes"}}/>
      <ActionBtn tweet={tweet} action={{type:"unlike", display:"Unlike"}}/>
      <ActionBtn tweet={tweet} action={{type:"retweet", display:"Retweet"}}/>
    </div>
  </div>
}
