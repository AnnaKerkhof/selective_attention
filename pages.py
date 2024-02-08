from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#from otree.models import player


class WelcomePage(Page):
    form_model = "player"
    form_fields = ["timeSpent_Welcome"]

class Payment(Page):

    form_model = "player"
    form_fields = ["timeSpent_Payment"]


class RedirectProlific(Page):
    pass


class Instructions_BackAndForth(Page):
    form_model = "player"
    form_fields = ["demo_true",
                   "timeSpent_Instructions_BackAndForth"]


class Cognitive(Page):
    form_model = "player"
    form_fields = ["cognitive", "timeSpent_Cognitive"]


class Survey1(Page):
    form_model = "player"
    form_fields = ["party", "timeSpent_Survey1"]


class Survey2(Page):
    form_model = "player"
    form_fields = ["media", "timeSpent_Survey2"]


class Survey3(Page):
    form_model = "player"
    form_fields = ["factchecking_realworld", "timeSpent_Survey3"]


class Slider_b1_blur(Page):

    form_model = "player"
    form_fields = ["certainty_blur", "timeSpent_Slider_b1_blur"]


class Slider_b1_1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "1_9_10"

    form_model = "player"
    form_fields = ["certainty_1", "timeSpent_Slider_b1_1"]


class Slider_b1_1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "9_1_10"

    form_model = "player"
    form_fields = ["certainty_1", "timeSpent_Slider_b1_1"]


class Slider_b1_1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "9_10_1"

    form_model = "player"
    form_fields = ["certainty_1", "timeSpent_Slider_b1_1"]


class Slider_b1_10_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    form_model = "player"
    form_fields = ["certainty_10", "timeSpent_Slider_b1_10"]


class Slider_b1_10_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    form_model = "player"
    form_fields = ["certainty_10", "timeSpent_Slider_b1_10"]


class Slider_b1_10_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    form_model = "player"
    form_fields = ["certainty_10", "timeSpent_Slider_b1_10"]


class Slider_b1_91_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    form_model = "player"
    form_fields = ["certainty_91", "timeSpent_Slider_b1_91"]


class Slider_b1_91_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "1_9_10"

    form_model = "player"
    form_fields = ["certainty_91", "timeSpent_Slider_b1_91"]


class Slider_b1_91_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    form_model = "player"
    form_fields = ["certainty_91", "timeSpent_Slider_b1_91"]




##### INSTRUCTIONS
########################################################################################################################
########################################################################################################################

class Instructions_Control(Page):
    form_model = "player"
    form_fields = ["control1", "control2", "control3", "control4", "control5",  "timeSpent_Instructions_Control"]


class Instructions_Control_blur_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10" or o == "9_10_1"

    form_model = "player"
    form_fields = ["control_blur",  "timeSpent_Instructions_Control_blur"]


class Instructions_Control_blur_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "10_9_1"

    form_model = "player"
    form_fields = ["control_blur",  "timeSpent_Instructions_Control_blur"]


class Instructions_Control_blur_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "10_1_9"

    form_model = "player"
    form_fields = ["control_blur",  "timeSpent_Instructions_Control_blur"]


class Instructions_Control_blur_X(Page):

    form_model = "player"
    form_fields = ["control_blur_X",  "timeSpent_Instructions_Control_blur_X"]


class Instructions_ControlOK(Page):
    def is_displayed(self):
        c = self.player.control_full()
        return c == 0

    form_model = "player"
    form_fields = ["timeSpent_Instructions_ControlOK"]


class Instructions_ControlOK1(Page):
    def is_displayed(self):
        c = self.player.control_full1()
        return c != 0

    form_model = "player"
    form_fields = ["timeSpent_Instructions_ControlOK1"]


class Instructions_Control_blurOK_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10" or o == "9_10_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_Control_blurOK"]


class Instructions_Control_blurOK_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "10_9_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_Control_blurOK"]


class Instructions_Control_blurOK_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "10_1_9"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_Control_blurOK"]


class Instructions_Control_blurOK_X(Page):

    form_model = "player"
    form_fields = ["timeSpent_Instructions_Control_blurOK_X"]


class Instructions_b1_1a_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "1_9_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_1a"]


class Instructions_b1_1a_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_1a"]


class Instructions_b1_1a_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "9_10_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_1a"]


class Instructions_b1_1b_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "1_9_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_1b"]


class Instructions_b1_1b_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_1b"]


class Instructions_b1_1b_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "9_10_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_1b"]


class Instructions_b1_10a_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_10a"]


class Instructions_b1_10a_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_10a"]


class Instructions_b1_10a_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_10a"]


class Instructions_b1_10b_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_10b"]


class Instructions_b1_10b_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_10b"]


class Instructions_b1_10b_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_10b"]


class Instructions_b1_91a_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_91a"]


class Instructions_b1_91a_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "1_9_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_91a"]


class Instructions_b1_91a_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_91a"]


class Instructions_b1_91b_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_91b"]


class Instructions_b1_91b_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "1_9_10"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_91b"]


class Instructions_b1_91b_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_91b"]


class Instructions_b1_blurreda(Page):

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_blurreda"]


class Instructions_b1_blurredb(Page):

    form_model = "player"
    form_fields = ["timeSpent_Instructions_b1_blurredb"]


##### DEMOS
########################################################################################################################
########################################################################################################################

class Demo_b1_blurreda(Page):

    form_model = "player"
    form_fields = ["demo_blurred_true", "timeSpent_Demo_b1_blurreda"]


class Demo_b1_blurredb(Page):

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_blurredb"]


class Demo_b1_1a1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    form_model = "player"
    form_fields = ["demo_11_true", "timeSpent_Demo_b1_1a1"]


class Demo_b1_1b1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_1b1"]


class Demo_b1_1a1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10" or o == "10_1_9"

    form_model = "player"
    form_fields = ["demo_11_true", "timeSpent_Demo_b1_1a1"]


class Demo_b1_1b1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10" or o == "10_1_9"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_1b1"]


class Demo_b1_1a1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    form_model = "player"
    form_fields = ["demo_11_true", "timeSpent_Demo_b1_1a1"]


class Demo_b1_1b1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_1b1"]


class Demo_b1_91a1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    form_model = "player"
    form_fields = ["demo_91_true",
                   "timeSpent_Demo_b1_91a1"]


class Demo_b1_91a1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "1_9_10"

    form_model = "player"
    form_fields = ["demo_91_true",
                   "timeSpent_Demo_b1_91a1"]


class Demo_b1_91a1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    form_model = "player"
    form_fields = ["demo_91_true",
                   "timeSpent_Demo_b1_91a1"]


class Demo_b1_91b1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_91b1"]


class Demo_b1_91b1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1" or o == "1_9_10"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_91b1"]


class Demo_b1_91b1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_91b1"]


class Demo_b1_101a1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    form_model = "player"
    form_fields = ["demo_10_true",
                   "timeSpent_Demo_b1_101a1"]


class Demo_b1_101a1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "1_10_9"

    form_model = "player"
    form_fields = ["demo_10_true",
                   "timeSpent_Demo_b1_101a1"]


class Demo_b1_101a1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    form_model = "player"
    form_fields = ["demo_10_true",
                   "timeSpent_Demo_b1_101a1"]


class Demo_b1_101b1_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_101b1"]


class Demo_b1_101b1_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "1_10_9"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_101b1"]


class Demo_b1_101b1_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    form_model = "player"
    form_fields = ["timeSpent_Demo_b1_101b1"]



##### MAIN
########################################################################################################################
########################################################################################################################

class Main_b1_blurred(Page):
    form_model = "player"
    form_fields = ["prob_blurred_true", "timeSpent_Main_b1_blurred"]


class Main_b1_101_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[0]
        t = self.player.sourcetype_1()[0]
        s = self.player.statementtype_1()[0]
        f_h = self.player.factcheck_1_high()[0]
        l_h = self.player.labels_1_high()[0]
        a_h = self.player.apply_labels_1_high()[0]
        f_l = self.player.factcheck_1_low()[0]
        l_l = self.player.labels_1_low()[0]
        a_l = self.player.apply_labels_1_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_11_true", "timeSpent_Main_b1_101"]


class Main_b1_102_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[1]
        t = self.player.sourcetype_1()[1]
        s = self.player.statementtype_1()[1]
        f_h = self.player.factcheck_1_high()[1]
        l_h = self.player.labels_1_high()[1]
        a_h = self.player.apply_labels_1_high()[1]
        f_l = self.player.factcheck_1_low()[1]
        l_l = self.player.labels_1_low()[1]
        a_l = self.player.apply_labels_1_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_12_true", "timeSpent_Main_b1_102"]


class Main_b1_103_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[2]
        t = self.player.sourcetype_1()[2]
        s = self.player.statementtype_1()[2]
        f_h = self.player.factcheck_1_high()[2]
        l_h = self.player.labels_1_high()[2]
        a_h = self.player.apply_labels_1_high()[2]
        f_l = self.player.factcheck_1_low()[2]
        l_l = self.player.labels_1_low()[2]
        a_l = self.player.apply_labels_1_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_13_true", "timeSpent_Main_b1_103"]


class Main_b1_104_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[3]
        t = self.player.sourcetype_1()[3]
        s = self.player.statementtype_1()[3]
        f_h = self.player.factcheck_1_high()[3]
        l_h = self.player.labels_1_high()[3]
        a_h = self.player.apply_labels_1_high()[3]
        f_l = self.player.factcheck_1_low()[3]
        l_l = self.player.labels_1_low()[3]
        a_l = self.player.apply_labels_1_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_14_true", "timeSpent_Main_b1_104"]


class Main_b1_105_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[4]
        t = self.player.sourcetype_1()[4]
        s = self.player.statementtype_1()[4]
        f_h = self.player.factcheck_1_high()[4]
        l_h = self.player.labels_1_high()[4]
        a_h = self.player.apply_labels_1_high()[4]
        f_l = self.player.factcheck_1_low()[4]
        l_l = self.player.labels_1_low()[4]
        a_l = self.player.apply_labels_1_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_15_true", "timeSpent_Main_b1_105"]


class Main_b1_106_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[5]
        t = self.player.sourcetype_1()[5]
        s = self.player.statementtype_1()[5]
        f_h = self.player.factcheck_1_high()[5]
        l_h = self.player.labels_1_high()[5]
        a_h = self.player.apply_labels_1_high()[5]
        f_l = self.player.factcheck_1_low()[5]
        l_l = self.player.labels_1_low()[5]
        a_l = self.player.apply_labels_1_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_16_true", "timeSpent_Main_b1_106"]


class Main_b1_107_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[6]
        t = self.player.sourcetype_1()[6]
        s = self.player.statementtype_1()[6]
        f_h = self.player.factcheck_1_high()[6]
        l_h = self.player.labels_1_high()[6]
        a_h = self.player.apply_labels_1_high()[6]
        f_l = self.player.factcheck_1_low()[6]
        l_l = self.player.labels_1_low()[6]
        a_l = self.player.apply_labels_1_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_17_true", "timeSpent_Main_b1_107"]


class Main_b1_108_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[7]
        t = self.player.sourcetype_1()[7]
        s = self.player.statementtype_1()[7]
        f_h = self.player.factcheck_1_high()[7]
        l_h = self.player.labels_1_high()[7]
        a_h = self.player.apply_labels_1_high()[7]
        f_l = self.player.factcheck_1_low()[7]
        l_l = self.player.labels_1_low()[7]
        a_l = self.player.apply_labels_1_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_18_true", "timeSpent_Main_b1_108"]


class Main_b1_109_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[8]
        t = self.player.sourcetype_1()[8]
        s = self.player.statementtype_1()[8]
        f_h = self.player.factcheck_1_high()[8]
        l_h = self.player.labels_1_high()[8]
        a_h = self.player.apply_labels_1_high()[8]
        f_l = self.player.factcheck_1_low()[8]
        l_l = self.player.labels_1_low()[8]
        a_l = self.player.apply_labels_1_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_19_true", "timeSpent_Main_b1_109"]


class Main_b1_110_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[9]
        t = self.player.sourcetype_1()[9]
        s = self.player.statementtype_1()[9]
        f_h = self.player.factcheck_1_high()[9]
        l_h = self.player.labels_1_high()[9]
        a_h = self.player.apply_labels_1_high()[9]
        f_l = self.player.factcheck_1_low()[9]
        l_l = self.player.labels_1_low()[9]
        a_l = self.player.apply_labels_1_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_110_true", "timeSpent_Main_b1_110"]


class Main_b1_901_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[10]
        t = self.player.sourcetype_91()[0]
        s = self.player.statementtype_91()[0]
        f_h = self.player.factcheck_91_high()[0]
        l_h = self.player.labels_91_high()[0]
        a_h = self.player.apply_labels_91_high()[0]
        f_l = self.player.factcheck_91_low()[0]
        l_l = self.player.labels_91_low()[0]
        a_l = self.player.apply_labels_91_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_911_true", "timeSpent_Main_b1_901"]


class Main_b1_902_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[11]
        t = self.player.sourcetype_91()[1]
        s = self.player.statementtype_91()[1]
        f_h = self.player.factcheck_91_high()[1]
        l_h = self.player.labels_91_high()[1]
        a_h = self.player.apply_labels_91_high()[1]
        f_l = self.player.factcheck_91_low()[1]
        l_l = self.player.labels_91_low()[1]
        a_l = self.player.apply_labels_91_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_912_true", "timeSpent_Main_b1_902"]


class Main_b1_903_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[12]
        t = self.player.sourcetype_91()[2]
        s = self.player.statementtype_91()[2]
        f_h = self.player.factcheck_91_high()[2]
        l_h = self.player.labels_91_high()[2]
        a_h = self.player.apply_labels_91_high()[2]
        f_l = self.player.factcheck_91_low()[2]
        l_l = self.player.labels_91_low()[2]
        a_l = self.player.apply_labels_91_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_913_true", "timeSpent_Main_b1_903"]


class Main_b1_904_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[13]
        t = self.player.sourcetype_91()[3]
        s = self.player.statementtype_91()[3]
        f_h = self.player.factcheck_91_high()[3]
        l_h = self.player.labels_91_high()[3]
        a_h = self.player.apply_labels_91_high()[3]
        f_l = self.player.factcheck_91_low()[3]
        l_l = self.player.labels_91_low()[3]
        a_l = self.player.apply_labels_91_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_914_true", "timeSpent_Main_b1_904"]


class Main_b1_905_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[14]
        t = self.player.sourcetype_91()[4]
        s = self.player.statementtype_91()[4]
        f_h = self.player.factcheck_91_high()[4]
        l_h = self.player.labels_91_high()[4]
        a_h = self.player.apply_labels_91_high()[4]
        f_l = self.player.factcheck_91_low()[4]
        l_l = self.player.labels_91_low()[4]
        a_l = self.player.apply_labels_91_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_915_true", "timeSpent_Main_b1_905"]


class Main_b1_906_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[15]
        t = self.player.sourcetype_91()[5]
        s = self.player.statementtype_91()[5]
        f_h = self.player.factcheck_91_high()[5]
        l_h = self.player.labels_91_high()[5]
        a_h = self.player.apply_labels_91_high()[5]
        f_l = self.player.factcheck_91_low()[5]
        l_l = self.player.labels_91_low()[5]
        a_l = self.player.apply_labels_91_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_916_true", "timeSpent_Main_b1_906"]


class Main_b1_907_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[16]
        t = self.player.sourcetype_91()[6]
        s = self.player.statementtype_91()[6]
        f_h = self.player.factcheck_91_high()[6]
        l_h = self.player.labels_91_high()[6]
        a_h = self.player.apply_labels_91_high()[6]
        f_l = self.player.factcheck_91_low()[6]
        l_l = self.player.labels_91_low()[6]
        a_l = self.player.apply_labels_91_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_917_true", "timeSpent_Main_b1_907"]


class Main_b1_908_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[17]
        t = self.player.sourcetype_91()[7]
        s = self.player.statementtype_91()[7]
        f_h = self.player.factcheck_91_high()[7]
        l_h = self.player.labels_91_high()[7]
        a_h = self.player.apply_labels_91_high()[7]
        f_l = self.player.factcheck_91_low()[7]
        l_l = self.player.labels_91_low()[7]
        a_l = self.player.apply_labels_91_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_918_true",  "timeSpent_Main_b1_908"]


class Main_b1_909_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[18]
        t = self.player.sourcetype_91()[8]
        s = self.player.statementtype_91()[8]
        f_h = self.player.factcheck_91_high()[8]
        l_h = self.player.labels_91_high()[8]
        a_h = self.player.apply_labels_91_high()[8]
        f_l = self.player.factcheck_91_low()[8]
        l_l = self.player.labels_91_low()[8]
        a_l = self.player.apply_labels_91_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_919_true",  "timeSpent_Main_b1_909"]


class Main_b1_910_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[19]
        t = self.player.sourcetype_91()[9]
        s = self.player.statementtype_91()[9]
        f_h = self.player.factcheck_91_high()[9]
        l_h = self.player.labels_91_high()[9]
        a_h = self.player.apply_labels_91_high()[9]
        f_l = self.player.factcheck_91_low()[9]
        l_l = self.player.labels_91_low()[9]
        a_l = self.player.apply_labels_91_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_9110_true",  "timeSpent_Main_b1_910"]


class Main_b1_1001_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[20]
        t = self.player.sourcetype_10()[0]
        s = self.player.statementtype_10()[0]
        f_h = self.player.factcheck_10_high()[0]
        l_h = self.player.labels_10_high()[0]
        a_h = self.player.apply_labels_10_high()[0]
        f_l = self.player.factcheck_10_low()[0]
        l_l = self.player.labels_10_low()[0]
        a_l = self.player.apply_labels_10_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_101_true",
                   "timeSpent_Main_b1_1001"]


class Main_b1_1002_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[21]
        t = self.player.sourcetype_10()[1]
        s = self.player.statementtype_10()[1]
        f_h = self.player.factcheck_10_high()[1]
        l_h = self.player.labels_10_high()[1]
        a_h = self.player.apply_labels_10_high()[1]
        f_l = self.player.factcheck_10_low()[1]
        l_l = self.player.labels_10_low()[1]
        a_l = self.player.apply_labels_10_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_102_true",
                   "timeSpent_Main_b1_1002"]


class Main_b1_1003_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[22]
        t = self.player.sourcetype_10()[2]
        s = self.player.statementtype_10()[2]
        f_h = self.player.factcheck_10_high()[2]
        l_h = self.player.labels_10_high()[2]
        a_h = self.player.apply_labels_10_high()[2]
        f_l = self.player.factcheck_10_low()[2]
        l_l = self.player.labels_10_low()[2]
        a_l = self.player.apply_labels_10_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_103_true",
                   "timeSpent_Main_b1_1003"]


class Main_b1_1004_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[23]
        t = self.player.sourcetype_10()[3]
        s = self.player.statementtype_10()[3]
        f_h = self.player.factcheck_10_high()[3]
        l_h = self.player.labels_10_high()[3]
        a_h = self.player.apply_labels_10_high()[3]
        f_l = self.player.factcheck_10_low()[3]
        l_l = self.player.labels_10_low()[3]
        a_l = self.player.apply_labels_10_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_104_true",
                   "timeSpent_Main_b1_1004"]


class Main_b1_1005_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[24]
        t = self.player.sourcetype_10()[4]
        s = self.player.statementtype_10()[4]
        f_h = self.player.factcheck_10_high()[4]
        l_h = self.player.labels_10_high()[4]
        a_h = self.player.apply_labels_10_high()[4]
        f_l = self.player.factcheck_10_low()[4]
        l_l = self.player.labels_10_low()[4]
        a_l = self.player.apply_labels_10_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_105_true",
                   "timeSpent_Main_b1_1005"]


class Main_b1_1006_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[25]
        t = self.player.sourcetype_10()[5]
        s = self.player.statementtype_10()[5]
        f_h = self.player.factcheck_10_high()[5]
        l_h = self.player.labels_10_high()[5]
        a_h = self.player.apply_labels_10_high()[5]
        f_l = self.player.factcheck_10_low()[5]
        l_l = self.player.labels_10_low()[5]
        a_l = self.player.apply_labels_10_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_106_true",
                   "timeSpent_Main_b1_1006"]


class Main_b1_1007_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[26]
        t = self.player.sourcetype_10()[6]
        s = self.player.statementtype_10()[6]
        f_h = self.player.factcheck_10_high()[6]
        l_h = self.player.labels_10_high()[6]
        a_h = self.player.apply_labels_10_high()[6]
        f_l = self.player.factcheck_10_low()[6]
        l_l = self.player.labels_10_low()[6]
        a_l = self.player.apply_labels_10_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_107_true",
                   "timeSpent_Main_b1_1007"]


class Main_b1_1008_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[27]
        t = self.player.sourcetype_10()[7]
        s = self.player.statementtype_10()[7]
        f_h = self.player.factcheck_10_high()[7]
        l_h = self.player.labels_10_high()[7]
        a_h = self.player.apply_labels_10_high()[7]
        f_l = self.player.factcheck_10_low()[7]
        l_l = self.player.labels_10_low()[7]
        a_l = self.player.apply_labels_10_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_108_true",
                   "timeSpent_Main_b1_1008"]


class Main_b1_1009_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[28]
        t = self.player.sourcetype_10()[8]
        s = self.player.statementtype_10()[8]
        f_h = self.player.factcheck_10_high()[8]
        l_h = self.player.labels_10_high()[8]
        a_h = self.player.apply_labels_10_high()[8]
        f_l = self.player.factcheck_10_low()[8]
        l_l = self.player.labels_10_low()[8]
        a_l = self.player.apply_labels_10_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_109_true",
                   "timeSpent_Main_b1_1009"]


class Main_b1_1010_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[29]
        t = self.player.sourcetype_10()[9]
        s = self.player.statementtype_10()[9]
        f_h = self.player.factcheck_10_high()[9]
        l_h = self.player.labels_10_high()[9]
        a_h = self.player.apply_labels_10_high()[9]
        f_l = self.player.factcheck_10_low()[9]
        l_l = self.player.labels_10_low()[9]
        a_l = self.player.apply_labels_10_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1010_true",
                   "timeSpent_Main_b1_1010"]


class Main_b1_1011_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[30]
        t = self.player.sourcetype_10()[10]
        s = self.player.statementtype_10()[10]
        f_h = self.player.factcheck_10_high()[10]
        l_h = self.player.labels_10_high()[10]
        a_h = self.player.apply_labels_10_high()[10]
        f_l = self.player.factcheck_10_low()[10]
        l_l = self.player.labels_10_low()[10]
        a_l = self.player.apply_labels_10_low()[10]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1011_true",
                   "timeSpent_Main_b1_1011"]


class Main_b1_1012_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[31]
        t = self.player.sourcetype_10()[11]
        s = self.player.statementtype_10()[11]
        f_h = self.player.factcheck_10_high()[11]
        l_h = self.player.labels_10_high()[11]
        a_h = self.player.apply_labels_10_high()[11]
        f_l = self.player.factcheck_10_low()[11]
        l_l = self.player.labels_10_low()[11]
        a_l = self.player.apply_labels_10_low()[11]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1012_true",
                   "timeSpent_Main_b1_1012"]


class Main_b1_1013_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[32]
        t = self.player.sourcetype_10()[12]
        s = self.player.statementtype_10()[12]
        f_h = self.player.factcheck_10_high()[12]
        l_h = self.player.labels_10_high()[12]
        a_h = self.player.apply_labels_10_high()[12]
        f_l = self.player.factcheck_10_low()[12]
        l_l = self.player.labels_10_low()[12]
        a_l = self.player.apply_labels_10_low()[12]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1013_true",
                   "timeSpent_Main_b1_1013"]

class Main_b1_1014_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[33]
        t = self.player.sourcetype_10()[13]
        s = self.player.statementtype_10()[13]
        f_h = self.player.factcheck_10_high()[13]
        l_h = self.player.labels_10_high()[13]
        a_h = self.player.apply_labels_10_high()[13]
        f_l = self.player.factcheck_10_low()[13]
        l_l = self.player.labels_10_low()[13]
        a_l = self.player.apply_labels_10_low()[13]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1014_true",
                   "timeSpent_Main_b1_1014"]


class Main_b1_1015_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[34]
        t = self.player.sourcetype_10()[14]
        s = self.player.statementtype_10()[14]
        f_h = self.player.factcheck_10_high()[14]
        l_h = self.player.labels_10_high()[14]
        a_h = self.player.apply_labels_10_high()[14]
        f_l = self.player.factcheck_10_low()[14]
        l_l = self.player.labels_10_low()[14]
        a_l = self.player.apply_labels_10_low()[14]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1015_true",
                   "timeSpent_Main_b1_1015"]


class Main_b1_1016_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[35]
        t = self.player.sourcetype_10()[15]
        s = self.player.statementtype_10()[15]
        f_h = self.player.factcheck_10_high()[15]
        l_h = self.player.labels_10_high()[15]
        a_h = self.player.apply_labels_10_high()[15]
        f_l = self.player.factcheck_10_low()[15]
        l_l = self.player.labels_10_low()[15]
        a_l = self.player.apply_labels_10_low()[15]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1016_true",
                   "timeSpent_Main_b1_1016"]


class Main_b1_1017_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[36]
        t = self.player.sourcetype_10()[16]
        s = self.player.statementtype_10()[16]
        f_h = self.player.factcheck_10_high()[16]
        l_h = self.player.labels_10_high()[16]
        a_h = self.player.apply_labels_10_high()[16]
        f_l = self.player.factcheck_10_low()[16]
        l_l = self.player.labels_10_low()[16]
        a_l = self.player.apply_labels_10_low()[16]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1017_true",
                   "timeSpent_Main_b1_1017"]


class Main_b1_1018_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[37]
        t = self.player.sourcetype_10()[17]
        s = self.player.statementtype_10()[17]
        f_h = self.player.factcheck_10_high()[17]
        l_h = self.player.labels_10_high()[17]
        a_h = self.player.apply_labels_10_high()[17]
        f_l = self.player.factcheck_10_low()[17]
        l_l = self.player.labels_10_low()[17]
        a_l = self.player.apply_labels_10_low()[17]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1018_true",
                   "timeSpent_Main_b1_1018"]


class Main_b1_1019_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[38]
        t = self.player.sourcetype_10()[18]
        s = self.player.statementtype_10()[18]
        f_h = self.player.factcheck_10_high()[18]
        l_h = self.player.labels_10_high()[18]
        a_h = self.player.apply_labels_10_high()[18]
        f_l = self.player.factcheck_10_low()[18]
        l_l = self.player.labels_10_low()[18]
        a_l = self.player.apply_labels_10_low()[18]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1019_true",
                   "timeSpent_Main_b1_1019"]


class Main_b1_1020_r1(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[39]
        t = self.player.sourcetype_10()[19]
        s = self.player.statementtype_10()[19]
        f_h = self.player.factcheck_10_high()[19]
        l_h = self.player.labels_10_high()[19]
        a_h = self.player.apply_labels_10_high()[19]
        f_l = self.player.factcheck_10_low()[19]
        l_l = self.player.labels_10_low()[19]
        a_l = self.player.apply_labels_10_low()[19]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1020_true",
                   "timeSpent_Main_b1_1020"]


class Main_b1_1011_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[30]
        t = self.player.sourcetype_10()[10]
        s = self.player.statementtype_10()[10]
        f_h = self.player.factcheck_10_high()[10]
        l_h = self.player.labels_10_high()[10]
        a_h = self.player.apply_labels_10_high()[10]
        f_l = self.player.factcheck_10_low()[10]
        l_l = self.player.labels_10_low()[10]
        a_l = self.player.apply_labels_10_low()[10]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1011_true",
                   "timeSpent_Main_b1_1011"]


class Main_b1_1012_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[31]
        t = self.player.sourcetype_10()[11]
        s = self.player.statementtype_10()[11]
        f_h = self.player.factcheck_10_high()[11]
        l_h = self.player.labels_10_high()[11]
        a_h = self.player.apply_labels_10_high()[11]
        f_l = self.player.factcheck_10_low()[11]
        l_l = self.player.labels_10_low()[11]
        a_l = self.player.apply_labels_10_low()[11]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1012_true",
                   "timeSpent_Main_b1_1012"]


class Main_b1_1013_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[32]
        t = self.player.sourcetype_10()[12]
        s = self.player.statementtype_10()[12]
        f_h = self.player.factcheck_10_high()[12]
        l_h = self.player.labels_10_high()[12]
        a_h = self.player.apply_labels_10_high()[12]
        f_l = self.player.factcheck_10_low()[12]
        l_l = self.player.labels_10_low()[12]
        a_l = self.player.apply_labels_10_low()[12]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1013_true",
                   "timeSpent_Main_b1_1013"]

class Main_b1_1014_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[33]
        t = self.player.sourcetype_10()[13]
        s = self.player.statementtype_10()[13]
        f_h = self.player.factcheck_10_high()[13]
        l_h = self.player.labels_10_high()[13]
        a_h = self.player.apply_labels_10_high()[13]
        f_l = self.player.factcheck_10_low()[13]
        l_l = self.player.labels_10_low()[13]
        a_l = self.player.apply_labels_10_low()[13]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1014_true",
                   "timeSpent_Main_b1_1014"]


class Main_b1_1015_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[34]
        t = self.player.sourcetype_10()[14]
        s = self.player.statementtype_10()[14]
        f_h = self.player.factcheck_10_high()[14]
        l_h = self.player.labels_10_high()[14]
        a_h = self.player.apply_labels_10_high()[14]
        f_l = self.player.factcheck_10_low()[14]
        l_l = self.player.labels_10_low()[14]
        a_l = self.player.apply_labels_10_low()[14]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1015_true",
                   "timeSpent_Main_b1_1015"]


class Main_b1_1016_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[35]
        t = self.player.sourcetype_10()[15]
        s = self.player.statementtype_10()[15]
        f_h = self.player.factcheck_10_high()[15]
        l_h = self.player.labels_10_high()[15]
        a_h = self.player.apply_labels_10_high()[15]
        f_l = self.player.factcheck_10_low()[15]
        l_l = self.player.labels_10_low()[15]
        a_l = self.player.apply_labels_10_low()[15]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1016_true",
                   "timeSpent_Main_b1_1016"]


class Main_b1_1017_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[36]
        t = self.player.sourcetype_10()[16]
        s = self.player.statementtype_10()[16]
        f_h = self.player.factcheck_10_high()[16]
        l_h = self.player.labels_10_high()[16]
        a_h = self.player.apply_labels_10_high()[16]
        f_l = self.player.factcheck_10_low()[16]
        l_l = self.player.labels_10_low()[16]
        a_l = self.player.apply_labels_10_low()[16]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1017_true",
                   "timeSpent_Main_b1_1017"]


class Main_b1_1018_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[37]
        t = self.player.sourcetype_10()[17]
        s = self.player.statementtype_10()[17]
        f_h = self.player.factcheck_10_high()[17]
        l_h = self.player.labels_10_high()[17]
        a_h = self.player.apply_labels_10_high()[17]
        f_l = self.player.factcheck_10_low()[17]
        l_l = self.player.labels_10_low()[17]
        a_l = self.player.apply_labels_10_low()[17]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1018_true",
                   "timeSpent_Main_b1_1018"]


class Main_b1_1019_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[38]
        t = self.player.sourcetype_10()[18]
        s = self.player.statementtype_10()[18]
        f_h = self.player.factcheck_10_high()[18]
        l_h = self.player.labels_10_high()[18]
        a_h = self.player.apply_labels_10_high()[18]
        f_l = self.player.factcheck_10_low()[18]
        l_l = self.player.labels_10_low()[18]
        a_l = self.player.apply_labels_10_low()[18]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1019_true",
                   "timeSpent_Main_b1_1019"]


class Main_b1_1020_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[39]
        t = self.player.sourcetype_10()[19]
        s = self.player.statementtype_10()[19]
        f_h = self.player.factcheck_10_high()[19]
        l_h = self.player.labels_10_high()[19]
        a_h = self.player.apply_labels_10_high()[19]
        f_l = self.player.factcheck_10_low()[19]
        l_l = self.player.labels_10_low()[19]
        a_l = self.player.apply_labels_10_low()[19]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1020_true",
                   "timeSpent_Main_b1_1020"]


class Main_b1_1011_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[30]
        t = self.player.sourcetype_10()[10]
        s = self.player.statementtype_10()[10]
        f_h = self.player.factcheck_10_high()[10]
        l_h = self.player.labels_10_high()[10]
        a_h = self.player.apply_labels_10_high()[10]
        f_l = self.player.factcheck_10_low()[10]
        l_l = self.player.labels_10_low()[10]
        a_l = self.player.apply_labels_10_low()[10]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1011_true",
                   "timeSpent_Main_b1_1011"]


class Main_b1_1012_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[31]
        t = self.player.sourcetype_10()[11]
        s = self.player.statementtype_10()[11]
        f_h = self.player.factcheck_10_high()[11]
        l_h = self.player.labels_10_high()[11]
        a_h = self.player.apply_labels_10_high()[11]
        f_l = self.player.factcheck_10_low()[11]
        l_l = self.player.labels_10_low()[11]
        a_l = self.player.apply_labels_10_low()[11]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1012_true",
                   "timeSpent_Main_b1_1012"]


class Main_b1_1013_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[32]
        t = self.player.sourcetype_10()[12]
        s = self.player.statementtype_10()[12]
        f_h = self.player.factcheck_10_high()[12]
        l_h = self.player.labels_10_high()[12]
        a_h = self.player.apply_labels_10_high()[12]
        f_l = self.player.factcheck_10_low()[12]
        l_l = self.player.labels_10_low()[12]
        a_l = self.player.apply_labels_10_low()[12]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1013_true",
                   "timeSpent_Main_b1_1013"]

class Main_b1_1014_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[33]
        t = self.player.sourcetype_10()[13]
        s = self.player.statementtype_10()[13]
        f_h = self.player.factcheck_10_high()[13]
        l_h = self.player.labels_10_high()[13]
        a_h = self.player.apply_labels_10_high()[13]
        f_l = self.player.factcheck_10_low()[13]
        l_l = self.player.labels_10_low()[13]
        a_l = self.player.apply_labels_10_low()[13]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1014_true",
                   "timeSpent_Main_b1_1014"]


class Main_b1_1015_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[34]
        t = self.player.sourcetype_10()[14]
        s = self.player.statementtype_10()[14]
        f_h = self.player.factcheck_10_high()[14]
        l_h = self.player.labels_10_high()[14]
        a_h = self.player.apply_labels_10_high()[14]
        f_l = self.player.factcheck_10_low()[14]
        l_l = self.player.labels_10_low()[14]
        a_l = self.player.apply_labels_10_low()[14]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1015_true",
                   "timeSpent_Main_b1_1015"]


class Main_b1_1016_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[35]
        t = self.player.sourcetype_10()[15]
        s = self.player.statementtype_10()[15]
        f_h = self.player.factcheck_10_high()[15]
        l_h = self.player.labels_10_high()[15]
        a_h = self.player.apply_labels_10_high()[15]
        f_l = self.player.factcheck_10_low()[15]
        l_l = self.player.labels_10_low()[15]
        a_l = self.player.apply_labels_10_low()[15]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1016_true",
                   "timeSpent_Main_b1_1016"]


class Main_b1_1017_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[36]
        t = self.player.sourcetype_10()[16]
        s = self.player.statementtype_10()[16]
        f_h = self.player.factcheck_10_high()[16]
        l_h = self.player.labels_10_high()[16]
        a_h = self.player.apply_labels_10_high()[16]
        f_l = self.player.factcheck_10_low()[16]
        l_l = self.player.labels_10_low()[16]
        a_l = self.player.apply_labels_10_low()[16]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1017_true",
                   "timeSpent_Main_b1_1017"]


class Main_b1_1018_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[37]
        t = self.player.sourcetype_10()[17]
        s = self.player.statementtype_10()[17]
        f_h = self.player.factcheck_10_high()[17]
        l_h = self.player.labels_10_high()[17]
        a_h = self.player.apply_labels_10_high()[17]
        f_l = self.player.factcheck_10_low()[17]
        l_l = self.player.labels_10_low()[17]
        a_l = self.player.apply_labels_10_low()[17]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1018_true",
                   "timeSpent_Main_b1_1018"]


class Main_b1_1019_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[38]
        t = self.player.sourcetype_10()[18]
        s = self.player.statementtype_10()[18]
        f_h = self.player.factcheck_10_high()[18]
        l_h = self.player.labels_10_high()[18]
        a_h = self.player.apply_labels_10_high()[18]
        f_l = self.player.factcheck_10_low()[18]
        l_l = self.player.labels_10_low()[18]
        a_l = self.player.apply_labels_10_low()[18]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1019_true",
                   "timeSpent_Main_b1_1019"]


class Main_b1_1020_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[39]
        t = self.player.sourcetype_10()[19]
        s = self.player.statementtype_10()[19]
        f_h = self.player.factcheck_10_high()[19]
        l_h = self.player.labels_10_high()[19]
        a_h = self.player.apply_labels_10_high()[19]
        f_l = self.player.factcheck_10_low()[19]
        l_l = self.player.labels_10_low()[19]
        a_l = self.player.apply_labels_10_low()[19]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1020_true",
                   "timeSpent_Main_b1_1020"]


class Main_b1_101_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[0]
        t = self.player.sourcetype_1()[0]
        s = self.player.statementtype_1()[0]
        f_h = self.player.factcheck_1_high()[0]
        l_h = self.player.labels_1_high()[0]
        a_h = self.player.apply_labels_1_high()[0]
        f_l = self.player.factcheck_1_low()[0]
        l_l = self.player.labels_1_low()[0]
        a_l = self.player.apply_labels_1_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_11_true", "timeSpent_Main_b1_101"]


class Main_b1_101_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[0]
        t = self.player.sourcetype_1()[0]
        s = self.player.statementtype_1()[0]
        f_h = self.player.factcheck_1_high()[0]
        l_h = self.player.labels_1_high()[0]
        a_h = self.player.apply_labels_1_high()[0]
        f_l = self.player.factcheck_1_low()[0]
        l_l = self.player.labels_1_low()[0]
        a_l = self.player.apply_labels_1_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_11_true", "timeSpent_Main_b1_101"]


class Main_b1_102_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[1]
        t = self.player.sourcetype_1()[1]
        s = self.player.statementtype_1()[1]
        f_h = self.player.factcheck_1_high()[1]
        l_h = self.player.labels_1_high()[1]
        a_h = self.player.apply_labels_1_high()[1]
        f_l = self.player.factcheck_1_low()[1]
        l_l = self.player.labels_1_low()[1]
        a_l = self.player.apply_labels_1_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_12_true", "timeSpent_Main_b1_102"]


class Main_b1_102_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[1]
        t = self.player.sourcetype_1()[1]
        s = self.player.statementtype_1()[1]
        f_h = self.player.factcheck_1_high()[1]
        l_h = self.player.labels_1_high()[1]
        a_h = self.player.apply_labels_1_high()[1]
        f_l = self.player.factcheck_1_low()[1]
        l_l = self.player.labels_1_low()[1]
        a_l = self.player.apply_labels_1_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_12_true", "timeSpent_Main_b1_102"]


class Main_b1_103_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[2]
        t = self.player.sourcetype_1()[2]
        s = self.player.statementtype_1()[2]
        f_h = self.player.factcheck_1_high()[2]
        l_h = self.player.labels_1_high()[2]
        a_h = self.player.apply_labels_1_high()[2]
        f_l = self.player.factcheck_1_low()[2]
        l_l = self.player.labels_1_low()[2]
        a_l = self.player.apply_labels_1_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_13_true", "timeSpent_Main_b1_103"]


class Main_b1_103_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[2]
        t = self.player.sourcetype_1()[2]
        s = self.player.statementtype_1()[2]
        f_h = self.player.factcheck_1_high()[2]
        l_h = self.player.labels_1_high()[2]
        a_h = self.player.apply_labels_1_high()[2]
        f_l = self.player.factcheck_1_low()[2]
        l_l = self.player.labels_1_low()[2]
        a_l = self.player.apply_labels_1_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_13_true", "timeSpent_Main_b1_103"]


class Main_b1_104_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[3]
        t = self.player.sourcetype_1()[3]
        s = self.player.statementtype_1()[3]
        f_h = self.player.factcheck_1_high()[3]
        l_h = self.player.labels_1_high()[3]
        a_h = self.player.apply_labels_1_high()[3]
        f_l = self.player.factcheck_1_low()[3]
        l_l = self.player.labels_1_low()[3]
        a_l = self.player.apply_labels_1_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_14_true", "timeSpent_Main_b1_104"]


class Main_b1_104_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[3]
        t = self.player.sourcetype_1()[3]
        s = self.player.statementtype_1()[3]
        f_h = self.player.factcheck_1_high()[3]
        l_h = self.player.labels_1_high()[3]
        a_h = self.player.apply_labels_1_high()[3]
        f_l = self.player.factcheck_1_low()[3]
        l_l = self.player.labels_1_low()[3]
        a_l = self.player.apply_labels_1_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_14_true", "timeSpent_Main_b1_104"]


class Main_b1_105_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[4]
        t = self.player.sourcetype_1()[4]
        s = self.player.statementtype_1()[4]
        f_h = self.player.factcheck_1_high()[4]
        l_h = self.player.labels_1_high()[4]
        a_h = self.player.apply_labels_1_high()[4]
        f_l = self.player.factcheck_1_low()[4]
        l_l = self.player.labels_1_low()[4]
        a_l = self.player.apply_labels_1_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_15_true", "timeSpent_Main_b1_105"]


class Main_b1_105_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[4]
        t = self.player.sourcetype_1()[4]
        s = self.player.statementtype_1()[4]
        f_h = self.player.factcheck_1_high()[4]
        l_h = self.player.labels_1_high()[4]
        a_h = self.player.apply_labels_1_high()[4]
        f_l = self.player.factcheck_1_low()[4]
        l_l = self.player.labels_1_low()[4]
        a_l = self.player.apply_labels_1_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_15_true", "timeSpent_Main_b1_105"]


class Main_b1_106_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[5]
        t = self.player.sourcetype_1()[5]
        s = self.player.statementtype_1()[5]
        f_h = self.player.factcheck_1_high()[5]
        l_h = self.player.labels_1_high()[5]
        a_h = self.player.apply_labels_1_high()[5]
        f_l = self.player.factcheck_1_low()[5]
        l_l = self.player.labels_1_low()[5]
        a_l = self.player.apply_labels_1_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_16_true", "timeSpent_Main_b1_106"]


class Main_b1_106_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[5]
        t = self.player.sourcetype_1()[5]
        s = self.player.statementtype_1()[5]
        f_h = self.player.factcheck_1_high()[5]
        l_h = self.player.labels_1_high()[5]
        a_h = self.player.apply_labels_1_high()[5]
        f_l = self.player.factcheck_1_low()[5]
        l_l = self.player.labels_1_low()[5]
        a_l = self.player.apply_labels_1_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_16_true", "timeSpent_Main_b1_106"]


class Main_b1_107_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[6]
        t = self.player.sourcetype_1()[6]
        s = self.player.statementtype_1()[6]
        f_h = self.player.factcheck_1_high()[6]
        l_h = self.player.labels_1_high()[6]
        a_h = self.player.apply_labels_1_high()[6]
        f_l = self.player.factcheck_1_low()[6]
        l_l = self.player.labels_1_low()[6]
        a_l = self.player.apply_labels_1_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_17_true", "timeSpent_Main_b1_107"]


class Main_b1_107_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[6]
        t = self.player.sourcetype_1()[6]
        s = self.player.statementtype_1()[6]
        f_h = self.player.factcheck_1_high()[6]
        l_h = self.player.labels_1_high()[6]
        a_h = self.player.apply_labels_1_high()[6]
        f_l = self.player.factcheck_1_low()[6]
        l_l = self.player.labels_1_low()[6]
        a_l = self.player.apply_labels_1_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_17_true", "timeSpent_Main_b1_107"]


class Main_b1_108_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[7]
        t = self.player.sourcetype_1()[7]
        s = self.player.statementtype_1()[7]
        f_h = self.player.factcheck_1_high()[7]
        l_h = self.player.labels_1_high()[7]
        a_h = self.player.apply_labels_1_high()[7]
        f_l = self.player.factcheck_1_low()[7]
        l_l = self.player.labels_1_low()[7]
        a_l = self.player.apply_labels_1_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_18_true", "timeSpent_Main_b1_108"]


class Main_b1_108_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[7]
        t = self.player.sourcetype_1()[7]
        s = self.player.statementtype_1()[7]
        f_h = self.player.factcheck_1_high()[7]
        l_h = self.player.labels_1_high()[7]
        a_h = self.player.apply_labels_1_high()[7]
        f_l = self.player.factcheck_1_low()[7]
        l_l = self.player.labels_1_low()[7]
        a_l = self.player.apply_labels_1_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_18_true", "timeSpent_Main_b1_108"]


class Main_b1_109_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[8]
        t = self.player.sourcetype_1()[8]
        s = self.player.statementtype_1()[8]
        f_h = self.player.factcheck_1_high()[8]
        l_h = self.player.labels_1_high()[8]
        a_h = self.player.apply_labels_1_high()[8]
        f_l = self.player.factcheck_1_low()[8]
        l_l = self.player.labels_1_low()[8]
        a_l = self.player.apply_labels_1_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_19_true", "timeSpent_Main_b1_109"]


class Main_b1_109_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[8]
        t = self.player.sourcetype_1()[8]
        s = self.player.statementtype_1()[8]
        f_h = self.player.factcheck_1_high()[8]
        l_h = self.player.labels_1_high()[8]
        a_h = self.player.apply_labels_1_high()[8]
        f_l = self.player.factcheck_1_low()[8]
        l_l = self.player.labels_1_low()[8]
        a_l = self.player.apply_labels_1_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_19_true", "timeSpent_Main_b1_109"]


class Main_b1_110_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9"

    def vars_for_template(self):
        source = self.player.sources()[9]
        t = self.player.sourcetype_1()[9]
        s = self.player.statementtype_1()[9]
        f_h = self.player.factcheck_1_high()[9]
        l_h = self.player.labels_1_high()[9]
        a_h = self.player.apply_labels_1_high()[9]
        f_l = self.player.factcheck_1_low()[9]
        l_l = self.player.labels_1_low()[9]
        a_l = self.player.apply_labels_1_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_110_true", "timeSpent_Main_b1_110"]


class Main_b1_110_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[9]
        t = self.player.sourcetype_1()[9]
        s = self.player.statementtype_1()[9]
        f_h = self.player.factcheck_1_high()[9]
        l_h = self.player.labels_1_high()[9]
        a_h = self.player.apply_labels_1_high()[9]
        f_l = self.player.factcheck_1_low()[9]
        l_l = self.player.labels_1_low()[9]
        a_l = self.player.apply_labels_1_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_110_true", "timeSpent_Main_b1_110"]


class Main_b1_901_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[10]
        t = self.player.sourcetype_91()[0]
        s = self.player.statementtype_91()[0]
        f_h = self.player.factcheck_91_high()[0]
        l_h = self.player.labels_91_high()[0]
        a_h = self.player.apply_labels_91_high()[0]
        f_l = self.player.factcheck_91_low()[0]
        l_l = self.player.labels_91_low()[0]
        a_l = self.player.apply_labels_91_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_911_true", "timeSpent_Main_b1_901"]


class Main_b1_901_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[10]
        t = self.player.sourcetype_91()[0]
        s = self.player.statementtype_91()[0]
        f_h = self.player.factcheck_91_high()[0]
        l_h = self.player.labels_91_high()[0]
        a_h = self.player.apply_labels_91_high()[0]
        f_l = self.player.factcheck_91_low()[0]
        l_l = self.player.labels_91_low()[0]
        a_l = self.player.apply_labels_91_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_911_true", "timeSpent_Main_b1_901"]


class Main_b1_902_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[11]
        t = self.player.sourcetype_91()[1]
        s = self.player.statementtype_91()[1]
        f_h = self.player.factcheck_91_high()[1]
        l_h = self.player.labels_91_high()[1]
        a_h = self.player.apply_labels_91_high()[1]
        f_l = self.player.factcheck_91_low()[1]
        l_l = self.player.labels_91_low()[1]
        a_l = self.player.apply_labels_91_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_912_true", "timeSpent_Main_b1_902"]


class Main_b1_902_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[11]
        t = self.player.sourcetype_91()[1]
        s = self.player.statementtype_91()[1]
        f_h = self.player.factcheck_91_high()[1]
        l_h = self.player.labels_91_high()[1]
        a_h = self.player.apply_labels_91_high()[1]
        f_l = self.player.factcheck_91_low()[1]
        l_l = self.player.labels_91_low()[1]
        a_l = self.player.apply_labels_91_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_912_true", "timeSpent_Main_b1_902"]


class Main_b1_903_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[12]
        t = self.player.sourcetype_91()[2]
        s = self.player.statementtype_91()[2]
        f_h = self.player.factcheck_91_high()[2]
        l_h = self.player.labels_91_high()[2]
        a_h = self.player.apply_labels_91_high()[2]
        f_l = self.player.factcheck_91_low()[2]
        l_l = self.player.labels_91_low()[2]
        a_l = self.player.apply_labels_91_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_913_true",  "timeSpent_Main_b1_903"]


class Main_b1_903_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[12]
        t = self.player.sourcetype_91()[2]
        s = self.player.statementtype_91()[2]
        f_h = self.player.factcheck_91_high()[2]
        l_h = self.player.labels_91_high()[2]
        a_h = self.player.apply_labels_91_high()[2]
        f_l = self.player.factcheck_91_low()[2]
        l_l = self.player.labels_91_low()[2]
        a_l = self.player.apply_labels_91_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_913_true",  "timeSpent_Main_b1_903"]


class Main_b1_904_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[13]
        t = self.player.sourcetype_91()[3]
        s = self.player.statementtype_91()[3]
        f_h = self.player.factcheck_91_high()[3]
        l_h = self.player.labels_91_high()[3]
        a_h = self.player.apply_labels_91_high()[3]
        f_l = self.player.factcheck_91_low()[3]
        l_l = self.player.labels_91_low()[3]
        a_l = self.player.apply_labels_91_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_914_true", "timeSpent_Main_b1_904"]


class Main_b1_904_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[13]
        t = self.player.sourcetype_91()[3]
        s = self.player.statementtype_91()[3]
        f_h = self.player.factcheck_91_high()[3]
        l_h = self.player.labels_91_high()[3]
        a_h = self.player.apply_labels_91_high()[3]
        f_l = self.player.factcheck_91_low()[3]
        l_l = self.player.labels_91_low()[3]
        a_l = self.player.apply_labels_91_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_914_true", "timeSpent_Main_b1_904"]


class Main_b1_905_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[14]
        t = self.player.sourcetype_91()[4]
        s = self.player.statementtype_91()[4]
        f_h = self.player.factcheck_91_high()[4]
        l_h = self.player.labels_91_high()[4]
        a_h = self.player.apply_labels_91_high()[4]
        f_l = self.player.factcheck_91_low()[4]
        l_l = self.player.labels_91_low()[4]
        a_l = self.player.apply_labels_91_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_915_true",  "timeSpent_Main_b1_905"]


class Main_b1_905_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[14]
        t = self.player.sourcetype_91()[4]
        s = self.player.statementtype_91()[4]
        f_h = self.player.factcheck_91_high()[4]
        l_h = self.player.labels_91_high()[4]
        a_h = self.player.apply_labels_91_high()[4]
        f_l = self.player.factcheck_91_low()[4]
        l_l = self.player.labels_91_low()[4]
        a_l = self.player.apply_labels_91_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_915_true",  "timeSpent_Main_b1_905"]


class Main_b1_906_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[15]
        t = self.player.sourcetype_91()[5]
        s = self.player.statementtype_91()[5]
        f_h = self.player.factcheck_91_high()[5]
        l_h = self.player.labels_91_high()[5]
        a_h = self.player.apply_labels_91_high()[5]
        f_l = self.player.factcheck_91_low()[5]
        l_l = self.player.labels_91_low()[5]
        a_l = self.player.apply_labels_91_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_916_true",  "timeSpent_Main_b1_906"]


class Main_b1_906_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[15]
        t = self.player.sourcetype_91()[5]
        s = self.player.statementtype_91()[5]
        f_h = self.player.factcheck_91_high()[5]
        l_h = self.player.labels_91_high()[5]
        a_h = self.player.apply_labels_91_high()[5]
        f_l = self.player.factcheck_91_low()[5]
        l_l = self.player.labels_91_low()[5]
        a_l = self.player.apply_labels_91_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_916_true",  "timeSpent_Main_b1_906"]


class Main_b1_907_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[16]
        t = self.player.sourcetype_91()[6]
        s = self.player.statementtype_91()[6]
        f_h = self.player.factcheck_91_high()[6]
        l_h = self.player.labels_91_high()[6]
        a_h = self.player.apply_labels_91_high()[6]
        f_l = self.player.factcheck_91_low()[6]
        l_l = self.player.labels_91_low()[6]
        a_l = self.player.apply_labels_91_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_917_true", "timeSpent_Main_b1_907"]


class Main_b1_907_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[16]
        t = self.player.sourcetype_91()[6]
        s = self.player.statementtype_91()[6]
        f_h = self.player.factcheck_91_high()[6]
        l_h = self.player.labels_91_high()[6]
        a_h = self.player.apply_labels_91_high()[6]
        f_l = self.player.factcheck_91_low()[6]
        l_l = self.player.labels_91_low()[6]
        a_l = self.player.apply_labels_91_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_917_true", "timeSpent_Main_b1_907"]


class Main_b1_908_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[17]
        t = self.player.sourcetype_91()[7]
        s = self.player.statementtype_91()[7]
        f_h = self.player.factcheck_91_high()[7]
        l_h = self.player.labels_91_high()[7]
        a_h = self.player.apply_labels_91_high()[7]
        f_l = self.player.factcheck_91_low()[7]
        l_l = self.player.labels_91_low()[7]
        a_l = self.player.apply_labels_91_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_918_true", "timeSpent_Main_b1_908"]


class Main_b1_908_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[17]
        t = self.player.sourcetype_91()[7]
        s = self.player.statementtype_91()[7]
        f_h = self.player.factcheck_91_high()[7]
        l_h = self.player.labels_91_high()[7]
        a_h = self.player.apply_labels_91_high()[7]
        f_l = self.player.factcheck_91_low()[7]
        l_l = self.player.labels_91_low()[7]
        a_l = self.player.apply_labels_91_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_918_true", "timeSpent_Main_b1_908"]


class Main_b1_909_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[18]
        t = self.player.sourcetype_91()[8]
        s = self.player.statementtype_91()[8]
        f_h = self.player.factcheck_91_high()[8]
        l_h = self.player.labels_91_high()[8]
        a_h = self.player.apply_labels_91_high()[8]
        f_l = self.player.factcheck_91_low()[8]
        l_l = self.player.labels_91_low()[8]
        a_l = self.player.apply_labels_91_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_919_true", "timeSpent_Main_b1_909"]


class Main_b1_909_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[18]
        t = self.player.sourcetype_91()[8]
        s = self.player.statementtype_91()[8]
        f_h = self.player.factcheck_91_high()[8]
        l_h = self.player.labels_91_high()[8]
        a_h = self.player.apply_labels_91_high()[8]
        f_l = self.player.factcheck_91_low()[8]
        l_l = self.player.labels_91_low()[8]
        a_l = self.player.apply_labels_91_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_919_true", "timeSpent_Main_b1_909"]


class Main_b1_910_r2a(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[19]
        t = self.player.sourcetype_91()[9]
        s = self.player.statementtype_91()[9]
        f_h = self.player.factcheck_91_high()[9]
        l_h = self.player.labels_91_high()[9]
        a_h = self.player.apply_labels_91_high()[9]
        f_l = self.player.factcheck_91_low()[9]
        l_l = self.player.labels_91_low()[9]
        a_l = self.player.apply_labels_91_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_9110_true", "timeSpent_Main_b1_910"]


class Main_b1_910_r2b(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10"

    def vars_for_template(self):
        source = self.player.sources()[19]
        t = self.player.sourcetype_91()[9]
        s = self.player.statementtype_91()[9]
        f_h = self.player.factcheck_91_high()[9]
        l_h = self.player.labels_91_high()[9]
        a_h = self.player.apply_labels_91_high()[9]
        f_l = self.player.factcheck_91_low()[9]
        l_l = self.player.labels_91_low()[9]
        a_l = self.player.apply_labels_91_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_9110_true", "timeSpent_Main_b1_910"]


class Main_b1_1001_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[20]
        t = self.player.sourcetype_10()[0]
        s = self.player.statementtype_10()[0]
        f_h = self.player.factcheck_10_high()[0]
        l_h = self.player.labels_10_high()[0]
        a_h = self.player.apply_labels_10_high()[0]
        f_l = self.player.factcheck_10_low()[0]
        l_l = self.player.labels_10_low()[0]
        a_l = self.player.apply_labels_10_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_101_true",
                   "timeSpent_Main_b1_1001"]


class Main_b1_1002_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[21]
        t = self.player.sourcetype_10()[1]
        s = self.player.statementtype_10()[1]
        f_h = self.player.factcheck_10_high()[1]
        l_h = self.player.labels_10_high()[1]
        a_h = self.player.apply_labels_10_high()[1]
        f_l = self.player.factcheck_10_low()[1]
        l_l = self.player.labels_10_low()[1]
        a_l = self.player.apply_labels_10_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_102_true",
                   "timeSpent_Main_b1_1002"]


class Main_b1_1003_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[22]
        t = self.player.sourcetype_10()[2]
        s = self.player.statementtype_10()[2]
        f_h = self.player.factcheck_10_high()[2]
        l_h = self.player.labels_10_high()[2]
        a_h = self.player.apply_labels_10_high()[2]
        f_l = self.player.factcheck_10_low()[2]
        l_l = self.player.labels_10_low()[2]
        a_l = self.player.apply_labels_10_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_103_true",
                   "timeSpent_Main_b1_1003"]


class Main_b1_1004_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[23]
        t = self.player.sourcetype_10()[3]
        s = self.player.statementtype_10()[3]
        f_h = self.player.factcheck_10_high()[3]
        l_h = self.player.labels_10_high()[3]
        a_h = self.player.apply_labels_10_high()[3]
        f_l = self.player.factcheck_10_low()[3]
        l_l = self.player.labels_10_low()[3]
        a_l = self.player.apply_labels_10_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_104_true",
                   "timeSpent_Main_b1_1004"]


class Main_b1_1005_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[24]
        t = self.player.sourcetype_10()[4]
        s = self.player.statementtype_10()[4]
        f_h = self.player.factcheck_10_high()[4]
        l_h = self.player.labels_10_high()[4]
        a_h = self.player.apply_labels_10_high()[4]
        f_l = self.player.factcheck_10_low()[4]
        l_l = self.player.labels_10_low()[4]
        a_l = self.player.apply_labels_10_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_105_true",
                   "timeSpent_Main_b1_1005"]


class Main_b1_1006_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[25]
        t = self.player.sourcetype_10()[5]
        s = self.player.statementtype_10()[5]
        f_h = self.player.factcheck_10_high()[5]
        l_h = self.player.labels_10_high()[5]
        a_h = self.player.apply_labels_10_high()[5]
        f_l = self.player.factcheck_10_low()[5]
        l_l = self.player.labels_10_low()[5]
        a_l = self.player.apply_labels_10_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_106_true",
                   "timeSpent_Main_b1_1006"]


class Main_b1_1007_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[26]
        t = self.player.sourcetype_10()[6]
        s = self.player.statementtype_10()[6]
        f_h = self.player.factcheck_10_high()[6]
        l_h = self.player.labels_10_high()[6]
        a_h = self.player.apply_labels_10_high()[6]
        f_l = self.player.factcheck_10_low()[6]
        l_l = self.player.labels_10_low()[6]
        a_l = self.player.apply_labels_10_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_107_true",
                   "timeSpent_Main_b1_1007"]


class Main_b1_1008_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[27]
        t = self.player.sourcetype_10()[7]
        s = self.player.statementtype_10()[7]
        f_h = self.player.factcheck_10_high()[7]
        l_h = self.player.labels_10_high()[7]
        a_h = self.player.apply_labels_10_high()[7]
        f_l = self.player.factcheck_10_low()[7]
        l_l = self.player.labels_10_low()[7]
        a_l = self.player.apply_labels_10_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_108_true",
                   "timeSpent_Main_b1_1008"]


class Main_b1_1009_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[28]
        t = self.player.sourcetype_10()[8]
        s = self.player.statementtype_10()[8]
        f_h = self.player.factcheck_10_high()[8]
        l_h = self.player.labels_10_high()[8]
        a_h = self.player.apply_labels_10_high()[8]
        f_l = self.player.factcheck_10_low()[8]
        l_l = self.player.labels_10_low()[8]
        a_l = self.player.apply_labels_10_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_109_true",
                   "timeSpent_Main_b1_1009"]


class Main_b1_1010_r2(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_10_9" or o == "9_10_1"

    def vars_for_template(self):
        source = self.player.sources()[29]
        t = self.player.sourcetype_10()[9]
        s = self.player.statementtype_10()[9]
        f_h = self.player.factcheck_10_high()[9]
        l_h = self.player.labels_10_high()[9]
        a_h = self.player.apply_labels_10_high()[9]
        f_l = self.player.factcheck_10_low()[9]
        l_l = self.player.labels_10_low()[9]
        a_l = self.player.apply_labels_10_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1010_true",
                   "timeSpent_Main_b1_1010"]


class Main_b1_101_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[0]
        t = self.player.sourcetype_1()[0]
        s = self.player.statementtype_1()[0]
        f_h = self.player.factcheck_1_high()[0]
        l_h = self.player.labels_1_high()[0]
        a_h = self.player.apply_labels_1_high()[0]
        f_l = self.player.factcheck_1_low()[0]
        l_l = self.player.labels_1_low()[0]
        a_l = self.player.apply_labels_1_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_11_true", "timeSpent_Main_b1_101"]


class Main_b1_102_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[1]
        t = self.player.sourcetype_1()[1]
        s = self.player.statementtype_1()[1]
        f_h = self.player.factcheck_1_high()[1]
        l_h = self.player.labels_1_high()[1]
        a_h = self.player.apply_labels_1_high()[1]
        f_l = self.player.factcheck_1_low()[1]
        l_l = self.player.labels_1_low()[1]
        a_l = self.player.apply_labels_1_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_12_true", "timeSpent_Main_b1_102"]


class Main_b1_103_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[2]
        t = self.player.sourcetype_1()[2]
        s = self.player.statementtype_1()[2]
        f_h = self.player.factcheck_1_high()[2]
        l_h = self.player.labels_1_high()[2]
        a_h = self.player.apply_labels_1_high()[2]
        f_l = self.player.factcheck_1_low()[2]
        l_l = self.player.labels_1_low()[2]
        a_l = self.player.apply_labels_1_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_13_true", "timeSpent_Main_b1_103"]


class Main_b1_104_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[3]
        t = self.player.sourcetype_1()[3]
        s = self.player.statementtype_1()[3]
        f_h = self.player.factcheck_1_high()[3]
        l_h = self.player.labels_1_high()[3]
        a_h = self.player.apply_labels_1_high()[3]
        f_l = self.player.factcheck_1_low()[3]
        l_l = self.player.labels_1_low()[3]
        a_l = self.player.apply_labels_1_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_14_true", "timeSpent_Main_b1_104"]


class Main_b1_105_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[4]
        t = self.player.sourcetype_1()[4]
        s = self.player.statementtype_1()[4]
        f_h = self.player.factcheck_1_high()[4]
        l_h = self.player.labels_1_high()[4]
        a_h = self.player.apply_labels_1_high()[4]
        f_l = self.player.factcheck_1_low()[4]
        l_l = self.player.labels_1_low()[4]
        a_l = self.player.apply_labels_1_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_15_true", "timeSpent_Main_b1_105"]


class Main_b1_106_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[5]
        t = self.player.sourcetype_1()[5]
        s = self.player.statementtype_1()[5]
        f_h = self.player.factcheck_1_high()[5]
        l_h = self.player.labels_1_high()[5]
        a_h = self.player.apply_labels_1_high()[5]
        f_l = self.player.factcheck_1_low()[5]
        l_l = self.player.labels_1_low()[5]
        a_l = self.player.apply_labels_1_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_16_true", "timeSpent_Main_b1_106"]


class Main_b1_107_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[6]
        t = self.player.sourcetype_1()[6]
        s = self.player.statementtype_1()[6]
        f_h = self.player.factcheck_1_high()[6]
        l_h = self.player.labels_1_high()[6]
        a_h = self.player.apply_labels_1_high()[6]
        f_l = self.player.factcheck_1_low()[6]
        l_l = self.player.labels_1_low()[6]
        a_l = self.player.apply_labels_1_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_17_true", "timeSpent_Main_b1_107"]


class Main_b1_108_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[7]
        t = self.player.sourcetype_1()[7]
        s = self.player.statementtype_1()[7]
        f_h = self.player.factcheck_1_high()[7]
        l_h = self.player.labels_1_high()[7]
        a_h = self.player.apply_labels_1_high()[7]
        f_l = self.player.factcheck_1_low()[7]
        l_l = self.player.labels_1_low()[7]
        a_l = self.player.apply_labels_1_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_18_true", "timeSpent_Main_b1_108"]


class Main_b1_109_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[8]
        t = self.player.sourcetype_1()[8]
        s = self.player.statementtype_1()[8]
        f_h = self.player.factcheck_1_high()[8]
        l_h = self.player.labels_1_high()[8]
        a_h = self.player.apply_labels_1_high()[8]
        f_l = self.player.factcheck_1_low()[8]
        l_l = self.player.labels_1_low()[8]
        a_l = self.player.apply_labels_1_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_19_true", "timeSpent_Main_b1_109"]


class Main_b1_110_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "9_10_1" or o == "10_9_1"

    def vars_for_template(self):
        source = self.player.sources()[9]
        t = self.player.sourcetype_1()[9]
        s = self.player.statementtype_1()[9]
        f_h = self.player.factcheck_1_high()[9]
        l_h = self.player.labels_1_high()[9]
        a_h = self.player.apply_labels_1_high()[9]
        f_l = self.player.factcheck_1_low()[9]
        l_l = self.player.labels_1_low()[9]
        a_l = self.player.apply_labels_1_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_110_true", "timeSpent_Main_b1_110"]


class Main_b1_901_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[10]
        t = self.player.sourcetype_91()[0]
        s = self.player.statementtype_91()[0]
        f_h = self.player.factcheck_91_high()[0]
        l_h = self.player.labels_91_high()[0]
        a_h = self.player.apply_labels_91_high()[0]
        f_l = self.player.factcheck_91_low()[0]
        l_l = self.player.labels_91_low()[0]
        a_l = self.player.apply_labels_91_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_911_true", "timeSpent_Main_b1_901"]


class Main_b1_902_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[11]
        t = self.player.sourcetype_91()[1]
        s = self.player.statementtype_91()[1]
        f_h = self.player.factcheck_91_high()[1]
        l_h = self.player.labels_91_high()[1]
        a_h = self.player.apply_labels_91_high()[1]
        f_l = self.player.factcheck_91_low()[1]
        l_l = self.player.labels_91_low()[1]
        a_l = self.player.apply_labels_91_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_912_true", "timeSpent_Main_b1_902"]


class Main_b1_903_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[12]
        t = self.player.sourcetype_91()[2]
        s = self.player.statementtype_91()[2]
        f_h = self.player.factcheck_91_high()[2]
        l_h = self.player.labels_91_high()[2]
        a_h = self.player.apply_labels_91_high()[2]
        f_l = self.player.factcheck_91_low()[2]
        l_l = self.player.labels_91_low()[2]
        a_l = self.player.apply_labels_91_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_913_true", "timeSpent_Main_b1_903"]


class Main_b1_904_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[13]
        t = self.player.sourcetype_91()[3]
        s = self.player.statementtype_91()[3]
        f_h = self.player.factcheck_91_high()[3]
        l_h = self.player.labels_91_high()[3]
        a_h = self.player.apply_labels_91_high()[3]
        f_l = self.player.factcheck_91_low()[3]
        l_l = self.player.labels_91_low()[3]
        a_l = self.player.apply_labels_91_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_914_true",  "timeSpent_Main_b1_904"]


class Main_b1_905_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[14]
        t = self.player.sourcetype_91()[4]
        s = self.player.statementtype_91()[4]
        f_h = self.player.factcheck_91_high()[4]
        l_h = self.player.labels_91_high()[4]
        a_h = self.player.apply_labels_91_high()[4]
        f_l = self.player.factcheck_91_low()[4]
        l_l = self.player.labels_91_low()[4]
        a_l = self.player.apply_labels_91_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_915_true",  "timeSpent_Main_b1_905"]


class Main_b1_906_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[15]
        t = self.player.sourcetype_91()[5]
        s = self.player.statementtype_91()[5]
        f_h = self.player.factcheck_91_high()[5]
        l_h = self.player.labels_91_high()[5]
        a_h = self.player.apply_labels_91_high()[5]
        f_l = self.player.factcheck_91_low()[5]
        l_l = self.player.labels_91_low()[5]
        a_l = self.player.apply_labels_91_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_916_true",   "timeSpent_Main_b1_906"]


class Main_b1_907_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[16]
        t = self.player.sourcetype_91()[6]
        s = self.player.statementtype_91()[6]
        f_h = self.player.factcheck_91_high()[6]
        l_h = self.player.labels_91_high()[6]
        a_h = self.player.apply_labels_91_high()[6]
        f_l = self.player.factcheck_91_low()[6]
        l_l = self.player.labels_91_low()[6]
        a_l = self.player.apply_labels_91_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_917_true", "timeSpent_Main_b1_907"]


class Main_b1_908_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[17]
        t = self.player.sourcetype_91()[7]
        s = self.player.statementtype_91()[7]
        f_h = self.player.factcheck_91_high()[7]
        l_h = self.player.labels_91_high()[7]
        a_h = self.player.apply_labels_91_high()[7]
        f_l = self.player.factcheck_91_low()[7]
        l_l = self.player.labels_91_low()[7]
        a_l = self.player.apply_labels_91_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_918_true", "timeSpent_Main_b1_908"]


class Main_b1_909_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[18]
        t = self.player.sourcetype_91()[8]
        s = self.player.statementtype_91()[8]
        f_h = self.player.factcheck_91_high()[8]
        l_h = self.player.labels_91_high()[8]
        a_h = self.player.apply_labels_91_high()[8]
        f_l = self.player.factcheck_91_low()[8]
        l_l = self.player.labels_91_low()[8]
        a_l = self.player.apply_labels_91_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_919_true",   "timeSpent_Main_b1_909"]


class Main_b1_910_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "10_1_9" or o == "1_10_9"

    def vars_for_template(self):
        source = self.player.sources()[19]
        t = self.player.sourcetype_91()[9]
        s = self.player.statementtype_91()[9]
        f_h = self.player.factcheck_91_high()[9]
        l_h = self.player.labels_91_high()[9]
        a_h = self.player.apply_labels_91_high()[9]
        f_l = self.player.factcheck_91_low()[9]
        l_l = self.player.labels_91_low()[9]
        a_l = self.player.apply_labels_91_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_9110_true",  "timeSpent_Main_b1_910"]


class Main_b1_1001_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[20]
        t = self.player.sourcetype_10()[0]
        s = self.player.statementtype_10()[0]
        f_h = self.player.factcheck_10_high()[0]
        l_h = self.player.labels_10_high()[0]
        a_h = self.player.apply_labels_10_high()[0]
        f_l = self.player.factcheck_10_low()[0]
        l_l = self.player.labels_10_low()[0]
        a_l = self.player.apply_labels_10_low()[0]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_101_true", "timeSpent_Main_b1_1001"]


class Main_b1_1002_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[21]
        t = self.player.sourcetype_10()[1]
        s = self.player.statementtype_10()[1]
        f_h = self.player.factcheck_10_high()[1]
        l_h = self.player.labels_10_high()[1]
        a_h = self.player.apply_labels_10_high()[1]
        f_l = self.player.factcheck_10_low()[1]
        l_l = self.player.labels_10_low()[1]
        a_l = self.player.apply_labels_10_low()[1]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_102_true",
                   "timeSpent_Main_b1_1002"]


class Main_b1_1003_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[22]
        t = self.player.sourcetype_10()[2]
        s = self.player.statementtype_10()[2]
        f_h = self.player.factcheck_10_high()[2]
        l_h = self.player.labels_10_high()[2]
        a_h = self.player.apply_labels_10_high()[2]
        f_l = self.player.factcheck_10_low()[2]
        l_l = self.player.labels_10_low()[2]
        a_l = self.player.apply_labels_10_low()[2]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_103_true",
                   "timeSpent_Main_b1_1003"]


class Main_b1_1004_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[23]
        t = self.player.sourcetype_10()[3]
        s = self.player.statementtype_10()[3]
        f_h = self.player.factcheck_10_high()[3]
        l_h = self.player.labels_10_high()[3]
        a_h = self.player.apply_labels_10_high()[3]
        f_l = self.player.factcheck_10_low()[3]
        l_l = self.player.labels_10_low()[3]
        a_l = self.player.apply_labels_10_low()[3]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_104_true",
                   "timeSpent_Main_b1_1004"]


class Main_b1_1005_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[24]
        t = self.player.sourcetype_10()[4]
        s = self.player.statementtype_10()[4]
        f_h = self.player.factcheck_10_high()[4]
        l_h = self.player.labels_10_high()[4]
        a_h = self.player.apply_labels_10_high()[4]
        f_l = self.player.factcheck_10_low()[4]
        l_l = self.player.labels_10_low()[4]
        a_l = self.player.apply_labels_10_low()[4]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_105_true",
                   "timeSpent_Main_b1_1005"]


class Main_b1_1006_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[25]
        t = self.player.sourcetype_10()[5]
        s = self.player.statementtype_10()[5]
        f_h = self.player.factcheck_10_high()[5]
        l_h = self.player.labels_10_high()[5]
        a_h = self.player.apply_labels_10_high()[5]
        f_l = self.player.factcheck_10_low()[5]
        l_l = self.player.labels_10_low()[5]
        a_l = self.player.apply_labels_10_low()[5]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_106_true",
                   "timeSpent_Main_b1_1006"]


class Main_b1_1007_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[26]
        t = self.player.sourcetype_10()[6]
        s = self.player.statementtype_10()[6]
        f_h = self.player.factcheck_10_high()[6]
        l_h = self.player.labels_10_high()[6]
        a_h = self.player.apply_labels_10_high()[6]
        f_l = self.player.factcheck_10_low()[6]
        l_l = self.player.labels_10_low()[6]
        a_l = self.player.apply_labels_10_low()[6]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_107_true",
                   "timeSpent_Main_b1_1007"]


class Main_b1_1008_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[27]
        t = self.player.sourcetype_10()[7]
        s = self.player.statementtype_10()[7]
        f_h = self.player.factcheck_10_high()[7]
        l_h = self.player.labels_10_high()[7]
        a_h = self.player.apply_labels_10_high()[7]
        f_l = self.player.factcheck_10_low()[7]
        l_l = self.player.labels_10_low()[7]
        a_l = self.player.apply_labels_10_low()[7]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_108_true",
                   "timeSpent_Main_b1_1008"]


class Main_b1_1009_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[28]
        t = self.player.sourcetype_10()[8]
        s = self.player.statementtype_10()[8]
        f_h = self.player.factcheck_10_high()[8]
        l_h = self.player.labels_10_high()[8]
        a_h = self.player.apply_labels_10_high()[8]
        f_l = self.player.factcheck_10_low()[8]
        l_l = self.player.labels_10_low()[8]
        a_l = self.player.apply_labels_10_low()[8]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_109_true",
                   "timeSpent_Main_b1_1009"]


class Main_b1_1010_r3(Page):
    def is_displayed(self):
        o = self.player.block_order()
        return o == "1_9_10" or o == "9_1_10"

    def vars_for_template(self):
        source = self.player.sources()[29]
        t = self.player.sourcetype_10()[9]
        s = self.player.statementtype_10()[9]
        f_h = self.player.factcheck_10_high()[9]
        l_h = self.player.labels_10_high()[9]
        a_h = self.player.apply_labels_10_high()[9]
        f_l = self.player.factcheck_10_low()[9]
        l_l = self.player.labels_10_low()[9]
        a_l = self.player.apply_labels_10_low()[9]
        return dict(
            image_path="AI_Fotos/{}.jpg".format(source),
            t=t,
            s=s,
            f_h=f_h,
            l_h=l_h,
            a_h=a_h,
            l1_h=a_h[0],
            l2_h=a_h[1],
            l3_h=a_h[2],
            l4_h=a_h[3],
            l5_h=a_h[4],
            l6_h=a_h[5],
            l7_h=a_h[6],
            l8_h=a_h[7],
            l9_h=a_h[8],
            l10_h=a_h[9],
            f_l=f_l,
            l_l=l_l,
            a_l=a_l,
            l1_l=a_l[0],
            l2_l=a_l[1],
            l3_l=a_l[2],
            l4_l=a_l[3],
            l5_l=a_l[4],
            l6_l=a_l[5],
            l7_l=a_l[6],
            l8_l=a_l[7],
            l9_l=a_l[8],
            l10_l=a_l[9],
            source=source,
        )
    form_model = "player"
    form_fields = ["prob_1010_true",
                   "timeSpent_Main_b1_1010"]



########################################################################################################################
########################################################################


page_sequence = [WelcomePage,
                 Instructions_BackAndForth,
                 Instructions_Control, Instructions_ControlOK, Instructions_ControlOK1,

                 Instructions_b1_1a_r1, Instructions_b1_10a_r1, Instructions_b1_91a_r1,
                 Instructions_Control_blur_r1, Instructions_Control_blurOK_r1,
                 Demo_b1_1a1_r1, Demo_b1_1b1_r1,
                 Demo_b1_91a1_r1, Demo_b1_91b1_r1,
                 Demo_b1_101a1_r1, Demo_b1_101b1_r1,
                 Instructions_b1_1b_r1, Instructions_b1_10b_r1, Instructions_b1_91b_r1,
                 Main_b1_101_r1, Main_b1_102_r1, Main_b1_103_r1, Main_b1_104_r1, Main_b1_105_r1, Main_b1_106_r1,
                 Main_b1_107_r1, Main_b1_108_r1, Main_b1_109_r1, Main_b1_110_r1,
                 Main_b1_1001_r1, Main_b1_1002_r1, Main_b1_1003_r1, Main_b1_1004_r1, Main_b1_1005_r1,
                 Main_b1_1006_r1, Main_b1_1007_r1, Main_b1_1008_r1, Main_b1_1009_r1, Main_b1_1010_r1,
                 Main_b1_1011_r1, Main_b1_1012_r1, Main_b1_1013_r1, Main_b1_1014_r1, Main_b1_1015_r1,
                 Main_b1_1016_r1, Main_b1_1017_r1, Main_b1_1018_r1, Main_b1_1019_r1, Main_b1_1020_r1,
                 Main_b1_901_r1, Main_b1_902_r1, Main_b1_903_r1, Main_b1_904_r1, Main_b1_905_r1,
                 Main_b1_906_r1, Main_b1_907_r1, Main_b1_908_r1, Main_b1_909_r1, Main_b1_910_r1,
                 Slider_b1_1_r1, Slider_b1_10_r1, Slider_b1_91_r1,

                 Instructions_b1_1a_r2, Instructions_b1_10a_r2, Instructions_b1_91a_r2,
                 Instructions_Control_blur_r2, Instructions_Control_blurOK_r2,
                 Demo_b1_1a1_r2, Demo_b1_1b1_r2,
                 Demo_b1_91a1_r2, Demo_b1_91b1_r2,
                 Demo_b1_101a1_r2, Demo_b1_101b1_r2,
                 Instructions_b1_1b_r2, Instructions_b1_10b_r2, Instructions_b1_91b_r2,
                 Main_b1_101_r2a, Main_b1_102_r2a, Main_b1_103_r2a, Main_b1_104_r2a, Main_b1_105_r2a,
                 Main_b1_106_r2a, Main_b1_107_r2a, Main_b1_108_r2a, Main_b1_109_r2a, Main_b1_110_r2a,
                 Main_b1_101_r2b, Main_b1_102_r2b, Main_b1_103_r2b, Main_b1_104_r2b, Main_b1_105_r2b,
                 Main_b1_106_r2b, Main_b1_107_r2b, Main_b1_108_r2b, Main_b1_109_r2b, Main_b1_110_r2b,
                 Main_b1_1001_r2, Main_b1_1002_r2, Main_b1_1003_r2, Main_b1_1004_r2, Main_b1_1005_r2,
                 Main_b1_1006_r2, Main_b1_1007_r2, Main_b1_1008_r2, Main_b1_1009_r2, Main_b1_1010_r2,
                 Main_b1_1011_r2, Main_b1_1012_r2, Main_b1_1013_r2, Main_b1_1014_r2, Main_b1_1015_r2,
                 Main_b1_1016_r2, Main_b1_1017_r2, Main_b1_1018_r2, Main_b1_1019_r2, Main_b1_1020_r2,
                 Main_b1_901_r2a, Main_b1_902_r2a, Main_b1_903_r2a, Main_b1_904_r2a, Main_b1_905_r2a,
                 Main_b1_906_r2a, Main_b1_907_r2a, Main_b1_908_r2a, Main_b1_909_r2a, Main_b1_910_r2a,
                 Main_b1_901_r2b, Main_b1_902_r2b, Main_b1_903_r2b, Main_b1_904_r2b, Main_b1_905_r2b,
                 Main_b1_906_r2b, Main_b1_907_r2b, Main_b1_908_r2b, Main_b1_909_r2b, Main_b1_910_r2b,
                 Slider_b1_1_r2, Slider_b1_10_r2, Slider_b1_91_r2,

                 Instructions_b1_1a_r3, Instructions_b1_10a_r3, Instructions_b1_91a_r3,
                 Instructions_Control_blur_r3, Instructions_Control_blurOK_r3,
                 Demo_b1_1a1_r3, Demo_b1_1b1_r3,
                 Demo_b1_91a1_r3, Demo_b1_91b1_r3,
                 Demo_b1_101a1_r3, Demo_b1_101b1_r3,
                 Instructions_b1_1b_r3, Instructions_b1_10b_r3, Instructions_b1_91b_r3,
                 Main_b1_101_r3, Main_b1_102_r3, Main_b1_103_r3, Main_b1_104_r3, Main_b1_105_r3, Main_b1_106_r3,
                 Main_b1_107_r3, Main_b1_108_r3, Main_b1_109_r3, Main_b1_110_r3,
                 Main_b1_1001_r3, Main_b1_1002_r3, Main_b1_1003_r3, Main_b1_1004_r3, Main_b1_1005_r3,
                 Main_b1_1006_r3, Main_b1_1007_r3, Main_b1_1008_r3, Main_b1_1009_r3, Main_b1_1010_r3,
                 Main_b1_1011_r3, Main_b1_1012_r3, Main_b1_1013_r3, Main_b1_1014_r3, Main_b1_1015_r3,
                 Main_b1_1016_r3, Main_b1_1017_r3, Main_b1_1018_r3, Main_b1_1019_r3, Main_b1_1020_r3,
                 Main_b1_901_r3, Main_b1_902_r3, Main_b1_903_r3, Main_b1_904_r3, Main_b1_905_r3,
                 Main_b1_906_r3, Main_b1_907_r3, Main_b1_908_r3, Main_b1_909_r3, Main_b1_910_r3,
                 Slider_b1_1_r3, Slider_b1_10_r3, Slider_b1_91_r3,

                 Instructions_b1_blurreda, Instructions_Control_blur_X, Instructions_Control_blurOK_X,
                 Demo_b1_blurreda, Demo_b1_blurredb, Instructions_b1_blurredb,
                 Main_b1_blurred, Slider_b1_blur,

                 Cognitive, Survey1, Survey2, Survey3, Payment,

                 RedirectProlific]



