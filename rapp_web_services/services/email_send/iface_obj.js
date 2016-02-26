/***
 * Copyright 2015 RAPP
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Authors: Konstantinos Panayiotou
 * Contact: klpanagi@gmail.com
 *
 */


var clientRes = function( error ){
  error = error || '';
  var obj = {
    error: error
  };
  return obj;
};


var clientReq = function( filepath, email, passwd, server, port,
  recipients, body, subject)
{
  filepath = filepath || '';
  email = email || '';
  passwd = passwd || '';
  server = server || '';
  port = port || '';
  recipients = recipients || [];
  body = body || '';
  subject = subject || '';

  var obj = {
    file_uri: filepath,
    email: email,
    passwd: passwd,
    server: server,
    port: port,
    recipients: recipients,
    body: body,
    subject: subject
  };
  return obj;
};


var rosReq = function( files, email, passwd, server, port,
  recipients, body, subject)
{
  files = files || [];
  email = email || '';
  passwd = passwd || '';
  server = server || '';
  port = port || '';
  recipients = recipients || [];
  body = body || '';
  subject = subject || '';

  var obj = {
    files: files,
    userEmail: email,
    password: passwd,
    server: server,
    port: port,
    recipients: recipients,
    body: body,
    subject: subject
  };
  return obj;
};


var rosRes = function(){
  var stat = 0;

  var obj = {
    status: stat
  };
  return obj;
};

exports.client_res = clientRes;
exports.client_req = clientReq;
exports.ros_req = rosReq;
exports.ros_res = rosRes;
