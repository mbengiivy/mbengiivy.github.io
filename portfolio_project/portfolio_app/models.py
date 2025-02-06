from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, help_text="e.g., Cloud, CI/CD, etc.")
    # ... other fields if needed

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_app/static/portfolio_app/images/', blank=True, null=True)  # Project image
    github_link = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Skill) # Many-to-many with skills
    # ... other fields (e.g., project date, etc.)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Allow for current roles
    description = models.TextField()
    # ... other fields

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    course = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    # ... other fields

    def __str__(self):
        return f"{self.course} from {self.institution}"


class About(models.Model):
    summary = models.TextField()
    contact_email = models.EmailField()
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField()
    # ... other fields (e.g., profile picture)

    def __str__(self):
        return "About Me" # Only one instance