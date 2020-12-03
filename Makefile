mutants: install
	mutmut run --paths-to-mutate geoambiental

.PHONY: \
    clean \
	coverage \
    install \
    lint \
    mutation \
    tests \

clean:
	rm --force --recursive .mutmut-cache
	rm --force --recursive .pytest_cache
	rm --force --recursive $$(find . -name '__pycache__')

coverage:
	pytest --cov=geoambiental --cov-report=term --verbose

install:
	pip install --editable .

tests:
	pytest --verbose

lint:
	pylint geoambiental
