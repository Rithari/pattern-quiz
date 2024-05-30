# Design Pattern Quiz Application

This is a simple Python application that quizzes you on different design patterns. 
It randomly picks a pattern snippet from a collection of text files, displays it, and asks you to identify the pattern.
The application runs in a loop until you terminate it with `Ctrl+C`.

Included pattern snippets are:
- Abstract Factory 2x
- Composite 2x
- Adapter 1x
- State 2x
- Strategy 2x
- Visitor 2x
- Observer 2x
- Decorator 2x
- Singleton 2x

Feel free to merge request additional code snippets.


## How to Run

1. Ensure you have Python installed on your machine.
2. Clone the repository and cd into the root directory
3. Run the application using the following command:

   ```sh
   python app.py
   ```

## How to Add More Patterns

1. **Create a New Text File**:
   - Navigate to the `patterns/` directory.
   - Create a new text file for the design pattern you want to add.

2. **Name the File**:
   - The filename should include the design pattern name followed by a unique number. 
   - For example:
     - `AbstractFactory3.txt`
     - `Strategy2.txt`
     - `Observer1.txt`

3. **Add the Code Snippet**:
   - Open the newly created text file.
   - Place the relevant code snippet for the design pattern inside the file.
   - Save the file.

4. **Ensure Correct Formatting**:
   - The pattern name should be camelCase if it consists of multiple words (e.g., `AbstractFactory`).
   - The application will automatically format it for display purposes.

5. **Run the Application**:
   - The application will automatically include your new pattern file in the quiz the next time it runs.

## How It Works

1. The application reads `.txt` files from the `patterns/` directory.
2. Each `.txt` file contains a code snippet for a specific design pattern.
3. The filename indicates the design pattern, e.g., `AbstractFactory1.txt`, `Singleton2.txt`.
4. The application randomly selects a file, displays its content, and prompts you to guess the design pattern.
5. Your guess is compared with the correct answer derived from the filename.
6. The application informs you whether your guess was correct or incorrect and waits for 2 seconds before showing the next pattern.
