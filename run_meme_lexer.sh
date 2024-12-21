#!/bin/bash

# Run the lexer Python script with standard input.
# This will execute the meme_lexer.py script using Python 3.
# You may provide input through standard input (e.g., by piping a file).

# python3 meme_lexer.py
# python3 meme_lexer.py 
# sleep 2
python3 meme_parser.py

# Check if the lexer execution was successful.
# The special variable $? holds the exit status of the last command executed.
# If the exit status is 0, the script will print a success message.
if [ $? -eq 0 ]; then
    echo "Syntax and lexical analysis completed successfully. AST generated."
else
    echo "Error occurred during syntax or lexical analysis."
    exit 1
fi