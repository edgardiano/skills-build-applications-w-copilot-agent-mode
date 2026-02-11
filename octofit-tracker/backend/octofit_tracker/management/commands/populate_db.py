from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
            steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
            bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
            clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=tony, type='Running', duration=30, date='2026-02-10')
            Activity.objects.create(user=steve, type='Cycling', duration=45, date='2026-02-09')
            Activity.objects.create(user=bruce, type='Swimming', duration=60, date='2026-02-08')
            Activity.objects.create(user=clark, type='Yoga', duration=20, date='2026-02-07')

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            w1 = Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
            w2 = Workout.objects.create(name='Speed Training', description='Speed workout for heroes')
            w1.suggested_for.set([marvel, dc])
            w2.suggested_for.set([marvel])

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(team=marvel, points=200)
            Leaderboard.objects.create(team=dc, points=150)

            self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
