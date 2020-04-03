import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = "https://api.github.com/search/repositories?q=language:python&ort=stars"

r = requests.get(url)
print("status code:",r.status_code)

#将api响应存储到变量中
response_dict = r.json()
print("total:", response_dict['total_count'])

#存储字典列表
repo_dicts = response_dict["items"]
print("repositories count:", len(repo_dicts))
#研究第一个仓库
repo_dict = repo_dicts[0]
print("\nthe first repositories num:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

names = []
stars = []
for rd in repo_dicts:
    names.append(rd["name"])
    stars.append(rd["stargazers_count"])

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "most populor python projects"
chart.x_labels = names
chart.add("", stars)
chart.render_to_file("python_repos.sgv")