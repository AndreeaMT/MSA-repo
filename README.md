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
 

running Angular project:
    ng serve --open
or simply:
    ng serve
    
Angular project at: 
    http://localhost:4200/