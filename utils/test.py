from supar import Parser

parser = Parser.load("con-crf-xlmr")
dataset = parser.predict(
    "Bruciata la sede del partito democratico mentre i reparti antisommossa si sono ritirati dalla citta ' .",
    lang="it",
)

print(dataset[0])
