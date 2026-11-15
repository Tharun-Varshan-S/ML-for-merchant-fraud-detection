"""
Section 3 — Explain the Project to a Normal Friend generator.
"""

def get_section3_html():
    return '''
<div class="page-break"></div>
<h1 id="section-3"><span class="section-number">3</span> EXPLAIN THE PROJECT TO A NORMAL FRIEND</h1>

<h2 id="sec-3-1">3.1 A Familiar Real-World Situation: Ananya's Handcrafted Silk Boutique</h2>
<p>
  Imagine you have a close friend named <strong>Ananya</strong> who runs a growing, independent online boutique in Bangalore called <em>"Varnam Silks"</em>. Ananya curates authentic Kanjivaram silk sarees and hand-woven garments. Over three years, Ananya has built a loyal community of several thousand repeat customers across India.
</p>
<p>
  Her typical customer spends between <strong>₹1,500 and ₹4,000</strong> per purchase. One such loyal customer is <strong>Vikram</strong>, a software engineer living in Indiranagar, Bangalore. Over the past eighteen months, Vikram has bought five sarees from Varnam Silks for his mother and sister. Every single time, Vikram ordered from his personal iPhone while connected to his home Wi-Fi network in Bangalore, paid around ₹2,500 using his familiar HDFC credit card, and the deliveries arrived without incident.
</p>
<p>
  To Vikram and Ananya, buying online feels instantaneous: Vikram clicks "Pay Now", a green checkmark appears three seconds later, Ananya packages the saree, and Blue Dart delivers it two days later.
</p>

<h2 id="sec-3-2">3.2 The Nightmare Without MerchantShield: The Chargeback Trap</h2>
<p>
  Now, let's see what happens when criminal fraud enters the picture without an intelligent system like MerchantShield AI.
</p>
<p>
  One Tuesday evening at 1:45 AM, an unauthorized third party operating from a computer in an unfamiliar location gains access to Vikram's stored payment credentials through an unrelated data breach. The attacker visits Ananya's website, creates a cart with four of her most luxurious wedding silk sarees totaling <strong>₹45,000</strong> (twenty times Vikram's normal spending), and clicks "Pay Now".
</p>
<p>
  What happens under a conventional, naive system?
</p>
<ol>
  <li><strong>The Bank Sees Valid Card Details:</strong> Because the card number, expiration date, and CVV match the bank's database, the payment processor authorizes the charge.</li>
  <li><strong>Ananya Ships the Goods:</strong> The next morning, Ananya sees a ₹45,000 order—her biggest sale of the week. Delighted, she carefully packages the exquisite hand-woven sarees and ships them via express courier.</li>
  <li><strong>The True Cardholder Discovers the Theft:</strong> Three days later, the real Vikram checks his credit card statement, panics, and immediately calls his bank to report fraud: <em>"I was asleep on Tuesday night; I never bought ₹45,000 worth of wedding sarees!"</em></li>
  <li><strong>The Devastating Chargeback:</strong> The issuing bank investigates, confirms the theft, and forcibly claws back the ₹45,000 from Ananya's business bank account. On top of that, the payment processor penalizes Ananya with a ₹1,500 chargeback fee.</li>
</ol>
<p>
  Ananya is left completely devastated: <strong>she has lost the ₹45,000 in revenue, her physical silk sarees are gone forever, and she had to pay a penalty fee.</strong>
</p>
<p>
  In response, many merchants try to protect themselves by hiring human staff to manually review every large transaction or by installing crude, rigid rules like: <em>"Block any order over ₹10,000"</em>. But this creates the opposite disaster: when Vikram genuinely wants to buy an expensive wedding anniversary gift for his wife for ₹25,000, the blunt rule blocks his card. Vikram is insulted, abandons the website, and buys from a giant retail competitor instead.
</p>

<h2 id="sec-3-3">3.3 Introducing MerchantShield AI: The Invisible Risk Manager</h2>
<p>
  This is why Ananya needs <strong>MerchantShield AI</strong>.
</p>
<p>
  Think of MerchantShield AI as an extraordinarily sharp, calm, and fair chief risk officer who stands behind the cash register 24 hours a day. Every time a customer clicks "Pay", this risk manager examines the transaction in less than fifty milliseconds.
</p>
<p>
  Crucially, this digital risk manager does not guess, does not jump to wild conclusions, and does not hold an axe to instantly cancel orders. Instead, it follows a disciplined three-step reasoning process:
</p>
<ol>
  <li><strong>It Looks at Behavioral Memory:</strong> It immediately retrieves Vikram's past shopping habits. It notices: <em>"Vikram usually spends ₹2,500, shops between 6 PM and 9 PM, and always uses his iPhone in Bangalore."</em></li>
  <li><strong>It Estimates the Objective Probability of Fraud:</strong> It compares the current purchase against thousands of past historical patterns using a sophisticated mathematical model. It calculates: <em>"The probability that this 1:45 AM, ₹45,000 purchase from a brand-new device in an unfamiliar region is fraudulent is 99.9%."</em></li>
  <li><strong>It Applies a Balanced Business Policy:</strong> Instead of doing something irreversible, it looks at its rulebook. Because the risk is overwhelming (above 80%), it recommends: <strong>BLOCK</strong>. But if the risk had been moderate (say, Vikram buying a ₹5,000 saree while traveling on business), it wouldn't block him—it would simply recommend <strong>STEP-UP VERIFICATION</strong>, prompting Vikram for a quick One-Time Password (OTP) on his registered mobile phone!</li>
</ol>

<h2 id="sec-3-4">3.4 The Complete Scenario Walkthrough: Step-by-Step</h2>
<p>
  Let's trace exactly what happens under MerchantShield AI during that Tuesday night attack:
</p>

<h3>Step 1: The Trigger</h3>
<p>
  At 01:45:12 UTC, the attacker clicks "Complete Purchase" on Varnam Silks' checkout page for transaction <code>txn_live_test_001</code>. The online storefront's backend captures the checkout event.
</p>

<h3>Step 2: Information Entering the System</h3>
<p>
  The storefront packages the transaction details into a structured digital envelope:
</p>
<ul>
  <li><strong>Current Purchase:</strong> Amount ₹45,000; Customer ID <code>cust_00042</code> (Vikram); Device ID <code>dev_BRAND_NEW</code>; Region <code>region_19</code> (unfamiliar); Time: 1:45 AM.</li>
  <li><strong>Prior History:</strong> Vikram's past six legitimate orders from the last six months (all card payments between ₹500 and ₹2,500 from <code>dev_known</code> in <code>region_03</code>).</li>
</ul>

<h3>Step 3: What the System Does With the Information</h3>
<p>
  MerchantShield AI's backend receives the envelope. In less than 15 milliseconds, its feature engine calculates 15 behavioral indicators strictly comparing the new order against the past history:
</p>
<ul>
  <li><strong>Amount Spike:</strong> The current amount (₹45,000) is <strong>85.7 times larger</strong> than Vikram's historical average amount (₹525).</li>
  <li><strong>Z-Score Outlier:</strong> The amount is more than 20 standard deviations above his typical spending distribution.</li>
  <li><strong>Device Novelty:</strong> The device hardware fingerprint has never been seen before in Vikram's account history.</li>
  <li><strong>Geographic Novelty:</strong> The IP address and cellular location originate from a state where Vikram has never transacted.</li>
  <li><strong>Time of Day:</strong> The purchase is taking place in the middle of the night (overnight hours).</li>
</ul>

<h3>Step 4: How It Makes Decisions (The Probability and Policy Ladder)</h3>
<p>
  The 15 numbers are passed to the trained LightGBM machine learning model. The model outputs a fraud probability of <strong>0.9997 (99.97%)</strong>.
</p>
<p>
  Next, the system passes <code>(probability=0.9997, amount=45000)</code> to its transparent 5-rule policy table:
</p>
<ul>
  <li>Rule 1 checks: <em>Is probability &ge; 0.80?</em> <strong>YES.</strong></li>
  <li>The rule fires immediately: <code>CRITICAL_BLOCK</code>.</li>
  <li>Recommended action: <code>BLOCK</code>.</li>
</ul>

<h3>Step 5: The Output Produced</h3>
<p>
  MerchantShield AI generates a comprehensive, transparent report:
</p>
<ul>
  <li><strong>Action:</strong> <code>BLOCK</code></li>
  <li><strong>Risk Score:</strong> <code>100 / 100 (CRITICAL)</code></li>
  <li><strong>Grounded Explanation:</strong> <em>"Why this transaction was flagged: Transaction amount is 85.7x the customer's historical average amount, which increased risk; Device has not been seen previously for this customer, which increased risk; Geographic location is new for this customer, which increased risk."</em></li>
</ul>

<h3>Step 6: What Happens Next</h3>
<p>
  Because the recommendation is <code>BLOCK</code>, the payment gateway halts the transaction before money moves. The attacker is stopped cold. Simultaneously, Ananya's dashboard logs the incident in its audit trail, and an automated SMS is sent to the real Vikram: <em>"Did you just attempt a ₹45,000 purchase? If not, please secure your card."</em> Ananya ships zero goods, loses zero rupees, and avoids a ₹1,500 bank penalty.
</p>

<h3>Step 7: When Something Goes Wrong (Fail-Safe Behavior)</h3>
<p>
  What happens if the database disk is full or the explanation module encounters a rare glitch?
</p>
<p>
  MerchantShield AI is built with <strong>defensive isolation</strong>: the policy decision is calculated <em>before</em> the explanation is built and <em>before</em> the database is touched. Even if the SQLite audit log fails to save to disk, the API still returns the correct <code>BLOCK</code> decision to the checkout page, logging an internal warning (<code>audit_persisted: false</code>). The store's security is never compromised by an ancillary bookkeeping glitch!
</p>

<h2 id="sec-3-5">3.5 Mapping Everyday Concepts to Real Code Components</h2>
<p>
  The table below connects every character, event, and decision in Ananya's story to the exact software components and source files in the MerchantShield AI repository:
</p>
<table>
  <thead>
    <tr>
      <th>Story Concept</th>
      <th>Meaning in Everyday Analogy</th>
      <th>Technical Software Concept</th>
      <th>Actual Source Code File</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>The Checkout Envelope</strong></td>
      <td>The order details and Vikram's past receipts passed to the risk manager.</td>
      <td>Validated Pydantic Request Model with historical context.</td>
      <td><code>backend/schemas/transaction.py</code> (<code>RiskRequest</code>)</td>
    </tr>
    <tr>
      <td><strong>The Behavioral Memory</strong></td>
      <td>Comparing the new saree order to Vikram's past spending and familiar devices.</td>
      <td>15 strictly-prior expanding statistical features.</td>
      <td><code>ml/features/build_features.py</code> (<code>build_features()</code>)</td>
    </tr>
    <tr>
      <td><strong>Sanity Inspection</strong></td>
      <td>Checking that the order doesn't contain nonsensical or corrupt data.</td>
      <td>Feature bounds and non-finite NaN/Inf validation.</td>
      <td><code>backend/services/risk_service.py</code> (<code>_validate_engineered_features()</code>)</td>
    </tr>
    <tr>
      <td><strong>The Mathematical Judge</strong></td>
      <td>Estimating the exact statistical likelihood that the order is stolen.</td>
      <td>Frozen gradient-boosted decision tree inference.</td>
      <td><code>ml/models/candidate_lgbm_v1.pkl</code> via <code>predict_proba()</code></td>
    </tr>
    <tr>
      <td><strong>The Explanatory Evidence</strong></td>
      <td>Proving exactly which facts (amount, device, location) pushed the score up.</td>
      <td>Exact Shapley Additive exPlanations with additivity verification.</td>
      <td><code>ml/evaluation/explainability.py</code> (<code>RiskExplainer</code>)</td>
    </tr>
    <tr>
      <td><strong>The Risk Thermometer</strong></td>
      <td>Translating the probability into a familiar 0–100 score for Ananya's eyes.</td>
      <td>Deterministic linear mapping and categorical bucketing.</td>
      <td><code>ml/evaluation/risk_scoring.py</code> (<code>score_transaction()</code>)</td>
    </tr>
    <tr>
      <td><strong>The Rulebook</strong></td>
      <td>The five clear guidelines that say when to allow, step-up, or block.</td>
      <td>Ordered policy cascade evaluated on <code>(probability, amount)</code>.</td>
      <td><code>ml/evaluation/policy.py</code> (<code>POLICY_RULES</code>)</td>
    </tr>
    <tr>
      <td><strong>The Permanent Ledger</strong></td>
      <td>The secure filing cabinet recording every decision without storing personal data.</td>
      <td>SQLAlchemy SQLite store persisting decision facts without PII.</td>
      <td><code>backend/services/audit_service.py</code> (<code>AuditStore</code>)</td>
    </tr>
    <tr>
      <td><strong>Ananya's Dashboard</strong></td>
      <td>The screen where Ananya reviews transactions, reasons, and audit logs.</td>
      <td>React 19 single-page application speaking HTTP/JSON.</td>
      <td><code>frontend/src/App.jsx</code></td>
    </tr>
  </tbody>
</table>
'''
