from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


# for creating a relative unique id per
# user
# User = get_user_model()


# Create your models here.
class charSheet(models.Model):
    # character's name
    char_name = models.CharField(max_length=45)

    # player's name which is the key that will
    # group together different character sheets
    # together
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    # tbd referencing an incrementing value in
    # user model through AUTH_USER_MODEL in
    # settings.py and above in User
    # character_id = User

    character_class = models.CharField(max_length=45)

    level = models.IntegerField(default=1)

    # stats
    charStr = models.IntegerField(default=10)
    charDex = models.IntegerField(default=10)
    charCon = models.IntegerField(default=10)
    charInt = models.IntegerField(default=10)
    charWis = models.IntegerField(default=10)
    charCha = models.IntegerField(default=10)

    # storing items in a json for now with the
    # future intent of making items that give
    # features show up on character sheet
    items = models.JSONField(null=True, blank=True)

    # Hit Points
    max_hp = models.IntegerField(default=1)
    current_hp = models.IntegerField(default=8)

    # similar idea as items with a JSON version
    feats = models.JSONField(null=True, blank=True)

    initiative = models.IntegerField(default=0)

    # to make a drop down, we have a predefined
    # list of choices before creating the field
    alignment_choices = (
        ("NE", "Neutral Evil"),
        ("CE", "Chaotic Evil"),
        ("LE", "Lawful Evil"),
        ("NN", "True Neutral"),
        ("CN", "Chaotic Neutral"),
        ("LN", "Lawful Neutral"),
        ("NG", "Neutral Good"),
        ("CG", "Chaotic Good"),
        ("LG", "Lawful Good"),
    )

    alignment = models.CharField(max_length=16, choices=alignment_choices, default="NN")

    # instead of making this a json, making this
    # an editable field makes more sense as it
    # doesn't need to be itemized

    background = models.TextField(default="Orphan who grew up on a farm...", blank=True)

    race = models.CharField(max_length=40)

    exp = models.IntegerField(default=0)

    language_proficiency = models.TextField(blank=True)

    weapon_proficiency = models.JSONField(null=True, blank=True)

    armor_proficiency = models.JSONField(null=True, blank=True)

    # we'll allow the user to define their
    # attack options for now

    attack_options = models.JSONField(null=True, blank=True)

    misc_features = models.JSONField(null=True, blank=True)

    spells_known = models.JSONField(null=True, blank=True)

    # spell slots tbd
    # spellslots =

    def __str__(self):
        return self.char_name

    def get_absolute_url(self):
        return reverse("character_details", kwargs={"str": self.author, "pk": self.pk})
