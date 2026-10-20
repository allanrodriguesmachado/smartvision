from smartvision.domain.interface.video_source import VideoSource

class VideoProcess:
    def __init__(self, source: VideoSource) -> None:
        self.source = source

    def process(self):
        frames_processed = 0

        try:
            self.source.connect()

            while True:
                frame = self.source.read_frame()

                if frame is None:
                    break
                frames_processed += 1
            print(f"Total frames processed: {frames_processed}")
        finally:
            self.source.disconnect()