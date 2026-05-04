const hamburger = document.getElementById('hamburger');
const sidebar   = document.getElementById('sidebar');
const overlay   = document.getElementById('sidebar-overlay');

function openSidebar() {
  sidebar.classList.add('open');
  overlay.classList.add('show');
  hamburger.classList.add('open');
}
function closeSidebar() {
  sidebar.classList.remove('open');
  overlay.classList.remove('show');
  hamburger.classList.remove('open');
}

hamburger.addEventListener('click', () => sidebar.classList.contains('open') ? closeSidebar() : openSidebar());
overlay.addEventListener('click', closeSidebar);

document.querySelectorAll('.page-btn:not(.disabled)').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.page-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

document.getElementById('course-form').addEventListener('submit', (e) => {
  e.preventDefault();
  alert('Curso salvo com sucesso!');
});

document.querySelectorAll('.btn-danger-sm').forEach(btn => {
  btn.addEventListener('click', () => {
    if (confirm('Deseja remover este curso?')) {
      btn.closest('tr').style.opacity = '.3';
      setTimeout(() => btn.closest('tr').remove(), 300);
    }
  });
});
