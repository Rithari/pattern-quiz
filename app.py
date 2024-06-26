import os
import random
import time
from collections import deque

# Extrapolate the pattern name from the filename (e.g., AbstractFactory1.txt -> Abstract Factory)
def get_pattern_from_filename(filename):
    basename = os.path.basename(filename)
    pattern_name = ''.join([i for i in basename if not i.isdigit()]).replace('.txt', '')
    return pattern_name.replace('Factory', ' Factory') # Add space after Abstract so the answer can be read

def main():
    # Directory where pattern files are stored
    pattern_dir = 'patterns/'
    
    # Define the size of the cache for recently shown files
    cache_size = 5
    recently_shown = deque(maxlen=cache_size)

    try:
        while True:
            # Get a list of all .txt files in the directory
            files = [f for f in os.listdir(pattern_dir) if f.endswith('.txt')]
            
            # Filter out files that were recently shown
            available_files = [f for f in files if f not in recently_shown]
            
            # If all files have been shown recently, reset the cache
            if not available_files:
                recently_shown.clear()
                available_files = files
            
            # Choose a random file from the available list
            chosen_file = random.choice(available_files)
            recently_shown.append(chosen_file)
            full_path = os.path.join(pattern_dir, chosen_file)
            
            # Read and display the content of the file
            with open(full_path, 'r') as file:
                content = file.read()
                print("\n" + content)
            
            # Ask the user to guess the pattern
            user_guess = input("\nWhat design pattern is this? (CTRL+C to exit) ").strip()

            # Get the correct answer from the filename
            correct_answer = get_pattern_from_filename(chosen_file)
            
            # Check if the user's guess is correct
            if user_guess.lower() == correct_answer.lower():
                print("\n************************************")
                print("Correct! This is the", correct_answer, "pattern.")
                print("************************************")
            else:
                print("\n************************************")
                print("Incorrect. The correct answer is:", correct_answer)
                print("************************************")

            # Wait for 2 seconds before showing the next pattern
            time.sleep(2)

    except FileNotFoundError:
        print("No .txt files found. Please check the filename and try again.")
    except KeyboardInterrupt:
        print("\nExiting the quiz. Goodbye!")

if __name__ == "__main__":
    main()