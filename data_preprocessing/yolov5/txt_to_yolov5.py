# ''' 파일을 read 하여 리스트에 저장하고, 그 리스트에 있는 문자열을 골라서 삭제 '''
#
# with open("2020-02-059.차량사람및영상_sample/sampleTxt/20201125_경기도_성남시_분당구_맑음_주간_실외_front_0025739.txt", "r") as f:
#     lines = f.readlines()
# with open("2020-02-059.차량사람및영상_sample/sampleTxt/20201125_경기도_성남시_분당구_맑음_주간_실외_front_0025739.txt", "w") as f:
#     for line in lines:
#         line.replace("(","")
#         line.replace(")","")
#         line.replace("'","")
#         f.write(line)

def replace_in_file(file_path, old_str, new_str):
    # 파일 읽어들이기
    fr = open(file_path, 'r')
    lines = fr.readlines()
    fr.close()

    # old_str -> new_str 치환
    fw = open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(old_str, new_str))
    fw.close()

nums = range(453,533) # 파일 전체 범위 설정
for num in nums:
    try:
        # 호출: file1.txt 파일에서 특수문자 없애기
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", "(", "")
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", ")", "")
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", "'", "")
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", ",", "")

        # 호출: file1.txt 파일에서 label 변환하기
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", "생육기", "0")
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", "개화기", "1")
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", "착화기", "1")
        replace_in_file(f"C:/Users/ss/PycharmProjects/pythonProject/smartfarm/image/곤줄박이/sampleTxt/09_20201228_2018{num}.txt", "수확기", "2")
    except FileNotFoundError:
        pass



