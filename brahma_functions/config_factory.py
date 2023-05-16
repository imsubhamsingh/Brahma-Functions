from abc import ABC, abstractmethod


class BaseConfig(ABC):
    """
    This is an abstract class that is used to generate config for any language.
    """

    config = {}

    @abstractmethod
    def generate_config(self, **kwargs):
        """
        This function is used to generate config for any language.
        """
        raise NotImplementedError


class PythonConfig(BaseConfig):
    """
    This class is used to generate Python config.
    """

    config = {}

    def generate_config(self, **kwargs):
        self.config["func_name"] = kwargs.get("func_name")
        self.config["func_args"] = kwargs.get("func_args")
        self.config["func_docstring"] = kwargs.get("func_docstring")
        self.config["return_type"] = kwargs.get("return_type")

        return self.config

    def get_config(self):
        return self.config

    def set_config(self, config):
        self.config = config


class JavaScriptConfig(BaseConfig):
    pass
