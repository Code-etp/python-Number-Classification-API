# Number-Classification-API
## Overview

The Number Classification API is a Flask-based RESTful API that classifies numbers based on various mathematical properties. It determines if a number is prime, perfect, or an Armstrong number, and provides additional insights such as its parity (odd/even) and digit sum. The API also fetches fun mathematical facts about numbers from the Numbers API.

## Features

- Classifies a given number as:
  - Prime
  - Perfect
  - Armstrong
  - Odd or Even
- Computes the sum of digits
- Fetches fun facts about numbers
- CORS-enabled for cross-origin access
- Deployed on Render for public accessibility

# Technologies Used

- Python 3.9
- Flask (Web framework)
- Flask-CORS (Cross-Origin Resource Sharing)
- Gunicorn (WSGI server)
- Requests (For fetching number facts)
- Render (For cloud deployment)
