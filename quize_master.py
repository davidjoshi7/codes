""" 
Asks a single quiz question and checks if the user's answer is correct.
    
    Parameters:
    question (str): The question to be asked.
    options (list): List of answer options.
    correct_option (int): The index of the correct answer in the options list.
    
    Returns:
    bool: True if the user's answer is correct, False otherwise.
    """

def ask_question(question, options, correct_option):
    
    
    # Print the question
    print(question)
    
    # Print each answer option with a corresponding number
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    # Prompt the user for their answer
    answer = input("Your answer (1/2/3/4): ")
    
    # Check if the user's answer matches the correct option
    return int(answer) == correct_option


#Runs the quiz by asking a series of questions and keeping track of the score.
def run_quiz():
    
    
    
    # Print a welcome message
    
    print("Welcome to QuizMaster!")
    print("Test your knowledge and see how much you score.\n")
    
    # Define a list of questions with their answer options and correct option indices
    questions = [
        {
            "question": "What is the capital of Nepal?",
            "options": ["Bharatpur", "Dhangadhi", "Kathmandu", "Damak"],
            "correct_option": 3
        },
        {
            "question": "Who was the first Prime minister of Nepal ?",
            "options": ["Girija Prasad Koirala", "BP Koirala", "Puspa kamal Dahal", "KP Sharma Oli"],
            "correct_option": 2
        },
        {
            "question": "What is Nepal's Biggest river?",
            "options": ["Koshi", "Gandagi", "Karnali", "Trisuli"],
            "correct_option": 1
        },
    ]
    
    # Initialize the score to 0
    score = 0
    
   
   
    # Loop through each question in the list
    
    for question_data in questions:
       
        question = question_data["question"]  # Get the question text
       
        options = question_data["options"]  # Get the list of answer options
       
        correct_option = question_data["correct_option"]  # Get the index of the correct answer
        
       
       
        # Ask the question and update the score based on the user's answer
       
       
        if ask_question(question, options, correct_option):
            print("Correct!\n")  # Inform the user if they answered correctly
            score += 1  # Increment the score
        else:
            print("Wrong!\n")  # Inform the user if they answered incorrectly
    
    
    
    # Print the final score
    print(f"Your final score is: {score} out of {len(questions)}")
    
   
    # Print a thank you message
    print("Thank you for playing QuizMaster!")

# Run the quiz if this script is executed as the main program
if __name__ == "__main__":
    run_quiz()
