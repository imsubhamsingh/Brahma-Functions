import os

# Define the default template directory
DEFAULT_TEMPLATE_DIR = "./templates"


class CodeGenerator:
    def __init__(self, template_dir=None):
        # If a custom template directory is specified, use it, otherwise use the default
        if template_dir:
            self.template_dir = template_dir
        else:
            self.template_dir = DEFAULT_TEMPLATE_DIR

    def generate_function_code(self, function_name, input_types, output_type, comments):
        # Load the template file
        if not os.path.exists(self.template_dir):
            os.makedirs(self.template_dir)
        template_path = os.path.join(self.template_dir, f"{function_name}.template")
        with open(template_path) as f:
            template = f.read()

        # Replace placeholders in the template with the actual values
        code = template.replace("{{function_name}}", function_name)
        code = code.replace("{{input_types}}", ", ".join(input_types))
        code = code.replace("{{output_type}}", output_type)
        code = code.replace("{{comments}}", comments)

        return code

    # def generate_tests(self, function_name, input_types, output_type, comments):
    #     # Load the template file
    #     template_path = os.path.join(self.template_dir, f'{function_name}.template')
    #     with open(template_path) as f:
    #         template = f.read()

    #     # Replace placeholders in the template with the actual values
    #     code = template.replace('{{function_name}}', function_name)
    #     code = code.replace('{{input_types}}', ', '.join(input_types))
    #     code = code.replace('{{output_type}}', output_type)
    #     code = code.replace('{{comments}}', comments)

    #     return code

    # def generate_class(self, class_name, attributes, methods, comments):
    #     # Load the template file
    #     template_path = os.path.join(self.template_dir, f'{class_name}.template')
    #     with open(template_path) as f:
    #         template = f.read()

    #     # Replace placeholders in the template with the actual values
    #     code = template.replace('{{class_name}}', class_name)
    #     code = code.replace('{{attributes}}', ', '.join(attributes))
    #     code = code.replace('{{methods}}', ', '.join(methods))
    #     code = code.replace('{{comments}}', comments)

    #     return code

    # def generate_class_tests(self, class_name, attributes, methods, comments):
    #     # Load the template file
    #     template_path = os.path.join(self.template_dir, f'{class_name}.template')
    #     with open(template_path) as f:
    #         template = f.read()

    #     # Replace placeholders in the template with the actual values
    #     code = template.replace('{{class_name}}', class_name)
    #     code = code.replace('{{attributes}}', ', '.join(attributes))
    #     code = code.replace('{{methods}}', ', '.join(methods))
    #     code = code.replace('{{comments}}', comments)

    #     return code


if __name__ == "__main__":
    # Test the code generation
    cg = CodeGenerator()
    code = cg.generate_code(
        "add_nums", ["int", "int"], "int", "This function adds two numbers"
    )
    print(code)
