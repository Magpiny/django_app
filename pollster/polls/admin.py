from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Magpiny Polls'
admin.site.index_title = 'Pollstar Admin'

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date information', {'fields':['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInLine]





#admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
