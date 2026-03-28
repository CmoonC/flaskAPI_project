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