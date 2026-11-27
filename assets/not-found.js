(() => {
  const supported = ['ca', 'es', 'en'];
  const brand = document.querySelector('.site-header .brand');
  const basePath = new URL(brand.href).pathname;
  const requested = location.pathname.slice(basePath.length).split('/')[0];
  let saved;
  try { saved = localStorage.getItem('podlinker-language'); } catch (_) { /* storage is optional */ }
  const browser = (navigator.language || '').slice(0, 2).toLowerCase();
  const language = [requested, saved, browser].find(part => supported.includes(part)) || 'ca';
  const recovery = document.querySelector(`[data-error-language][lang="${language}"]`);
  document.documentElement.lang = language;
  document.querySelector('[data-error-fallback]').hidden = true;
  recovery.hidden = false;
  brand.href = recovery.querySelector('a').href;
  document.title = recovery.querySelector('h1').textContent + ' · Podlinker';
})();
