# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .mapper import Mapper


# Module API

class Spider(base.Spider):

    # Public

    name = 'isrctn'
    allowed_domains = ['isrctn.com']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = Mapper()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=utils.make_pattern('search'))),
            Rule(
                LinkExtractor(allow=r'ISRCTN\d+'),
                callback=self.mapper.map_response,
            ),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)