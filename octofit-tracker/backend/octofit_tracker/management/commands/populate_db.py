from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Collections should be dropped with mongosh before running this command.

        # Create teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create users (superheroes)
        ironman = User.objects.create(email='tony@stark.com', name='Iron Man', team=marvel)
        cap = User.objects.create(email='steve@rogers.com', name='Captain America', team=marvel)
        batman = User.objects.create(email='bruce@wayne.com', name='Batman', team=dc)
        superman = User.objects.create(email='clark@kent.com', name='Superman', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Flight', duration=60, date=timezone.now().date())
        Activity.objects.create(user=cap, type='Shield Training', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Detective Work', duration=90, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Flying', duration=120, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Agility Course', description='Agility and reflexes')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([marvel, dc])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=200)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
