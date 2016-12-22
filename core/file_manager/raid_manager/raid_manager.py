#encoding: utf-8

#更新
def update():
    # 每当进行了文件操作或者查询操作的时候
    # 需要对系统的configuration文件进行操作

#此处为用于file_manager调用的接口
class controller:
    # 文件映射表
    # MD5码 | 分块信息（adaptor序号 - 块序号 - 块路径的键值对） | 修改时间 | 原文件大小 | 冗余比例 |
    #
    map = []
    recent_delete = []
    def __init__(self):
        # 检查系统运行根目录下是否存在文件块映射表 是：正常运行； 否： 创建
        # 登陆节点，检查是否有名为sys的目录，有则说明为之前的节点，没有则新建一个目录，并在该sys目录下新建一个以该设备名命名的文件夹
        # 检查sys目录下是否存在以该设备名命名的目录，如果有，则证明该设备之前曾经使用过
        # 检查        部分不用考虑
        ``
    def rsys_operation(self, device_name, op_code):
        pass
        # note 针对节点而言
        # 相应的设备目录下的系统配置文件操作
        # 下载配置文件的时候无文件映射表，需要有一定概率能在单一节点上恢复相应的文件，登录设备越多，概率越大
        # 无文件映射表的机制，仅针对配置文件，1. 系统文件冗余和其他文件相分离，2. 系统文件无文件映射机制


    def rfetch_devices(self):
        pass
        # note 针对节点而言
        # 返回sys目录下的所有的子目录的名字
        # 适用于恢复该设备的文件块映射表

    # 上传
    def rupload(self, name, priority = False):
        pass
        # 将分块文件上传到adapter之中
        # 获取到成功的反馈
        # 成功则将信息写入映射表
        # 优先级（priority）用于上传系统配置文件，高优先级传输时，提高冗余度

    # 下载
    def rdownload(self, name, priority = False):
        pass
        # 通过参数来查询相应的映射表
        # 获取adaptor数组
        # 从数组中取出相应数量的文件块
        # 组合成文件然后返回给file_manager模块

    # 查询信息
    def get_info(self):
        pass
        # node信息：node数量，每个node的容量
        # 为每个node建立一个deviceInfo文件，用来标识该设备的详细信息（类型，容量，可扩展性，读写速度预期），当新加入设备
        # 的时候需要对该文件更改。

    # 删除文件
    def rdiscard(self, path = '/', name, trash_bin):
        pass
    # 通过参数查询映射表
        # 检查是否开启回收站机制
        # 如果没有删除所有adapter上的文件块，并删除映射
        # 如果开启了，则将相应的记录移动到recent_discarded的字典中

    # 查错
    def check(self):
        pass

if __name__ == '__main__':
    #instance
