# language to extension mapping
LANG_C = "C"
LANG_CPP = "C++"
LANG_CPP11 = "C++11"
LANG_CPP14 = "C++14"
LANG_CPP17 = "C++17"
LANG_CSHARP = "C#"
LANG_GO = "GO"
LANG_JAVA = "JAVA"
LANG_JAVA8 = "JAVA8"
LANG_JAVA14 = "JAVA14"
LANG_JAVASCRIPT = "JAVASCRIPT"
LANG_JAVASCRIPT_NODE = "JAVASCRIPT_NODE"
LANG_PHP = "PHP"
LANG_PYTHON = "PYTHON"
LANG_PYTHON3 = "PYTHON3"
LANG_RUBY = "RUBY"
LANG_SWIFT_4_1 = "SWIFT_4_1"
LANG_SWIFT_5_1 = "SWIFT"


LANG_TO_FILE_EXTENSION = {
    LANG_C: "c",
    LANG_CPP: "cpp",
    LANG_CPP11: "cpp11",
    LANG_CPP14: "cpp14",
    LANG_CPP17: "cpp17",
    LANG_CSHARP: "cs",
    LANG_GO: "go",
    LANG_JAVA: "java",
    LANG_JAVA8: "java8",
    LANG_JAVA14: "java14",
    LANG_JAVASCRIPT: "js",
    LANG_JAVASCRIPT_NODE: "njs",
    LANG_PHP: "php",
    LANG_PYTHON3: "py3",
    LANG_PYTHON: "py",
    LANG_RUBY: "rb",
    LANG_SWIFT_4_1: "swift",
    LANG_SWIFT_5_1: "swift",
}

LANG_TO_VERSIONS = {
    LANG_C: ["GCC 10.3", "GCC 9.3", "GCC 8.4"],
    LANG_CPP: ["C++17", "C++14", "C++11"],
    LANG_CPP11: ["C++17", "C++14", "C++11"],
    LANG_CPP14: ["C++17", "C++14", "C++11"],
    LANG_CPP17: ["C++17", "C++14", "C++11"],
    LANG_CSHARP: ["C# 9", "C# 8", "C# 7"],
    LANG_GO: ["1.15", "1.14", "1.13"],
    LANG_JAVA: ["14", "11", "8"],
    LANG_JAVA8: ["14", "11", "8"],
    LANG_JAVA14: ["14", "11", "8"],
    LANG_JAVASCRIPT: ["ES6", "ES5", "Rhino1.7", "Nodejs v18.15.0"],
    LANG_JAVASCRIPT_NODE: ["ES6", "ES5", "Rhino1.7", "Nodejs v18.15.0"],
    LANG_PHP: ["7.4", "7.3", "7.2"],
    LANG_PYTHON: ["3", "2"],
    LANG_PYTHON3: ["3", "2"],
    LANG_RUBY: ["3.0", "2.7", "2.6", "2.5"],
    LANG_SWIFT_4_1: ["4.1"],
    LANG_SWIFT_5_1: ["5.1"],
}
