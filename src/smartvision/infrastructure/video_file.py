import cv2

from smartvision.domain.interface.video_source import VideoSource

class VideoFile(VideoSource):
    def __init__ (self, path: str) -> None:
        self.path = path
        self.capture = None

    def connect(self) -> None:
        self.capture = cv2.VideoCapture(self.path)
        if not self.capture.isOpened():
            self.capture.release()
            self.capture = None
            raise RuntimeError(f'Failed to open video file: {self.path}')
        print(f"Connected to video file: {self.path}")

    def disconnect(self) -> None:
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            print(f"Disconnected from video file: {self.path}")

    def read_frame(self):
        if self.capture is None:
            raise RuntimeError(f'Failed to open video file: {self.path}')
        success, frame = self.capture.read()

        if not success:
            return None
        return frame