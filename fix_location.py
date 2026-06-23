import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r') as file:
        content = file.read()
    
    # "in the sacred streets of Srirangam, Trichy" -> "in all over tamil nadu"
    content = content.replace('in the sacred streets of Srirangam, Trichy', 'in all over tamil nadu')
    
    # "in the sacred streets of Srirangam,\n                        Trichy"
    content = re.sub(r'in the sacred streets of Srirangam,\s*Trichy', 'in all over tamil nadu', content)
    
    # "Srirangam, Trichy City" -> "in all over tamil nadu"
    content = content.replace('Srirangam, Trichy City', 'in all over tamil nadu')
    
    # "Srirangam, Trichy" -> "in all over tamil nadu"
    content = content.replace('Srirangam, Trichy', 'in all over tamil nadu')
    
    # "in Trichy/Srirangam" -> "in all over tamil nadu"
    content = content.replace('in Trichy/Srirangam', 'in all over tamil nadu')
    
    # "on the streets of Trichy" -> "in all over tamil nadu"
    content = content.replace('on the streets of Trichy', 'in all over tamil nadu')
    
    # "across the Trichy\n                                region"
    content = re.sub(r'across the Trichy\s*region', 'in all over tamil nadu', content)
    
    # Meta tags: "NGO in Trichy, charity Srirangam"
    content = content.replace('NGO in Trichy, charity Srirangam', 'NGO in all over tamil nadu, charity in all over tamil nadu')
    
    # "focus on roadside food distribution in Srirangam" -> "focus on roadside food distribution in all over tamil nadu"
    content = content.replace('distribution in\n                                Srirangam', 'distribution in all over tamil nadu')

    with open(f, 'w') as file:
        file.write(content)
