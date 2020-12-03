mutants: install
	mutmut run --paths-to-mutate geoambiental

.PHONY: \
    clean \
	coverage \
    install \
    lint \
	format \
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

format:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests

tests:
	pytest --verbose

lint:
	pylint geoambiental
