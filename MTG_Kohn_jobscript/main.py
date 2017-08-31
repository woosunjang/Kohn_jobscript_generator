#!/usr/bin/python
import argparse



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
