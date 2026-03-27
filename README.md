# FastAPI CV Project

A modern backend application built with FastAPI, designed with modular architecture and best practices.

## Getting Started

### Prerequisites
*Python 3.10+
*Virtual Environment (venv)

### Installation 
1. **Clone the repository**
    ''' bash
    git clone <https://github.com/CmoonC/flaskAPI_project.git>
    '''
2. **Setup Environment**
    cp .env.sample .env
    #Update .env with your secrets
3. Install Dependencies 
    pip install -r requirements.txt


Running the App
Start the development with auto-reload:
    uvicorn app.main:app --reload

Testing 
To execute the test suite, run: 
    pytest