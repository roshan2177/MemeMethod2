Zakiy Manigo UNI: ztm2106
Roshan Prakash UNI: rp3187

### README.txt




The optimization code was added to the meme_lexer_parser_generation.py. That part runs the same as previous parts, implimentation listed below.
I also brought the code optimization to a seperate file, if you want to specifically test its functionality run: python3 -m unittest test_optimizer.py.









What we ran for assignment 3:

./scanner.sh sample_meme_code.txt
javac sample_part1.java(replace with whichever file you want to test)
java sample_part1


Programming Assignment 3 Video: https://youtu.be/OEw1hR7519E

Programming Assignment 2 Video: https://youtu.be/5MtNUdKvdgQ


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
