import xml.dom.minidom as dm

'''
创建步骤：
1.创建XML空白文档
2.产生根对象
3.向根对象中加入数据
4.将xml内存对象写入文件
'''
'''
#内存中创建一个新的文档
doc = dm.Document()
#创建根节点对象
root = doc.createElement("customer")
#给根节点添加属性
root.setAttribute("id", "001")
#将根节点添加到文件对象中
doc.appendChild(root)

#添加一个叶子节点
name = doc.createElement("name")
#给叶子节点设置一个文本节点，用于文本显示
name.appendChild(doc.createTextNode("lijian"))
root.appendChild(name)

phone = doc.createElement("phone")
phone.appendChild(doc.createTextNode("09231974"))
root.appendChild(phone)  #将叶子节点添加到父节点中

comment = doc.createElement("comments")
comment.appendChild(doc.createTextNode("singer"))
root.appendChild(comment)

file = open("creat.xml", "w", encoding="utf-8")
#将内存中xml写入文件
doc.writexml(file, indent="", addindent=" ", newl=" ", encoding="utf-8")
file.close()
'''
# #创建解释器
# tree = dm.parse("creat.xml")
# root = tree.documentElement  #获取文档的根元素
#
# #创建一个节点
# newc = tree.createElement("customer")
# newc.setAttribute("id", "002")
#
# name = tree.createElement("name")
# name.appendChild(tree.createTextNode("李太白"))
# root.appendChild(name)
#
# with open("creat.xml", "w+", encoding="utf-8") as f:
#     tree.writexml(f, addindent=" ", encoding="utf-8")


'''更新'''
tree = dm.parse("xmltest.xml")
root = tree.documentElement
years = root.getElementsByTagName("year")
print("years:", years)
#找到对应的节点并修改其值
for y in years:
    if y.childNodes[0].data =="1989" :
        print(y.childNodes[0].data)
        y.childNodes[0].data = "2020"

with open("xmltest.xml", "w+", encoding="utf-8") as f:
    tree.writexml(f, addindent=" ", encoding="utf-8")