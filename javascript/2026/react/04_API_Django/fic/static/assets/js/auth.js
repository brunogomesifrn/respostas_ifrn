const form = document.getElementById('auth-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const successMsg = document.getElementById('success-msg');
    if (successMsg) {
      successMsg.classList.add('show');
      setTimeout(() => successMsg.classList.remove('show'), 5000);
    }
  });
}

// CPF mask
const cpfInput = document.getElementById('cpf');
if (cpfInput) {
  cpfInput.addEventListener('input', (e) => {
    let v = e.target.value.replace(/\D/g, '');
    v = v.replace(/(\d{3})(\d)/, '$1.$2');
    v = v.replace(/(\d{3})(\d)/, '$1.$2');
    v = v.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    e.target.value = v;
  });
}

// Password strength indicator
const pwdInput = document.getElementById('senha');
const pwdBar   = document.getElementById('pwd-bar');
if (pwdInput && pwdBar) {
  pwdInput.addEventListener('input', () => {
    const v = pwdInput.value;
    let strength = 0;
    if (v.length >= 8) strength++;
    if (/[A-Z]/.test(v)) strength++;
    if (/[0-9]/.test(v)) strength++;
    if (/[^A-Za-z0-9]/.test(v)) strength++;
    const colors = ['#ef4444', '#f97316', '#eab308', '#22c55e'];
    const widths  = ['25%', '50%', '75%', '100%'];
    pwdBar.style.width      = strength ? widths[strength - 1] : '0';
    pwdBar.style.background = strength ? colors[strength - 1] : '';
  });
}
