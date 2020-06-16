mutants: install
	mutmut run --paths-to-mutate geoambiental

.PHONY: \
    clean \
    install \
    lint \
    mutation \
    tests \

clean:
	rm --force --recursive .mutmut-cache
	rm --force --recursive .pytest_cache
	rm --force --recursive $$(find . -name '__pycache__')

install:
	pip install --editable .

tests:
	pytest --cov=geoambiental --cov-report=term --verbose

lint:
	pylint geoambiental
