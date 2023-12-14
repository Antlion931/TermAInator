from args import parse_args

def handle_files(args):
    filenames, files = args['filenames'], args['files']

    if filenames is None:
        return None
    
    proompt = "Here is the list of files:\n"
    for filename, file in zip(filenames, files):
        proompt += filename + ":\n"
        proompt += file + "\n\n"

    return proompt

def main():
    args = parse_args()
    proompt = ""

    proompt += handle_files(args) or ""

    print(proompt)

if __name__ == "__main__":
    main()