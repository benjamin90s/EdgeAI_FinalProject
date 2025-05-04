# Bird Voice Classifier (Edge Impulse + Web Interface)

## Overview
This project allows you to run `edge-impulse-run-impulse` from a web page and display real-time classification results.

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate.bat on Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open browser:
```
http://localhost:5000/
```

Make sure your Arduino or Edge Impulse supported device is connected and accessible via CLI.
