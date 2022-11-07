import requests


resource = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
resource.raise_for_status()
question_data = resource.json()['results']

