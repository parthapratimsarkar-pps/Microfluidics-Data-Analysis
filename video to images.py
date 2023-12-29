import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    """
    Extracts frames from a video.
    
    :param video_path: Path to the video file.
    :param output_folder: Folder to save the extracted frames.
    :param frame_rate: Extract every 'frame_rate' frames. Default is 1 (every frame).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture video
    video = cv2.VideoCapture(video_path)
    count = 0
    success = True

    while success:
        success, image = video.read()

        if not success:
            break

        if count % frame_rate == 0:
            frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(frame_path, image)

        count += 1

    video.release()
    cv2.destroyAllWindows()

# Converting video to images
video_path = 'D:\SUTD\Experiment (Partha)\80 microlitre per min (1-6).avi'  # Replace with your .avi video path
output_folder = 'D:\SUTD\Experiment (Partha)\Frames'     # Folder to save frames
frame_rate = 10                        # Extract every 10th frame

extract_frames(video_path, output_folder, frame_rate)
