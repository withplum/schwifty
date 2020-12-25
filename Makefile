.PHONY: docs
docs:
	(cd docs; make html)

.PHONY: test
test:
	@tox -e py27,py37,py38

.PHONY: lint
lint:
	@tox -e lint

.PHONY: lint-docs
lint-docs:
	@tox -e lint-docs

.PHONY: fmt
fmt:
	@tox -e fmt
