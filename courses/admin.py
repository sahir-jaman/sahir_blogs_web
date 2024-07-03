from django.contrib import admin
from .models import Course, Module, Section

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1  # Number of empty section forms to display

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1  # Number of empty module forms to display
    inlines = [SectionInline]  # Add SectionInline to ModuleInline

class CustomModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_course_title')
    list_filter = ('course__title',)  # Add course title to the filter
    search_fields = ('course__title', 'name')  # Add search fields

    def get_course_title(self, obj):
        return obj.course.title
    get_course_title.short_description = 'Course Title'

class CustomSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_module_name', 'get_course_title')
    list_filter = ('module__course__title', 'module__name')  # Add course and module name to the filter
    search_fields = ('module__course__title', 'module__name', 'title')  # Add search fields

    def get_module_name(self, obj):
        return obj.module.name
    get_module_name.short_description = 'Module Name'

    def get_course_title(self, obj):
        return obj.module.course.title
    get_course_title.short_description = 'Course Title'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(CustomModuleAdmin):
    inlines = [SectionInline]

@admin.register(Section)
class SectionAdmin(CustomSectionAdmin):
    pass
