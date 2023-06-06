import mandb
import menu

balance = 1000000   # 카드 잔액
rewards = 0         # 카드 적립금

# 적립금 쌓이면 쿠폰으로 교환하여 추가할 수 있게 하는 기능을 넣기(맥도날드 앱 참고)

def total_without_dc():
    costsum = 0
    sql = "SELECT * FROM orders"
    mandb.mc_cur.execute(sql)
    orderlist = mandb.mc_cur.fetchall()
    for order in orderlist:
        if order[4] is None:
            costsum += menu.getinfo("price", order[0]) * order[2]
        else:
            costsum += order[3] * order[2]
    return costsum