from django.test import TestCase
from notes.models import Tag

from cards.fsrs import *
from cards.fsrsmodels import Card as fsrscard
from cards.models import Card as ankicard
from userapp.models import *


class SRTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(email='email@email.com', name='test', birthdate='2001-01-01', max_reviews=0, password='kfkjls3/5445.', phone_number='5567394820')
        query_results = CustomUser.objects.all()
        print(query_results)


    def testCard(self):
        f = FSRS()
        fsrs_card = fsrscard()
        anki_card = ankicard()
        now = datetime(2022, 11, 29, 12, 30, 0, 0)
        fsrs_scheduling_cards = f.repeat(fsrs_card, now)
        anki_scheduling_cards = f.repeat(anki_card, now)

        print("fsrs {0} anki {1}".format(fsrs_scheduling_cards[Rating.Good].card.due , anki_scheduling_cards[Rating.Good].card.due))
        self.assertEqual(fsrs_scheduling_cards[Rating.Again].card.scheduled_days, 
        anki_scheduling_cards[Rating.Again].card.scheduled_days)
        self.assertEqual(fsrs_scheduling_cards[Rating.Again].card.elapsed_days, 
        anki_scheduling_cards[Rating.Again].card.elapsed_days)
        self.assertEqual(fsrs_scheduling_cards[Rating.Again].card.stability, 
        anki_scheduling_cards[Rating.Again].card.stability)


        fsrs_card = fsrs_scheduling_cards[Rating.Good].card
        anki_card = anki_scheduling_cards[Rating.Good].card
        now = datetime(2022, 11, 30, 12, 30, 0, 0)
        fsrs_scheduling_cards = f.repeat(fsrs_card, now)
        anki_scheduling_cards = f.repeat(anki_card, now)
        print("fsrs {0} anki {1}".format(fsrs_scheduling_cards[Rating.Easy].card.due , anki_scheduling_cards[Rating.Easy].card.due))

