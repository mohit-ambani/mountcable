# -*- coding: utf-8 -*-
"""Finolex Wires Stories page — content and the real-customer story register.

READ THIS BEFORE ADDING ANYTHING TO `STORIES`
=============================================
Every entry in STORIES is published as a customer endorsement. Under the CCPA
"Guidelines for Prevention of Misleading Advertisements and Endorsements" (2022)
an endorsement must reflect the genuine, current opinion of a real, identified
person, and under BIS IS 19000:2022 fabricated reviews are prohibited. Google's
site-reputation and scaled-content policies treat invented testimonials as spam.

So: only add a story when ALL of these are true.
  1. A real, named customer actually said it.
  2. They gave permission for their words, first name, area and photo to be used.
  3. `consent` records HOW that permission was given (e.g. "WhatsApp 2026-08-04").
  4. The photo is of that person, not a stock or generated image.

An empty STORIES list is fine — the page renders an honest collection state.
Never pad this list to make the page look fuller.

Schema:
    {
      "name": "First name or full name, as they agreed",
      "area": "Locality / city",
      "role": "Homeowner | Electrician | Contractor | Builder",   (optional)
      "photo": "filename in assets/img/stories-real/",            (optional)
      "en": "Their words in English",
      "kn": "Their words in Kannada",     (optional; only if genuinely given/translated)
      "hi": "Their words in Hindi",       (optional)
      "bought": "What they bought, e.g. 'Finolex FR 90m coils, 2BHK'",  (optional)
      "consent": "How and when permission was recorded",
    }
"""

# Real, consented customer stories. Empty until genuine ones are collected.
STORIES = []


# --- Illustrative photography -------------------------------------------------
# AI-generated ILLUSTRATIONS. Labelled as illustrations on the page and never
# paired with a name or an attributed quote. Prompts banned all brand marks, so
# no generated Finolex branding exists in any of these.
ILLUSTRATIONS = [
    ("story-homeowner-man-coil.jpg", "Homeowner in Bangalore holding a coil of house wiring cable for his new house"),
    ("story-homeowner-woman-coil.jpg", "Woman homeowner holding electrical wire coils in her newly built home"),
    ("story-couple-together-coils.jpg", "Couple holding house wire coils in their half-built home in Bangalore"),
    ("story-electrician-portrait-coil.jpg", "Electrician holding a coil of house wiring cable at a job in Bangalore"),
    ("story-senior-man-coil.jpg", "Senior homeowner holding a coil of electrical cable outside his home"),
    ("story-contractor-team-coils.jpg", "Building contractor and his team with house wire coils at a residential site"),
    ("story-young-man-first-home.jpg", "Young homeowner holding house wiring cable in his first new home"),
    ("story-woman-engineer-site.jpg", "Woman civil engineer holding electrical cable at a construction site in Karnataka"),
    ("story-family-with-materials.jpg", "Family with electrical material delivered for their new house in Bangalore"),
    ("story-shopkeeper-handover.jpg", "Electrical dealer handing a coil of house wire to a customer across the counter"),
    ("story-man-scanning-pack.jpg", "Customer scanning the QR code on a wire coil before paying for it"),
    ("story-builder-bulk-order.jpg", "Builder with a bulk order of electrical material at a site in Bangalore"),
]

# The four real Finolex pack photographs supplied by the owner.
PACK_PHOTOS = [
    ("finolex-pack-1.jpg", "Genuine Finolex house wire coil in its sealed factory pack"),
    ("finolex-pack-2.jpg", "Finolex wire coil pack showing the printed grade and size markings"),
    ("finolex-pack-3.jpg", "Finolex FLAMEGARD FR-LSH 1.5 sq mm coil pack with the QR code visible on the wrapper"),
    ("finolex-pack-4.jpg", "Sealed Finolex cable pack as supplied by Mount Cable India in Bangalore"),
]


# --- Trilingual editorial ------------------------------------------------------
# First-party brand copy in Mount Cable's own voice. This is the argument the
# owner makes to customers every day; it is not attributed to any customer.
NARRATIVE = {
    "en": {
        "label": "English",
        "html": """
<p>Most people who buy their house wiring from us are not buying wire for the first time. They are buying it for the second time. They bought once somewhere else, something went wrong or a doubt was never settled, and then they went looking for a dealer who would let them check before paying.</p>
<p>That is the whole reason this page exists. Not to tell you we are the best — anyone can print that on a website. It is here to tell you exactly what to check, so you can decide for yourself, whether you buy from us or from anyone else.</p>
<p>Many firms will tell you they are Finolex dealers. Many large, impressive showrooms will tell you the same thing. Some of them are. The showroom cannot tell you which. <strong>Scan every single coil before you pay — the QR printed on the outside of the pack, and the QR inside the box.</strong> A genuine coil passes both. A refilled carton passes only the first. And a seller who does not want you scanning before you pay has already answered your question.</p>
<p>We keep everything in stock, we give the best pricing we can across Bangalore, and you are welcome to verify any single coil — or our entire stock — before you buy anything at all.</p>
"""},
    "kn": {
        "label": "ಕನ್ನಡ",
        "html": """
<p>ನಮ್ಮಿಂದ ಮನೆಯ ವೈರಿಂಗ್ ಖರೀದಿಸುವ ಹೆಚ್ಚಿನವರು ಮೊದಲ ಬಾರಿಗೆ ವೈರ್ ಖರೀದಿಸುತ್ತಿರುವುದಿಲ್ಲ. ಅವರು ಎರಡನೇ ಬಾರಿ ಖರೀದಿಸುತ್ತಿರುತ್ತಾರೆ. ಒಮ್ಮೆ ಬೇರೆಡೆ ಖರೀದಿಸಿದರು, ಏನೋ ತಪ್ಪಾಯಿತು ಅಥವಾ ಅನುಮಾನ ಪರಿಹಾರವಾಗಲಿಲ್ಲ — ನಂತರ ಹಣ ಕೊಡುವ ಮೊದಲು ಪರಿಶೀಲಿಸಲು ಅವಕಾಶ ಕೊಡುವ ಡೀಲರ್‌ನನ್ನು ಹುಡುಕಿಕೊಂಡು ಬಂದರು.</p>
<p>ಈ ಪುಟ ಇರುವುದೇ ಅದಕ್ಕಾಗಿ. ನಾವೇ ಅತ್ಯುತ್ತಮ ಎಂದು ಹೇಳಲು ಅಲ್ಲ — ಅದನ್ನು ಯಾವ ವೆಬ್‌ಸೈಟ್‌ನಲ್ಲಿ ಬೇಕಾದರೂ ಮುದ್ರಿಸಬಹುದು. ನೀವು ಏನನ್ನು ಪರಿಶೀಲಿಸಬೇಕು ಎಂದು ಹೇಳಲು ಈ ಪುಟ ಇದೆ — ನೀವು ನಮ್ಮಿಂದ ಖರೀದಿಸಿದರೂ, ಬೇರೆಯವರಿಂದ ಖರೀದಿಸಿದರೂ, ನೀವೇ ನಿರ್ಧರಿಸಬಹುದು.</p>
<p>ಹಲವು ಸಂಸ್ಥೆಗಳು ತಾವು ಫಿನೋಲೆಕ್ಸ್ ಡೀಲರ್ ಎಂದು ಹೇಳುತ್ತವೆ. ದೊಡ್ಡ, ಆಕರ್ಷಕ ಶೋರೂಂಗಳೂ ಅದನ್ನೇ ಹೇಳುತ್ತವೆ. ಕೆಲವರು ನಿಜವಾಗಿಯೂ ಡೀಲರ್ ಆಗಿರುತ್ತಾರೆ. ಆದರೆ ಯಾರು ಎಂಬುದನ್ನು ಶೋರೂಂ ನೋಡಿ ಹೇಳಲಾಗದು. <strong>ಹಣ ಕೊಡುವ ಮೊದಲು ಪ್ರತಿಯೊಂದು ಕಾಯಿಲ್ ಅನ್ನೂ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ — ಪ್ಯಾಕ್‌ನ ಹೊರಗಿನ QR ಮತ್ತು ಡಬ್ಬದ ಒಳಗಿನ QR, ಎರಡನ್ನೂ.</strong> ನಿಜವಾದ ಕಾಯಿಲ್ ಎರಡರಲ್ಲೂ ಪಾಸ್ ಆಗುತ್ತದೆ. ಮತ್ತೆ ತುಂಬಿಸಿದ ಡಬ್ಬ ಮೊದಲನೆಯದರಲ್ಲಿ ಮಾತ್ರ ಪಾಸ್ ಆಗುತ್ತದೆ. ಹಣ ಕೊಡುವ ಮೊದಲು ಸ್ಕ್ಯಾನ್ ಮಾಡಲು ಬಿಡದ ಮಾರಾಟಗಾರ ನಿಮಗೆ ಈಗಾಗಲೇ ಉತ್ತರ ಕೊಟ್ಟಿದ್ದಾನೆ.</p>
<p>ನಾವು ಎಲ್ಲವನ್ನೂ ಸ್ಟಾಕ್‌ನಲ್ಲಿ ಇಟ್ಟಿರುತ್ತೇವೆ, ಬೆಂಗಳೂರಿನಲ್ಲಿ ನಮ್ಮಿಂದ ಸಾಧ್ಯವಾದ ಅತ್ಯುತ್ತಮ ಬೆಲೆ ಕೊಡುತ್ತೇವೆ, ಮತ್ತು ಏನನ್ನಾದರೂ ಖರೀದಿಸುವ ಮೊದಲು ಯಾವುದೇ ಒಂದು ಕಾಯಿಲ್ ಅನ್ನು — ಅಥವಾ ನಮ್ಮ ಇಡೀ ಸ್ಟಾಕ್ ಅನ್ನು — ಪರಿಶೀಲಿಸಲು ನಿಮಗೆ ಸ್ವಾಗತ.</p>
"""},
    "hi": {
        "label": "हिन्दी",
        "html": """
<p>हमसे घर की वायरिंग खरीदने वाले ज़्यादातर लोग पहली बार तार नहीं खरीद रहे होते। वे दूसरी बार खरीद रहे होते हैं। एक बार कहीं और से खरीदा, कुछ गड़बड़ हुई या शक कभी दूर नहीं हुआ — और फिर वे ऐसा डीलर ढूँढने निकले जो पैसे देने से पहले जाँच करने दे।</p>
<p>यही वजह है कि यह पेज बनाया गया है। यह बताने के लिए नहीं कि हम सबसे अच्छे हैं — ऐसा तो कोई भी वेबसाइट पर छाप सकता है। यह इसलिए है ताकि आपको पता चले कि जाँचना क्या है, और आप खुद फ़ैसला कर सकें — चाहे हमसे खरीदें या कहीं और से।</p>
<p>बहुत सी फ़र्में कहेंगी कि वे फिनोलेक्स डीलर हैं। बड़े और प्रभावशाली शोरूम भी यही कहेंगे। कुछ सचमुच डीलर होते हैं। लेकिन शोरूम देखकर यह तय नहीं किया जा सकता कि कौन है। <strong>पैसे देने से पहले हर एक कॉइल स्कैन कीजिए — पैक के बाहर छपा QR और डिब्बे के अंदर वाला QR, दोनों।</strong> असली कॉइल दोनों में पास होती है। दोबारा भरा गया डिब्बा सिर्फ़ पहले में पास होता है। और जो दुकानदार पैसे देने से पहले स्कैन नहीं करने देता, उसने आपको जवाब दे ही दिया है।</p>
<p>हमारे पास सब कुछ स्टॉक में रहता है, बैंगलोर में हम अपनी तरफ़ से सबसे अच्छी कीमत देते हैं, और कुछ भी खरीदने से पहले आप कोई भी एक कॉइल — या हमारा पूरा स्टॉक — जाँच सकते हैं।</p>
"""},
}

FAQS = [
    ("Are the stories on this page real customers?",
     "Yes. We only publish a story when a real, named customer has told it to us and has given permission for their words, first name and area to be used. Where a page section is illustrated with photography rather than a customer photograph, it is labelled as an illustration. We would rather show fewer stories than invent any."),
    ("How do I know a shop is really a Finolex dealer?",
     "Ask to see the authorisation certificate for Finolex and check that the name on it matches the shop's billing entity. Then, regardless of the answer, scan the QR on the outside of every coil and the QR inside the box before you pay. Genuine stock passes both scans; a refilled carton passes only the outer one."),
    ("Why do people say they were fooled at another electrical shop?",
     "Usually because they were sold wire at a price that looked like a bargain. Genuine branded wire runs on a 3 to 5% dealer margin, so a discount of 15% or more is not a discount at all — it indicates copper shortfall, a short coil or counterfeit stock. None of that is visible once the wire is inside a wall."),
    ("Can I check your stock before buying anything?",
     "Yes, and we encourage it. Come to Jayanagar or Chickpete and scan any coil you like, or the entire stock if you want to. You can also buy on pay-on-delivery terms, scan every carton at your own site, and pay only after everything verifies."),
    ("Do you really give the best price in Bangalore?",
     "We give the best price we can, and we would rather you checked than took our word for it. Send your list to 88676 76700 for an itemised quote within 60 minutes and use it as your reference anywhere in the city. There is no obligation to buy from us — plenty of people use our quote only to cross-check another shop."),
    ("Where can I read independent reviews?",
     "On our Google listing, which we do not control and cannot edit. That is the point of it — those reviews are written by customers, not by us."),
]
