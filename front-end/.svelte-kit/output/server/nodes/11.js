

export const index = 11;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/landing/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/11.56G6Osks.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js"];
export const stylesheets = ["_app/immutable/assets/3.BGYUmmmQ.css"];
export const fonts = [];
