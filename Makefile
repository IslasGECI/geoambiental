.PHONY: clean mutation

clean:
	sudo rm --recursive $$(find . -name "__pycache__")

mutation:
	mutmut run --paths-to-mutate geoambiental