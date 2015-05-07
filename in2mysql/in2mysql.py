#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import sys
import os
import MySQLdb
import warnings

# connect
con = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="weibo", charset="utf8", use_unicode=True)
warnings.filterwarnings('ignore', 'Incorrect string value')
warnings.filterwarnings('ignore', "Row")


# init the weibo table
def init_table():
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `tweet` (
          `id` varchar(100) NOT NULL,
          `uid` varchar(100) NOT NULL,
          `user` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
          `nick` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
          `twid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
          `message` text COLLATE utf8_unicode_ci,
          `murl` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
          `refer` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
          `image` text COLLATE utf8_unicode_ci,
          `audio` text COLLATE utf8_unicode_ci,
          `vedio` text COLLATE utf8_unicode_ci,
          `gps` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
          `twnum` varchar(50) DEFAULT '0',
          `comnum` varchar(50) DEFAULT '0',
          `plusnum` varchar(50) DEFAULT '0',
          `createtime` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
        ) ENGINE=myisam DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
    """)
    con.commit()


# import data to table
def im2my(path):
    cursor = con.cursor()
    for k in sorted(os.listdir(path)):
        if k.endswith('.csv'):
            filename = path + '/' + k
            try:
                imsql = "LOAD DATA INFILE '" + filename + "' INTO TABLE tweet COLUMNS TERMINATED BY ',' ENCLOSED BY '" + '"' + "';"
                cursor.execute(imsql)
                con.commit()
            except:
                pass

if __name__ == "__main__":
    print '[*] App: in2mysql'
    print '[*] Version: V1.0(20150506)'
    print '[*] Use: python in2mysql.py /home/cover/pm_file'
    if len(sys.argv) == 2:
        init_table()
        path = sys.argv[1]
        im2my(path)
    else:
        exit()