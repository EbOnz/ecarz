# Set up

For Windows
- cd be
- python -m venv .venv
- .venv\Scripts\activate
- python -m pip install --upgrade pip
- pip install -r requirements\dev.txt
- python src\main.py

## Structure folder reference
https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#dependencies

## Template
- client # client model for external service communication
- config
- constants
- dependencies
- exceptions
- models # db models
- router
- schemas # pydantic models
- services 
- utils