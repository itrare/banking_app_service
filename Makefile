
#####################################################################################
############################     Banking Server : API     ###########################
############################ Author: Abhishek Kumar Gupta ###########################
############################ Date Created: 16 Nov 2022    ###########################
#####################################################################################


format:
	set -e
	isort --force-single-line-imports app tests
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables  --in-place app tests --exclude __init__.py
	black app tests
	isort app tests

test:
	set -e
	set -x
	pytest -p no:warnings ./tests/*

test_with_coverage:
	set -e
	set -x
	coverage run -m pytest -p no:warnings ./tests/*

run_server:
	python main.py --initdb 1
