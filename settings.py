from os import environ


SESSION_CONFIGS = [
    dict(
        name='implied_reliability',
        display_name="Experiment",
        num_demo_participants=10,
        app_sequence=['implied_reliability'],
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name="implied_reliability",
        display_name="Experiment"
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = " "



SECRET_KEY = 'y5+d3x0wth28=%pufm)bzde8sv+@kc_i3*jo=*g5ba*2u9w_bz'

INSTALLED_APPS = ['otree']

