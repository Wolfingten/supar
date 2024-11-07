from supar import Parser

Parser.load("con-crf-xlmr").evaluate(
    "/data/users/jguertler/datasets/tut/NEWS.pred",
    delete={"TOP", "ROOT", "S1", "-NONE-", "VROOT"},
    equal={},
    verbose=False,
)
