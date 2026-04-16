#!/usr/bin/env python3
"""
Update EDF shopping list with corrected parts based on verification
Replaces undersized components with properly rated alternatives
"""

with open('index.html', 'r') as f:
    html = f.read()

# 1. Replace 10 AWG wire with 6 AWG wire
old_wire = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">🧵</td>
                            <td>1</td>
                            <td>BNTECHGO 10 AWG Silicone Wire</td>
                            <td>High-current power cables (25ft red/black)</td>
                            <td>$40</td>
                            <td><a href="https://www.amazon.com/BNTECHGO-Silicone-Flexible-Strands-Stranded/dp/B01ABOPO2S" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

new_wire = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">🧵</td>
                            <td>1</td>
                            <td>6 AWG Silicone Wire (25ft)</td>
                            <td>High-current power cables (rated 101A continuous)</td>
                            <td>$70</td>
                            <td><a href="https://www.amazon.com/Shirbly-Battery-Automotive-Generator-Standard/dp/B0CDLMWB1L" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

html = html.replace(old_wire, new_wire)

# 2. Replace XT90 with XT120 connectors
old_xt90 = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">🔗</td>
                            <td>1</td>
                            <td>XT90 Connectors (5 pairs)</td>
                            <td>EDF to ESC connections</td>
                            <td>$15</td>
                            <td><a href="https://www.amazon.com/MADCATZ-Connectors-High-Temp-Gold-Plated-Battery/dp/B0F8VLN34V" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

new_xt120 = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">🔗</td>
                            <td>1</td>
                            <td>XT120 Connectors (5 pairs)</td>
                            <td>EDF to ESC connections (rated 120A continuous)</td>
                            <td>$18</td>
                            <td><a href="https://www.amazon.com/XT120-Current-Battery-Connector-Sheathed/dp/B0BWGWNWYM" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

html = html.replace(old_xt90, new_xt120)

# 3. Replace 4mm bullets with 5.5mm bullets
old_4mm = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">📍</td>
                            <td>1</td>
                            <td>4mm Bullet Connectors</td>
                            <td>Motor to ESC connections</td>
                            <td>$12</td>
                            <td><a href="https://www.amazon.com/FLY-RC-Bullet-Connector-Battery/dp/B07CSQH2QC" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

new_5_5mm = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">📍</td>
                            <td>1</td>
                            <td>5.5mm Bullet Connectors (10 pairs)</td>
                            <td>Motor to ESC connections (rated 100A+)</td>
                            <td>$15</td>
                            <td><a href="https://www.amazon.com/Female-Banana-Bullet-Connector-Battery/dp/B07YZMTWDC" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

html = html.replace(old_4mm, new_5_5mm)

# 4. Replace Kill-A-Watt with DC watt meter
old_kilawatt = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">📊</td>
                            <td>1</td>
                            <td>Kill-A-Watt Power Meter</td>
                            <td>Electricity usage monitoring</td>
                            <td>$25</td>
                            <td><a href="https://www.amazon.com/P3-International-P4460-Electricity-Monitor/dp/B000RGF29Q" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

new_dc_meter = '''                        <tr>
                            <td style="text-align: center; font-size: 2em;">📊</td>
                            <td>1</td>
                            <td>DC Power Analyzer (0-200A, 0-60V)</td>
                            <td>Measures wattage, voltage, amperage at battery</td>
                            <td>$35</td>
                            <td><a href="https://www.amazon.com/HTRC-Precision-Analyzer-Measuring-Voltage/dp/B07GB71YSB" target="_blank" class="shop-link">View on Amazon</a></td>
                        </tr>'''

html = html.replace(old_kilawatt, new_dc_meter)

# Update subtotals
# Wiring & Connectors: $122-127 → $150-158 (wire +$30, XT120 +$3, bullets +$3)
old_wiring_total = '''                        <tr>
                            <td colspan="4"><strong>Wiring & Connectors Subtotal</strong></td>
                            <td><strong>$122-127</strong></td>
                            <td></td>
                        </tr>'''

new_wiring_total = '''                        <tr>
                            <td colspan="4"><strong>Wiring & Connectors Subtotal</strong></td>
                            <td><strong>$158-163</strong></td>
                            <td></td>
                        </tr>'''

html = html.replace(old_wiring_total, new_wiring_total)

# Tools & Testing: $80 → $90 (DC meter +$10)
old_tools_total = '''                        <tr>
                            <td colspan="4"><strong>Tools & Testing Subtotal</strong></td>
                            <td><strong>$80</strong></td>
                            <td></td>
                        </tr>'''

new_tools_total = '''                        <tr>
                            <td colspan="4"><strong>Tools & Testing Subtotal</strong></td>
                            <td><strong>$90</strong></td>
                            <td></td>
                        </tr>'''

html = html.replace(old_tools_total, new_tools_total)

# Update grand total: $535-574 → $581-620 (+$46)
old_grand_total = '''                    <h2 style="margin-bottom: 10px;">💰 Total Amazon Shopping List</h2>
                    <p style="color: #666; margin-bottom: 30px;">All electronics and tools needed for EDF prototype testing</p>
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
                        <h3 style="margin-bottom: 15px; font-size: 1.8em;">Complete Parts Cost</h3>
                        <div style="font-size: 3em; font-weight: bold; margin: 20px 0;">$535 - $574</div>'''

new_grand_total = '''                    <h2 style="margin-bottom: 10px;">💰 Total Amazon Shopping List</h2>
                    <p style="color: #666; margin-bottom: 30px;">All electronics and tools needed for EDF prototype testing (upgraded components)</p>
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
                        <h3 style="margin-bottom: 15px; font-size: 1.8em;">Complete Parts Cost</h3>
                        <div style="font-size: 3em; font-weight: bold; margin: 20px 0;">$581 - $620</div>'''

html = html.replace(old_grand_total, new_grand_total)

# Add upgrade note
old_note_section = '''                        <p style="margin-top: 20px; font-size: 0.9em; opacity: 0.9;">
                            <strong>📦 Note:</strong> All items available via Amazon Prime for fast shipping. Prices approximate and subject to change.
                        </p>'''

new_note_section = '''                        <p style="margin-top: 20px; font-size: 0.9em; opacity: 0.9;">
                            <strong>✅ Upgraded Components:</strong> Wire upgraded to 6 AWG (101A rating), connectors upgraded to XT120 (120A) and 5.5mm bullets (100A+), DC power meter supports full 9kW testing
                        </p>
                        <p style="margin-top: 10px; font-size: 0.9em; opacity: 0.9;">
                            <strong>📦 Note:</strong> All items available via Amazon Prime for fast shipping. Prices approximate and subject to change.
                        </p>'''

html = html.replace(old_note_section, new_note_section)

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Updated EDF shopping list with verified parts!")
print("\nUpgrades Applied:")
print("  1. 🧵 10 AWG wire → 6 AWG wire ($40 → $70)")
print("     Reason: 10 AWG only rated 55A, need 101A for 94A draw")
print("\n  2. 🔗 XT90 → XT120 connectors ($15 → $18)")
print("     Reason: XT90 rated 90A, 94A draw = 4% over spec")
print("\n  3. 📍 4mm → 5.5mm bullet connectors ($12 → $15)")
print("     Reason: 4mm rated 60-80A, need 100A+ for 94A draw")
print("\n  4. 📊 Kill-A-Watt → DC Power Analyzer ($25 → $35)")
print("     Reason: Kill-A-Watt max 1,875W, need to measure 9,000W")
print("\nCost Impact:")
print("  • Wiring & Connectors: $122-127 → $158-163 (+$36)")
print("  • Tools & Testing: $80 → $90 (+$10)")
print("  • Total: $535-574 → $581-620 (+$46)")
print("\n⚠️  Additional $46 investment ensures safe operation at full power!")
