#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：使用MySQL数据库演示程序'

__author__ = 'HouBin'

'''
准备工作：
1.安装MySQL
2.修改配置
（1）在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
（2）在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。
MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
[client]
default-character-set = utf8
[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
3.安装MySQL驱动（mysql-connector-python）
pip3 install mysql-connector-python --allow-external mysql-connector-python
若失败，安装
pip install mysql-connector
'''
import mysql.connector

# 输入用户名和密码
conn = mysql.connector.connect(user='root', password='password', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
