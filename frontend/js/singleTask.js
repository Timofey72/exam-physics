const toggleAnswerButton = document.querySelector('.toggle-answer');
const fullAnswer = document.querySelector('.full-answer');

toggleAnswerButton.addEventListener('click', () => {
  if (fullAnswer.classList.contains('active')) {
    toggleAnswerButton.textContent = 'Показать ответ'
    fullAnswer.classList.remove('active')
  } else {
    toggleAnswerButton.textContent = 'Скрыть ответ'
    fullAnswer.classList.add('active')
  }
})