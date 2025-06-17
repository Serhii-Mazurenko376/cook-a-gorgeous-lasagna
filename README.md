# 🍝 Lasagna Time Calculator

This simple Python project calculates cooking times for a lasagna recipe.  
It demonstrates basic function definitions, constants, and how to structure a clean Python script.

## 🧠 Features

- Calculate **remaining bake time**
- Calculate **preparation time** based on number of layers
- Calculate **total elapsed cooking time**

## 📄 Functions Overview

- `bake_time_remaining(elapsed_bake_time)`  
  Returns the remaining bake time in minutes.

- `preparation_time_in_minutes(number_of_layers)`  
  Returns total preparation time based on 2 minutes per layer.

- `elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)`  
  Returns total time spent: prep + baking so far.

## 🧪 Example Usage

```python
print(bake_time_remaining(30))           # Output: 10
print(preparation_time_in_minutes(2))    # Output: 4
print(elapsed_time_in_minutes(3, 20))    # Output: 26

🧰 Requirements
	-	Python 3.x
(No external libraries are required.)

✅ Style

This project follows PEP 8 style guidelines and passes Pylint.

---

📚 License

MIT License. Feel free to use or contribute!
