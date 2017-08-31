#!/usr/bin/python
import argparse


# TODO: shm infiniband warning
class Kohn(object):
    def __init__(self, outfile, jobname, nodegroup, numnode, corepernode, walltime, program, version, options):
        self.outfile = outfile
        self.jobname = jobname
        self.nodegroup = nodegroup
        self.numnode = numnode
        self.corepernode = corepernode
        self.wall = walltime
        self.prog = program
        self.ver = version
        self.option = options
        self.optim = ''
        self.bininfo = {}
        self.nodeinfo = {}
        self.setdata()

    def setdata(self):
        # Node informations here
        self.nodeinfo = {'shm': {'maxnode': 4,
                                 'maxcore': 8,
                                 'opt': 'NOR'},
                         'west': {'maxnode': 4,
                                  'maxcore': 8,
                                  'opt': 'NOR'},
                         'west2': {'maxnode': 4,
                                   'maxcore': 12,
                                   'opt': 'NOR'},
                         'sandy': {'maxnode': 8,
                                   'maxcore': 12,
                                   'opt': 'AVX1'},
                         'xeon': {'maxnode': 8,
                                  'maxcore': 20,
                                  'opt': 'AVX2'},
                         }

        # Binary informations here
        vaspdic = {'5.3.5': {'NOR': {'path': '/GRAPE/Apps/VASP/bin/5.3.5/NORMAL/',
                                   'bin': 'vasp.5.3.5_31MAR2014_GRP7_NORMAL',
                                   'options': ['VTST.x', 'VTST_GAMMA.x', 'VTST_NCL.x'],
                                   'suffix': ' > stdout'
                                   },
                           'AVX1': {'path': '/GRAPE/Apps/VASP/bin/5.3.5/AVX1/',
                                    'bin': 'vasp.5.3.5_31MAR2014_GRP7_AVX1',
                                    'options': ['.x', 'GAMMA.x', 'NCL.x', 'VTST.x', 'VTST_GAMMA.x', 'VTST_NCL.x'],
                                    'suffix': ' > stdout'
                                    },
                           'AVX2': {'path': '/GRAPE/Apps/VASP/bin/5.3.5/AVX2/',
                                    'bin': 'vasp.5.3.5_31MAR2014_GRP7_AVX2',
                                    'options': ['VTST.x', 'VTST_GAMMA.x', 'VTST_NCL.x'],
                                    'suffix': ' > stdout'
                                    },
                           },

                   '5.4.1': {'NOR': {'path': '/GRAPE/Apps/VASP/bin/5.4.1/NORMAL/',
                                   'bin': 'vasp_5.4.1_GRP7_NORMAL_p13082016',
                                   'options': ['.x', 'CELL_X_AXIS_RELAX.x', 'CELL_X_AXIS_RELAX_GAMMA.x',
                                               'CELL_X_AXIS_RELAX_NCL.x', 'CELL_Z_AXIS_RELAX.x',
                                               'CELL_Z_AXIS_RELAX_GAMMA.x', 'CELL_Z_AXIS_RELAX_NCL.x',
                                               'GAMMA.x', 'NCL.x', 'VASPSOL.x', 'VASPSOL_GAMMA.x', 'VASPSOL_NCL.x',
                                               'VTST.x', 'VTST_GAMMA.x', 'VTST_NCL.x'],
                                   'suffix': ' > stdout'
                                   },
                           'AVX1': {'path': '/GRAPE/Apps/VASP/bin/5.4.1/AVX1/',
                                    'bin': 'vasp_5.4.1_GRP7_AVX1_p13082016',
                                    'options': ['.x', 'CELL_X_AXIS_RELAX.x', 'CELL_X_AXIS_RELAX_GAMMA.x',
                                               'CELL_X_AXIS_RELAX_NCL.x', 'CELL_Z_AXIS_RELAX.x',
                                               'CELL_Z_AXIS_RELAX_GAMMA.x', 'CELL_Z_AXIS_RELAX_NCL.x',
                                               'GAMMA.x', 'NCL.x', 'VASPSOL.x', 'VASPSOL_GAMMA.x', 'VASPSOL_NCL.x',
                                               'VTST.x', 'VTST_GAMMA.x', 'VTST_NCL.x'],
                                    'suffix': ' > stdout'
                                    },
                           'AVX2': {'path': '/GRAPE/Apps/VASP/bin/5.4.1/AVX2/',
                                    'bin': 'vasp_5.4.1_GRP7_AVX2_p13082016',
                                    'options': ['.x', 'CELL_X_AXIS_RELAX.x', 'CELL_X_AXIS_RELAX_GAMMA.x',
                                               'CELL_X_AXIS_RELAX_NCL.x', 'CELL_Z_AXIS_RELAX.x',
                                               'CELL_Z_AXIS_RELAX_GAMMA.x', 'CELL_Z_AXIS_RELAX_NCL.x',
                                               'GAMMA.x', 'NCL.x', 'VASPSOL.x', 'VASPSOL_GAMMA.x', 'VASPSOL_NCL.x',
                                               'VTST.x', 'VTST_GAMMA.x', 'VTST_NCL.x'],
                                    'suffix': ' > stdout'
                                    },
                           '': {'path': '/home/woosun/Programs/VASP/bin/',
                                'bin': 'vasp_541_20161021_WS',
                                'options': ['W90_std.x', 'W90_gam.x', 'W90_ncl.x'],
                                'suffix': ' > stdout'
                                },
                           },

                   '5.4.4': {'': {'path': '/home/woosun/Programs/VASP/bin/',
                                'bin': 'vasp_544_20170627_WS',
                                'options': ['std.x', 'gam.x', 'ncl.x'],
                                'suffix': ' > stdout'
                                }
                           }

                   }

        qedic = {'5.4.0': {'': {'path': '/home/woosun/Programs/espresso-5.4.0/bin/',
                              'bin': '',
                              'options': ['pw.x'],
                              'suffix': ' < *.in > *.out'
                              }
                         }
                 }

        w90dic = {'1.2': {'': {'path': '/home/woosun/Programs/wannier90/',
                               'bin': 'wannier90_1.2',
                               'options': ['.x'],
                               'suffix': ' wannier90'
                               }
                          },

                  # '2.0': {'': {'path'    : '/home/woosun/Programs/wannier90/',
                  #              'bin'     : 'wannier90_2.0',
                  #              'options' : ['.x'],
                  #              'suffix': ' wannier90'
                  #              }
                  #         }
                  }

        aimsdic = {'160328': {'': {'path': '/home/woosun/Programs/FHI-AIMS/',
                                   'bin': 'aims.160328_3.scalapack.mpi',
                                   'options': '.x',
                                   'suffix': ' < /dev/null > stdout'
                                   }
                              }
                   }

        self.bininfo = {'vasp': vaspdic,
                        'qe': qedic,
                        'w90': w90dic,
                        'aims': aimsdic
                        }

        return

    def test(self):
        self.optim = self.nodeinfo[self.nodegroup]['opt']
        if self.nodegroup not in self.nodeinfo.keys():
            raise AssertionError('No such node groups in MTG-Kohn!')

        if self.numnode > self.nodeinfo[self.nodegroup]['maxnode']:
            raise AssertionError('Requested more nodes than its limitations!')

        if self.corepernode > self.nodeinfo[self.nodegroup]['maxcore']:
            raise AssertionError('Requested more cores than its limitations!')

        if self.prog not in self.bininfo.keys():
            raise AssertionError('No such program installed in MTG-Kohn!')

        if self.ver not in self.bininfo[self.prog].keys():
            raise AssertionError('MTG-Kohn does not have %s version of %s!' % (self.ver, self.prog))

        if self.option not in self.bininfo[self.prog][self.ver][self.optim]['options']:
            raise AssertionError('MTG-Kohn does not have %s options in %s version of %s!'
                                 % (self.option, self.ver, self.prog))
        return

    def exceptions(self):
        # VASP exceptions
        if self.prog == 'vasp':
            if self.ver == '5.3.5':
                exceptionlist = ['.x', 'GAMMA.x', 'NCL.x']
                if self.nodeinfo[self.nodegroup]['opt'] != 'AVX1':
                    if self.option in exceptionlist:
                        print("%s is not compatible with proper optimization in %s nodes."
                              % (self.option, self.nodegroup))
                        if self.option == '.x':
                            self.option = 'VTST.x'
                        elif self.option == 'GAMMA.x':
                            self.option = 'VTST_GAMMA.x'
                        elif self.option == 'NCL.x':
                            self.option = 'VTST_NCL.x'
                        print("Automatically changing the executable file to %s." % self.option)

    def whatisinside(self):
        if self.prog is None:
            print("List of programs:")
            print("--------------------------------")
            for key, value in sorted(self.bininfo.items()):
                print(key)
        else:
            if self.ver is None:
                print("Version list of %s:" % self.prog)
                print("--------------------------------")
                for key, value in sorted(self.bininfo[self.prog].items()):
                    print(key)

            else:
                optionlist = []
                print("List of %s version %s binaries:" % (self.prog, self.ver))
                print("--------------------------------")
                for key, value in sorted(self.bininfo[self.prog][self.ver].items()):
                    for key2 in sorted(self.bininfo[self.prog][self.ver][key]['options']):
                        if key2 not in optionlist:
                            optionlist.append(key2)

                for x in sorted(optionlist):
                    print(x)
                    # if x == '':
                    #     print('.x')
                    # else:
                    #     print(x + '.x')
                print("")
                print("--------------------------------")

        return

    def writescript(self):
        self.exceptions()
        self.test()
        header = ("#!/bin/sh\n"
                  "#PBS -q %s\n"
                  "#PBS -l nodes=%i:ppn=%i\n" % (self.nodegroup, self.numnode, self.corepernode))

        jobname = ("#PBS -N %s\n" % self.jobname)

        walltime = ("#PBS -l walltime=%i:00:00\n" % self.wall)

        midline = ("\nNPROCS=`wc -l < $PBS_NODEFILE`\n"
                   "hostname\n"
                   "date\n"
                   "\ncd $PBS_O_WORKDIR\n"
                   "cp $PBS_NODEFILE nodefile\n\n")

        modules = ("module add Intel/Compiler/17.0.1\n"
                   "module add Intel/MKL/2017.1-132\n"
                   "module add Intel/MPI/2017.1-132\n\n")

        optim = self.nodeinfo[self.nodegroup]['opt']

        with open(self.outfile, 'w') as out:
            out.write(header)

            if self.jobname is not None:
                out.write(jobname)

            if self.wall is not None:
                out.write(walltime)

            out.write(midline)
            out.write(modules)
            out.write('mpirun -genv I_MPI_DEBUG 5 -np $NPROCS ')
            out.write(self.bininfo[self.prog][self.ver][optim]['path'])
            out.write(self.bininfo[self.prog][self.ver][optim]['bin'])

            if self.bininfo[self.prog][self.ver][optim]['options'] != '':
                out.write('_')

            # out.write(self.bininfo[self.prog][self.ver][optim]['options'])
            out.write(self.option)
            out.write(self.bininfo[self.prog][self.ver][optim]['suffix'])
        return


def executemake(args):
    m = Kohn(args.output, args.jobname, args.node, args.numnode, args.core,
             args.walltime, args.program, args.version, args.option)
    m.writescript()
    return


def executelist(args):
    l = Kohn(None, None, None, None, None, None, args.program, args.version, None)
    l.whatisinside()
    return


def executeinteractive(args):
    return


def main():
    description = """description here
"""
    descmake = """
    """
    descint = """
        """
    desclist = """
    """

    # Main parser
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)

    # Subparsers
    subparsers = parser.add_subparsers(title="Functions")
    parser_make = subparsers.add_parser("make", formatter_class=argparse.RawTextHelpFormatter, description=descmake)
    parser_make.add_argument("-o", dest="output", type=str, default="job.sh")
    parser_make.add_argument("-j", dest="jobname", type=str, default=None)
    parser_make.add_argument("-N", dest="node", type=str, required=True)
    parser_make.add_argument("-n", dest="numnode", type=int, required=True)
    parser_make.add_argument("-c", dest="core", type=int, required=True)
    parser_make.add_argument("-w", dest="walltime", type=int, default=None)
    parser_make.add_argument("-p", dest="program", type=str, required=True)
    parser_make.add_argument("-v", dest="version", type=str, required=True)
    parser_make.add_argument("-O", dest="option", type=str, default='.x')
    parser_make.set_defaults(func=executemake)

    parser_list = subparsers.add_parser("list", formatter_class=argparse.RawTextHelpFormatter, description=desclist)
    parser_list.add_argument("-p", dest="program", type=str)
    parser_list.add_argument("-v", dest="version", type=str)
    parser_list.set_defaults(func=executelist)

    parser_interactive = subparsers.add_parser("i", formatter_class=argparse.RawTextHelpFormatter, description=descint)
    parser_interactive.set_defaults(func=executeinteractive)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
