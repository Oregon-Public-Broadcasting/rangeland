from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Standard(models.Model):
    name = models.CharField(max_length=255)

class Cause(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class NEPAType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FieldOffice(models.Model):
    state = models.ForeignKey("State")
    office_code = models.CharField(max_length=55)
    office_name = models.CharField(max_length=255)

    def __str__(self):
        return self.office_name


class Operator(models.Model):

    field_office = models.ForeignKey("FieldOffice")
    auth_no = models.CharField(max_length=255)
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
    allotment_id = models.CharField(max_length=255)
    allotment_name = models.CharField(max_length=255)
    available_for_grazing = models.CharField(max_length=1)
    grazing_decision = models.CharField(max_length=255)
    public_acres = models.IntegerField()
    amp_text = models.CharField(max_length=255)
    amp_implement_date = models.DateTimeField()
    management_stat_text = models.CharField(max_length=255)
    auth_no	= models.ManyToManyField("Operator")
    permitted_aums = models.IntegerField()
    suspended_aums = models.IntegerField()
    susp_use_temp = models.CharField(max_length=10)
    new_allotment_id = models.CharField(max_length=10)

    def __str__(self):
        return "Allotment name: {}, State: {}".format(self.allotment_name,  self.field_office.state)

class Permit(models.Model):

    field_office = models.ForeignKey("FieldOffice")
    auth_no = models.ForeignKey("Operator")
    pl_effect_dt = models.DateTimeField()
    pl_exp_dt = models.DateTimeField()
    permit_status = models.CharField(max_length=50)
    allotment = models.ForeignKey("Allotment")
    livestock_number = models.IntegerField()
    livestock_kind = models.CharField(max_length=25)
    pd_beg_dt = models.DateTimeField()
    pd_end_dt = models.DateTimeField()
    type_use = models.CharField(max_length=50)
    pl_percent = models.IntegerField()
    aums = models.IntegerField()

    def __str__(self):
        return self.auth_no.operator_display_name

class Health(models.Model):

    field_office = models.ForeignKey("FieldOffice")
    allotment = models.ForeignKey("Allotment")
    auth_no = models.ForeignKey("Operator")
    land_health_eval_date = models.DateTimeField(null=True,blank=True) # Date of Most Recent Land Health Evaluation Report (mm/dd/yyyy)1
    causal_factors_date = models.DateTimeField(null=True,blank=True) #Date of most recent Determination of Causal Factor(s) (mm/dd/yy
    standards_not_met = models.ForeignKey("Standard") # Land Health Standard(s) Not Achieved in the Allotment and Signi	text	1
    cause_not_met = models.ForeignKey("Cause")
    nepa_type = models.ForeignKey("NEPAType") #Type of NEPA Analysis for Grazing Authorization (EA, EIS, CX, D
    nepa_date = models.DateTimeField(null=True,blank=True) #Date NEPA Analysis Completed (mm/dd/yyyy)5
    nepa_identifier = models.CharField(max_length=55) #NEPA Identifier6
    permit_status = models.CharField(max_length=55) #Permit or Lease Status

    def __str__(self):
        return self.allotment.allotment_name
