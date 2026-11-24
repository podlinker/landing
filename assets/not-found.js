(() => {
  const supported = ['ca', 'es', 'en'];
  const requested = location.pathname.split('/').find(part => supported.includes(part));
  let saved;
  try { saved = localStorage.getItem('podlinker-language'); } catch (_) { /* storage is optional */ }
  const browser = navigator.language.slice(0, 2).toLowerCase();
  const language = [requested, saved, browser].find(part => supported.includes(part)) || 'ca';
  document.documentElement.lang = language;
  document.querySelectorAll('[data-error-language]').forEach(section => { section.hidden = section.lang !== language; });
  document.title = document.querySelector('[data-error-language]:not([hidden]) h1').textContent + ' · Podlinker';
})();
