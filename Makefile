.PHONY: clean mutation tests

clean:
	rm --recursive $$(find . -name "__pycache__")

mutation:
	mutmut run --paths-to-mutate geoambienta

tests:
	pytest --cov=geoambiental --cov-report=term --verbose