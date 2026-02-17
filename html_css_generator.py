from abc import ABC, abstractmethod
import logging
from typing import Dict, Any
from jinja2 import Environment, Template

# Constants for template loading
TEMPLATE_PATH = "templates/"
DEFAULT_TEMPLATE_NAME = "default.html"

class HTMLCSSGenerator(ABC):
    """Abstract Base Class for generating and optimizing web components.
    
    This class provides the foundation for creating web components with 
    optimized conversion elements. It uses Jinja2 templating for dynamic content.
    """
    
    def __init__(self, template_name: str = DEFAULT_TEMPLATE_NAME) -> None:
        self.template_name = template_name
        self.environment = Environment(loader=self._get_template_loader())
        
    @staticmethod
    def _get_template_loader() -> Environment:
        """Load templates from the specified directory.
        
        Returns:
            Jinja2 Environment with loaded templates.
        """
        try:
            return Environment(loader=FileSystemLoader(TEMPLATE_PATH))
        except Exception as e:
            logging.error(f"Failed to load templates: {e}")
            raise FileNotFoundError("Template directory not found.")
    
    @abstractmethod
    def generate(self, data: Dict[str, Any]) -> str:
        """Generate HTML/CSS content based on input data.
        
        Args:
            data: Dictionary containing template variables.
            
        Returns:
            Generated HTML string with embedded CSS.
        """
        pass
    
class LandingPageGenerator(HTMLCSSGenerator):
    """Specialized generator for landing pages."""
    
    def __init__(self) -> None:
        super().__init__("landing_page.html")
        
    def generate(self, data: Dict[str, Any]) -> str:
        """Generate a personalized landing page.
        
        Args:
            data: Includes user demographics and behavior info.
            
        Returns:
            Optimized HTML/CSS string for the landing page.
        """
        try:
            template = self.environment.get_template(self.template_name)
            return template.render(data)
        except TemplateNotFound as e:
            logging.error(f"Template not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error during rendering: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    try:
        generator = LandingPageGenerator()
        data = {"user_id": "123", "product_name": "AI Suite Pro"}
        html_content = generator.generate(data)
        print(html_content)
    except Exception as e:
        logging.error(f"Main execution failed: {e}")