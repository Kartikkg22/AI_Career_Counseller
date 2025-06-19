import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
print(openai.api_key)

def generate_career_suggestions(user_profile):
    prompt = f"""
    You are an AI career counselor. A student has submitted their profile:
    
    Name: {user_profile.name}
    Email: {user_profile.email}
    Interests: {user_profile.interests}
    Strengths: {user_profile.strengths}
    Academic Scores:
      - 10th: {user_profile.tenth_score}%
      - 12th: {user_profile.twelfth_score}%
      - Degree CGPA: {user_profile.degree_cgpa}
    Skills: {user_profile.skills}
    Career Goal: {user_profile.career_goal}

    Based on this, suggest the top 3 suitable career paths for this student.
    For each, provide:
      - A brief explanation (2–3 lines)
      - 3 actionable steps or skill recommendations to start

    Format the response clearly with bullet points.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert career counselor."},
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
        

    except Exception as e:
        return f"⚠️ GPT API Error: {e}"
