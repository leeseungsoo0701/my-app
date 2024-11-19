import random

def rock_paper_scissors():
    선택지 = ['가위', '바위', '보']
    승리 = 0
    패배 = 0
    무승부 = 0
    
    while True:
        컴퓨터_선택 = random.choice(선택지)
        
        while True:
            사용자_선택 = input("가위, 바위, 보 중 하나를 선택하세요: ")
            if 사용자_선택 in 선택지:
                break
            print("잘못된 입력입니다. 다시 시도해주세요.")
        
        print(f"사용자: {사용자_선택}, 컴퓨터: {컴퓨터_선택}")
        
        if 사용자_선택 == 컴퓨터_선택:
            print("비겼습니다!")
            무승부 += 1
        elif (사용자_선택 == '가위' and 컴퓨터_선택 == '보') or \
             (사용자_선택 == '바위' and 컴퓨터_선택 == '가위') or \
             (사용자_선택 == '보' and 컴퓨터_선택 == '바위'):
            print("사용자가 이겼습니다!")
            승리 += 1
        else:
            print("컴퓨터가 이겼습니다!")
            패배 += 1
            
        계속하기 = input("게임을 계속하시겠습니까? (예/아니오): ")
        if 계속하기.lower() not in ['예', 'y', 'yes']:
            break
    
    print("\n===== 게임 결과 =====")
    print(f"승리: {승리}번")
    print(f"패배: {패배}번")
    print(f"무승부: {무승부}번")
    print(f"승률: {(승리/(승리+패배+무승부)*100):.1f}%")

if __name__ == "__main__":
    rock_paper_scissors()