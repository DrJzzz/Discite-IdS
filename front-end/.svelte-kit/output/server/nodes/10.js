

export const index = 10;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/dashboard/user/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/10.Daxru3Z-.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js"];
export const stylesheets = [];
export const fonts = [];
