Vim�UnDo� �Z�ʍ��u�0�I8��m� ��5\���jI
]      $    path('', include("users.urls")),      
                       e�P   	 _�                             ����                                                                                                                                                                                                                                                                                                                                                V       e�    �                 """   #URL configuration for todo project.       MThe `urlpatterns` list routes URLs to views. For more information please see:   ;    https://docs.djangoproject.com/en/5.0/topics/http/urls/   	Examples:   Function views   /    1. Add an import:  from my_app import views   C    2. Add a URL to urlpatterns:  path('', views.home, name='home')   Class-based views   7    1. Add an import:  from other_app.views import Home   G    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')   Including another URLconf   K    1. Import the include() function: from django.urls import include, path   E    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))   """5��                                   �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       e�     �             �             5��                          t               %       5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                V       e�     �               $    path('admin/', admin.site.urls),5��       
                 ~                     �       
                 ~                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                         !       v   !    e�%     �               $    path('login/', admin.site.urls),�               from django.urls import path5��                        �                     �                        �                     �                        �                     �                        �                     �                        �                     �                      	   9               	       �                        �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                         !       v   !    e�)     �                   path('login/', include),5��                         �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                         !       v   !    e�)     �                   path('login/', include()),5��                         �                      �                         �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                         !       v   !    e�+     �                   path('login/', include()),5��                         �                      5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                         !       v   !    e�,    �                    path('login/', include("")),5��                      
   �               
       5�_�      
           	      
    ����                                                                                                                                                                                                                                                                                                                                         
       v   
    e�@    �               *    path('login/', include("users.urls")),5��       
                  �                      5�_�   	              
      
    ����                                                                                                                                                                                                                                                                                                                                         
       v   
    e���     �             �             5��                          �               %       5�_�   
                    
    ����                                                                                                                                                                                                                                                                                                                                         
       v   
    e���    �               $    path('', include("users.urls")),5��       
                  �                      �       
                 �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       e���    �               (    path('api/', include("users.urls")),5��                        �                     �                     	   �              	       �              	       	   �       	       	       �              	          �       	              �                     	   �              	       �       !                 �                     �       "                  �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e��    �               *    path('api/', include("todoAPI.urls")),5��                         �                      �                        �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e��    �               -    path('api/v1/', include("todoAPI.urls")),5��                         �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       e�O   	 �               /    path('api/v1.0/', include("todoAPI.urls")),5��                         �                      5��