import { c as create_ssr_component, i as add_attribute, v as validate_component } from "../../../chunks/ssr.js";
import "../../../chunks/client.js";
/* empty css                                                      */
import { N as NavBar } from "../../../chunks/NavBar.js";
const Login = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let email = "";
  let password = "";
  return `<main><div class="container-fluid align-content-center "><div class="row"><div class="col-md-4"></div> <div class="col-md-4"><h1 data-svelte-h="svelte-1zuaex">Login</h1> <form><div class="mb-3"><label for="exampleInputEmail1" class="form-label" data-svelte-h="svelte-owkedn">Email address</label> <input style="color: black;" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"${add_attribute("value", email, 0)}></div> <div class="mb-3"><label for="exampleInputPassword1" class="form-label" data-svelte-h="svelte-15mf3ip">Password</label> <input style="color: black;" type="password" class="form-control" id="exampleInputPassword1"${add_attribute("value", password, 0)}></div> <div class="mb-3 form-check" data-svelte-h="svelte-16bhjha"><input type="checkbox" class="form-check-input" id="exampleCheck1"> <label class="form-check-label" for="exampleCheck1">Check me out</label></div> <button type="submit" class="btn btn-primary" data-svelte-h="svelte-kscvqj">Submit</button></form></div> <div class="col-md-4"></div></div></div></main>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${validate_component(NavBar, "NavBar").$$render($$result, {}, {}, {})} <div class="container">${validate_component(Login, "Login").$$render($$result, {}, {}, {})}</div>`;
});
export {
  Page as default
};
