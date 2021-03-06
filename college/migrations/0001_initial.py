# Generated by Django 3.1.7 on 2021-04-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(default=None, max_length=20)),
                ('image', models.ImageField(default=None, upload_to='college/admission')),
                ('course_type', models.CharField(default=None, max_length=20)),
                ('year', models.CharField(default=None, max_length=20)),
                ('branch', models.CharField(default=None, max_length=20)),
                ('applicant_name', models.CharField(default=None, max_length=50)),
                ('date_of_birth', models.CharField(default=None, max_length=20)),
                ('age', models.IntegerField(default=None, null=True)),
                ('blood_group', models.CharField(default=None, max_length=3)),
                ('mother_tounge', models.CharField(default=None, max_length=15)),
                ('religion', models.CharField(default=None, max_length=20)),
                ('cast', models.CharField(default=None, max_length=50)),
                ('community', models.CharField(default=None, max_length=20)),
                ('reserved_category', models.CharField(default=None, max_length=20)),
                ('physically_handicapped', models.CharField(default=None, max_length=20)),
                ('father_name', models.CharField(default=None, max_length=30)),
                ('father_occupation', models.CharField(default=None, max_length=50)),
                ('father_income', models.CharField(default=None, max_length=20)),
                ('mother_name', models.CharField(default=None, max_length=30)),
                ('mother_occupation', models.CharField(default=None, max_length=50)),
                ('mother_income', models.CharField(default=None, max_length=20)),
                ('gaurdian_name', models.CharField(default=None, max_length=30)),
                ('gaurdian_occupation', models.CharField(default=None, max_length=50)),
                ('gaurdian_income', models.CharField(default=None, max_length=20)),
                ('nationality', models.CharField(default=None, max_length=20)),
                ('native_place', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('currrent_address_line1', models.CharField(default=None, max_length=20)),
                ('current_address_line2', models.CharField(default=None, max_length=20)),
                ('current_city', models.CharField(default=None, max_length=30)),
                ('current_pincode', models.CharField(default=None, max_length=15)),
                ('current_phone', models.CharField(default=None, max_length=20)),
                ('permanent_address_line1', models.CharField(default=None, max_length=20)),
                ('permanent_address_line2', models.CharField(default=None, max_length=20)),
                ('permanent_city', models.CharField(default=None, max_length=30)),
                ('permanent_pincode', models.CharField(default=None, max_length=15)),
                ('permanent_phone', models.CharField(default=None, max_length=20)),
                ('tc_no', models.CharField(default=None, max_length=20)),
                ('tc_date', models.CharField(default=None, max_length=20)),
                ('medium_of_instruction', models.CharField(default=None, max_length=20)),
                ('language', models.CharField(default=None, max_length=20)),
                ('english', models.CharField(default=None, max_length=20)),
                ('maths', models.CharField(default=None, max_length=20)),
                ('physics', models.CharField(default=None, max_length=20)),
                ('chemistry', models.CharField(default=None, max_length=20)),
                ('biology', models.CharField(default=None, max_length=20)),
                ('eligible_percentage', models.CharField(default=None, max_length=20)),
                ('reg_no', models.CharField(default=None, max_length=20)),
                ('month_and_year_of_passing', models.CharField(default=None, max_length=20)),
                ('percentage_of_marks', models.CharField(default=None, max_length=3)),
                ('board', models.CharField(default=None, max_length=10)),
                ('name_of_institution', models.CharField(default=None, max_length=100)),
                ('language1', models.CharField(default=None, max_length=20)),
                ('english1', models.CharField(default=None, max_length=20)),
                ('maths1', models.CharField(default=None, max_length=20)),
                ('physics1', models.CharField(default=None, max_length=20)),
                ('chemistry1', models.CharField(default=None, max_length=20)),
                ('biology1', models.CharField(default=None, max_length=20)),
                ('eligible_percentage1', models.CharField(default=None, max_length=20)),
                ('has_enquired', models.BooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.PositiveIntegerField(choices=[(1, 'Physiology'), (2, 'Anatomy'), (3, 'Community Medicine'), (4, 'Tb & Chest Diseases'), (5, 'Paediatrics'), (6, 'Orthopaedics'), (7, 'Opthalmology'), (8, 'Psychiatry'), (9, 'Obstetrics & Gynaecology'), (10, 'General Surgery'), (11, 'Forensic Medicine'), (12, 'ENT'), (13, 'Dermatology'), (14, 'Dentistry'), (15, 'Anaesthesiology'), (16, 'Pharmacology'), (17, 'Bio Chemistry'), (18, 'Pathology'), (19, 'Micro Biology'), (20, 'Radio Diagnosis'), (21, 'General Medicine')], default='1')),
                ('background_image', models.ImageField(default=None, upload_to='college/department')),
                ('vision', models.TextField(default=None)),
                ('mission', models.TextField(default=None)),
                ('program_type', models.PositiveIntegerField(choices=[(1, 'Under Graduate'), (2, 'Post Graduate')], default='1')),
                ('duration', models.IntegerField(default=None, help_text='No of years')),
                ('brochure', models.FileField(blank=True, default=None, upload_to='college/department/brochure')),
                ('department_description', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50)),
                ('description', models.TextField(default=None)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='college/events')),
                ('brochure', models.FileField(blank=True, default=None, null=True, upload_to='college/events/brochure')),
            ],
        ),
        migrations.CreateModel(
            name='Main_facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.PositiveIntegerField(choices=[(1, 'Central Laboratory'), (2, 'Library'), (3, 'Infrastructure'), (4, 'Internet Facility'), (5, 'Seminar Hall'), (6, 'Canteen'), (7, 'Hostel and Quarters'), (8, 'Transport'), (9, 'Anti-ragging & Gender harassment')], default='1')),
                ('image', models.ImageField(default=None, upload_to='college/facility')),
                ('overview', models.TextField()),
            ],
            options={
                'verbose_name': 'facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(default=None)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='college/news')),
                ('brochure', models.ImageField(blank=True, default=None, null=True, upload_to='college/news/brochure')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('Qualification_And_Specification', models.CharField(default=None, max_length=50)),
                ('AreaOfIntrest', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.IntegerField(default=None)),
                ('Phone', models.IntegerField()),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professors',
            },
        ),
        migrations.CreateModel(
            name='PaperPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=250)),
                ('author', models.CharField(default=None, max_length=150)),
                ('date', models.DateField()),
                ('pdf_file', models.FileField(upload_to='college/department/paper_publications')),
                ('department_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
        ),
        migrations.CreateModel(
            name='Hyperlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=250)),
                ('hyperlink', models.URLField(max_length=250)),
                ('facility_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='college.main_facility')),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('image', models.ImageField(default=None, upload_to='college/department/HOD')),
                ('Qualification_And_Specification', models.CharField(default=None, max_length=50)),
                ('AreaOfIntrest', models.CharField(default=None, max_length=50)),
                ('experience', models.IntegerField(default=None, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Head of the department',
                'verbose_name_plural': 'Head of the department',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='college/department/gallery')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('quantity', models.IntegerField(default=None)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='best_moments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_moment', models.ImageField(default=None, upload_to='college/department/best-moments')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Best Moment',
                'verbose_name_plural': 'Best Moments',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards', models.TextField(default=None, max_length=100)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.TextField(default=None, max_length=100)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
            ],
            options={
                'verbose_name': 'Achievement',
                'verbose_name_plural': 'Achievements',
            },
        ),
    ]
