#/workspaces/testpython/VideoForImg/actress.jpg
#/workspaces/testpython/VideoForImg/actress.jpg

import cv2
import os

def create_video_from_image(image_path, output_path, duration=5, fps=30):
    """
    Generates a video clip from a single image.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the output video file.
        duration (int): Duration of the video in seconds.
        fps (int): Frames per second of the video.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")

    height, width, _ = img.shape
    size = (width, height)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, size)

    num_frames = int(duration * fps)
    for _ in range(num_frames):
        out.write(img)
    
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")

if __name__ == "__main__":
    image_file = "actress.jpg" 
    video_file = "video_from_photo.mp4"
    try:
        create_video_from_image(image_file, video_file)
    except FileNotFoundError as e:
        print(e)

'''
opencv-contrib-python==4.11.0.86
opencv-contrib-python-headless==4.11.0.86
opencv-python==4.11.0.86
'''
