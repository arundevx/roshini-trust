import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Replace "trichy and srirangam" -> "In all over tamilnadu"
    content = content.replace('in Trichy and Srirangam', 'In all over tamilnadu')
    content = content.replace('Trichy and Srirangam', 'In all over tamilnadu')
    content = content.replace('in the Trichy and Srirangam regions', 'In all over tamilnadu')
    
    # 2. Replace favicon
    content = content.replace('images/rct-icon.png', 'images/logo.png')
    
    # 3. Replace logo "R" div with img
    pattern = r'<div\s*class="w-10 h-10 rounded-full bg-primary flex items-center justify-center text-white font-bold text-xl">\s*R\s*</div>'
    new_logo = r'<img src="images/logo.png" alt="Roshini Logo" class="w-14 h-14 md:w-16 md:h-16 rounded-full object-cover shadow-sm border border-gray-100">'
    content = re.sub(pattern, new_logo, content)

    # Specific fix for about.html (Women Empowerment Section)
    if f == 'about.html':
        target = r'    <!-- Our Journey Section -->'
        
        empowerment_section = """    <!-- Women Empowerment Section -->
    <section id="empowerment" class="py-24 bg-gray-50 border-t border-gray-100 mt-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-primary font-bold tracking-wider uppercase text-sm mb-2">Our Initiatives</h2>
                <h3 class="text-4xl font-bold text-gray-900 mb-6">Women Empowerment Programs</h3>
                <p class="text-lg text-gray-600">
                    Women empowerment programs are organized initiatives designed to improve the social, economic, and political status of women. They typically offer education, vocational training, micro-loans, and legal support to promote self-reliance, gender equality, and leadership opportunities. A variety of highly actionable and localized empowerment programs, entrepreneurship initiatives, and safety frameworks are available.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                <div class="bg-white rounded-3xl p-8 shadow-sm hover:shadow-xl transition-shadow border border-gray-100 group">
                    <div class="w-14 h-14 rounded-full bg-pink-100 text-pink-500 flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-hands-holding-child"></i>
                    </div>
                    <h4 class="text-2xl font-bold text-gray-900 mb-4">Rural Upliftment</h4>
                    <p class="text-gray-600 leading-relaxed">
                        It focuses on the upliftment of rural women and children through health, education, livelihood support, and environmental initiatives in the all over tamilnadu.
                    </p>
                </div>

                <div class="bg-white rounded-3xl p-8 shadow-sm hover:shadow-xl transition-shadow border border-gray-100 group">
                    <div class="w-14 h-14 rounded-full bg-purple-100 text-purple-500 flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-cut"></i>
                    </div>
                    <h4 class="text-2xl font-bold text-gray-900 mb-4">Livelihood & Skill Training</h4>
                    <p class="text-gray-600 leading-relaxed">
                        The NGO runs vocational training programs—such as skill-building in beauty care and tailoring—to promote economic sustainability for rural women. Vocational Training on Beauty Care for Women.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Our Journey Section -->"""
        content = content.replace(target, empowerment_section)
        
    with open(f, 'w') as file:
        file.write(content)
