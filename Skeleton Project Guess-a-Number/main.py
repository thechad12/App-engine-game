#!/usr/bin/env python

"""main.py - This file contains handlers that are called by taskqueue and/or
cronjobs."""
import logging
import webapp2
from google.appengine.api import mail, app_identity
from api import GuessANumberApi

from models import User, Game


class SendReminderEmail(webapp2.RequestHandler):
    def get(self):
        """Send a reminder email to each User with an unfinished about games.
        Called every  12 hours using a cron job"""
        app_id = app_identity.get_application_id()
        users = User.query(User.email != None)
        game_left = Game.query(game_over == False for user in users)
        for user in users:
            if user in game_left:
                subject = 'This is a reminder!'
                body = 'Hello {}, FINISH YOUR GAME!'.format(user.name)
                # This will send test emails, the arguments to send_mail are:
                # from, to, subject, body
                mail.send_mail('noreply@{}.appspotmail.com'.format(app_id),
                           user.email,
                           subject,
                           body)


class UpdateAverageMovesRemaining(webapp2.RequestHandler):
    def post(self):
        """Update game listing announcement in memcache."""
        GuessANumberApi._cache_average_attempts()
        self.response.set_status(204)


app = webapp2.WSGIApplication([
    ('/crons/send_reminder', SendReminderEmail),
    ('/tasks/cache_average_attempts', UpdateAverageMovesRemaining),
], debug=True)
