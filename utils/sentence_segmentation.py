import argparse

import stanza


def segment_setnences(in_file, out_file):
    nlp = stanza.Pipeline(lang="it", processors="tokenize")
    with open(in_file, "r") as f:
        doc = nlp(f.read())
    with open(out_file, "w") as f:
        for s in doc.sentences:
            line = " ".join([token.text for token in s.tokens])
            if not line.startswith("FILE-LABEL"):
                f.write(line + "\n")


########################################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="segment sentences to one per line")
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    segment_setnences(
        args.input_file,
        args.output_file,
    )
