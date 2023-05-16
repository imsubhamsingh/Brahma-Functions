# language to extension mapping
C = "C"
CPP = "C++"
CPP11 = "C++11"
CPP14 = "C++14"
CPP17 = "C++17"
CSHARP = "C#"
GO = "GO"
JAVA = "JAVA"
JAVA8 = "JAVA8"
JAVA14 = "JAVA14"
JAVASCRIPT = "JAVASCRIPT"
JAVASCRIPT_NODE = "JAVASCRIPT_NODE"
PHP = "PHP"
PYTHON = "PYTHON"
PYTHON3 = "PYTHON3"
RUBY = "RUBY"
SWIFT_4_1 = "SWIFT_4_1"
SWIFT_5_1 = "SWIFT"


LANG_TO_FILE_EXTENSION = {
    C: "c",
    CPP: "cpp",
    CPP11: "cpp11",
    CPP14: "cpp14",
    CPP17: "cpp17",
    CSHARP: "cs",
    GO: "go",
    JAVA: "java",
    JAVA8: "java8",
    JAVA14: "java14",
    JAVASCRIPT: "js",
    JAVASCRIPT_NODE: "njs",
    PHP: "php",
    PYTHON3: "py3",
    PYTHON: "py",
    RUBY: "rb",
    SWIFT_4_1: "swift",
    SWIFT_5_1: "swift",
}


TO_VERSIONS = {
    C: ["GCC 10.3", "GCC 9.3", "GCC 8.4"],
    CPP: ["C++17", "C++14", "C++11"],
    CPP11: ["C++17", "C++14", "C++11"],
    CPP14: ["C++17", "C++14", "C++11"],
    CPP17: ["C++17", "C++14", "C++11"],
    CSHARP: ["C# 9", "C# 8", "C# 7"],
    GO: ["1.15", "1.14", "1.13"],
    JAVA: ["14", "11", "8"],
    JAVA8: ["14", "11", "8"],
    JAVA14: ["14", "11", "8"],
    JAVASCRIPT: ["ES6", "ES5", "Rhino1.7", "Nodejs v18.15.0"],
    JAVASCRIPT_NODE: ["ES6", "ES5", "Rhino1.7", "Nodejs v18.15.0"],
    PHP: ["7.4", "7.3", "7.2"],
    PYTHON: ["3", "2"],
    PYTHON3: ["3", "2"],
    RUBY: ["3.0", "2.7", "2.6", "2.5"],
    SWIFT_4_1: ["4.1"],
    SWIFT_5_1: ["5.1"],
}


# Code types
CODE_TYPE_FUN = "Function"
CODE_TYPE_CLASS = "Class"
CODE_TYPE_STUB = "Code Stub"
CODE_TYPE_METHOD = "Method"

# Default placeholders
OPT_1 = "Auto-generate {} based on config (Recommended)"
OPT_2 = "Write custom {} prompt"

# Class options
CLASS_OPT_1 = OPT_1.format("class")
CLASS_OPT_2 = OPT_2.format("class")
CLASS_PLACEHOLDER = "Write your prompt here\nEg: Write a program to create a Vehicle class with max_speed and mileage instance attributes."

# Function options
FUN_OPT_1 = OPT_1.format("function")
FUN_OPT_2 = OPT_2.format("function")
FUN_PLACEHOLDER = "Write your prompt here\nEg: Write a function find_max to find the max of two numbers."

# Code stub options
STUB_OPT_1 = OPT_1.format("code stub")
STUB_OPT_2 = OPT_2.format("code stub")
STUB_PLACEHOLDER = "Write your prompt here\nEg: Write a Code stub program to find the max of two numbers."

# GPT-3 models
MODEL_OPT_1 = "gpt-3.5-turbo (recommended)"
MODEL_OPT_2 = "text-davinci-003"
MODEL_OPT_3 = "gpt-4 (coming soon)"
