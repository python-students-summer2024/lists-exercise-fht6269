# mood_assessor.py

import datetime
import os

def assess_mood():
    
    date_today = datetime.date.today()
    date_today = str(date_today)

    if mood_recorded():
        print("Mood already entered today.")
        return
    
    valid_moods = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2
    }
    response = True
    while response:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").lower()
        if mood in valid_moods:
            response = False
            return valid_moods[mood]
            
        else:
            print("Invalid mood entered. Please try again.")
    
    storing_mood(date_today, valid_moods)
    diagnosis()

def mood_recorded():
    date_today = str(datetime.date.today())
    filepath = os.path.join('data', 'mood_diary.txt')
    
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith(date_today):
                return True
    return False

def storing_mood(date_today, mood_value):
    date_today = str(datetime.date.today())
    filepath = os.path.join('data', 'mood_diary.txt')
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'a') as file:
        file.write(f"{date_today},{mood_value}\n")

def diagnosis():
    filepath = os.path.join('data', 'mood_diary.txt')
    
    with open(filepath, 'r') as file:
        entries = file.readlines()
    
    if len(lines) < 7:
        return 
    elif len(entries) >= 7:
        last_seven_entries = entries[-7:]
        return last_seven_entries
    
    happy_count = 0
    sad_count = 0
    apathetic_count = 0

    for entries in last_seven_entries:
        if entries == 2:
            happy_count += 1
        elif entries == -1:
            sad_count += 1
        elif entries == 0:
            apathetic_count += 1
        
    if happy_count >= 5:
        diagnosis = "Maniac"
    elif sad_count >= 4:
        diagnosis = "depressive"
    elif apathetic_count >= 6:
        diagnosis = "schizoid"
    else:
        diagnosis = sum(last_seven_entries) / 7
    
    print(f'Your diagnosis is {diagnosis}')
