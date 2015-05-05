cmake_minimum_required(VERSION 2.8.3)
project(rapp_knowrob_wrapper)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  json_prolog
  rostest 
  rapp_platform_ros_communications
  message_generation
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  CATKIN_DEPENDS
    roscpp
    json_prolog
    rapp_platform_ros_communications
  INCLUDE_DIRS
    include
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}  
)

###########
## Build ##
###########
# Library for unit testing
add_library(knowrob_connector_lib
  src/knowrob_wrapper.cpp
  )
target_link_libraries(knowrob_connector_lib
  ${catkin_LIBRARIES}
  )
add_dependencies(knowrob_connector_lib
  rapp_platform_ros_communications_gencpp
  ${catkin_EXPORTED_TARGETS}
  )

# RIS executable
add_executable(knowrob_wrapper_node
  src/knowrob_wrapper_node.cpp
  src/knowrob_wrapper_communications.cpp
  )
target_link_libraries(knowrob_wrapper_node
  knowrob_connector_lib
  ${catkin_LIBRARIES}
  )
add_dependencies(knowrob_wrapper_node
  rapp_platform_ros_communications_gencpp
  ${catkin_EXPORTED_TARGETS}
  )