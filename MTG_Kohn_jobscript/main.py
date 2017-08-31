#!/usr/bin/python
import argparse

class Kohn(object):
    def __init__(self, outfile):
        self.outfile = outfile


    def node_info(self, node_group):
        if node_group == 'shm':
            num_nodes_max = 4
            num_cores_max = 8
            opt_level = 'NOR'
        elif node_group == 'west':
            num_nodes_max = 4
            num_cores_max = 8
            opt_level = 'NOR'
        elif node_group == 'west2':
            num_nodes_max = 4
            num_cores_max = 12
            opt_level = 'NOR'
        elif node_group == 'sandy':
            num_nodes_max = 8
            num_cores_max = 12
            opt_level = 'AVX1'
        elif node_group == 'xeon':
            num_nodes_max = 8
            num_cores_max = 20
            opt_level = 'AVX2'

        return num_nodes_max, num_cores_max, opt_level



def main():
    description = """description here
"""
    descvasp = """
    """
    descqe = """
    """
    descbt = """
    """
    descaims = """
    """

    # Main parser
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)

    # Subparsers
    subparsers = parser.add_subparsers(title="Functions")

    # VASP parsers
    parser_vasp = subparsers.add_parser("vasp", formatter_class=argparse.RawTextHelpFormatter, description=descvasp)
    parser_vasp.set_defaults(func=executevasp)

    parser_qe = subparsers.add_parser("qe", formatter_class=argparse.RawTextHelpFormatter, description=descqe)
    parser_qe.set_defaults(func=executeqe)

    parser_bt = subparsers.add_parser("bt", formatter_class=argparse.RawTextHelpFormatter, description=descbt)
    parser_bt.set_defaults(func=executebt)

    parser_aims = subparsers.add_parser("aims", formatter_class=argparse.RawTextHelpFormatter, description=descaims)
    parser_aims.set_defaults(func=executeaims)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
