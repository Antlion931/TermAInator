from args import parse_args

def main():
    args = parse_args()
    print(args['filenames'])

    for file in args['files']:
        print(file)

if __name__ == "__main__":
    main()