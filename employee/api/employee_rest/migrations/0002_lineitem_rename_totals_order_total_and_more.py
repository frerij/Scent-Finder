# Generated by Django 4.0.3 on 2022-06-23 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='totals',
            new_name='total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='productvo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productvo',
            name='limited_item',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserVO',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineItem', to='employee_rest.productvo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='employee_rest.lineitem'),
        ),
    ]
