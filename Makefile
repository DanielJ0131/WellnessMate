#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python3 # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

# To make targets in each directory under the src/
define FOREACH
    for DIR in app/*; do \
        $(MAKE) -C $$DIR $(1); \
    done
endef

# Define the subdirectories
SUBDIRS := $(wildcard app/*)

all:



# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

# ---------------------------------------------------------
# Run the app.
#
run: 
	$(PYTHON) app/main.py


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-src:
	$(call FOREACH,clean)

clean-all: clean clean-doc clean-src
	rm -rf .venv


# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	-pylint app/*.py app/src/*.py app/ui/*.py


flake8:
	@$(call MESSAGE,$@)
	-flake8 app/*.py app/src/*.py app/ui/*.py

lint: flake8 pylint



# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black .

codestyle: black


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest discover

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage html
	coverage report -m

test: lint coverage


# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	# This does not work on Windows installed Python
	$(PYTHON) -m pydoc -w "$(PWD)"
	install -d doc/pydoc
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/pdoc *.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse app/*.py app/src/*.py app/ui/*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc sphinx



# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average .

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show targets app/*.py app/src/*.py app/ui/*.py

radon-raw:
	@$(call MESSAGE,$@)
	radon raw .

radon-hal:
	@$(call MESSAGE,$@)
	radon hal .

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory .

metrics: radon-cc radon-mi radon-raw radon-hal cohesion



# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive targets app/*.py app/src/*.py app/ui/*.py
