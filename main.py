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

    #烹饪逻辑
    #在潮汕小吃店里，我们要把“原材料”变成“商品”
    #逻辑规则：制作一份“腐乳鸡翅”,需要消耗1份鸡翅和1份腐乳
    #检查机制:如果库存里没有足够的材料，就不能开火
    def cook(self,dish_name):
        #定义配方：制作腐乳鸡翅
        if dish_name == "腐乳鸡翅":
            #检查材料是否足够
            wings = self.inventory.get("鸡翅",0)
            fermented_tofu = self.inventory.get("腐乳",0)

            if wings >= 1 and fermented_tofu >= 1:

                #消耗食材
                self.inventory["鸡翅"]-=1
                self.inventory["腐乳"]-=1
                print(f"滋啦！ 一份香喷喷的[{dish_name}]出炉了")
                return True     #return True表示制作成功

            else:
                print(f"NO! 食材不足，做不成[{dish_name}]")
                return False

    def sell(self,dish_name,price):
        print(f"\n🔔 [前台]：有客人点了一份[{dish_name}]")

        #调用之前的烹饪逻辑
        #如果cook返回True，说明饭做好了可以收钱
        if self.cook(dish_name):
            self.money += price
            self.reputation += 2    #卖出一份，品牌声誉加2
            print(f"[系统]：收银成功！收入{price}元")
            print(f"[系统]：品牌声望提升了！")
        else:
            print(f"[前台]:不好意思，食材不够，没法卖")
#--- 第二部分：真正开始玩（实例化）---

#实例化：找出一个对象
my_shop = ChaoShanStore("粿条大王")

#调用方法：让这个对象去买东西
my_shop.buy_ingredient("鸡翅",5,10)

my_shop.sell("腐乳鸡翅",15)
my_shop.sell("腐乳鸡翅",15)

# 查看结果
my_shop.show_status()

# 测试1：买了腐乳再做鸡翅
# my_shop.buy_ingredient("腐乳",2,5)
# my_shop.cook("腐乳鸡翅")

# 测试2：没买腐乳直接做鸡翅
# my_shop.cook("腐乳鸡翅")