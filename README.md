stocks_exercise
===============
A command line utility for stock performance analysis.

Usage
------
For printing highest stock price month for all the companies mentioned in the csv data file.
```bash
python stocks.py -f <csv_filename>
```

For printing highest stock price month for a particular company
```bash
python stocks.py -f <csv_filename> -c <company_name>
```

Unit test execution
```bash
python test_stocks.py
```

File Structure
--------------
1. stocks_exercise
	* stocks.py -- Command line utility script
	* test_stocks.py -  utility unit tests
	* test_shares_data.csv -  sample test data for stocks.py
	* test_parse_data.csv	- sample test data for unit test script