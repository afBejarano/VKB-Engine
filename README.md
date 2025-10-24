# VKB-Engine

A minimal Vulkan engine demonstrating triangle rendering with Vulkan 1.3 dynamic rendering.

## Features

- **Vulkan 1.3** with dynamic rendering extensions
- **vk-bootstrap** for simplified Vulkan initialization
- **GLFW** for window management
- **GLM** for mathematical operations
- **cgltf** for model loading capability
- **Triangle rendering** with colorful vertices
- **Cross-platform** support (tested on macOS)

## Dependencies

- **vk-bootstrap**: Vulkan initialization and management
- **GLM**: OpenGL Mathematics library
- **GLFW**: Window management and input handling
- **cgltf**: glTF 2.0 model loading

## Requirements

- CMake 3.20+
- C++17 compatible compiler
- Vulkan SDK
- Python 3 (for dependency management)
- Git (for dependency cloning)

## Setup

1. **Bootstrap dependencies**:
   ```bash
   cd deps
   python3 bootstrap.py
   ```

2. **Create build directory**:
   ```bash
   mkdir build
   cd build
   ```

3. **Configure with CMake**:
   ```bash
   cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5
   ```

4. **Build the project**:
   ```bash
   ninja
   ```

5. **Run the application**:
   ```bash
   ./VKB-Engine
   ```

## Project Structure

```
VKB-Engine/
├── deps/
│   ├── bootstrap.json      # Dependency configuration
│   ├── bootstrap.py       # Dependency management script
│   └── src/               # Downloaded dependencies
├── src/
│   └── main.cpp           # Main triangle renderer
├── shaders/
│   ├── triangle.vert      # Vertex shader
│   └── triangle.frag      # Fragment shader
├── CMakeLists.txt         # CMake configuration
└── README.md              # This file
```

## What You'll See

When you run the application, you'll see a window with a colorful triangle:
- **Red vertex** at the bottom
- **Green vertex** at the top right
- **Blue vertex** at the top left
- **Black background**

The triangle is rendered using Vulkan 1.3 dynamic rendering with proper synchronization and command buffer management.

## Controls

- **ESC** or **Close window** to exit

## License

This project is open source and available under the MIT License.