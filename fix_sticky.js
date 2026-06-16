const fs = require('fs');
const files = ['index.html', 'about.html', 'volunteer.html', 'request-help.html', 'celebrate.html'];

for (let file of files) {
    let content = fs.readFileSync(file, 'utf8');
    
    // First, remove the old sticky from nav
    content = content.replace(/<nav class="sticky top-10 (w-full z-50 glass shadow-sm transition-all duration-300)" id="navbar">/, '<nav class="$1" id="navbar">');
    
    // Also handle if I had changed z-index or something. Let's just do a more robust replace for nav:
    content = content.replace(/<nav class="sticky top-10 w-full z-50 glass shadow-sm transition-all duration-300" id="navbar">/g, '<nav class="w-full glass shadow-sm transition-all duration-300 relative z-50" id="navbar">');
    
    // Now wrap both in a sticky container
    // Find the emergency alert bar
    const alertStart = '<!-- Emergency Alert Bar -->';
    if(content.includes('<div class="sticky top-0 z-[60] w-full flex-col">')) {
        console.log("Already wrapped", file);
        continue;
    }
    
    content = content.replace(alertStart, '<div class="sticky top-0 z-[60] w-full flex flex-col">\n    ' + alertStart);
    
    // Find the end of nav
    const navEnd = '</nav>';
    // We want to replace the FIRST </nav> with </nav>\n    </div>
    let navEndIndex = content.indexOf(navEnd);
    if (navEndIndex !== -1) {
        content = content.slice(0, navEndIndex + navEnd.length) + '\n    </div>' + content.slice(navEndIndex + navEnd.length);
    }
    
    // Also remove the sticky top-0 from the emergency alert bar itself, since the wrapper is sticky now
    content = content.replace('sticky top-0 z-[60] justify-center', 'justify-center');
    
    // Ensure the alert logic handles hide correctly: it should set display: none in JS too
    // Wait, let's also update the JS to explicitly hide it if it's "off" (even though it defaults to none)
    content = content.replace("alertBar.style.display = 'flex';", "alertBar.style.display = 'flex';\n                    } else {\n                        alertBar.style.display = 'none';");
    
    fs.writeFileSync(file, content);
    console.log("Updated", file);
}
