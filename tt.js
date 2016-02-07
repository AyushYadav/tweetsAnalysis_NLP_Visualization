
var indico = require('indico.io');
indico.apiKey =  '0f895ffef7dd20aef5bc9da1c6e75e4a';

var response = function(res) { console.log(res); }
var logError = function(err) { console.log(err); }

// single example
indico.sentiment("I love writing code!")
  .then(response)
  .catch(logError);

// batch example
var batchInput = [
    "I love writing code!",
    "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
];
indico.sentiment(batchInput)
  .then(response)
  .catch(logError);



// $.post(
//   'https://apiv2.indico.io/sentiment?key=0f895ffef7dd20aef5bc9da1c6e75e4a',
//   JSON.stringify({
//     'data': "I love writing code!"
//   })
// ).then(function(res) { console.log(res) });

// // batch example
// $.post(
//   'https://apiv2.indico.io/sentiment/batch?key=0f895ffef7dd20aef5bc9da1c6e75e4a',
//   JSON.stringify({
//     'data': [
//       "I love writing code!",
//       "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
//     ]
//   })
// ).then(function(res) { console.log(res) });

// 851 032 514
// ku5d69