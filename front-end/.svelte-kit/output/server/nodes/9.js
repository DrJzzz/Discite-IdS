

export const index = 9;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/dashboard/settings/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/9.o8EPRo2y.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js"];
export const stylesheets = [];
export const fonts = [];
