## This proyect is backend practice to get the AWS Certified

### Steps to get started

create virtual environment
`python -m venv env`

activate virtual env (linux/mac)
`source env/bin/activate`

install dependencies
`pip install -r requirements.txt`

build:
`docker-compose build `

run
`docker-compose up`

### Docker

build docker image:

```
docker build -t fastapi_aws .
```

run docker container locally:

```
docker run -p 8000:8000 -e DATABASE_USER=<user> -e DATABASE_PASSWORD=<password> -e DATABASE_HOST=<host> -e DATABASE_NAME=<database name> fastapi_aws
```

User Data for ec2:

```
sudo yum install git -y
git clone https://github.com/Manuel11713/fastapi-docker-aws.git
cd fastapi-docker-aws/
fastapi-docker-aws]$ pip3 install -r requirements.txt
export DATABASE_USER="..."
export DATABASE_PASSWORD="..."
export DATABASE_HOST="..."
export DATABASE_NAME="..."
export STRIPE_PUBLIC_KEY="..."
pip3 install gunicorn
```
