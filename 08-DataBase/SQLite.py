#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：使用SQLite数据库演示程序'

__author__ = 'HouBin'

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')
# 继续执行一条SQL语句，插入一条记录
cursor.execute(r"insert into user (id, name, score) values ('001', '张三',99)")
cursor.execute(r"insert into user (id, name, score) values ('002', '李四',88)")
cursor.execute(r"insert into user (id, name, score) values ('003', '王五',77)")
cursor.execute(r"insert into user (id, name, score) values ('004', '赵六',66)")
# 通过rowcount获得插入的行数
print('rowcount =', cursor.rowcount)
# 关闭Cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()

# 查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句
cursor.execute('select * from user where id=?',( '001',))
# 获得查询结果集
values = cursor.fetchall()
print(values)
# 执行查询语句
cursor.execute('select * from user')
# 获得查询结果集
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
