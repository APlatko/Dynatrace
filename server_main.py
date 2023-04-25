from flask import Flask, render_template, request, flash, redirect
import request_function
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdh124arasdWEE@liNsdfb*U(#@$'


@app.route("/")
def index():
    """
    Index page with request choose.
    Change enter blocks due to the chosen request.
    """
    return render_template("index.html", available_cur=" | ".join(request_function.available_currencies))


@app.route("/results", methods=["POST"])
def result():
    """
    Get the values entered by the user and call the selected function(request).
    Invoke flash message in case of error. Redirect to "index" page.
    Convert results to JSON, redirect to the page with the request results in case of success.
    """
    currency_code = request.form["currency_code"]
    date_or_period = request.form["date_or_period"]
    function = request.form["selected_request"]

    if function == "0":
        request_result = request_function.get_avg_rate(currency_code, date_or_period)
        if check_flash_error(request_result, function) is False:
            return redirect("/")
        avg_rate = json.dumps([{"avg_rate": request_result}])
        return render_template("results.html", request_result=avg_rate)

    elif function == "1":
        request_result = request_function.get_max_min_avg_value(currency_code, date_or_period)
        if check_flash_error(request_result) is False:
            return redirect("/")
        max_min_avg = json.dumps([{"max_avg": request_result[0], "min_avg": request_result[1]}])
        return render_template("results.html", request_result=max_min_avg)

    elif function == "2":
        request_result = request_function.get_max_diff_buy_and_ask(currency_code, date_or_period)
        if check_flash_error(request_result) is False:
            return redirect("/")
        max_difference = json.dumps([{"max_difference": request_result}])
        return render_template("results.html", request_result=max_difference)


def check_flash_error(value: int, func: str = None) -> bool:
    """Invoke flash message with an error description in case user entered incorrect information."""
    if func == "0":
        if value == -2:
            flash('Invalid date format, enter date in YYYY-MM-DD format.')
            return False
        if value == -3:
            flash('It is holiday or weekend on your date. Enter a workday.')
            flash('Or you are a traveler from the future:) Check your date.')
            return False
    if value in [-1, -3]:
        flash('No such currency code. Look at the bottom and try again.')
        return False
    if value == -2:
        flash('Invalid period. It is not a digit or not between 1 <= N <= 255.')
        return False


# app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
