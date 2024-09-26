from easyofd.ofd import OFD

# 读取OFD文件
ofd = OFD()
ofd.read('example.ofd')
2. 转换OFD到PDF：
# 将OFD转换为PDF
pdf_bytes = ofd.to_pdf()
with open('output.pdf', 'wb') as pdf_file:
    pdf_file.write(pdf_bytes)
3. 转换OFD到图片：
# 将OFD转换为图片
images = ofd.to_img()
for i, image in enumerate(images):
    image.save(f'page_{i}.png', 'PNG')
4. 提取OFD文本：
# 提取OFD文本内容
text = ofd.get_text()
print(text)
5. 提取OFD中的图片：
# 提取OFD中的图片
images = ofd.get_images()
for i, image in enumerate(images):
    image.save(f'page_{i}.png', 'PNG')
6. 清除OFD解析数据：
# 清除OFD解析数据
ofd.del_data()