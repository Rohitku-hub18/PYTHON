
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>

    <input type="number" id="num1" placeholder="First number">
    <input type="number" id="num2" placeholder="Second number">

    <br><br>

    <button onclick="calculate('+')">Add</button>
    <button onclick="calculate('-')">Subtract</button>
    <button onclick="calculate('*')">Multiply</button>
    <button onclick="calculate('/')">Divide</button>

    <h2 id="result">Result: </h2>

    <script>
        function calculate(operator) {
            let a = Number(document.getElementById("num1").value);
            let b = Number(document.getElementById("num2").value);
            let result;

            if (operator === '+') result = a + b;
            else if (operator === '-') result = a - b;
            else if (operator === '*') result = a * b;
            else if (operator === '/') {
                result = b !== 0 ? a / b : "Cannot divide by zero";
            }

            document.getElementById("result").textContent =
                "Result: " + result;
        }
    </script>
</body>
</html>
