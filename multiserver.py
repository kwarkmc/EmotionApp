from flask import Flask, request
from werkzeug.utils import secure_filename
from datetime import datetime
import pydub
from pipeLine import process_audio_files
import os


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    UPLOAD_FOLDER = 'm4a'
    file = request.files['file']
    filename = secure_filename(file.filename)

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    today = datetime.today().strftime('%y%m%d')

    foldername = os.path.join(os.getcwd(), today)
    os.makedirs(foldername, exist_ok=True)

    sound = pydub.AudioSegment.from_file(os.path.join(UPLOAD_FOLDER, filename))
    duration = len(sound)
    segment_length = 5000 # 5초

    if today in filename:
        for i, start_time in enumerate(range(0, duration, segment_length)):
          end_time = start_time + segment_length
          segment = sound[start_time:end_time]
          new_filename = f"{filename.split('.')[0]}_{i}.wav"
          segment.export(os.path.join(foldername, new_filename), format='wav')

    ret = process_audio_files()
    print(ret)
    return str(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
