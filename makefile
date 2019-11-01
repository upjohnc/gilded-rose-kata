test:
	PYTHONPATH=. pytest -v

isort:
	isort -rc . .isort.cfg

mypy:
	mypy --ignore-missing-imports python
