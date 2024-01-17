document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('videoFeed');

    if (!video) {
        console.error('Video element not found');
        return;
    }

    const videoPath = 'path/to/your/video.mp4';

    video.src = videoPath;
});
