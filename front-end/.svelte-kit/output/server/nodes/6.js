import * as universal from '../entries/pages/dashboard/decks/_id_/_page.js';

export const index = 6;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/dashboard/decks/_id_/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/dashboard/decks/[id]/+page.js";
export const imports = ["_app/immutable/nodes/6.BxIR9_fL.js","_app/immutable/chunks/scheduler.BxOO2Wxk.js","_app/immutable/chunks/index.dKgiUWrV.js","_app/immutable/chunks/entry._9W_0XD-.js","_app/immutable/chunks/index.CmgL7U1m.js","_app/immutable/chunks/SvelteMarkdown.Bj8nW6U6.js","_app/immutable/chunks/marked.esm.ubRjD-Zf.js","_app/immutable/chunks/spread.CgU5AtxT.js","_app/immutable/chunks/Pencil.BLAlQsXI.js"];
export const stylesheets = [];
export const fonts = [];
