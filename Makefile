.PHONY: docs
docs:
	(cd docs; make html)

.PHONY: test
test:
	@tox -e py27,py37,py38

.PHONY: lint
lint:
	@tox -e lint

.PHONY: fmt
fmt:
	@tox -e fmt
