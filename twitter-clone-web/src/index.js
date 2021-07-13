import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {TweetComponent,TweetDetailComponent} from './tweets'
import reportWebVitals from './reportWebVitals';


const appEl = document.getElementById('root')


if (appEl){
  ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  appEl
  );
}
const e = React.createElement
const tweetEl = document.getElementById('tweet-row')

if (tweetEl){
   ReactDOM.render(
      e(TweetComponent,tweetEl.dataset),tweetEl);
}

const tweetDetailElement = document.querySelectorAll(".tweet-2-detail")

tweetDetailElement.forEach(container=> {
  ReactDOM.render(
      e(TweetDetailComponent,container.dataset),container);
})


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
