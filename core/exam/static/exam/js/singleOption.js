const answers = document.querySelectorAll('.check-answer');

answers.forEach(answerElem => {
  const toggleAnswerButton = answerElem.querySelector('.toggle-answer');
  const fullAnswer = answerElem.querySelector('.full-answer');

  toggleAnswerButton.addEventListener('click', () => {
    if (fullAnswer.classList.contains('active')) {
      toggleAnswerButton.textContent = 'Показать ответ'
      fullAnswer.classList.remove('active')
    } else {
      toggleAnswerButton.textContent = 'Скрыть ответ'
      fullAnswer.classList.add('active')
    }
  })
})
