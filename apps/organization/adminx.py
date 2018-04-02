# coding:utf-8
__date__ = '2018/3/14 11:36'

import xadmin
from .models import *


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', ]
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', ]
    list_filter = ['name', 'desc', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years']
    search_fields = ['org', 'name', 'work_years']
    list_filter = ['org', 'name', 'work_years']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)