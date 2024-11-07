from supar import Parser

parser = Parser.load("con-crf-xlmr")

parser.predict(
    "/data/users/jguertler/datasets/tut/NEWS.seg",
    "/data/users/jguertler/datasets/tut/NEWS.pred",
    lang="it",
)
