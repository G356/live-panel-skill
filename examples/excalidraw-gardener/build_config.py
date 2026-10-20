#!/usr/bin/env python3
"""园丁 loop in the excalidraw view (Chinese): 4:5 (X) and 3:4 (小红书).
Content and figures from the gardener README (github.com/ythx-101/gardener, the author's own loop):
B 段最佳候选规则 30 题 10% -> 57%（没过 75% 线，一条没提）；C 段「审美」攒到 5 次后作者提前批准固化。
  python3 examples/excalidraw-gardener/build_config.py   -> config-4x5.json, config-3x4.json"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def build(preset):
    tall = preset == "3:4"
    SH = 1330 if tall else 1250
    Y = (lambda y: round(28 + y * 1.04)) if tall else (lambda y: y)

    def P(pts):
        return [[x, Y(y)] for x, y in pts]

    nodes = [
        dict(id="daily", t="每日复盘", sub="读完昨天全部对话", x=500, y=250, w=300, h=116, hue="blue", size=42, subSize=24),
        dict(id="A", t="A 成果", sub="每天最多 3 条", x=185, y=470, w=250, h=118, hue="green"),
        dict(id="B", t="B 失败模式", sub="被纠正、返工", x=500, y=470, w=250, h=118, hue="red"),
        dict(id="C", t="C 成功模式", sub="被夸、被拿去发", x=815, y=470, w=250, h=118, hue="yellow"),
        dict(id="test", t="loop 机实测", sub="合格率至少 75%\n且比无规则高 25 点", x=500, y=720, w=330, h=150, hue="blue"),
        dict(id="count", t="攒次数", sub="满 2 次：待固化\n满 6 次：已固化", x=838, y=720, w=250, h=150, hue="yellow"),
        dict(id="nod", t="青月点头", sub="人是闸门", x=680, y=952, w=250, h=112, hue="violet", size=40),
        dict(id="rule", t="写进常驻规矩", x=680, y=1146, w=320, h=100, hue="green", size=40),
    ]
    for n in nodes:
        n["y"] = Y(n["y"])
        n.setdefault("size", 36)
        n.setdefault("subSize", 26); n.setdefault("subC", "#495057")

    def E(id, f, t, fs, ts, bend=0.0, fo=0, to=0, **kw):
        return dict(id=id, **{"from": f}, to=t, fromSide=fs, toSide=ts, bend=bend, fromOff=fo, toOff=to, **kw)

    edges = [
        E("dA", "daily", "A", "bottom", "top", 0.08, fo=-0.62),
        E("dB", "daily", "B", "bottom", "top"),
        E("dC", "daily", "C", "bottom", "top", -0.08, fo=0.62),
        E("Bt", "B", "test", "bottom", "top"),
        E("Cc", "C", "count", "bottom", "top", 0, fo=0.18),
        E("tn", "test", "nod", "bottom", "top", 0.12, fo=0.45, to=-0.5),
        E("cn", "count", "nod", "bottom", "top", -0.12, fo=-0.4, to=0.5),
        E("nr", "nod", "rule", "bottom", "top"),
        dict(id="back", **{"from": "rule"}, to="daily", dashed=True,
             pts=P([[508, 1146], [150, 1112], [34, 760], [40, 430], [128, 270], [328, 250]]),
             label="第二天继续积累", labelAt=[108, Y(1010)], labelAlign="left", labelSize=28),
    ]
    steps = [
        ("daily", "dA", "读完昨天的对话", [500, Y(152)], "center"),
        ("daily", "dB", "记下被纠正的地方", [500, Y(152)], "center"),
        ("B", "Bt", "≥2 次才写候选规则", [522, Y(592)], "left"),
        ("test", None, "还差 18 个点", [450, Y(842)], "center"),
        ("daily", "dC", "记下被夸的地方", [500, Y(152)], "center"),
        ("C", "Cc", "按底层原则归类", [800, Y(592)], "right"),
        ("count", "cn", "审美攒到 5 次", [990, Y(842)], "right"),
        ("nod", "nr", "提前批准固化", [830, Y(952)], "left"),
        ("rule", "back", "明天开工就读", [902, Y(1060)], "center"),
    ]
    view = {
        "type": "view", "kind": "excalidraw", "space": [1000, SH], "period": 22.5, "t0": 8.7, "seed": 5,
        "boil": {"step": 0.125, "variants": 4, "amp": 0.6}, "noteSize": 29, "roughness": 1.35, "strokeWidth": 2.6,
        "texts": [
            {"t": "园丁 loop · 让 AI 每天复盘一次自己", "x": 500, "y": Y(62), "size": 50, "c": "ink", "weight": 0.6,
             "underline": {"hue": "yellow", "width": 16, "dy": 22, "tilt": -4}},
            {"t": "每天早上：\n复盘昨天", "x": 118, "y": Y(186), "size": 28, "c": "slate"},
            {"t": "跨天：\n验证 → 点头 → 固化", "x": 178, "y": Y(1196), "size": 26, "c": "sage"},
            {"t": "真实数据 · B 段", "x": 170, "y": Y(612), "size": 25, "c": "red"},
            {"t": "最佳候选规则，30 题", "x": 170, "y": Y(648), "size": 25, "c": "red"},
            {"t": "10% → 57%", "x": 170, "y": Y(700), "size": 42, "c": "red", "weight": 0.7},
            {"t": "没过 75% 线，一条没提", "x": 170, "y": Y(752), "size": 24, "c": "red"},
        ],
        "icons": [{"kind": "sprout", "x": 928, "y": Y(1124), "w": 84}, {"kind": "server", "x": 404, "y": Y(560), "w": 0}],
        "nodes": nodes, "edges": edges,
        "steps": [{"node": n, "edge": e, "note": t, "at": at, "align": al} for n, e, t, at, al in steps],
    }
    view["icons"] = [i for i in view["icons"] if i.get("w")]
    ch = 1440 if tall else 1500
    return {
        "meta": {"title": "园丁 loop（excalidraw 主题）", "lang": "zh-CN"},
        "canvas": {"preset": preset, "duration": 22.5, "fps": 30},
        "theme": {"preset": "light-pastel", "font": 'Excalifont, Xiaolai, "Noto Sans CJK SC", sans-serif',
                  "fonts": [{"family": "Excalifont", "src": "Excalifont-Regular-Latin.woff2", "weight": "400"},
                            {"family": "Xiaolai", "src": "Xiaolai-Regular.ttf", "weight": "400"}],
                  "colors": {"bg": "#ffffff", "muted": "#5c636b"}},
        "credit": {"text": "数据：园丁 README（B 段最佳候选 30 题 10%→57%，作者 loop 机实测；C 段「审美」攒到 5 次后作者提前批准）\n"
                           "门槛 2 / 6 次借自胡海岚团队 Science 2017 · 动效为示意 · live-panel excalidraw 主题",
                   "y": ch - 34, "size": 12.5, "lh": 16, "c": "#868e96", "font": '"Noto Sans CJK SC", sans-serif'},
        "elements": [view],
    }


if __name__ == "__main__":
    for preset, name in (("4:5", "config-4x5.json"), ("3:4", "config-3x4.json")):
        (HERE / name).write_text(json.dumps(build(preset), ensure_ascii=False, indent=1), encoding="utf-8")
        print("wrote", HERE / name)
