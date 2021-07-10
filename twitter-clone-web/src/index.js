import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {TweetComponent} from './tweets'
import reportWebVitals from './reportWebVitals';


const appEl = document.getElementById('root')

const tweetEl = document.getElementById('tweet-row')
if (appEl){
  ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  appEl
  );
}

if (tweetEl){
   ReactDOM.render(
  <React.StrictMode>
    <TweetComponent />
  </React.StrictMode>,
  tweetEl
  );
}


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
