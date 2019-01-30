from __future__ import division

from datetime import date


import numpy as np
import string

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

author = 'Hernán Villamizar'

doc = """
Income Inequality and Effort:
This is the introduction to a Tullock Contest in form of a Real Effort Task and Investment decision
It welcomes the participants and helps them trough the first stages
"""


class Constants(BaseConstants):
    name_in_url = 'Tullock_Income_Intro'
    players_per_group = None

    effective_tax_rate = 0.4
    num_rounds = 1  # first round is with low, second with high wage, third and fourth with taxed income in treat

    t = 180  # Total Time in seconds available for both solving and staying in switch
    # make sure to change images in instructions to be consistent with max time
    # also instructions tables
    time_in_minutes = t/60

    tokensper_string = 1

    eurosper_token = c(0.1)  # make sure to change it in both models
    secondsper_token = 10  # if changing this correct SwitchInstructions

    increase_per_string = 4  # how many more characters each string has

    random_seed_intro = 113

    # this is a summarized instruction to be shown under each sequence as a reminder:
    instructions_summarized = 'Tullock_Income_Intro/InstructionsSum.html'



class Subsession(BaseSubsession):
    # save setting values as an extra column
    def creating_session(self):
        for p in self.get_players():
            p.time_per_round = Constants.t  # Total Time in seconds available for both solving and staying in switch
            p.tokensper_string = Constants.tokensper_string
            p.eurosper_token = float(Constants.eurosper_token)
            p.secondsper_token = Constants.secondsper_token
            p.increase_per_string = Constants.increase_per_string
            p.date_of_session = str(date.today())
            p.random_seed_intro = Constants.random_seed_intro
            if p.id_in_subsession < 10:
                p.unique_id = f'P-0{p.id_in_subsession}-{p.date_of_session}-{p.participant.code}'
            else:
                p.unique_id = f'P-{p.id_in_subsession}-{p.date_of_session}-{p.participant.code}'


class Group(BaseGroup):

    total_production = models.IntegerField(initial=0)  # define group variable

    # determine total production:

    def set_total_production(self):
        total_production = sum(p.production_strings for p in self.get_players())
        # retrieves a list of all individual productions
        # and sums them up
        self.total_production = total_production

    # determine income:
    def set_incomes(self):
        for p in self.get_players():
            p.income_strings_gross = p.production_strings * Constants.tokensper_string
            p.net_income = p.income_strings_gross + p.income_in_switch

    # determine payoffs:
    def set_payoffs(self):
        for p in self.get_players():
            p.earnings = p.net_income
            p.payoff = p.net_income * Constants.eurosper_token


class Player(BasePlayer):

    # save Constants as an extra column for each observation
    unique_id = models.CharField()

    time_per_round = models.PositiveIntegerField()  # Total Time in seconds available for both solving and staying in switch

    tokensper_string = models.PositiveIntegerField()
    tokensper_string_high = models.PositiveIntegerField()
    eurosper_token = models.FloatField()
    secondsper_token = models.PositiveIntegerField()

    increase_per_string = models.PositiveIntegerField()

    date_of_session = models.DateField()
    random_seed_intro = models.PositiveIntegerField()

    role = models.CharField()

    # Number of Tasks Solved
    output_trial = models.FloatField(default=0)
    production_strings = models.FloatField(default=0)

    # available income after solving RET
    income_strings_gross = models.FloatField(default=0)
    net_income = models.FloatField(default=0)
    earnings = models.FloatField(default=0)

    # Variable is 1 when entering switch
    switch1 = models.PositiveIntegerField(default=0)

    switch_time = models.PositiveIntegerField(default=0)

    time_in_switch = models.PositiveIntegerField(default=0)

    additional_time = models.PositiveIntegerField(default=0)

    income_in_switch = models.FloatField(default=0)

    total_production = models.FloatField(default=0)

    # Time Needed to Solve Task i in Round j with tjxi

    t001 = models.PositiveIntegerField(default=0)
    t002 = models.PositiveIntegerField(default=0)
    t003 = models.PositiveIntegerField(default=0)
    t004 = models.PositiveIntegerField(default=0)
    t005 = models.PositiveIntegerField(default=0)

    # correct to allow a variable number of tasks
    # for now, created with:
    # for i in range(10, 46):
    # print('t1{} = models.PositiveIntegerField(default=0)'.format(i))

    # def set_time_fields(self):
    #     for i in range(31):
    #         self.participant.vars['t1{}'.format(i)] = models.PositiveIntegerField(default=0)
    #     print(self.participant.vars)

    t101 = models.PositiveIntegerField(default=0)
    t102 = models.PositiveIntegerField(default=0)
    t103 = models.PositiveIntegerField(default=0)
    t104 = models.PositiveIntegerField(default=0)
    t105 = models.PositiveIntegerField(default=0)
    t106 = models.PositiveIntegerField(default=0)
    t107 = models.PositiveIntegerField(default=0)
    t108 = models.PositiveIntegerField(default=0)
    t109 = models.PositiveIntegerField(default=0)
    t110 = models.PositiveIntegerField(default=0)
    t111 = models.PositiveIntegerField(default=0)
    t112 = models.PositiveIntegerField(default=0)
    t113 = models.PositiveIntegerField(default=0)
    t114 = models.PositiveIntegerField(default=0)
    t115 = models.PositiveIntegerField(default=0)
    t116 = models.PositiveIntegerField(default=0)
    t117 = models.PositiveIntegerField(default=0)
    t118 = models.PositiveIntegerField(default=0)
    t119 = models.PositiveIntegerField(default=0)
    t120 = models.PositiveIntegerField(default=0)
    t121 = models.PositiveIntegerField(default=0)
    t122 = models.PositiveIntegerField(default=0)
    t123 = models.PositiveIntegerField(default=0)
    t124 = models.PositiveIntegerField(default=0)
    t125 = models.PositiveIntegerField(default=0)
    t126 = models.PositiveIntegerField(default=0)
    t127 = models.PositiveIntegerField(default=0)
    t128 = models.PositiveIntegerField(default=0)
    t129 = models.PositiveIntegerField(default=0)
    t130 = models.PositiveIntegerField(default=0)
    t131 = models.PositiveIntegerField(default=0)
    t132 = models.PositiveIntegerField(default=0)
    t133 = models.PositiveIntegerField(default=0)
    t134 = models.PositiveIntegerField(default=0)
    t135 = models.PositiveIntegerField(default=0)
    t136 = models.PositiveIntegerField(default=0)
    t137 = models.PositiveIntegerField(default=0)
    t138 = models.PositiveIntegerField(default=0)
    t139 = models.PositiveIntegerField(default=0)
    t140 = models.PositiveIntegerField(default=0)
    t141 = models.PositiveIntegerField(default=0)
    t142 = models.PositiveIntegerField(default=0)
    t143 = models.PositiveIntegerField(default=0)
    t144 = models.PositiveIntegerField(default=0)
    t145 = models.PositiveIntegerField(default=0)

    def set_switch1(self):
        # Time at which switch was entered
        self.switch_time = self.switch1 * (
            self.additional_time + self.t101 + self.t102 + self.t103 + self.t104 + self.t105 +
            self.t106 + self.t107 + self.t108 + self.t109 + self.t110 +
            self.t111 +
            self.t112 +
            self.t113 +
            self.t114 +
            self.t115 +
            self.t116 +
            self.t117 +
            self.t118 +
            self.t119 +
            self.t120 +
            self.t121 +
            self.t122 +
            self.t123 +
            self.t124 +
            self.t125 +
            self.t126 +
            self.t127 +
            self.t128 +
            self.t129 +
            self.t130 +
            self.t131 +
            self.t132 +
            self.t133 +
            self.t134 +
            self.t135 +
            self.t136 +
            self.t137 +
            self.t138 +
            self.t139 +
            self.t140 +
            self.t141 +
            self.t142 +
            self.t143 +
            self.t144 +
            self.t145
        )

        # This variable determines the total time spent in switch
        self.time_in_switch = self.switch1 * (Constants.t - self.switch_time)

        # This variable determines the tokens per string received
        self.income_in_switch = self.time_in_switch / Constants.secondsper_token

        # This is the sum of strings + production in switch
        self.total_production = self.production_strings + self.income_in_switch
