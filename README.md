# skills
# https://gist.github.com/rxaviers/7360908
Repository with projects especially focused on Computer Science and Natural Sciences.

# ARCHITECTURE SCAFFOLD

```
📦jorge_cardona_project [project_directory]
┗ 📂application [package]
┃ ┣ main.py [__main__]
┃ ┣ 📂configuration
┃ ┣ 📂log
┃ ┣ 📂htmlcov
┃ ┣ 📂utils
┃ ┣ 📂domain [package]
┃ ┃ ┣ 📂models [package]
┃ ┃ ┣ 📂interfaces [package]
┃ ┃ ┃ ┗ 📂repository [package]
┃ ┃ ┃ ┗ 📂business [package]
┃ ┃ ┣ 📂usecases [package]
┃ ┃ ┣ 📂services [package]
┗ 📂deployment [package]
┗ 📂requirements [package]
┗ 📂test [package]
┗ 📜 README.md
┗ ⚠️ .gitignore
```

# PROJECT PACKAGES STRUCTURE
```
📦jorge_cardona_project [project_directory]
┗ 📂application [package]
┃ ┣ main.py [__main__]
┃ ┣ 📂configuration
┃ ┣ ┗ 🏩 app_configuration.py
┃ ┣ 📂log
┃ ┣ ┗ 💬 logging.log
┃ ┣ 📂htmlcov
┃ ┣ ┗ 📜 main_py.html
┃ ┣ 📂utils
┃ ┣ ┗ 🐍 script.py
┃ ┣ ┗ 🎰 file.yaml
┃ ┣ ┗ 📜 image.jpg
┃ ┣ 📂domain [package]
┃ ┃ ┣ 📂models [package]
┃ ┃ ┃ ┣ 📂entity_one
┃ ┃ ┃ ┃ ┗ 🐍 Entity_ONE.py
┃ ┃ ┃ ┣ 📂entity_two
┃ ┃ ┃ ┃ ┗ 🐍 Entity_TWO.py
┃ ┃ ┃ ┣ 📂entity_n
┃ ┃ ┃ ┃ ┗ 🐍 Entity_N.py
┃ ┃ ┣ 📂interfaces [package]
┃ ┃ ┃ ┗ 📂repository [package]
┃ ┃ ┃ ┃ ┣ 📂model_one
┃ ┃ ┃ ┃ ┃ ┗ 🐟 database_method_model_Entity_ONE.py
┃ ┃ ┃ ┃ ┣ 📂model_two
┃ ┃ ┃ ┃ ┃ ┗ 🐟 database_method_model_Entity_TWO.py
┃ ┃ ┃ ┃ ┣ 📂model_n
┃ ┃ ┃ ┃ ┃ ┗ 🐟 database_method_model_Entity_N.py
┃ ┃ ┃ ┗ 📂business [package]
┃ ┃ ┃ ┃ ┣ 📂model_one
┃ ┃ ┃ ┃ ┃ ┗ 🐦 business_method_model_Entity_ONE.py
┃ ┃ ┃ ┃ ┣ 📂model_two
┃ ┃ ┃ ┃ ┃ ┗ 🐦 business_method_model_Entity_TWO.py
┃ ┃ ┃ ┃ ┣ 📂model_n
┃ ┃ ┃ ┃ ┃ ┗ 🐦 business_method_model_Entity_N.py
┃ ┃ ┣ 📂usecases [package]
┃ ┃ ┃ ┣ 📂model_one
┃ ┃ ┃ ┃ ┗ 🎎 use_case_implementation_business_repository_logic_model_ONE.py
┃ ┃ ┃ ┣ 📂model_two
┃ ┃ ┃ ┃ ┗ 🎎 use_case_implementation_business_repository_logic_model_TWO.py
┃ ┃ ┃ ┣ 📂model_n
┃ ┃ ┃ ┃ ┗ 🎎 use_case_implementation_business_repository_logic_model_N.py
┃ ┃ ┣ 📂services [package]
┃ ┃ ┃ ┣ 📂model_one
┃ ┃ ┃ ┃ ┗ ✈️ services_use_case_implementation_model_ONE.py
┃ ┃ ┃ ┣ 📂model_two
┃ ┃ ┃ ┃ ┗ ✈️ services_use_case_implementation_model_TWO.py
┃ ┃ ┃ ┣ 📂model_n
┃ ┃ ┃ ┃ ┗ ✈️ services_use_case_implementation_model_N.py
┗ 📂deployment [package]
┃ ┗ 🐳 Dockerfile
┃ ┗ 🎰 Manifest.yaml
┗ 📂requirements [package]
┃ ┗ 📄 requirements.txt
┗ 📂test [package]
┃ ┃ ┣ 📂test_one
┃ ┃ ┃ ┗ 🍄 use_case_implementation_one.py
┃ ┃ ┃ ┗ 🍄 services_use_case_implementation_one.py
┃ ┃ ┣ 📂test_two
┃ ┃ ┃ ┗ 🍄 use_case_implementation_two.py
┃ ┃ ┃ ┗ 🍄 services_use_case_implementation_two.py
┃ ┃ ┣ 📂test_n
┃ ┃ ┃ ┗ 🍄 use_case_implementation_n.py
┃ ┃ ┃ ┗ 🍄 services_use_case_implementation_n.py
┗ 📜 README.md
┗ ⚠️ .gitignore
```

# Application
Directory that contains the packages with the application code.

# Configuration
Contains all configuration files for the Application

# Log
Save information about the application log.

# htmlcov
Save unit testing coverage information about the application code.

# Utils
Contains transversal resources for the application, that is not possible to include in other layers.

# Entities
is a package that contains modules, the module it's a plain script, it contains only the class definition, no logic in the classes

# Interfaces
are interfaces that contain only the methods that need to be implemented in the use cases one directory by class.
- Repository: Contains modules with methods that are needed to communicate with the database by class.
- Business: Contains modules with methods that are needed to process the information by class.

# Use Cases
is a package that contains modules, the module is a class that implements the methods from the package interfaces(Repository, Business) and defines the business logic by module.

# Services
is a package that contains modules, the module is a class that contains the API services by functionality or by class and use the UseCases classes.

# Deployment
Directory that contains the Dockerfile, k8s Manifest, and every file needed for the deployment.

# Requirements
Directory containing the requirements.txt with the definition of project dependencies.

# Test
Directory that contains the unit testing from the Use Cases and Services files.