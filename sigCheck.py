import base64
import argparse
import sys




def process_command_line():
    parser = argparse.ArgumentParser("sigCheck.py")
    parser.add_argument("-e", "--exponent", dest="exponent", type=int, help="the expnent \
            that is used in the RSA algorithm. This is usually written as the first part \
            of the private and public key.")
    parser.add_argument("-n", "--modulus", dest="modulus", type=int, help="the modulus \
            that is used in the RSA algorithm. This value should be at least 65536, since \
            this program will be encrypting two bytes at a time.")
    parser.add_argument("-H", "--hex", dest="hex_message", help="A message in hex format")
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        quit()
    return parser.parse_args()


def check_errors(args):
    if args.exponent is None or args.modulus is None or args.hex_message is None:
        raise SystemExit("You must supply an exponent, a modulus, and a hex message")
    hexvals = "1234567890abcdef"
    args.hex_message = args.hex_message.lower()
    for char in args.hex_message:
        if char not in hexvals:
            raise SystemExit("The hex message must consist of digits and a-f)")

def twoBytes(hex_string):
    '''
       Break a string of hex values into a list of numbers, 4 hex values (2 bytes) at a time
    '''
    while len(hex_string) % 4 != 0:
        hex_string = '0' + hex_string # left pad with zeros
    for i in range(0, len(hex_string), 4):
        print(hex_string[i:i + 4])
        intval = int(hex_string[i:i+4], 16)
        print(intval)




def main():
    '''
       Parse command line arguments, then the run the appropriate encryption/decryption
    '''
    args = process_command_line()
    check_errors(args)
    twoBytes(args.hex_message)
    print("good so far")


if __name__=="__main__":
    main()
