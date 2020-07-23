# rasa-rest-api-loadtest

## What is it?

Basic tool (based on [Locust.io](https://www.locust.io)) to perform load test of [Rasa](https://www.rasa.com) based chatbot via REST API.

We use it to test our bots and create fact-based sizing calculators.

## Prerequisites

### Rasa

1. You should have Rasa bot :)
2. You should enable Rasa REST API endpoint (see [Rasa docs](https://rasa.com/docs/) on how to do it - final method depends on your deployment method)
3. Bot's REST API endpoint should be acessable via network

### Environment & Dependencies
- Python 3
- Locust.io

## Setup

### Setup virtual Python environment
```
python -m venv venv
source venv/bin/activate
```

### Install dependencies
```
install -r requirements.txt
```

### Correct API Url
Correct REST API URL in `rasa-rest-explode-brain.py` (it depends on your Rasa installation)

Common RasaX endpoint: `/core/webhooks/rest/webhook`

Common Rasa Open Source endpoint: `webhooks/rest/webhook`

## Usage

Launch Locust:
```
locust -f rasa-rest-explode-brain.py
```

then open Locust Web UI [http://127.0.0.1:8089](http://127.0.0.1:8089), enter number of Users, Hatch rate and your Rasa host (e.g. http://localhost:5005) and press 'Start swarming'

## Example of results

I've used [this](https://github.com/clinc/oos-eval) dataset to generate Rasa configuration with some Python scripts (150 intents with 100 training phrases each = 15 000 phrases and 150 generated stories with length=6 steps)

With this stress test i've managed to get stable 300 concurrent users, ±45 rps, with response time around 370ms (95th percentile) - which is pretty impressive imho.

Testing environment:
MacBook Pro 13 2017 with launched in parallel VSCode, MS Teams, Safari, Mail, etc.
