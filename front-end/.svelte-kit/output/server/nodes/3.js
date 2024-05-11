

export const index = 3;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/3.DZpBNgA5.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js","_app/immutable/chunks/NavBar.8RlMtNKe.js"];
export const stylesheets = ["_app/immutable/assets/3.BGYUmmmQ.css","_app/immutable/assets/Footer.CPYke1nY.css"];
export const fonts = [];
