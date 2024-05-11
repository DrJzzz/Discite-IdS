import { c as create_ssr_component, v as validate_component } from "../../chunks/ssr.js";
/* empty css                                                */
const css = {
  code: "#footer.svelte-1nq110o.svelte-1nq110o{background-color:#333;padding:2rem 0;display:flex;flex-wrap:wrap;justify-content:space-around;align-items:flex-start}#footer.svelte-1nq110o section.svelte-1nq110o{margin:1rem}.about.svelte-1nq110o.svelte-1nq110o{color:aliceblue;flex-grow:1}.about.svelte-1nq110o .h5.svelte-1nq110o{color:aliceblue;font-size:1.25rem;margin-bottom:0.5rem}.about.svelte-1nq110o div.svelte-1nq110o{margin-bottom:0.25rem}.copyright.svelte-1nq110o.svelte-1nq110o{font-size:0.875rem;color:#6a747c}",
  map: null
};
const Footer = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  (/* @__PURE__ */ new Date()).getFullYear();
  $$result.css.add(css);
  return `<div id="footer" class="svelte-1nq110o" data-svelte-h="svelte-1h8519m"><section class="svelte-1nq110o"><img src="images/favicon.png" width="40" height="40" alt="Mochi logo"></section> <section class="about svelte-1nq110o"><span class="h5 svelte-1nq110o">AnkiCards</span> <div class="svelte-1nq110o">Anki Cards la mejor opción para aprender</div> <div class="copyright svelte-1nq110o">© <span id="current-year">2024</span> Anki Cards, Inc</div></section> <section class="footer-links svelte-1nq110o"></section> <section class="footer-links svelte-1nq110o"></section></div>`;
});
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${slots.default ? slots.default({}) : ``} ${validate_component(Footer, "Footer").$$render($$result, {}, {}, {})}`;
});
export {
  Layout as default
};
