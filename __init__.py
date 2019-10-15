from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder


class RepeatSkill(MycroftSkill):
    def __init__(self):
        super(RepeatSkill, self).__init__(name='RepeatSkill')

    def initialize(self):
        self.add_event('speak', self.handle_remember_last)
        self.last_spoken = None

    def handle_remember_last(self, event):
        utterance = event.data['utterance']
        self.last_spoken = utterance
        if self.last_spoken.startswith('I said, '):
            self.last_spoken = self.last_spoken.replace('I said, ', '')
        print(self.last_spoken)

    @intent_handler(IntentBuilder('repeat.last').require('Repeat').optionally(
        'Testing'))
    def handle_repeat_last_intent(self, message):
        if message.data.get('Testing') == "True":
            self.speak('Testing')
        if self.last_spoken:
            self.speak('I said, ' + self.last_spoken)
        else:
            self.speak('I didn\'t say anything.')


def create_skill():
    return RepeatSkill()
