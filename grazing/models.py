from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class NEPAType(models.Model):
    name = models.CharField(max_length=255)
    abbr = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.name

# class Standard(models.Model):
#     name = models.CharField(max_length=255)
#
# class Cause(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name

class FieldOffice(models.Model):
    state = models.ForeignKey("State")
    office_code = models.CharField(max_length=55)
    office_name = models.CharField(max_length=255)

    def __str__(self):
        return self.office_name

class Authorization(models.Model):
    number = models.CharField(max_length=55)

    def __str__(self):
        return self.number

class Operator(models.Model):
    # field_office = models.ForeignKey("FieldOffice")
    # auth_no = models.CharField(max_length=55, null=True)
    auth_no = models.ManyToManyField("Authorization")
    operator_display_name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    st2 = models.CharField(max_length=255)
    zipcode15 = models.CharField(max_length=255)
    zipcode69 = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    release_text = models.CharField(max_length=255)

    def __str__(self):
        return self.operator_display_name

class Allotment(models.Model):

    field_office = models.ForeignKey("FieldOffice")
    allotment_number = models.CharField(max_length=11)
    allotment_unique = models.CharField(max_length=255)
    allotment_name = models.CharField(max_length=255)
    available_for_grazing = models.CharField(max_length=1)
    grazing_decision = models.CharField(max_length=255)
    public_acres = models.FloatField()
    amp_text = models.CharField(max_length=255)
    amp_implement_date = models.DateTimeField(null=True)
    management_stat_text = models.CharField(max_length=255)
    auth_no	= models.ManyToManyField("Authorization", null=True, blank=True)
    # following three fields are actually tied to permit rather than allotment
        #permitted_aums = models.IntegerField()
        #suspended_aums = models.IntegerField()
        #susp_use_temp = models.CharField(max_length=10)

    def __str__(self):
        return "Allotment name: {}, State: {}".format(self.allotment_name,  self.field_office.state)

class Permit(models.Model):

    field_office = models.ForeignKey("FieldOffice") # Is this really necessary if its already tied to allotment?
    auth_no = models.ForeignKey("Authorization")
    pl_effect_dt = models.DateTimeField()
    pl_exp_dt = models.DateTimeField()
    permit_status = models.CharField(max_length=50)
    allotment = models.ForeignKey("Allotment")
    livestock_number = models.FloatField()
    livestock_kind = models.CharField(max_length=25)
    pd_beg_dt = models.DateTimeField()
    pd_end_dt = models.DateTimeField()
    type_use = models.CharField(max_length=50)
    pl_percent = models.FloatField()
    aums = models.FloatField()

    def __str__(self):
        return self.auth_no.operator_display_name


class Health(models.Model):

    #field_office = models.ForeignKey("FieldOffice") # Is this really necessary if its already tied to allotment?
    allotment = models.ForeignKey("Allotment")
    allotment_name = models.CharField(max_length=255, null=True)
    allotment_unique = models.CharField(max_length=55, null=True)
    # auth_no = models.ForeignKey("Authorization") # Is this really necessary if its already tied to allotment?
    land_health_eval_date = models.DateTimeField(null=True,blank=True) # Date of Most Recent Land Health Evaluation Report (mm/dd/yyyy)1
    causal_factors_date = models.DateTimeField(null=True,blank=True) #Date of most recent Determination of Causal Factor(s) (mm/dd/yy
    land_health_status = models.CharField(max_length=3) #models.ManyToManyField("Standard") # Land Health Standard(s) Not Achieved in the Allotment and Signi	text	1
    #livestock_factor = models.NullBooleanField()
    description = models.TextField(null=True)
    # cause_not_met = models.ForeignKey("Cause")
    nepa_type = models.ForeignKey("NEPAType") #Type of NEPA Analysis for Grazing Authorization (EA, EIS, CX, D
    nepa_date = models.DateTimeField(null=True,blank=True) #Date NEPA Analysis Completed (mm/dd/yyyy)5
    nepa_identifier = models.CharField(max_length=55) #NEPA Identifier6
    permit_status = models.CharField(max_length=55) #Permit or Lease Status
    year_released = models.IntegerField(null=True) # 2012 or 2007 release from BLM to PEER/WWP?

    def __str__(self):
        return self.allotment.allotment_name

##############################################################################################################################################################################################

class Boundary(models.Model):
    allotment = models.ForeignKey("Allotment", null=True)  # Link this to our allotments, looks like some will not have a match
    allotment_name = models.CharField(max_length=255, null=True) # for boundaries that don't have an allotment entry in our db
    # allotment_number = models.CharField(max_length=55, null=True) # for boundaries that don't have an allotment entry in our db
    allotment_unique = models.CharField(max_length=255, null=True) # for boundaries that don't have an allotment entry in our db
    state = models.CharField(max_length=2, null=True) # for boundaries that don't have an allotment entry in our db
    geom = models.MultiPolygonField(srid=4326)  # Adjust SRID accordingly
    objects = models.GeoManager()

    def __str__(self):
        return "Allotment Boundary: " + self.allotment_name
