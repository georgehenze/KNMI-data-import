#!/usr/bin/python
# coding=UTF-8
#
# ----------------------------------------------------------------------------
#   
#   knmi_daily_data_import.py
#   
#   Copyright (C) 2013 George Henze
#   
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   
# ----------------------------------------------------------------------------
#
# BRON:
# KONINKLIJK NEDERLANDS METEOROLOGISCH INSTITUUT (KNMI)
#
# SOURCE:
# ROYAL NETHERLANDS METEOROLOGICAL INSTITUTE (KNMI)
#
# for a list of all weatherstations http://www.knmi.nl/climatology/daily_data/selection.cgi)
#
# for an explanation of script access http://www.knmi.nl/kd/daggegevens/scriptxs-nl.html

import urllib2
import csv
import MySQLdb
import datetime
import logging
import logging.handlers
import sys

WEATHERSTATION = '344' 
STARTINGDATE   = '20121001'

MYSQL_SERVER   = 'server'
MYSQL_USER     = 'user'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE = 'databasename'

REQUEST_URL    = 'http://www.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi'
REQUEST_DATA   = 'stns='+WEATHERSTATION+'&vars=ALL&start='+STARTINGDATE #+'&end='+einddatum

def skip_comments(iterable):
    for line in iterable:
        if not line.startswith('#'):
            yield line

def print_fields(iterable):  
    for line in iterable:
        print line

def create_logger():
    global logger
    logger = logging.getLogger('knmi_daily_data_import')
    
    global hdlr
    hdlr = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s %(message)s')
    
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel('DEBUG')    

def log(text):
    try:
        logger.debug(text)
    except NameError:
        pass
        
def insert_database(row):
    
    try:
        db = MySQLdb.connect(MYSQL_SERVER, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)  
        cursor = db.cursor()
        
        query = "INSERT IGNORE INTO " + MYSQL_DATABASE + ".weather_data VALUES ('" + \
                    row['YYYYMMDD'] + "\',\'" + \
                    row['STN'] + "\',\'" + \
                    row['DVEC'] + "\',\'" + \
                    row['FHVEC'] + "\',\'" + \
                    row['FG'] + "\',\'" + \
                    row['FHX'] + "\',\'" + \
                    row['FHXH'] + "\',\'" + \
                    row['FXX'] + "\',\'" + \
                    row['FXXH'] + "\',\'" + \
                    row['TG'] + "\',\'" + \
                    row['TN'] + "\',\'" + \
                    row['TNH'] + "\',\'" + \
                    row['TX'] + "\',\'" + \
                    row['TXH'] + "\',\'" + \
                    row['T10N'] + "\',\'" + \
                    row['T10NH'] + "\',\'" + \
                    row['SQ'] + "\',\'" + \
                    row['SP'] + "\',\'" + \
                    row['Q'] + "\',\'" + \
                    row['DR'] + "\',\'" + \
                    row['RH'] + "\',\'" + \
                    row['RHX'] + "\',\'" + \
                    row['RHXH'] + "\',\'" + \
                    row['PG'] + "\',\'" + \
                    row['PX'] + "\',\'" + \
                    row['PXH'] + "\',\'" + \
                    row['PN'] + "\',\'" + \
                    row['PNH'] + "\',\'" + \
                    row['VVN'] + "\',\'" + \
                    row['VVNH'] + "\',\'" + \
                    row['VVX'] + "\',\'" + \
                    row['VVXH'] + "\',\'" + \
                    row['NG'] + "\',\'" + \
                    row['UG'] + "\',\'" + \
                    row['UX'] + "\',\'" + \
                    row['UXH'] + "\',\'" + \
                    row['UN'] + "\',\'" + \
                    row['UNH'] + "\',\'" + \
                    row['EV24'] + "\',\'" + \
                    row['YYYYMMDD'] + "\')"
        cursor.execute(query)
        db.commit()        
    
    except MySQLdb.Error, e:
        log("Database error %d: %s" % (e.args[0], e.args[1]))

def main():

    log('Running knmi_daily_data_import.py')
    log('Request URL        : ' + REQUEST_URL)
    log('Request parameters : ' + REQUEST_DATA)

    try:
        serv_req = urllib2.Request(url=REQUEST_URL, data=REQUEST_DATA)
        serv_resp = urllib2.urlopen(serv_req)
    except urllib2.HTTPError, e:
        log('Error requesting data: %s - %s.' % (e.code, e.reason))
        sys.exit(1)
        
    log('Data received') 
    
    fields = ('STN','YYYYMMDD','DVEC','FHVEC','FG','FHX','FHXH','FHN','FHNH','FXX','FXXH','TG','TN','TNH','TX','TXH','T10N','T10NH','SQ','SP','Q','DR','RH','RHX','RHXH','PG','PX','PXH','PN','PNH','VVN','VVNH','VVX','VVXH','NG','UG','UX','UXH','UN','UNH','EV24')
    delimiter = ','
    
    reader = csv.DictReader(skip_comments(serv_resp), delimiter=delimiter, fieldnames=fields, skipinitialspace=True)
    
    log('Inserting records into database')
    
    for row in reader:
        insert_database(row)

    log('Done.')
    
if __name__ == "__main__":
    create_logger()
    main()
    
