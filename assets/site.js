(() => {
  const header = document.querySelector('.site-header');
  if (header && 'ResizeObserver' in window) {
    new ResizeObserver(() => {
      const offset = Math.ceil(header.getBoundingClientRect().height) + 12;
      document.documentElement.style.setProperty('--header-offset', offset + 'px');
    }).observe(header);
  }

  const current = document.documentElement.lang;
  document.querySelectorAll('[data-lang]').forEach(link => {
    link.addEventListener('click', () => {
      try { localStorage.setItem('podlinker-language', link.dataset.lang); } catch (_) { /* storage is optional */ }
    });
  });
  try { if (!localStorage.getItem('podlinker-language')) localStorage.setItem('podlinker-language', current); } catch (_) { /* storage is optional */ }
})();
