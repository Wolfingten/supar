import argparse

from stanza.models.constituency import tree_reader, parse_tree


def flatten_trees(in_file, out_file):
    flat_trees = tree_reader.read_tree_file(in_file)
    flat_trees = [t.children[0] for t in flat_trees]
    parse_tree.Tree.write_treebank(flat_trees, out_file)


########################################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert indented trees to linearized ones."
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    flatten_trees(
        args.input_file,
        args.output_file,
    )
