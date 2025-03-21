/*
    Timer code
    Note: This is a sample WIP, see: javascript self - adjusting timer

    var interval = 1000; // ms
    var expected = Date.now() + interval;
    setTimeout(step, interval);
    function step() {
        var time = Date.now() - expected; // the drift (positive for overshooting)
        if (time > interval) {
            console.log("big error");
            // something really bad happened. Maybe the browser (tab) was inactive?
            // possibly special handling to avoid futile "catch up" run
        }
        expected += interval;
        setTimeout(step, Math.max(0, interval - time)); // take into account drift
        document.getElementById("timer").innerHTML = time;
    }
    let listOfQuestions = [
  {
     question: 'Some text here',
     answer: 'this-is-answer'
  }, {
     question: 'Some text here2',
     answer: 'this-is-answer2'
  }
]; //---> dummy
let generatedQuestion = listOfWords.random();  //---> abang for later integration
let objectives = {
   isAnswerCorrect: false,
   isTimeExpired: false,
   //...
};

function userSubmitAnswer(inputAnswer) {
  if (inputAnswer == generatedQuestion.answer) {
     // User wins this round
  } else {
     // Bot wins this round
  }
};
 
*/

/*
     Button codes
*/
