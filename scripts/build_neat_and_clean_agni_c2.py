html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AGNI C2 | Cognitive Command & Control for Red Teaming & Cybersecurity Education</title>
  <meta name="description" content="AGNI C2: AI-Powered Cognitive Command & Control framework integrating Local LLMs for explainable offensive security workflows, MITRE ATT&CK mapping, and risk analysis. Authored by Shakthi Sri T S & Pooja A.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <script src="https://cdn.tailwindcss.com"></script>
  
  <style>
    body {
      background-color: #FAF8F5;
      color: #1c1917;
      font-family: 'Inter', sans-serif;
      overflow-x: hidden;
    }
    
    .brand-font {
      font-family: 'Outfit', sans-serif;
    }

    .mono-font {
      font-family: 'JetBrains Mono', monospace;
    }
    
    /* Clean Minimal Cards */
    .neat-card {
      background: #FFFFFF;
      border: 1px solid rgba(139, 34, 82, 0.1);
      box-shadow: 0 4px 25px -2px rgba(0, 0, 0, 0.03), 0 10px 15px -3px rgba(0, 0, 0, 0.02);
      border-radius: 20px;
      transition: box-shadow 0.3s ease;
    }

    .neat-card:hover {
      box-shadow: 0 12px 35px -4px rgba(139, 34, 82, 0.08);
    }
    
    .pill-tag {
      border: 1px solid rgba(139, 34, 82, 0.18);
      border-radius: 9999px;
      padding: 0.35rem 0.95rem;
      font-size: 0.75rem;
      color: #6b1d42;
      background: rgba(139, 34, 82, 0.05);
      font-weight: 600;
    }

    .keyword-badge {
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 0.3rem 0.75rem;
      font-size: 0.75rem;
      color: #475569;
      background: #FFFFFF;
      font-weight: 500;
      font-family: 'JetBrains Mono', monospace;
    }
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.27/bundled/lenis.min.js"></script>
</head>
<body class="antialiased selection:bg-[#8b2252] selection:text-white">

  <!-- Top Sticky Navigation Bar -->
  <nav class="w-full py-4 px-6 md:px-12 flex justify-between items-center max-w-6xl mx-auto border-b border-amber-900/10 sticky top-0 bg-[#FAF8F5]/90 backdrop-blur-md relative z-50">
    <a href="index.html#projects" class="text-gray-800 font-semibold text-xs md:text-sm flex items-center gap-2 hover:text-[#8b2252] transition-colors">
      <i class="fas fa-arrow-left text-xs"></i> Back to Portfolio
    </a>
    
    <div class="flex items-center gap-2.5">
      <!-- Mail Me for Full PDF Report -->
      <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request&body=Hi%20Shakthi%20Sri,%0A%0AI%20would%20like%20to%20request%20the%20full%20AGNI%20C2%20136-page%20Technical%20Report%20PDF...%0A%0AName:%20%0AOrganization/Role:%20" class="px-3.5 py-2 bg-rose-50 hover:bg-rose-100 text-rose-800 border border-rose-200/80 rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-xs">
        <i class="fas fa-envelope text-rose-600"></i>
        <span class="hidden sm:inline">Request Report PDF</span>
        <span class="sm:hidden">PDF</span>
      </a>
      
      <!-- Mail Me for GitHub Repo Access -->
      <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request&body=Hi%20Shakthi%20Sri,%0A%0AI%20am%20interested%20in%20requesting%20access%20to%20the%20AGNI%20C2%20GitHub%20repository...%0A%0AName:%20%0AOrganization/Role:%20" class="px-3.5 py-2 bg-[#8b2252] hover:bg-[#721b42] text-white rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
        <i class="fab fa-github"></i>
        <span class="hidden sm:inline">Request GitHub Access</span>
        <span class="sm:hidden">GitHub</span>
      </a>
    </div>
  </nav>

  <!-- Clean Centered Paper Header -->
  <header class="max-w-4xl mx-auto px-6 pt-12 pb-8 text-center space-y-4 gs-reveal">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-[#8b2252]/10 text-[#8b2252] text-xs font-mono font-bold rounded-full border border-[#8b2252]/20">
      <i class="fas fa-certificate text-xs"></i>
      <span>PUBLISHED RESEARCH PAPER • ICTACA'26</span>
    </div>

    <h1 class="text-3xl md:text-5xl font-black brand-font tracking-tight text-gray-900 leading-tight">
      AGNI C2: Cognitive Command &amp; Control For Red Teaming And Cybersecurity Education
    </h1>

    <!-- Authors & Institution Info -->
    <div class="pt-4 border-t border-gray-200/80 max-w-2xl mx-auto text-center space-y-1">
      <p class="text-sm font-bold text-gray-900">
        Authors: <span class="text-[#8b2252]">Shakthi Sri T S</span> &amp; <span class="text-[#8b2252]">Pooja A</span>
      </p>
      <p class="text-xs text-gray-600">
        Department of Information Technology, Kingston Engineering College, Vellore, Tamil Nadu, India
      </p>
      <p class="text-xs font-mono text-gray-500 pt-1">
        Emails: <a href="mailto:srishakthi799@gmail.com" class="text-[#8b2252] underline">srishakthi799@gmail.com</a> | <a href="mailto:poojaa0042@gmail.com" class="text-[#8b2252] underline">poojaa0042@gmail.com</a>
      </p>

      <div class="pt-2 text-xs text-gray-500 font-medium">
        Anna University: Chennai 600 025 | Supervisor: Dr. M. Vasumathy, MS(SE)., Ph.D(CSE) | HOD: Mrs. M. Menaka, M.Tech., (Ph.D)
      </div>
    </div>

    <!-- Keywords -->
    <div class="flex flex-wrap items-center justify-center gap-2 pt-3">
      <span class="keyword-badge">Command &amp; Control</span>
      <span class="keyword-badge">Red Teaming</span>
      <span class="keyword-badge">Large Language Models</span>
      <span class="keyword-badge">MITRE ATT&amp;CK</span>
      <span class="keyword-badge">Cybersecurity Education</span>
      <span class="keyword-badge">Local LLM (Ollama)</span>
    </div>
  </header>

  <!-- Abstract Card & Mail Request Banner -->
  <section class="max-w-4xl mx-auto px-6 mb-16 space-y-6 gs-reveal">
    <div class="neat-card p-8 md:p-10 border-t-4 border-t-[#8b2252] space-y-4">
      <h2 class="text-xs font-mono font-bold text-[#8b2252] uppercase tracking-widest flex items-center gap-2">
        <i class="fas fa-file-alt"></i> Abstract
      </h2>
      <p class="text-base text-gray-800 leading-relaxed font-normal">
        Modern Command and Control (C2) frameworks used in red teaming lack integrated intelligence, real-time risk assessment, and structured learning support, creating a gap between operational execution and informed decision-making. Existing platforms are often fragmented, requiring multiple tools for session management, attack planning, and defensive mapping, while offering minimal AI-driven assistance.
      </p>
      <p class="text-sm text-gray-700 leading-relaxed font-light">
        To address these limitations, <strong class="font-bold text-[#8b2252]">AGNI C2</strong> is developed as a unified, AI-enhanced Command and Control orchestration platform for adversary simulation and cybersecurity education. The system integrates a React-based frontend with a FastAPI backend and leverages Sliver C2 via gRPC/mTLS for secure communication. It incorporates a cognitive intelligence layer powered by local LLMs (Ollama with Qwen2.5) with fallback mechanisms, enabling real-time command explanation, attack path analysis, and detection rule generation.
      </p>
    </div>

    <!-- Restricted Access Mail Banner -->
    <div class="bg-gradient-to-r from-purple-50 via-rose-50 to-purple-50 border border-[#8b2252]/20 rounded-2xl p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6 shadow-xs">
      <div class="space-y-1 text-left">
        <div class="flex items-center gap-2 text-[#8b2252] font-mono text-xs font-bold uppercase tracking-wider">
          <i class="fas fa-shield-alt"></i>
          <span>Controlled Research &amp; Source Code Access</span>
        </div>
        <h3 class="text-lg md:text-xl font-bold text-gray-900 brand-font">Need the 136-Page Report PDF or GitHub Repository Access?</h3>
        <p class="text-xs text-gray-600 max-w-2xl leading-relaxed">
          Due to cybersecurity compliance, public downloads are restricted. Interested researchers and professionals can request access via email.
        </p>
      </div>

      <div class="flex items-center gap-3 shrink-0">
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request" class="px-4 py-2.5 bg-rose-700 hover:bg-rose-800 text-white font-bold rounded-xl text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
          <i class="fas fa-file-pdf"></i>
          <span>Mail for PDF Report ✉</span>
        </a>
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request" class="px-4 py-2.5 bg-[#8b2252] hover:bg-[#721b42] text-white font-bold rounded-xl text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
          <i class="fab fa-github"></i>
          <span>Mail for GitHub Access ✉</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Main Content Structure -->
  <main class="max-w-4xl mx-auto px-6 mb-24 space-y-16">

    <!-- Official Tech Stack Image Section (techstack.png) -->
    <section class="gs-reveal space-y-4">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">System Tech Stack &amp; Core Architecture</h2>
      </div>

      <div class="neat-card p-4 md:p-6 overflow-hidden bg-white text-center shadow-sm">
        <img src="techstack.png" alt="AGNI C2 Official Technology Stack Architecture" class="w-full h-auto object-contain rounded-xl block border border-gray-100 mx-auto max-h-[550px]">
        <p class="text-center text-xs font-mono text-gray-500 mt-4">AGNI C2 End-to-End Technology Stack &amp; Layered Component Architecture</p>
      </div>
    </section>

    <!-- 1. Introduction & Background -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">1. Introduction &amp; The C2 Landscape</h2>
      </div>

      <div class="neat-card p-6 md:p-8 space-y-4 text-xs text-gray-700 leading-relaxed">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="space-y-2">
            <h3 class="text-sm font-bold text-gray-900 brand-font flex items-center gap-2">
              <i class="fas fa-chart-line text-[#8b2252]"></i> 1.1 Background &amp; Industry Gap
            </h3>
            <p>
              There is currently a global shortage of <strong>3.4 million cybersecurity professionals</strong>. Defensive capabilities lag behind offensive innovation. Red Team operations measure defense response capabilities using adversarial simulations requiring C2 beacon infrastructure.
            </p>
          </div>

          <div class="space-y-2">
            <h3 class="text-sm font-bold text-gray-900 brand-font flex items-center gap-2">
              <i class="fas fa-dollar-sign text-[#8b2252]"></i> 1.2 Commercial vs Open-Source C2
            </h3>
            <p>
              Commercial C2 tools like Cobalt Strike cost over <strong>$3,500/year per user</strong> and are closed-source. Open-source tools (Sliver, Covenant, Mythic, Empire) manage beacons well but lack integrated cognitive assistance and real-time MITRE ATT&amp;CK guidance.
            </p>
          </div>
        </div>

        <div class="pt-4 border-t border-gray-100 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="space-y-2">
            <h3 class="text-sm font-bold text-gray-900 brand-font flex items-center gap-2">
              <i class="fas fa-microchip text-[#8b2252]"></i> 1.3 Local LLM Opportunity
            </h3>
            <p>
              Quantized local models (Qwen2.5, Llama 3) run on 16GB RAM laptops with &lt;1s latency. Cloud AI APIs (OpenAI, Anthropic, Google) leak confidential operational target data and credentials, making local-first LLM inference mandatory.
            </p>
          </div>

          <div class="space-y-2">
            <h3 class="text-sm font-bold text-gray-900 brand-font flex items-center gap-2">
              <i class="fas fa-graduation-cap text-[#8b2252]"></i> 1.4 Educational Gap
            </h3>
            <p>
              High lab infrastructure costs, CTF limitations, and absence of integrated AI tutors in C2 workflows restrict students from mastering realistic offensive security decision-making.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. C2 Evolution Timeline -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">2. C2 Evolution &amp; Literature Review</h2>
      </div>

      <div class="neat-card p-6 md:p-8 space-y-6">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200/70 space-y-1">
            <span class="font-mono text-[#8b2252] font-bold">2003 • METERPRETER</span>
            <h4 class="font-bold text-gray-900">Single-Instance Plugins</h4>
            <p class="text-gray-600 text-[11px]">Early post-exploitation plugins without multiplexed beacon management.</p>
          </div>

          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200/70 space-y-1">
            <span class="font-mono text-[#8b2252] font-bold">2012 • COBALT STRIKE</span>
            <h4 class="font-bold text-gray-900">Team Server &amp; Malleable C2</h4>
            <p class="text-gray-600 text-[11px]">Introduced team servers &amp; sleep/jitter beacons. Closed-source ($3,500/yr).</p>
          </div>

          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200/70 space-y-1">
            <span class="font-mono text-[#8b2252] font-bold">2015-2019 • EMPIRE / MYTHIC</span>
            <h4 class="font-bold text-gray-900">PowerShell &amp; Modular Agents</h4>
            <p class="text-gray-600 text-[11px]">Starkiller web interface and modular agent profiles (Apollo, Medusa, Poseidon).</p>
          </div>

          <div class="p-4 bg-purple-50 rounded-xl border border-[#8b2252]/30 space-y-1">
            <span class="font-mono text-[#8b2252] font-bold">2020-2026 • SLIVER &amp; AGNI C2</span>
            <h4 class="font-bold text-gray-900">Embedded Cognitive AI</h4>
            <p class="text-gray-700 text-[11px]">Sliver mTLS/gRPC backend + AGNI C2 local LLM cognitive intelligence layer.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Problem Statement & 4. Objectives -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">3. Problem Statement &amp; 4. Core Objectives</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- 3 Problems -->
        <div class="neat-card p-6 space-y-3 border-l-4 border-l-rose-600">
          <h3 class="text-sm font-bold text-rose-900 brand-font uppercase tracking-wide">3 Specific Problems</h3>
          <div class="space-y-2.5 text-xs text-gray-700">
            <div class="p-3 bg-rose-50/60 rounded-xl border border-rose-100">
              <strong class="text-rose-950 font-bold block">1. No Integrated Intelligence in C2</strong>
              Operators manage multiple browser tabs for MITRE ATT&amp;CK, command references, and threat intel.
            </div>
            <div class="p-3 bg-rose-50/60 rounded-xl border border-rose-100">
              <strong class="text-rose-950 font-bold block">2. Cloud AI Data Leakage Risk</strong>
              Sending C2 terminal outputs &amp; target configurations to cloud LLM APIs violates NDA data privacy.
            </div>
            <div class="p-3 bg-rose-50/60 rounded-xl border border-rose-100">
              <strong class="text-rose-950 font-bold block">3. Educational Feedback Lag</strong>
              Students face static documentation and massive feedback delays during hands-on cybersecurity exercises.
            </div>
          </div>
        </div>

        <!-- 4 Objectives -->
        <div class="neat-card p-6 space-y-3 border-l-4 border-l-[#8b2252]">
          <h3 class="text-sm font-bold text-[#8b2252] brand-font uppercase tracking-wide">4 Core Objectives</h3>
          <div class="space-y-2.5 text-xs text-gray-700">
            <div class="p-3 bg-purple-50/60 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block">1. Local-First Open-Source C2</strong>
              Run 100% on consumer hardware (16GB RAM laptop) with zero cloud dependency using Ollama.
            </div>
            <div class="p-3 bg-purple-50/60 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block">2. Embedded Real-Time AI</strong>
              Provide command explanations, attack path reasoning, pre-execution risk scoring, and rule generation.
            </div>
            <div class="p-3 bg-purple-50/60 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block">3. Isolated VirtualBox Cyber Range</strong>
              Deploy an isolated lab with Kali Linux attack VM and Windows victim VM.
            </div>
            <div class="p-3 bg-purple-50/60 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block">4. Educational Distribution</strong>
              Release under educational license with complete research documentation.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. System Architecture & Diagrams -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">5. Overall System Architecture Diagram</h2>
      </div>

      <div class="neat-card p-4 md:p-6 overflow-hidden bg-white shadow-sm space-y-3">
        <img src="agni_arch_diagram.png" alt="AGNI C2 Overall System Architecture Diagram" class="w-full h-auto object-contain rounded-xl block border border-gray-100 mx-auto max-h-[700px]">
        <p class="text-center text-xs font-mono text-gray-500">Figure 3.1: AGNI C2 Overall System Architecture &amp; Module Interaction Diagram</p>
      </div>
    </section>

    <!-- 6. Platform Modules & UI Showcase -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">6. Platform Modules &amp; UI Screenshots</h2>
      </div>

      <!-- Dashboard UI -->
      <div class="neat-card p-6 space-y-3">
        <div class="flex justify-between items-center border-b border-gray-100 pb-3">
          <h3 class="text-base font-bold text-gray-900 brand-font">Dashboard &amp; Main Overview Interface</h3>
          <span class="pill-tag font-mono text-xs">Figure 4.1</span>
        </div>
        <div class="overflow-hidden rounded-xl border border-gray-200">
          <img src="agni_dashboard_ui.png" alt="AGNI C2 Dashboard Interface" class="w-full h-auto object-cover block">
        </div>
      </div>

      <!-- Operator Panel -->
      <div class="neat-card p-6 space-y-3">
        <div class="flex justify-between items-center border-b border-gray-100 pb-3">
          <h3 class="text-base font-bold text-gray-900 brand-font">Operator Panel &amp; Session Beacon Console</h3>
          <span class="pill-tag font-mono text-xs">Figure 4.2</span>
        </div>
        <div class="overflow-hidden rounded-xl border border-gray-200">
          <img src="agni_operator_panel.png" alt="AGNI C2 Operator Panel" class="w-full h-auto object-cover block">
        </div>
      </div>

      <!-- Network Topology Map -->
      <div class="neat-card p-6 space-y-3">
        <div class="flex justify-between items-center border-b border-gray-100 pb-3">
          <h3 class="text-base font-bold text-gray-900 brand-font">Network Visualization &amp; Topology Graph</h3>
          <span class="pill-tag font-mono text-xs">Figure 4.8</span>
        </div>
        <div class="overflow-hidden rounded-xl border border-gray-200">
          <img src="agni_network_topology.png" alt="Network Topology Graph" class="w-full h-auto object-cover block">
        </div>
      </div>

      <!-- Two Column: MITRE & Playbook -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="neat-card p-6 space-y-3">
          <div class="flex justify-between items-center border-b border-gray-100 pb-2">
            <h3 class="text-sm font-bold text-gray-900 brand-font">MITRE ATT&amp;CK Browser</h3>
            <span class="pill-tag font-mono text-xs">Figure 4.11</span>
          </div>
          <div class="overflow-hidden rounded-xl border border-gray-200">
            <img src="agni_mitre_attack.png" alt="MITRE ATT&CK Browser" class="w-full h-auto object-cover block">
          </div>
        </div>

        <div class="neat-card p-6 space-y-3">
          <div class="flex justify-between items-center border-b border-gray-100 pb-2">
            <h3 class="text-sm font-bold text-gray-900 brand-font">Visual Playbook Flow Builder</h3>
            <span class="pill-tag font-mono text-xs">Figure 4.5</span>
          </div>
          <div class="overflow-hidden rounded-xl border border-gray-200">
            <img src="agni_playbook_builder.png" alt="Playbook Builder" class="w-full h-auto object-cover block">
          </div>
        </div>
      </div>
    </section>

    <!-- 7. 5 Cognitive Intelligence Algorithms -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">7. 5 Core Cognitive Intelligence Algorithms</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
        <div class="neat-card p-5 space-y-2 border-t-4 border-t-[#8b2252]">
          <h4 class="font-bold text-[#8b2252] text-sm">1. Command Explanation Engine</h4>
          <p class="text-gray-600 leading-relaxed">Parses raw terminal flags and translates complex offensive commands into structured human-readable explanations.</p>
        </div>

        <div class="neat-card p-5 space-y-2 border-t-4 border-t-indigo-600">
          <h4 class="font-bold text-indigo-900 text-sm">2. Command Risk Scoring</h4>
          <p class="text-gray-600 leading-relaxed">Evaluates OPSEC risk (0-100) before command dispatch based on process creation, network noise, and artifact footprints.</p>
        </div>

        <div class="neat-card p-5 space-y-2 border-t-4 border-t-purple-600">
          <h4 class="font-bold text-purple-900 text-sm">3. Lateral Movement Suggester</h4>
          <p class="text-gray-600 leading-relaxed">Analyzes domain trust relationships and credentials to suggest optimal attack paths across the network topology.</p>
        </div>

        <div class="neat-card p-5 space-y-2 border-t-4 border-t-[#8b2252]">
          <h4 class="font-bold text-[#8b2252] text-sm">4. Automated Detection Rule Generator</h4>
          <p class="text-gray-600 leading-relaxed">Generates Sigma and YARA rules automatically for executed commands to facilitate Blue Team defense gap analysis.</p>
        </div>

        <div class="neat-card p-5 space-y-2 border-t-4 border-t-indigo-600">
          <h4 class="font-bold text-indigo-900 text-sm">5. Intent Compiler</h4>
          <p class="text-gray-600 leading-relaxed">Translates high-level natural language operator requests into OPSEC-safe low-level terminal commands via Local LLMs.</p>
        </div>

        <div class="neat-card p-5 space-y-2 border-t-4 border-t-rose-600 flex flex-col justify-between">
          <div>
            <h4 class="font-bold text-rose-900 text-sm">Full Technical Report</h4>
            <p class="text-gray-600 leading-relaxed">Request the complete 136-page Anna University B.Tech thesis project report PDF via email.</p>
          </div>
          <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request" class="mt-2 inline-flex items-center gap-1.5 font-bold text-rose-700 hover:underline">
            <span>Mail for Full PDF Report ✉</span>
          </a>
        </div>
      </div>
    </section>

    <!-- 8. Future Scope -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-6 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl font-extrabold brand-font text-gray-900">8. Future Research Directions</h2>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
        <div class="p-4 bg-white rounded-xl border border-gray-200/80 shadow-xs space-y-1">
          <span class="font-mono text-[#8b2252] font-bold">FINE-TUNING</span>
          <h4 class="font-bold text-gray-900">Qwen2.5 1.5B Fine-Tuning</h4>
          <p class="text-gray-600 text-[11px]">Training lightweight local LLMs specifically on C2 operations and MITRE syntaxes to eliminate hallucinations.</p>
        </div>

        <div class="p-4 bg-white rounded-xl border border-gray-200/80 shadow-xs space-y-1">
          <span class="font-mono text-[#8b2252] font-bold">GNN MODELS</span>
          <h4 class="font-bold text-gray-900">Graph Neural Networks</h4>
          <p class="text-gray-600 text-[11px]">Replacing LLM path suggestions with GNN models trained on historical red team attack graphs.</p>
        </div>

        <div class="p-4 bg-white rounded-xl border border-gray-200/80 shadow-xs space-y-1">
          <span class="font-mono text-[#8b2252] font-bold">CTF INTEGRATION</span>
          <h4 class="font-bold text-gray-900">CTFd &amp; rCTF Plugins</h4>
          <p class="text-gray-600 text-[11px]">Automated hint generation and student progress tracking during academic cyber range exercises.</p>
        </div>

        <div class="p-4 bg-white rounded-xl border border-gray-200/80 shadow-xs space-y-1">
          <span class="font-mono text-[#8b2252] font-bold">MULTI-OPERATOR</span>
          <h4 class="font-bold text-gray-900">Team Session Graphs</h4>
          <p class="text-gray-600 text-[11px]">Multi-operator coordination, deconfliction controls, and synchronized red team AI reasoning.</p>
        </div>
      </div>
    </section>

  </main>

  <!-- Clean Bottom CTA Footer -->
  <footer class="bg-white py-14 border-t border-gray-200 relative z-20">
    <div class="max-w-4xl mx-auto px-6 text-center space-y-6">
      <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">
        Request Research Artifacts &amp; Access
      </h2>

      <div class="flex flex-wrap justify-center gap-3">
        <!-- Mail for GitHub Access -->
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request" class="px-5 py-3 bg-[#8b2252] hover:bg-[#721b42] text-white rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
          <i class="fab fa-github"></i>
          <span>Request GitHub Repo Access (Mail Me)</span>
        </a>

        <!-- Mail for PDF Report -->
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request" class="px-5 py-3 bg-rose-50 border border-rose-200 hover:border-rose-300 text-rose-800 rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-xs">
          <i class="fas fa-envelope text-rose-600"></i>
          <span>Request Technical Report PDF (Mail Me)</span>
        </a>

        <a href="index.html#projects" class="px-5 py-3 bg-gray-100 hover:bg-gray-200 text-gray-900 rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-xs">
          <i class="fas fa-arrow-left text-xs"></i>
          <span>Back to Portfolio</span>
        </a>
      </div>

      <p class="text-xs text-gray-500 font-mono pt-4 border-t border-gray-100">
        © 2026 Shakthi Sri T S &amp; Pooja A — AGNI C2 Cognitive Command &amp; Control Research
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
        { y: 30, opacity: 0 },
        {
          y: 0, 
          opacity: 1, 
          duration: 0.9,
          ease: "power3.out",
          scrollTrigger: {
            trigger: el,
            start: "top 90%",
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
    f.write(html_content)

print("SUCCESSFULLY BUILT NEAT, CLEAN, AND PERFECTLY ALIGNED AGNI-C2.HTML PAGE WITH TECHSTACK.PNG!")
