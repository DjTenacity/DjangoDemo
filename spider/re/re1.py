# coding:utf-8
import re

# 至少一个或者无限多个数字
pattern = re.compile(r"\d+")
print("----------------match-------------")

print(pattern.match("12fff3fdsf4566").group())
print(pattern.match("abc123fdsf4566", 2, 5))
print(pattern.match("ab123fdsf4566", 2, 5).group())
print(pattern.match(" sd123fdsf4566", 3, 5).group())
# m.group(0)

# 仅仅匹配两组 空格结束
pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)

m = pattern.match("hello world hello  Today")
print(m.group(0) + "__" + m.group(1) + "__" + m.group(2))

print("----------------search-------------")

pattern = re.compile(r"\d+")
print(pattern.search(r"aaaa3  2423423aaaasd123fdsf4566").group())
print(pattern.search(r"aa3  2423 f4566", 3, 8).group() + "__search__"
      + pattern.search(r"aa3  2423 f4566").group())

print("----------------findall-------------")
print(pattern.findall(r"aa3 f 2423 ff4566"))
print(pattern.findall(r"aa3 f 2423 ff4566", 1, 8))

print(re.compile(r"\d?").findall(r"aa3 f 2423 ff4566"))
print(re.compile(r"\d*").findall(r"aa3 f 2423 ff4566"))

print("----------------finditer-------------")
m = pattern.finditer(r"aa3 f 2423 ff4566")
for i in m:
    print(i.group())
