import pickle

def save_preferences(preferences, filename='preferences.pkl'):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(preferences, file)
        print("Preferences saved successfully")
    except Exception as e:
        print("Error saving preferences:", e)

def load_preferences(filename='preferences.pkl'):
    try:
        with open(filename, 'rb') as file:
            preferences = pickle.load(file)
        print("Preferences loaded successfully")
        return preferences
    except FileNotFoundError:
        print("Preferences file not found. Using default settings")
        return {'theme': 'light', 'language': 'English', 'notifications': True}
    except (pickle.UnpicklingError, EOFError):
        print("Error: Preferences file is corrupted")
        return {'theme': 'light', 'language': 'English', 'notifications': True}

user_preferences = {
    'theme': 'dark',
    'language': 'Spanish',
    'notifications': False
}

save_preferences(user_preferences)
loaded_preferences = load_preferences()
print("Loaded Preferences:", loaded_preferences)

