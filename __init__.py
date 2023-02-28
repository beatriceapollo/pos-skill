from mycroft import MycroftSkill, intent_file_handler
from nltk.tokenize import word_tokenize
import nltk


class Pos(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pos.intent')
    def handle_pos(self, message):
        self.speak_dialog('pos')

    def converse(self, utterances, lang):
        if utterances:
            text = utterances[0]
            tokenized_text = word_tokenize(text)
            tagged_text = nltk.pos_tag(tokenized_text)
            self.speak(print(tagged_text))
            return True
        else:
            return False
        
    def stop(self):
        self.stop

def create_skill():
    return Pos()

