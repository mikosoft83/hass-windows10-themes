template = open("template.yaml").read().split("# card mod")

template_f_string = 'f"""' + template[0] + '"""'


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v


def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return (v, v, v)
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p, q, t = v * (1.0 - s), v * (1.0 - s * f), v * (1.0 - s * (1.0 - f))
    i %= 6
    if i == 0:
        return (v, t, p)
    if i == 1:
        return (q, v, p)
    if i == 2:
        return (p, v, t)
    if i == 3:
        return (p, q, v)
    if i == 4:
        return (t, p, v)
    if i == 5:
        return (v, p, q)


for mode in ["Dark", "Light"]:
    if mode == "Dark":
        primary_background_color = "rgb(26, 26, 26)"
        secondary_background_color = "rgb(38, 38, 38)"
        text_color = "rgb(250, 250, 250)"
        secondary_text_color = "rgb(200, 200, 200)"
    elif mode == "Light":
        primary_background_color = "rgb(255, 255, 255)"
        secondary_background_color = "rgb(243, 243, 243)"
        text_color = "rgb(0, 0, 0)"
        secondary_text_color = "rgb(100, 100, 100)"
    for theme_color_name, theme_color in {
        "Blue Gray": [105, 121, 126],
        "Brick Red": [209, 52, 56],
        "Camouflage": [126, 115, 95],
        "Camouflage Desert": [132, 117, 69],
        "Cool Blue": [45, 125, 154],
        "Cool Blue Bright": [0, 153, 188],
        "Default Blue": [0, 120, 215],
        "Gold": [255, 140, 0],
        "Gray": [122, 117, 116],
        "Gray Brown": [93, 90, 88],
        "Gray Dark": [74, 84, 89],
        "Green": [16, 124, 16],
        "Iris Pastel": [135, 100, 184],
        "Iris Spring": [116, 77, 169],
        "Liddy Green": [100, 124, 100],
        "Meadow Green": [73, 130, 5],
        "Metal Blue": [81, 92, 107],
        "Mint Dark": [1, 133, 116],
        "Mint Light": [0, 178, 148],
        "Mod Red": [255, 67, 67],
        "Moss": [72, 104, 96],
        "Navy Blue": [0, 99, 177],
        "Orange Bright": [247, 99, 12],
        "Orange Dark": [202, 80, 16],
        "Orchid": [154, 0, 137],
        "Orchid Light": [194, 57, 179],
        "Overcast": [104, 118, 138],
        "Pale Moss": [86, 124, 115],
        "Pale Red": [231, 72, 86],
        "Pale Rust": [239, 105, 80],
        "Plum": [191, 0, 119],
        "Plum Light": [227, 0, 140],
        "Purple Orchid": [154, 0, 137],
        "Purple Shadow": [142, 140, 216],
        "Purple Shadow Dark": [107, 105, 214],
        "Red": [232, 17, 35],
        "Rose": [195, 0, 82],
        "Rose Bright": [234, 0, 94],
        "Rust": [218, 59, 1],
        "Sage": [82, 94, 84],
        "Seafoam": [0, 183, 195],
        "Seafoam Teal": [3, 131, 135],
        "Sport Green": [16, 137, 62],
        "Steel Blue": [104, 118, 138],
        "Storm": [76, 74, 72],
        "Turf Green": [0, 204, 106],
        "Violet Red": [136, 23, 152],
        "Violet Red Light": [177, 70, 194],
        "Yellow Gold": [255, 185, 0],
    }.items():
        theme_name = f"Windows 10 {theme_color_name} - {mode}"
        primary_ui_color = [str(color) for color in theme_color]
        primary_ui_color = f"rgb({', '.join(primary_ui_color)})"
        h, s, v = rgb_to_hsv(*theme_color)
        light_primary_ui_color = [h, max(0, s - 5.0), min(100, v + 5.0)]
        light_primary_ui_color = list(hsv_to_rgb(*light_primary_ui_color))
        light_primary_ui_color = [round(color) for color in light_primary_ui_color]
        light_primary_ui_color = [str(color) for color in theme_color]
        light_primary_ui_color = f"rgb({', '.join(light_primary_ui_color)})"
        with open(fr".\themes\windows10\{theme_name.lower().replace(' ', '-')}.yaml", "w") as theme_file:
            theme_file.write(eval(template_f_string) + "# card mod" + template[1])
            print("Wrote to " + theme_file.name)
