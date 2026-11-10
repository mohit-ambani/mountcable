// Quote request endpoint for AI agents and other software clients.
// Validates the request and forwards it to the shop's quote inbox, the same
// inbox the form on /quote posts to. A person replies to the buyer on WhatsApp.
const INBOX = "https://formsubmit.co/ajax/mountcable@gmail.com";
const WA = "https://wa.me/918867676700";
const clean = (v, max) => (typeof v === "string" ? v.replace(/[\u0000-\u0008\u000b-\u001f]/g, "").trim().slice(0, max) : "");

module.exports = async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Cache-Control", "no-store");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") {
    return res.status(405).json({
      error: "Use POST with a JSON body.",
      required: ["phone", "requirement"], optional: ["name", "area", "agent", "dry_run"],
      docs: "https://mountcable.com/for-ai-agents", spec: "https://mountcable.com/openapi.json",
    });
  }
  let b = req.body;
  if (typeof b === "string") { try { b = JSON.parse(b); } catch (e) { b = null; } }
  if (!b || typeof b !== "object") return res.status(400).json({ error: "Body must be JSON." });

  const name = clean(b.name, 80), area = clean(b.area, 80), agent = clean(b.agent, 60);
  const requirement = clean(b.requirement, 3000);
  const phone = clean(b.phone, 20).replace(/[^0-9+]/g, "");
  const digits = phone.replace(/\D/g, "");
  const problems = [];
  if (digits.length < 10 || digits.length > 13) problems.push("phone: a 10-digit Indian mobile number (the quote is sent there on WhatsApp)");
  if (requirement.length < 5) problems.push("requirement: the items needed, e.g. 'Finolex FR-LSH 1.5 sq mm x 6 coils, 2.5 sq mm x 4 coils'");
  if (problems.length) return res.status(400).json({ error: "Missing or invalid fields.", fix: problems });

  const whatsapp = WA + "?text=" + encodeURIComponent(
    "Quote request" + (name ? " from " + name : "") + (area ? " (" + area + ")" : "") + ":\n" + requirement);
  const next = "Mount Cable India replies on WhatsApp to the buyer's number, normally within 60 minutes, Mon-Sat 10:00-20:00 IST. Delivery is free across Bangalore by the next day; payment is taken after delivery.";

  if (b.dry_run === true) {
    return res.status(200).json({ status: "valid", sent: false, whatsapp_link: whatsapp, next_steps: next });
  }
  try {
    const r = await fetch(INBOX, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json",
                 Origin: "https://mountcable.com", Referer: "https://mountcable.com/quote" },
      body: JSON.stringify({
        _subject: "Quote request via AI agent" + (agent ? " (" + agent + ")" : ""),
        _template: "table", _captcha: "false",
        Name: name || "(not given)", Phone: phone, Area: area || "(not given)",
        Requirement: requirement, Source: agent ? "AI agent: " + agent : "Quote API",
      }),
    });
    const j = await r.json().catch(() => ({}));
    if (r.ok && String(j.success) === "true") {
      return res.status(200).json({ status: "received", sent: true, whatsapp_link: whatsapp, next_steps: next });
    }
    throw new Error("inbox " + r.status);
  } catch (e) {
    // Never leave the agent without a way through: hand back the WhatsApp link.
    return res.status(200).json({
      status: "not_delivered", sent: false, whatsapp_link: whatsapp,
      next_steps: "The request could not be delivered automatically. Ask the buyer to open whatsapp_link, which starts a chat with Mount Cable India with the list already typed, or call +91 88676 76700.",
    });
  }
};
