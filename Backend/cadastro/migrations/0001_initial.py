# Generated by Django 3.2.5 on 2021-09-03 00:34

import django.contrib.auth.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id_identificador', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('catalogo', models.CharField(blank=True, max_length=20, null=True)),
                ('EntradaNoCatalogo', models.DateField(auto_now_add=True)),
                ('Lingua', models.CharField(blank=True, max_length=20, null=True)),
                ('Descrisao', models.CharField(blank=True, max_length=20, null=True)),
                ('palavrachave', models.CharField(blank=True, max_length=20, null=True)),
                ('Corbertura', models.CharField(blank=True, max_length=20, null=True)),
                ('Estrtura', models.CharField(blank=True, max_length=20, null=True)),
                ('NiveldeAgregacao', models.IntegerField(blank=True, default=0, null=True)),
                ('Versao', models.CharField(blank=True, max_length=20, null=True)),
                ('Status', models.CharField(blank=True, max_length=10, null=True)),
                ('ContribuinteFuncao', models.CharField(blank=True, max_length=20, null=True)),
                ('ContribuinteEntidadae', models.CharField(blank=True, max_length=20, null=True)),
                ('ContribuinteData', models.CharField(blank=True, max_length=20, null=True)),
                ('identificador', models.CharField(blank=True, max_length=20, null=True)),
                ('catalogoMeta', models.CharField(blank=True, max_length=20, null=True)),
                ('catalogoMetaEntrada', models.CharField(blank=True, max_length=20, null=True)),
                ('catalogoMetaData', models.CharField(blank=True, max_length=20, null=True)),
                ('EsquemaMeta', models.CharField(blank=True, max_length=20, null=True)),
                ('idiomameta', models.CharField(blank=True, max_length=20, null=True)),
                ('formato', models.CharField(blank=True, max_length=20, null=True)),
                ('tamanho', models.CharField(blank=True, max_length=20, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=20, null=True)),
                ('requisitoTipo', models.CharField(blank=True, max_length=20, null=True)),
                ('requisitoNome', models.CharField(blank=True, max_length=20, null=True)),
                ('Observacao', models.CharField(blank=True, max_length=20, null=True)),
                ('outrosRequitos', models.CharField(blank=True, max_length=20, null=True)),
                ('duracao', models.CharField(blank=True, max_length=20, null=True)),
                ('tipodeinteratividade', models.CharField(blank=True, max_length=20, null=True)),
                ('tipodeRecursodeAprendizagem', models.CharField(blank=True, max_length=20, null=True)),
                ('niveldeinteratividade', models.CharField(blank=True, max_length=20, null=True)),
                ('densidadesemantica', models.CharField(blank=True, max_length=20, null=True)),
                ('funcaodousuariofinalpretendido', models.CharField(blank=True, max_length=20, null=True)),
                ('contexto', models.CharField(blank=True, max_length=20, null=True)),
                ('faixaEtaria', models.CharField(blank=True, max_length=20, null=True)),
                ('dificuldade', models.CharField(blank=True, max_length=20, null=True)),
                ('TempodeAprendizagem', models.CharField(blank=True, max_length=20, null=True)),
                ('DescrisaoEducacional', models.CharField(blank=True, max_length=20, null=True)),
                ('idioma', models.CharField(blank=True, max_length=20, null=True)),
                ('custo', models.CharField(blank=True, max_length=20, null=True)),
                ('DireitosautoraisRestricoes', models.CharField(blank=True, max_length=20, null=True)),
                ('DescrisaoDireitos', models.CharField(blank=True, max_length=20, null=True)),
                ('tipoRelacao', models.CharField(blank=True, max_length=20, null=True)),
                ('recursoRelacao', models.CharField(blank=True, max_length=20, null=True)),
                ('pessoaAnotacao', models.CharField(blank=True, max_length=20, null=True)),
                ('dataanotacao', models.CharField(blank=True, max_length=20, null=True)),
                ('descrisaoanotacao', models.CharField(blank=True, max_length=20, null=True)),
                ('closificacaoObjetivo', models.CharField(blank=True, max_length=20, null=True)),
                ('taxon', models.CharField(blank=True, max_length=20, null=True)),
                ('taxonFonte', models.CharField(blank=True, max_length=20, null=True)),
                ('taxonId', models.CharField(blank=True, max_length=20, null=True)),
                ('taxonEntrada', models.CharField(blank=True, max_length=20, null=True)),
                ('classificacaoDescrisao', models.CharField(blank=True, max_length=20, null=True)),
                ('PalavraPasseClassificacao', models.CharField(blank=True, max_length=20, null=True)),
                ('autor', models.CharField(blank=True, max_length=20, null=True)),
                ('ano_pulicacao', models.IntegerField(default=2020)),
                ('estado', models.CharField(blank=True, max_length=20, null=True)),
                ('Npaginas', models.IntegerField(blank=True, default=0, null=True)),
                ('editora', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.CharField(db_index=True, max_length=255, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
