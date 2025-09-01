from django.core.management.base import BaseCommand
from drf_spectacular.generators import SchemaGenerator

class Command(BaseCommand):
    help = "List all views included in drf-spectacular's schema"

    def handle(self, *args, **options):
        generator = SchemaGenerator()
        generator.get_schema(request=None, public=True)

        endpoints = getattr(generator, "endpoints", [])

        if isinstance(endpoints, dict):
            for path, path_endpoints in endpoints.items():
                for method, view in path_endpoints:
                    self._print_endpoint(path, method, view)

        elif isinstance(endpoints, list):
            for path, path_endpoints in endpoints:
                for method, view in path_endpoints:
                    self._print_endpoint(path, method, view)

        else:
            self.stdout.write(f"⚠️ Unexpected endpoints type: {type(endpoints)}")

    def _print_endpoint(self, path, method, view):
        view_name = view.__class__.__name__
        mark = "❌" if "Spectacular" in view_name else "✅"
        self.stdout.write(f"{mark} {path} [{method}] -> {view_name}")
