from django.core.management.base import BaseCommand
from django.db import models, transaction
from typing import Any, Optional

from api.apps.users.models import User
from api.apps.users.factory import (AdminUser,
                                    AdminProfile,
                                    ActiveUser,
                                    ActiveProfile,
                                    InactiveProfile,
                                    InactiveUser,
                                    )
from api.apps.users.models import User

ACTIVE = 15
INACTIVE = 4


class Command(BaseCommand):
    help = "Generates test data for Users and related profiles"
    models = [
              AdminUser,
              AdminProfile,
              ActiveUser,
              ActiveProfile,
              InactiveUser,
              InactiveProfile,
              ]

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        if User.objects.count() > 1:
            self.stdout.write("Users seem to already exist")
            exit("exiting.")
        self.stdout.write("Creating test data.")

        self.stdout.write("Creating active users.")
        for _ in range(ACTIVE):
            active_user = ActiveUser()

        self.stdout.write("Creating inactive users.")
        for _ in range(INACTIVE):
            inactive_user = InactiveUser()
