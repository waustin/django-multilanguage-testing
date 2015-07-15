from django.contrib import admin
from django import forms
from django.conf import settings
from .models import Page, PageTemplate

from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin

#from redactor.widgets import RedactorEditor


#class PageAdminForm(forms.ModelForm):
#    class Meta:
#        widgets = {
#            'content_en': RedactorEditor(),
#            'content_es': RedactorEditor(),
#        }


class PageAdmin(MPTTModelAdmin, TranslationAdmin):
    mptt_level_indent = 20
    list_select_related = True

    search_fields = ('title', 'content',)
    list_display = ('title', 'relative_url', 'template', 'is_hidden')
    list_filter = ('template',)

    #form = PageAdminForm

    fieldsets = (
        (None, {
            'fields': ('title', 'display_order', 'parent', 'is_hidden'),
        }),
        ('Body Content', {
            'classes': ('full-width',),
            'fields': ('content',),
        }),
        #('Media', {
        #    'fields': ('header_image',),
        #}),
        ('Meta Information', {
            'classes': ('collapse', 'grp-collapse grp-closed'),
            'fields': ('head_title', 'meta_description')
        }),
        ('Advaced options', {
            'classes': ('collapse', 'grp-collapse grp-closed'),
            'fields': ('template', )
        }),
    )

    #def formfield_for_dbfield(self, db_field, **kwargs):
    #    if db_field.name == 'content':
    #        kwargs.pop('request', None)
    #        kwargs['widget'] = forms.widgets.Textarea(attrs={'class': 'mceEditor',
    #                                                         'size': '40'})
    #        return db_field.formfield(**kwargs)
    #    return super(PageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    class Media:
        pass
        #js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
        #      settings.STATIC_URL + 'js/tiny_mce_init.js')


class PageTemplateAdmin(admin.ModelAdmin):
    pass


admin.site.register(PageTemplate, PageTemplateAdmin)
admin.site.register(Page, PageAdmin)
