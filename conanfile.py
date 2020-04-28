from conans import ConanFile, MSBuild

class LibGizmoConan(ConanFile):
    name = "LibGizmo"
    version = "0.1"
    description = """LibGizmo"""
    generators = "visual_studio"
    requires = []

    def source(self):
        self.run("git clone https://github.com/Murazaki/LibGizmo.git libgizmo")

    def build(self):
        msbuild = MSBuild(self)
        msbuild.build("libgizmo/src/LibGizmo.sln", build_type="Release", arch="x64")
        msbuild.build("libgizmo/src/LibGizmo.sln", build_type="Debug", arch="x64")