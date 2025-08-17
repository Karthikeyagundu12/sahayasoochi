import os

folder_path = 'd:/sahayasoochi_voice_app'  # Update this if needed

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f'--- {filename} ---')
            print(f.read())
            print('\n')