from datetime import datetime

def print_instructions():
    """
    Prints the instructions for playing the MadLibs game.
    """
    print('''
    Welcome to the MadLibs game!

    In this game, you'll be asked to provide various words - nouns, verbs, adjectives, etc.
    These words will be used to fill in the blanks in a story, creating often humorous or whimsical results.

    How to play:
    1. You will be prompted to enter different types of words (like a noun, a verb, or an adjective).
    2. Enter any word that fits the requested type.
    3. Type 'undo' to undo your last entered word.
    4. Once all words are provided, the completed story will be revealed!

    Ready to have some fun? Let's get started!
    ''')

def read_template(file_path):
    """
    Reads a template file and returns its content.

    Args:
    file_path (str): The path to the template file.

    Returns:
    str: The content of the file as a string.

    Raises:
    FileNotFoundError: If the file at the specified path does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as error:
        raise FileNotFoundError(f"The file '{file_path}' was not found.") from error

def parse_template(string):
    """
    Extracts placeholders from a template string and returns a tuple containing the 
    template with placeholders replaced by empty braces and a tuple of extracted placeholders.

    Args:
    string (str): The template string with placeholders.

    Returns:
    tuple: A tuple containing the modified template string and a tuple of placeholders.
    """
    parts_of_speech = tuple(word[1:-1] for word in string.split() if word.startswith('{') and word.endswith('}'))
    stripped_string = ' '.join(['{}' if word.startswith('{') and word.endswith('}') else word for word in string.split()])
    return stripped_string, parts_of_speech

def merge(empty, word_list):
    """
    Fills the placeholders in the template string with the user's inputs.

    Args:
    empty (str): The template string with empty placeholders.
    word_list (list of str): A list of user inputs.

    Returns:
    str: The completed MadLibs story.
    """
    return empty.format(*word_list)

def write_to_file(madlib):
    """
    Writes the completed MadLibs story to a file with a unique timestamp in its name.

    Args:
    madlib (str): The completed MadLibs story.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = f'madlib_cli/assets/completed_madlib_{timestamp}.txt'
    with open(output_file_path, 'w') as file:
        file.write(madlib)

def get_user_inputs(parts_of_speech):
    """
    Loops through a list of parts of speech, prompting the user for inputs, and returns a list of those inputs.

    Args:
    parts_of_speech (list of str): A list of parts of speech.

    Returns:
    list of str: A list containing the user's inputs.
    """
    inputs = []

    for part in parts_of_speech:
        user_input = input(f"Enter a {part}: ")
        if user_input.strip() == '':
            user_input = "blank"
        inputs.append(user_input)

    return inputs

def main():
    """
    The main function to run the MadLibs game. It orchestrates reading the template, getting user inputs, 
    merging inputs into the template, and writing the result to a file.
    """
    print_instructions()
    try:
        template = read_template('madlib_cli/assets/dark_and_stormy_night_template.txt')

        stripped_template, parts_of_speech = parse_template(template)

        user_inputs = get_user_inputs(parts_of_speech)

        completed_madlib = merge(stripped_template, user_inputs)

        print("\nHere is your completed MadLib:")
        print(completed_madlib)

        write_to_file(completed_madlib)

    except FileNotFoundError as error:
        print(error)

if __name__ == "__main__":
    main()
