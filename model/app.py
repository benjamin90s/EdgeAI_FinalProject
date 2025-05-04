import subprocess
import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

# Full path to the executable
edge_impulse_path = r"C:\Users\Admin\AppData\Roaming\npm\edge-impulse-run-impulse.cmd"
# Explicit working directory (this can be omitted, as we're specifying the full executable path)
working_directory = r"C:\Users\Admin\AppData\Roaming\npm"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bird-classifier-secret-key'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", logger=True, engineio_logger=True)

def run_inference():
    print("Starting inference process...")

    process = subprocess.Popen(
        [edge_impulse_path],
        cwd=working_directory,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )
    
    # Read and emit output in real-time
    for line in process.stdout:
        line = line.strip()
        print(f"Captured: {line}")
        socketio.emit('inference_output', {'data': line}, namespace='/')
        socketio.sleep(0.01)  # Allow eventlet to process events

    # Once the inference is done, emit a final message
    socketio.emit('inference_output', {'data': 'Inference process completed.'}, namespace='/')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print(f"Client connected: {request.sid}")
    emit('connection_response', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")

@socketio.on('start_inference')
def start_inference():
    print(f"Received start_inference request from client: {request.sid}")
    emit('inference_output', {'data': 'Starting inference process...'})
    
    # Use socketio background task for better compatibility with eventlet
    socketio.start_background_task(run_inference)

if __name__ == '__main__':
    print("Starting server on http://0.0.0.0:5000")
    print(f"Edge Impulse executable: {os.path.exists(edge_impulse_path)}")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
