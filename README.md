# Distribuirani Sistemi

## Server App

1. Create root directory
```batch
mkdir server_app
cd server_app
```

2. Create Virtual Environment
```batch
python -m venv venv
.\venv\Scripts\activate
```
    1. Fix ExecutionPolicy
    ```shell
    Get-ExecutionPolicy
    
    Set-ExecutionPolicy RemoteSigned
    ```

3. Install Flask (in venv)
```batch
python -m pip install Flask
```

## Client App

1. Create react app
```batch
npx create-react-app client_app
```