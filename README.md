## card-application

### To run this project locally, follow the steps below:

git clone https://github.com/seymaozler/card-application.git

### Create a virtual environment

python -m venv venv

### Activate virtual environment

venv\Scripts\activate

### Create a .env file based on .env.example and configure your environment variables:

copy env.example .env

### Build the Docker containers:

docker-compose build

### Start the Docker containers:

docker-compose up -d

If you encounter an error at this step, you should run the command "docker start cardapp" because 
MySQL is started with a delay, which can sometimes result in a connection error with FastAPI. 
Running this command will resolve the issue:

docker start cardapp

### And again;
docker-compose up -d

The API documentation is available at http://localhost:8000/docs

# Endpoints
## Create User
![create-user](https://github.com/seymaozler/card-application/assets/63790943/eaff879e-29ea-4f75-88f3-6b4e0101d699)

## Login User
![login-user](https://github.com/seymaozler/card-application/assets/63790943/c5426995-2fc7-4ae3-8051-df65b3e768ce)

## Create Card
![create-card](https://github.com/seymaozler/card-application/assets/63790943/4e8ed78a-d70d-477a-84cc-e9750c36be29)

## List Cards
![list-cards](https://github.com/seymaozler/card-application/assets/63790943/f7fe6e1d-b5bb-4d67-a9cf-0b6f9880339b)

## Update Card
![update-card](https://github.com/seymaozler/card-application/assets/63790943/12cf1bfb-1b24-42f7-a11d-38f59000f7e0)

## Delete Card
![delete-card](https://github.com/seymaozler/card-application/assets/63790943/c5ddb9b7-c86e-4b6d-aae0-92ff6ba9f7ec)



