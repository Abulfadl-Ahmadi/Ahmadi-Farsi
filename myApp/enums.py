from django.db import models


class Gender(models.TextChoices):
    male = 'M', 'Male'
    female = 'F', 'Female'
    
 

class Grade(models.TextChoices):
    Freshman = "Fr", "Freshman"
    Sophomore = "So", "Sophomore"
    Junior = "Ju", "Junior"
    Senior = "Se", "Senior"
    Bachelor = "Ba", "Bachelor"
    Master = "Ma", "Master"
    Doctor = "Do", "Doctor"


class Term(models.TextChoices):
    One = "1", "1"
    Two = "2", "2"
    Three = "3", "3"
    Four = "4", "4"
    Five = "5", "5"
    Six = "6", "6"
    Seven = "7", "7"
    Eight = "8", "8"
    Nine = "9", "9"
    Ten = "10", "10"


class TypeUniversity(models.TextChoices):
    State = "State", "State"
    Night = "Night", "Night"
    Azad = "Azad", "Azad"


class EmploymentStatus(models.TextChoices):
    Formal = "F", "Formal"
    Informal = "I", "Informal"
