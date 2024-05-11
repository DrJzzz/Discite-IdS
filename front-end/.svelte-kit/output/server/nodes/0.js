

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_layout.svelte.js')).default;
export const imports = ["_app/immutable/nodes/0.Caq-3FH0.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js"];
export const stylesheets = ["_app/immutable/assets/0.-FI2vkne.css","_app/immutable/assets/Footer.CPYke1nY.css"];
export const fonts = [];
