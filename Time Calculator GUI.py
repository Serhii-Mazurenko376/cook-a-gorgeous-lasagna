import ui

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


def calculate_results(sender):
    try:
        layers = int(layer_input.text)
        elapsed = int(elapsed_input.text)

        prep = preparation_time_in_minutes(layers)
        remaining = bake_time_remaining(elapsed)
        total = elapsed_time_in_minutes(layers, elapsed)

        result_label.text = (
            f"Prep time: {prep} min\n"
            f"Remaining bake: {remaining} min\n"
            f"Total time: {total} min"
        )
    except ValueError:
        result_label.text = "Please enter valid numbers."


# Build the UI
view = ui.View(name='Lasagna Timer', bg_color='white', width=320, height=300)

layer_input = ui.TextField(placeholder='Number of layers', frame=(20, 20, 280, 32))
elapsed_input = ui.TextField(placeholder='Elapsed bake time (min)', frame=(20, 60, 280, 32))

button = ui.Button(title='Calculate', frame=(20, 100, 280, 40), bg_color='lightblue')
button.action = calculate_results

result_label = ui.Label(frame=(20, 160, 280, 100), number_of_lines=3)
result_label.text_color = 'black'

# Add components to view
view.add_subview(layer_input)
view.add_subview(elapsed_input)
view.add_subview(button)
view.add_subview(result_label)


view.present('sheet')
def chef_gpt_response(prompt):
    """Simulated GPT response (can replace with real GPT later)."""
    prompt = prompt.lower()
    if "joke" in prompt:
        return "Why did the lasagna go to therapy? Too many layers of issues! 😄"
    elif "side dish" in prompt:
        return "How about a fresh green salad or garlic bread? Classic!"
    elif "cheese" in prompt:
        return "If you’re using extra cheese, add 5-7 minutes to the bake time."
    else:
        return "I'm ChefGPT! Ask me anything about lasagna, recipes, or fun tips!"
        

gpt_input = ui.TextField(placeholder='Ask ChefGPT...', frame=(20, 210, 280, 32))

gpt_button = ui.Button(title='Ask ChefGPT', frame=(20, 250, 280, 40), bg_color='orange')
gpt_result = ui.Label(frame=(20, 300, 280, 100), number_of_lines=3)
gpt_result.text_color = 'darkgray'

def ask_chef_gpt(sender):
    response = chef_gpt_response(gpt_input.text)
    gpt_result.text = response

gpt_button.action = ask_chef_gpt

# Add to view
view.add_subview(gpt_input)
view.add_subview(gpt_button)
view.add_subview(gpt_result)
