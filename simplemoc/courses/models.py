from django.db import models

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='imagem', null=True, blank=True
    )
    created_at = models.DateTimeField(
        'criado em', auto_now_add=True
    )
    updated_at =  models.DateTimeField(
        'Atualizado em', auto_now=True
    )
    objects = CourseManager()

    def __str__(self):
        return  self.name

    #o django sugere que vc crie o get_absoulute_url e retorna uma tupla
    #esta tupla é a URL no caso details(namespace:url), argumentos não nomeaveis entre parenteses (), argumentos noveaveis {}
    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']


