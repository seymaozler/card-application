# card-application

# To run this project locally, follow the steps below:

git clone https://github.com/seymaozler/card-application.git

# Create a virtual environment

python -m venv venv

# Activate virtual environment

venv\Scripts\activate

# Create a .env file based on .env.example and configure your environment variables:

copy env.example .env

# Build the Docker containers:

docker-compose build

# Start the Docker containers:

docker-compose up -d

If you encounter an error at this step, you should run the command "docker start cardapp" because 
MySQL is started with a delay, which can sometimes result in a connection error with FastAPI. 
Running this command will resolve the issue:

docker start cardapp

# And again;
docker-compose up -d

The API documentation is available at http://localhost:8000/docs
