document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('fade-in');
  document.querySelectorAll('a').forEach(link => {
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#') || link.target === '_blank') return;
    link.addEventListener('click', e => {
      e.preventDefault();
      document.body.classList.remove('fade-in');
      document.body.classList.add('fade-out');
      setTimeout(() => {
        window.location.href = href;
      }, 300);
    });
  });
});

window.addEventListener('pageshow', event => {
  if (event.persisted) {
    document.body.classList.remove('fade-out');
    document.body.classList.add('fade-in');
  }
});
