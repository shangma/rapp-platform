/*!
 * @file worker_utils.js
 * @brief Server worker utility functions.
 */

/**
 *  MIT License (MIT)
 *
 *  Copyright (c) <2014> <Rapp Project EU>
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the "Software"), to deal
 *  in the Software without restriction, including without limitation the rights
 *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *  copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in
 *  all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *  THE SOFTWARE.
 *
 *
 *  Authors: Konstantinos Panayiotou
 *  Contact: klpanagi@gmail.com
 *
 */

var path = require('path');
var util = require('util');


var callParent = function( msg ){
  postMessage(msg);
};


var onMessage = function( msg ){
  msg = msg || {};
  //TODO Create worker child thread interfaces.
  //console.log("hello there")
};


var registerSvc = function( svcImpl, svcParams ){
  // Register service to service handler.
  var msg = {
    request: "svc_registration",
    svc_name: svcParams.name,
    worker_name: WORKER.name,
    svc_frame: undefined,
    svc_path: ''
  };

  var svc = new hop.Service( svcImpl );
  // Set path if not anonymous service
  if( ! svcParams.anonymous ){
    svc.name = (svcParams.namespace) ?
      util.format("%s/%s", svcParams.namespace, svcParams.name) :
      svcParams.url_name;
  }
  msg.svc_path = svc.path;
  msg.svc_frame = svc;
  postMessage(msg);

  WORKER.services.push(svcParams.name);
};


/*!
 * @brief Sets worker's name in global scope object.
 *
 * @param wName - Worker's name to assign;
 */
var setWorkerName = function( wName ){
  if( ! wName ){
    throw new Error("Invalid set of Arguments. Missing wName!");
  }
  global.WORKER = global.WORKER || {name: wName, services: []};
};


var launchSvcAll = function(){
  var workerSvc = ENV.WORKERS[ WORKER.name ].services;
  var workerDir = path.dirname(path.join(
    ENV.PATHS.PKG_DIR, ENV.WORKERS[ WORKER.name ].path));

  for( var i in workerSvc ){
    if( ENV.SERVICES[ workerSvc[i] ].launch ){

      if( ENV.SERVICES[ workerSvc[i] ].path ){
        require(
          path.join(ENV.PATHS.SERVICES_DIR, ENV.SERVICES[ workerSvc[i] ].path)
        );
      }
      else{
        require(
          path.join(
            ENV.PATHS.SERVICES_DIR,
            ENV.SERVICES[ workerSvc[i] ].name, 'svc.js'
          )
        );
      }
    }
  }
};


// Global worker thread space hack!!
global.ENV = require( path.join(__dirname, '../..', 'env.js') );
global.registerSvc = registerSvc;


exports.callParent = callParent;
exports.onMessage = onMessage;
exports.setWorkerName = setWorkerName;
exports.launchSvcAll = launchSvcAll;
