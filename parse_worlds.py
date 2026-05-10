from pathlib import Path
import json
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

for s in Path.home().glob(".local/share/hosty/servers/*"):
    ld = s / "world" / "level.dat"
    if ld.exists():
        data = _read_nbt_file(ld)
        print(f"\n--- {s.name} ---")
        
        lower_map = {str(k).casefold(): v for k, v in data.items()}
        print("Keys:", list(data.keys()))
        
        wg = lower_map.get("worldgen") or lower_map.get("world_gen")
        if wg:
            print("Found worldgen!")
            print(json.dumps(explore(wg), indent=2))
        elif "worldgensettings" in lower_map:
            print("Found WorldGenSettings!")
            
        server_brands = lower_map.get("serverbrands")
        print("Brands:", server_brands)
