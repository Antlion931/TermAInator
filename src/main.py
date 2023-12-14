from args import parse_args
from gpt import gpt_proompt
import sys

MAX_PROOMPT_LEN = 10000

def handle_files(proompt, args):
    filenames, files = args['filenames'], args['files']

    if filenames is None:
        return None
    
    proompt = "Here is the list of files:\n"
    for filename, file in zip(filenames, files):
        proompt += filename + ":\n"
        proompt += file + "\n\n"

    return proompt

def handler_error_flag(proompt, args):
    if args['error'] is None:
        return None
    
    proompt = "Here is an error, help me fix it, point me to the right lines in the file:\n"
    
    stdin_content = sys.stdin.read()

    max_len = MAX_PROOMPT_LEN - len(proompt)
    if len(stdin_content) > max_len:
        stdin_content = stdin_content[:max_len]
    return proompt + stdin_content

def main():
    args = parse_args(MAX_PROOMPT_LEN)
    proompt = ""

    proompt += handler_error_flag(proompt, args) or ""
    proompt += handle_files(proompt, args) or ""

    system_proompt = "You are a programming expert trained by OpenAI. Answer as concisely as possible."

    backend = args['backend']
    response = ""
    if backend == 'chatGPT':
        response = gpt_proompt(system_proompt, proompt)
    
    print(response)

if __name__ == "__main__":
    main()