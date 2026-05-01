extends Node

var ws = WebSocketPeer.new()
@onready var skeleton = $"../Skeleton"

func _ready():
    ws.connect_to_url("ws://localhost:8766")

func _process(_delta):
    ws.poll()

    while ws.get_available_packet_count() > 0:
        var msg = ws.get_packet().get_string_from_utf8()
        var data = JSON.parse_string(msg)

        if data:
            skeleton.update_skeleton(data["people"][0]["keypoints"])
