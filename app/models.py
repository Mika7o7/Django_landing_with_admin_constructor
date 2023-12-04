from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class NavBar(models.Model):
    logo = models.CharField(max_length=50)
    first_link = models.CharField(max_length=100)
    first_qordinate = models.IntegerField()
    second_link = models.CharField(max_length=100)
    second_qordinate = models.IntegerField()
    three_link = models.CharField(max_length=100)
    three_qordinate = models.IntegerField()

    def __str__(self):
        return f"{self.logo}"


class InfoSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Վերնագիր")
    sub_title = models.CharField(max_length=200, verbose_name="փոքր Վերնագիր")
    photo = models.ImageField("Նկար", upload_to="images/")
    bg_image = models.ImageField("ֆոնի Նկար", upload_to="images/backgraund/")


    def __str__(self):
        return f"{self.title}"



class CaruselSection(models.Model):
    photo = models.ImageField("Նկար", upload_to="images/")


class MainStyle(models.Model):
    __tablename__ = 'main'
    number = models.IntegerField("թվեր")
    sub_title = models.CharField(max_length=200, verbose_name="փոքր Վերնագիր")
    description = models.TextField("նկարագրություն")
    offer = models.ForeignKey("OfferSection", on_delete=models.CASCADE, related_name="main", null=True, blank=True)
    courseprogram = models.ForeignKey("CourseProgram", on_delete=models.CASCADE, related_name="main", null=True, blank=True)
    endOfcourse = models.ForeignKey("EndOfCourse", on_delete=models.CASCADE, related_name="main", null=True, blank=True)
    courseconducted = models.ForeignKey("CourseConducted", on_delete=models.CASCADE, related_name="main", null=True, blank=True)


class OfferSection(models.Model):
    __tablename__ = 'offer'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")



class CourseProgram(models.Model):
    __tablename__ = 'cours'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    



class EndOfCourse(models.Model):
    __tablename__ = 'endofcours'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    



class CourseConducted(models.Model):
    __tablename__ = 'conducted'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    
    


class SpecialOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    sub_title = models.CharField(max_length=200, verbose_name="փոքր Վերնագիր")
    description_1 = models.TextField("նկարագրություն")
    description_2 = models.TextField("նկարագրություն")
    description_3 = models.TextField("նկարագրություն")
    description_4 = models.TextField("նկարագրություն")
    button = models.CharField(max_length=40, verbose_name="կնոպկա")



class Contacts(models.Model):
    title = models.CharField(max_length=50, verbose_name="Վերնագիր")
    icon_1 = models.ImageField("Նկար", upload_to="images/icon/")
    href_1 = models.CharField(max_length=100, verbose_name="հղում")
    icon_2 = models.ImageField("Նկար", upload_to="images/icon/")
    href_2 = models.CharField(max_length=100, verbose_name="հղում")
    tel = models.CharField("հեր", max_length=40)
    email = models.CharField("մեիլ", max_length=100)