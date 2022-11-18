
### Steps to setup the service
1. Install dependencies `pip install -r requirements.txt` Note: All dependencies are installed with python 3.9
2. Run `make run_server or python main.py --initdb 1` to start the cli
3. If the input needs to be taken from file, "specifiy" `INPUT_FILE_PATH=path/to/input.txt` in `.env` or in terminal
4. If the input needs to be from terminal  "specifiy" `INPUT_FILE_PATH=`  as empty.


### Testing

Run `make test` to run all the unit test cases.