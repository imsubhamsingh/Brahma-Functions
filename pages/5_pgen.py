import streamlit as st
import shutil
import os

from brahma_functions.constants import FRAMEWORKS, PROJECT_TYPES

# Define the project templates directory
PROJECT_TEMPLATES_DIR = "project_templates"

# Define the destination directory for the generated project
OUTPUT_DIR = "generated_project"

# List of available frameworks for each project type
FRAMEWORKS = FRAMEWORKS

# Project Templates:
# Prepare a set of project templates for different project types and frameworks.
# Templates should include placeholder variables for customization.


def setup_web_project(project_type="Web", framework="Html-Css-Js"):
    # Setup the project templates for the "Web" project type
    # create the files and folders for the project templates
    # Folder structure:
    # {PROJECT_TEMPLATES_DIR}/Web/{project_name}/
    # ├── README.md
    # ├── index.html
    # ├── app.js
    # ├── style.css

    # Create the project templates directory if it doesn't exist
    if not os.path.exists(PROJECT_TEMPLATES_DIR):
        os.makedirs(PROJECT_TEMPLATES_DIR)

        # Create the project templates
        if project_type == "Web":
            for framework in FRAMEWORKS[project_type]:
                # Define the source directory for the project template
                project_template_dir = os.path.join(
                    PROJECT_TEMPLATES_DIR, project_type, framework
                )

                # Create the project template directory if it doesn't exist
                if not os.path.exists(project_template_dir):
                    os.makedirs(project_template_dir)

                # Create the project template files
                open(os.path.join(project_template_dir, "README.md"), "w").close()
                open(os.path.join(project_template_dir, "main.py"), "w").close()
                open(os.path.join(project_template_dir, "index.html"), "w").close()

                # Create the project template folders
                os.makedirs(os.path.join(project_template_dir, "static"))
                os.makedirs(os.path.join(project_template_dir, "static", "css"))
                os.makedirs(os.path.join(project_template_dir, "static", "js"))

                # Copy the project template files from the source directory to the destination directory
                shutil.copy(
                    os.path.join(project_template_dir, "README.md"),
                    os.path.join(project_template_dir, "README.md"),
                )
                shutil.copy(
                    os.path.join(project_template_dir, "main.py"),
                    os.path.join(project_template_dir, "main.py"),
                )
                shutil.copy(
                    os.path.join(project_template_dir, "index.html"),
                    os.path.join(project_template_dir, "index.html"),
                )
                shutil.copy(
                    os.path.join(project_template_dir, "static", "css", "style.css"),
                    os.path.join(project_template_dir, "static", "css", "style.css"),
                )
                shutil.copy(
                    os.path.join(project_template_dir, "static", "js", "app.js"),
                    os.path.join(project_template_dir, "static", "js", "app.js"),
                )


def generate_project_template(project_type, framework):
    # Logic to generate project template based on project_type and framework
    if project_type == "Web":
        if framework == "Html-Css-Js":
            # Generate template for HTML/CSS/JS project
            template = """
            <!-- HTML/CSS/JS project template -->
            """
        elif framework == "Bootstrap":
            # Generate template for Bootstrap project
            template = """
            <!-- Bootstrap project template -->
            """
        elif framework == "Tailwind":
            # Generate template for Tailwind project
            template = """
            <!-- Tailwind project template -->
            """
        # Add more conditions for other frameworks within the "Web" project type

    elif project_type == "Backend":
        pass
    return template


def setup_project_templates():
    # Create the project templates directory if it doesn't exist
    if not os.path.exists(PROJECT_TEMPLATES_DIR):
        os.makedirs(PROJECT_TEMPLATES_DIR)

    # Create the project templates
    for project_type in PROJECT_TYPES:
        for framework in FRAMEWORKS[project_type]:
            # Define the source directory for the project template
            project_template_dir = os.path.join(
                PROJECT_TEMPLATES_DIR, project_type, framework
            )

            # Create the project template directory if it doesn't exist
            if not os.path.exists(project_template_dir):
                os.makedirs(project_template_dir)

            # Create the project template files
            open(os.path.join(project_template_dir, "README.md"), "w").close()
            open(os.path.join(project_template_dir, "main.py"), "w").close()
            open(os.path.join(project_template_dir, "index.html"), "w").close()
            open(os.path.join(project_template_dir, "app.js"), "w").close()
            open(os.path.join(project_template_dir, "style.css"), "w").close()
            open(os.path.join(project_template_dir, "requirements.txt"), "w").close()
            open(os.path.join(project_template_dir, "package.json"), "w").close()
            open(os.path.join(project_template_dir, "package-lock.json"), "w").close()
            open(os.path.join(project_template_dir, "Dockerfile"), "w").close()
            open(os.path.join(project_template_dir, "docker-compose.yml"), "w").close()
            open(os.path.join(project_template_dir, "Procfile"), "w").close()
            open(os.path.join(project_template_dir, "manage.py"), "w").close()
            open(os.path.join(project_template_dir, "config.py"), "w").close()
            open(os.path.join(project_template_dir, "settings.py"), "w").close()
            open(os.path.join(project_template_dir, "urls.py"), "w").close()
            open(os.path.join(project_template_dir, "views.py"), "w").close()
            open(os.path.join(project_template_dir, "models.py"), "w").close()
            open(os.path.join(project_template_dir, "admin.py"), "w").close()
            open(os.path.join(project_template_dir, "serializers.py"), "w").close()
            open(os.path.join(project_template_dir, "api.py"), "w").close()
            open(os.path.join(project_template_dir, "api.js"), "w").close()
            open(os.path.join(project_template_dir, "api.test.js"), "w").close()

            # Create the project template directories
            os.makedirs(os.path.join(project_template_dir, "static"))
            os.makedirs(os.path.join(project_template_dir, "templates"))
            os.makedirs(os.path.join(project_template_dir, "src"))
            os.makedirs(os.path.join(project_template_dir, "src", "components"))
            os.makedirs(os.path.join(project_template_dir, "src", "pages"))
            os.makedirs(os.path.join(project_template_dir, "src", "utils"))
            os.makedirs(os.path.join(project_template_dir, "src", "assets"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles"))
            os.makedirs(
                os.path.join(project_template_dir, "src", "styles", "components")
            )
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "pages"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "utils"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "assets"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "global"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "themes"))
            os.makedirs(
                os.path.join(project_template_dir, "src", "styles", "animations")
            )
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "mixins"))
            os.makedirs(
                os.path.join(project_template_dir, "src", "styles", "variables")
            )
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "fonts"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "icons"))
            os.makedirs(os.path.join(project_template_dir, "src", "styles", "images"))

        return True

    return False


def generate_project(project_type, framework, project_name):
    # Define the source directory for the project template
    project_template_dir = os.path.join(PROJECT_TEMPLATES_DIR, project_type, framework)

    # Copy the project template to the output directory
    shutil.copytree(project_template_dir, OUTPUT_DIR)

    # Rename the project directory
    os.rename(
        os.path.join(OUTPUT_DIR, framework), os.path.join(OUTPUT_DIR, project_name)
    )


def main():
    st.title("PGen 🕊️")

    # User inputs
    project_type = st.selectbox("Select Project Type", PROJECT_TYPES)
    framework = st.selectbox("Select Framework", FRAMEWORKS[project_type])
    project_name = st.text_input("Enter Project Name")

    if st.button("Generate Project"):
        # Create the output directory if it doesn't exist
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # Generate the project
        generate_project(project_type, framework, project_name)
        st.success("Project generated successfully!")

        # Provide a download link for the generated project
        st.markdown(
            f'<a href="{OUTPUT_DIR}" download="generated_project.zip">Download Project</a>',
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
