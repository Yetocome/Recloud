"""
- 块表（块号，存储节点号，存储节点文件号）
- 文件表（文件名，文件号，块号集合）

块表和文件表包含的是每个用户的文件信息和存储方式。
以类的形式封装起来，每当用户登陆，生成类的对象。
"""

class BlockTable(object):

    def __init__(self):
        #从远端加载块表
