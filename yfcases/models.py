from django.db import models

class City(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  class Meta:
    # managed = True
    db_table = 'yfcase_city'

class Township(models.Model):
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name
 
  class Meta:
    # managed = True
    db_table = 'yfcase_township'
    
class Yfcase(models.Model):
  yfcaseCaseNumber=models.CharField(u'案號(*)',max_length=100)
  yfcaseCompany=models.CharField(u'所屬公司',max_length=50,null=True,blank=True)
  yfcaseCity=models.ForeignKey(City,verbose_name = u'縣市',on_delete=models.SET_NULL,null=True)
  yfcaseTownship=models.ForeignKey(Township,verbose_name = u'鄉鎮區里', on_delete=models.SET_NULL, null=True)
  yfcaseBigSection=models.CharField(u'段號',max_length=10,null=True,blank=True)
  yfcaseSmallSection=models.CharField(u'小段',max_length=10,null=True,blank=True)
  yfcaseVillage=models.CharField(u'村里',max_length=100,null=True,blank=True)
  yfcaseNeighbor=models.CharField(u'鄰',max_length=100,null=True,blank=True)
  yfcaseStreet=models.CharField(u'街路',max_length=100,null=True,blank=True)
  yfcaseSection=models.CharField(u'段',max_length=100,null=True,blank=True)
  yfcaseLane=models.CharField(u'巷',max_length=100,null=True,blank=True)
  yfcaseAlley=models.CharField(u'弄',max_length=100,null=True,blank=True)
  yfcaseNumber=models.CharField(u'號',max_length=100,null=True,blank=True)
  yfcaseFloor=models.CharField(u'樓(含之幾)',max_length=100,null=True,blank=True)
  yfcaseDebtor=models.CharField(u'債務人',max_length=10,null=True,blank=True)
  yfcaseCreditor=models.CharField(u'債權人',max_length=10,null=True,blank=True)
  yfcaseStatus = models.BooleanField(u'案件狀態',default=False)
  user = models.ForeignKey('users.CustomUser',verbose_name = u'區域負責人', on_delete=models.CASCADE)
		

  def __str__(self):
    return self.yfcaseCaseNumber	

  class Meta:
    # managed = True
    db_table = 'yfcase_yfcase'
