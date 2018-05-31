import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pandas as pd


def diabete_status2016():
    non_smoke = [511011, 50812, 40109]
    cut_smoke = [131585, 22025, 18341]
    now_smoke = [175904, 23560, 20771]

    non_smoke2 = [6.6, 15.1]
    cut_smoke2 = [10.6, 23]
    now_smoke2 = [9.43, 20.1]

    # 그래프에 쓰일 데이터 프레임의 배열
    s_list = [['피우지 않는다', non_smoke[0], non_smoke[1], non_smoke[2]],
              ['피웠으나 끊었다', cut_smoke[0], cut_smoke[1], cut_smoke[2]],
              ['지금도 피운다', now_smoke[0], now_smoke[1], now_smoke[2]]]

    s_list2 = [['피우지 않는다', non_smoke2[0], non_smoke2[1]],
              ['피웠으나 끊었다', cut_smoke2[0], cut_smoke2[1]],
              ['지금도 피운다', now_smoke2[0], now_smoke2[1]]]

    # 판다를 이용해 배열을 데이터프레임화
    s_table = pd.DataFrame(s_list, columns=('흡연', '정상', '예비 당뇨', '당뇨 판정'))
    s_table2 = pd.DataFrame(s_list2, columns=('흡연', '당뇨 판정 %', '예비당뇨 + 당뇨 판정 %'))

    # 원형 그래프를 위한 설정
    df = pd.DataFrame({'당뇨 판정': (non_smoke2[0], cut_smoke2[0], now_smoke2[0]),
                       '예비당뇨 + 당뇨 판정': (non_smoke2[1], cut_smoke2[1], now_smoke2[1])},
                      index=['피우지 않는다', '피웠으나 끊었다', '지금도 피운다'])

    # 인덱스 정하기
    s_table = s_table.set_index('흡연')
    s_table2 = s_table2.set_index('흡연')

    # 만들어진 데이터프레임 보여주기
    print(s_table.head())
    print(s_table2.head())

    # 시각화되는 데이터의 특징
    s_table.plot(kind='bar', rot=0)
    s_table2.plot(kind='line', rot=0)
    df.plot.pie(subplots=True, figsize=(12, 6))


def diabete_status2015():
    non_smoke = [507096, 48611, 38247]
    cut_smoke = [137439, 21935, 22188]
    now_smoke = [38247, 18214, 19468]

    non_smoke2 = [6.0, 14.6]
    cut_smoke2 = [10.2, 22.6]
    now_smoke2 = [9.0, 19.2]

    # 그래프에 쓰일 데이터 프레임의 배열
    s_list = [['피우지 않는다', non_smoke[0], non_smoke[1], non_smoke[2]],
              ['피웠으나 끊었다', cut_smoke[0], cut_smoke[1], cut_smoke[2]],
              ['지금도 피운다', now_smoke[0], now_smoke[1], now_smoke[2]]]

    s_list2 = [['피우지 않는다', non_smoke2[0], non_smoke2[1]],
               ['피웠으나 끊었다', cut_smoke2[0], cut_smoke2[1]],
               ['지금도 피운다', now_smoke2[0], now_smoke2[1]]]

    # 판다를 이용해 배열을 데이터프레임화
    s_table = pd.DataFrame(s_list, columns=('흡연', '정상', '예비 당뇨', '당뇨 판정'))
    s_table2 = pd.DataFrame(s_list2, columns=('흡연', '당뇨 판정 %', '예비당뇨 + 당뇨 판정 %'))

    # 원형 그래프를 위한 설정
    df = pd.DataFrame({'당뇨 판정': (non_smoke2[0], cut_smoke2[0], now_smoke2[0]),
                       '예비당뇨 + 당뇨 판정': (non_smoke2[1], cut_smoke2[1], now_smoke2[1])},
                      index=['피우지 않는다', '피웠으나 끊었다', '지금도 피운다'])

    # 인덱스 정하기
    s_table = s_table.set_index('흡연')
    s_table2 = s_table2.set_index('흡연')

    # 만들어진 데이터프레임 보여주기
    print(s_table.head())
    print(s_table2.head())

    # 시각화되는 데이터의 특징
    s_table.plot(kind='bar', rot=0)
    s_table2.plot(kind='line', rot=0)
    df.plot.pie(subplots=True, figsize=(12, 6))


def diabete_status2014():
    non_smoke = [512101, 47389, 36706]
    cut_smoke = [127827, 19307, 15619]
    now_smoke = [19186, 23215, 19978]

    non_smoke2 = [6.1, 14.1]
    cut_smoke2 = [9.5, 21.4]
    now_smoke2 = [8.5, 18.4]

    # 그래프에 쓰일 데이터 프레임의 배열
    s_list = [['피우지 않는다', non_smoke[0], non_smoke[1], non_smoke[2]],
              ['피웠으나 끊었다', cut_smoke[0], cut_smoke[1], cut_smoke[2]],
              ['지금도 피운다', now_smoke[0], now_smoke[1], now_smoke[2]]]

    s_list2 = [['피우지 않는다', non_smoke2[0], non_smoke2[1]],
               ['피웠으나 끊었다', cut_smoke2[0], cut_smoke2[1]],
               ['지금도 피운다', now_smoke2[0], now_smoke2[1]]]

    # 판다를 이용해 배열을 데이터프레임화
    s_table = pd.DataFrame(s_list, columns=('흡연', '정상', '예비 당뇨', '당뇨 판정'))
    s_table2 = pd.DataFrame(s_list2, columns=('흡연', '당뇨 판정 %', '예비당뇨 + 당뇨 판정 %'))

    # 원형 그래프를 위한 설정
    df = pd.DataFrame({'당뇨 판정': (non_smoke2[0], cut_smoke2[0], now_smoke2[0]),
                       '예비당뇨 + 당뇨 판정': (non_smoke2[1], cut_smoke2[1], now_smoke2[1])},
                      index=['피우지 않는다', '피웠으나 끊었다', '지금도 피운다'])

    # 인덱스 정하기
    s_table = s_table.set_index('흡연')
    s_table2 = s_table2.set_index('흡연')

    # 만들어진 데이터프레임 보여주기
    print(s_table.head())
    print(s_table2.head())

    # 시각화되는 데이터의 특징
    s_table.plot(kind='bar', rot=0)
    s_table2.plot(kind='line', rot=0)
    df.plot.pie(subplots=True, figsize=(12, 6))


def cholesterol_status2016():
    non_smoke = [345291, 186137, 74137]
    cut_smoke = [96369, 54953, 21334]
    now_smoke = [122829, 70425, 28270]

    non_smoke2 = [12.2, 42.9]
    cut_smoke2 = [12.3, 44.1]
    now_smoke2 = [12.7, 44.5]

    # 그래프에 쓰일 데이터 프레임의 배열
    s_list = [['피우지 않는다', non_smoke[0], non_smoke[1], non_smoke[2]],
              ['피웠으나 끊었다', cut_smoke[0], cut_smoke[1], cut_smoke[2]],
              ['지금도 피운다', now_smoke[0], now_smoke[1], now_smoke[2]]]

    s_list2 = [['피우지 않는다', non_smoke2[0], non_smoke2[1]],
               ['피웠으나 끊었다', cut_smoke2[0], cut_smoke2[1]],
               ['지금도 피운다', now_smoke2[0], now_smoke2[1]]]

    # 판다를 이용해 배열을 데이터프레임화
    s_table = pd.DataFrame(s_list, columns=('흡연', '정상', '경계', '고혈증'))
    s_table2 = pd.DataFrame(s_list2, columns=('흡연', '고혈증 %', '경계 + 고혈증 %'))

    # 원형 그래프를 위한 설정
    df = pd.DataFrame({'고혈증': (non_smoke2[0], cut_smoke2[0], now_smoke2[0]),
                       '경계 + 고혈증': (non_smoke2[1], cut_smoke2[1], now_smoke2[1])},
                      index=['피우지 않는다', '피웠으나 끊었다', '지금도 피운다'])

    # 인덱스 정하기
    s_table = s_table.set_index('흡연')
    s_table2 = s_table2.set_index('흡연')

    # 만들어진 데이터프레임 보여주기
    print(s_table.head())
    print(s_table2.head())

    # 시각화되는 데이터의 특징
    s_table.plot(kind='bar', rot=0)
    s_table2.plot(kind='line', rot=0)
    df.plot.pie(subplots=True, figsize=(12, 6))


def cholesterol_status2015():
    non_smoke = [353007, 181436, 68835]
    cut_smoke = [101327, 56120, 20874]
    now_smoke = [123468, 68329, 26198]

    non_smoke2 = [11.4, 41.4]
    cut_smoke2 = [11.7, 43.1]
    now_smoke2 = [12.0, 43.3]

    # 그래프에 쓰일 데이터 프레임의 배열
    s_list = [['피우지 않는다', non_smoke[0], non_smoke[1], non_smoke[2]],
              ['피웠으나 끊었다', cut_smoke[0], cut_smoke[1], cut_smoke[2]],
              ['지금도 피운다', now_smoke[0], now_smoke[1], now_smoke[2]]]

    s_list2 = [['피우지 않는다', non_smoke2[0], non_smoke2[1]],
               ['피웠으나 끊었다', cut_smoke2[0], cut_smoke2[1]],
               ['지금도 피운다', now_smoke2[0], now_smoke2[1]]]

    # 판다를 이용해 배열을 데이터프레임화
    s_table = pd.DataFrame(s_list, columns=('흡연', '정상', '경계', '고혈증'))
    s_table2 = pd.DataFrame(s_list2, columns=('흡연', '고혈증 %', '경계 + 고혈증 %'))

    # 원형 그래프를 위한 설정
    df = pd.DataFrame({'고혈증': (non_smoke2[0], cut_smoke2[0], now_smoke2[0]),
                        '경계 + 고혈증': (non_smoke2[1], cut_smoke2[1], now_smoke2[1])},
                        index=['피우지 않는다', '피웠으나 끊었다', '지금도 피운다'])

    # 인덱스 정하기
    s_table = s_table.set_index('흡연')
    s_table2 = s_table2.set_index('흡연')

    # 만들어진 데이터프레임 보여주기
    print(s_table.head())
    print(s_table2.head())

    # 시각화되는 데이터의 특징
    s_table.plot(kind='bar', rot=0)
    s_table2.plot(kind='line', rot=0)
    df.plot.pie(subplots=True, figsize=(12, 6))


def cholesterol_status2014():
    non_smoke = [356462, 178407, 65214]
    cut_smoke = [94965, 50656, 17889]
    now_smoke = [137041, 72296, 26681]

    non_smoke2 = [10.8, 40.5]
    cut_smoke2 = [10.9, 41.9]
    now_smoke2 = [11.3, 41.9]

    # 그래프에 쓰일 데이터 프레임의 배열
    s_list = [['피우지 않는다', non_smoke[0], non_smoke[1], non_smoke[2]],
              ['피웠으나 끊었다', cut_smoke[0], cut_smoke[1], cut_smoke[2]],
              ['지금도 피운다', now_smoke[0], now_smoke[1], now_smoke[2]]]

    s_list2 = [['피우지 않는다', non_smoke2[0], non_smoke2[1]],
               ['피웠으나 끊었다', cut_smoke2[0], cut_smoke2[1]],
               ['지금도 피운다', now_smoke2[0], now_smoke2[1]]]

    # 판다를 이용해 배열을 데이터프레임화
    s_table = pd.DataFrame(s_list, columns=('흡연', '정상', '경계', '고혈증'))
    s_table2 = pd.DataFrame(s_list2, columns=('흡연', '고혈증 %', '경계 + 고혈증 %'))

    # 원형 그래프를 위한 설정
    df = pd.DataFrame({'고혈증': (non_smoke2[0], cut_smoke2[0], now_smoke2[0]),
                       '경계 + 고혈증': (non_smoke2[1], cut_smoke2[1], now_smoke2[1])},
                      index=['피우지 않는다', '피웠으나 끊었다', '지금도 피운다'])

    # 인덱스 정하기
    s_table = s_table.set_index('흡연')
    s_table2 = s_table2.set_index('흡연')

    # 만들어진 데이터프레임 보여주기
    print(s_table.head())
    print(s_table2.head())

    # 시각화되는 데이터의 특징
    s_table.plot(kind='bar', rot=0)
    s_table2.plot(kind='line', rot=0)
    df.plot.pie(subplots=True, figsize=(12, 6))

# 메인 함수
if __name__ == "__main__":
    # 그래프에 쓰일 폰트지정(나눔고딕)
    font_location = "C:/Windows/Fonts/NanumGothic.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)
    # 연도별 혈당
    diabete_status2016()
    diabete_status2015()
    diabete_status2014()
    # 연도별 콜레스테롤 수치
    cholesterol_status2016()
    cholesterol_status2015()
    cholesterol_status2014()

    plt.show()
