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


import ObjectCreationParameters

class ConnectorParameters(ObjectCreationParameters.ObjectCreationParameters):
  def __init__(self,cName,cvName,fName,fInf,tName,tInf,caName):
    ObjectCreationParameters.ObjectCreationParameters.__init__(self)
    self.theName = cName
    self.theViewName = cvName
    self.theFromName = fName
    self.theFromInterface = fInf
    self.theToName = tName
    self.theToInterface = tInf
    self.theAssetName = caName

  def name(self): return self.theName
  def view(self): return self.theViewName
  def fromName(self): return self.theFromName
  def fromInterface(self): return self.theFromInterface
  def toName(self): return self.theToName
  def toInterface(self): return self.theToInterface
  def asset(self): return self.theAssetName
