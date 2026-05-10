import json
from pathlib import Path
from hosty.shared.utils.nbt_utils import _read_nbt_file

def explore(node, depth=0):
    if depth > 4:
        return "..."
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if isinstance(v, (dict, list)):
                out[k] = explore(v, depth+1)
            else:
                out[k] = v
        return out
    if isinstance(node, list):
        if len(node) > 2:
            return [explore(node[0], depth+1), explore(node[1], depth+1), f"... ({len(node)-2} more)"]
        return [explore(i, depth+1) for i in node]
    return node

data = _read_nbt_file(Path('/home/sugarycandybar/.local/share/hosty/servers/a309fc3a-9959-44fd-9abe-8837ca2d87a5/world/data/minecraft/world_gen_settings.dat'))
if data:
    print("Keys:", list(data.keys()))
    print(json.dumps(explore(data), indent=2))
else:
    print("Failed to read NBT")
