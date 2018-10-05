#!/usr/bin/env python2
# -*- coding: UTF-8 -*-


import argparse
import os, sys
import timeit
from functools import partial
import multiprocessing as mp
from string import punctuation


def main(argc, argv):
    if argc == 3:
        print "Error: No policy specified!"
        sys.exit(1)


    start = timeit.default_timer()
    args = parse_my_args()

    global args_list
    file_input = argv[1]
    file_output = argv[2]
    procs=[]

    manager = mp.Manager()
    pwds_output = manager.list()

    pool = mp.Pool(mp.cpu_count())

    if os.path.isfile(file_input):
        if os.stat(file_input).st_size:
            policy=create_policy(args)

            with open(file_input, 'rU') as f_input, open(file_output, 'wb') as f_output:
                print "[+] Filtering..."
<<<<<<< HEAD

=======
>>>>>>> f9547790db7e9396c7a6592482133ed76ecff59e
                f_read = partial(f_input.read, SIZE_32_MBYTES)

                for chunk in iter(f_read, ''):
                    chunk += f_input.readline()
                    proc = mp.Process(target=process_chunk, args=(chunk, policy, pwds_output))
                    procs.append(proc)
                    proc.start()

                for proc in procs: proc.join()

                print "[+] Done! Writing results (%i), please be patient..." %(len(pwds_output))
                f_output.write(os.linesep.join(pwds_output))

        else:
            print "Error: Input file is empty!"
            sys.exit(1)
    else:
        print "Error: Input file does not exist!"
        sys.exit(1)

    end = timeit.default_timer()
    print "\nExecuted in %is" %(end - start)




def is_valid(policy, password):
    valid = True

    if policy["minl"] and len(password) < policy['minl']: valid = False
    if policy["maxl"] and len(password) > policy['maxl']: valid = False
    if policy["low"] and not any([c.islower() for c in password]): valid = False
    elif policy["up"] and not any([c.isupper() for c in password]): valid = False
    elif policy["num"] and not any([c.isdigit() for c in password]): valid = False
    elif policy["spec"] and not any([c for c in password if c in SPECIAL_CHARS]): valid = False

    return valid


def process_chunk(chunk, policy, pwds_output):
    passwords = chunk.splitlines()
    pwds_output += [ p for p in passwords if is_valid(policy, p) ]


def create_policy(args):
    global args_list
    policy = []

    args_list = vars(args)
    del args_list['file_input']
    del args_list['file_output']

    if not [ key for key, value in args_list.iteritems() if key not in ('minl','maxl') and value ]:
        print "[+] WARNING: You may want to include lowercase [-low], uppercase [-up] or numbers [-num]."
        # choice=raw_input("Continue? [y/n] ")
        # while choice != "y" or "Y" or "n" or "N":
        #     if choice == "y" or "Y": continue
        #     elif choice == "n" or "N": 
        #         print "Aborting!"
        #         sys.exit(1)
        #     else: choice=raw_input("Continue? [y/n] ")
    
    return args_list


def parse_my_args():
    parser = MyParser(
        description='Password Filterer: Filter a password dictionary by applying a specific password policy.'
        )

    parser.add_argument('file_input', type=str, help='input file')
    parser.add_argument("file_output", type=str, help="output file")
    parser.add_argument('-minl', type=int, help='minimum password length')
    parser.add_argument('-maxl', type=int, help='maximum password length')
    parser.add_argument('-low', action="store_true", help='include lowercase characters')
    parser.add_argument('-up', action="store_true", help='include uppercase characters')
    parser.add_argument('-num', action="store_true", help='include numbers')
    parser.add_argument('-spec', action="store_true", help='include special characters')

    args = parser.parse_args()

    if args.minl and args.maxl and args.minl > args.maxl:
        print "Error: Minimum length cannot be bigger than maximum length!"
        sys.exit(1)

    return args


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


SIZE_4k = 4096
SIZE_16_MBYTES = 16777216
SIZE_32_MBYTES = 33554432
SIZE_64_MBYTES = 67108864
SIZE_128_MBYTES = 134217728
SPECIAL_CHARS = set(punctuation)
args_list = {}


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
