from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.functional import cached_property


class IdentityModel(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, default=None, blank=True)
    address = models.TextField('Address', default=None, blank=True)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25, default=None, blank=True)
    web_site = models.URLField('Web site', blank=True)
    job_title = models.CharField(max_length=50)
    presentation = models.TextField('Presentation', default=None, blank=True)
    profile_picture = models.ImageField('Profile picture', blank=True)
    profile_background = models.ImageField('Profile background picture', blank=True)

    @cached_property
    def get_profile_background(self):
        try:
            return self.profile_background.url
        except:
            return static('img/default-profile-bg.png')

    @cached_property
    def get_profile_picture(self):
        try:
            return self.profile_picture.url
        except:
            return static('img/default-profile-img.png')

    @cached_property
    def has_studies(self):
        return self.studies.count() > 0

    @cached_property
    def has_skills(self):
        return self.skills.count() > 0

    def __str__(self):
        return """Name: %s
First name: %s
Adress: %s
Postal code: %s
City: %s
Email: %s
Phone number: %s
Web site: %s
Job tite: %s""" % (self.name, self.first_name, self.address, self.postal_code, self.city,
                   self.email, self.phone_number, self.web_site, self.job_title)


class StudiesModel(models.Model):
    # Todo : Add possibility to put only year and/or month
    person = models.ForeignKey(IdentityModel, related_name='studies')
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    title = models.CharField(max_length=50)
    study_year = models.CharField(max_length=50, blank=True)
    school_name = models.CharField(max_length=10, blank=True)
    school_long_name = models.CharField(max_length=255)
    comment = models.TextField('Comments', blank=True)

    def get_complete_study_title(self):
        if self.study_year:
            return "%s — %s" % (self.title, self.study_year)
        else:
            return self.title

    def get_period(self):
        return "%s — %s" % (self.start_date.year, self.end_date.year)

    def get_complete_school_name(self):
        if self.school_name:
            return "%s (%s)" % (self.school_name, self.school_long_name)
        else:
            return self.school_long_name

    def __str__(self):
        return """%s-%s:%s
Year: %s
School: %s
Comment: %s""" % (str(self.start_date), str(self.end_date), self.title, self.study_year, self.school_name, self.comment)


class WorkExperiencesModel(models.Model):
    person = models.ForeignKey(IdentityModel, related_name='work_experiences')
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    job_title = models.CharField('Job title', max_length=50)
    company = models.TextField('Company name', max_length=255)
    place = models.TextField('Place', blank=True)
    comment = models.TextField('Comments', blank=True)

    def __str__(self):
        return """%s-%s:%s
Company: %s
Place: %s
Comment: %s""" % (str(self.start_date), str(self.end_date), self.job_title, self.company, self.place, self.comment)


class SkillsModel(models.Model):
    person = models.ForeignKey(IdentityModel, related_name='skills')
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    level = models.IntegerField('Level from 1 to 5', validators=[MaxValueValidator, MinValueValidator])
    comment = models.TextField('Comments', blank=True)

    @staticmethod
    def get_categories(person):
        return person.skills.values_list('category', flat=True).distinct()

    def __str__(self):
        return """Categrory: %s
Title: %s
Level: %s
Comment: %s """ % (self.category, self.title, self.level, self.comment)


class HobbiesModel(models.Model):
    person = models.ForeignKey(IdentityModel, related_name='hobbies')
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    comment = models.TextField('Comments', blank=True)

    def __str__(self):
        return """Categrory: %s
Title: %s
Comment: %s """ % (self.category, self.title, self.comment)
