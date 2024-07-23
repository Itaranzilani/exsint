def handle_response(snowball_prompt_response_1):
    # Print the text content of the response
    print("Snowball #1: ", snowball_prompt_response_1.text())

# Assuming snowball_prompt_response_1 is obtained from some previous code
import requests
snowball_prompt_response_1 = requests.get('https://api.example.com/data')

# Call the function with the response object
handle_response(snowball_prompt_response_1)
