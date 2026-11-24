(() => {
  const current = document.documentElement.lang;
  const languages = [...document.querySelectorAll('[data-lang]')];
  const sections = [...document.querySelectorAll('main section[id]')];
  const header = document.querySelector('.site-header');
  let frame = 0;

  function setDestination(hash) {
    languages.forEach(link => { link.href = new URL(link.dataset.home + hash, location.href); });
  }
  function updateDestination() {
    frame = 0;
    const readingLine = header.getBoundingClientRect().bottom + 32;
    const section = sections.findLast(item => item.getBoundingClientRect().top <= readingLine);
    setDestination(section ? '#' + section.id : '');
  }

  languages.forEach(link => {
    link.dataset.home = link.getAttribute('href');
    link.addEventListener('click', () => {
      try { localStorage.setItem('podlinker-language', link.dataset.lang); } catch (_) { /* storage is optional */ }
    });
  });
  setDestination(sections.some(section => '#' + section.id === location.hash) ? location.hash : '');
  window.addEventListener('scroll', () => {
    if (!frame) frame = window.requestAnimationFrame(updateDestination);
  }, { passive: true });
  window.addEventListener('resize', updateDestination);
  try { if (!localStorage.getItem('podlinker-language')) localStorage.setItem('podlinker-language', current); } catch (_) { /* storage is optional */ }
})();
