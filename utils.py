
import json
from typing import Dict, Any, List
from datetime import datetime


def load_data_from_file(filename: str) -> List[Dict[str, Any]]:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def save_response_to_file(response: Dict[str, Any], filename: str) -> Dict[str, Any]:
    data: List[Dict[str, Any]] = []

    # Load existing data from the file
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # If the file doesn't exist or is empty, we'll just use an empty list

    # Add an id and createDate to the response
    response['id'] = len(data) + 1  # The id is one more than the number of items already in the list
    response['createDate'] = datetime.now().isoformat()  # The createDate is the current date and time

    # Add the new response to the list
    data.append(response)

    # Write the updated list back to the file
    with open(filename, 'w') as f:
        json.dump(data, f)

    # Return the updated response
    return response