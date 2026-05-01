import cv2
import mediapipe as mp
import json
import asyncio
import websockets

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        while True:
            cap = cv2.VideoCapture(0)
            success, frame = cap.read()

            if not success:
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = pose.process(rgb)

            if result.pose_landmarks:
                keypoints = []

                for idx, lm in enumerate(result.pose_landmarks.landmark):
                    keypoints.append({
                        "id": idx,
                        "x": lm.x,
                        "y": lm.y,
                        "z": lm.z,
                        "c": lm.visibility
                    })

                data = json.dumps({
                    "people": [{"id": 0, "keypoints": keypoints}]
                })

                for client in clients:
                    await client.send(data)

            await asyncio.sleep(0.03)

    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
