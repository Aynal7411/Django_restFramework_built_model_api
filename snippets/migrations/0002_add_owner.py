from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="snippet",
            name="owner",
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="snippets",
                null=True,
            ),
        ),
    ]
