import{s as oe,e as m,z as V,c as p,k as C,g as A,A as S,d as _,a as r,C as P,B as G,M as $e,i as N,m as d,N as se,D as F,E as Ve,n as W,G as ie,O as ce,v as X,w as K,F as de,P as _e,H as re,y as Se}from"../chunks/scheduler.BxOO2Wxk.js";import{S as ue,i as fe,c as Y,b as Z,m as ee,t as te,a as le,d as ae}from"../chunks/index.dKgiUWrV.js";import{e as Q}from"../chunks/marked.esm.ubRjD-Zf.js";import{w as he}from"../chunks/index.CmgL7U1m.js";import{g as xe}from"../chunks/entry._9W_0XD-.js";import{P as be}from"../chunks/Plus.OLYl-RqZ.js";let ge=he([]),ne=he([]);function ke(c,e,l){const t=c.slice();return t[12]=e[l],t}function ye(c){let e,l,t="Deck",o,s,a,u="Open to select a deck",h,T,y=Q(c[4].decks),n=[];for(let f=0;f<y.length;f+=1)n[f]=Ee(ke(c,y,f));return{c(){e=m("div"),l=m("label"),l.textContent=t,o=V(),s=m("select"),a=m("option"),a.textContent=u;for(let f=0;f<n.length;f+=1)n[f].c();this.h()},l(f){e=p(f,"DIV",{class:!0});var b=C(e);l=p(b,"LABEL",{for:!0,class:!0,"data-svelte-h":!0}),A(l)!=="svelte-1puxtmy"&&(l.textContent=t),o=S(b),s=p(b,"SELECT",{class:!0,style:!0,"aria-label":!0});var i=C(s);a=p(i,"OPTION",{"data-svelte-h":!0}),A(a)!=="svelte-1am7o1c"&&(a.textContent=u);for(let v=0;v<n.length;v+=1)n[v].l(i);i.forEach(_),b.forEach(_),this.h()},h(){r(l,"for","front-area"),r(l,"class","form-label"),a.__value="",P(a,a.__value),a.disabled=!0,a.selected=!0,r(s,"class","form-select"),G(s,"color","black"),r(s,"aria-label","Select template"),c[2]===void 0&&$e(()=>c[8].call(s)),r(e,"class","mb-3")},m(f,b){N(f,e,b),d(e,l),d(e,o),d(e,s),d(s,a);for(let i=0;i<n.length;i+=1)n[i]&&n[i].m(s,null);se(s,c[2],!0),h||(T=F(s,"change",c[8]),h=!0)},p(f,b){if(b&16){y=Q(f[4].decks);let i;for(i=0;i<y.length;i+=1){const v=ke(f,y,i);n[i]?n[i].p(v,b):(n[i]=Ee(v),n[i].c(),n[i].m(s,null))}for(;i<n.length;i+=1)n[i].d(1);n.length=y.length}b&20&&se(s,f[2])},d(f){f&&_(e),ce(n,f),h=!1,T()}}}function Ee(c){let e,l=c[12].name+"",t,o;return{c(){e=m("option"),t=X(l),this.h()},l(s){e=p(s,"OPTION",{});var a=C(e);t=K(a,l),a.forEach(_),this.h()},h(){e.__value=o=c[12].id,P(e,e.__value)},m(s,a){N(s,e,a),d(e,t)},p(s,a){a&16&&l!==(l=s[12].name+"")&&de(t,l),a&16&&o!==(o=s[12].id)&&(e.__value=o,P(e,e.__value))},d(s){s&&_(e)}}}function Ce(c){let e,l,t="Front Area",o,s,a,u,h,T="Back Area",y,n,f,b;return{c(){e=m("div"),l=m("label"),l.textContent=t,o=V(),s=m("textarea"),a=V(),u=m("div"),h=m("label"),h.textContent=T,y=V(),n=m("textarea"),this.h()},l(i){e=p(i,"DIV",{class:!0});var v=C(e);l=p(v,"LABEL",{for:!0,class:!0,"data-svelte-h":!0}),A(l)!=="svelte-10u5p2t"&&(l.textContent=t),o=S(v),s=p(v,"TEXTAREA",{style:!0,class:!0,id:!0,rows:!0,placeholder:!0}),C(s).forEach(_),v.forEach(_),a=S(i),u=p(i,"DIV",{class:!0});var g=C(u);h=p(g,"LABEL",{for:!0,class:!0,"data-svelte-h":!0}),A(h)!=="svelte-1jgnx0z"&&(h.textContent=T),y=S(g),n=p(g,"TEXTAREA",{style:!0,class:!0,id:!0,rows:!0,placeholder:!0}),C(n).forEach(_),g.forEach(_),this.h()},h(){r(l,"for","front-area"),r(l,"class","form-label"),G(s,"color","black"),r(s,"class","form-control"),r(s,"id","front-area"),r(s,"rows","5"),r(s,"placeholder","Type in Markdown"),r(e,"class","mb-3"),r(h,"for","back-area"),r(h,"class","form-label"),G(n,"color","black"),r(n,"class","form-control"),r(n,"id","back-area"),r(n,"rows","10"),r(n,"placeholder","Type in Markdown"),r(u,"class","mb-3")},m(i,v){N(i,e,v),d(e,l),d(e,o),d(e,s),P(s,c[0]),N(i,a,v),N(i,u,v),d(u,h),d(u,y),d(u,n),P(n,c[1]),f||(b=[F(s,"input",c[9]),F(n,"input",c[10])],f=!0)},p(i,v){v&1&&P(s,i[0]),v&2&&P(n,i[1])},d(i){i&&(_(e),_(a),_(u)),f=!1,ie(b)}}}function Te(c){let e,l="Save changes";return{c(){e=m("button"),e.textContent=l,this.h()},l(t){e=p(t,"BUTTON",{type:!0,class:!0,"data-bs-dismiss":!0,"data-svelte-h":!0}),A(e)!=="svelte-qs4ve2"&&(e.textContent=l),this.h()},h(){r(e,"type","submit"),r(e,"class","btn btn-primary"),r(e,"data-bs-dismiss","modal")},m(t,o){N(t,e,o)},d(t){t&&_(e)}}}function Le(c){let e,l,t='<h5 class="modal-title" id="exampleModalLabel">Add card</h5>',o,s,a,u,h,T="Template",y,n,f,b="Open to select template",i,v="Basic",g,I,k,O,$,x="Cancel",B,j,U,w=c[3]!=0&&ye(c),E=c[3]==1&&Ce(c),D=c[3]!=0&&Te();return{c(){e=m("div"),l=m("div"),l.innerHTML=t,o=V(),s=m("form"),a=m("div"),u=m("div"),h=m("label"),h.textContent=T,y=V(),n=m("select"),f=m("option"),f.textContent=b,i=m("option"),i.textContent=v,g=V(),w&&w.c(),I=V(),E&&E.c(),k=V(),O=m("div"),$=m("button"),$.textContent=x,B=V(),D&&D.c(),this.h()},l(L){e=p(L,"DIV",{});var M=C(e);l=p(M,"DIV",{class:!0,"data-svelte-h":!0}),A(l)!=="svelte-1ikk5ng"&&(l.innerHTML=t),o=S(M),s=p(M,"FORM",{});var J=C(s);a=p(J,"DIV",{class:!0});var H=C(a);u=p(H,"DIV",{class:!0});var R=C(u);h=p(R,"LABEL",{for:!0,class:!0,"data-svelte-h":!0}),A(h)!=="svelte-jndamv"&&(h.textContent=T),y=S(R),n=p(R,"SELECT",{class:!0,style:!0,"aria-label":!0});var z=C(n);f=p(z,"OPTION",{"data-svelte-h":!0}),A(f)!=="svelte-tv2fe6"&&(f.textContent=b),i=p(z,"OPTION",{"data-svelte-h":!0}),A(i)!=="svelte-190bggj"&&(i.textContent=v),z.forEach(_),R.forEach(_),g=S(H),w&&w.l(H),I=S(H),E&&E.l(H),H.forEach(_),k=S(J),O=p(J,"DIV",{class:!0});var q=C(O);$=p(q,"BUTTON",{type:!0,class:!0,"data-bs-dismiss":!0,"data-svelte-h":!0}),A($)!=="svelte-1f0lmv"&&($.textContent=x),B=S(q),D&&D.l(q),q.forEach(_),J.forEach(_),M.forEach(_),this.h()},h(){r(l,"class","modal-header"),r(h,"for","front-area"),r(h,"class","form-label"),f.__value="",P(f,f.__value),f.disabled=!0,f.selected=!0,i.__value="1",P(i,i.__value),r(n,"class","form-select"),G(n,"color","black"),r(n,"aria-label","Select template"),c[3]===void 0&&$e(()=>c[7].call(n)),r(u,"class","mb-3"),r(a,"class","modal-body"),r($,"type","button"),r($,"class","btn btn-secondary"),r($,"data-bs-dismiss","modal"),r(O,"class","modal-footer")},m(L,M){N(L,e,M),d(e,l),d(e,o),d(e,s),d(s,a),d(a,u),d(u,h),d(u,y),d(u,n),d(n,f),d(n,i),se(n,c[3],!0),d(a,g),w&&w.m(a,null),d(a,I),E&&E.m(a,null),d(s,k),d(s,O),d(O,$),d(O,B),D&&D.m(O,null),j||(U=[F(n,"change",c[7]),F($,"click",c[5]),F(s,"submit",Ve(c[6]))],j=!0)},p(L,[M]){M&8&&se(n,L[3]),L[3]!=0?w?w.p(L,M):(w=ye(L),w.c(),w.m(a,I)):w&&(w.d(1),w=null),L[3]==1?E?E.p(L,M):(E=Ce(L),E.c(),E.m(a,null)):E&&(E.d(1),E=null),L[3]!=0?D||(D=Te(),D.c(),D.m(O,null)):D&&(D.d(1),D=null)},i:W,o:W,d(L){L&&_(e),w&&w.d(),E&&E.d(),D&&D.d(),j=!1,ie(U)}}}function Me(c,e,l){let t="",o="",s="",a="",u=[];function h(){l(3,a=""),l(2,s="")}async function T(){try{const v=await fetch("http://127.0.0.1:8000/users/1/decks/",{method:"GET",headers:{"Content-Type":"application/json"}});v.ok?l(4,u=await v.json()):console.error("Failed decks")}catch(v){console.error("An error occurred while getting decks: ",v)}}async function y(){const v="/decks/"+s+"/",g={front:t,back:o,deck:v};console.log(JSON.stringify(g));try{(await fetch("http://127.0.0.1:8000/fcards/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(g)})).ok?console.log("Form submitted successfully!"):console.error("Failed to submit form")}catch(I){console.error("An error occurred while submitting the form:",I)}}T();function n(){a=_e(this),l(3,a)}function f(){s=_e(this),l(2,s),l(4,u)}function b(){t=this.value,l(0,t)}function i(){o=this.value,l(1,o)}return[t,o,s,a,u,h,y,n,f,b,i]}class Ae extends ue{constructor(e){super(),fe(this,e,Me,Le,oe,{})}}function Ne(c){let e,l,t='<h5 class="modal-title" id="exampleModalLabel">Add deck</h5>',o,s,a,u,h,T,y,n="Name",f,b,i='<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button> <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>',v,g;return{c(){e=m("div"),l=m("div"),l.innerHTML=t,o=V(),s=m("form"),a=m("div"),u=m("div"),h=m("input"),T=V(),y=m("label"),y.textContent=n,f=V(),b=m("div"),b.innerHTML=i,this.h()},l(I){e=p(I,"DIV",{});var k=C(e);l=p(k,"DIV",{class:!0,"data-svelte-h":!0}),A(l)!=="svelte-av1xwb"&&(l.innerHTML=t),o=S(k),s=p(k,"FORM",{});var O=C(s);a=p(O,"DIV",{class:!0});var $=C(a);u=p($,"DIV",{class:!0});var x=C(u);h=p(x,"INPUT",{type:!0,class:!0,id:!0,placeholder:!0,style:!0}),T=S(x),y=p(x,"LABEL",{for:!0,style:!0,"data-svelte-h":!0}),A(y)!=="svelte-125df89"&&(y.textContent=n),x.forEach(_),$.forEach(_),f=S(O),b=p(O,"DIV",{class:!0,"data-svelte-h":!0}),A(b)!=="svelte-12doy0k"&&(b.innerHTML=i),O.forEach(_),k.forEach(_),this.h()},h(){r(l,"class","modal-header"),r(h,"type","text"),r(h,"class","form-control"),r(h,"id","floatingInput"),r(h,"placeholder","name"),G(h,"color","black"),r(y,"for","floatingInput"),G(y,"color","black"),r(u,"class","form-floating mb-3"),r(a,"class","modal-body"),r(b,"class","modal-footer")},m(I,k){N(I,e,k),d(e,l),d(e,o),d(e,s),d(s,a),d(a,u),d(u,h),P(h,c[0]),d(u,T),d(u,y),d(s,f),d(s,b),v||(g=[F(h,"input",c[2]),F(s,"submit",Ve(c[1]))],v=!0)},p(I,[k]){k&1&&h.value!==I[0]&&P(h,I[0])},i:W,o:W,d(I){I&&_(e),v=!1,ie(g)}}}function Be(c,e,l){let t="";async function o(){const u={name:t,owner:1};console.log(JSON.stringify(u));try{(await fetch("http://127.0.0.1:8000/decks/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(u)})).ok?console.log("Form submitted successfully!"):console.error("Failed to submit form")}catch(h){console.error("An error occurred while submitting the form:",h)}}function s(){t=this.value,l(0,t)}return[t,o,s]}class Pe extends ue{constructor(e){super(),fe(this,e,Be,Ne,oe,{})}}function Ie(c,e,l){const t=c.slice();return t[8]=e[l],t}function De(c,e,l){const t=c.slice();return t[4]=e[l],t}function je(c){let e,l="<h3>Cargando..</h3>";return{c(){e=m("div"),e.innerHTML=l},l(t){e=p(t,"DIV",{"data-svelte-h":!0}),A(e)!=="svelte-1ln7ra0"&&(e.innerHTML=l)},m(t,o){N(t,e,o)},p:W,d(t){t&&_(e)}}}function He(c){let e,l=Q(c[0]),t=[];for(let o=0;o<l.length;o+=1)t[o]=Oe(Ie(c,l,o));return{c(){e=m("div");for(let o=0;o<t.length;o+=1)t[o].c();this.h()},l(o){e=p(o,"DIV",{class:!0,id:!0});var s=C(e);for(let a=0;a<t.length;a+=1)t[a].l(s);s.forEach(_),this.h()},h(){r(e,"class","accordion"),r(e,"id","accordionPanelsStayOpenExample")},m(o,s){N(o,e,s);for(let a=0;a<t.length;a+=1)t[a]&&t[a].m(e,null)},p(o,s){if(s&5){l=Q(o[0]);let a;for(a=0;a<l.length;a+=1){const u=Ie(o,l,a);t[a]?t[a].p(u,s):(t[a]=Oe(u),t[a].c(),t[a].m(e,null))}for(;a<t.length;a+=1)t[a].d(1);t.length=l.length}},d(o){o&&_(e),ce(t,o)}}}function we(c){let e,l,t,o,s=c[4].id+"",a,u,h,T;function y(){return c[5](c[4])}return{c(){e=m("a"),l=m("div"),t=m("p"),o=X("Card "),a=X(s),u=V(),this.h()},l(n){e=p(n,"A",{class:!0,"aria-current":!0});var f=C(e);l=p(f,"DIV",{class:!0});var b=C(l);t=p(b,"P",{});var i=C(t);o=K(i,"Card "),a=K(i,s),i.forEach(_),b.forEach(_),u=S(f),f.forEach(_),this.h()},h(){r(l,"class","d-flex w-100 justify-content-between"),r(e,"class","list-group-item list-group-item-action active card-view svelte-1ab66qd"),r(e,"aria-current","true")},m(n,f){N(n,e,f),d(e,l),d(l,t),d(t,o),d(t,a),d(e,u),h||(T=F(e,"click",y),h=!0)},p(n,f){c=n,f&1&&s!==(s=c[4].id+"")&&de(a,s)},d(n){n&&_(e),h=!1,T()}}}function Oe(c){let e,l,t,o=c[8].deck.name+"",s,a,u,h,T,y,n,f,b,i=Q(c[8].cards),v=[];for(let g=0;g<i.length;g+=1)v[g]=we(De(c,i,g));return{c(){e=m("div"),l=m("h2"),t=m("button"),s=X(o),h=V(),T=m("div"),y=m("div"),n=m("div");for(let g=0;g<v.length;g+=1)v[g].c();b=V(),this.h()},l(g){e=p(g,"DIV",{class:!0});var I=C(e);l=p(I,"H2",{class:!0});var k=C(l);t=p(k,"BUTTON",{class:!0,type:!0,"data-bs-toggle":!0,"data-bs-target":!0,"aria-expanded":!0,"aria-controls":!0});var O=C(t);s=K(O,o),O.forEach(_),k.forEach(_),h=S(I),T=p(I,"DIV",{id:!0,class:!0});var $=C(T);y=p($,"DIV",{class:!0});var x=C(y);n=p(x,"DIV",{class:!0});var B=C(n);for(let j=0;j<v.length;j+=1)v[j].l(B);B.forEach(_),x.forEach(_),$.forEach(_),b=S(I),I.forEach(_),this.h()},h(){r(t,"class","accordion-button"),r(t,"type","button"),r(t,"data-bs-toggle","collapse"),r(t,"data-bs-target",a="#panelsStayOpen-collapse"+c[8].deck.id),r(t,"aria-expanded","true"),r(t,"aria-controls",u="panelsStayOpen-collapse"+c[8].deck.id),r(l,"class","accordion-header"),r(n,"class","list-group"),r(y,"class","accordion-body"),r(T,"id",f="panelsStayOpen-collapse"+c[8].deck.id),r(T,"class","accordion-collapse collapse"),r(e,"class","accordion-item")},m(g,I){N(g,e,I),d(e,l),d(l,t),d(t,s),d(e,h),d(e,T),d(T,y),d(y,n);for(let k=0;k<v.length;k+=1)v[k]&&v[k].m(n,null);d(e,b)},p(g,I){if(I&1&&o!==(o=g[8].deck.name+"")&&de(s,o),I&1&&a!==(a="#panelsStayOpen-collapse"+g[8].deck.id)&&r(t,"data-bs-target",a),I&1&&u!==(u="panelsStayOpen-collapse"+g[8].deck.id)&&r(t,"aria-controls",u),I&5){i=Q(g[8].cards);let k;for(k=0;k<i.length;k+=1){const O=De(g,i,k);v[k]?v[k].p(O,I):(v[k]=we(O),v[k].c(),v[k].m(n,null))}for(;k<v.length;k+=1)v[k].d(1);v.length=i.length}I&1&&f!==(f="panelsStayOpen-collapse"+g[8].deck.id)&&r(T,"id",f)},d(g){g&&_(e),ce(v,g)}}}function Fe(c){let e,l,t,o,s,a,u,h,T,y,n,f,b,i,v,g,I,k,O,$,x,B;o=new be({}),T=new be({});function j(E,D){return E[1]?He:je}let U=j(c),w=U(c);return g=new Ae({}),x=new Pe({}),{c(){e=m("div"),l=m("button"),t=m("div"),Y(o.$$.fragment),s=X(`
            Add card`),a=V(),u=m("button"),h=m("div"),Y(T.$$.fragment),y=X(`
            Add deck`),n=V(),w.c(),f=V(),b=m("div"),i=m("div"),v=m("div"),Y(g.$$.fragment),I=V(),k=m("div"),O=m("div"),$=m("div"),Y(x.$$.fragment),this.h()},l(E){e=p(E,"DIV",{});var D=C(e);l=p(D,"BUTTON",{type:!0,class:!0,"data-bs-toggle":!0,"data-bs-target":!0});var L=C(l);t=p(L,"DIV",{class:!0});var M=C(t);Z(o.$$.fragment,M),s=K(M,`
            Add card`),M.forEach(_),L.forEach(_),a=S(D),u=p(D,"BUTTON",{type:!0,class:!0,"data-bs-toggle":!0,"data-bs-target":!0});var J=C(u);h=p(J,"DIV",{class:!0});var H=C(h);Z(T.$$.fragment,H),y=K(H,`
            Add deck`),H.forEach(_),J.forEach(_),n=S(D),w.l(D),f=S(D),b=p(D,"DIV",{class:!0,id:!0,tabindex:!0,"aria-labelledby":!0,"aria-hidden":!0});var R=C(b);i=p(R,"DIV",{class:!0});var z=C(i);v=p(z,"DIV",{class:!0});var q=C(v);Z(g.$$.fragment,q),q.forEach(_),z.forEach(_),R.forEach(_),I=S(D),k=p(D,"DIV",{class:!0,id:!0,tabindex:!0,"aria-labelledby":!0,"aria-hidden":!0});var ve=C(k);O=p(ve,"DIV",{class:!0});var me=C(O);$=p(me,"DIV",{class:!0});var pe=C($);Z(x.$$.fragment,pe),pe.forEach(_),me.forEach(_),ve.forEach(_),D.forEach(_),this.h()},h(){r(t,"class","d-flex align-items-center"),r(l,"type","button"),r(l,"class","btn btn-primary"),r(l,"data-bs-toggle","modal"),r(l,"data-bs-target","#exampleModal"),r(h,"class","d-flex align-items-center"),r(u,"type","button"),r(u,"class","btn btn-primary"),r(u,"data-bs-toggle","modal"),r(u,"data-bs-target","#deckModal"),r(v,"class","modal-content"),r(i,"class","modal-dialog"),r(b,"class","modal fade"),r(b,"id","exampleModal"),r(b,"tabindex","-1"),r(b,"aria-labelledby","exampleModalLabel"),r(b,"aria-hidden","true"),r($,"class","modal-content"),r(O,"class","modal-dialog"),r(k,"class","modal fade"),r(k,"id","deckModal"),r(k,"tabindex","-1"),r(k,"aria-labelledby","exampleModalLabel"),r(k,"aria-hidden","true")},m(E,D){N(E,e,D),d(e,l),d(l,t),ee(o,t,null),d(t,s),d(e,a),d(e,u),d(u,h),ee(T,h,null),d(h,y),d(e,n),w.m(e,null),d(e,f),d(e,b),d(b,i),d(i,v),ee(g,v,null),d(e,I),d(e,k),d(k,O),d(O,$),ee(x,$,null),B=!0},p(E,[D]){U===(U=j(E))&&w?w.p(E,D):(w.d(1),w=U(E),w&&(w.c(),w.m(e,f)))},i(E){B||(te(o.$$.fragment,E),te(T.$$.fragment,E),te(g.$$.fragment,E),te(x.$$.fragment,E),B=!0)},o(E){le(o.$$.fragment,E),le(T.$$.fragment,E),le(g.$$.fragment,E),le(x.$$.fragment,E),B=!1},d(E){E&&_(e),ae(o),ae(T),w.d(),ae(g),ae(x)}}}function Ue(c,e,l){let t,o,s;re(c,ge,n=>l(0,t=n)),re(c,ne,n=>l(7,o=n));function a(n){xe(`/dashboard/decks/${n}`)}let u=he(!1);re(c,u,n=>l(1,s=n));let h;Se(async function(){const b=await(await fetch("http://localhost:8000/users/1/decks/")).json();ne.set([]),ge.set([]),h=b.decks,ne.set(h),Object.keys(o).forEach(i=>{T(o[i].id)}),u.set(!0)});async function T(n){const f=`http://localhost:8000/decks/${n}/cards/`,i=await(await fetch(f)).json();t.push(i)}return[t,s,a,u,T,n=>a(n.id)]}class Ke extends ue{constructor(e){super(),fe(this,e,Ue,Fe,oe,{})}}export{Ke as component};
