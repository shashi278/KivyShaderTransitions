
$HEADER$

uniform float t;
uniform float direction;

uniform vec2 resolution;
uniform sampler2D tex_in;
uniform sampler2D tex_out;

float progress;

vec4 getToColor(vec2 p){
    if(direction == 2.0){return texture2D(tex_in, p);}
    else{return texture2D(tex_out, p);}
}

vec4 getFromColor(vec2 p){
    if(direction == 2.0){return texture2D(tex_out, p);}
    else{return texture2D(tex_in, p);}
    
}

