
cmake_minimum_required(VERSION 3.0.0)
set(PROJECT "minimal")

project(${PROJECT} CXX)

if(NOT DEFINED EMSCRIPTEN)
    include("${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake")
    conan_basic_setup()
endif()

message("Project ${PROJECT}")
message(" - CC: ${CC}")
message(" - CXX: ${CXX}")
message(" - TOOLCHAIN: ${CMAKE_TOOLCHAIN_FILE}")
message(" - EMSCRIPTEN: ${EMSCRIPTEN}")
message(" - WASM: ${WASM}")


set(SOURCES 
        "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp"
    )
message("${SOURCES}")

add_executable(${PROJECT} ${SOURCES})
