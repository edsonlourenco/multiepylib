clean:
	python3 setup.py clean --all
	rm -rf dist
	rm -rf *.egg-info

build:
	python3 setup.py bdist_wheel

verify:
	pycodestyle ./multiepy/