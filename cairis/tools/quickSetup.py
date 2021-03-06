#!/usr/bin/env python

#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from cairis.core.ARM import ARMException
from sqlalchemy.exc import SQLAlchemyError
import os
import sys
import MySQLdb
import _mysql_exceptions
from cairis.core.MySQLDatabaseProxy import createDatabaseAccount, createDatabaseAndPrivileges, createDatabaseSchema

__author__ = 'Shamal Faily'


def quick_setup(dbHost,dbPort,dbRootPassword,tmpDir,rootDir,imageDir,configFile,webPort,logLevel,staticDir,uploadDir,userName,passWd):
  if (len(userName) > 255):
    raise ARMException("Username cannot be longer than 255 characters")
  if (userName == "root"):
    raise ARMException("Username cannot be root")
  createUserDatabase(dbHost,dbPort,dbRootPassword,rootDir)
  os.environ["CAIRIS_CFG"] = configFile
  pathName = os.path.split(os.path.split(os.path.realpath(os.path.dirname(__file__)))[0])[0]
  sys.path.insert(0, pathName)
  fileName = os.environ.get("HOME") + "/.bashrc"
  f = open(fileName,'a')
  f.write("export CAIRIS_CFG="+ configFile +"\n")
  f.write("export PYTHONPATH=${PYTHONPATH}:" + pathName +"\n")
  f.close()
  createCairisCnf(configFile,dbRootPassword,dbHost,dbPort,tmpDir,rootDir,imageDir,webPort,logLevel,staticDir,uploadDir)

  from cairis.bin.add_cairis_user import user_datastore, db

  db.create_all()
  user_datastore.create_user(email=userName, password=passWd)
  db.session.commit()
  createDatabaseAccount(dbRootPassword,dbHost,dbPort,userName,'')
  createDatabaseAndPrivileges(dbRootPassword,dbHost,dbPort,userName,'',userName + '_default')
  createDatabaseSchema(rootDir,dbHost,dbPort,userName,'',userName + '_default')


def createUserDatabase(dbHost,dbPort,dbRootPassword,rootDir):
  try:
    rootConn = MySQLdb.connect(host=dbHost,port=int(dbPort),user='root',passwd=dbRootPassword)
    rootCursor = rootConn.cursor()
  except _mysql_exceptions.DatabaseError as e:
    id,msg = e
    exceptionText = 'Error connecting to MySQL (id:' + str(id) + ',message:' + msg + ')'
    raise ARMException(exceptionText)

  try:
    dropUserDbSql = "drop database if exists cairis_user"
    rootCursor.execute(dropUserDbSql)
  except _mysql_exceptions.DatabaseError as e:
    id,msg = e
    exceptionText = 'MySQL error removing existing cairis_user database (id: ' + str(id) + ', message: ' + msg
    raise ARMException(exceptionText)

  createDatabaseAccount(dbRootPassword,dbHost,dbPort,'cairis_test','cairis_test')
  createDatabaseAndPrivileges(dbRootPassword,dbHost,dbPort,'cairis_test','cairis_test','cairis_test_default')
  createDatabaseSchema(rootDir,dbHost,dbPort,'cairis_test','cairis_test','cairis_test_default')

  try:
    createUserDbSql = "create database if not exists cairis_user"
    rootCursor.execute(createUserDbSql)
  except _mysql_exceptions.DatabaseError as e:
    id,msg = e
    exceptionText = 'MySQL error creating cairis_user database (id: ' + str(id) + ', message: ' + msg
    raise ARMException(exceptionText)

  try:
    recursionDepthSql = "set global max_sp_recursion_depth = 255"
    rootCursor.execute(recursionDepthSql)
  except _mysql_exceptions.DatabaseError as e:
    id,msg = e
    exceptionText = 'MySQL error setting recursion depth (id: ' + str(id) + ', message: ' + msg
    raise ARMException(exceptionText)

  try:
    flushPrivilegesSql = "flush privileges"
    rootCursor.execute(flushPrivilegesSql)
  except _mysql_exceptions.DatabaseError as e:
    id,msg = e
    exceptionText = 'MySQL error flushing privileges (id: ' + str(id) + ', message: ' + msg
    raise ARMException(exceptionText)

  rootCursor.close()
  rootConn.close()

def createCairisCnf(configFile,dbRootPassword,dbHost,dbPort,tmpDir,rootDir,imageDir,webPort,logLevel,staticDir,uploadDir):
  f = open(configFile,'w')
  f.write("rpasswd = " + dbRootPassword + "\n")
  f.write("dbhost = " + dbHost + "\n")
  f.write("dbport = " + str(dbPort) + "\n")
  f.write("tmp_dir = " + tmpDir + "\n")
  f.write("root = " + rootDir + "\n")
  f.write("default_image_dir = " + imageDir + "\n")
  f.write("web_port = " + str(webPort) + "\n")
  f.write("log_level = " + logLevel + "\n")
  f.write("web_static_dir = " + staticDir + "\n")
  f.write("upload_dir = " + uploadDir + "\n")

  f.write("\n")
  f.write("secret_key = " + os.urandom(16).encode('hex') + "\n")
  f.write("password_hash = sha512_crypt\n")
  f.write("password_salt = " + os.urandom(16).encode('hex') + "\n")
  f.close()
