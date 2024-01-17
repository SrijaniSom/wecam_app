import cv2
import asyncio
import base64
import websockets

async def send_video(websocket, path):
    video_path = 'Minecraft Death Swap 2 {Smarty VS Dreamboy}.mp4.crdownload'  # Replace with the path to your video file
    cap = cv2.VideoCapture(video_path)

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            # Convert frame to base64
            _, buffer = cv2.imencode('.jpg', frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')

            await websocket.send(frame_base64)
            await asyncio.sleep(0.05)  # Adjust the delay based on your desired frame rate

    finally:
        cap.release()

if __name__ == "__main__":
    start_server = websockets.serve(send_video, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever() 
