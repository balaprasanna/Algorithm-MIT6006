# -*- coding: utf-8 -*-
__author__ = 'zym'
import re
import jieba
import string
import DocumentDistance
import math
import PyCluster
import DBHelper


text1=u"""白新华，女，1966 年出生。北方交通大学财务会计专业本科、对外经济贸易大学国际法
专业硕士。会计师。历任：北京市审计局助理审计师；中国远大集团公司财务管理本部
会计经理、监审部审计经理；现任中国远大集团公司财务管理本部副总经理。
"""

text2=u"""白新华，曾在北京市审计局、国证经济开发有限公司工作，现任中国远大集
团公司财务管理本部副总经理、华东医药股份有限公司监事、武汉远大制药集团
有限公司监事。"""

text3=u"""刘星先生，1956年生，会计学教授、博士生导师、2000年国务院“政府特殊津贴”获得者，重庆大学经济与工商管理学院院长。1983年获重庆大学工学学士学位，1987年加入中国-加拿大联合培养研究生项目并获西安交通大学管理学硕士学位，1997年获重庆大学管理学博士学位。1991-1992年、1996年、2000年分别在香港城市大学、香港中文大学参加国际合作研究项目或任访问学者、访问教授，并先后赴美国、加拿大等国家进行学术访问或学术交流。中国会计学会理事、中国会计学会教育分会常务理事、重庆市会计学会副会长、重庆"""

text4=u"""刘星，现任本公司独立董事，重庆大学经济与工商管理学院院长、会计学教授、博
士生导师，本公司及东风电子科技股份有限公司、攀钢集团重庆钛业股份有限公司、重庆钢
铁股份有限公司独立董事，曾任香港城市大学会计学系研究员，重庆大学工商管理学院会计
学系系主任，香港中文大学会计学院访问学者、重庆大学经济与工商管理学院副院长、院长、
本公司第三届、第四届董事会独立董事等。"""
oracle_db=DBHelper.OracleDB.get_instance()
oracle_db.connect('edgar','edgar','PROXY')
data=oracle_db.execute_sql("select id,d0801c,d0301b,birth,stkcd,name_cat from t_director where d0101b='安涛'")
jieba.load_userdict('dicname.txt')

clusters=PyCluster.scan_similar_names(data)
for cluster in clusters:
    print cluster.id
    for point in cluster.points:
        print point[0]
    print

