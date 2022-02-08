import csv

def show_profit(data):
    name = data[0] # 종목명
    purchase_price = int(data[1]) # 매입가격
    amount = int(data[2]) # 수량
    target_price = int(data[3]) # 목표가

    profit = (target_price - purchase_price) * amount # 수익금
    profit_ratio = (target_price/purchase_price - 1) * 100 # 수익률

    print(f"{name} 수익금 : {profit}원 수익률 : {profit_ratio:.2f}%")


file = open("./myvenv/Chapter10/mystock.csv", "r", encoding="utf-8-sig")

reader = list(csv.reader(file))

for data in reader[1:]:
    show_profit(data)

file.close()

# 수익금 = (목표가 - 매입가) * 수량
# 수익률 = (목표가/매입가-1) * 100