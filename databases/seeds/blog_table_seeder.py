"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title":"HTML","body":"skeleton"})
        Blog.create({"title":"CSS","body":"skin"})
        Blog.create({"title":"JavaScript","body":"functions"})
