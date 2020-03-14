from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)



class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE,blank=True, null=True)

    
    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline




class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # date_created = models.DateTimeField(auto_now_add=True)
    salary = models.FloatField(null=True)

    
    def __str__(self):
        return self.name




class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door')
    )

    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100,choices=CATEGORY,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    
    def __str__(self):
        return self.name


    

class Order(models.Model):
    STATUS = (
           ('pending','Pending'),
           ('out','Out for Delivery'),
           ('delivered','Delivered')
    )


    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,null=True,choices=STATUS)
