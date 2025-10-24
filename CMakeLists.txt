cmake_minimum_required(VERSION 3.20)
project(VKB-Engine)

# Set policy to handle older CMake requirements
set(CMAKE_POLICY_DEFAULT_CMP0077 NEW)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(Vulkan REQUIRED)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/deps/src)

# Add subdirectories for dependencies
add_subdirectory(deps/src/glm)
add_subdirectory(deps/src/glfw)
add_subdirectory(deps/src/vk-bootstrap)

# Create executable
add_executable(${PROJECT_NAME} src/main.cpp)

# Define platform-specific macros for GLFW Vulkan support
if(APPLE)
    target_compile_definitions(${PROJECT_NAME} PRIVATE VK_USE_PLATFORM_METAL_EXT)
elseif(UNIX)
    target_compile_definitions(${PROJECT_NAME} PRIVATE VK_USE_PLATFORM_XLIB_KHR)
elseif(WIN32)
    target_compile_definitions(${PROJECT_NAME} PRIVATE VK_USE_PLATFORM_WIN32_KHR)
endif()

# Add GLM include directory
target_include_directories(${PROJECT_NAME} PRIVATE deps/src/glm)

# cgltf is header-only, just add include path
target_include_directories(${PROJECT_NAME} PRIVATE deps/src/cgltf)

# Link libraries
target_link_libraries(${PROJECT_NAME} 
    Vulkan::Vulkan
    glfw
    vk-bootstrap
    glm
)

# Set C++ standard for the target
set_target_properties(${PROJECT_NAME} PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
)

# Copy shaders to build directory
file(COPY shaders DESTINATION ${CMAKE_BINARY_DIR})

# Compile shaders
find_program(GLSL_VALIDATOR glslangValidator)
if(GLSL_VALIDATOR)
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/shaders/triangle.vert.spv
        COMMAND ${GLSL_VALIDATOR} -V ${CMAKE_SOURCE_DIR}/shaders/triangle.vert -o ${CMAKE_BINARY_DIR}/shaders/triangle.vert.spv
        DEPENDS ${CMAKE_SOURCE_DIR}/shaders/triangle.vert
        COMMENT "Compiling triangle vertex shader"
    )
    
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/shaders/triangle.frag.spv
        COMMAND ${GLSL_VALIDATOR} -V ${CMAKE_SOURCE_DIR}/shaders/triangle.frag -o ${CMAKE_BINARY_DIR}/shaders/triangle.frag.spv
        DEPENDS ${CMAKE_SOURCE_DIR}/shaders/triangle.frag
        COMMENT "Compiling triangle fragment shader"
    )
    
    add_custom_target(compile_shaders DEPENDS 
        ${CMAKE_BINARY_DIR}/shaders/triangle.vert.spv
        ${CMAKE_BINARY_DIR}/shaders/triangle.frag.spv
    )
    
    add_dependencies(${PROJECT_NAME} compile_shaders)
else()
    message(WARNING "glslangValidator not found, shaders will not be compiled")
endif()

# Set output directory
set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
)