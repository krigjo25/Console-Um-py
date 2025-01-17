# Word counter
An application that counting number of selected word ums.

The application was implemented as a CS50P assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [CS50P's Problem set 7 : Um..Umm..](https://cs50.harvard.edu/python/2022/psets/7/um/)

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/Console-Um-py.git

# Using git bash
git clone https://github.com/krigjo25/Console-Um-py.git

# Using Github Cli
gh repo clone Console-Um-py
```

2. Navigate to the project directory
```sh
cd Console-Um-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

```sh
Usage : type in the terminal python app.py, wait for the prompted message
then type in some names.
python app.py 
```


## Example
```sh
python app.py

Text: <"Um, thanks for the album">
expected output: 1

Text: <"Um, thanks, um..">
expected output: 2

Text: <This is, um... CS50.>
expected output: 1


```
Replace `<This is, um... CS50.">` with the text name

##  Testing framework / Datasets
Pytest was used in this project to ensure that the functions printed out the correct number of "um's"

```sh
pytest test_app.py
pytest -k test_app.py
pytest --html=index.html
```

Through this test there were used some [Datasets](./tests/test_app.py) to verify the functions integerty.

##  Credits

### Responsories
[regex -  Matthew Barnett](https://github.com/mrabarnett/mrab-regex)
[pytest - Holger Krekel ( and many other developers)](https://github.com/pytest-dev/pytest)

## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25
