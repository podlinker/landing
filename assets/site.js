(() => {
  const current = document.documentElement.lang;
  document.querySelectorAll('[data-lang]').forEach(link => {
    link.addEventListener('click', () => {
      try { localStorage.setItem('podlinker-language', link.dataset.lang); } catch (_) { /* storage is optional */ }
    });
  });
  try { if (!localStorage.getItem('podlinker-language')) localStorage.setItem('podlinker-language', current); } catch (_) { /* storage is optional */ }
})();
