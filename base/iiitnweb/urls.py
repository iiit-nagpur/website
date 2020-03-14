from django.urls import path
from . import views

# lol = views.Home()

urlpatterns = [
		path('', views.home, name='home'),
		path('contact/', views.contact, name='contact'),
		path('undergraduate/', views.Admission.Undergraduate, name='undergraduate'),
		path('postgraduate/', views.Admission.Postgraduate, name='postgraduate'),
		path('phd/', views.Admission.PhD, name='phd'),
		path('fees/', views.Admission.Fees, name='fees'),
		path('financialassist/', views.Admission.FinancialAssistance, name='financialassist'),
		path('questions/', views.Admission.Questions, name='question'),
		path('about/', views.Home.Abouts, name='about'),
        path('', views.Home.Mission, name='mission'),
		path('', views.Home.UpcomingCampus, name='campus'),
		path('', views.Home.Act, name='act'),
		path('faculty/', views.People.Faculty, name='facult'),
		path('adjunctfaculty/', views.People.AdjunctFaculty, name='adjunctfac'),
		path('staff/', views.People.Staff, name='staf'),
		path('btech/', views.People.Btech, name='btec'),
		path('mtech/', views.People.Mtech, name='mtec'),
		path('phd/', views.People.Phd, name='phdpeople'),
		path('', views.People.Alumni, name='alumni'),
		path('', views.Academics.Departments, name='departments'),
		path('', views.Academics.Programmes, name='program'),
		path('', views.Academics.Convocation, name='convocation'),
		path('', views.Academics.Resources, name='resources'),
		path('', views.Academics.StudentVerification, name='verification'),
		path('', views.Research.Publications, name='publications'),
		path('', views.Research.ResearchAreas, name='researchareas'),
		path('', views.Research.Events, name='events'),
		path('', views.Research.FellowshipAwards, name='awards'),
		path('', views.Placement.Message, name='message'),
		path('', views.Placement.WhyRecruit, name='whyrecruit'),
		path('', views.Placement.Procedure, name='procedure'),
		path('', views.Placement.Statistics, name='statistics'),
		path('', views.Placement.Internships, name='internships'),
		path('', views.Placement.Recruiters, name='recruiters'),
		path('', views.Placement.Startups, name='startups'),
		path('', views.Placement.ContactTnP, name='contactTnp'),
		path('', views.Careers.FacultyRecruitment, name='facrecruit'),
		path('', views.Careers.FacultyRecruitment, name='staffrecruit'),
		path('', views.StudentAffairs.EventsNews, name='eventnews'),
		path('', views.StudentAffairs.Facilities, name='facilities'),
		path('', views.StudentAffairs.Hostels, name='hostels'),
		path('', views.StudentAffairs.StudentClubs, name='studentclubs'),
		path('', views.StudentAffairs.DisciplineGrievance, name='grievance'),
]
