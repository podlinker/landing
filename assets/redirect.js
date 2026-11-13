try {
  const selected = localStorage.getItem('podlinker-language');
  const browser = (navigator.language || '').slice(0, 2).toLowerCase();
  const supported = ['ca', 'es', 'en'];
  const language = supported.includes(selected) ? selected : supported.includes(browser) ? browser : 'ca';
  location.replace(`${language}/`);
} catch (_) {
  location.replace('ca/');
}
