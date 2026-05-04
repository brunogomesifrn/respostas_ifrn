document.getElementById('contact-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const successMsg = document.getElementById('success-msg');
  successMsg.classList.add('show');
  e.target.reset();
  setTimeout(() => successMsg.classList.remove('show'), 5000);
});

document.getElementById('celular').addEventListener('input', (e) => {
  let v = e.target.value.replace(/\D/g, '');
  if (v.length <= 11) {
    v = v.replace(/^(\d{2})(\d)/, '($1) $2');
    v = v.replace(/(\d{5})(\d)/, '$1-$2');
  }
  e.target.value = v;
});
