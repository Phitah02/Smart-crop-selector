// Handle form submission and API call
const form = document.getElementById('cropForm');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    resultsDiv.textContent = 'Loading...';
    const soil_type = document.getElementById('soil_type').value;
    const rainfall_level = document.getElementById('rainfall_level').value;
    const region = document.getElementById('region').value;

    // Basic validation
    if (!soil_type || !rainfall_level || !region) {
        resultsDiv.textContent = 'Please fill all fields.';
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ soil_type, rainfall_level, region })
        });
        const data = await response.json();
        if (data.crops) {
            resultsDiv.innerHTML = '<b>Recommended Crops:</b><ul>' +
                data.crops.map(crop => `<li>${crop}</li>`).join('') + '</ul>';
        } else if (data.error) {
            resultsDiv.textContent = 'Error: ' + data.error;
        } else {
            resultsDiv.textContent = 'No recommendations found.';
        }
    } catch (err) {
        resultsDiv.textContent = 'Server error. Please try again.';
    }
});

// Premium payment integration
const payBtn = document.getElementById('payPremiumBtn');
const paymentStatus = document.getElementById('paymentStatus');

if (payBtn) {
    payBtn.addEventListener('click', async () => {
        const email = document.getElementById('premiumEmail').value;
        paymentStatus.textContent = '';
        if (!email) {
            paymentStatus.textContent = 'Please enter your email.';
            return;
        }
        payBtn.disabled = true;
        paymentStatus.textContent = 'Processing payment...';
        try {
            const response = await fetch('http://localhost:5000/pay', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, amount: 5 })
            });
            const data = await response.json();
            if (data.url) {
                paymentStatus.innerHTML = `<a href="${data.url}" target="_blank">Click here to complete payment</a>`;
            } else if (data.error) {
                paymentStatus.textContent = 'Payment error: ' + data.error;
            } else {
                paymentStatus.textContent = 'Unexpected error.';
            }
        } catch (err) {
            paymentStatus.textContent = 'Server error. Please try again.';
        }
        payBtn.disabled = false;
    });
}
