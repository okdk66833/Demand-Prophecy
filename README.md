# 수평적 패턴의 수요 예측 프로그램
![스크린샷 2024-08-22 155740](https://github.com/user-attachments/assets/77a45b26-1f1a-4074-a6fd-400f33755c46)

## 개요
추세, 계절적 패턴, 주기적 패턴이 없는 수요를 통계적 기법으로 분석하는 프로그램입니다.

## 기능
1. 사용자로부터 월별 수요를 입력 받습니다. (모든 월을 입력할 필요는 없습니다.)
2. 사용자로부터 예측 방법을 선택 받습니다. (단순이동평균법/가중이동평균법/지수평활법/tensorflow)
3. 예측 방법에 따라 다음 달의 수요를 예측합니다.

## 상세
### 단순이동평균법 (Simple Moving Average Method)
- 공식: (최근 n기 수요의 합) / n = 다음 달의 예측치
- 최근 n기간의 평균 수요를 예측치로 이용하는 시계열 분석 기법

### 가중이동평균법 (Weighted Moving Average Method)
- 공식: (가중치1 * 수요1) + (가중치2 * 수요2) + ... + (가중치n * 수요n) = 다음 달의 예측치
- 조건: 각 가중치의 합은 1이며, 최근 수요에 더 높은 비중 부여
- 평균 계산에 사용하는 과거 실적치마다 다른 가중치를 부여하며, 가중치의 합은 1인 시계열 분석 기법
- 가중치는 사용자가 임의로 설정

### 지수평활법 (Exponential Smoothing Method)
- 공식: a * (이번 달 실적 수요) + (1 - a) * (이번 달 예측 수요) = 다음 달의 예측치
- 조건: 평활상수 a는 0과 1 사이 (즉, 가중치)
- 시계열의 평균을 계산할 때 최근 수요에 더 많은 가중치를 부과하는 발전된 형태의 가중이동평균법
### tensorflow ai 예측
- teonsorflow 모듈을 이용해 머신러닝을 통하여 미래의 수요 계측

## 요구 사항
- 모듈
```
CTkTable
tensorflow
numpy
matplotlib
customtkinter
pillow
```

## 기타
- 분류: 2024 대학교 프로젝트
