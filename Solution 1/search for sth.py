def search_for_de(previous_inputs):
    # Iterate through each input value and its index in the list
    for index, value in enumerate(previous_inputs):
        # Check if the value is a float and if it contains the string "de"
        if isinstance(value, float) and "de" in str(value):
            # If "de" is found in the value, print its index and value
            print(f"Found 'de' in the input at index {index}: {value}")
    
    # After checking all inputs, print a message indicating the search is completed
    print("Search completed.")

if __name__ == "__main__":
    # Ask the user for the number of float inputs they want to provide
    num_inputs = int(input("How many float inputs do you want to provide? "))
    inputs = []
    # Loop to gather the float inputs from the user
    for i in range(num_inputs):
        input_value = input(f"Enter float input {i + 1}: ")
        try:
            # Convert the input to a float and append it to the list of inputs
            float_value = float(input_value)
            inputs.append(float_value)
        except ValueError:
            # If the input cannot be converted to a float, inform the user
            print(f"Invalid input: '{input_value}' is not a valid float.")

    # Call the search_for_de function with the list of entered float inputs
    search_for_de(inputs)
`