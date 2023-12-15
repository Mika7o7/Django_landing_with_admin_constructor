from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Անուն")
    last_name = models.CharField(max_length=50, verbose_name="Ազգանուն")
    phone = models.CharField(max_length=50, verbose_name="նկար")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    class Meta:
        verbose_name="Օկտատեր"
        verbose_name_plural="Օկտատեր"



class NavBar(models.Model):
    logo = models.CharField(max_length=50, verbose_name="լոգո")
    first_link = models.CharField(max_length=100, verbose_name="առաջին լինկի անուն")
    first_qordinate = models.IntegerField(verbose_name="կորդինատներ")
    second_link = models.CharField(max_length=100, verbose_name="եկրորդ լինկի անուն")
    second_qordinate = models.IntegerField(verbose_name="կորդինատներ")
    three_link = models.CharField(max_length=100, verbose_name="երորդ լինկի անուն")
    three_qordinate = models.IntegerField(verbose_name="կորդինատներ")

    def __str__(self):
        return f"{self.logo}"


    class Meta:
        verbose_name="Մենյու"
        verbose_name_plural="Մենյու"



class InfoSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Վերնագիր")
    sub_title = models.CharField(max_length=200, verbose_name="փոքր Վերնագիր")
    photo = models.ImageField("Նկար", upload_to="images/")
    bg_image = models.ImageField("ֆոնի Նկար", upload_to="images/backgraund/")


    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Ինֆո Սեկցիա"
        verbose_name_plural="Ինֆո Սեկցիա"


class CaruselSection(models.Model):
    photo = models.ImageField("Նկար", upload_to="images/")


    class Meta:
        verbose_name="Նկարների Սեկցիա"
        verbose_name_plural="Նկարների Սեկցիա"



class MainStyle(models.Model):
    __tablename__ = 'main'
    number = models.IntegerField("թվեր")
    sub_title = models.CharField(max_length=200, verbose_name="փոքր Վերնագիր")
    description = models.TextField("նկարագրություն")
    offer = models.ForeignKey("OfferSection", on_delete=models.CASCADE, related_name="main", null=True, blank=True, verbose_name="Առարջակի կապ")
    courseprogram = models.ForeignKey("CourseProgram", on_delete=models.CASCADE, related_name="main", null=True, blank=True, verbose_name="Դասընթացի ծրագրի կապ")
    endOfcourse = models.ForeignKey("EndOfCourse", on_delete=models.CASCADE, related_name="main", null=True, blank=True, verbose_name="Դասընթացի ավարտի կապ")
    courseconducted = models.ForeignKey("CourseConducted", on_delete=models.CASCADE, related_name="main", null=True, blank=True, verbose_name="Դասընթացը անցկացվել կապ")

    def __str__(self):
        return f"{self.sub_title}"


    class Meta:
        verbose_name="Միասնական Տեսակ"
        verbose_name_plural="Միասնական Տեսակ"



class OfferSection(models.Model):
    __tablename__ = 'offer'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")


    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Առաջարկի սեկցիա"
        verbose_name_plural="Առաջարկի սեկցիա"



class CourseProgram(models.Model):
    __tablename__ = 'cours'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    
    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Դասընթացի ծրագրի սեկցիա"
        verbose_name_plural="Դասընթացի ծրագրի սեկցիա"



class EndOfCourse(models.Model):
    __tablename__ = 'endofcours'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    
    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Դասընթացի ավարտի սեկցիա"
        verbose_name_plural="Դասընթացի ավարտի սեկցիա"



class CourseConducted(models.Model):
    __tablename__ = 'conducted'
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    
    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Դասընթացը անցկացվել սեկցիա"
        verbose_name_plural="Դասընթացը անցկացվել սեկցիա"



class SpecialOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Վերնագիր")
    sub_title = models.CharField(max_length=200, verbose_name="փոքր Վերնագիր")
    description_1 = models.TextField("նկարագրություն")
    description_2 = models.TextField("նկարագրություն")
    description_3 = models.TextField("նկարագրություն")
    description_4 = models.TextField("նկարագրություն")
    button = models.CharField(max_length=40, verbose_name="կնոպկա")


    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Հատուկ առաջարկ սեկցիա"
        verbose_name_plural="Հատուկ առաջարկ սեկցիա"


class Contacts(models.Model):
    title = models.CharField(max_length=50, verbose_name="Վերնագիր")
    icon_1 = models.ImageField("Նկար", upload_to="images/icon/")
    href_1 = models.CharField(max_length=100, verbose_name="հղում")
    icon_2 = models.ImageField("Նկար", upload_to="images/icon/")
    href_2 = models.CharField(max_length=100, verbose_name="հղում")
    tel = models.CharField("հեր", max_length=40)
    email = models.CharField("մեիլ", max_length=100)


    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Կոնտակտային սեկցիա"
        verbose_name_plural="Կոնտակտային սեկցիա"