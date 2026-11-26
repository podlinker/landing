(() => {
  const header = document.querySelector('.site-header');
  if (header && 'ResizeObserver' in window) {
    new ResizeObserver(() => {
      const offset = Math.ceil(header.getBoundingClientRect().height) + 12;
      document.documentElement.style.setProperty('--header-offset', offset + 'px');
    }).observe(header);
  }

  const current = document.documentElement.lang;
  const languages = [...document.querySelectorAll('[data-lang]')];
  const sections = [...document.querySelectorAll('main section[id]')].reverse();
  const destinations = languages.map(link => new URL(link.href));
  let frame = 0;

  function setSection(id) {
    languages.forEach((link, index) => {
      const destination = destinations[index];
      destination.hash = id;
      if (link.href !== destination.href) link.href = destination.href;
    });
  }

  function updateSection() {
    frame = 0;
    const readingLine = (header?.getBoundingClientRect().bottom ?? 0) + 32;
    const scroller = document.scrollingElement;
    const atEnd = scroller.scrollTop > 0 &&
      scroller.scrollHeight - scroller.scrollTop <= scroller.clientHeight + 2;
    const section = atEnd
      ? sections[0]
      : sections.find(item => item.getBoundingClientRect().top <= readingLine);
    setSection(section?.id ?? '');
  }

  function scheduleUpdate() {
    if (!frame) frame = requestAnimationFrame(updateSection);
  }

  setSection(sections.find(section => '#' + section.id === location.hash)?.id ?? '');
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate);
  window.addEventListener('pageshow', scheduleUpdate);

  languages.forEach(link => {
    link.addEventListener('click', () => {
      try { localStorage.setItem('podlinker-language', link.dataset.lang); } catch (_) { /* storage is optional */ }
    });
  });
  try { if (!localStorage.getItem('podlinker-language')) localStorage.setItem('podlinker-language', current); } catch (_) { /* storage is optional */ }
})();
