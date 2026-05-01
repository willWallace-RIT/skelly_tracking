# Godot Human Skeleton Tracking

Real-time human pose detection streamed into Godot as a 3D skeleton.

## Pipeline
Camera → MediaPipe Pose → WebSocket → Godot Skeleton Rig

## Features
- Real-time pose detection
- WebSocket streaming bridge
- 3D skeleton rendering in Godot

## Run

### 1. Start backend
```bash
python ml_backend/pose_server.py

NOTE CURRENTLY NEEDs A main PROJ
