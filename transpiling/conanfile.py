from conans import ConanFile, CMake

class TranspilingExample(ConanFile):
    name = "transpiling"
    version = "0.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("index.html")
        self.copy("*.js")
        self.copy("*.wasm")
