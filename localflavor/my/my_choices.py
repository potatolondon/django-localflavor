# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

# see https://en.wikipedia.org/wiki/ISO_3166-2:MY
STATE_CHOICES = (

    # federal territories
    ('MY-14', _('Wilayah Persekutuan Kuala Lumpur')),
    ('MY-15', _('Wilayah Persekutuan Labuan')),
    ('MY-16', _('Wilayah Persekutuan Putrajaya')),

    # states
    ('MY-01', _('Johor')),
    ('MY-02', _('Kedah')),
    ('MY-03', _('Kelantan')),
    ('MY-04', _('Melaka')),
    ('MY-05', _('Negeri Sembilan')),
    ('MY-06', _('Pahang')),
    ('MY-08', _('Perak')),
    ('MY-09', _('Perlis')),
    ('MY-07', _('Pulau Pinang')),
    ('MY-12', _('Sabah')),
    ('MY-13', _('Sarawak')),
    ('MY-10', _('Selangor')),
    ('MY-11', _('Terengganu'))
)
