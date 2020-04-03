import xml.dom.minidom as dm

#dom解析器打开xml文档，并解析为dom文档
# domTree = dm.parse("xmltest.xml")

# #获取xml文档对象，拿到dom树的根
# countryList = domTree.documentElement
# #print("读取xml文档的内容\n",countryList.toxml())
# print("读取xml文件的最后一个子节点：", countryList.lastChild)
# print("读取xml文件的第一个子节点：", countryList.firstChild)
# # print("获取country节点的list地址：", countryList.getElementsByTagName("country"))
# countrys = countryList.getElementsByTagName("country")
# for ct in countrys:
#     print("*********countrys***********")
#     for node in ct.childNodes:
#         print("name %s -- value %s --- type %s"%(node.nodeName, node.nodeValue, node.nodeType))

'''读取xml文件并写入excel'''
#创建解释器
domTree = dm.parse("xmltest.xml")
#获取文件元素
movielist = domTree.documentElement
#通过tagName找到元素列表
movies = movielist.getElementsByTagName("movie")
for movie in movies:
    print("******** movie list in xml file *********")
    my_list = []
    if movie.hasAttribute("title") :
        print("title is %s" % movie.getAttribute("title"))  #获取元素属性

    for node in movie.childNodes:  #遍历子节点，返回值为列表
        my_list.append(node.nodeName)
    print("list:", my_list)

    type = movie.getElementsByTagName("type")[0]
    print("type is %s" % type.childNodes[0].data)  #获取子节点的数据

    fm = movie.getElementsByTagName("format")[0]
    print("format is %s" % fm.childNodes[0].data)

    if "year" in my_list:
        year = movie.getElementsByTagName("year")[0]
        print("year is %s" % year.childNodes[0].data)

    rating = movie.getElementsByTagName("rating")[0]
    print("rating is %s" % rating.childNodes[0].data)

    stars = movie.getElementsByTagName("stars")[0]
    print("stars is %s" % stars.childNodes[0].data)

    description = movie.getElementsByTagName("description")[0]
    print("description is %s" % description.childNodes[0].data)