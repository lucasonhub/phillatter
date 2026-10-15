(() => {
  const select = document.querySelector('#topic');
  if (!select) return;
  const papers = [...document.querySelectorAll('.paper')];
  const update = () => {
    for (const paper of papers) {
      paper.hidden = !!select.value && !JSON.parse(paper.dataset.topics).includes(select.value);
    }
    document.querySelector('#result-count').textContent = `${papers.filter(p => !p.hidden).length} publicações`;
  };
  select.addEventListener('change', update);
  update();
})();
