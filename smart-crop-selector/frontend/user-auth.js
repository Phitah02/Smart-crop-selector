// User Authentication Modal Logic & API Calls
const authModal = document.getElementById('authModal');
const openLoginBtn = document.getElementById('openLoginBtn');
const openRegisterBtn = document.getElementById('openRegisterBtn');
const closeModal = document.getElementById('closeModal');
const loginFormBox = document.getElementById('loginFormBox');
const registerFormBox = document.getElementById('registerFormBox');
const showRegister = document.getElementById('showRegister');
const showLogin = document.getElementById('showLogin');
const authStatus = document.getElementById('authStatus');

openLoginBtn.onclick = () => {
    authModal.style.display = 'block';
    loginFormBox.style.display = 'block';
    registerFormBox.style.display = 'none';
};
openRegisterBtn.onclick = () => {
    authModal.style.display = 'block';
    loginFormBox.style.display = 'none';
    registerFormBox.style.display = 'block';
};
closeModal.onclick = () => { authModal.style.display = 'none'; };
showRegister.onclick = (e) => { e.preventDefault(); loginFormBox.style.display = 'none'; registerFormBox.style.display = 'block'; };
showLogin.onclick = (e) => { e.preventDefault(); loginFormBox.style.display = 'block'; registerFormBox.style.display = 'none'; };
window.onclick = (event) => { if (event.target === authModal) authModal.style.display = 'none'; };

// Login
document.getElementById('loginForm').onsubmit = async (e) => {
    e.preventDefault();
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const res = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    document.getElementById('loginMsg').textContent = data.message || data.error;
    if (res.ok) {
        authStatus.textContent = 'Logged in as ' + username;
        authModal.style.display = 'none';
    }
};
// Register
document.getElementById('registerForm').onsubmit = async (e) => {
    e.preventDefault();
    const username = document.getElementById('registerUsername').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const res = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password })
    });
    const data = await res.json();
    document.getElementById('registerMsg').textContent = data.message || data.error;
    if (res.ok) {
        registerFormBox.style.display = 'none';
        loginFormBox.style.display = 'block';
    }
};