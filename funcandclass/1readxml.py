from xml.dom import minidom

#打开xml文件
dom = minidom.parse("contact.xml")
#得到文档元素的对象
root = dom.documentElement
#打印每个节点都有的属性值
print(root.nodeName,root.nodeValue,root.nodeType,root.ELEMENT_NODE)

#通过标签名获取一组标签
tagName = root.getElementsByTagName("Name")
print(tagName[0].tagName)

#获取属性值
name = tagName[0].getAttribute("name")
print(name)

#获取第一个标签对的值
print(tagName[0].firstChild.data)