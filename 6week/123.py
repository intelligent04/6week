import sys
##### 앞으로는 확률과 통계 열심히 공부하겠습니다...

def facto(n):
    out = n
    for _ in range(1, n):
        out *= _
    if out == 0:
        out = 1
    return out

def combi(one, two=0, three=0, four=0, five=0, six=0, seven=0, eight=0, nine=0):
    return facto(one+two+three+four+five+six+eight+nine) / (facto(one) * facto(two) *facto(three) *facto(four) *facto(five) *facto(six) *facto(seven) *facto(eight) *facto(nine))

def simple(len):
    for i in range(1, len+ 1): 
            num += facto(len - i, i)

print(combi(3, 2))


t = int(sys.stdin.readline())
for i in range(t):
    num = 1 # 1+1+1+1... 이렇게 표현되는 경우의 수는 미리 더해놓고 시작
    a = int(sys.stdin.readline())
    for j in range(2,a): # j=3
        a_li = [j]
        while sum(a_li) < a: # a_li를 [3,1,1,1,1] 이런식으로 만듦
            a_li.append(1)
        len_a_li = len(a_li)
        simple(len_a_li) #[3,1,1,1,1,1,1], [3,3,1,1,1] , [3,3,3] 이렇게 3이 늘어나고 순서 섞이는 경우의 수 계산
        for k in range(1,a-1):
                                                                                #for i in range(1, len_a_li + 1): # i는 3의 개수를 의미
                                                                                    #num += facto(len_a_li - i, i) #[3,1,1,1,1,1,1], [3,3,1,1,1] , [3,3,3] 이렇게 3일 늘어나고 순서 섞이는 경우의 수 계산

        a_li[0] += 1

    """
    while sum(a_li) < a:
        a_li.append(1)
    len_a_li = len(a_li)
    """
