VERSION=$(shell python3 -c "import dmsh; print(dmsh.__version__)")

default:
	@echo "\"make publish\"?"

# https://packaging.python.org/distributing/#id72
upload: setup.py
	# Make sure we're on the master branch
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then exit 1; fi
	rm -f dist/*
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal
	twine upload dist/*

tag:
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then exit 1; fi
	@echo "Tagging v$(VERSION)..."
	git tag v$(VERSION)
	git push --tags

publish: tag upload

clean:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
	@rm -rf *.egg-info/ build/ dist/ MANIFEST .pytest_cache/

format:
	isort -rc .
	black .

black:
	black .

lint:
	black --check setup.py dmsh/ test/*.py
	flake8 setup.py dmsh/ test/*.py
