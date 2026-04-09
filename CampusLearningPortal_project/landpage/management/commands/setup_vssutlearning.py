from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from landpage.models import LandpageTeamMember
from landpage.models import LandpagePartner

class Command(BaseCommand):
    """
        Run in your console:
        $ python manage.py setup_vssutlearning
    """
    help = 'Picks the top 9 courses with the highest student enrollment.'
    
    def handle(self, *args, **options):
        """
            Function will create the objects necessary for some of the UI
            elements in the landpage.
        """
        LandpageTeamMember.objects.all().delete()
        LandpageTeamMember.objects.create(
            id=1,
            full_name="D. Gouri Sankar Mohanty",
            role="Lead Designer",
            # twitter_url="https://twitter.com/BartlomiejMika",
            facebook_url="https://www.facebook.com/gourisankar.mohanty.148",
            image_filename="DSC_0019.jpg",
            linkedin_url="https://www.linkedin.com/in/d-gourisankar-mohanty-5239bb1a2/",
            email="dgourisankarmohanty@gmail.com",
        )
        # LandpageTeamMember.objects.create(
        #     id=2,
        #     full_name="Michael Murray",
        #     role="Lead Designer",
        #     twitter_url="https://twitter.com/iamnotchad",
        #     facebook_url="https://www.facebook.com/michael.murray.75033149",
        #     image_filename="d.chandrasekhar-rao_photo1606604783.jpg",
        #     github_url="https://github.com/Michael-Murray",
        #     email="m_poet5@hotmail.com",
        # )
        LandpageTeamMember.objects.create(
            id=2,
            full_name="Devi Prasana Mishra",
            role="Developer",
            twitter_url="https://twitter.com/Deviprasan25803",
            # google_url="https://plus.google.com/u/0/108001172254765225648/posts",
            image_filename="IMG-20220314-WA0004 8.jpg",
            linkedin_url="https://www.linkedin.com/in/devi-prasan-mishra-606064bb/",
            email="deviprasan25803@gmail.com",
        )

        # LandpagePartner.objects.all().delete()
        # LandpagePartner.objects.create(
        #     id=1,
        #     image_filename="duplexsoft.png",
        #     title="Duplexsoft",
        #     url="www.duplexsoft.com"
        # )
        # LandpagePartner.objects.create(
        #     id=2,
        #     image_filename="eurasiasoft.png",
        #     title="Eurasiasoft",
        #     url="www.eurasiasoft.com"
        # )
