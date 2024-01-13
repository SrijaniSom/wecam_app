document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('videoFeed');

    // Using navigator.mediaDevices to access the user's camera
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((error) => {
            console.error('Error accessing the camera:', error);
        });
});
