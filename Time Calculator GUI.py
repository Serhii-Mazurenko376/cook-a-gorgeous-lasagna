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
