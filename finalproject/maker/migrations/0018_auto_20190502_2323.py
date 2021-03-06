# Generated by Django 2.1.7 on 2019-05-02 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maker', '0017_gradedtestmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradedQuestionModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maker.QuestionModel')),
            ],
        ),
        migrations.AddField(
            model_name='gradedtestmodel',
            name='questions',
            field=models.ManyToManyField(to='maker.GradedQuestionModel'),
        ),
    ]
