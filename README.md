# TermAInator
TermAInator is a terminal based wrapper for AI models like chatGPT or Llama, it should have a lot of features that would make prompting faster like directly inserting terminal console outputs to prompt, set some predefined profiles like "admin", "rust", "compact", "eli5".
## TODO
- [ ] Learn about different AI models
- [ ] Make frontend
  - [ ] Program can take command-line arguments and prompt based on that
  - [ ] Program can open chat that will handle running commands
  - [ ] Program can have different profiles to add from to your prompt
- [ ] Think about format so that it is easy to use and flexible enough

## Examples of usage
You words like *eli5* will be changed to appropriate prompt, every thing between " will be inserted raw to prompt, prompt is created from left to right, so it is possible to specify order.
> tai "What is 2 + 2 ?" eli5 

You can use predifined tasks like *error*, which will explain error, we can also use !{} to run some command. In prompt there will be command that was run and output of that command.
> tai error !{ g++ test.cpp} eli5

Some of the words can have arguments so they are more flexible, for example this will ask AI to make command that does what we want.
> tai command(prints all files in current directory) compact

There can be also multiple arguments.
> tai program(rust, combine two sorted vectors to one that is sorted) "Additinaly write tests for it"

To avoid some boilerplate with !{cat <file>} we can use !f{} to read file and insert it to prompt.
> tai error !{ g++ test.cpp} !f{test.cpp} emphasize_changes

To avoid Errors there can be only one word that is task, giving multiple *error* and *program* will result in not running prompt at all.
