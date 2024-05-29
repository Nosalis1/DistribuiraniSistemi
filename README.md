# Distribuirani Sistemi

## Server App

### Integration

1. Create root dir
   ```batch
   mkdir server_app
   cd server_app
   ```
2. Check ExecutionPolicy
   ```shell
   Set-ExecutionPolicy RemoteSigned
   ```
3. Create virtual environment
   ```batch
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. Install Flask
   ```batch
   python -m pip install Flask
   ```

### Architecture

1. Setup project
   ```
    ├── server_app/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── views.py
    │   │   ├── services.py
    │   │   ├── schemas.py
    │   │   ├── config.py
    │   │   ├── utils.py
    │   │   ├── extensions.py
    │   ├── migrations/
    │   ├── tests/
    │   ├── venv/...
    │   ├── .env
    │   ├── .flaskenv
    │   ├── requirements.txt
    │   ├── run.py
   ```
2. Install Requirements
    - `requirements.txt`
        ```
        Flask
        Flask-SQLAlchemy
        Flask-Migrate
        Flask-Marshmallow
        marshmallow-sqlalchemy
        python-dotenv
        Flask-JWT-Extended
        Flask-Bcrypt
        ```
    - Install
        ```batch
        pip install -r requirements.txt
        ```

## Client App

### Integration

1. Create React App
   ```batch
   npx create-react-app client_app
   cd client_app
   ```
2. Install Dependencies
   ```batch
   npm install react-router-dom
   ```

### Architecture

1. Cleanup template
   - [Cleanup tutorial](https://www.youtube.com/watch?v=PAqbIbdvTuU)
2. Setup project
   ```
├── client_app/
│   ├── node_modules/ ...
│   ├── public/
│   │   ├── index.html
│   ├── src/
│   │   ├── components/...
│   │   ├── pages/...
│   │   ├── services/...
│   │   ├── utils/...
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── routes.js
│   ├── .gitignore
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
   ```