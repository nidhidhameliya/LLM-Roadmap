install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	ruff check .
	black .
