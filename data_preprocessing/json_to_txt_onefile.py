import json

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

file_path = "smartfarm/image/곤줄박이/라벨링데이터/상추/20201125_경기도_성남시_분당구_맑음_주간_실외_front_0025739.json"
f = open("smartfarm/image/곤줄박이/라벨링데이터/상추/20201125_경기도_성남시_분당구_맑음_주간_실외_front_0025739.txt", 'w')

with open(file_path, 'r', encoding='UTF-8') as file:
    data = json.load(file)
    annot = data["annotations"]

things = []
for i in range(len(annot)):
    annotp = annot[i]
    boundingbox = annotp["points"]
    b = boundingbox[0][0], boundingbox[2][0], boundingbox[0][1], boundingbox[2][1]
    label = annotp["label"]
    b = convert((1980,1080), b)
    f.write(f"{label, b}\n")
    things.append((label,b))
print(things)
f.close()


