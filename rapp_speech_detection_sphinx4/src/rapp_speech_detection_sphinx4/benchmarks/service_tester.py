#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright 2015 RAPP

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

# Authors: Athanassios Kintsakis, Manos Tsardoulias
# contact: akintsakis@issel.ee.auth.gr, etsardou@iti.gr

import rospy

from rapp_platform_ros_communications.srv import (
  SpeechRecognitionSphinx4Srv,
  SpeechRecognitionSphinx4SrvResponse,
  SpeechRecognitionSphinx4SrvRequest,
  SpeechRecognitionSphinx4ConfigureSrv,
  SpeechRecognitionSphinx4ConfigureSrvResponse,
  SpeechRecognitionSphinx4ConfigureSrvRequest,
  SpeechRecognitionSphinx4TotalSrv,
  SpeechRecognitionSphinx4TotalSrvResponse,
  SpeechRecognitionSphinx4TotalSrvRequest
  )

class SpeechRecognitionTester:

  def setup_fifty_words_voc(self):
    spreq = SpeechRecognitionSphinx4ConfigureSrvRequest()
    spreq.language = 'el'
    spreq.words = []
    spreq.words.append(u'όχι')
    spreq.words.append(u'ναι')
    spreq.words.append(u'ίσως')
    spreq.words.append(u'δε')
    spreq.words.append(u'θυμάμαι')
    spreq.words.append(u'αρκετά')
    spreq.words.append(u'κοντά')
    spreq.words.append(u'έλα')
    spreq.words.append(u'φύγε')
    spreq.words.append(u'σήκω')
    spreq.words.append(u'κάτσε')
    spreq.words.append(u'είμαι')
    spreq.words.append(u'είσαι')
    spreq.words.append(u'σε')
    spreq.words.append(u'λένε')
    spreq.words.append(u'πώς')
    spreq.words.append(u'που')
    spreq.words.append(u'ποτήρι')
    spreq.words.append(u'φούρνος')
    spreq.words.append(u'ώρα')
    spreq.words.append(u'είναι')
    spreq.words.append(u'τι')
    spreq.words.append(u'γιατί')
    spreq.words.append(u'ρομπότ')
    spreq.words.append(u'σκάιπ')
    spreq.words.append(u'ιμέηλ')
    spreq.words.append(u'κόρη')
    spreq.words.append(u'γιός')
    spreq.words.append(u'στείλε')
    spreq.words.append(u'μη')
    spreq.words.append(u'στείλεις')
    spreq.words.append(u'θέλω')
    spreq.words.append(u'βοήθεια')
    spreq.words.append(u'γιατρός')
    spreq.words.append(u'χάπια')
    spreq.words.append(u'χάπι')
    spreq.words.append(u'το')
    spreq.words.append(u'τα')
    spreq.words.append(u'του')
    spreq.words.append(u'ξέρω')
    spreq.words.append(u'ξέρεις')
    spreq.words.append(u'ποδόσφαιρο')
    spreq.words.append(u'ποιός')
    spreq.words.append(u'είναι')
    spreq.words.append(u'τώρα')
    spreq.words.append(u'μετά')
    spreq.words.append(u'πριν')
    spreq.words.append(u'χτές')
    spreq.words.append(u'αύριο')
    spreq.words.append(u'ο')

    spreq.sentences = []
    spreq.sentences.append(u'όχι δε θυμάμαι')
    spreq.sentences.append(u'ναι στείλε ιμέηλ')
    spreq.sentences.append(u'ίσως δε θυμάμαι')
    spreq.sentences.append(u'τι ώρα είναι')
    spreq.sentences.append(u'πώς σε λένε')
    spreq.sentences.append(u'που είναι το ποτήρι')
    spreq.sentences.append(u'θέλω βοήθεια')
    spreq.sentences.append(u'που είναι ο γιατρός')
    spreq.sentences.append(u'τι ώρα είναι τώρα')
    spreq.sentences.append(u'που είναι τα χάπια')
    spreq.sentences.append(u'το ξέρω')
    spreq.sentences.append(u'έλα αρκετά κοντά')
    spreq.sentences.append(u'που είναι το χάπι')
    spreq.sentences.append(u'ναι έλα')
    spreq.sentences.append(u'στείλε ιμέηλ τώρα')
    spreq.sentences.append(u'στείλε ιμέηλ αύριο')
    spreq.sentences.append(u'είσαι ρομποτ')
    spreq.sentences.append(u'που είναι ο φούρνος')
    spreq.sentences.append(u'δε θυμάμαι ποιός είσαι')
    spreq.sentences.append(u'δε θυμάμαι')
    spreq.sentences.append(u'ποιός είσαι')
    spreq.sentences.append(u'θέλω τα χάπια')

    spreq.grammar = []
    spreq.grammar.append(u'όχι')
    spreq.grammar.append(u'δε θυμάμαι')
    spreq.grammar.append(u'όχι δε θυμάμαι')
    spreq.grammar.append(u'στείλε ιμέηλ')
    spreq.grammar.append(u'τι ώρα είναι')
    spreq.grammar.append(u'τι είναι')
    spreq.grammar.append(u'που είναι')
    spreq.grammar.append(u'που είναι το ποτήρι')
    spreq.grammar.append(u'τι είσαι')
    spreq.grammar.append(u'ποιός είσαι')
    spreq.grammar.append(u'δε θυμάμαι ποιός είσαι')
    spreq.grammar.append(u'που είναι ο φούρνος')
    spreq.grammar.append(u'θέλω')
    spreq.grammar.append(u'θέλω τα χάπια')
    spreq.grammar.append(u'θέλω το χάπι')
    spreq.grammar.append(u'πώς σε λένε')
    spreq.grammar.append(u'σε λένε')
    spreq.grammar.append(u'ίσως')
    spreq.grammar.append(u'έλα κοντά')
    spreq.grammar.append(u'αρκετά κοντά')
    spreq.grammar.append(u'ξέρεις ποδόσφαιρο')
    spreq.grammar.append(u'θέλω βοήθεια')
    spreq.grammar.append(u'γιατί')
    spreq.grammar.append(u'τι είσαι')
    spreq.grammar.append(u'μη στείλεις')
    spreq.grammar.append(u'στείλε αύριο')
    spreq.grammar.append(u'είναι αύριο')
    spreq.grammar.append(u'είναι τώρα')
    spreq.grammar.append(u'το ξέρεις')
    spreq.grammar.append(u'δεν το ξέρεις')

    return spreq

  def setup_six_words_voc(self):
    spreq = SpeechRecognitionSphinx4ConfigureSrvRequest()
    spreq.language = 'gr'
    spreq.words = []
    spreq.words.append(u'όχι')
    spreq.words.append(u'ναι')
    spreq.words.append(u'μπορεί')
    spreq.words.append(u'ίσως')
    spreq.words.append(u'δε')
    spreq.words.append(u'ξέρω')

    spreq.sentences = []
    spreq.sentences.append(u'όχι')
    spreq.sentences.append(u'ναι')
    spreq.sentences.append(u'μπορεί')
    spreq.sentences.append(u'ίσως')
    spreq.sentences.append(u'δε')
    spreq.sentences.append(u'ξέρω')
    spreq.sentences.append(u'όχι δε ξέρω')
    spreq.sentences.append(u'ναι μπορεί')
    spreq.sentences.append(u'ίσως δε ξέρω')
    spreq.sentences.append(u'δε ξέρω')
    spreq.sentences.append(u'ναι ίσως')
    spreq.sentences.append(u'μπορεί δε ξέρω')
    spreq.sentences.append(u'ίσως όχι')

    spreq.grammar = []
    spreq.grammar.append(u'(όχι)')
    spreq.grammar.append(u'(ναι)')
    spreq.grammar.append(u'(μπορεί)')
    spreq.grammar.append(u'(μπορεί δε ξέρω)')
    spreq.grammar.append(u'(δε ξέρω)')
    spreq.grammar.append(u'(ίσως όχι)')
    spreq.grammar.append(u'(ίσως ναι)')
    spreq.grammar.append(u'(ναι ίσως)')

    return spreq

  def setup_two_words_voc(self):
    spreq = SpeechRecognitionSphinx4ConfigureSrvRequest()
    spreq.language = 'gr'
    spreq.words = []
    spreq.words.append(u'όχι')
    spreq.words.append(u'ναι')

    spreq.sentences = []
    spreq.sentences.append(u'όχι')
    spreq.sentences.append(u'ναι')

    spreq.grammar = []
    spreq.grammar.append(u'(όχι)')
    spreq.grammar.append(u'(ναι)')

    return spreq

  def perform_experiment(self, file_path, int_words, grammar,\
      experiments_number, audio_source):

    spreq = ""
    if int_words == 2:
      spreq = self.setup_two_words_voc()
    elif int_words == 6:
      spreq = self.setup_six_words_voc()
    elif int_words == 50:
      spreq = self.setup_fifty_words_voc()

    spee_req = SpeechRecognitionSphinx4TotalSrvRequest()
    spee_req.language = spreq.language
    spee_req.words = spreq.words
    spee_req.grammar = spreq.grammar
    spee_req.user = 'etsardou'
    if grammar == "no_gr":
      spee_req.grammar = []
    spee_req.sentences = spreq.sentences
    mean = 0.0

    for i in range(0, experiments_number):
      self.counter += 1
      spee_req.path = file_path
      spee_req.audio_source = audio_source
      res = self.conf_sp_ser(spee_req)
      print res
      exp_res = []
      if int_words == 2:
        exp_res = self.two_words_res
      elif int_words == 6:
        exp_res = self.six_words_res
      elif int_words == 50:
        exp_res = self.fifty_words_res
      #self.overall_score[file_path + "_" + grammar + "_" + str(i)] =\
              #self.lcs_length(res.words, exp_res) / (1.0 * len(exp_res))
      if len(exp_res) == 0:
        mean += 0
        self.total_mean += 0
      else:
        mean += self.lcs_length(res.words, exp_res) / (1.0 * len(exp_res))
        self.total_mean += self.lcs_length(res.words, exp_res) / (1.0 * len(exp_res))
      print file_path + "_" + grammar
      for w in res.words:
          print w
      print exp_res
      if len(exp_res) != 0:
        print "Score: " + str(self.lcs_length(res.words, exp_res) / \
            (1.0 * len(exp_res)))
      else:
        print "Score: 0"
      print "overall up to now: " + str(self.total_mean / self.counter * 100.0) + "%"
      print "-------------------------------------------------"
    mean /= experiments_number * 1.0
    self.overall_score[file_path + "_" + grammar + "_mean"] = mean
    print ">>>>> Mean Score: " + str(self.overall_score[file_path + "_" + grammar + "_mean"])
    print "-------------------------------------------------"


  def lcs_length(self,a, b):
    table = [[0] * (len(b) + 1) for _ in xrange(len(a) + 1)]
    for i, ca in enumerate(a, 1):
      for j, cb in enumerate(b, 1):
        table[i][j] = (
          table[i - 1][j - 1] + 1 if ca == cb else
          max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]

  def lcs(self, xstr, ystr):
    if not xstr or not ystr:
      return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
      return x + self.lcs(xs, ys)
    else:
      return max(self.lcs(xstr, ys), self.lcs(xs, ystr), key=len)

  def __init__(self):

    self.conf_sp_ser = rospy.ServiceProxy(\
        '/ric/speech_detection_sphinx4_batch',\
        SpeechRecognitionSphinx4TotalSrv)

    self.two_words_res = [u'ναι', u'όχι', u'ναι']
    self.six_words_res = [u'ναι', u'μπορεί', u'δε', u'ξέρω', u'ίσως', u'όχι']
    self.fifty_words_res = ['πώς', 'σε', 'λένε', 'δε', 'θυμάμαι', 'ποιός', 'είσαι',\
            'θέλω', 'τα', 'χάπια', 'που', 'είναι', 'το', 'ποτήρι']

    self.overall_score = {}

    self.total_mean = 0.0
    self.counter = 0

    noftests = 1

    # Must add grammar in the arguments
    filename = "/home/etsardou/recordings/benchmark_recordings/nao_ogg/original_ogg/nao_ogg_d05_a3.ogg"
    self.perform_experiment(filename, 50, "no_gr", noftests, "nao_ogg")

    #filename = "/home/etsardou/recordings/benchmark_recordings/nao_wav/original_4_ch_48kHz/nao_wav_d05_a3.wav"
    #self.perform_experiment(filename, 50, "no_gr", noftests, "nao_wav_4_ch")

    for el in self.overall_score:
      print el + " : " + str(self.overall_score[el]*100.0) + " %"
    print "Final overall: " + str(self.total_mean / self.counter * 100.0) + "%"

# Main function
if __name__ == "__main__":
  rospy.init_node('SpeechRecognitionTester')
  SpeechRecognitionTesterNode = SpeechRecognitionTester()
  #rospy.spin()

