
cmake_minimum_required(VERSION 3.0.0)
set(PROJECT "transpiling")

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

set(SOURCES 
        "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp"
    )
message("${SOURCES}")

add_executable(${PROJECT} ${SOURCES})
add_executable(${PROJECT}.html ${SOURCES})
