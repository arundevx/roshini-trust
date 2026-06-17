const fs = require('fs');
const files = ['index.html', 'about.html', 'volunteer.html', 'request-help.html', 'celebrate.html'];

const oldFooterContact = `<li class="flex items-center gap-3 text-gray-400">
                            <i class="fas fa-phone text-primary"></i>
                            <span>+91 99444 70511, +91 82202 89504</span>
                        </li>`;

const newFooterContact = `<li class="flex items-center gap-3 text-gray-400">
                            <i class="fas fa-phone text-primary"></i>
                            <span>+91 99444 70511</span>
                        </li>
                        <li class="flex items-center gap-3 text-gray-400">
                            <i class="fas fa-phone text-primary"></i>
                            <span>+91 82202 89504</span>
                        </li>`;

for (const file of files) {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        content = content.replace(oldFooterContact, newFooterContact);
        fs.writeFileSync(file, content);
        console.log(`Updated footer in ${file}`);
    }
}
