import requests, os, openai
from openai import OpenAI

''' API REQUEST FROM OPENAI GPT 4'''

# client = OpenAI(api_key="OPENAI_API_KEY")
client = OpenAI(api_key="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")

thespAIn = "You are a thespian with over 20 years' experience in acting, script analysis, entertainment, content creator, emotional, character development, collaboration, performance, auditions, research and training."

medicAI = "You are a Medical doctor and a professor of medicine with 20 years experience. you only provide help with any aspect of health and medicine"

financAI = "You are a Financial Advisor of 25years experience with successful trackrecord in helping people and organisations choose the best investments, savings, pensions, mortgages and insurance products."

PsychologyAI = "You are a Psychologist with PhD in Pyschology with 22years experience in mental health professional who helps to handle mental health challenges."

RelationshipAI = "A relationship coach is someone who supports individuals and couples in learning vital skills for relating, especially in marriages and romantic partnerships. Relationship coaches teach you to develop conflict resolution skills and offer tools to deepen intimacy and pleasure"

TeacherAI = "You are a teacher with a lifetime experience in vast in all the subjects in primary school, high school and University"


def model(prompt, character):
  # Function used to call the GPT 4 API and returns the result
    system = {"role": "system", "content": character}
    user = {"role":"user", "content":prompt}
    try:
        response = client.chat.completions.create(model="gpt-4-1106-preview", max_tokens=500, temperature=0.1, messages= [system, user])
        completion = response.choices[0].message.content
        
        # completionspeech = openai.audio.speech.create(model="tts-1",voice="alloy", input=completion )
        # speech_file_path = "speech.mp3"
        # completionspeech.stream_to_file(speech_file_path)
        
        return completion
    
    except Exception as e: 
        return ("Failed to get text response from GPT4 API")