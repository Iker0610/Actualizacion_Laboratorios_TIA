# classificationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
import sys

import perceptron_pacman
from dataClassifier import runClassifier, enhancedFeatureExtractorPacman
from game import Agent


class DummyOptions:
    def __init__(self):
        self.data = "pacman"
        self.training = 25000
        self.test = 100
        self.odds = False
        self.weights = False


class ClassifierAgent(Agent):
    def __init__(self, trainingData=None, validationData=None, classifierType="perceptron", agentToClone=None, numTraining=3):
        super().__init__()

        legalLabels = ['Stop', 'West', 'East', 'North', 'South']
        if classifierType == "perceptron":
            classifier = perceptron_pacman.PerceptronClassifierPacman(legalLabels, numTraining)
        else:
            print("Unknown classifier:", classifierType)
            sys.exit(2)

        self.classifier = classifier
        self.featureFunction = enhancedFeatureExtractorPacman
        args = {'featureFunction': self.featureFunction,
                'classifier': self.classifier,
                'printImage': None,
                'trainingData': trainingData,
                'validationData': validationData,
                'agentToClone': agentToClone,
                }
        options = DummyOptions()
        options.classifier = classifierType
        runClassifier(args, options)

    def getAction(self, state):
        features = self.featureFunction(state)
        action = self.classifier.classify([features])[0]
        return action


def scoreEvaluation(state):
    return state.getScore()
