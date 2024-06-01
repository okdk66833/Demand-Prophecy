# 월별 실적 수요 입력
def makeDemands():
    demands = []
    i = 1
    print('월별 실적 수요를 입력하세요. (중단하려면 공백 입력)')
    while True:
        temp = input(f'{i}번째 실적 수요 입력:')
        if temp == '': # 공백 입력 시
            if i == 1: # 입력한 수요가 없을 시 재입력
                print('최소 1개의 수요를 입력해야 합니다. 다시 입력하세요.')
            else: # 입력 중단
                break
        else:
            temp = int(temp)
            if temp < 0: # 음수일 시 재입력
                print('0 이상의 값을 입력해야 합니다. 다시 입력하세요.')
            else: # 입력한 수요를 리스트에 추가하고 다음 수요 입력 
                demands.append(temp)
                i += 1
    return demands # 월별 실적 수요 반환

# 수요 예측 방법 선택
def makeMethod():
    print('사용할 수평적 수요 예측 방법의 번호를 입력하세요.')
    print('1. 단순이동평균법: 최근 n기간의 평균 수요를 예측치로 이용')
    print('2. 가중이동평균법: 평균 계산에 사용하는 과거 실적치마다 다른 가중치를 부여')
    print('3. 지수평활법: 최근 수요에 더 많은 가중치를 부과하는 가중이동평균법')
    while True:
        method = int(input('방법(1, 2, 3) 선택:'))
        if method != 1 and method != 2 and method != 3: # 방법이 아닐 시 재입력
            print('1, 2, 3 중에 하나를 입력해야 합니다. 다시 입력하세요.')
        else: # 방법 입력 시 입력 중단
            break
    return method # 수요 예측 방법 반환

# 수요 예측 계산
def demandProphecy(method, demands):
    if method == 1: # 단순이동평균법
        cal = sum(demands) / len(demands)
    elif method == 2: # 가중이동평균법
        print('각 수요의 가중치를 입력하세요. 가중치의 합은 1이 되어야 합니다.')
        while True:
            weight = []
            i = 1
            while i != len(demands) + 1:
                if i == len(demands): # 마지막 가중치 자동 계산
                    weight.append(abs(1 - sum(weight)))
                    i += 1
                else:
                    temp = float(input(f'{i}번째 가중치 입력:'))
                    if 0 < temp < 1: # 0과 1 사이의 가중치 입력 시 다음 가중치 입력
                        weight.append(temp)
                        i += 1
                    else: # 범위를 벗어난 가중치 입력 시 재입력
                        print('0과 1 사이의 값을 입력해야 합니다. 다시 입력하세요.')
            if sum(weight) > 1: # 가중치의 합이 1이 아닐 시 모든 가중치 재입력
                print('가중치의 합이 1을 초과했습니다. 다시 입력하세요.')
            else: # 가중치의 합이 1일 시 수요 예측 계산으로 넘어감
                break
        cal = 0
        for i in range(0, len(demands)):
            cal += weight[i] * demands[i]
    elif method == 3: # 지수평활법
        while True:
            weight = float(input('이번 달 수요의 가중치 입력:'))
            if 0 < weight < 1: # 0과 1 사이의 가중치 입력 시 중단
                break
            else: # 범위를 벗어난 가중치 입력 시 재입력
                print('0과 1 사이의 값을 입력해야 합니다. 다시 입력하세요.')
        while True:
            demandForecast = int(input('이번 달 예측 수요 입력:'))
            if demandForecast < 0: # 음수일 시 재입력
                print('0 이상의 값을 입력해야 합니다. 다시 입력하세요.')
            else:
                break
        cal = weight * demands[len(demands) - 1] + (1 - weight) * demandForecast
    return cal # 계산 결과 반환