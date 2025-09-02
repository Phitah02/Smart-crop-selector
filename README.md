
# Smart Crop Selector

## Overview
Smart Crop Selector is a web application designed to help farmers select the best crops to plant based on various factors. It features a Flask backend API and a frontend interface for user interaction.

## Features
- Crop recommendation based on user input
- Submission and history tracking of user data
- Payment integration for premium features (currently using IntaSend)
- User authentication and feedback system

## Deployment

### Backend
- The backend is built with Flask and uses SQLAlchemy for database interactions.
- To deploy the backend, ensure you have the following files:
  - `requirements.txt` listing all dependencies
  - `Procfile` for specifying the app startup command
  - `.gitignore` to exclude sensitive files like `.env`
- Recommended deployment platforms: Heroku, Render, AWS Elastic Beanstalk
- Set environment variables for database URI and secret keys on the hosting platform.

### Frontend
- The frontend is a static site served separately.
- Can be deployed on platforms like Vercel, Netlify, or any static hosting service.
- Update frontend API URLs to point to the deployed backend.

## Running Locally
1. Create and activate a Python virtual environment.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set environment variables in a `.env` file (do not commit this file):
   ```
   SECRET_KEY=your_secret_key
   MYSQL_URI=your_database_uri
   OPENAI_API_KEY=your_openai_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```
4. Run the backend:
   ```
   python -m backend.app
   ```
5. Open the frontend by opening `frontend/index.html` in a browser or serve it with a static server.

## Testing
- Backend endpoints:
  - `/submit`
  - `/recommend`
  - `/history`
  - `/pay`
  - `/feedback`
- Frontend forms and UI flows including feedback submission and premium payment.

## Notes
- The payment integration with IntaSend currently returns a 404 error due to an invalid API endpoint. This needs to be fixed by updating the IntaSend API URL or credentials.
- Ensure secrets are never committed to the repository. Use `.gitignore` and environment variables.

## Contribution
Feel free to fork the repository and submit pull requests.

## License
MIT License
