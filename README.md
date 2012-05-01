cvex
====

computer vision exercises

* setting up environment - ubuntu
    
    sudo apt-get install libopencv-dev

* compile example with:
    
    g++ -Wall -g -o cvex cvex.cpp -lopencv_highgui -lopencv_core

* run with

    ./cvex <some_picture>
