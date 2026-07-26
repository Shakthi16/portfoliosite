import shutil

# Copy report pdf to root web folder
shutil.copy('e:/portfoliosite/agnic2/agnic2final.pdf', 'e:/portfoliosite/agnic2_technical_report.pdf')

agni_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AGNI C2 | Cognitive Command & Control Platform</title>
  <meta name="description" content="AGNI C2: AI-Powered Cognitive Command & Control framework integrating Local LLMs for explainable offensive security workflows and MITRE ATT&CK mapping.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <script src="https://cdn.tailwindcss.com"></script>
  
  <style>
    body {
      background-color: #0b0f19;
      color: #f3f4f6;
      font-family: 'Inter', sans-serif;
      overflow-x: hidden;
    }
    
    .brand-font {
      font-family: 'Outfit', sans-serif;
    }

    .mono-font {
      font-family: 'JetBrains Mono', monospace;
    }
    
    /* Premium Glass Cards */
    .glass-card {
      background: rgba(17, 24, 39, 0.7);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
    }
    
    .pill-tag {
      border: 1px solid rgba(168, 85, 247, 0.25);
      border-radius: 9999px;
      padding: 0.4rem 1rem;
      font-size: 0.8125rem;
      color: #e9d5ff;
      background: rgba(147, 51, 234, 0.12);
      font-weight: 500;
    }

    /* Gradient Glowing Borders */
    .glow-border {
      box-shadow: 0 0 40px -10px rgba(147, 51, 234, 0.25);
    }
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.27/bundled/lenis.min.js"></script>
</head>
<body class="antialiased selection:bg-purple-500 selection:text-white">

  <!-- Navigation Bar -->
  <nav class="w-full py-6 px-6 md:px-12 flex justify-between items-center max-w-7xl mx-auto border-b border-white/10 relative z-50">
    <a href="index.html#projects" class="text-gray-300 font-semibold text-sm flex items-center gap-2.5 hover:text-purple-400 transition-colors">
      <i class="fas fa-arrow-left text-xs"></i> Back to Portfolio
    </a>
    
    <div class="flex items-center gap-4">
      <a href="agnic2_technical_report.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 bg-purple-950/80 hover:bg-purple-900 text-purple-200 border border-purple-400/30 rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-md">
        <i class="fas fa-file-pdf text-rose-400 text-sm"></i>
        <span>Full Technical Report PDF ↗</span>
      </a>
      
      <a href="mailto:shakthisri1605@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request&body=Hi%20Shakthi%20Sri,%0A%0AI%20am%20interested%20in%20requesting%20access%20to%20the%20AGNI%20C2%20repository..." class="px-4 py-2 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-lg">
        <i class="fab fa-github text-sm"></i>
        <span>Request GitHub Repo Access ✉</span>
      </a>
    </div>
  </nav>

  <!-- Hero Header Section -->
  <header class="max-w-7xl mx-auto px-6 md:px-12 pt-16 pb-12 gs-reveal">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-white/10 pb-12 gap-8">
      <div class="flex items-center gap-6">
        <div class="w-16 h-16 bg-gradient-to-br from-purple-600 via-indigo-600 to-pink-600 text-white rounded-2xl flex items-center justify-center text-3xl font-black shadow-lg glow-border">
          🔥
        </div>
        <div>
          <span class="text-xs font-mono text-purple-400 font-bold uppercase tracking-widest block mb-1">ANNUALLY PUBLISHED RESEARCH • ICTACA'26</span>
          <h1 class="text-4xl md:text-6xl font-black brand-font tracking-tight text-white">AGNI C2</h1>
        </div>
      </div>
      
      <div class="text-left md:text-right">
        <p class="font-bold text-sm tracking-widest uppercase text-purple-400">Cybersecurity | AI Cognitive Platform</p>
        <p class="text-gray-400 mt-1 font-mono text-xs">Authored by Shakthi Sri T S &amp; Pooja A</p>
      </div>
    </div>
  </header>

  <!-- Executive Summary & Project Intro -->
  <section class="max-w-7xl mx-auto px-6 md:px-12 mb-20 gs-reveal">
    <p class="text-xl md:text-2xl text-gray-200 leading-relaxed font-light mb-16 max-w-5xl">
      <strong class="font-bold text-purple-300">AGNI C2</strong> is an AI-enhanced Command and Control orchestration platform designed for adversary simulation, red teaming, and cybersecurity education. Powered by local LLMs (Ollama) with secure gRPC/mTLS communication and Sliver C2 integration, AGNI bridges the gap between operational execution, real-time risk assessment, and structured learning.
    </p>

    <!-- Metadata Grid Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="glass-card p-6">
        <h3 class="text-xs font-mono font-bold uppercase tracking-wider text-purple-400 mb-3">Domains</h3>
        <div class="flex flex-wrap gap-2">
          <span class="pill-tag">Offensive Security</span>
          <span class="pill-tag">AI / Local LLMs</span>
          <span class="pill-tag">Red Teaming</span>
          <span class="pill-tag">Full-Stack FastAPI</span>
        </div>
      </div>
      
      <div class="glass-card p-6">
        <h3 class="text-xs font-mono font-bold uppercase tracking-wider text-purple-400 mb-3">Tech Stack</h3>
        <div class="flex flex-wrap gap-2">
          <span class="pill-tag">React / TypeScript</span>
          <span class="pill-tag">FastAPI / WebSocket</span>
          <span class="pill-tag">Sliver C2 (gRPC)</span>
          <span class="pill-tag">Ollama (Qwen LLM)</span>
        </div>
      </div>

      <div class="glass-card p-6">
        <h3 class="text-xs font-mono font-bold uppercase tracking-wider text-purple-400 mb-3">Core Problem</h3>
        <p class="text-xs text-gray-300 leading-relaxed">
          Traditional C2 setups lack integrated intelligence and risk scoring, causing cognitive overload for operators managing live beacons during operations.
        </p>
      </div>

      <div class="glass-card p-6">
        <h3 class="text-xs font-mono font-bold uppercase tracking-wider text-purple-400 mb-3">Research Outcome</h3>
        <p class="text-xs text-gray-300 leading-relaxed">
          Published &amp; presented at <strong class="text-white">ICTACA'26 International Conference</strong>. Developed 5 cognitive algorithms &amp; MITRE ATT&CK mapping.
        </p>
      </div>
    </div>
  </section>

  <!-- GitHub Repo Access Mail Notification Banner -->
  <section class="max-w-7xl mx-auto px-6 md:px-12 mb-20 gs-reveal">
    <div class="bg-gradient-to-r from-purple-950/80 via-indigo-950/90 to-purple-950/80 border-2 border-purple-500/40 rounded-3xl p-8 md:p-10 flex flex-col md:flex-row items-center justify-between gap-6 shadow-2xl glow-border">
      <div class="space-y-2 text-left">
        <div class="flex items-center gap-2 text-purple-300 font-mono text-xs font-bold uppercase tracking-wider">
          <i class="fas fa-lock text-purple-400"></i>
          <span>Controlled Source Code Access</span>
        </div>
        <h3 class="text-2xl md:text-3xl font-extrabold text-white brand-font">Want to view the AGNI C2 GitHub Repository?</h3>
        <p class="text-sm text-gray-300 max-w-2xl">
          Due to offensive security &amp; research compliance, repository access is restricted. Interested researchers, recruiters, or cybersecurity professionals can request private access by sending an email.
        </p>
      </div>

      <a href="mailto:shakthisri1605@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request&body=Hi%20Shakthi%20Sri,%0A%0AI%20am%20interested%20in%20gaining%20access%20to%20the%20AGNI%20C2%20repository...%0A%0AOrganization/Role:%20%0AReason%20for%20Access:%20" class="shrink-0 px-6 py-4 bg-purple-600 hover:bg-purple-500 text-white font-bold rounded-2xl flex items-center gap-3 transition-all hover:scale-105 shadow-xl">
        <i class="fas fa-paper-plane text-base"></i>
        <span class="text-sm">Mail Me for GitHub Access ↗</span>
      </a>
    </div>
  </section>

  <!-- Main Content & Diagrams -->
  <main class="max-w-7xl mx-auto px-6 md:px-12 mb-32 space-y-24">
    
    <!-- Vision Shift & System Architecture -->
    <div class="gs-reveal">
      <div class="flex items-center gap-3 mb-4">
        <span class="w-8 h-1 bg-purple-500 rounded-full"></span>
        <h2 class="text-3xl md:text-4xl font-extrabold brand-font text-white">System Architecture &amp; Vision</h2>
      </div>
      <p class="text-base text-gray-300 leading-relaxed mb-8 max-w-4xl">
        AGNI C2 replaces traditional fragmented setups with a unified cognitive workflow: 
        <span class="font-mono text-purple-300 bg-purple-950/60 px-3 py-1 rounded-lg border border-purple-500/30 text-xs">Operator → AI Intelligence → Risk Analysis → Attack Graph → Target</span>.
      </p>

      <div class="glass-card p-4 md:p-6 overflow-hidden rounded-3xl border border-white/15 shadow-2xl">
        <img src="agni_arch_diagram.png" alt="AGNI C2 Overall System Architecture Diagram" class="w-full h-auto object-contain rounded-2xl block bg-white/5 mx-auto max-h-[750px]">
        <p class="text-center text-xs font-mono text-gray-400 mt-4">Figure 3.1: AGNI C2 Overall System Architecture &amp; Module Interaction Diagram</p>
      </div>
    </div>

    <!-- Core Interfaces & Features Grid -->
    <div class="gs-reveal space-y-16">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-purple-500 rounded-full"></span>
        <h2 class="text-3xl md:text-4xl font-extrabold brand-font text-white">Platform Modules &amp; UI Screenshots</h2>
      </div>
      
      <!-- Feature 1: Operator Panel & Session View -->
      <div class="glass-card p-6 md:p-8 space-y-6">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-white/10 pb-4">
          <div>
            <span class="text-xs font-mono text-purple-400 font-bold uppercase">MODULE 01</span>
            <h3 class="text-2xl font-bold text-white brand-font">Operator Panel &amp; Session Management</h3>
          </div>
          <span class="pill-tag font-mono text-xs">Real-Time Beacon Stream</span>
        </div>
        <p class="text-sm text-gray-300 leading-relaxed">
          Provides live multi-beacon control, command execution terminals, and automated session logging via gRPC channels connected to Sliver C2 backend nodes.
        </p>
        <div class="overflow-hidden rounded-2xl border border-white/10 shadow-xl bg-black/40">
          <img src="agni_operator_panel.png" alt="AGNI C2 Operator Panel Session View" class="w-full h-auto object-cover rounded-xl block">
        </div>
      </div>

      <!-- Feature 2: Network Topology & Attack Graph -->
      <div class="glass-card p-6 md:p-8 space-y-6">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-white/10 pb-4">
          <div>
            <span class="text-xs font-mono text-purple-400 font-bold uppercase">MODULE 02</span>
            <h3 class="text-2xl font-bold text-white brand-font">Network Topology &amp; Attack Graph Visualizer</h3>
          </div>
          <span class="pill-tag font-mono text-xs">SVG Node Graph</span>
        </div>
        <p class="text-sm text-gray-300 leading-relaxed">
          Interactive network graph representing compromised hosts, lateral movement paths, and target nodes with live risk heatmaps and MITRE technique overlays.
        </p>
        <div class="overflow-hidden rounded-2xl border border-white/10 shadow-xl bg-black/40">
          <img src="agni_network_topology.png" alt="AGNI C2 Network Topology Map" class="w-full h-auto object-cover rounded-xl block">
        </div>
      </div>

      <!-- Feature 3: MITRE ATT&CK Browser & Playbook Builder -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="glass-card p-6 space-y-4">
          <div class="border-b border-white/10 pb-3">
            <span class="text-xs font-mono text-purple-400 font-bold uppercase">MODULE 03</span>
            <h3 class="text-xl font-bold text-white brand-font">MITRE ATT&amp;CK Browser</h3>
          </div>
          <p class="text-xs text-gray-300 leading-relaxed">
            Real-time technique lookup and automated tagging of operational commands to MITRE TTP matrix IDs.
          </p>
          <div class="overflow-hidden rounded-xl border border-white/10 bg-black/40">
            <img src="agni_mitre_attack.png" alt="MITRE ATT&CK Browser Interface" class="w-full h-auto object-cover rounded-lg block">
          </div>
        </div>

        <div class="glass-card p-6 space-y-4">
          <div class="border-b border-white/10 pb-3">
            <span class="text-xs font-mono text-purple-400 font-bold uppercase">MODULE 04</span>
            <h3 class="text-xl font-bold text-white brand-font">Visual Playbook Flow Builder</h3>
          </div>
          <p class="text-xs text-gray-300 leading-relaxed">
            Drag-and-drop workflow editor to assemble automated red team playbooks and attack execution chains.
          </p>
          <div class="overflow-hidden rounded-xl border border-white/10 bg-black/40">
            <img src="agni_playbook_builder.png" alt="Visual Playbook Flow Builder" class="w-full h-auto object-cover rounded-lg block">
          </div>
        </div>
      </div>

    </div>

    <!-- 5 Cognitive Intelligence Algorithms -->
    <div class="gs-reveal">
      <div class="flex items-center gap-3 mb-8">
        <span class="w-8 h-1 bg-purple-500 rounded-full"></span>
        <h2 class="text-3xl md:text-4xl font-extrabold brand-font text-white">5 Core Intelligence Algorithms</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="glass-card p-6 space-y-2 border-t-4 border-t-purple-500">
          <h4 class="text-lg font-bold text-purple-300">1. Command Explanation Engine</h4>
          <p class="text-xs text-gray-300 leading-relaxed">Parses raw terminal flags and translates complex offensive commands into structured human-readable explanations.</p>
        </div>

        <div class="glass-card p-6 space-y-2 border-t-4 border-t-indigo-500">
          <h4 class="text-lg font-bold text-indigo-300">2. Command Risk Scoring</h4>
          <p class="text-xs text-gray-300 leading-relaxed">Evaluates OPSEC risk (0-100) before command dispatch based on process creation, network noise, and artifact footprints.</p>
        </div>

        <div class="glass-card p-6 space-y-2 border-t-4 border-t-pink-500">
          <h4 class="text-lg font-bold text-pink-300">3. Lateral Movement Suggester</h4>
          <p class="text-xs text-gray-300 leading-relaxed">Analyzes domain trust relationships and credentials to suggest optimal attack paths across the network topology.</p>
        </div>

        <div class="glass-card p-6 space-y-2 border-t-4 border-t-purple-500">
          <h4 class="text-lg font-bold text-purple-300">4. Automated Detection Rule Generator</h4>
          <p class="text-xs text-gray-300 leading-relaxed">Generates Sigma and YARA rules automatically for executed commands to facilitate Blue Team defense gap analysis.</p>
        </div>

        <div class="glass-card p-6 space-y-2 border-t-4 border-t-indigo-500">
          <h4 class="text-lg font-bold text-indigo-300">5. Intent Compiler</h4>
          <p class="text-xs text-gray-300 leading-relaxed">Translates high-level natural language operator requests into OPSEC-safe low-level terminal commands via Local LLMs.</p>
        </div>

        <div class="glass-card p-6 space-y-2 border-t-4 border-t-pink-500 flex flex-col justify-between">
          <div>
            <h4 class="text-lg font-bold text-pink-300">Full Research Paper</h4>
            <p class="text-xs text-gray-300 leading-relaxed">Read the complete 136-page Anna University B.Tech thesis project report PDF.</p>
          </div>
          <a href="agnic2_technical_report.pdf" target="_blank" rel="noopener noreferrer" class="mt-3 inline-flex items-center gap-2 text-xs font-bold text-purple-300 hover:text-white transition-colors">
            <span>Download Full Thesis PDF ↗</span>
          </a>
        </div>
      </div>
    </div>

  </main>

  <!-- Bottom CTA Footer -->
  <footer class="bg-black/60 py-16 border-t border-white/10 relative z-20">
    <div class="max-w-7xl mx-auto px-6 md:px-12 text-center space-y-8">
      <h2 class="text-3xl font-extrabold brand-font text-white">
        Explore Project Artifacts &amp; Research
      </h2>
      <div class="flex flex-wrap justify-center gap-4">
        <a href="mailto:shakthisri1605@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request" class="px-6 py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-xl">
          <i class="fab fa-github text-sm"></i>
          <span>Request GitHub Repo Access (Mail Me)</span>
        </a>

        <a href="agnic2_technical_report.pdf" target="_blank" rel="noopener noreferrer" class="px-6 py-3.5 bg-zinc-900 border border-white/20 hover:border-purple-400 text-purple-200 rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-lg">
          <i class="fas fa-file-pdf text-rose-400 text-sm"></i>
          <span>Read Technical Report PDF</span>
        </a>

        <a href="index.html#projects" class="px-6 py-3.5 bg-white text-black hover:bg-gray-200 rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-md">
          <i class="fas fa-arrow-left text-xs"></i>
          <span>Back to Main Portfolio</span>
        </a>
      </div>

      <p class="text-xs text-gray-500 font-mono pt-4 border-t border-white/5">
        © 2026 Shakthi Sri T S — AGNI C2 Cognitive Command &amp; Control Project
      </p>
    </div>
  </footer>

  <script>
    // Initialize Lenis (Smooth Scroll)
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      direction: 'vertical',
      smooth: true
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // GSAP ScrollTrigger Integration
    gsap.registerPlugin(ScrollTrigger);
    
    const reveals = document.querySelectorAll('.gs-reveal');
    reveals.forEach(el => {
      gsap.fromTo(el, 
        { y: 35, opacity: 0 },
        {
          y: 0, 
          opacity: 1, 
          duration: 1.0,
          ease: "power3.out",
          scrollTrigger: {
            trigger: el,
            start: "top 88%",
            toggleActions: "play none none reverse"
          }
        }
      );
    });
  </script>
</body>
</html>
'''

with open('e:/portfoliosite/agni-c2.html', 'w', encoding='utf-8') as f:
    f.write(agni_html)

print("SUCCESSFULLY BUILT CLEAN AGNI-C2.HTML PAGE WITH DIAGRAMS, SCREENSHOTS, PDF LINK, AND GITHUB MAIL REQUEST BUTTON!")
