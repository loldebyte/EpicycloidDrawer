val := $(shell readlink -f .)

.PHONY: test make

default: test

test : ; PYTHONPATH=$(PYTHONPATH):$(val) \
	pytest --html=tests/report.html --mpl