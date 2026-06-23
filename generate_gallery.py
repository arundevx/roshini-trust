import os
import glob
import re

proj_dir = '/home/arun/Documents/projects/roshinitrust'
img_dir = os.path.join(proj_dir, 'images', 'gallery')

# 1. Get all WhatsApp images
images = []
for file in sorted(os.listdir(img_dir)):
    if file.startswith('WhatsApp Image') or file.endswith(('.jpg', '.jpeg', '.png')):
        images.append(file)

print(f"Found {len(images)} WhatsApp images.")

# 2. Add Gallery to Navbars in all HTML files
html_files = glob.glob(os.path.join(proj_dir, '*.html'))

for file_path in html_files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Desktop Nav Insertion
    desktop_pattern = r'(<a href="request-help.html" class="text-(?:gray-600|primary)[^>]+>Request Help</a>)'
    if 'gallery.html' not in content:
        # Find exactly how the request-help link is styled to copy it (just for the structure, we will force inactive color for now)
        replacement_desktop = r'<a href="gallery.html" class="text-gray-600 hover:text-primary transition-colors font-medium">Gallery</a>\n                        \g<1>'
        content = re.sub(desktop_pattern, replacement_desktop, content)
        
    # Mobile Nav Insertion
    mobile_pattern = r'(<a href="request-help.html" class="block px-3 py-3[^>]+>Request Help</a>)'
    if 'gallery.html"' not in content or len(re.findall('gallery.html', content)) < 2:
        replacement_mobile = r'<a href="gallery.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-700 hover:text-primary hover:bg-gray-50">Gallery</a>\n                    \g<1>'
        content = re.sub(mobile_pattern, replacement_mobile, content)
        
    # Also add Gallery to Footer Quick Links
    footer_pattern = r'(<li><a href="request-help.html" class="text-gray-400[^>]+>Request Help</a></li>)'
    if 'gallery.html' not in content or len(re.findall('gallery.html', content)) < 3:
         replacement_footer = r'<li><a href="gallery.html" class="text-gray-400 hover:text-primary transition-colors">Gallery</a></li>\n                        \g<1>'
         content = re.sub(footer_pattern, replacement_footer, content)

    with open(file_path, 'w') as f:
        f.write(content)

print("Updated navigation menus.")

# 3. Create gallery.html based on index.html
with open(os.path.join(proj_dir, 'index.html'), 'r') as f:
    index_content = f.read()

# Extract header (up to the end of <nav> div)
nav_end = index_content.find('</nav>') + 6
header_part = index_content[:nav_end]
# Find the next closing div which closes the sticky header div
header_end = index_content.find('</div>', nav_end) + 6
header = index_content[:header_end]

# Extract footer (from <footer> to the end)
footer_start = index_content.find('<footer')
footer = index_content[footer_start:]

# Modify title and active links for gallery.html
header = header.replace('<title>Roshini Charitable Trust | Connect with Love</title>', '<title>Gallery | Roshini Charitable Trust</title>')
header = header.replace('<meta name="description" content="Roshini Charitable Trust - Connect with Love. Your Small Step, Their Big Smile. Helping those forgotten by society In all over tamilnadu.">', '<meta name="description" content="Explore the gallery of Roshini Charitable Trust. See our impact, food distributions, and tree plantations In all over tamilnadu.">')

# Make Home inactive
header = header.replace('<a href="index.html" class="text-primary font-bold">Home</a>', '<a href="index.html" class="text-gray-600 hover:text-primary transition-colors font-medium">Home</a>')
header = header.replace('<a href="index.html"\n                        class="block px-3 py-3 rounded-md text-base font-bold text-primary bg-primary/10">Home</a>', '<a href="index.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-700 hover:text-primary hover:bg-gray-50">Home</a>')

# Make Gallery active
header = header.replace('<a href="gallery.html" class="text-gray-600 hover:text-primary transition-colors font-medium">Gallery</a>', '<a href="gallery.html" class="text-primary font-bold">Gallery</a>')
header = header.replace('<a href="gallery.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-700 hover:text-primary hover:bg-gray-50">Gallery</a>', '<a href="gallery.html"\n                        class="block px-3 py-3 rounded-md text-base font-bold text-primary bg-primary/10">Gallery</a>')

# Generate Gallery Section
gallery_html = """
    <!-- Header Section -->
    <section class="relative pt-24 pb-16 bg-white overflow-hidden border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
            <span class="inline-block py-1 px-3 rounded-full bg-primary/10 text-primary border border-primary/20 font-semibold text-sm mb-4 uppercase tracking-wider">Our Impact</span>
            <h1 class="text-4xl md:text-6xl font-extrabold text-gray-900 tracking-tight">Image <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-green-600">Gallery</span></h1>
            <p class="text-lg text-gray-600 mt-4 max-w-2xl mx-auto">Glimpses of our daily activities, food distribution, and community support In all over tamilnadu.</p>
        </div>
    </section>

    <!-- Gallery Grid -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="columns-1 sm:columns-2 md:columns-3 lg:columns-4 gap-4 space-y-4">
"""

for img in images:
    gallery_html += f"""                <div class="break-inside-avoid overflow-hidden rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 group bg-white border border-gray-100">
                    <img src="images/gallery/{img}" alt="Gallery Image" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
                </div>\n"""

gallery_html += """            </div>
        </div>
    </section>
"""

# Write to gallery.html
with open(os.path.join(proj_dir, 'gallery.html'), 'w') as f:
    f.write(header + gallery_html + footer)

print("Created gallery.html.")
