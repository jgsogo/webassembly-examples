from conans import ConanFile, CMake

class MandelbrotExample(ConanFile):
    name = "mandelbrot"
    version = "0.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("index.html", src="resources", dst="html")
        self.copy("*.js", dst="html", keep_path=False)
        self.copy("*.wasm", dst="html")
