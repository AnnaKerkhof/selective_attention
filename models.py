from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


import random
import itertools


author = 'AnnaK'

doc = """
Definition of Constants and Players
"""


class Constants(BaseConstants):
    name_in_url = 'my_experiment'
    players_per_group = None
    num_rounds = 1

    prolific_redirect = "399A651C"

    c_l = [0.25, 0.75]
    c_low = "25%"
    c_h = [0.75, 0.25]
    c_high = "75%"
    c_high_int = 75
    c_low_int = 25

    h = [0.8, 0.2]
    Type1_true = "20%"
    l = [0.2, 0.8]
    Type2_true = "80%"

    Type1 = "Typ 1 (unzuverlässig)"
    Type2 = "Typ 2 (zuverlässig)"

    label = "FALSE"

    pages_per_block = 10

    p1 = "Pic1"
    p2 = "Pic2"
    p3 = "Pic3"
    p4 = "Pic4"
    p5 = "Pic5"
    p6 = "Pic6"
    p7 = "Pic7"
    p8 = "Pic8"
    p9 = "Pic9"
    p10 = "Pic10"
    p11 = "Pic11"
    p12 = "Pic12"
    p13 = "Pic13"
    p14 = "Pic14"
    p15 = "Pic15"
    p16 = "Pic16"
    p17 = "Pic17"
    p18 = "Pic18"
    p19 = "Pic19"
    p20 = "Pic20"
    p21 = "Pic21"
    p22 = "Pic22"
    p23 = "Pic23"
    p24 = "Pic24"
    p25 = "Pic25"
    p26 = "Pic26"
    p27 = "Pic27"
    p28 = "Pic28"
    p29 = "Pic29"
    p30 = "Pic30"
    p31 = "Pic31"
    p32 = "Pic32"
    p33 = "Pic33"
    p34 = "Pic34"
    p35 = "Pic35"
    p36 = "Pic36"
    p37 = "Pic37"
    p38 = "Pic38"
    p39 = "Pic39"
    p40 = "Pic40"
    p41 = "Pic41"
    p42 = "Pic42"
    p43 = "Pic43"
    p44 = "Pic44"
    p45 = "Pic45"
    p46 = "Pic46"
    p47 = "Pic47"
    p48 = "Pic48"
    p49 = "Pic49"
    p50 = "Pic50"
    p51 = "Pic51"
    p52 = "Pic52"
    p53 = "Pic53"
    p54 = "Pic54"
    p55 = "Pic55"
    p56 = "Pic56"
    p57 = "Pic57"
    p58 = "Pic58"
    p59 = "Pic59"
    p60 = "Pic60"
    p61 = "Pic61"
    p62 = "Pic62"
    p63 = "Pic63"

    pic_list = [p4, p5, p6, p7, p8, p9, p10,
                p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,
                p21, p22, p23, p24, p25, p26, p27, p28, p29, p30,
                p31, p32, p33, p34, p35, p36, p37, p38, p39, p40,
                 p41, p42, p43, p44, p45, p46, p47, p48, p49, p50,
                 p51, p52, p53, p54, p55, p56, p57, p58, p59, p60,
                 p61]



class Subsession(BaseSubsession):
    pass

    def creating_session(self):
        for player in self.get_players():
            player.participant.vars["treatment"] = player.treatment()
            player.participant.vars["blocks"] = player.blocks()
            player.participant.vars["sources"] = player.sources()
            player.participant.vars["sourcetype_1"] = player.sourcetype_1()
            player.participant.vars["sourcetype_91"] = player.sourcetype_91()
            player.participant.vars["sourcetype_10"] = player.sourcetype_10()
            player.participant.vars["statementtype_1"] = player.statementtype_1()
            player.participant.vars["statementtype_91"] = player.statementtype_91()
            player.participant.vars["statementtype_10"] = player.statementtype_10()
            player.participant.vars["factcheck_1_high"] = player.factcheck_1_high()
            player.participant.vars["factcheck_10_high"] = player.factcheck_10_high()
            player.participant.vars["factcheck_91_high"] = player.factcheck_91_high()
            player.participant.vars["factcheck_1_low"] = player.factcheck_1_low()
            player.participant.vars["factcheck_10_low"] = player.factcheck_10_low()
            player.participant.vars["factcheck_91_low"] = player.factcheck_91_low()
            player.participant.vars["labels_1_low"] = player.labels_1_low()
            player.participant.vars["labels_10_low"] = player.labels_10_low()
            player.participant.vars["labels_91_low"] = player.labels_91_low()
            player.participant.vars["labels_1_high"] = player.labels_1_high()
            player.participant.vars["labels_10_high"] = player.labels_10_high()
            player.participant.vars["labels_91_high"] = player.labels_91_high()
            player.participant.vars["apply_labels_1_low"] = player.apply_labels_1_low()
            player.participant.vars["apply_labels_10_low"] = player.apply_labels_10_low()
            player.participant.vars["apply_labels_91_low"] = player.apply_labels_91_low()
            player.participant.vars["apply_labels_1_high"] = player.apply_labels_1_high()
            player.participant.vars["apply_labels_10_high"] = player.apply_labels_10_high()
            player.participant.vars["apply_labels_91_high"] = player.apply_labels_91_high()


class Group(BaseGroup):
    pass



class Player(BasePlayer):

    party = models.StringField(
        choices=["Democrat", "Republican", "Independent", "Other"],
        label="In politics, as of today, do you consider yourself a Republican, a Democrat or an Independent?",
        widget=widgets.RadioSelect,
    )

    media = models.StringField(
        choices=["Several hours per day", "About an hour per day", "Less than an hour per day",
                 "Several times per week", "Once per week", "Several times per month", "Once per month",
                 "Never"],
        label="How often do you use social media sites like Facebook, Twitter etc.?",
        widget=widgets.RadioSelect,
    )

    factchecking_realworld = models.FloatField(
        label="Please insert a number between 0 and 100.",
              min=0, max=100)

    cognitive = models.FloatField(label="", min=0)

    certainty_10 = models.FloatField(label="", min=0, max=100)
    certainty_1 = models.FloatField(label="", min=0, max=100)
    certainty_91 = models.FloatField(label="", min=0, max=100)
    certainty_blur = models.FloatField(label="", min=0, max=100)

    control1 = models.IntegerField(label="", min=0, max=100)
    control2 = models.IntegerField(label="", min=0, max=100)
    control3 = models.IntegerField(label="", min=0, max=100)
    control4 = models.IntegerField(label="", min=0, max=100)
    control5 = models.IntegerField(label="", min=0, max=100)
    control_blur = models.StringField(
        choices=["The blurred statements are never checked by the fact checker.",
                 "The blurred statements are checked with the same probability as the other statements."],
        label="Which of the following statements is true?",
        widget=widgets.RadioSelect,
    )
    control_blur_X = models.StringField(
        choices=["The blurred statement is never checked by the fact checker.",
                 "The blurred statement is checked with the same probability as the other statements."],
        label="Which of the following statements is true?",
        widget=widgets.RadioSelect,
    )

    def sources(self):
        r = random.Random(self.id_in_group + 1)
        all_sources = Constants.pic_list.copy()
        r.shuffle(all_sources)
        n = 40
        self.sources = all_sources[:n]
        return self.sources

    def sourcetype_1(self):
        r = random.Random(self.id_in_group + 2)
        n = 10
        self.sourcetype_1 = r.choices([1, 2], k=n)
        return self.sourcetype_1

    def statementtype_1(self):
        r = random.Random(self.id_in_group + 3)
        t = self.sourcetype_1
        self.statementtype_1 = []
        for s in t:
            if s == 1:
                a = r.choices([1, 0], weights=Constants.h, k=1)
                self.statementtype_1.append(a[0])
            if s == 2:
                a = r.choices([1, 0], weights=Constants.l, k=1)
                self.statementtype_1.append(a[0])
        return self.statementtype_1

    def factcheck_1_high(self):
        r = random.Random(self.id_in_group + 4)
        n = 10
        self.factcheck_1_high = r.choices([1, 0], weights=Constants.c_h, k=n)
        return self.factcheck_1_high

    def factcheck_1_low(self):
        r = random.Random(self.id_in_group + 5)
        n = 10
        self.factcheck_1_low = r.choices([1, 0], weights=Constants.c_l, k=n)
        return self.factcheck_1_low

    def labels_1_high(self):
        statements = self.statementtype_1
        check = self.factcheck_1_high
        self.labels_1_high = []
        n = 10
        for i in range(n):
            s = statements[i]
            c = check[i]
            if s == 1 and c == 1:
                self.labels_1_high.append(1)
            else:
                self.labels_1_high.append(0)
        return self.labels_1_high

    def labels_1_low(self):
        statements = self.statementtype_1
        check = self.factcheck_1_low
        self.labels_1_low = []
        n = 10
        for i in range(n):
            s = statements[i]
            c = check[i]
            if s == 1 and c == 1:
                self.labels_1_low.append(1)
            else:
                self.labels_1_low.append(0)
        return self.labels_1_low

    def apply_labels_1_high(self):
        label = Constants.label
        labels = self.labels_1_high
        application_1_high = []
        n = 10
        for j in range(n):
            l = labels[j]
            if l == 0:
                application_1_high.append(" ")
            if l == 1:
                application_1_high.append(label)
        return application_1_high

    def apply_labels_1_low(self):
        label = Constants.label
        labels = self.labels_1_low
        application_1_low = []
        n = 10
        for j in range(n):
            l = labels[j]
            if l == 0:
                application_1_low.append(" ")
            if l == 1:
                application_1_low.append(label)
        return application_1_low

    def sourcetype_91(self):
        r = random.Random(self.id_in_group + 91)
        n = 10
        self.sourcetype_91 = r.choices([1, 2], k=n)
        return self.sourcetype_91

    def statementtype_91(self):
        r = random.Random(self.id_in_group + 93)
        t = self.sourcetype_91
        m = 10
        self.statementtype_91 = []
        for s in t:
            if s == 1:
                a = r.choices([1, 0], weights=Constants.h, k=m)
                self.statementtype_91.append(a)
            if s == 2:
                a = r.choices([1, 0], weights=Constants.l, k=m)
                self.statementtype_91.append(a)
        return self.statementtype_91

    def factcheck_91_high(self):
        r = random.Random(self.id_in_group + 94)
        n = 10
        m = 9
        self.factcheck_91_high = []
        for i in range(n):
            check = r.choices([1, 0], weights=Constants.c_h, k=m)
            self.factcheck_91_high.append(check)
        return self.factcheck_91_high

    def factcheck_91_low(self):
        r = random.Random(self.id_in_group + 94)
        n = 10
        m = 9
        self.factcheck_91_low = []
        for i in range(n):
            check = r.choices([1, 0], weights=Constants.c_l, k=m)
            self.factcheck_91_low.append(check)
        return self.factcheck_91_low

    def labels_91_high(self):
        statements = self.statementtype_91
        check = self.factcheck_91_high
        self.labels_91_high = []
        n = 10
        m = 9
        for i in range(n):
            aux = []
            for j in range(m):
                s = statements[i][j]
                c = check[i][j]
                if s == 1 and c == 1:
                    aux.append(1)
                else:
                    aux.append(0)
            self.labels_91_high.append(aux)
        return self.labels_91_high

    def labels_91_low(self):
        statements = self.statementtype_91
        check = self.factcheck_91_low
        self.labels_91_low = []
        n = 10
        m = 9
        for i in range(n):
            aux = []
            for j in range(m):
                s = statements[i][j]
                c = check[i][j]
                if s == 1 and c == 1:
                    aux.append(1)
                else:
                    aux.append(0)
            self.labels_91_low.append(aux)
        return self.labels_91_low

    def apply_labels_91_high(self):
        label = Constants.label
        labels = self.labels_91_high
        application_91_high = []
        n = 10
        for j in range(n):
            aux = []
            l = labels[j]
            for k in l:
                if k == 0:
                    aux.append(" ")
                if k == 1:
                    aux.append(label)
            application_91_high.append(aux)
        return application_91_high

    def apply_labels_91_low(self):
        label = Constants.label
        labels = self.labels_91_low
        application_91_low = []
        n = 10
        for j in range(n):
            aux = []
            l = labels[j]
            for k in l:
                if k == 0:
                    aux.append(" ")
                if k == 1:
                    aux.append(label)
            application_91_low.append(aux)
        return application_91_low

    def sourcetype_10(self):
        r = random.Random(self.id_in_group + 10)
        n = 20
        self.sourcetype_10 = r.choices([1, 2], k=n)
        return self.sourcetype_10

    def statementtype_10(self):
        r = random.Random(self.id_in_group + 11)
        t = self.sourcetype_10
        m = 10
        self.statementtype_10 = []
        for s in t:
            if s == 1:
                a = r.choices([1, 0], weights=Constants.h, k=m)
                self.statementtype_10.append(a)
            if s == 2:
                a = r.choices([1, 0], weights=Constants.l, k=m)
                self.statementtype_10.append(a)
        return self.statementtype_10

    def factcheck_10_high(self):
        r = random.Random(self.id_in_group + 12)
        n = 20
        m = 10
        self.factcheck_10_high = []
        for i in range(n):
            check = r.choices([1, 0], weights=Constants.c_h, k=m)
            self.factcheck_10_high.append(check)
        return self.factcheck_10_high

    def factcheck_10_low(self):
        r = random.Random(self.id_in_group + 12)
        n = 20
        m = 10
        self.factcheck_10_low = []
        for i in range(n):
            check = r.choices([1, 0], weights=Constants.c_l, k=m)
            self.factcheck_10_low.append(check)
        return self.factcheck_10_low

    def labels_10_high(self):
        statements = self.statementtype_10
        check = self.factcheck_10_high
        self.labels_10_high = []
        n = 20
        m = 10
        for i in range(n):
            aux = []
            for j in range(m):
                s = statements[i][j]
                c = check[i][j]
                if s == 1 and c == 1:
                    aux.append(1)
                else:
                    aux.append(0)
            self.labels_10_high.append(aux)
        return self.labels_10_high

    def labels_10_low(self):
        statements = self.statementtype_10
        check = self.factcheck_10_low
        self.labels_10_low = []
        n = 20
        m = 10
        for i in range(n):
            aux = []
            for j in range(m):
                s = statements[i][j]
                c = check[i][j]
                if s == 1 and c == 1:
                    aux.append(1)
                else:
                    aux.append(0)
            self.labels_10_low.append(aux)
        return self.labels_10_low

    def apply_labels_10_high(self):
        label = Constants.label
        labels = self.labels_10_high
        application_10_high = []
        n = 20
        for j in range(n):
            aux = []
            l = labels[j]
            for k in l:
                if k == 0:
                    aux.append(" ")
                if k == 1:
                    aux.append(label)
            application_10_high.append(aux)
        return application_10_high

    def apply_labels_10_low(self):
        label = Constants.label
        labels = self.labels_10_low
        application_10_low = []
        n = 20
        for j in range(n):
            aux = []
            l = labels[j]
            for k in l:
                if k == 0:
                    aux.append(" ")
                if k == 1:
                    aux.append(label)
            application_10_low.append(aux)
        return application_10_low

    def control_full(self):
        c1 = self.control1
        c2 = self.control2
        c3 = self.control3
        c4 = self.control4
        c5 = self.control5
        check = self.check_order()
        full = 0
        if c1 != 0:
            full = full + 1
        if check == "high_low":
            if c2 != 75:
                full = full + 1
        if check == "low_high":
            if c2 != 25:
                full = full + 1
        if c3 != 80:
            full = full + 1
        if c4 != 20:
            full = full + 1
        if c5 != 50:
            full = full + 1
        self.control_full = full
        return self.control_full

    def control_full1(self):
        c1 = self.control1
        c2 = self.control2
        c3 = self.control3
        c4 = self.control4
        c5 = self.control5
        check = self.check_order1()
        full = 0
        if c1 != 0:
            full = full + 1
        if check == "high_low":
            if c2 != 75:
                full = full + 1
        if check == "low_high":
            if c2 != 25:
                full = full + 1
        if c3 != 80:
            full = full + 1
        if c4 != 20:
            full = full + 1
        if c5 != 50:
            full = full + 1
        self.control_full1 = full
        return self.control_full1

    def control_blur_wrong(self):
        cb = self.control_blur
        b = -1
        if cb != "The blurred statements are never checked by the fact checker.":
            b = b + 1
        self.control_blur_wrong= b
        return self.control_blur_wrong

    def control_blur_wrong_X(self):
        cb = self.control_blur_X
        b = -1
        if cb != "The blurred statements are never checked by the fact checker.":
            b = b + 1
        self.control_blur_wrong_X= b
        return self.control_blur_wrong_X

    def check_order(self):
        r = random.Random(self.id_in_group + 13)
        o = ["low_high", "high_low"]
        r.shuffle(o)
        self.check_order = o[0]
        return self.check_order

    def check_order1(self):
        r = random.Random(self.id_in_group + 13)
        o = ["low_high", "high_low"]
        r.shuffle(o)
        self.check_order1 = o[0]
        return self.check_order1

    def treatment(self):
        r = random.Random(self.id_in_group + 13)
        o = ["low", "high"]
        r.shuffle(o)
        self.treatment = o[0]
        return self.treatment

    def block_order(self):
        r = random.Random(self.id_in_group + 14)
        o = ["10_9_1", "10_1_9", "9_1_10", "9_10_1", "1_9_10", "1_10_9"]
        r.shuffle(o)
        order = o[0]
        return order

    def blocks(self):
        r = random.Random(self.id_in_group + 14)
        o = ["10_9_1", "10_1_9", "9_1_10", "9_10_1", "1_9_10", "1_10_9"]
        r.shuffle(o)
        self.blocks = o[0]
        return self.blocks

    def blocks2(self):
        r = random.Random(self.id_in_group + 14)
        o = ["10_9_1", "10_1_9", "9_1_10", "9_10_1", "1_9_10", "1_10_9"]
        r.shuffle(o)
        self.blocks2 = o[0]
        return self.blocks2

    timeSpent_Welcome = models.FloatField()
    timeSpent_Payment = models.FloatField()
    timeSpent_Instructions_BackAndForth = models.FloatField()
    timeSpent_Cognitive = models.FloatField()
    timeSpent_Demo_b1_1a1 = models.FloatField()
    timeSpent_Demo_b1_1b1 = models.FloatField()
    timeSpent_Demo_b1_91a1 = models.FloatField()
    timeSpent_Demo_b1_91b1 = models.FloatField()
    timeSpent_Demo_b1_101a1 = models.FloatField()
    timeSpent_Demo_b1_101b1 = models.FloatField()
    timeSpent_Demo_b1_blurreda = models.FloatField()
    timeSpent_Demo_b1_blurredb = models.FloatField()
    timeSpent_Instructions_b1_1a = models.FloatField()
    timeSpent_Instructions_b1_1b = models.FloatField()
    timeSpent_Instructions_b1_10a = models.FloatField()
    timeSpent_Instructions_b1_10b = models.FloatField()
    timeSpent_Instructions_b1_91a = models.FloatField()
    timeSpent_Instructions_b1_91b = models.FloatField()
    timeSpent_Instructions_b1_blurreda = models.FloatField()
    timeSpent_Instructions_b1_blurredb = models.FloatField()
    timeSpent_Instructions_Control = models.FloatField()
    timeSpent_Instructions_ControlOK = models.FloatField()
    timeSpent_Instructions_ControlOK1 = models.FloatField()
    timeSpent_Instructions_Control_blur = models.FloatField()
    timeSpent_Instructions_Control_blur_X = models.FloatField()
    timeSpent_Instructions_Control_blurOK = models.FloatField()
    timeSpent_Instructions_Control_blurOK_X = models.FloatField()
    timeSpent_Main_b1_101 = models.FloatField()
    timeSpent_Main_b1_102 = models.FloatField()
    timeSpent_Main_b1_103 = models.FloatField()
    timeSpent_Main_b1_104 = models.FloatField()
    timeSpent_Main_b1_105 = models.FloatField()
    timeSpent_Main_b1_106 = models.FloatField()
    timeSpent_Main_b1_107 = models.FloatField()
    timeSpent_Main_b1_108 = models.FloatField()
    timeSpent_Main_b1_109 = models.FloatField()
    timeSpent_Main_b1_110 = models.FloatField()
    timeSpent_Main_b1_901 = models.FloatField()
    timeSpent_Main_b1_902 = models.FloatField()
    timeSpent_Main_b1_903 = models.FloatField()
    timeSpent_Main_b1_904 = models.FloatField()
    timeSpent_Main_b1_905 = models.FloatField()
    timeSpent_Main_b1_906 = models.FloatField()
    timeSpent_Main_b1_907 = models.FloatField()
    timeSpent_Main_b1_908 = models.FloatField()
    timeSpent_Main_b1_909 = models.FloatField()
    timeSpent_Main_b1_910 = models.FloatField()
    timeSpent_Main_b1_1001 = models.FloatField()
    timeSpent_Main_b1_1002 = models.FloatField()
    timeSpent_Main_b1_1003 = models.FloatField()
    timeSpent_Main_b1_1004 = models.FloatField()
    timeSpent_Main_b1_1005 = models.FloatField()
    timeSpent_Main_b1_1006 = models.FloatField()
    timeSpent_Main_b1_1007 = models.FloatField()
    timeSpent_Main_b1_1008 = models.FloatField()
    timeSpent_Main_b1_1009 = models.FloatField()
    timeSpent_Main_b1_1010 = models.FloatField()
    timeSpent_Main_b1_1011 = models.FloatField()
    timeSpent_Main_b1_1012 = models.FloatField()
    timeSpent_Main_b1_1013 = models.FloatField()
    timeSpent_Main_b1_1014 = models.FloatField()
    timeSpent_Main_b1_1015 = models.FloatField()
    timeSpent_Main_b1_1016 = models.FloatField()
    timeSpent_Main_b1_1017 = models.FloatField()
    timeSpent_Main_b1_1018 = models.FloatField()
    timeSpent_Main_b1_1019 = models.FloatField()
    timeSpent_Main_b1_1020 = models.FloatField()
    timeSpent_Main_b1_blurred = models.FloatField()
    timeSpent_Slider_b1_1 = models.FloatField()
    timeSpent_Slider_b1_10 = models.FloatField()
    timeSpent_Slider_b1_91 = models.FloatField()
    timeSpent_Slider_b1_blur = models.FloatField()
    timeSpent_Survey1 = models.FloatField()
    timeSpent_Survey2 = models.FloatField()
    timeSpent_Survey3 = models.FloatField()

    demo_true = models.IntegerField(label="", min=0, max=100, blank=True)
    demo_11_true = models.IntegerField(label="", min=0, max=100)
    demo_91_true = models.IntegerField(label="", min=0, max=100)
    demo_10_true = models.IntegerField(label="", min=0, max=100)
    demo_blurred_true = models.IntegerField(label="", min=0, max=100)

    prob_11_true = models.IntegerField(label="", min=0, max=100)
    prob_12_true = models.IntegerField(label="", min=0, max=100)
    prob_13_true = models.IntegerField(label="", min=0, max=100)
    prob_14_true = models.IntegerField(label="", min=0, max=100)
    prob_15_true = models.IntegerField(label="", min=0, max=100)
    prob_16_true = models.IntegerField(label="", min=0, max=100)
    prob_17_true = models.IntegerField(label="", min=0, max=100)
    prob_18_true = models.IntegerField(label="", min=0, max=100)
    prob_19_true = models.IntegerField(label="", min=0, max=100)
    prob_110_true = models.IntegerField(label="", min=0, max=100)

    prob_911_true = models.IntegerField(label="", min=0, max=100)
    prob_912_true = models.IntegerField(label="", min=0, max=100)
    prob_913_true = models.IntegerField(label="", min=0, max=100)
    prob_914_true = models.IntegerField(label="", min=0, max=100)
    prob_915_true = models.IntegerField(label="", min=0, max=100)
    prob_916_true = models.IntegerField(label="", min=0, max=100)
    prob_917_true = models.IntegerField(label="", min=0, max=100)
    prob_918_true = models.IntegerField(label="", min=0, max=100)
    prob_919_true = models.IntegerField(label="", min=0, max=100)
    prob_9110_true = models.IntegerField(label="", min=0, max=100)

    prob_101_true = models.IntegerField(label="", min=0, max=100)
    prob_102_true = models.IntegerField(label="", min=0, max=100)
    prob_103_true = models.IntegerField(label="", min=0, max=100)
    prob_104_true = models.IntegerField(label="", min=0, max=100)
    prob_105_true = models.IntegerField(label="", min=0, max=100)
    prob_106_true = models.IntegerField(label="", min=0, max=100)
    prob_107_true = models.IntegerField(label="", min=0, max=100)
    prob_108_true = models.IntegerField(label="", min=0, max=100)
    prob_109_true = models.IntegerField(label="", min=0, max=100)
    prob_1010_true = models.IntegerField(label="", min=0, max=100)
    prob_1011_true = models.IntegerField(label="", min=0, max=100)
    prob_1012_true = models.IntegerField(label="", min=0, max=100)
    prob_1013_true = models.IntegerField(label="", min=0, max=100)
    prob_1014_true = models.IntegerField(label="", min=0, max=100)
    prob_1015_true = models.IntegerField(label="", min=0, max=100)
    prob_1016_true = models.IntegerField(label="", min=0, max=100)
    prob_1017_true = models.IntegerField(label="", min=0, max=100)
    prob_1018_true = models.IntegerField(label="", min=0, max=100)
    prob_1019_true = models.IntegerField(label="", min=0, max=100)
    prob_1020_true = models.IntegerField(label="", min=0, max=100)

    prob_blurred_true = models.IntegerField(label="", min=0, max=100)


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group',
           "sources", "blocks", "treatment",
           "sourcetype_1", "sourcetype_91", "sourcetype_10",
           "statementtype_10", "statementtype_1", "statementtype_91",
           "factcheck_1_low", "factcheck_10_low", "factcheck_91_low",
           "factcheck_1_high", "factcheck_91_high", "factcheck_10_high",
           "labels_1_low", "labels_10_low", "labels_91_low",
           "labels_1_high", "labels_10_high", "labels_91_high",
           "apply_labels_1_low", "apply_labels_10_low", "apply_labels_91_low",
           "apply_labels_1_high", "apply_labels_10_high", "apply_labels_91_high",
           ]
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group,
               p.participant.vars.get("sources", None),
               p.participant.vars.get("blocks", None),
               p.participant.vars.get("treatment", None),
               p.participant.vars.get("sourcetype_1", None),
               p.participant.vars.get("sourcetype_91", None),
               p.participant.vars.get("sourcetype_10", None),
               p.participant.vars.get("statementtype_10", None),
               p.participant.vars.get("statementtype_1", None),
               p.participant.vars.get("statementtype_91", None),
               p.participant.vars.get("factcheck_1_low", None),
               p.participant.vars.get("factcheck_10_low", None),
               p.participant.vars.get("factcheck_91_low", None),
               p.participant.vars.get("factcheck_1_high", None),
               p.participant.vars.get("factcheck_91_high", None),
               p.participant.vars.get("factcheck_10_high", None),
               p.participant.vars.get("labels_1_low", None),
               p.participant.vars.get("labels_10_low", None),
               p.participant.vars.get("labels_91_low", None),
               p.participant.vars.get("labels_1_high", None),
               p.participant.vars.get("labels_10_high", None),
               p.participant.vars.get("labels_91_high", None),
               p.participant.vars.get("apply_labels_1_low", None),
               p.participant.vars.get("apply_labels_10_low", None),
               p.participant.vars.get("apply_labels_91_low", None),
               p.participant.vars.get("apply_labels_1_high", None),
               p.participant.vars.get("apply_labels_10_high", None),
               p.participant.vars.get("apply_labels_91_high", None),
               ]




