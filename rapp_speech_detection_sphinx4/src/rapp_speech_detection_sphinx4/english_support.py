#!/usr/bin/env python

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

# Authors: Athanassios Kintsakis, Aris Thallas, Manos Tsardoulias
# contact: akintsakis@issel.ee.auth.gr, aris.thallas@{iti.gr, gmail.com}, etsardou@iti.gr


import rospy
import sys
import mmap

from global_parameters import GlobalParams
from rapp_exceptions import RappError
from limited_vocabulary_creator import *
from rapp_tools import *

## @class EnglishSupport
# @brief Allows the creation of configuration files for English Sphinx speech recognition
class EnglishSupport(GlobalParams):

  ## Performs initializations
  def __init__(self):
    ## Contains global Sphinx parameters
    #
    # (see global_parameters.GlobalParams)
    self._globalParams = GlobalParams()

    ## The limited vocabulary creator
    #
    # Instantiates limited_vocabulary_creator.LimitedVocabularyCreator
    self._vocabulary = LimitedVocabularyCreator()

    # TODO: Split the rapp_sphinx4_java_libraries package into libraries and
    # language models
    english_dictionary = self._globalParams._language_models_url + \
        "/englishPack/cmudict-en-us.dict"

    jar_path = ".:" + self._globalParams._sphinx_jar_files_url + "/" + \
        self._globalParams._sphinx_jar_file + ":" + \
        self._globalParams._sphinx_package_url + "/src"

    # Grammar is dummy here..
    ## The generic Sphinx configuration
    #
    # @note Check acoustic model!!
    self._generic_sphinx_configuration = { \
      'jar_path' : jar_path, \
      'configuration_path' : self._globalParams._language_models_url + \
                                      "/greekPack/default.config.xml", \
      'acoustic_model' : self._globalParams._acoustic_models_url, \
      'grammar_name' : 'hello', \
      'grammar_folder' : self._globalParams._language_models_url + \
                                                    "/greekPack/", \
      'dictionary' : self._globalParams._language_models_url + \
                            "/englishPack/cmudict-en-us.dict", \
      'language_model' : self._globalParams._language_models_url + \
                                      "/englishPack/en-us.lm.bin", \
      'grammar_disabled' : True
      }

    ## The English dictionary file
    #
    # Located in path global_parameters.GlobalParams#_language_models_url +
    # "/englishPack/cmudict-en-us.dict"
    self._english_dict_file = None
    ## The mmap of the English dictionary file contents
    self._english_dict_mapping = None

    # Open the generic english dictionary file
    try:
      self._english_dict_file = open(english_dictionary, 'r')
    except IOError:
      rapp_print("English dictionary could not be opened!")
    # Create a mapping of the file
    self._english_dict_mapping = mmap.mmap(self._english_dict_file.fileno(), 0, \
        access = mmap.ACCESS_READ)

  ## Compute the English word phonemes
  #
  # @param words [list::string] The set of English words
  # @return enhanced_words  [dictionary] The English word->phonemes mapping
  def getWordPhonemes(self, words):
    enhanced_words = {}
    for word in words:
      inner_words = []
      inner_phonemes = []
      if "-" not in word: # Check for conjoined english words
        index = self._english_dict_mapping.find("\n" + word + " ")
        if index == -1:
           raise RappError("ERROR: Word " + word +\
                    " does not exist in the English Dictionary")
        else:
          self._english_dict_file.seek(index + 1)
          line = self._english_dict_file.readline()
          line = line[:-1]
          split_line = line.split(" ")
          inner_phonemes = split_line[1:]

      else:
        inner_words = word.split("-")
        for in_w in inner_words:
          index = self._english_dict_mapping.find("\n" + in_w + " ")
          if  index == -1:
            raise RappError("ERROR: Word " + in_w +\
                    " does not exist in the English Dictionary")
          else:
            self._english_dict_file.seek(index + 1) # +1 because of the extra \n
            line = self._english_dict_file.readline()
            line = line[:-1] # to erase the \n
            split_line = line.split(" ")

            #enhanced_words[split_line[0]] = []
            for i in range(1, len(split_line)):
              inner_phonemes.append(split_line[i])
      enhanced_words[word] = inner_phonemes

    return enhanced_words

  ## Computes the Limited English Configuration
  #
  # @param words      [list::string] The set of words to be identified
  # @param grammar    [list::string] The Sphinx grammar parameter
  # @param sentences  [list::string] The Sphinx sentences parameter
  #
  # @return limited_sphinx_configuration [dictionary] The Limited English configuration
  def getLimitedVocebularyConfiguration(self, words, grammar, sentences):
    rapp_print(words)

    enhanced_words = self.getWordPhonemes( words )

    try:
        limited_sphinx_configuration= \
            self._vocabulary.createConfigurationFiles(enhanced_words, grammar, sentences)
    except RappError as e:
        raise RappError(e.value)

    return limited_sphinx_configuration

  ## Returns the Generic English Configuration
  #
  # @return #_generic_sphinx_configuration [dictionary] The Generic English configuration
  def getGenericConfiguration(self):
    return self._generic_sphinx_configuration
