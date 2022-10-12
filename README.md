# Тестовое задание

## Installation:
* With Docker
* Default

### With Docker:
Mount to the directory:
```
$ cd ./test_tasks
```

Build the project:
```
$ docker-compose build
```

Start the project
```
$ docker-compose up
```

### Default:
Mount to the directory:
```
$ cd ./test_tasks
```

Create and activate virtualenv:
```
$ python3 -m virtualenv venv
$ source venv/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```

Run the script:
```
python test_tasks.py
```

### Environmental variables:

Save them in .env file in the following format:
```
MONGO_INITDB_ROOT_USERNAME=
MONGO_INITDB_ROOT_PASSWORD=
```