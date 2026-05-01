extends Node3D

var joints = {}

func update_skeleton(keypoints):
    for p in keypoints:
        var name = str(p["id"])
        var pos = Vector3(
            (p["x"] - 0.5) * 5,
            -(p["y"] - 0.5) * 5,
            -p["z"] * 5
        )

        if not joints.has(name):
            var joint = MeshInstance3D.new()
            add_child(joint)
            joints[name] = joint

        joints[name].position = pos
