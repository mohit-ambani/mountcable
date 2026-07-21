// Mount Cable India — lightweight interactions
document.addEventListener('click', function (e) {
  const links = document.getElementById('navlinks');
  if (links && links.classList.contains('open') && !e.target.closest('#navlinks') && !e.target.closest('.nav-toggle')) {
    links.classList.remove('open');
  }
});
// close mobile menu after clicking a link
document.querySelectorAll('#navlinks a').forEach(a =>
  a.addEventListener('click', () => document.getElementById('navlinks').classList.remove('open'))
);
// close language dropdown on outside click
document.addEventListener('click', function (e) {
  document.querySelectorAll('.lang-menu.open').forEach(function (menu) {
    if (!e.target.closest('.lang-switch')) menu.classList.remove('open');
  });
});
