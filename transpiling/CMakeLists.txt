
cmake_minimum_required(VERSION 3.0.0)
set(PROJECT "transpiling")

project(${PROJECT} CXX)

set(SOURCES 
        "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp"
    )
message("${SOURCES}")

add_executable(${PROJECT} ${SOURCES})
