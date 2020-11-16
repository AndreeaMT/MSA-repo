# Parasites' Map
project for Mobile Systems Applications laboratory, 4th year of Uni

for Mapbox installation:
npm install mapbox-gl --save
npm install @types/mapbox-gl --save

put in the header of index.html:
  <script src='https://api.mapbox.com/mapbox-gl-js/v1.0.0/mapbox-gl.js'></script>
  <link href='https://api.mapbox.com/mapbox-gl-js/v1.0.0/mapbox-gl.css' rel='stylesheet' />
  
in environment.ts:
firebaseConfig: {
    //your firebase config
  },

  mapbox: {
    accessToken: 'pk.eyJ1IjoiYW5kcmVlYWFuZHJlZXNjdSIsImEiOiJja2dxbHpkOHgwNWlmMnJtZnZhOTkxbmVjIn0.tj__Y5aYxguOzCoGh-UR3A'
  }

    
for django installation:
    https://www.django-rest-framework.org/tutorial/quickstart/
    https://youtu.be/z_H-oxQVsPw
  
* * * * * * * * * * * * * * * * * * * * * * * * * * * *
Running Angular: ng serve
                 server listening: http://localhost:4200/
        django: python manage.py runserver
                 server listening: http://127.0.0.1:8000/
* * * * * * * * * * * * * * * * * * * * * * * * * * * *   

installing django cores:
    pip install django-cors-headers              
                 