pep8_test:
	pycodestyle tests/*.py

pep8_model:
	pycodestyle models/*.py

pep8_rec:
	pycodestyle models/rectangle.py

pep8_squ:
	pycodestyle models/square.py

pep8_bas:
	pycodestyle models/base.py

test_all:
	python3 -m unittest discover tests

test_base:
	python3 -m unittest tests/test_models/test_base.py

test_rectangle:
	python3 -m unittest tests/test_models/test_rectangle.py

test_square:
	python3 -m unittest tests/test_models/test_square.py