# FastAPI CV Project

A modern backend application built with FastAPI, designed with modular architecture and best practices.

## Getting Started

### Prerequisites
*Python 3.10+
*Virtual Environment (venv)

### Installation 
1. **Clone the repository**
    ```bash
      git clone <https://github.com/CmoonC/flaskAPI_project.git>
    ```
2. **Setup Environment**
    ```bash
    cp .env.sample .env
    #Update .env with your secrets
    ``` 
   
3. **Install Dependencies** 
   ```bash
   pip install -r requirements.txt
    ```

4. **Running the App**
Start the development with auto-reload:
    ```bash
    uvicorn app.main:app --reload
    ```
5. **Testing** 
To execute the test suite, run: 
    ```bash
    pytest
   ```

## Running with Docker 
If you have Docker installed, you can run the application withut setting up a local Python environment.

1. **Build the image** 
    ```bash
   docker build -t fastapi-cv-app .
   ```
2. ** Run the container**
    ```bash
   docker run -p 8000:8000 fastapi-cv-app
   ```
The API will be available at http://localhost:8000/

## Database management 

This project uses **PostgreSQL** for persistent data and **Redis** for cashing. 

### How to access the databases:
-**Postgres**: Accessible  on 'localhost:5432' from your host machine.
-**Redis**: Accessible on 'localhost:6379'.

### Useful commands:
- `docker-compose up --build`: Starts all services and builds images.
- `docker-compose down`: Stops and removes all containers. 
- `docker-compose down -v`: Stops containers **and deletes the database data** (use with caution!)

### Data Models 
- Located in 'app/models/'
- Every time you change a model, you must create a migration

### Database Migrations (Alembic)
To apply the current database schema:
```bash
alembic upgrade head
```
To create a new migration after changing a model:
```bash
alembic revision --autogenerate -m "describe your changes"
```

##Logging 
Application logs are visible in the Docker console. Configuration is hadnled in app/utils/logging.py.
I used the lifeshpan event handler to log app startup and shutdown.
