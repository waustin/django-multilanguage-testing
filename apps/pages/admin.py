from django.contrib import admin
from django import forms
from django.conf import settings
from .models import Page, PageTemplate


from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin


#class PageAdminForm(forms.ModelForm):
#    content = forms.CharField(
#        widget=forms.widgets.Textarea(attrs={'class': 'mceEditor',
#                                             'size': '40'}),
#        required=False)


class PageAdmin(MPTTModelAdmin, TranslationAdmin):
    mptt_level_indent = 20
    list_select_related = True

    search_fields = ('title', 'content',)
    list_display = ('title', 'relative_url', 'template', 'is_hidden')
    list_filter = ('template',)

    # form = PageAdminForm

    fieldsets = (
        (None, {
            'fields': ('title', 'display_order', 'parent', 'is_hidden'),
        }),
        ('Body Content', {
            'classes': ('full-width',),
            'fields': ('content',),
        }),
        ('Meta Information', {
            'classes': ('collapse', 'grp-collapse grp-closed'),
            'fields': ('head_title', 'meta_description')
        }),
        ('Advaced options', {
            'classes': ('collapse', 'grp-collapse grp-closed'),
            'fields': ('template', )
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.widgets.Textarea(attrs={'class': 'mceEditor',
                                                             'size': '40'})
            return db_field.formfield(**kwargs)
        return super(PageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
              settings.STATIC_URL + 'js/tiny_mce_init.js')


class PageTemplateAdmin(admin.ModelAdmin):
    pass


admin.site.register(PageTemplate, PageTemplateAdmin)
admin.site.register(Page, PageAdmin)
