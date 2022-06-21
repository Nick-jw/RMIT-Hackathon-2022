from django import forms
from django.forms import widgets

CHOICES = [('one', 'One'), ('two', 'Two')]

# creating a form ""


class InputForm(forms.Form):

    company_name = forms.CharField(label="Select Company Name",
                                   widget=forms.Select(choices=[
                                       ('AGL', 'AGL Energy Ltd'),
                                       ('ALU', 'Altium'),
                                       ('CSL', 'CSL'),
                                       ('APT', "Afterpay")
                                   ]
                                   )
                                   )

    role = forms.CharField(label="Please select your job title",
                           widget=forms.Select(choices=[
                               ('software developer', 'Software Developer'),
                               ('lead engineer', 'Lead Engineer'),
                               ('junior engineer', 'Junior Engineer'),
                               ('qa tester', 'QA Tester')],
                           )
                           )
    gender = forms.CharField(label="Please select your Gender",
                             widget=forms.Select(choices=[
                                 ('male', 'Male'),
                                 ('female', 'Female'),
                                 ('non-binary', 'Non-Binary'),
                                 ('other', 'Other/Prefer not to say')]
                             )
                             )

    salary_band = forms.CharField(label="Please select your salary band",
                                  widget=forms.Select(choices=[
                                      ('60-79k', '60-79k'),
                                      ('80-99k', '80-99k'),
                                      ('100-109k', '100-109k'),
                                      ('110-119k', '110-119k'),
                                      ('120-129k', '120-129k'),
                                      ('130-139k', '130-139k'),
                                      ('140-149k', '140-149k'),
                                      ('150-159k', '150-159k'),
                                      ('160-169k', '160-169k'),
                                      ('170-179k', '170-179k'),
                                      ('180k+', '180k+'),
                                  ]
                                  )
                                  )

    question_1 = forms.ChoiceField(label="Q1: How often have you ever witnessed gender-based discrimination in the workplace?",
                                   choices=[
                                       (1, 'Never'),
                                       (2, 'Rarely'),
                                       (3, 'Sometimes'),
                                       (4, 'Frequently'),
                                       (5, 'Often'),
                                       (6, 'Daily')],
                                   widget=forms.RadioSelect
                                   )

    question_2 = forms.ChoiceField(label="Q2: How often do you or your coworkers feel unsafe at work?",
                                   choices=[
                                       (1, 'Never'),
                                       (2, 'Rarely'),
                                       (3, 'Sometimes'),
                                       (4, 'Frequently'),
                                       (5, 'Often'),
                                       (6, 'Daily')],
                                   widget=forms.RadioSelect
                                   )

    question_3 = forms.ChoiceField(label="Q3: Are promotions distributed on merit rather than gender?",
                                   choices=[
                                       (1, 'Not at all'),
                                       (2, 'Not Really'),
                                       (3, 'Somewhat'),
                                       (4, 'Relatively'),
                                       (5, 'Mostly'),
                                       (6, 'Yes')],
                                   widget=forms.RadioSelect
                                   )

    question_4 = forms.ChoiceField(label="Q4: Do you feel as if management is representative of the demographics within your company?",
                                   choices=[
                                       (1, 'Not at all'),
                                       (2, 'Not Really'),
                                       (3, 'Somewhat'),
                                       (4, 'Relatively'),
                                       (5, 'Mostly'),
                                       (6, 'Yes')],
                                   widget=forms.RadioSelect
                                   )

    question_5 = forms.ChoiceField(label="Q5:How often do you hear of or witness individuals being bullied at your company?",
                                   choices=[
                                       (1, 'Never'),
                                       (2, 'Rarely'),
                                       (3, 'Sometimes'),
                                       (4, 'Frequently'),
                                       (5, 'Often'),
                                       (6, 'Daily')],
                                   widget=forms.RadioSelect
                                   )

    question_6 = forms.ChoiceField(label="Q6: Are inappropriate jokes ever made within your company that might discriminate against someone based on their gender?",
                                   choices=[
                                       (1, 'Never'),
                                       (2, 'Rarely'),
                                       (3, 'Sometimes'),
                                       (4, 'Frequently'),
                                       (5, 'Often'),
                                       (6, 'Daily')],
                                   widget=forms.RadioSelect
                                   )

    question_7 = forms.ChoiceField(label="Q7: How would you rate the company culture?",
                                   choices=[
                                       (1, 'Very good'),
                                       (2, 'Pretty good'),
                                       (3, 'Not bad'),
                                       (4, 'Okay'),
                                       (5, 'Sub-par'),
                                       (6, 'Terrible')],
                                   widget=forms.RadioSelect
                                   )

    question_8 = forms.ChoiceField(label="Q8: How often do you experience or witness social exclusion based on gender?",
                                   choices=[

                                       (1, 'Never'),
                                       (2, 'Rarely'),
                                       (3, 'Sometimes'),
                                       (4, 'Frequently'),
                                       (5, 'Often'),
                                       (6, 'Daily')],
                                   widget=forms.RadioSelect
                                   )

    question_9 = forms.ChoiceField(label="Q9: Do you feel as if there is a gender pay gap at your workplace?",
                                   choices=[
                                       (1, 'Not at all'),
                                       (2, 'Not Really'),
                                       (3, 'Somewhat'),
                                       (4, 'Relatively'),
                                       (5, 'Mostly'),
                                       (6, 'Yes')],
                                   widget=forms.RadioSelect
                                   )

    question_10 = forms.CharField(
        label="Anything else you'd like to add?", max_length=200)
