#define pi 3.14159265359
#define radius .1
float aspect_ratio = resolution.x / resolution.y;

float map(float value)
{
    float low_map_from = 0., high_map_from = 1., low_map_to = 0.075, high_map_to = -1.15;
    return low_map_to + (value - low_map_from) * (high_map_to - low_map_to) / (high_map_from - low_map_from);
}
vec4 transition (vec2 uv) {

    vec2 dir = vec2(0.5,-1.0);
    vec2 origin = vec2(.2,0.0);
    
    float move = map(progress);
    vec4 final_tex;
    
    float proj = dot(uv - origin, dir);
    float dist = proj - move ;
    
    vec2 linePoint = uv - dist * dir ;
    
    if (dist > radius) 
    {
        
        final_tex = getToColor(uv);
        final_tex.rgb *= pow(clamp(dist - radius, 0., 1.) * 1.5, .2);


    }
    else if (dist >= 0.)
    {
        float theta = asin(dist / radius);
        vec2 p2 = linePoint + dir * (pi - theta) * radius;
        vec2 p1 = linePoint + dir * theta * radius;
        uv = (p2.x <= aspect_ratio && p2.y <= 1. && p2.x > 0. && p2.y > 0.) ? p2 : p1;
        
        final_tex = getFromColor(uv);
        final_tex.rgb *= pow(clamp((radius - dist) / radius, 0., 1.), .2);
    }
    else 
    {
        vec2 p = linePoint + dir * (abs(dist) + pi * radius) ;
        uv = (p.x <= aspect_ratio && p.y <= 1. && p.x > 0. && p.y > 0.) ? p : uv;
        
        final_tex = getFromColor(uv);
    }
    
    return final_tex;
}