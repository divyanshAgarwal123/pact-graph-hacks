const $ = (id) => document.getElementById(id);
const labels = {devices:"Retired devices",wipe:"Data wiping",repair:"Preparation",room:"Clinic room"};
const stepLabels = {wipe:"Wipe devices",transfer:"Move to workshop",prepare:"Prepare devices",deliver:"Deliver to school"};
function clock(minutes){const m=minutes%1440;return `${String(Math.floor(m/60)).padStart(2,"0")}:${String(m%60).padStart(2,"0")}`}
function el(tag,className,text){const node=document.createElement(tag);if(className)node.className=className;if(text!==undefined)node.textContent=text;return node}
function render(data){
  const {scenario,proposal,episodes,memories}=data;
  const recovered=scenario.completed_wipe_ids.length>0;
  const verdict=document.querySelector(".verdict");verdict.classList.toggle("blocked",proposal.status!=="feasible_within_model");
  $("verdict-title").textContent=proposal.status==="feasible_within_model"?"Feasible within model":"Proposal blocked";
  $("verdict-time").textContent=proposal.status==="feasible_within_model"?`Delivery ${clock(proposal.delivery_by_minute)}`:"Needs a new plan";
  $("verdict-detail").textContent=proposal.status==="feasible_within_model"?
    `${recovered?"W2 covers the remaining 10 devices. ":"Four organizations cover every contribution. "}The checked schedule meets the school's 15:00 deadline.`:proposal.reason;
  const partners=$("partner-grid");partners.replaceChildren();
  for(const kind of ["devices","wipe","repair","room"]){
    const offer=scenario.offers[kind];const card=el("article","partner");card.dataset.kind=kind;
    card.append(el("span","role",labels[kind]),el("h3",null,offer?.organization||"No active provider"),
      el("p",null,offer?`${offer.id.replaceAll("-"," ")} · from the live graph`:"This requirement needs another offer."),
      el("div","qty",offer?`${offer.quantity} declared ${kind==="room"?"room":"units"}`:"Missing"));
    partners.append(card);
  }
  const schedule=$("schedule");schedule.replaceChildren();
  if(proposal.steps){for(const key of ["wipe","transfer","prepare","deliver"]){
    const step=el("div","step");step.append(el("small",null,key==="deliver"?"Before 15:00 deadline":"Day 1"),el("strong",null,stepLabels[key]),
      el("span",null,`${clock(proposal.steps[key].start)}–${clock(proposal.steps[key].end)}`));schedule.append(step)}
    schedule.after(document.querySelector(".day2")||el("div","day2","Day 2: community clinic 09:00–12:00, then school introduction 12:00–13:00. The room is never double booked."));
  }else{schedule.append(el("p","empty",proposal.reason));document.querySelector(".day2")?.remove()}
  const done=new Set(scenario.completed_wipe_ids);$("retained-count").textContent=`${done.size} / ${scenario.quantity}`;
  const devices=$("devices");devices.replaceChildren();for(const id of scenario.device_ids.slice(0,scenario.quantity)){
    const node=el("span",`device${done.has(id)?" done":""}`,id);node.title=done.has(id)?"Synthetic wipe completed":"Wipe outstanding";devices.append(node)}
  $("recovery-title").textContent=recovered?"Replacement after withdrawal":"Original plan";
  $("recovery-copy").textContent=recovered?"W's completed records remain. W2 handles only L11–L20; the transfer and preparation shift later, while the school deadline still holds.":"The original wiping provider can process all 20 devices before transfer.";
  const past=memories?.[0];
  $("memory-note").textContent=past?`${episodes.length?"Withdrawal recorded. ":""}Earlier, W2 failed at ${past.past_rate}/hour. Its current offer is ${past.current_rate}/hour, so that old failure ${past.applicable_now?"still warrants caution":"does not apply"}. No approval is inferred from memory.`:"No historical case is available in this graph.";
  $("withdraw").disabled=recovered;
  $("action-status").textContent=recovered?"Withdrawal simulated. No real organization was contacted.":"Original synthetic scenario loaded.";
  $("agent-result").textContent="Run a review to see the tools and evidence used.";
}
async function load(path="/api/state",method="GET"){
  $("action-status").textContent="Reading FalkorDB…";
  try{const response=await fetch(path,{method});const data=await response.json();if(!response.ok)throw new Error(data.detail||"Request failed");render(data)}
  catch(error){$("action-status").textContent=error.message;$("verdict-title").textContent="Graph unavailable";$("verdict-time").textContent="";$("verdict-detail").textContent="Start FalkorDB and refresh this page."}
}
$("withdraw").addEventListener("click",()=>load("/api/withdraw","POST"));
$("reset").addEventListener("click",()=>load("/api/reset","POST"));
$("agent-review").addEventListener("click",async()=>{
  const button=$("agent-review"),output=$("agent-result");button.disabled=true;output.textContent="The local agent is reading the graph…";
  try{const response=await fetch("/api/agent-review",{method:"POST"});const result=await response.json();
    if(!response.ok)throw new Error(result.detail||"Agent unavailable");
    output.replaceChildren();if(result.status!=="reviewed"){output.textContent=result.reason;return}
    output.append(el("strong",null,result.recommendation==="present_plan"?"Present the checked proposal":"Seek a new offer"),
      el("p",null,result.explanation),
      el("small",null,`Tools: ${result.trace.join(" → ")}`),
      el("small",null,`Evidence: ${result.evidence_ids.join(", ")}`));
  }catch(error){output.textContent=error.message}finally{button.disabled=false}
});
load();
