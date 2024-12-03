install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
format:
	black *.py logic/*.py
lint:
	pylint --disable=R,C *.py logic/*.py
test:
	python -m pytest -vv --cov=logic
build:
	docker build -t deploy-fastapi .
run:
	#run docker
	docker run -d -p 8080:8080 deploy-fastapi

deploy:
	#deploy
all: install format lint test build deploy

