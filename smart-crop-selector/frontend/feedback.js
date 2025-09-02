// Feedback form submission
document.getElementById('feedbackForm').onsubmit = async (e) => {
    e.preventDefault();
    const name = document.getElementById('fbName').value;
    const email = document.getElementById('fbEmail').value;
    const comment = document.getElementById('fbComment').value;
    const res = await fetch('http://127.0.0.1:5000/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, comment })
    });
    const data = await res.json();
    document.getElementById('feedbackMsg').textContent = data.message || data.error;
    if (res.ok) {
        document.getElementById('feedbackForm').reset();
    }
};