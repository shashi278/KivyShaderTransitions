//https://www.shadertoy.com/view/Ml3XR2

// inspired by shader from VoidChicken
// https://www.shadertoy.com/view/XtdXR2
// ... and portal of course ;)

// 1 .. 3
#define TRANSITION_TYPE 1

vec2 plane(vec3 p, vec3 d, vec3 normal)
{
    vec3 up = vec3(0,1,0);
    vec3 right = cross(up, normal);
    
    float dn = dot(d, normal);
    float pn = dot(p, normal);
    
    vec3 hit = p - d / dn * pn;
    
    vec2 uv;
    uv.x = dot(hit, right);
    uv.y = dot(hit, up);
    
    return uv;
}

vec4 transition(vec2 xy)
{
    float grid_width = 64.0;
    xy /= grid_width;
    vec2 grid = floor(xy);
    xy = mod(xy, 1.0) - 0.5;
    
    float alpha = 0.0;//iMouse.x / resolution.x;
    float offset = (grid.y - grid.x)*0.1;
    float time = progress - offset/2.0;
#if TRANSITION_TYPE == 1
    // looping + wrapping
    time = mod(time, 6.0);
#elif TRANSITION_TYPE == 2
    // flip once
    time = clamp(time - 1., 0., 1.);
#elif TRANSITION_TYPE == 3
    // flip and return once
#endif
    alpha += smoothstep(0.0, 1.0, time);
    alpha += 1.0 - smoothstep(3.0, 4.0, time);
    alpha = abs(mod(alpha, 2.0)-1.0);
    
    float side = step(0.5, alpha);
    
    alpha = radians(alpha*180.0);
    vec4 n = vec4(cos(alpha),0,sin(alpha),-sin(alpha));
    vec3 d = vec3(1.0,xy.y,xy.x);
    vec3 p = vec3(-1.0+n.w/4.0,0,0);
    vec2 uv = plane(p, d, n.xyz);
    
    uv += 0.5;
    if (uv.x<0.0||uv.y<0.0||uv.x>1.0||uv.y>1.0)
    {
        return gl_FragColor*0.0;
    }
    
    vec2 guv = grid*grid_width/resolution.xy+0.5;
    vec2 scale = vec2(grid_width)/resolution.xy;
    vec4 c1;
    if(direction == 2.0){c1 = texture2D(tex_in, guv + vec2(1.0-uv.x,uv.y)*scale);}
    else{c1 = texture2D(tex_out, guv + vec2(1.0-uv.x,uv.y)*scale);}
    
    vec4 c2;
    if(direction == 2.0){c2 = texture2D(tex_out, guv + vec2(uv.x,uv.y)*scale);}
    else{c2 = texture2D(tex_in, guv + vec2(uv.x,uv.y)*scale);}
    
    return mix(c1, c2, side);
}