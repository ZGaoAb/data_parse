from django.db import models


class Temperature(models.Model):
  #Year,No_Smoothing,Lowess
   year = models.IntegerField(db_index=True, primary_key=True)
   no_smoothing = models.FloatField()
   lowess = models.FloatField()



class Co2(models.Model):
    #Year, Month, Monthly_average, De_season_alized, St_dev_mon, Unc_of_mean
    year = models.ForeignKey(Temperature,on_delete=models.CASCADE)
    month = models.IntegerField()
    monthly_average = models.FloatField()
    de_season_alized = models.FloatField()
    st_dev_mon = models.FloatField()
    unc_of_mean = models.FloatField()




