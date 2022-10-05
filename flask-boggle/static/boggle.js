let $word = $(".word");
let $form = $(".word-form");
let $message = $(".message");
let $score = $(".score");
let $timer = $(".timer");
let $played = $(".times-played");
let $hiScoreNum = $(".hi-score-num");
let $reset = $(".reset");
let $resetDiv = $(".reset-div");
let $boggle = $("#boggle");
let score = 0;
let timer = 60;

function keepTime() {
  // Count down from 60
  x = setInterval(function () {
    timer -= 1;
    if (timer < 0) {
      $form.hide();
      endGame(x);
    } else {
      $timer.text("Time: " + timer);
    }
  }, 1000);
}

async function getWord(evt) {
  evt.preventDefault();
  // Get the word out of the form
  let word = $word.val();
  // Send it to the server
  let response = await axios.get("/check", { params: { word: word } });
  console.log(response);
  // Reset the form
  $word.val("");
  // If we got a response back from the server, process it
  if (response.data.result) {
    message(response.data.result);
    if (response.data.result === "ok") updateScore(word);
  }
}

function message(msg) {
  $message.text(msg);
}

function updateScore(word) {
  score += word.length;
  console.log(score);
  console.log(word.length);
  $score.text("Score: " + score);
}

function updatePlayed(times) {
  $played.text("Number of times played: " + times);
}

function updateHiScore() {
  if (parseInt($hiScoreNum.text()) < score) {
    $hiScoreNum.text(score);
  }
}

async function endGame(intervalId) {
  // Stop the interval from counting
  clearInterval(intervalId);
  // Send a axios request to the server with the score
  let response = await axios.get("/end", { params: { score: score } });
  message("Game Over!");
  updatePlayed(response.data.result);
  updateHiScore();
  showReset();
}

function showReset() {
  $resetDiv.show();
}

async function reset() {
  $resetDiv.hide();
  $form.show();
  score = 0;
  timer = 60;
  $boggle.html("");
  let response = await axios.get("/reset");
  message("");
  resetBoard(response.data.board);
  keepTime();
}

function resetBoard(board) {
  $table = $("<table><table/>");
  for (let row of board) {
    console.log(row);
    $row = $("<tr></tr>");
    $table.append($row);
    for (let cell of row) {
      $cell = $("<td></td>");
      $cell.text(cell);
      $row.append($cell);
    }
  }
  $boggle.append($table);
}

$form.on("submit", getWord);
$reset.on("click", reset);
keepTime();
