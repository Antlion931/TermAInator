from args import parse_args
from gpt import gpt_proompt
import sys

def handle_files(args):
    filenames, files = args['filenames'], args['files']

    if filenames is None:
        return None
    
    proompt = "Here is the list of files:\n"
    for filename, file in zip(filenames, files):
        proompt += filename + ":\n"
        proompt += file + "\n\n"

    return proompt

def handler_error_flag(args):
    if args['error'] is None:
        return None
    
    proompt = "Here is an error, help me fix it:\n"
    
    stdin_content = sys.stdin.read()
    return proompt + stdin_content

def main():
    args = parse_args()
    proompt = ""

    proompt += handler_error_flag(args) or ""
    proompt += handle_files(args) or ""

    system_proompt = "You are a programming expert trained by OpenAI. Answer as concisely as possible."

    backend = args['backend']
    response = ""
    if backend == 'chatGPT':
        response = gpt_proompt(system_proompt, proompt)
    
    print(response)

if __name__ == "__main__":
    main()