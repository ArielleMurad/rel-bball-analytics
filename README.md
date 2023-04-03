# rel-bball-analytics
This is a Python/Flask app built to view and analyze NBA player statistics. The data is obtained through https://api-sports.io/ via API requests. 
The long term goal for this application is to train ML models to serve predictions on future player and team performance. 
These insights would help fantasy basketball enthusiasts make informed decisions in their fantasy leagues.

## Running the Application
Poetry is used to manage package dependencies. You can learn more about poetry [here](https://python-poetry.org/docs/), including how to install it on your machine.
1. Activate the virtual environment: `poetry shell` 
2. Install package dependencies: `poetry install`
3. Configure environment variables: `cp .env.example .env`
4. Run database migrations: `flask db upgrade`
5. Run the flask application: `poetry run flask run`

## Demo
https://user-images.githubusercontent.com/43834783/229386518-664f2b66-792b-4929-89d6-dba8d4d8d435.mov
