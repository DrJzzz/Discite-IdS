import { c as create_ssr_component, i as add_attribute, a as subscribe, v as validate_component, j as each, e as escape } from "../../../../chunks/ssr.js";
import { w as writable } from "../../../../chunks/index.js";
import "marked";
import "../../../../chunks/client.js";
import { P as Plus } from "../../../../chunks/Plus.js";
let CardStore = writable([]);
let DeckStore = writable([]);
const NewCard = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let decks = [];
  async function getDecks() {
    try {
      const response = await fetch("http://127.0.0.1:8000/users/1/decks/", {
        method: "GET",
        headers: { "Content-Type": "application/json" }
      });
      if (response.ok) {
        decks = await response.json();
      } else {
        console.error("Failed decks");
      }
    } catch (error) {
      console.error("An error occurred while getting decks: ", error);
    }
  }
  getDecks();
  return `<div><div class="modal-header" data-svelte-h="svelte-1ikk5ng"><h5 class="modal-title" id="exampleModalLabel">Add card</h5></div> <form><div class="modal-body"><div class="mb-3"><label for="front-area" class="form-label" data-svelte-h="svelte-jndamv">Template</label> <select class="form-select" style="color:black" aria-label="Select template"><option value="" disabled selected data-svelte-h="svelte-tv2fe6">Open to select template</option><option value="1" data-svelte-h="svelte-190bggj">Basic</option></select></div> ${``} ${``}</div> <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal" data-svelte-h="svelte-1f0lmv">Cancel</button> ${``}</div></form></div>`;
});
const NewDeck = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let name = "";
  return `<div><div class="modal-header" data-svelte-h="svelte-av1xwb"><h5 class="modal-title" id="exampleModalLabel">Add deck</h5></div> <form><div class="modal-body"><div class="form-floating mb-3"><input type="text" class="form-control" id="floatingInput" placeholder="name" style="color:black"${add_attribute("value", name, 0)}> <label for="floatingInput" style="color:black" data-svelte-h="svelte-125df89">Name</label></div></div> <div class="modal-footer" data-svelte-h="svelte-12doy0k"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button> <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button></div></form></div>`;
});
const css = {
  code: ".card-view.svelte-1ab66qd{cursor:pointer}",
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $CardStore, $$unsubscribe_CardStore;
  let $$unsubscribe_DeckStore;
  let $isMounted, $$unsubscribe_isMounted;
  $$unsubscribe_CardStore = subscribe(CardStore, (value) => $CardStore = value);
  $$unsubscribe_DeckStore = subscribe(DeckStore, (value) => value);
  let isMounted = writable(false);
  $$unsubscribe_isMounted = subscribe(isMounted, (value) => $isMounted = value);
  $$result.css.add(css);
  $$unsubscribe_CardStore();
  $$unsubscribe_DeckStore();
  $$unsubscribe_isMounted();
  return `<div> <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal"><div class="d-flex align-items-center">${validate_component(Plus, "Plus").$$render($$result, {}, {}, {})}
            Add card</div></button>  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#deckModal"><div class="d-flex align-items-center">${validate_component(Plus, "Plus").$$render($$result, {}, {}, {})}
            Add deck</div></button> ${$isMounted ? `<div class="accordion" id="accordionPanelsStayOpenExample">${each($CardStore, (data) => {
    return `<div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="${"#panelsStayOpen-collapse" + escape(data.deck.id, true)}" aria-expanded="true" aria-controls="${"panelsStayOpen-collapse" + escape(data.deck.id, true)}">${escape(data.deck.name)} </button></h2> <div id="${"panelsStayOpen-collapse" + escape(data.deck.id, true)}" class="accordion-collapse collapse"><div class="accordion-body"><div class="list-group">${each(data.cards, (card) => {
      return `<a class="list-group-item list-group-item-action active card-view svelte-1ab66qd" aria-current="true"><div class="d-flex w-100 justify-content-between"> <p>Card ${escape(card.id)}</p></div> </a>`;
    })}</div> </div></div> </div>`;
  })}</div>` : `<div data-svelte-h="svelte-1ln7ra0"><h3>Cargando..</h3></div>`}  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content">${validate_component(NewCard, "NewCard").$$render($$result, {}, {}, {})}</div></div></div> <div class="modal fade" id="deckModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content">${validate_component(NewDeck, "NewDeck").$$render($$result, {}, {}, {})}</div></div></div></div>`;
});
export {
  Page as default
};
