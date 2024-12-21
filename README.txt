Zakiy Manigo UNI: ztm2106
Roshan Prakash UNI: rp3187

### README.txt




The optimization code was added to the meme_lexer_parser_generation.py. That part runs the same as previous parts, implimentation listed below.
I also brought the code optimization to a seperate file, if you want to specifically test its functionality run: python3 -m unittest test_optimizer.py.





What we ran for assignment 3:

./scanner.sh sample_meme_code.txt
javac sample_part1.java(replace with whichever file you want to test)
java sample_part1

Programming Assignment 4 video: https://youtu.be/tuzW1efa_aI

Programming Assignment 3 Video: https://youtu.be/OEw1hR7519E

Programming Assignment 2 Video: https://youtu.be/5MtNUdKvdgQ



PART 4:

Code Optimizer

Our project includes a CodeOptimizer class designed to perform basic compiler optimizations on lines of generated code. After generating Java code (for our meme-generation tool), we pass the resulting lines through the optimizer to clean up and simplify the final output. Below are the details of each optimization technique implemented.

1. Constant Folding

What It Does
Constant folding identifies arithmetic expressions in the form of number operator number and evaluates them at “compile time” rather than at runtime. For instance, if the generated code contains int x = 2 + 3;, constant folding will replace it with int x = 5;.
How It Works in Our Project
We use a regular expression to detect occurrences of \b(\d+)\s*([+\-*/])\s*(\d+)\b in each line.
Each match is evaluated via Python’s eval(), then substituted directly into the code.
The process repeats on the same line if multiple constant expressions are found (e.g., 2 + 3 - 1 → 4 after folding 2 + 3 → 5, then 5 - 1 → 4).
Why It Matters for Our Generated Java Code
The code we generate might contain many numeric expressions for sizes, borders, or loops (if any). By folding these expressions upfront, we reduce unnecessary runtime calculations.
This is especially useful in our meme-generation flow, where image dimensions or counts might be expressed as sums or products.
2. Dead Code Elimination

What It Does
Dead code elimination (DCE) removes assignments to variables that are never used later in the code.
How It Works in Our Project
For each line, the optimizer checks if it contains varName = ....
It then searches subsequent lines to see if varName ever appears again.
If not, the line is considered “dead” and is removed from the final output.
Why It Matters for Our Generated Java Code
During code generation, it’s possible some parameters or variables are created but not utilized (e.g., an unreferenced border color or overlay variable). Removing these lines keeps the final Java file minimal and clean.
It also helps reduce confusion and clutter when reviewing the generated code.
3. Strength Reduction

What It Does
Strength reduction replaces “expensive” arithmetic operations with equivalent but cheaper operations. In our project, it specifically targets multiplication or division by 2.
How It Works in Our Project
After constant folding and dead code elimination, each line is scanned for:
* 2 which is replaced with << 1
/ 2 which is replaced with >> 1
This transformation is a common micro-optimization where shifting bits is (in many architectures) faster than multiplication or division by 2.
Why It Matters for Our Generated Java Code
Although modern Java compilers/JVMs already perform many such optimizations, our approach demonstrates how you might manually optimize at the code level.
If, for instance, you were generating code for an embedded system or a performance-critical loop, these transformations could yield noticeable benefits.
4. Loop Unrolling (Placeholder)

What It Does
Loop unrolling typically expands a loop’s body to reduce overhead (e.g., turning a 4-iteration loop into four successive statements).
How It Works in Our Project
Currently, no loop detection or transformation is implemented. The function is a stub that simply returns the code unmodified.
A future enhancement could detect small for loops in the generated Java code (e.g., a loop that runs from 0 to 3) and replace them with repeated code blocks.
Why It Matters for Our Generated Java Code
Repeatedly calling methods in a loop can add overhead. Unrolling small loops can sometimes improve performance, especially in tight, performance-critical sections of code (e.g., image processing steps).
In a meme-generation scenario, unrolling small loops might reduce overhead, but it would also increase code size, so it’s a trade-off.
Putting It All Together

When you invoke the CodeOptimizer class (usually by creating an instance and calling optimize() on a list of code lines), it applies these techniques in the following order:

Constant Folding – Simplifies numeric expressions at compile time (e.g., 2 + 3 → 5).
Dead Code Elimination – Removes unused variable assignments.
Strength Reduction – Replaces * 2 with << 1 and / 2 with >> 1.
Loop Unrolling  – sets the stage for future expansions.
The end result is typically cleaner, more efficient, and easier-to-read Java code for our meme-generation system.

Example Usage

Below is a short snippet demonstrating how we typically use CodeOptimizer after generating Java code lines:

lines_of_code = java_code.split("\n")
optimizer = CodeOptimizer(lines_of_code)
optimized_code = optimizer.optimize()
final_code = "\n".join(optimized_code)
At that point, final_code contains the optimized Java source, which can then be written to a .java file or used as needed.

---
For part 3 we worked on the same laptop for some of the parts, and ran git reset and git push origin main --force so some of our commits from part 2 and on may be gone. 


# **Meme Generation Program**

## **Overview**

This program processes meme description scripts using a custom lexer, parser, and code generator. It transforms the input script into Java code that generates memes with specified configurations. The pipeline includes:
1. **Lexical Analysis:** Tokenizes the input script.
2. **Parsing:** Constructs an Abstract Syntax Tree (AST) from the tokens.
3. **Code Generation:** Converts the AST into Java code.
4. **Execution:** The generated Java code produces the desired meme configuration.

---

## **Files in the Project**

1. **`meme_lexer_parser_generation.py`**:
   - Python script for lexical analysis, parsing, and Java code generation.
   - Generates a Java file `GeneratedMemeProgram.java`.

2. **`scanner.sh`**:
   - Bash script to process input files containing multiple sample scripts.
   - Splits input files and executes the Python script for each sample.

3. **Sample Input File**:
   - Contains meme configurations in the following format:
     ```
     #Sample input 1
     create meme
         background red
         load pictures beach sun umbrella
         size 800 x 600
         border dotted
             color
         style montage
         text "summer vibes"
             placement top
             overlay yes
         count 10
     save images
     ```

---

## **How to Run**

### **Requirements**
- **Python 3** installed on your system.
- **Java JDK** installed for compiling and executing the generated Java code.

---

### **Steps**

1. **Prepare Input File**:
   - Create Sample Input file: `Sample_meme_code.txt`.

2. **Run the Program**:
   - Execute the `scanner.sh` script with the input file:
     ```bash
     ./scanner.sh Sample_meme_code.txt
     ```
   - This will:
     - Split the input file into smaller files.
     - Process each file with the Python script.
     - Generate a Java program for each sample.

3. **Generated Output**:
   - Each processed input will create a file named `GeneratedMemeProgram.java`.
   - Example:
     ```java
     import java.util.*;

     public class GeneratedMemeProgram {
         public static void main(String[] args) {
             System.out.println("Creating a meme...");
             String background = "red";
             List<String> pictures = Arrays.asList("beach", "sun", "umbrella");
             int width = 800, height = 600;
             String borderStyle = "dotted";
             String borderColor = "color";
             String style = "montage";
             String text = "summer vibes";
             String textPlacement = "top";
             boolean overlay = true;
             int count = 10;

             save_images(background, pictures, width, height, borderStyle, borderColor, style, text, textPlacement, overlay, count);

             System.out.println("Meme generation completed!");
         }

         public static void save_images(String background, List<String> pictures, int width, int height, String borderStyle, String borderColor, String style, String text, String textPlacement, boolean overlay, int count) {
             // Add logic to generate and save images here.
         }
     }
     ```

---

## **Example Input and Output**

### **Input Script**
```plaintext
create meme
    background blue
    load pictures sky cloud bird
    size 1024 x 768
    border solid
        color
    style landscape
    text "peaceful skies"
        placement center
        overlay no
    count 5
save images
```

### **Code Generation**
Running Lexer followed by Parser on sample_part4.txt...
Lexical analysis completed successfully.
[('KEYWORD', 'create'), ('KEYWORD', 'meme'), ('KEYWORD', 'background'), ('ID', 'green'), ('KEYWORD', 'load'), ('ID', 'pictures'), ('ID', 'tree'), ('ID', 'river'), ('ID', 'mountain'), ('KEYWORD', 'size'), ('INT', '1024'), ('OP', 'x'), ('INT', '768'), ('KEYWORD', 'border'), ('ID', 'solid'), ('ID', 'color'), ('KEYWORD', 'style'), ('ID', 'landscape'), ('KEYWORD', 'text'), ('STRING', "nature's beauty"), ('KEYWORD', 'placement'), ('ID', 'bottom'), ('KEYWORD', 'overlay'), ('ID', 'yes'), ('KEYWORD', 'count'), ('INT', '15'), ('KEYWORD', 'save'), ('KEYWORD', 'images')]
Abstract Syntax Tree:
Program
    |-- CreateCommand
    |-- Background ID (green)
    |-- LoadPictures
        |-- Image ID (tree)
        |-- Image ID (river)
        |-- Image ID (mountain)
    |-- Size
        |-- Width INT (1024)
        |-- Operation OP (x)
        |-- Height INT (768)
    |-- Border
        |-- BorderType ID (solid)
        |-- BorderColor ID (color)
    |-- Style ID (landscape)
    |-- Text
        |-- TextContent STRING (nature's beauty)
        |-- Placement ID (bottom)
        |-- Overlay ID (yes)
    |-- Count INT (15)
    |-- SaveCommand

Parsing completed successfully.


Generated Java Code:
import java.util.*;

public class GeneratedMemeProgram {
    public static void main(String[] args) {
        System.out.println("Creating a meme...");
        String background = "green";
        List<String> pictures = Arrays.asList("tree", "river", "mountain");
        int width = 1024, height = 768;
        String borderStyle = "solid";
        String borderColor = "color";
        String style = "landscape";
        String text = "nature's beauty";
        String textPlacement = "bottom";
        boolean overlay = yes;
        int count = 15;
        save_images(background, pictures, width, height, borderStyle, borderColor, style, text, textPlacement, overlay, count);
        System.out.println("Meme generation completed!");
    }

    public static void save_images(String background, List<String> pictures, int width, int height, String borderStyle, String borderColor, String style, String text, String textPlacement, boolean overlay, int count) {
        // Add logic to generate and save images here.
    }

}
```

---

## **Troubleshooting**

1. **Permission Denied for `scanner.sh`**:
   - Ensure the script has execute permissions:
     ```bash
     chmod +x scanner.sh
     ```

2. **Python Script Errors**:
   - Check the input file for syntax errors (e.g., missing keywords or invalid characters).

3. **Java Compilation Errors**:
   - Ensure Java is installed and added to the system PATH.

4. **File Not Found**:
   - Verify the input file path when running the program.

---

