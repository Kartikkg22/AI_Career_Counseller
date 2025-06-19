from django.shortcuts import render, redirect
from .forms import UserProfileForm
import openai
from django.conf import settings
from .models import UserProfile
from .openai_logic import generate_career_suggestions  # put GPT logic here

def user_profile_form(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            saved_user = form.save()
            return redirect('career_suggestions', user_id=saved_user.id)
    else:
        form = UserProfileForm()
    return render(request, 'counsellor/form.html', {'form': form})


def career_suggestions(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    suggestions = generate_career_suggestions(user)
    return render(request, 'counsellor/results.html', {
        'user': user,
        'suggestions': suggestions
    })


def home(request):
    return render(request, 'counsellor/home.html')


def thank_you(request):  # Optional now
    return render(request, 'counsellor/thank_you.html')


def career_suggestions(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    suggestions = generate_career_suggestions(user)
    return render(request, 'counsellor/results.html', {
        'user': user,
        'suggestions': suggestions
    })

openai.api_key = settings.OPENAI_API_KEY

def generate_career_suggestions(user_profile):
    prompt = f"""
    Based on the following student profile:
    - Interests: {user_profile.interests}
    - Strengths: {user_profile.strengths}
    - Academic Scores: 10th: {user_profile.tenth_score}, 12th: {user_profile.twelfth_score}, Degree CGPA: {user_profile.degree_cgpa}
    - Skills: {user_profile.skills}
    - Career Goal: {user_profile.career_goal}

    Suggest the top 3 suitable career paths for this student. For each, give a short explanation and 3 skill-building suggestions.
    """

    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert career counselor."},
                {"role": "user", "content": prompt}
            ]
    )
    return response['choices'][0]['message']['content']


# Create your views here.
def home(request):
    return render(request, 'counsellor/home.html')

def user_profile_form(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            saved_user = form.save()
            return redirect('career_suggestions', user_id=saved_user.id)
    else:
        form = UserProfileForm()
    return render(request, 'counsellor/form.html', {'form': form})  # Render the form template

def thank_you(request):
    return render(request, 'counsellor/thank_you.html')