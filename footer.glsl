void main( void ) {
    vec2  uv = gl_FragCoord.xy / resolution.xy;
    if(direction == 1.0){progress = 1.0 - t;}
    else{progress = t;}

    gl_FragColor = transition(uv);
}

