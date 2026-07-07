import os
#Librerias para laucn con ros2
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node, SetRemap #Remap para cambiar en los nodos el topic de entrada
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_nav2 = get_package_share_directory('nav2_bringup') #Traemos el directorio de Nav2
    pkg_pmb2 = get_package_share_directory('pmb2_nav') #Traemos el directorio del paquete actual

    # Archivos
    params_file = os.path.join(pkg_pmb2, 'config', 'nav2_params.yaml') #Incluimos el fichero de configuración de Nav2
    map_file = os.path.join(pkg_pmb2, 'maps', 'mapapasillo.yaml')#Incluimos el mapa que debe de configurarse al cambiar el mapa
    rviz_config = os.path.join(pkg_pmb2, 'rviz', '/home/sergio/.rviz2/nav2_config.rviz') #Incluimos el fichero de configuración de RViZ2 para Nav2 hecho en este TFM

    # NAV2
    #Esta parte se encarga de lanzar a Nav2
    nav2_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_file,
            'params_file': params_file,
            'use_sim_time': 'false', #Cambiado
            'autostart': 'true'
        }.items()
    )

    # Remapeos PMB2
    remap_nav2 = GroupAction(
        actions=[
            SetRemap(src='/cmd_vel', dst='/nav_vel'),
            SetRemap(src='/odom', dst='/mobile_base_controller/odom'), 
            nav2_bringup
        ]
    )
    # Se puede lanazar RViz 2 desde un launch
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    return LaunchDescription([
        remap_nav2,
        #rviz
    ])