// Author: gre
// License: MIT

uniform sampler2D luma;

vec4 transition(vec2 uv) {
  return mix(
    getToColor(uv),
    getFromColor(uv),
    step(progress, mix( texture2D(tex_out, uv), texture2D(tex_in, uv), 0.0).r)
  );
}
