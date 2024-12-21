import sys

class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_state = "Start"
        self.keywords = {"create", "meme", "background", "load", "size", "border", "style", "text", 
                         "placement", "overlay", "count", "save", "images"}
        self.operators = {"x"}
        self.delimiters = {" ", "\n"}
    
    def scan(self):
        index = 0
        while index < len(self.source_code):
            # Skip comment lines that start with '#'
            if self.source_code[index] == '#':
                # Move the index to the next line
                index = self.source_code.find('\n', index)
                if index == -1:
                    break  # End of file reached
                index += 1
                continue

            char = self.source_code[index]
            
            if self.current_state == "Start":
                if char.isalpha():
                    start_index = index
                    # Continue scanning while characters are alphabetic, numeric, underscores, or hyphens
                    while index < len(self.source_code) and (
                        self.source_code[index].isalpha() or 
                        self.source_code[index].isdigit() or 
                        self.source_code[index] == '_' or 
                        self.source_code[index] == '-'):
                        index += 1
                    value = self.source_code[start_index:index]
                    if value in self.operators:
                        self.tokens.append(("OP", value))
                    else:
                        token_type = "KEYWORD" if value in self.keywords else "ID"
                        self.tokens.append((token_type, value))
                    self.current_state = "Start"
                elif char.isdigit():
                    start_index = index
                    while index < len(self.source_code) and self.source_code[index].isdigit():
                        index += 1
                    value = self.source_code[start_index:index]
                    self.tokens.append(("INT", value))
                    self.current_state = "Start"
                elif char == '"':
                    start_index = index + 1
                    index += 1
                    while index < len(self.source_code) and self.source_code[index] != '"':
                        index += 1
                    value = self.source_code[start_index:index]
                    index += 1
                    self.tokens.append(("STRING", value))
                    self.current_state = "Start"
                elif char in self.operators:
                    self.tokens.append(("OP", char))
                    index += 1
                    self.current_state = "Start"
                elif char in self.delimiters:
                    index += 1
                    self.current_state = "Start"
                else:
                    self.current_state = "Error"
                    print(f"Lexical Error: Unexpected character '{char}'")
                    break
        return self.tokens

# Check if an input file was provided as an argument
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        input_text = f.read()
else:
    input_text = """
    create meme
        background blue
        load pictures dogs cats grass
        size 1024 x 1024
        border solid
            color
        style collage
        text "we all love animals"
            placement middle
            overlay yes
        text "of course"
            placement bottom
            overlay no
        count 50
    save images
    """

# Create a scanner object with the input text
scanner = Scanner(input_text)

# Run the scanner to tokenize the input
tokens = scanner.scan()

# Print the tokens
for token in tokens:
    print(token)