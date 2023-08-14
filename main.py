import os
import subprocess

def install_packages():
    """ Function for installing packages """
    path = os.path.join(os.getcwd(), app_name)
    # Change the working directory to the new directory
    os.chdir(path)
    # Run the "flutter create testapp" command in the new folder
    result = subprocess.run('flutter pub add flutter_inappwebview && flutter pub add --dev flutter_launcher_icons', shell=True, capture_output=True, text=True)
    # Print the output of the command
    print(result.stdout)

def modify_main_dart(app_name):
    """ Function for modifying main.dart content """
    main_dart_path = os.path.join(os.getcwd(), app_name, 'lib', 'main.dart')
    
    # Read the content of main.dart
    with open(main_dart_path, 'r') as file:
        main_dart_content = file.read()

    # Make the necessary modifications to the content
    modified_main_dart = main_dart_content.replace(
        'You have pushed the button this many times:',
        'Modified Welcome Walid!'
    )

    # Write the modified content back to main.dart
    with open(main_dart_path, 'w') as file:
        file.write(modified_main_dart)
    file.close()

def create_flutter_app(app_name, package_name):
    """ For Creating Default App """
    try:
        os.system(f"flutter create --org {package_name} {app_name}")
        print(f"Flutter app '{app_name}' with package name '{package_name}' created successfully.")
        
        # Modify main.dart content
        modify_main_dart(app_name)
        
        # Install packages
        install_packages()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app_name = "noteapp"          # Change this to the desired app name
    package_name = "app"   # Change this to the desired package name
    create_flutter_app(app_name, package_name)
