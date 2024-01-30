const answersElements = document.querySelectorAll('.answer');

answersElements.forEach(answer => {
  answer.querySelector('.answer-button').addEventListener('click', (e) => {
    const answerInput = answer.querySelector('.answer-input')
    const userAnswer = answerInput.value;
    const correctAnswer = answer.parentElement.querySelector('.full-answer').textContent;
    
    if (userAnswer == correctAnswer) {
      answerInput.classList.remove('answer-uncorrect');
      answerInput.classList.add('answer-correct');
    } else {
      answerInput.classList.remove('answer-correct');
      answerInput.classList.add('answer-uncorrect');
    }
  })
})