import argparse


def clean_file(in_file, out_file):
    with open(in_file, "r") as f:
        text = f.readlines()
    with open(out_file, "w") as f:
        for t in text:
            if not t.startswith("*"):
                f.writelines(t)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="remove non-trees from file")
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    clean_file(
        args.input_file,
        args.output_file,
    )
