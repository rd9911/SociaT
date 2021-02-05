import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { TweetComponent } from './tweets';
import reportWebVitals from './reportWebVitals';

const sociat = document.getElementById('sociat')
ReactDOM.render(
  <React.StrictMode>
    <TweetComponent />
  </React.StrictMode>,
  sociat
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
