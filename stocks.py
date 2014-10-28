"""
A command line utility for stock performance analysis.

Normal Usage:
stocks.py -f <csv_filename>

Optional args:
-c <company name>

stocks.py -f <csv_filename> -c <company name>
"""
import csv
import sys
import os
from optparse import OptionParser

__author__ = "hbansal"
__version__ = "0.1.1"


class Stocks(object):

    def __init__(self, fname, compname="all"):
        if not os.path.exists(fname):
            raise Exception("File %s not found on the given path" % fname)
        self.fname = fname
        self.compname = compname

    def parse_data(self, fname):
        """
        """
        # perf_matrix format = {"comp_name1": [], "comp_name2":[].........}
        perf_matrix = {}

        try:
            csv_data = csv.reader(open(fname))
            headers = next(csv_data)
            for header_text in headers[2:]:
                perf_matrix.update({header_text: []})

            for row in csv_data:
                index = row.index(max(row[2:]))
                perf_matrix[headers[index]].append((row[0], row[1]))
        except Exception as eee:
            raise Exception("Unable to parse csv data\n. Error %s" % eee)
        return headers, perf_matrix

    def print_stocks_info(self, headers, perf_data, comp_name="all"):
        """"""
        print "%s" % "-" * 80
        print "%s" % "-" * 80
        if comp_name.lower() != "all":
            print "%40s" % comp_name
            print "%s" % "-" * 80
            print "%s" % "-" * 80
            print "%-40s%s" % headers[:2]
            print "%s" % "-" * 80
        else:
            for comp_name, result in perf_data.items():
                print "%40s" % comp_name
                print "%s" % "-" * 80
                print "%s" % "-" * 80
                print "%-40s%s" % ("Year", "Month")
                print "%s" % "-" * 80
                for dat in result:
                    print "%-40s%s" % (dat[0], dat[1])
                print "%s" % "-" * 80
                print "%s" % "-" * 80

    def compute_stock_perf(self):
        """
        """
        headers, perf_results = self.parse_data(self.fname)
        self.print_stocks_info(headers, perf_results, self.compname)


if __name__ == "__main__":
    # parse the command line arguments
    parser = OptionParser("usage: stocks % [options] ")

    parser.add_option("-f", "--filename",
                      dest="filename",
                      help="name of csv file having stocks data")
    help_str = """Optional argument for choosing company name.

                  If this arguement is not provided than utility will print
                  stock information for all the companies mentioned in the
                  csv file.
                """
    parser.add_option("-c", "--compname",
                      dest="compname",
                      default="all",
                      help=help_str)
    (options, args) = parser.parse_args()
    #
    # Copy argument values from the command line
    # to local variables
    #
    filename = options.filename
    compname = options.compname

    if filename is None:
        print "Please provide csv filename in the argument. \
              Use -h options for more details."
        parser.print_help()
        sys.exit(1)

    obj_stocks = Stocks(filename, compname)
    obj_stocks.compute_stock_perf()
