from store import ChaoShanStore

#实例化
my_shop = ChaoShanStore("粿条大王")

# 1. 进货（现在不需要手动打价格了）
my_shop.buy_ingredient("鸡翅", 10)
my_shop.buy_ingredient("腐乳", 10)

# 2. 经营
my_shop.sell("腐乳鸡翅", 15)

# 3. 喝茶
my_shop.gongfu_tea_event()

# 4. 状态
my_shop.show_status()
