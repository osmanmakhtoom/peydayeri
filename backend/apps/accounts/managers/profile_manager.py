from django.db.models.manager import Manager, QuerySet


class ProfileQuerySet(QuerySet):
    def get(self, user):
        return self.filter(user=user)


class ProfileManager(Manager):
    pass