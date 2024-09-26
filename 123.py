from odfrw import OFDDocument

ofd_file = "C:\\19.ofd"

try:
    document = OFDDocument.load(ofd_file)
    print(f"成功读取文件: {ofd_file}")
    # 你可以在这里进一步处理文档内容
except Exception as e:
    print(f"读取文件时出错: {e}")
