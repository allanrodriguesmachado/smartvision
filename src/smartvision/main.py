from smartvision.application.video_process import VideoProcess
from smartvision.infrastructure.video_file import VideoFile

def main() -> None:
    file = VideoFile("/app/videos/teste.mp4")
    file.connect()

    files = VideoProcess(file)
    files.process()

if __name__ == "__main__":
    main()