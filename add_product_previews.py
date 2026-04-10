#!/usr/bin/env python3
"""
Add product preview icons to shopping list table
Since Amazon blocks image scraping, use relevant emojis/icons for each product type
"""

with open('index.html', 'r') as f:
    html = f.read()

# Add a "Preview" column header to ESCs & Control table
old_escs_header = '''                    <thead>
                        <tr>
                            <th>Qty</th>
                            <th>Item</th>
                            <th>Purpose</th>
                            <th>Est. Price</th>
                            <th>Link</th>
                        </tr>
                    </thead>'''

new_escs_header = '''                    <thead>
                        <tr>
                            <th>Preview</th>
                            <th>Qty</th>
                            <th>Item</th>
                            <th>Purpose</th>
                            <th>Est. Price</th>
                            <th>Link</th>
                        </tr>
                    </thead>'''

html = html.replace(old_escs_header, new_escs_header, 1)

# Update ESCs & Control products with icons
products_escs = [
    ('<td>2</td>\n                            <td>Castle Phoenix Edge 120 ESC</td>',
     '<td style="text-align: center; font-size: 2em;">⚡</td>\n                            <td>2</td>\n                            <td>Castle Phoenix Edge 120 ESC</td>'),

    ('<td>1</td>\n                            <td>PWM Controller</td>',
     '<td style="text-align: center; font-size: 2em;">🎛️</td>\n                            <td>1</td>\n                            <td>PWM Controller</td>'),

    ('<td>1</td>\n                            <td>Servo Extension Cables (3ft)</td>',
     '<td style="text-align: center; font-size: 2em;">🔌</td>\n                            <td>1</td>\n                            <td>Servo Extension Cables (3ft)</td>'),

    ('<td>1</td>\n                            <td>Emergency Stop Button</td>',
     '<td style="text-align: center; font-size: 2em;">🛑</td>\n                            <td>1</td>\n                            <td>Emergency Stop Button</td>'),
]

for old, new in products_escs:
    html = html.replace(old, new, 1)

# Update ESCs footer to span correct columns
html = html.replace(
    '<td colspan="3"><strong>ESCs & Control Subtotal</strong></td>',
    '<td colspan="4"><strong>ESCs & Control Subtotal</strong></td>',
    1
)

# Add preview column to Wiring & Connectors table (appears twice in the file)
# We need to update both occurrences
count = 0
while True:
    idx = html.find(old_escs_header, count)
    if idx == -1:
        break
    html = html[:idx] + new_escs_header + html[idx + len(old_escs_header):]
    count = idx + len(new_escs_header)

# Update Wiring & Connectors products with icons
products_wiring = [
    ('<td>1</td>\n                            <td>BNTECHGO 10 AWG Silicone Wire</td>',
     '<td style="text-align: center; font-size: 2em;">🧵</td>\n                            <td>1</td>\n                            <td>BNTECHGO 10 AWG Silicone Wire</td>'),

    ('<td>1</td>\n                            <td>XT90 Connectors (5 pairs)</td>',
     '<td style="text-align: center; font-size: 2em;">🔗</td>\n                            <td>1</td>\n                            <td>XT90 Connectors (5 pairs)</td>'),

    ('<td>1</td>\n                            <td>Anderson Powerpole 45A</td>',
     '<td style="text-align: center; font-size: 2em;">🔌</td>\n                            <td>1</td>\n                            <td>Anderson Powerpole 45A</td>'),

    ('<td>1</td>\n                            <td>4mm Bullet Connectors</td>',
     '<td style="text-align: center; font-size: 2em;">📍</td>\n                            <td>1</td>\n                            <td>4mm Bullet Connectors</td>'),

    ('<td>1</td>\n                            <td>100A Inline Fuse Holders</td>',
     '<td style="text-align: center; font-size: 2em;">🔒</td>\n                            <td>1</td>\n                            <td>100A Inline Fuse Holders</td>'),

    ('<td>1</td>\n                            <td>Heat Shrink Tubing Kit (650pcs)</td>',
     '<td style="text-align: center; font-size: 2em;">🎨</td>\n                            <td>1</td>\n                            <td>Heat Shrink Tubing Kit (650pcs)</td>'),
]

for old, new in products_wiring:
    html = html.replace(old, new, 1)

# Update Wiring footer
html = html.replace(
    '<td colspan="3"><strong>Wiring & Connectors Subtotal</strong></td>',
    '<td colspan="4"><strong>Wiring & Connectors Subtotal</strong></td>',
    1
)

# Update Tools & Testing products
products_tools = [
    ('<td>1</td>\n                            <td>Helping Hands with Magnifier</td>',
     '<td style="text-align: center; font-size: 2em;">🔧</td>\n                            <td>1</td>\n                            <td>Helping Hands with Magnifier</td>'),

    ('<td>1</td>\n                            <td>Cable Ties & Clamps</td>',
     '<td style="text-align: center; font-size: 2em;">📎</td>\n                            <td>1</td>\n                            <td>Cable Ties & Clamps</td>'),

    ('<td>1</td>\n                            <td>Digital Fish Scale (100lb)</td>',
     '<td style="text-align: center; font-size: 2em;">⚖️</td>\n                            <td>1</td>\n                            <td>Digital Fish Scale (100lb)</td>'),

    ('<td>1</td>\n                            <td>Infrared Thermometer</td>',
     '<td style="text-align: center; font-size: 2em;">🌡️</td>\n                            <td>1</td>\n                            <td>Infrared Thermometer</td>'),

    ('<td>1</td>\n                            <td>Kill-A-Watt Power Meter</td>',
     '<td style="text-align: center; font-size: 2em;">📊</td>\n                            <td>1</td>\n                            <td>Kill-A-Watt Power Meter</td>'),
]

for old, new in products_tools:
    html = html.replace(old, new, 1)

# Update Tools footer
html = html.replace(
    '<td colspan="3"><strong>Tools & Testing Subtotal</strong></td>',
    '<td colspan="4"><strong>Tools & Testing Subtotal</strong></td>',
    1
)

# Update table styling to accommodate preview column
old_table_style = '''        .shopping-table th, .shopping-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }'''

new_table_style = '''        .shopping-table th, .shopping-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        .shopping-table th:first-child, .shopping-table td:first-child {
            width: 80px;
            text-align: center;
        }'''

html = html.replace(old_table_style, new_table_style)

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Added product preview icons to shopping list!")
print("\nPreview Icons Added:")
print("  ESCs & Control:")
print("    ⚡ ESC Controllers")
print("    🎛️ PWM Controller")
print("    🔌 Extension Cables")
print("    🛑 Emergency Stop")
print("\n  Wiring & Connectors:")
print("    🧵 Silicone Wire")
print("    🔗 XT90 Connectors")
print("    🔌 Powerpole Connectors")
print("    📍 Bullet Connectors")
print("    🔒 Fuse Holders")
print("    🎨 Heat Shrink")
print("\n  Tools & Testing:")
print("    🔧 Helping Hands")
print("    📎 Cable Ties")
print("    ⚖️ Digital Scale")
print("    🌡️ Thermometer")
print("    📊 Power Meter")
