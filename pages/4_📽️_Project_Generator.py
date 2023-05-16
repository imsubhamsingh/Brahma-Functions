import streamlit as st
import os
import shutil
from jinja2 import Template

# Function to create function file with given function name
def create_function_file(function_name):
    file_name = f"{function_name}.py"
    file_path = os.path.join("functions", file_name)
    st.write(file_path)
    with open(file_path, "w") as f:
        f.write(f"def {function_name}():\n    pass\n")
    st.success(f"Function file '{file_name}' created successfully!")


# Function to create package with given package name
def create_package(package_name):
    package_path = os.path.join("functions", package_name)
    os.mkdir(package_path)
    init_file_path = os.path.join(package_path, "__init__.py")
    with open(init_file_path, "w") as f:
        pass
    st.success(f"Package '{package_name}' created successfully!")


# Function to generate code based on selected template
def generate_code(template, function_name, package_name=None):
    if package_name:
        package_path = os.path.join("functions", package_name)
        if not os.path.exists(package_path):
            create_package(package_name)
        file_path = os.path.join(package_path, f"{function_name}.py")
    else:
        file_path = os.path.join("functions", f"{function_name}.py")
    with open(template, "r") as f:
        template_code = f.read()
    with open(file_path, "w") as f:
        f.write(template_code.replace("{function_name}", function_name))
    st.success(f"Code generated successfully at {file_path}!")


# Function to create a new template
def create_template(template_name, template_code):
    template_path = os.path.join("templates", f"{template_name}.txt")
    with open(template_path, "w") as f:
        f.write(template_code)
    st.success(f"Template '{template_name}' created successfully!")


# Function to load existing templates
def load_template(template_name):
    template_path = os.path.join("templates", f"{template_name}")
    with open(template_path, "r") as f:
        template_code = f.read()
    return template_code


# Function to delete template
def delete_template(template_name):
    template_path = os.path.join("templates", f"{template_name}")
    os.remove(template_path)
    st.success(f"Template '{template_name}' deleted successfully!")


# Streamlit app
def sapp():
    st.set_page_config(page_title="Brahma Functions App", page_icon=":rocket:")
    st.title("Brahma Functions App")

    menu_items = [
        "Create function file",
        "Create package",
        "Generate code from template",
        "Create template",
        "Load template",
        "Delete template",
    ]
    choice = st.sidebar.selectbox("Select an action", menu_items)

    if choice == "Create function file":
        function_name = st.text_input("Enter function name")
        if st.button("Create"):
            if not function_name:
                st.error("Please enter a function name!")
            else:
                create_function_file(function_name)

    elif choice == "Create package":
        package_name = st.text_input("Enter package name")
        if st.button("Create"):
            if not package_name:
                st.error("Please enter a package name!")
            else:
                create_package(package_name)

    elif choice == "Generate code from template":
        template_name = st.selectbox("Select a template", os.listdir("templates"))
        function_name = st.text_input("Enter function name")
        package_name = st.text_input("Enter package name (optional)")
        if st.button("Generate"):
            if not function_name:
                st.error("Please enter a function name!")
            else:
                template_path = os.path.join("templates", template_name)
                generate_code(template_path, function_name, package_name)

    elif choice == "Create template":
        template_name = st.text_input("Enter template name")
        template_code = st.text_area("Enter template code")
        if st.button("Create"):
            if not template_name:
                st.error("Please enter a template name!")
            elif not template_code:
                st.error("Please enter template code!")
            else:
                create_template(template_name, template_code)

    elif choice == "Load template":
        template_name = st.selectbox("Select a template", os.listdir("templates"))
        if st.button("Load"):
            template_code = load_template(template_name)
            st.code(template_code)

    elif choice == "Delete template":
        template_name = st.selectbox("Select a template", os.listdir("templates"))
        if st.button("Delete"):
            delete_template(template_name)


def generate_script(template_file, output_file, **kwargs):
    """Generate a script using the specified template and arguments."""
    # Load the template file
    with open(template_file, "r") as f:
        template = Template(f.read())

    # Render the template with the specified arguments
    rendered = template.render(**kwargs)

    # Write the rendered script to the output file
    with open(output_file, "w") as f:
        f.write(rendered)


def generate_project(project_name, template_dir, output_dir, **kwargs):
    """Generate a project using the specified template directory and arguments."""
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Recursively copy the template directory to the output directory
    shutil.copytree(template_dir, os.path.join(output_dir, project_name))

    # Render all the templates in the output directory with the specified arguments
    for root, dirs, files in os.walk(os.path.join(output_dir, project_name)):
        for filename in files:
            template_file = os.path.join(root, filename)
            with open(template_file, "r") as f:
                template = Template(f.read())
            rendered = template.render(**kwargs)
            output_file = os.path.join(root, filename)
            with open(output_file, "w") as f:
                f.write(rendered)


# Define constants for the app
APP_TITLE = "Brahma Functions"
TEMPLATES_DIR = "templates"

# Define the main function to generate the code
def generate_code(function_name, function_description, inputs, outputs, template):

    # Load the selected template
    with open(os.path.join(TEMPLATES_DIR, template)) as f:
        template_str = f.read()

    # Render the template with the given inputs
    rendered_template = Template(template_str).render(
        function_name=function_name,
        function_description=function_description,
        inputs=inputs,
        outputs=outputs,
    )

    # Return the rendered code
    return rendered_template


# Define a function to save a template to a file
def save_template(template_name, template_code):
    with open(os.path.join(TEMPLATES_DIR, f"{template_name}.jinja"), "w") as f:
        f.write(template_code)


# Define a function to load a list of available templates
def load_templates():
    templates = os.listdir(TEMPLATES_DIR)
    return [t for t in templates if t.endswith(".jinja")]


# Define the main app function
def app():
    # Set the app title
    st.set_page_config(page_title=APP_TITLE)

    # Set the app header
    st.title(APP_TITLE)

    # Get the function name from the user
    function_name = st.text_input("Function Name")

    # Get the function description from the user
    function_description = st.text_input("Function Description")

    # Get the inputs from the user
    inputs = []
    add_input = st.button("Add Input")
    while add_input:
        input_name = st.text_input("Input Name", key="input_name")
        input_type = st.selectbox("Input Type", ["int", "float", "string", "boolean"])
        inputs.append((input_name, input_type))
        # add_input = st.button("Add Another Input")

    # Get the outputs from the user
    outputs = []
    add_output = st.button("Add Output")
    while add_output:
        output_name = st.text_input("Output Name", key="output_name")
        output_type = st.selectbox("Output Type", ["int", "float", "string", "boolean"])
        outputs.append((output_name, output_type))
        add_output = st.button("Add Another Output")

    # Get the selected template from the user
    templates = load_templates()
    selected_template = st.selectbox("Select a template", templates)

    # Allow the user to customize the selected template
    with open(os.path.join(TEMPLATES_DIR, selected_template)) as f:
        template_str = f.read()
    template_code = st.text_area("Customize the template", template_str)

    # Allow the user to save the customized template
    save_template_name = st.text_input("Save the template as")
    if save_template_name:
        save_template(save_template_name, template_code)

    # Generate the code using the user inputs and the selected template
    code = generate_code(
        function_name, function_description, inputs, outputs, selected_template
    )

    # Display the generated code to the user
    st.code(code, language="python")


if __name__ == "__main__":
    app()
    sapp()
