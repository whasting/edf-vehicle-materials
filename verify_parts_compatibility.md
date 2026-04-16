# EDF Prototype Parts Verification

## System Requirements
- **2× JP Hobby 120mm EDFs**
- **Per EDF:** 4,500W @ 100% throttle (94A @ 48V)
- **Both EDFs:** 9,000W combined
- **Voltage:** 48V DC system
- **Current per EDF:** Up to 100A continuous

---

## ESCs & Control Systems

### ✅ 1. ESC Controllers (2 needed)
**Link:** https://www.amazon.com/Creations-Brushless-Supports-Programmable-Helicopters/dp/B0GQ9PNTLD

**Product:** Castle Creations Phoenix Edge (Based on URL pattern)

**Requirements:**
- Continuous current: ≥94A per ESC
- Voltage range: Compatible with 48V (10-12S LiPo)
- Power handling: ≥4,500W

**Typical Castle Phoenix Edge Specs:**
- **120A ESC:** 120A continuous, 10-12S LiPo (37-50.4V)
- **Voltage:** ✅ 48V compatible (within 10-12S range)
- **Current:** ✅ 120A > 94A required
- **Power:** ✅ 120A × 48V = 5,760W > 4,500W needed

**Verification:** ✅ **COMPATIBLE** - Adequate current rating with 20% safety margin

**Concerns:**
- ⚠️ Verify this is the 120A model specifically
- ⚠️ Price seems low for Castle Phoenix Edge (~$160 each vs typical $300)
- May be clone/alternative brand, not genuine Castle

---

### ⚠️ 2. PWM Controller
**Link:** https://www.amazon.com/Regulator-Control-Brushless-Aeromodelling-Controller/dp/B0DFTHDZ92

**Product:** PWM Servo Tester / Speed Controller

**Requirements:**
- Output: PWM signal (50Hz, 1-2ms pulse width)
- Channels: 1 (can control both ESCs in parallel)
- Power: Low voltage (5V signal)

**Typical RC PWM Controller Specs:**
- PWM output: 50Hz, 1000-2000μs
- Control: Potentiometer knob
- Power: 5-6V input

**Verification:** ✅ **LIKELY COMPATIBLE**

**Concerns:**
- ⚠️ Verify it outputs standard RC PWM signal (not analog voltage)
- ⚠️ Some "speed controllers" are actual ESCs, not PWM generators
- Need to confirm this is a servo tester / signal generator

**Alternative if incompatible:**
- Standard RC servo tester: $10-15
- Arduino-based PWM generator: $15-20

---

### ✅ 3. Servo Extension Cables (3ft)
**Link:** https://www.amazon.com/BackBayRC-Twisted-Extension-Vehicles-Bikes/dp/B0D38DDTQX

**Product:** BackBayRC Servo Extension Cables

**Requirements:**
- Length: ≥3ft (cabin to roof)
- Type: Standard RC servo connector (JR/Futaba)
- Signal: Carries PWM signal (low voltage, low current)

**Typical Specs:**
- 22-26 AWG wire (sufficient for signal, not power)
- Twisted pair for noise reduction
- 3-pin connector (signal, +5V, ground)

**Verification:** ✅ **COMPATIBLE** - Standard RC servo extension

**Notes:**
- These carry signal only, not high current
- 3ft may be short - measure roof to cabin distance
- Consider 6ft cables if needed

---

### ✅ 4. Emergency Stop Button
**Link:** https://www.amazon.com/GUETNEU-Waterproof-Emergency-Momentary-Transparent/dp/B0CR19ZTBJ

**Product:** GUETNEU Waterproof Emergency Stop Button (Momentary)

**Requirements:**
- Type: Momentary (press to cut power)
- Rating: Handle low-current signal (not main power)
- Waterproof: Desirable for outdoor use

**Typical Specs:**
- Momentary contact (normally open or normally closed)
- Signal voltage: 12V capable
- Current: 1-5A (signal use only)

**Verification:** ✅ **COMPATIBLE**

**Implementation:**
- Wire into PWM signal line (cuts signal to ESCs)
- Or wire to ESC arming circuit
- NOT wired into main 48V power line (too much current)

**Note:** Emergency stop should cut ESC signal, not main power

---

## Wiring & Connectors

### ⚠️ 5. BNTECHGO 10 AWG Silicone Wire
**Link:** https://www.amazon.com/BNTECHGO-Silicone-Flexible-Strands-Stranded/dp/B01ABOPO2S

**Requirements:**
- Wire gauge: 10 AWG minimum for 94A continuous
- Temperature rating: ≥150°C (silicone insulation)
- Length: 25ft (red/black pair)

**10 AWG Wire Specs:**
- **Max continuous current:** 40A (chassis wiring) / 55A (power transmission)
- Temperature: 200°C (silicone insulation)

**Current per EDF:** 94A

**Verification:** ❌ **UNDERSIZED FOR MAIN POWER**

**Analysis:**
- 10 AWG rated for 40-55A continuous
- Your EDFs draw 94A each
- **Need 6 AWG or 8 AWG for 94A loads**

**Wire Gauge Recommendations:**
- **6 AWG:** 101A continuous (✅ adequate)
- **8 AWG:** 73A continuous (⚠️ marginal, would run hot)
- **10 AWG:** 55A continuous (❌ insufficient)

**Verdict:** ❌ **REPLACE WITH 6 AWG OR 8 AWG WIRE**

**Alternative:**
- BNTECHGO 6 AWG Silicone Wire: ~$60-80 for 25ft
- Or run 2× 10 AWG in parallel per polarity (doubles capacity to 110A)

---

### ✅ 6. XT90 Connectors
**Link:** https://www.amazon.com/MADCATZ-Connectors-High-Temp-Gold-Plated-Battery/dp/B0F8VLN34V

**Product:** XT90 Connectors (5 pairs)

**Requirements:**
- Current rating: ≥94A continuous per connector
- Connections: Battery→ESC, ESC→EDF

**XT90 Specs:**
- **Continuous:** 90A rated
- **Burst:** 120A for 30 seconds
- Voltage: Up to 60V

**Your usage:** 94A continuous

**Verification:** ⚠️ **MARGINAL**

**Analysis:**
- XT90 rated for 90A continuous
- Your EDFs draw 94A (4% over rating)
- Will work but run warm
- Consider XT120 or QS8 connectors for safety margin

**Verdict:** ⚠️ **ACCEPTABLE but consider upgrade**

**Better alternatives:**
- **XT120:** 120A continuous (✅ 27% margin)
- **QS8-S (8mm bullets):** 150A+ continuous (✅ 60% margin)
- **Anderson Powerpole 75A:** 75A per contact, 2-contact = 150A

---

### ❌ 7. Anderson Powerpole 45A (Listed as "Assortment")
**Link:** https://www.amazon.com/Relaxweex-Connectors-Assortment-Disconnect-Terminals/dp/B0GHNRXHH1

**Product:** Connector Assortment (may include Powerpole-style)

**Requirements:**
- Current: ≥94A (if used for main power)
- Or ≥40A (if used for battery→inverter only)

**Anderson Powerpole 45A Specs:**
- **Continuous:** 45A per pair
- Can stack multiple pairs for higher current

**Verification:** ❌ **INSUFFICIENT for main EDF power**

**Analysis:**
- 45A << 94A required
- Would need 3 pairs in parallel (3 × 45A = 135A)
- Suitable for lower-current connections only

**Verdict:**
- ✅ OK for battery→inverter (if inverter draws <45A on DC side)
- ❌ NOT OK for battery→ESC or ESC→EDF connections

---

### ⚠️ 8. 4mm Bullet Connectors
**Link:** https://www.amazon.com/FLY-RC-Bullet-Connector-Battery/dp/B07CSQH2QC

**Product:** 4mm Gold Bullet Connectors

**Requirements:**
- Motor→ESC connections (3 wires per motor)
- Current: 94A continuous

**4mm Bullet Connector Specs:**
- **Continuous:** 60-80A (varies by quality)
- Voltage: Up to 60V
- Typical use: RC motors up to 3,500W

**Your usage:** 94A per phase wire

**Verification:** ⚠️ **MARGINAL**

**Analysis:**
- 4mm bullets typically rated 60-80A
- Your motors draw 94A (18-57% over rating)
- Will get warm but should work
- **5.5mm or 6mm bullets recommended** (120A+ rating)

**Verdict:** ⚠️ **Will work but not ideal**

**Better alternatives:**
- **5.5mm bullets:** 100A+ continuous
- **6mm bullets:** 120A+ continuous
- **8mm bullets (QS8):** 150A+ continuous

---

### ✅ 9. 100A Inline Fuse Holders
**Link:** https://www.amazon.com/BOJACK-Plated-Inline-Automotive-Protection/dp/B0B7VW4Y9X

**Product:** BOJACK 100A Inline Fuse Holders

**Requirements:**
- Rating: ≥94A per EDF circuit
- Type: ANL or MIDI fuse preferred
- Voltage: 48V compatible

**Typical 100A Inline Fuse Holder:**
- Current: 100A continuous
- Fuse type: ATC/ATO or ANL style
- Voltage: 12-48V

**Verification:** ✅ **ADEQUATE**

**Analysis:**
- 100A rating > 94A draw (6% margin)
- Small margin but acceptable
- Use 100A slow-blow fuses (handle startup surge)

**Recommended fuse values:**
- **100A slow-blow** for each EDF circuit
- **200A slow-blow** for main battery output (both EDFs)

**Verdict:** ✅ **COMPATIBLE**

---

### ✅ 10. Heat Shrink Tubing Kit (650pcs)
**Link:** https://www.amazon.com/650pcs-Shrink-Tubing-innhom-Approved/dp/B07WWWPR2X

**Product:** Heat Shrink Tubing Assortment

**Requirements:**
- Sizes: Various (to cover wire splices and connectors)
- Material: Polyolefin or similar
- Shrink ratio: 2:1 or 3:1

**Verification:** ✅ **COMPATIBLE**

**Notes:**
- Ensure kit includes larger sizes for 6-10 AWG wires
- Need 3/8" or 1/2" diameter for main power connections
- Smaller sizes OK for signal wires

---

## Tools & Testing Equipment

### ✅ 11. Helping Hands with Magnifier
**Link:** https://www.amazon.com/Neiko-01902-Adjustable-Magnifying-Alligator/dp/B000P42O3C

**Verification:** ✅ **USEFUL** - Standard soldering helper

---

### ✅ 12. Cable Ties
**Link:** https://www.amazon.com/HAVE-ME-TD-Cable-Ties/dp/B08TVLYB3Q

**Verification:** ✅ **ESSENTIAL** - Cable management

**Recommendation:** Get UV-resistant for outdoor use

---

### ✅ 13. Digital Fish Scale (100lb)
**Link:** https://www.amazon.com/Fishfun-Digital-Hanging-Fishing-Compound/dp/B072SVHZLC

**Requirements:**
- Range: 0-100 lbs (need to measure 33 lbs max thrust)
- Accuracy: ±1 lb acceptable

**Verification:** ✅ **ADEQUATE** for thrust testing

**Usage:** Measure EDF thrust on test bench

---

### ✅ 14. Infrared Thermometer
**Link:** https://www.amazon.com/Etekcity-Thermometer-774-Temperature-Accessories/dp/B0B71HFH9K

**Requirements:**
- Range: Up to 200°C (check wire/connector temperatures)
- Accuracy: ±2°C

**Verification:** ✅ **ESSENTIAL** - Safety monitoring

**Usage:**
- Monitor ESC temperatures (shouldn't exceed 80°C)
- Check wire connections for hot spots
- Verify motor temperatures

---

### ⚠️ 15. Kill-A-Watt Power Meter
**Link:** https://www.amazon.com/P3-International-P4460-Electricity-Monitor/dp/B000RGF29Q

**Product:** P3 Kill-A-Watt (P4460)

**Requirements:**
- Measure AC power input to inverter or Jackery
- Range: Up to 9,000W

**Kill-A-Watt Specs:**
- **Max power:** 1,875W (15A × 125V)
- Voltage: 125V AC
- Current: 15A max

**Your usage:** 9,000W at full power (72A @ 125V AC)

**Verification:** ❌ **INSUFFICIENT for full power testing**

**Analysis:**
- Kill-A-Watt maxes at 1,875W
- Your system draws up to 9,000W
- **Will damage the meter**

**Alternatives:**
- **Clamp meter** (measures AC current up to 200A): $40-60
- **AC power meter 30A** (3,750W @ 125V): $80-120
- **DC watt meter** (measure at 48V DC before inverter): $30-50

**Verdict:** ❌ **REPLACE with higher-capacity meter**

**Recommended:**
- **DC Power Analyzer (48V, 200A):** Measure at battery terminals
- Example: Turnigy 200A Watt Meter (~$25-40)

---

## Summary: Pass/Fail Analysis

### ✅ COMPATIBLE (Use as-is):
1. ✅ ESC Controllers (verify 120A rating)
2. ✅ Servo Extension Cables
3. ✅ Emergency Stop Button
4. ✅ Heat Shrink Tubing
5. ✅ 100A Fuse Holders
6. ✅ Helping Hands
7. ✅ Cable Ties
8. ✅ Digital Scale
9. ✅ IR Thermometer

### ⚠️ MARGINAL (Will work but not ideal):
1. ⚠️ PWM Controller (verify it's a servo tester, not ESC)
2. ⚠️ XT90 Connectors (4% over rating, consider XT120)
3. ⚠️ 4mm Bullet Connectors (consider 5.5mm or 6mm)

### ❌ INCOMPATIBLE (Replace):
1. ❌ **10 AWG Wire** → Replace with **6 AWG or 8 AWG**
2. ❌ **Anderson Powerpole 45A** → Only use for low-current connections
3. ❌ **Kill-A-Watt Meter** → Replace with DC watt meter or high-current AC meter

---

## Critical Upgrades Needed

### 1. WIRE GAUGE (Critical Safety Issue)
**Problem:** 10 AWG can't handle 94A continuous
**Solution:**
- **Option A:** Buy 6 AWG silicone wire (~$70 for 25ft)
- **Option B:** Run 2× 10 AWG in parallel (use existing wire)

### 2. POWER METER (Can't measure full system)
**Problem:** Kill-A-Watt maxes at 1,875W (you need 9,000W)
**Solution:**
- **DC Watt Meter** (48V, 200A): $30-50
  - Measures at battery terminals (before inverter)
  - More accurate for your use case
  - Example: Turnigy 200A, RC Watt Meter

### 3. CONSIDER CONNECTOR UPGRADES (Safety margin)
**XT90 → XT120:**
- Current: 90A → 120A (27% safety margin)
- Cost: +$5-10 for set

**4mm bullets → 5.5mm bullets:**
- Current: 60-80A → 100-120A
- Cost: +$8-12

---

## Recommended Shopping List Changes

### Replace:
1. ❌ BNTECHGO 10 AWG Wire
   - ✅ **BNTECHGO 6 AWG Silicone Wire** (~$70)
   - Link: https://www.amazon.com/dp/B01KQ4PH8E

2. ❌ Kill-A-Watt P4460
   - ✅ **DC Watt Meter 200A** (~$35)
   - Link: https://www.amazon.com/dp/B07JKFS4KT (or similar)

### Upgrade (Optional but recommended):
3. ⚠️ XT90 Connectors
   - ✅ **XT120 Connectors** (~$18 for 5 pairs)

4. ⚠️ 4mm Bullet Connectors
   - ✅ **5.5mm or 6mm Bullet Connectors** (~$15)

---

## Bottom Line

**6 out of 15 parts need attention:**
- **2 critical failures** (wire gauge, power meter)
- **3 marginal items** (connectors slightly undersized)
- **1 needs verification** (PWM controller type)

**Total additional cost for fixes:** ~$105-140
- 6 AWG wire: $70
- DC watt meter: $35
- Optional connector upgrades: $0-35

**This is fixable** - the issues are mostly undersized wiring/connectors, which is common when adapting RC parts for high-power use. The core components (ESCs, control, tools) look good.
