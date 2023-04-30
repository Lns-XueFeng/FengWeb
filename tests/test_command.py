from fengweb.extensions import db
from tests.base import BaseTest


class CommandTest(BaseTest):

    def setUp(self):
        super(CommandTest, self).setUp()
        db.drop_all()

    def test_initdb_cmd(self):
        result = self.runner.invoke(args=["initdb"])
        self.assertIn("初始化数据库", result.output)

    def test_initdb_cmd_drop(self):
        result = self.runner.invoke(args=["initdb", "--drop"], input="y\n")
        self.assertIn("此操作将会删除数据库, 是否继续？", result.output)
        self.assertIn("已删除", result.output)

    def test_forge_cmd(self):
        result = self.runner.invoke(args=["forge"])
        self.assertIn("生成ing 10 categories...", result.output)
        self.assertIn("生成ing 50 posts...", result.output)
        self.assertIn("生成ing links...", result.output)
        self.assertIn("生成ing name title about for notes...", result.output)
        self.assertIn("生成ing messages...", result.output)
        self.assertIn("生成完成", result.output)

    def test_forge_cmd_custom(self):
        result = self.runner.invoke(args=["forge", "--category", "5", "--post", "10"])
        self.assertIn("生成ing 5 categories...", result.output)
        self.assertIn("生成ing 10 posts...", result.output)
        self.assertIn("生成ing links...", result.output)
        self.assertIn("生成ing name title about for notes...", result.output)
        self.assertIn("生成ing messages...", result.output)
        self.assertIn("生成完成", result.output)

    def test_init_admin_cmd(self):
        result = self.runner.invoke(args=["init_admin", "--username", "XueFeng", "--password", "123456789"])
        self.assertIn("正在初始化数据库...", result.output)
        self.assertIn("创建管理员账户...", result.output)
        self.assertIn("创建默认分类...", result.output)
        self.assertIn("创建完成", result.output)

    def test_init_admin_cmd_update(self):
        self.runner.invoke(args=["init_admin", "--username", "XueFeng", "--password", "123456789"])
        result = self.runner.invoke(args=["init_admin", "--username", "XueXue", "--password", "123456789"])
        self.assertIn("正在初始化数据库...", result.output)
        self.assertIn("此管理员已存在, 更新ing...", result.output)
        self.assertIn("创建默认分类...", result.output)
        self.assertIn("创建完成", result.output)

