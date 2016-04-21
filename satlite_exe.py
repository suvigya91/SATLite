"""
Command line tool for SATLite
"""
import argparse
import imp
from satlite import SATLite


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',action='store', help='Scientific tool name')
    parser.add_argument('--resource',action='store', help='Target machine name')
    parser.add_argument('--arguments', help='Input files with arguments')
    parser.add_argument('--exe',action='store', help='Executable (Optional)')
    parser.add_argument('--modules', help='Modules list file (Optional)')
    parser.add_argument('--runtime',action='store', help='(Optional) Runtime range format: [mintime (hh:mm:ss), maxtime(hh:mm:ss)]')
    args = parser.parse_args()
    
    if args.name is None:
        parser.error('Please enter a Scientific tool name')
        sys.exit(1)

    if args.resource is None:
        parser.error('Please enter a Target resouce name')
        sys.exit(1)

    if args.arguments is None:
        parser.error('Please enter a Argument file')
        sys.exit(1)
    
    scientific_tool = args.name
    inp_resource = args.resource
    
    inp_arguments = imp.load_source('arguments', args.arguments)
    
    if args.modules is not None:
        inp_modules = imp.load_source('modules', args.modules)
        inp_modules_list = inp_modules.arguments

    else:
        inp_modules_list = None

##    print args.name
##    print args.resource
##    print args.arguments
##    print inp_arguments.arguments
##    print len(inp_arguments.arguments)
    test = SATLite()
    test.set_attribute(name = args.name,
                       resource = args.resource,
                       arguments = inp_arguments.arguments,
                       exe = args.exe,
                       modules = inp_modules_list,
                       runtime = args.runtime
                       )
    test.run()
