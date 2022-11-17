
#####################################################################################
############################     Banking Server : API     ###########################
############################ Author: Abhishek Kumar Gupta ###########################
############################ Date Created: 16 Nov 2022    ###########################
#####################################################################################


format:
	set -e
	isort --force-single-line-imports app
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables  --in-place app --exclude __init__.py
	black app
	isort app

run_server:
	python main.py --initdb 1
