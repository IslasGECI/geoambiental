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

module = geoambiental
codecov_token = 6c56bccb-1758-4ed9-8161-97c845591c26

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive .mutmut-cache
	rm --force --recursive .pytest_cache
	rm --force --recursive $$(find . -name '__pycache__')

coverage: install
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}


install:
	pip install --editable .

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

tests:
	pytest --verbose

linter:
	$(call lint, ${module})
	$(call lint, tests)
