import { c as create_ssr_component, a as subscribe, e as escape } from "../../../../../chunks/ssr.js";
import { N as NoteStore } from "../../../../../chunks/note-store.js";
import "marked";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $$unsubscribe_NoteStore;
  $$unsubscribe_NoteStore = subscribe(NoteStore, (value) => value);
  let { data } = $$props;
  if ($$props.data === void 0 && $$bindings.data && data !== void 0)
    $$bindings.data(data);
  $$unsubscribe_NoteStore();
  return `${`<h2>No se encontro la nota con id: ${escape(data.id)}</h2>`}`;
});
export {
  Page as default
};
