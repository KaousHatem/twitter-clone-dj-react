
import React, {useEffect, useState} from 'react';

import {TweetsList} from './list'
import {TweetCreate} from './create'
import {apiTweetDetail} from './lookup'
import {Tweet} from './detail'
 

export function TweetComponent(props) {
  const [newTweets, setNewTweets] = useState([])
  // const {canTweet} = props
  const canTweet = props.canTweet === "false" ? false : true
  // console.log(canTweet === true)
  const handleNewTweet = (newTweet) => {
    // backend api handler
    let tempNewTweets = [...newTweets]
    tempNewTweets.unshift(newTweet)
    setNewTweets(tempNewTweets)
   
  }
  return <div className={props.className}> 
      { canTweet === true && <TweetCreate didTweet={handleNewTweet} className="col-12 mb-3" />}
    {<TweetsList newTweets={newTweets} {...props}/>}
  </div>
}

export function TweetDetailComponent(props) {
  const {tweetId} = props
  const [didLookup, setDidLookup] = useState(false)
  const [tweet, setTweet] = useState(null)

  const handleBackendLookup = (response,status) => {
    if(status === 200){
      setTweet(response)
    }else {
      alert("There is an error finding your tweet")
    }
  }
  useEffect(()=>{
    if (didLookup === false){
      apiTweetDetail(tweetId,handleBackendLookup)
      setDidLookup(true)
    }
  },[tweetId,didLookup, setDidLookup])

  return tweet === null ? null : <Tweet tweet={tweet} className={props.className} />
}






