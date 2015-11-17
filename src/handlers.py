# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import json
import logging

from google.appengine.api import memcache  # For XsrfHandler.  Remove if unused.
from google.appengine.api import users

from base import constants
from base import handlers

# Example handlers to demonstrate functionality.
# Replace with your own implementations.

class RootHandler(handlers.BaseHandler):

  def get(self):
    self.redirect('/static/index.html')

class CspHandler(handlers.BaseAjaxHandler):

  def post(self):
    try:
      report = json.loads(self.request.body)
      logging.warn('CSP Violation: %s' % (json.dumps(report['csp-report'])))
      self.render_json({})
    except:
      self.render_json({'error': 'invalid CSP report'})
