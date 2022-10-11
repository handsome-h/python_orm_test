from pymysql import connect


class JD(object):
    """
    京东商城
    """

    def __init__(self):
        """
        构造方法
        """
        self.conn = connect(host='182.92.221.214', port=3306, user='root', password='HB1q2w3e!@#', database='jing_dong',
                            charset='utf8')
        # 通过数据库连接对象创建游标对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        析构方法

        """
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def show_cates(self):
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)

    def show_brands(self):
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)

    def add_brands(self):
        item_name = input('输入新商品分类的名称:')
        sql = 'insert into goods_brands (name) values ("%s")' % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def update_brands(self):
        items_name_new = input('输入新品牌')
        items_name_old = input('输入被替换的品牌')
        sql = "update goods_brands set name = '%s' where name = '%s'" % (items_name_new, items_name_old)
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_brands(self):
        item_name = input('输入要删除商品分类的名称:')
        sql = "delete from goods_brands where name = '%s'" % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def select_goods(self):
        item_name = input('输入要查询的商品名字')
        sql = "select * from goods where name = '%s'" % item_name
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print('京东商城')
        print('1：所有的商品')
        print('2：所有的商品分类')
        print('3：所有的商品品牌分类')
        print('4：添加一个商品分类')
        print('5: 更新一个商品品牌')
        print('6:删除一个商品品牌')
        print('7:查询商品')
        return input('请输入功能对应的序号')

    def run(self):
        while True:
            num = self.print_menu()
            if num == '1':
                # 查询所有的商品
                self.show_all_items()
            elif num == '2':
                # 查询所有的商品分类
                self.show_cates()
            elif num == '3':
                # 查询所有的商品品牌分类
                self.show_brands()
            elif num == '4':
                self.add_brands()
            elif num == '5':
                self.update_brands()
            elif num == '6':
                self.delete_brands()
            elif num == '7':
                self.select_goods()
            else:
                print('输入有误，重新输入')


def main():
    # 创建一个京东对象
    jd = JD()
    # 调用这个对象的run方法
    jd.run()


if __name__ == '__main__':
    main()
