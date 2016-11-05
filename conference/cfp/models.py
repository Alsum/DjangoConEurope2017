# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractSubmission(models.Model):
    EVERY = 'every'
    BEGINNER = 'beginner'
    INTER = 'inter'
    ADVANCED = 'advanced'
    AUDIENCE = (
        (EVERY, _('Everyone')),
        (BEGINNER, _('Beginner')),
        (INTER, _('Intermediate')),
        (ADVANCED, _('Advances')),
    )
    author = models.CharField(
        _('Name'), max_length=400
    )
    email = models.EmailField(
        _('E-Mail'), max_length=400
    )
    author_bio = models.CharField(
        _('Bio'), max_length=100
    )
    created_at = models.DateTimeField(
        _('Submitted'), auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated'), auto_now=True
    )
    notes = models.TextField(_('Notes'))
    selected = models.BooleanField(_('Selected'), default=False)
    proposal_title = models.CharField(
        _('Title'), max_length=400
    )
    proposal_abstract = models.TextField(
        _('Abstract')
    )
    proposal_audience = models.CharField(
        _('Audience'), choices=AUDIENCE, max_length=10,
    )

    class Meta:
        verbose_name = _('talk submission')
        verbose_name_plural = _('talk submissions')

    def __str__(self):
        return '{} "{}" by {}'.format(self._meta.verbose_name, self.proposal_title, self.author)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} "{}" by {}'.format(self._meta.verbose_name, self.proposal_title, self.author)


class TalkSubmission(AbstractSubmission):
    proposal_why = models.TextField(
        _('Motivation')
    )
    proposal_requirements = models.TextField(
        _('Requirements'), blank=False, default='',
    )
    mentor_wanted = models.BooleanField(
        _('Mentor'), default=False,
        help_text=_('More experienced speakers can help you reviewing your talk, '
                    'practicing, and getting ready for the presentation')
    )
    mentor_offer = models.BooleanField(
        _('Mentor - Offer'), default=False,
        help_text=_('Are you an experienced speaker and are you willing to help other speakers? '
                    'Select this and we will get in contact with you!')
    )
    pycon = models.BooleanField(
        _('PyCon'), default=False,
        help_text=_('We will share your proposal with the PyCon Italia Team and they will '
                    'evaluate independently your proposal.')
    )

    class Meta:
        verbose_name = _('talk submission')
        verbose_name_plural = _('talk submissions')


class WorkshopSubmission(AbstractSubmission):
    TWO_HOURS = '2_hrs'
    THREE_HOURS = '3_hrs'
    DURATIONS = (
        (TWO_HOURS, _('Two Hours')),
        (THREE_HOURS, _('Three Hours')),
    )
    workshop_duration = models.CharField(
        _('Durtation'), choices=DURATIONS, max_length=10,
    )

    class Meta:
        verbose_name = _('workshop submission')
        verbose_name_plural = _('workshop submissions')
