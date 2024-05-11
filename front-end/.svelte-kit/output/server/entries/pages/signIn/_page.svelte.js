import { c as create_ssr_component, i as add_attribute, v as validate_component } from "../../../chunks/ssr.js";
import "../../../chunks/client.js";
/* empty css                                                      */
import { N as NavBar } from "../../../chunks/NavBar.js";
const css = {
  code: "main.svelte-21yu4y{max-width:400px;margin:0 auto;padding:2rem}",
  map: null
};
const Registro = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let name = "";
  let email = "";
  let password1 = "";
  let password2 = "";
  let phone_number = "";
  let birthdate = "";
  $$result.css.add(css);
  return `<main class="svelte-21yu4y"><h1 class="" data-svelte-h="svelte-oqi9ef">Sign in</h1> <form><div class="mb-3"><label for="name" class="form-label" data-svelte-h="svelte-17mpp60">Name</label> <input style="color: black;" type="text" class="form-control" id="name"${add_attribute("value", name, 0)}></div> <div class="mb-3"><label for="exampleInputEmail1" class="form-label" data-svelte-h="svelte-owkedn">Email address</label> <input style="color: black;" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"${add_attribute("value", email, 0)}></div> <div class="mb-3"><label for="phoneNumber" class="form-label" data-svelte-h="svelte-1hjoij8">Phone Number</label> <input style="color: black;" type="tel" class="form-control" id="phoneNumber" placeholder="Enter your phone number"${add_attribute("value", phone_number, 0)}></div> <div class="mb-3"><label for="dob" class="form-label" data-svelte-h="svelte-1a8z2i2">Birthdate</label> <input style="color: black;" type="date" class="form-control" id="dob"${add_attribute("value", birthdate, 0)}></div> <div class="mb-3"><label for="exampleInputPassword1" class="form-label" data-svelte-h="svelte-15mf3ip">Password</label> <input style="color: black;" type="password" class="form-control" id="exampleInputPassword1"${add_attribute("value", password1, 0)}></div> <div class="mb-3"><label for="exampleInputPassword2" class="form-label" data-svelte-h="svelte-1tqtrta">Confirm Password</label> <input style="color: black;" type="password" class="form-control" id="exampleInputPassword2"${add_attribute("value", password2, 0)}></div> <button class="btn btn-primary" type="submit" data-svelte-h="svelte-9ceaob">Sign in</button></form> </main>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${validate_component(NavBar, "NavBar").$$render($$result, {}, {}, {})} <div class="mx-auto">${validate_component(Registro, "Registro").$$render($$result, {}, {}, {})}</div>`;
});
export {
  Page as default
};
