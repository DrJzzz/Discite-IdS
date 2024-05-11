

export const index = 4;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/dashboard/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/4.BpAgd8Np.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js"];
export const stylesheets = [];
export const fonts = [];
