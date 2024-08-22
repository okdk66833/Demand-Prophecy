def demandProphecy(method, demands, weight, demandForecast):
    if method == 1: # 단순이동평균법
        cal = sum(demands) / len(demands)
    elif method == 2: # 가중이동평균법
        #print('각 수요의 가중치를 입력하세요. 가중치의 합은 1이 되어야 합니다.')
        # while True:
        #     weight = []
        #     i = 1
        #     while i != len(demands) + 1:
        #         if i == len(demands): # 마지막 가중치 자동 계산
        #             weight.append(abs(1 - sum(weight)))
        #             i += 1
        #         else:
        #             temp = float(input(f'{i}번째 가중치 입력:'))
        #             if 0 < temp < 1: # 0과 1 사이의 가중치 입력 시 다음 가중치 입력
        #                 weight.append(temp)
        #                 i += 1
        #             else: # 범위를 벗어난 가중치 입력 시 재입력
        #                 print('0과 1 사이의 값을 입력해야 합니다. 다시 입력하세요.')
        #     if sum(weight) > 1: # 가중치의 합이 1이 아닐 시 모든 가중치 재입력
        #         print('가중치의 합이 1을 초과했습니다. 다시 입력하세요.')
        #     else: # 가중치의 합이 1일 시 수요 예측 계산으로 넘어감
        #         break
        cal = 0
        for i in range(0, len(demands)):
            cal += weight[i] * demands[i]
    elif method == 3: # 지수평활법
        # while True:
        #     weight = float(input('이번 달 수요의 가중치 입력:'))
        #     if 0 < weight < 1: # 0과 1 사이의 가중치 입력 시 중단
        #         break
        #     else: # 범위를 벗어난 가중치 입력 시 재입력
        #         print('0과 1 사이의 값을 입력해야 합니다. 다시 입력하세요.')
        # while True:
        #     demandForecast = int(input('이번 달 예측 수요 입력:'))
        #     if demandForecast < 0: # 음수일 시 재입력
        #         print('0 이상의 값을 입력해야 합니다. 다시 입력하세요.')
        #     else:
        #         break
        cal = weight[len(weight)-1] * demands[len(demands) - 1] + (1 - weight[len(weight)-1]) * demandForecast
    return cal # 계산 결과 반환