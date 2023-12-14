import argparse
import sys

# Returns a dictionary of parsed arguments
# file_names: list of file names from the -f flag
def parse_args():
    parser = argparse.ArgumentParser(description="TermAInator is a terminal based wrapper for AI models like chatGPT or Llama.")

    parser.add_argument(
        '-f', '--files', 
        nargs='+',
        help='List of files, separated by commas',
        required=False,
    )

    parser.add_argument(
        '-b', '--backend',
        help='Backend to use for the AI model. Currently supported: chatGPT, llama',
        default='chatGPT',
    )

    # it does not take an argument, so it is a flag
    parser.add_argument(
        '-e', '--error',
        help='Takes error from stdin.',
        required=False,
        action = 'store_true',
    )

    args = parser.parse_args()

    parsed_arguments = {}

    args.files
    filenames = None
    files = None
    if args.files is not None:
        filenames = [f for f in args.files]
        files = load_files(filenames, MAX_LEN=10000)
    parsed_arguments['filenames'] = filenames or None
    parsed_arguments['files'] = files or None

    parsed_arguments['backend'] = args.backend

    parsed_arguments['error'] = args.error or None


    return parsed_arguments


def load_files(filenames, MAX_LEN=10000):
    files = []
    total_length = 0

    for filename in filenames:
        try:
            with open(filename, 'r') as f:
                file_content = f.read()
                files.append(file_content)
                total_length += len(file_content)

                if total_length > MAX_LEN:
                    print(f"Error: The total length of the files exceeds the maximum allowed length of {MAX_LEN} characters.")
                    sys.exit(1)

        except IOError as e:
            print(f"Error opening file {filename}: {e}")
            sys.exit(1)

    return files