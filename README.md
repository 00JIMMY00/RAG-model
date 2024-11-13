#mini-rag

This is minimal implementation of the RAG model for question answering.

##Requirements 

-Python 3.8 or later 

### Install python using Anaconda 
- create your env
###activate your enviroment

###setup you command line for better readability 

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

###Installation

###Install the required packages 

```bash
$ pip install -r requirements.txt

```

### Setup the enviroment variables

```bash
$ cp .env.example .env
```

Set your enviroments variables in the `.env` file. Like 'OPENAI_API_KEY` value .

### Run the fastApi server 
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```


### so you don't need to reload your server on every edit 

```bash
$ uvicorn main:app --reload
```