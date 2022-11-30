import json
import PIL

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

nums = range(453,533) # 파일 전체 범위 설정
for num in nums:
    try:  # 예외처리
        file_path = f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/라벨링데이터/상추/09_20201228_2018{num}.json"  # 해당 json 파일 복사
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            images_im = data["images"]
            images_im2 = images_im[0]
            pl_step = images_im2["pl_step"]
            annot = data["annotations"]
            things = []

        f = open(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", 'w')  # 해당 json 정보를 저장할 txt 파일 생성
        for i in range(len(annot)):  # 이미지 내 모든 객체의 정보를 추출
            annotp = annot[i]
            bbox = annotp["bbox"]
            b = bbox[0], bbox[2], bbox[1], bbox[3]

            image = PIL.Image.open(
                f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/images/상추/09_20201228_2018{num}.JPG")  # 해당 이미지 사이즈 확인
            width, height = image.size

            boundingbox = convert((width, height), b)  # 위에서 선언한 convert()함수 적용
            f.write(f"{pl_step, boundingbox}\n")
            things.append((pl_step, boundingbox))
        print(things)
        f.close()
    except FileNotFoundError:
        pass
