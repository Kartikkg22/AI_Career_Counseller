from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'name', 'email', 'interests', 'strengths',
            'tenth_score', 'twelfth_score', 'degree_cgpa',
            'skills', 'career_goal'
        ]
        widgets = {
            'interests': forms.Textarea(attrs={'rows': 2}),
            'strengths': forms.Textarea(attrs={'rows': 2}),
            'career_goal': forms.Textarea(attrs={'rows': 2}),
            'skills': forms.Textarea(attrs={'rows': 2}),
        }

# if form.is_valid():
#     saved_user = form.save()
#     return redirect('career_suggestions', user_id=saved_user.id)
