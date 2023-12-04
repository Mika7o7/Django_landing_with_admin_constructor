# Generated by Django 4.2.5 on 2023-12-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaruselSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Նկար')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Վերնագիր')),
                ('icon_1', models.ImageField(upload_to='images/icon/', verbose_name='Նկար')),
                ('href_1', models.CharField(max_length=100, verbose_name='հղում')),
                ('icon_2', models.ImageField(upload_to='images/icon/', verbose_name='Նկար')),
                ('href_2', models.CharField(max_length=100, verbose_name='հղում')),
                ('tel', models.CharField(max_length=40, verbose_name='հեր')),
                ('email', models.CharField(max_length=100, verbose_name='մեիլ')),
            ],
        ),
        migrations.CreateModel(
            name='CourseConducted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
            ],
        ),
        migrations.CreateModel(
            name='CourseProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
            ],
        ),
        migrations.CreateModel(
            name='EndOfCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
            ],
        ),
        migrations.CreateModel(
            name='InfoSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Վերնագիր')),
                ('sub_title', models.CharField(max_length=200, verbose_name='փոքր Վերնագիր')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Նկար')),
                ('bg_image', models.ImageField(upload_to='images/backgraund/', verbose_name='ֆոնի Նկար')),
            ],
        ),
        migrations.CreateModel(
            name='NavBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=50)),
                ('first_link', models.CharField(max_length=100)),
                ('first_qordinate', models.IntegerField()),
                ('second_link', models.CharField(max_length=100)),
                ('second_qordinate', models.IntegerField()),
                ('three_link', models.CharField(max_length=100)),
                ('three_qordinate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OfferSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
                ('sub_title', models.CharField(max_length=200, verbose_name='փոքր Վերնագիր')),
                ('description_1', models.TextField(verbose_name='նկարագրություն')),
                ('description_2', models.TextField(verbose_name='նկարագրություն')),
                ('description_3', models.TextField(verbose_name='նկարագրություն')),
                ('description_4', models.TextField(verbose_name='նկարագրություն')),
                ('button', models.CharField(max_length=40, verbose_name='կնոպկա')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MainStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='թվեր')),
                ('sub_title', models.CharField(max_length=200, verbose_name='փոքր Վերնագիր')),
                ('description', models.TextField(verbose_name='նկարագրություն')),
                ('courseconducted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='app.courseconducted')),
                ('courseprogram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='app.courseprogram')),
                ('endOfcourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='app.endofcourse')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='app.offersection')),
            ],
        ),
    ]