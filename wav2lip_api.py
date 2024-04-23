from flask import Flask, request

app = Flask(__name__)

@app.route('/wav2lip', methods=['POST'])
def process_wav2lip():
    video_file = request.files['video']
    audio_file = request.files['audio']
    checkpoint_path = "content\Wav2Lip\checkpoints\wav2lip_gan.pth"
    final_output_directory = "content\wav2lip_output.mp4"
    inferenc.convert(audio_file, video_file, checkpoint_path, final_output_directory)
    
    return "Wav2lip processing completed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
