from flask import Flask, request, render_template_string

app = Flask(__name__)

# Define HTML template with placeholders for dynamic content
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .calculator {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .calculator input, .calculator select, .calculator button {
            margin: 10px 0;
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>Basic Calculator</h1>
        <form method="POST">
            <input type="number" name="num1" placeholder="Enter the first number" required>
            <input type="number" name="num2" placeholder="Enter the second number" required>
            <select name="operation">
                <option value="">Select an operation</option>
                <option value="+">Addition (+)</option>
                <option value="-">Subtraction (-)</option>
                <option value="*">Multiplication (*)</option>
                <option value="/">Division (/)</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
        <div class="result">The result is: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    result = 'Error: Division by zero is not allowed.'
                else:
                    result = num1 / num2
            else:
                result = 'Error: Invalid operation selected.'
        except ValueError:
            result = 'Error: Invalid input. Please enter numeric values.'

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
