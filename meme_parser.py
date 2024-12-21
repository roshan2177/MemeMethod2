import sys

# Lexer Code Logic
class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_state = "Start"
        self.error_occurred = False  # Add this flag
        self.keywords = {"create", "meme", "background", "load", "size", "border", "style", "text", 
                         "placement", "overlay", "count", "save", "images"}
        self.operators = {"x"}
        self.delimiters = {" ", "\n"}
    
    def scan(self):
        index = 0
        while index < len(self.source_code):
            # Skip comment lines that start with '#'
            if self.source_code[index] == '#':
                index = self.source_code.find('\n', index)
                if index == -1:
                    break  # End of file reached
                index += 1
                continue

            char = self.source_code[index]
            
            if self.current_state == "Start":
                if char.isalpha():
                    start_index = index
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
                    self.error_occurred = True  # Set error flag
                    break
        return not self.error_occurred  # Return success status





# Parsing Code Logic
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class ASTNode:
    def __init__(self, node_type, token=None, children=None):
        self.node_type = node_type
        self.token = token
        self.children = children if children is not None else []
    
    def to_string(self, level=0):
        prefix = "    " * level + "|-- " if level > 0 else ""
        token_type = self.token[0] if self.token else ""
        token_value = self.token[1] if self.token else "None"
        
        if self.node_type in ["CreateCommand", "SaveCommand", "Program"]:
            ret = f"{prefix}{self.node_type}\n"
        elif self.node_type in ["LoadPictures", "Size", "Border", "Text"]:
            ret = f"{prefix}{self.node_type}\n"        
        else:
            ret = f"{prefix}{self.node_type} {token_type} ({token_value})\n"
        
        for child in self.children:
            if isinstance(child, ASTNode):
                ret += child.to_string(level + 1)
            else:
                ret += "    " * (level + 1) + f"|-- {str(child)}\n"
                
        return ret

    def __repr__(self):
        return self.to_string()
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.ast = None

    def parse(self):
        self.match("KEYWORD", "create")
        self.match("KEYWORD", "meme")
        create_node = ASTNode("CreateCommand")

        children = [create_node]
        while not self.check("KEYWORD", "save"):
            children.append(self.parse_section())
        
        self.match("KEYWORD", "save")
        self.match("KEYWORD", "images")
        save_node = ASTNode("SaveCommand")
        children.append(save_node)

        return ASTNode("Program", children=children)

    def parse_section(self):
        if self.check("KEYWORD", "background"):
            self.match("KEYWORD", "background")
            color = self.consume("ID")
            return ASTNode("Background", token=color)
        
        elif self.check("KEYWORD", "load"):
            self.match("KEYWORD", "load")
            self.match("ID", "pictures")
            images = []
            while self.check("ID"):
                images.append(ASTNode("Image", token=self.consume("ID")))
            return ASTNode("LoadPictures", children=images)
        
        elif self.check("KEYWORD", "size"):
            self.match("KEYWORD", "size")
            width = self.consume("INT")
            operation = self.consume("OP")
            height = self.consume("INT")
            return ASTNode("Size", children=[ASTNode("Width", token=width), ASTNode("Operation", token=operation), ASTNode("Height", token=height)])
        
        elif self.check("KEYWORD", "border"):
            self.match("KEYWORD", "border")
            border_type = self.consume("ID")
            color = None
            if self.check("ID", "color"):
                color = self.consume("ID")
            return ASTNode("Border", children=[ASTNode("BorderType", token=border_type), ASTNode("BorderColor", token=color)])
        
        elif self.check("KEYWORD", "style"):
            self.match("KEYWORD", "style")
            style_value = self.consume("ID")
            return ASTNode("Style", token=style_value)
        
        elif self.check("KEYWORD", "text"):
            self.match("KEYWORD", "text")
            text_content = self.consume("STRING")
            properties = [ASTNode("TextContent", token=text_content)]
            if self.check("KEYWORD", "placement"):
                self.match("KEYWORD", "placement")
                placement = self.consume("ID")
                properties.append(ASTNode("Placement", token=placement))
            if self.check("KEYWORD", "overlay"):
                self.match("KEYWORD", "overlay")
                overlay = self.consume("ID")
                properties.append(ASTNode("Overlay", token=overlay))
            return ASTNode("Text", children=properties)
        
        elif self.check("KEYWORD", "count"):
            self.match("KEYWORD", "count")
            count_value = self.consume("INT")
            return ASTNode("Count", token=count_value)
        
        else:
            raise SyntaxError(f"Unexpected token: {self.peek()}")

    def match(self, token_type, token_value=None):
        if self.check(token_type, token_value):
            return self.advance()
        raise SyntaxError(f"Expected {token_type} {token_value or ''} but found {self.peek()}")

    def consume(self, token_type, token_value=None):
        if self.check(token_type, token_value):
            return self.advance()
        raise SyntaxError(f"Expected token {token_type} {token_value or ''}, got {self.peek()}")

    def check(self, token_type, token_value=None):
        if self.is_at_end():
            return False
        current_token = self.peek()
        if current_token[0] != token_type:
            return False
        if token_value is not None and current_token[1] != token_value:
            return False
        return True

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.current >= len(self.tokens) or self.peek()[0] == "EOF"

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

# Check if an input file was provided as an argument
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        input_text = f.read()
else:
    input_text = """
    create meme
        background green
        load pictures cat dog tree
        size 1024 / 768
        border dashed
        style grid
    save images
    """

# Create a scanner and tokenize the input
scanner = Scanner(input_text)
if scanner.scan():
    print("Lexical analysis completed successfully.")
    tokens = scanner.tokens
    print(tokens)

    # Parse the tokens and create the AST
    parser = Parser(tokens)
    ast = parser.parse()

    # Print the AST
    print("Abstract Syntax Tree:")
    print(ast)
    print("Parsing completed successfully.")
    print("\n")
else:
    print("Lexical analysis failed due to errors.")
