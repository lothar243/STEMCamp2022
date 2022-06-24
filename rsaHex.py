#! /usr/bin/python3

import argparse
import sys


def process_command_line():
    parser = argparse.ArgumentParser("sigCheck.py")
    parser.add_argument("-e", "--exponent", dest="exponent", type=int,
            help="the expnent that is used in the RSA algorithm. This is\
                    usually written as the first part of the private and \
                    public key.")
    parser.add_argument("-n", "--modulus", dest="modulus", type=int, help="the\
            modulus that is used in the RSA algorithm. This is usually written\
            as the second part of the private and public key.")
    parser.add_argument("hex_message", nargs="*", help="A message \
            expressed as a number in hexadecimal format (all characters should\
            be in 0123456789abcdef)")
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        quit()
    return parser.parse_args()


def check_errors(args):
    '''
    Checks to ensure that all three required arguments are set, and that \
    the hex message is in actually in hex
    '''
    if not sys.stdin.isatty():
        standard_input = sys.stdin.read().split(' ')
        # print(f"{standard_input=}")
        args.hex_message = standard_input[0].lower().strip()
    else:
        args.hex_message = args.hex_message[0].lower()
    if args.exponent is None or args.modulus is None or args.hex_message is None:
        raise SystemExit("You must supply an exponent (with -e), a modulus \
                (with -n), and a hex message")
    hexvals = "1234567890abcdef"
    for char in args.hex_message:
        #stderr("Testing " + char)
        if char not in hexvals:
            raise SystemExit("The hex message must consist of digits and a-f: '" + char + "'")


def break_into_chunks(hex_string, modulus):
    '''
    Break a string of hex values into a list of numbers, each between 0 \
    and n-1
    '''
    number = int(hex_string, 16)
    list_of_chunks = []
    while number > 0:
        list_of_chunks.append(number % modulus)
        number = number // modulus
    return list_of_chunks


def rsa(message, exponent, modulus):
    return message ** exponent % modulus


def join_list_of_chunks(list_of_chunks, modulus):
    val = 0
    for chunk in reversed(list_of_chunks):
        val = chunk + modulus * val
    return hex(val)


def main():
    '''
    Parse command line arguments, then the run the appropriate encryption/\
    decryption
    '''
    args = process_command_line()
    check_errors(args)
    list_of_chunks = break_into_chunks(args.hex_message, args.modulus)
    encoded_list = [rsa(message, args.exponent, args.modulus) for message in list_of_chunks]
    output_string = str(join_list_of_chunks(encoded_list, args.modulus))[2:]
    sys.stdout.write(output_string + "\n")


if __name__ == "__main__":
    main()
