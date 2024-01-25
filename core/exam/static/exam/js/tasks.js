const topics = document.querySelectorAll('.topic');

topics.forEach((topic) => {
  const topicTitle = topic.querySelector('.topic-title');
  const topicContent = topic.querySelector('.topic-content');

  topicTitle.addEventListener('click', () => {
    topicContent.classList.toggle('active');
    topicTitle.classList.toggle('arrow-up');
  });
});
