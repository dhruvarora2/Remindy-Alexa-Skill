def createQueryResponse(thing, preposition, location):
    resp_body = thing + " is " + preposition + " " + location
    if " my " in resp_body:
      print("Hi hi")
      resp_body = resp_body.replace(" my "," your ")
      print("new ",resp_body)
    
    return {
      "version": "1.0",
      "sessionAttributes": {},
      "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "Your " + resp_body
        },
        "card": {
          "type": "Simple",
          "title": "SessionSpeechlet - Welcome",
          "content": "Your " + resp_body
        },
        "reprompt": {
          "outputSpeech": {
            "type": "PlainText",
            "text": "Your " + resp_body
          }
        },
        "shouldEndSession": False
      }
    }
    
def createItemNotFoundResponse():
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Oops! You never told me where it was!"
            },
            "card": {
                "type": "Simple",
                "title": "SessionSpeechlet - Welcome",
                "content": "Oops! You never told me where it was!"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Oops! You never told me where it was! Are you sure you are logged in with correct username?"
                }
            },
            "shouldEndSession": True
        }
    }
  
  
def createDeniedResponse():
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "I'm sorry! Can you try again?"
            },
            "card": {
                "type": "Simple",
                "title": "SessionSpeechlet - Welcome",
                "content": "I'm sorry! Can you try again?"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I'm sorry! Can you try saying that again?"
                }
            },
            "shouldEndSession": True
        }
    }
    
def createSaveResponse():
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Okay. You can ask me about it whenever you forget."
            },
            "card": {
                "type": "Simple",
                "title": "SessionSpeechlet - Welcome",
                "content": "Okay. You can ask me about it whenever you forget."
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Okay. I'll remember it."
                }
            },
            "shouldEndSession": True
        }
    }
    
def createInProgressResponse():
    return {
      "version": "1.0",
      "sessionAttributes": {},
      "response": {
        "directives": [
          {
            "type": "Dialog.Delegate"
          }
        ],
        "shouldEndSession": False
      }
    }

def createWelcomeResponse():
  return {
      "version": "1.0",
      "sessionAttributes": {},
      "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "Welcome to the Remindy. Please tell me about your things by saying something like I am keeping my phone on the table."
        },
        "card": {
          "type": "Simple",
          "title": "SessionSpeechlet - Welcome",
          "content": "Welcome to the Remindy. Please tell me about your things by saying something like I am keeping my phone on the table."
        },
        "reprompt": {
          "outputSpeech": {
            "type": "PlainText",
            "text": "Welcome to Remindy!"
          }
        },
        "shouldEndSession": False
      }
    }
    
def createThankyouResponse():
  return {
      "version": "1.0",
      "sessionAttributes": {},
      "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "You're welcome. This skill was created by Dhruv and Ujjwal."
        },
        "card": {
          "type": "Simple",
          "title": "Welcome",
          "content": "You're welcome. This skill was created by Dhruv and Ujjwal."
        },
        "reprompt": {
          "outputSpeech": {
            "type": "PlainText",
            "text": "Welcome!"
          }
        },
        "shouldEndSession": False
      }
    }
    
def createHelpResponse():
  strBody = "Remindy to remember where you have kept your things! Just tell me about your things by saying something like I am keeping my phone on the table."
  return {
      "version": "1.0",
      "sessionAttributes": {},
      "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "Use "+ strBody
        },
        "card": {
          "type": "Simple",
          "title": "SessionSpeechlet - Welcome",
          "content": "Use "+ strBody
        },
        "reprompt": {
          "outputSpeech": {
            "type": "PlainText",
            "text": "Use "+ strBody
          }
        },
        "shouldEndSession": False
      }
    }