#!/usr/bin/python
#Author: Kuziwa Sachikonye
#Date: 28 May 2017 06h44
#Description: Little calculator to help me learn about the poisson distibution.

import math

#parameters
from argparse import ArgumentParser

parser = ArgumentParser(description="Bitcoint_Calculator")

parser.add_argument('--currency','-c',
                    dest="currency",
                    help="Currency",
                    default="BTC")

parser.add_argument('-i',
                    dest="rate_in",
                    type=int,
                    help="The rate the the currency was purchased")

parser.add_argument('-o',
                    dest="rate_out",
                    type=int,
                    help="The rate the the currency was sold")

parser.add_argument('-p',
                    dest="investment",
                    type=int,
                    help="The amount of money invested")

# Expt parameters
args = parser.parse_args()

def main():
    #initialisation
    ans = 0
    #obtain parameter (for efficiency?)
    currency = args.currency
    rate_in = args.rate_in
    rate_out = args.rate_out
    investment = args.investment

        #normal calculation (BTC)
    if(currency == "BTC"):
        #calculations
        currency_holdings = float(investment)/float(rate_in)
        revenue = rate_out * currency_holdings
        profit = revenue - investment

        print "Investment: ZAR:"
        print "Profit: ZAR",profit,"\n"

        print "Rate In: ZAR",rate_in
        print "Rate Out: ZAR ",rate_out
        print "Holdings: BTC",currency_holdings
if __name__ == '__main__':
    main()
