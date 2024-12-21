#!/bin/bash

# Check if the input file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Input file to be processed
INPUT_FILE=$1

# Check if the file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' not found."
    exit 1
fi

# Use awk to split the file by each "#Sample" comment line
awk -v prefix="sample_part" '
/^#Sample/ {
    # Close previous part file and increment part counter
    if (out) close(out)
    out = sprintf("%s%d.txt", prefix, ++count)
}
{
    # Write each line to the current part file
    if (out) print > out
}
' "$INPUT_FILE"

# Loop through each generated sample_part file and run the lexer and parser on it
for PART in sample_part*.txt; do
    echo "Processing $PART..."
    python3 meme_lexer_parser_generation.py "$PART"

    # Remove processed sample part file
    rm -f "$PART"
done

echo "Processing complete."
