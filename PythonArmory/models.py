from django.db import models

# Create your models here.

class armorySearch (models.Model):
    charName = models.TextField(max_length=30)
    region = models.TextField(max_length=20)
    armoryDate = models.DateTimeField()
    serverName = models.TextField(max_length=50)
    classType = models.TextField(max_length=20)
    raceType = models.TextField(max_length=15)
    levelNumber = models.IntegerField()
    avgItemLevel = models.IntegerField()
    headName = models.TextField(max_length=100)
    neckName = models.TextField(max_length=100)
    shouldersName = models.TextField(max_length=100)
    backName = models.TextField(max_length=100)
    chestName = models.TextField(max_length=100)
    shirtName = models.TextField(max_length=100)
    tabardName = models.TextField(max_length=100)
    wristsName = models.TextField(max_length=100)
    glovesName = models.TextField(max_length=100)
    beltName = models.TextField(max_length=100)
    legsName = models.TextField(max_length=100)
    feetName = models.TextField(max_length=100)
    ringOneName = models.TextField(max_length=100)
    ringTwoName = models.TextField(max_length=100)
    trinketOneName = models.TextField(max_length=100)
    trinketTwoName = models.TextField(max_length=100)
    mainHandName = models.TextField(max_length=100)
    offHandName = models.TextField(max_length=100)

    headSlotURL = models.URLField(max_length=2000)
    neckSlotURL = models.URLField(max_length=2000)
    shoulderSlotURL = models.URLField(max_length=2000)
    backSlotURL = models.URLField(max_length=2000)
    chestSlotURL = models.URLField(max_length=2000)
    shirtSlotURL = models.URLField(max_length=2000)
    tabardSlotURL = models.URLField(max_length=2000)
    wristsSlotURL = models.URLField(max_length=2000)
    glovesSlotURL = models.URLField(max_length=2000)
    beltSlotURL = models.URLField(max_length=2000)
    legsSlotURL = models.URLField(max_length=2000)
    feetSlotURL = models.URLField(max_length=2000)
    ringOneSlotURL = models.URLField(max_length=2000)
    ringTwoSlotURL = models.URLField(max_length=2000)
    trinketOneSlotURL = models.URLField(max_length=2000)
    trinketTwoSlotURL = models.URLField(max_length=2000)
    mainHandSlotURL = models.URLField(max_length=2000)
    offHandSlotURL = models.URLField(max_length=2000)

    professionOneName = models.TextField(max_length=50)
    professionTwoName = models.TextField(max_length=50)

    professionOneLevel = models.IntegerField()
    professionTwoLevel = models.IntegerField()
    cookingLevel = models.IntegerField()
    firstAidLevel = models.IntegerField()

    agilityStatAmount = models.IntegerField()
    strengthStatAmount = models.IntegerField()
    intellectStatAmount = models.IntegerField()
    staminaStatAmount = models.IntegerField()
    armourStatAmount = models.IntegerField()

    critStatAmount = models.IntegerField()
    masteryStatAmount = models.IntegerField()
    hasteStatAmount = models.IntegerField()
    versStatAmount = models.IntegerField()

    def __unicode__(self):
        return '/%s/' % self.id

    def get_absolute_url(self):
        return '/%s/' % self.id

