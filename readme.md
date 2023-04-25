It is a small web server on Flask.

Script does the following three requests:

1. Provide an average exchange rate on entered date (formatted YYYY-MM-DD) and a currency code.
2. Provide the max and min average value of a currency and for the number of last quotations N (N <= 255).
3. Provide the major difference between the buy and ask rate of a currency and the number of last quotations N (N <= 255).

Source is http://api.nbp.pl/

How to use:

- To run server enter in terminal 'python server_main.py'.
- Go to browser and enter 'http://localhost:5000'.
- Choose one of the request and enter the required data.
- Get the result.


Link to docker image: https://hub.docker.com/repository/docker/aplatko/dynatrace-web/general

