document.querySelectorAll('select.language').forEach(select => {
  select.addEventListener('change', () => {
    const target = new URL(select.value, window.location.origin);
    if (target.origin === window.location.origin) window.location.assign(target.href);
  });
});
