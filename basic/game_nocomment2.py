#1. 모듈 가져오기
import random #모듈가져오기
import time #시간


#2. 전역변수 정의
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = False
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')
cards = [ i+j for i in types for j in nums ]
score_table = dict()
for key in nums:score_table[ key ] = nums.index( key ) +1
# 트럼트 K는 패널티를 주어서 -5점이다
score_table[ 'K' ] = -5
#함수지역~

#3. 함수들 나열
#함수 지향적 프로그램은 반드시(대체적으로) 시작점이 존재한다
#시작점, 엔트리포인트!!
def main():
    step1()
    #26번의 gameTitle 과 step2()안의 gameTitle은 서로 다른변수다
    #그냥 편의상 이름만 동일하게 사용했다(이후 안고치기 위해)
    gameTitle=step2()
    step3()
    step4()
    step5()
    step6()
    step7()
    

def step1():
    print("Enjoy Custom Game world")

def step2():
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')        
        elif not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')        
        elif int(tmp)>9 or int(tmp)<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')        
        else:
            game_level = tmp
            break
     print('gameTitle', gameTitle)   
     #gameTitle은 절차적 코드에서는 그냥 사용해도 되나,
     #함수지향적으로 전개해서 함수 내부로 가면 지역변수가 된다
     #함수 밖에서 사용이 불가하므로, 값을 리턴하거나, 아예
     #전역 변수로 뺴야 한다

def step3():
    while True:
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            break
def step4():
   while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break
def step5():pass
def step6():pass
def step7():pass


#4. 프로그램 시작
#__name__이 변수는 그냥 사용이 가능하고, 값이 
#프로그램을 구동하는 방식에 따라 2가지로 변경된다
#1)python 파일명.py로 구동하면=>__name__=>'__main__'세팅된다
#2)누군가가 파일명. py를 가져와서 사용하면=>__name__=>'파일명'
print('__name__=>',__name__)
if __name__== '__main__':
  main()