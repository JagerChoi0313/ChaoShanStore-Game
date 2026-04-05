class ChaoShanStore:  #写一个store类
    def __init__(self,name):
        self.name="粿条大王"  #店名
        self.money=500      #初始资金
        self.reputation=0   #声望（决定客流量）
        self.level="地摊"    #当前阶段
        self.inventory={}   #食材库存

    #商店状态
    def show_status(self):
        print(f"\n---[{self.name}]经营状态---]")
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

    def buy_ingredient(self,item_name,price,quantity):
        total_cost=price*quantity
        if self.money >= total_cost:
            self.money -= total_cost

            #更新库存：如果食材已存在则累加，不存在则初始化
            self.inventory[item_name]=self.inventory.get(item_name,0)+quantity
            print(f"✅ 成功导入{quantity}份{item_name}!")
        else:
            print("❌ 钱不够了，去赚点钱再来吧!")



#--- 第二部分：真正开始玩（实例化）---

#实例化：找出一个对象
my_shop = ChaoShanStore("粿条大王")

#调用方法：让这个对象去买东西
my_shop.buy_ingredient("鸡翅",5,10)

#查看结果
my_shop.show_status()


