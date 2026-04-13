import random
from ingredients import PRICES,RECIPES

class ChaoShanStore:  #写一个store类
    def __init__(self,name):
        self.name=name  #店名
        self.money=500      #初始资金
        self.reputation=0   #声望（决定客流量）
        self.level="地摊"    #当前阶段
        self.inventory={}   #食材库存

    #商店状态
    def show_status(self):
        print(f"\n---[{self.name}]经营状态---")
        print(f"\n当前资金：{self.money}元")
        print(f"\n品牌等级:{self.level}")
        print(f"\n品牌声望:{self.reputation}")

        print("---仓库库存---")
        if not self.inventory:
            print("仓库空空如也...")
        for item,count in self.inventory.items():
            print(f"-{item}:{count}份")
        print("------------------------")

    #进货系统
    #钱都不够不可以白嫖
    #库存更新（买了之后inventory里的数量要增加）

    def buy_ingredient(self,item_name,quantity):
        price = PRICES.get(item_name,0)     #自动从配置中取价
        if price == 0:
            print(f"市场上没有{item_name}")
            return

        total_cost = quantity * price
        if self.money >= total_cost:
            self.money -= total_cost

            #更新库存：如果食材已存在则累加，不存在则初始化
            self.inventory[item_name]=self.inventory.get(item_name,0)+quantity
            print(f"✅ 成功导入{quantity}份{item_name}!")
        else:
            print("❌ 钱不够了，去赚点钱再来吧!")

    #烹饪逻辑
    #改装为通用型，支持所有的RECIPE的菜
    def cook(self,dish_name):
        recipe = RECIPES.get(dish_name)
        if not recipe:
            print(f"🤔 店里还没研发出[{dish_name}")
            return False

        #检查所有所需材料
        for ingredient,amount in recipe.items():
            if self.inventory.get(ingredient,0)<amount:
                print(f"NO! 缺少{ingredient},做不成[{dish_name}]")
                return False

        #2.只有材料都够，才统一扣除
        for ingredient ,amount in recipe.items():
            self.inventory[ingredient]-=amount

        print(f"滋啦！ 一份香喷喷的[{dish_name}]出炉了")
        return True

    def sell(self,dish_name,price):
        print(f"\n🔔 [前台]：有客人点了一份[{dish_name}]")

        #调用之前的烹饪逻辑
        #如果cook返回True，说明饭做好了可以收钱
        if self.cook(dish_name):
            self.money += price
            self.reputation += 2    #卖出一份，品牌声誉加2
            print(f"[系统]：收银成功！,卖出一份{dish_name},收入{price}元")
            print(f"[系统]：品牌声望提升了！")
        else:
            print(f"[前台]:不好意思，食材不够，没法卖")

    def gongfu_tea_event(self):
        print(f"\n🍵 [茶桌]：{self.name} 摆开了工夫茶...")
        event_type = random.randint(1,3)
        if event_type == 1:
            print("🌟 一位老华侨留下了 100 元赞助款！")
            self.money += 100
        elif event_type == 2:
            print("📊 一位美食家竖起大拇指，声望+10！")
            self.reputation += 10
        else:
            print("只是平淡地喝了会茶")

