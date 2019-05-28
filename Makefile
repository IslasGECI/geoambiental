nombreRepositorio := $(notdir $(CURDIR))
pruebasModulo := $(basename $(notdir $(wildcard $(nombreRepositorio)/tests/test_*.py)))

tests:
	docker build -t $(nombreRepositorio) .
	docker run -it $(nombreRepositorio) bash -c "pip install . && $(foreach script, $(pruebasModulo), python -m $(nombreRepositorio).tests.$(script) -v; )"
