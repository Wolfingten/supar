from supar import Parser

parser = Parser.load("con-crf-xlmr")

parser.predict("/data/users/jguertler/datasets/tut/NEWS-22nov2010.txt")
