#!/bin/bash

# VKB-Engine Build Script

echo "Building VKB-Engine..."

# Check if dependencies are bootstrapped
if [ ! -d "deps/src" ]; then
    echo "Dependencies not found. Running bootstrap..."
    cd deps
    python3 bootstrap.py
    cd ..
fi

# Create build directory if it doesn't exist
if [ ! -d "build" ]; then
    mkdir build
fi

cd build

# Configure with CMake
echo "Configuring with CMake..."
cmake ..

# Build the project
echo "Building project..."
make -j$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)

echo "Build complete!"
echo "Run './VKB-Engine' to start the application."
