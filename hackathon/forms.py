from sre_constants import CH_LOCALE
from click import Choice
from django import forms


CHOICES = [('one', 'One'), ('two', 'Two')]

# creating a form ""


class InputForm(forms.Form):
    question_1 = forms.ChoiceField(label="Q1: How often have you ever witnessed gender-based discrimination in the workplace?",
                                   choices=[
                                       ('never', 'Never'),
                                       ('rarely', 'Rarely'),
                                       ('sometimes', 'Sometimes'),
                                       ('frequently', 'Frequently'),
                                       ('often', 'Often'),
                                       ('daily', 'Daily')],
                                   widget=forms.RadioSelect
                                   )
    question_2 = forms.ChoiceField(label="Q2: How often do you or your coworkers feel unsafe at work?",
                                   choices=[
                                       ('never', 'Never'),
                                       ('rarely', 'Rarely'),
                                       ('sometimes', 'Sometimes'),
                                       ('frequently', 'Frequently'),
                                       ('often', 'Often'),
                                       ('daily', 'Daily')],
                                   widget=forms.RadioSelect
                                   )
    question_3 = forms.ChoiceField(label="Q3: Are promotions distributed on merit rather than gender?",
                                   choices=[
                                       ('no', 'Not at all'),
                                       ('notreally', 'Not Really'),
                                       ('somewhat', 'Somewhat'),
                                       ('relatively', 'Relatively'),
                                       ('mostly', 'Mostly'),
                                       ('yes', 'Yes')],
                                   widget=forms.RadioSelect
                                   )
    question_4 = forms.ChoiceField(label="Q4: Do you feel as if management is representative of the demographics within your company?",
                                   choices=[
                                       ('no', 'Not at all'),
                                       ('notreally', 'Not Really'),
                                       ('somewhat', 'Somewhat'),
                                       ('relatively', 'Relatively'),
                                       ('mostly', 'Mostly'),
                                       ('yes', 'Yes')],
                                   widget=forms.RadioSelect
                                   )
    question_5 = forms.ChoiceField(label="Q5: Do you feel as if management is representative of the demographics within your company?",
                                   choices=[
                                       ('no', 'Not at all'),
                                       ('notreally', 'Not Really'),
                                       ('somewhat', 'Somewhat'),
                                       ('relatively', 'Relatively'),
                                       ('mostly', 'Mostly'),
                                       ('yes', 'Yes')],
                                   widget=forms.RadioSelect
                                   )
