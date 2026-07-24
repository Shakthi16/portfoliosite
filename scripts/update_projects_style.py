import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

new_projects_grid = '''<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10" id="project-grid">
          <!-- 1. AGNI C2 -->
          <div class="project-card-container group proj-item web flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1000" alt="AGNI C2" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Cybersecurity</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">AI C2</span>
              </div>
              <a href="agni-c2.html" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">AGNI C2 Platform</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">AI-Powered Cognitive Command &amp; Control framework integrating Local LLMs for explainable security workflows.</p>
            </div>
          </div>

          <!-- 2. Reality Lag -->
          <div class="project-card-container group proj-item web flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?q=80&w=1000" alt="Reality Lag" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Deception Security</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Python Engine</span>
              </div>
              <a href="https://github.com/Shakthi16/realitylagv1" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Reality Lag Prototype</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Deception-based security platform featuring behavioral pattern analysis and attacker environment simulation.</p>
            </div>
          </div>

          <!-- 3. Syclone -->
          <div class="project-card-container group proj-item web flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000" alt="Syclone App" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Web App</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Full-Stack</span>
              </div>
              <a href="https://syclone.onrender.com" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Syclone Web App</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Modern web application featuring dynamic animations, live interactive cards, and backend API setup.</p>
            </div>
          </div>

          <!-- 4. EduGo -->
          <div class="project-card-container group proj-item uiux flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://i.ibb.co/413tnkC/Screenshot-2025-01-17-232717.png" alt="EduGo Platform" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">UI/UX</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">EdTech Platform</span>
              </div>
              <a href="https://www.figma.com/proto/823yMjZjFP7NlHpt7Cx6bQ/edugo" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">EduGo Learning App</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">EdTech platform UI design focused on intuitive course navigation, progress tracking, and accessibility.</p>
            </div>
          </div>

          <!-- 5. Modern Sign-up Flow -->
          <div class="project-card-container group proj-item uiux flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://i.ibb.co/mhpMpNL/Screenshot-2025-01-17-233410.png" alt="Modern Sign-up Flow" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">UI/UX</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">User Onboarding</span>
              </div>
              <a href="https://www.figma.com/proto/I1ASQY2n71Ny3SHtDbZX3R" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Modern Sign-up Flow</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Frictionless multi-step registration UX with subtle micro-interactions and real-time form validation.</p>
            </div>
          </div>

          <!-- 6. Flexy Men's Ecommerce -->
          <div class="project-card-container group proj-item uiux flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://i.ibb.co/XspL7xY/Screenshot-2025-01-17-233654.png" alt="Flexy Ecommerce" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">UI/UX</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">E-Commerce</span>
              </div>
              <a href="https://www.figma.com/proto/0DLbG9VmXQKAGVpXYc1WhG" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Flexy Apparel Store</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">High-conversion mobile &amp; desktop shopping interface with streamlined product filtering and quick checkout.</p>
            </div>
          </div>

          <!-- 7. Nudge Finance -->
          <div class="project-card-container group proj-item uiux flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="nudge.png" alt="Nudge Finance" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">UI/UX</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Fintech</span>
              </div>
              <a href="https://www.figma.com/proto/I1ASQY2n71Ny3SHtDbZX3R" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Nudge Finance App</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Behavioral money management interface encouraging Gen-Z savings habits and budget tracking.</p>
            </div>
          </div>

          <!-- 8. Perfume Design -->
          <div class="project-card-container group proj-item uiux flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="new.png" alt="Perfume Design" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">UI/UX</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Luxury Brand</span>
              </div>
              <a href="https://www.figma.com/proto/6Z7eRUtDhLp4pDR8ANijP6" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Elegance Fragrance</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Bespoke fragrance brand experience highlighting scent profiles, ingredient notes, and minimalist aesthetics.</p>
            </div>
          </div>

          <!-- 9. Weather App -->
          <div class="project-card-container group proj-item web flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://i.ibb.co/F0wPrRJ/Screenshot-2025-01-17-231636.png" alt="Weather App" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Web Dev</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Weather API</span>
              </div>
              <a href="https://weatherappweb1.netlify.app/" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Atmosphere Weather</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Clean weather dashboard built with JavaScript API integrations and responsive climate metrics.</p>
            </div>
          </div>

          <!-- 10. Aurum Page -->
          <div class="project-card-container group proj-item web flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://i.ibb.co/YL0J9tL/Screenshot-2025-01-17-232117.png" alt="Aurum Page" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Web Dev</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Frontend</span>
              </div>
              <a href="https://aurumpage5.netlify.app/" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Aurum Studio</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Premium brand website featuring glassmorphism cards, micro-animations, and responsive layouts.</p>
            </div>
          </div>

          <!-- 11. 3D Cosmic -->
          <div class="project-card-container group proj-item web flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="https://i.ibb.co/HptDXhJr/Screenshot-2025-06-17-140305.png" alt="3D Cosmic" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Three.js</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">3D Galaxy</span>
              </div>
              <a href="https://cosmicstar.netlify.app/" target="_blank" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Cosmic Voyage Explorer</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Interactive 3D Milky Way visualization rendered with Three.js WebGL shaders and starfields.</p>
            </div>
          </div>

          <!-- 12. Graphic: Startuptn -->
          <div class="project-card-container group proj-item graphic hidden flex flex-col space-y-4">
            <div class="relative w-full bg-[#FAF6EE] rounded-[32px] overflow-hidden p-6 border border-gray-200/60 shadow-xs transition-all duration-500 group-hover:shadow-md group-hover:-translate-y-1">
              <span class="absolute top-4 left-4 z-20 bg-[#8b2252] text-white text-[10px] font-mono font-bold tracking-wider px-3 py-1 rounded-full shadow-xs">TO VIEW</span>
              <div class="w-full h-[240px] md:h-[270px] rounded-[20px] overflow-hidden bg-white shadow-xs flex items-center justify-center">
                <img src="Picture4.png" alt="Startuptn Poster" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              </div>
            </div>
            <div class="flex items-center justify-between gap-2 pt-1">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-4 py-1.5 rounded-full border border-pink-200/80 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Graphic Design</span>
                <span class="px-4 py-1.5 rounded-full border border-gray-200 bg-white text-xs font-semibold text-[#1F1F1F] shadow-2xs">Poster</span>
              </div>
              <a href="startuptn.html" class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#1F1F1F] hover:bg-[#1F1F1F] hover:text-white transition-all shadow-2xs shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
            <div class="space-y-1 text-left">
              <h3 class="text-2xl font-extrabold text-[#1F1F1F] tracking-tight font-sans group-hover:text-[#8b2252] transition-colors leading-snug">Startuptn.in Poster</h3>
              <p class="text-xs md:text-sm text-gray-500 font-medium leading-relaxed">Creative event poster design highlighting government startup initiatives and innovation hubs.</p>
            </div>
          </div>
        </div>'''

pattern = r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="project-grid">[\s\S]*?</div>\s*</div>\s*</section>'

replacement = new_projects_grid + '\n      </div>\n    </section>'

updated_html = re.sub(pattern, replacement, html)

if len(updated_html) != len(html):
    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print('SUCCESSFULLY UPDATED PROJECT GRID!')
else:
    print('Pattern not matched, attempting line-by-line replacement...')
