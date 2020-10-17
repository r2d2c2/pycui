import os
def user():
    inp=input('''
    0.취소
    1.사용자 추가
    2.그룹 추가
    3.사용자 제거
    4.그룹 제거
    5.그룹에 사용자 추가
    6.계정에 속한 그룹 조회
    7.비빌 번호 변경
    입력해주세요>''')
    if(inp=='2'):
        name=input("추가할 그룹의 이름을 입력 하세요")
        os.system("sudo groupadd  "+name)
    elif(inp=='5'):
        name=input("그룹에 추가할 사용자를 입력 하세요")
        nam=input('그룸의 이름울 입력 하세요')
        os.system('sudo adduser '+name+" "+nam)
    elif(inp=='3'):
        name=input('제거할 사용자 이름을 입력 하세요')
        os.system('sudo deluser --remove-home '+name)
    elif(inp=='4'):
        name=input("제거할 그룹 이름을 입력 하세요")
        os.system('sudo groupdel '+name)
    elif(inp=='0'):
        start()
    elif(inp=='1'):
        name=input("추가할 사용자를 입력하세요")
        os.system('sudo adduser '+name)
    elif(inp=='6'):
        name=input('그룹을 조회할 사용자의 이름을 입력 하세요')
        os.system('sudo groups '+name)
    elif(inp=='7'):
        name=input('비밀번호를 변경할 사용자의 이름을 입력하세요')
        os.system('sudo passwd '+name)
    else:
        print("잘못 입력 하였습니다.")


def start():
    inp = input('''
    0.종료 
    1.cpu온도 확인
    2.gpu온도 확인
    3.ip확인
    4.gpio확인
    5.업데이트
    6.웹 브라우저 
    7.사용자 관리
    8.라즈베리파이 관리
    9.초기 환경 설정
    10.한글 설정
    입력해주세요>''')
    if (inp == '1'):
        os.system('vcgencmd measure_temp')
    elif (inp == '2'):
        os.system('/opt/vc/bin/vcgencmd measure_temp')
    elif(inp == '3'):
        os.system('ifconfig')
    elif(inp == '0'):
        exit()
    elif(inp == '4'):
        os.system('pinout')
    elif(inp=='5'):
        os.system('sudo apt update -y')
        os.system('sudo apt upgrade -y')
        os.system('sudo apt-get update -y')
        os.system('sudo apt-get upgrade -y')
        os.system('sudo rpi-update -y')#펌웨어 업데이트
    elif(inp=='6'):
        os.system('sudo apt-get install w3m -y')
        os.system('w3m google.co.kr')
    elif(inp=='7'):
        user()
    elif(inp=='8'):
        os.system('sudo raspi-config')
    elif(inp=='9'):
        #os.system('chmod +x pycui.py')#실행 파일로 변경
        os.system('sudo cp pycui /usr/local/bin/')
        #os.system('sudo mv /usr/local/bin/pycui.py /usr/local/bin/pycui')
    elif(inp=='10'):
        os.system('sudo apt-get install ibus')
        os.system('sudo apt-get install ibus-hangul')
        os.system('sudo apt-get install fonts-unfonts-core')
    else:
        print("잘못 입력 하였습니다.")
    start()
start()
