import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AGNI C2 | Cognitive Command & Control for Red Teaming & Cybersecurity Education</title>
  <meta name="description" content="AGNI C2: AI-Powered Cognitive Command & Control framework integrating Local LLMs for explainable offensive security workflows, MITRE ATT&CK mapping, and risk analysis. Authored by Shakthi Sri T S & Pooja A.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <script src="https://cdn.tailwindcss.com"></script>
  
  <style>
    body {
      background-color: #FAF9F5;
      color: #1F1F1F;
      font-family: 'Inter', sans-serif;
      overflow-x: hidden;
    }
    
    .brand-font {
      font-family: 'Outfit', sans-serif;
    }

    .mono-font {
      font-family: 'JetBrains Mono', monospace;
    }
    
    /* Clean Light Theme Cards */
    .light-card {
      background: #FFFFFF;
      border: 1px solid rgba(139, 34, 82, 0.12);
      box-shadow: 0 10px 35px -5px rgba(0, 0, 0, 0.05);
      border-radius: 20px;
    }
    
    .pill-tag {
      border: 1px solid rgba(139, 34, 82, 0.2);
      border-radius: 9999px;
      padding: 0.35rem 0.9rem;
      font-size: 0.75rem;
      color: #6b1d42;
      background: rgba(139, 34, 82, 0.06);
      font-weight: 600;
    }

    .keyword-tag {
      border: 1px solid rgba(15, 23, 42, 0.15);
      border-radius: 8px;
      padding: 0.3rem 0.75rem;
      font-size: 0.75rem;
      color: #334155;
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

  <!-- Navigation Bar -->
  <nav class="w-full py-5 px-6 md:px-12 flex justify-between items-center max-w-7xl mx-auto border-b border-amber-900/10 relative z-50">
    <a href="index.html#projects" class="text-gray-800 font-semibold text-sm flex items-center gap-2.5 hover:text-[#8b2252] transition-colors">
      <i class="fas fa-arrow-left text-xs"></i> Back to Portfolio
    </a>
    
    <div class="flex items-center gap-3">
      <!-- Mail Me for Full PDF Report -->
      <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request&body=Hi%20Shakthi%20Sri,%0A%0AI%20would%20like%20to%20request%20the%20full%20AGNI%20C2%20136-page%20Technical%20Report%20PDF...%0A%0AName:%20%0AOrganization/Role:%20" class="px-4 py-2 bg-rose-50 hover:bg-rose-100 text-rose-800 border border-rose-200 rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
        <i class="fas fa-envelope text-rose-600 text-sm"></i>
        <span>Request Technical Report PDF ✉</span>
      </a>
      
      <!-- Mail Me for GitHub Repo Access -->
      <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request&body=Hi%20Shakthi%20Sri,%0A%0AI%20am%20interested%20in%20requesting%20access%20to%20the%20AGNI%20C2%20GitHub%20repository...%0A%0AName:%20%0AOrganization/Role:%20" class="px-4 py-2 bg-[#8b2252] hover:bg-[#721b42] text-white rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-md">
        <i class="fab fa-github text-sm"></i>
        <span>Request GitHub Repo Access ✉</span>
      </a>
    </div>
  </nav>

  <!-- Paper Title & Header -->
  <header class="max-w-7xl mx-auto px-6 md:px-12 pt-14 pb-10 gs-reveal">
    <div class="space-y-4 border-b border-amber-900/10 pb-10">
      <div class="flex items-center gap-3">
        <span class="px-3 py-1 bg-[#8b2252]/10 text-[#8b2252] text-xs font-mono font-bold rounded-full border border-[#8b2252]/20">
          PUBLISHED RESEARCH PAPER • ICTACA'26
        </span>
        <span class="text-xs font-mono text-gray-500">ANNA UNIVERSITY B.TECH THESIS</span>
      </div>

      <h1 class="text-3xl md:text-5xl lg:text-6xl font-black brand-font tracking-tight text-gray-900 leading-tight">
        AGNI C2: Cognitive Command &amp; Control For Red Teaming And Cybersecurity Education
      </h1>

      <!-- Authors & Institution Info -->
      <div class="pt-4 flex flex-wrap items-center justify-between gap-6 border-t border-gray-200/80">
        <div class="space-y-1">
          <p class="text-base font-bold text-gray-900">
            Authors: <span class="text-[#8b2252]">Shakthi Sri T S</span> &amp; <span class="text-[#8b2252]">Pooja A</span>
          </p>
          <p class="text-xs text-gray-600">
            Department of Information Technology, Kingston Engineering College, Vellore, Tamil Nadu, India
          </p>
          <p class="text-xs font-mono text-gray-500">
            Contact Emails: <a href="mailto:srishakthi799@gmail.com" class="text-[#8b2252] underline">srishakthi799@gmail.com</a> | <a href="mailto:poojaa0042@gmail.com" class="text-[#8b2252] underline">poojaa0042@gmail.com</a>
          </p>
        </div>

        <!-- Supervisor / Institution Details -->
        <div class="text-left md:text-right space-y-1">
          <p class="text-xs font-bold text-gray-800">Anna University: Chennai 600 025</p>
          <p class="text-xs text-gray-600">Supervisor: Dr. M. Vasumathy, MS(SE)., Ph.D(CSE)</p>
          <p class="text-xs text-gray-600">HOD: Mrs. M. Menaka, M.Tech., (Ph.D)</p>
        </div>
      </div>
    </div>
  </header>

  <!-- Keywords Bar -->
  <section class="max-w-7xl mx-auto px-6 md:px-12 mb-12 gs-reveal">
    <div class="flex flex-wrap items-center gap-2 pt-2">
      <span class="text-xs font-mono font-bold text-gray-500 mr-2 uppercase">KEYWORDS:</span>
      <span class="keyword-tag">Command and Control</span>
      <span class="keyword-tag">Red Teaming</span>
      <span class="keyword-tag">Large Language Models</span>
      <span class="keyword-tag">MITRE ATT&amp;CK</span>
      <span class="keyword-tag">Cybersecurity Education</span>
      <span class="keyword-tag">Offensive Security</span>
      <span class="keyword-tag">Local LLM (Ollama)</span>
      <span class="keyword-tag">Virtual Lab</span>
    </div>
  </section>

  <!-- Abstract & Controlled Access Banner -->
  <section class="max-w-7xl mx-auto px-6 md:px-12 mb-16 space-y-8 gs-reveal">
    <div class="light-card p-8 md:p-10 border-l-4 border-l-[#8b2252] space-y-4">
      <h2 class="text-xs font-mono font-bold text-[#8b2252] uppercase tracking-widest">RESEARCH ABSTRACT</h2>
      <p class="text-base md:text-lg text-gray-800 leading-relaxed font-normal">
        Modern Command and Control (C2) frameworks used in red teaming lack integrated intelligence, real-time risk assessment, and structured learning support, creating a gap between operational execution and informed decision-making. Existing platforms are often fragmented, requiring multiple tools for session management, attack planning, and defensive mapping, while offering minimal AI-driven assistance.
      </p>
      <p class="text-sm md:text-base text-gray-700 leading-relaxed font-light">
        To address these limitations, <strong class="font-bold text-[#8b2252]">AGNI C2</strong> is developed as a unified, AI-enhanced Command and Control orchestration platform for adversary simulation and cybersecurity education. The system integrates a React-based frontend with a FastAPI backend and leverages Sliver C2 via gRPC/mTLS for secure communication. It incorporates a cognitive intelligence layer powered by local LLMs (Ollama with Qwen2.5) with fallback mechanisms, enabling real-time command explanation, attack path analysis, and detection rule generation.
      </p>
    </div>

    <!-- Restricted PDF & GitHub Mail Banner -->
    <div class="bg-gradient-to-r from-purple-50 via-rose-50 to-purple-50 border-2 border-[#8b2252]/25 rounded-3xl p-8 flex flex-col lg:flex-row items-center justify-between gap-6 shadow-sm">
      <div class="space-y-2 text-left">
        <div class="flex items-center gap-2 text-[#8b2252] font-mono text-xs font-bold uppercase tracking-wider">
          <i class="fas fa-user-shield"></i>
          <span>Restricted Research Access Notice</span>
        </div>
        <h3 class="text-xl md:text-2xl font-extrabold text-gray-900 brand-font">Need the Full 136-Page PDF Report or GitHub Repository?</h3>
        <p class="text-xs md:text-sm text-gray-600 max-w-3xl leading-relaxed">
          Due to cybersecurity confidentiality policies and offensive security research compliance, direct public downloading of the source code and full PDF thesis is restricted. Please email the author directly to request private access.
        </p>
      </div>

      <div class="flex flex-wrap sm:flex-nowrap gap-3 shrink-0">
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request" class="px-5 py-3.5 bg-rose-700 hover:bg-rose-800 text-white font-bold rounded-xl text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-md">
          <i class="fas fa-file-pdf"></i>
          <span>Mail for Full PDF Report ✉</span>
        </a>
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request" class="px-5 py-3.5 bg-[#8b2252] hover:bg-[#721b42] text-white font-bold rounded-xl text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-md">
          <i class="fab fa-github"></i>
          <span>Mail for GitHub Access ✉</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Detailed Chapter Breakdown -->
  <main class="max-w-7xl mx-auto px-6 md:px-12 mb-32 space-y-20">

    <!-- Chapter 1: Introduction & Problem Landscape -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">1. Introduction &amp; The C2 Landscape</h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- 1.1 Background -->
        <div class="light-card p-6 space-y-3">
          <h3 class="text-lg font-bold text-gray-900 brand-font flex items-center gap-2">
            <i class="fas fa-user-ninja text-[#8b2252]"></i> 1.1 Background
          </h3>
          <p class="text-xs text-gray-600 leading-relaxed">
            There is currently a global shortage of <strong>3.4 million cybersecurity professionals</strong>. Defensive capabilities lag behind sophisticated attacks. Red Team operations measure cyberdefense detection and response capabilities using adversarial simulation. C2 frameworks maintain encrypted beacons between target systems and operators.
          </p>
        </div>

        <!-- 1.2 The C2 Landscape Problem -->
        <div class="light-card p-6 space-y-3">
          <h3 class="text-lg font-bold text-gray-900 brand-font flex items-center gap-2">
            <i class="fas fa-coins text-[#8b2252]"></i> 1.2 Commercial vs Open-Source C2
          </h3>
          <p class="text-xs text-gray-600 leading-relaxed">
            Commercial C2 solutions like Cobalt Strike cost over <strong>$3,500/year per user</strong> and are closed-source. Open-source alternatives (Sliver, Covenant, Mythic, Empire) manage beacons well but require high operator experience and offer zero built-in cognitive assistance or real-time MITRE ATT&CK guidance.
          </p>
        </div>

        <!-- 1.3 The LLM Opportunity -->
        <div class="light-card p-6 space-y-3">
          <h3 class="text-lg font-bold text-gray-900 brand-font flex items-center gap-2">
            <i class="fas fa-brain text-[#8b2252]"></i> 1.3 Local LLM Opportunity
          </h3>
          <p class="text-xs text-gray-600 leading-relaxed">
            Quantized models (Qwen2.5, Llama 3) run locally on 16GB RAM hardware with sub-second response times. Cloud AI APIs (OpenAI, Anthropic, Google) leak confidential operational data, credentials, and network topologies, making local-first LLM inference mandatory for red teaming.
          </p>
        </div>
      </div>
    </section>

    <!-- Chapter 2: Evolution Timeline of C2 Frameworks -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">2. Literature Review: Evolution of C2 Frameworks</h2>
      </div>

      <div class="light-card p-6 md:p-8 space-y-6">
        <p class="text-xs text-gray-600 leading-relaxed">
          Historical overview of Command &amp; Control framework evolution leading up to AGNI C2's cognitive layer:
        </p>

        <!-- Timeline Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200/80 space-y-1.5">
            <span class="text-xs font-mono font-bold text-[#8b2252]">2003 • METERPRETER</span>
            <h4 class="text-sm font-bold text-gray-900">Single-Instance Plugins</h4>
            <p class="text-[11px] text-gray-600">Early post-exploitation plugins. Single command-and-control instances without multiplexed beacon management.</p>
          </div>

          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200/80 space-y-1.5">
            <span class="text-xs font-mono font-bold text-[#8b2252]">2012 • COBALT STRIKE</span>
            <h4 class="text-sm font-bold text-gray-900">Team Server &amp; Malleable C2</h4>
            <p class="text-[11px] text-gray-600">Pioneered team server architecture, sleep/jitter beacons, and GUI clients. Closed-source ($3,500/yr).</p>
          </div>

          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200/80 space-y-1.5">
            <span class="text-xs font-mono font-bold text-[#8b2252]">2015-2019 • EMPIRE / MYTHIC</span>
            <h4 class="text-sm font-bold text-gray-900">PowerShell &amp; Modular Agents</h4>
            <p class="text-[11px] text-gray-600">Empire introduced web interfaces (Starkiller). Mythic introduced modular payload types (Apollo, Medusa, Poseidon).</p>
          </div>

          <div class="p-4 bg-purple-50 rounded-xl border border-[#8b2252]/30 space-y-1.5">
            <span class="text-xs font-mono font-bold text-[#8b2252]">2020-2026 • SLIVER &amp; AGNI C2</span>
            <h4 class="text-sm font-bold text-gray-900">Embedded Cognitive AI</h4>
            <p class="text-[11px] text-gray-700">Sliver provided mTLS &amp; gRPC API. AGNI C2 embeds local LLMs for command explanation &amp; attack path reasoning.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Chapter 3 & 4: Problem Statement & Core Objectives -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">3. Problem Statement &amp; 4. Core Objectives</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- 3 Specific Problems -->
        <div class="light-card p-6 md:p-8 space-y-4 border-l-4 border-l-rose-600">
          <h3 class="text-lg font-bold text-rose-900 brand-font uppercase tracking-wide">3 Identifed Problems</h3>

          <div class="space-y-3 text-xs text-gray-700">
            <div class="p-3 bg-rose-50/50 rounded-xl border border-rose-100">
              <strong class="text-rose-950 font-bold block mb-0.5">Problem 1: No Integrated Intelligence in C2</strong>
              Operators must manage multiple tabs for MITRE ATT&amp;CK documentation, command syntaxes, and threat intelligence.
            </div>

            <div class="p-3 bg-rose-50/50 rounded-xl border border-rose-100">
              <strong class="text-rose-950 font-bold block mb-0.5">Problem 2: Cloud-Dependent AI Risk</strong>
              Sending C2 terminal outputs and target system configurations to cloud LLM APIs leaks sensitive operational IP under NDA.
            </div>

            <div class="p-3 bg-rose-50/50 rounded-xl border border-rose-100">
              <strong class="text-rose-950 font-bold block mb-0.5">Problem 3: Educational C2 Feedback Lag</strong>
              Students face static documentation and massive feedback delays during hands-on cybersecurity exercises.
            </div>
          </div>
        </div>

        <!-- 4 Objectives -->
        <div class="light-card p-6 md:p-8 space-y-4 border-l-4 border-l-[#8b2252]">
          <h3 class="text-lg font-bold text-[#8b2252] brand-font uppercase tracking-wide">4 Primary Objectives</h3>

          <div class="space-y-3 text-xs text-gray-700">
            <div class="p-3 bg-purple-50/50 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block mb-0.5">Objective 1: Local-First Open-Source C2</strong>
              Operate completely on consumer hardware (16GB RAM laptop) with zero cloud dependency using Ollama.
            </div>

            <div class="p-3 bg-purple-50/50 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block mb-0.5">Objective 2: Real-Time Integrated Assistance</strong>
              Provide command explanations, attack path reasoning, pre-execution risk scoring, and detection rule generation.
            </div>

            <div class="p-3 bg-purple-50/50 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block mb-0.5">Objective 3: Isolated VirtualBox Lab</strong>
              Deploy an isolated academic cyber range with Kali Linux attack VM and Windows victim VM.
            </div>

            <div class="p-3 bg-purple-50/50 rounded-xl border border-purple-100">
              <strong class="text-[#8b2252] font-bold block mb-0.5">Objective 4: Educational Distribution</strong>
              Distribute with comprehensive research documentation for authorized academic training.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Chapter 5 & 6: System Architecture & Figures -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">5. System Architecture &amp; Diagrams</h2>
      </div>

      <!-- Architecture Diagram Image -->
      <div class="light-card p-4 md:p-6 overflow-hidden rounded-3xl border border-gray-200 shadow-xl bg-white space-y-4">
        <img src="agni_arch_diagram.png" alt="AGNI C2 Overall System Architecture Diagram" class="w-full h-auto object-contain rounded-2xl block border border-gray-100 mx-auto max-h-[750px]">
        <p class="text-center text-xs font-mono text-gray-500">Figure 3.1: AGNI C2 Overall System Architecture &amp; Module Interaction Diagram</p>
      </div>

      <!-- Design Principles Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-2">
          <span class="text-xs font-mono font-bold text-[#8b2252]">PRINCIPLE 1</span>
          <h4 class="text-sm font-bold text-gray-900">Embedded AI Capability</h4>
          <p class="text-xs text-gray-600">AI support is embedded directly inside the operator command terminal to prevent task switching.</p>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-2">
          <span class="text-xs font-mono font-bold text-[#8b2252]">PRINCIPLE 2</span>
          <h4 class="text-sm font-bold text-gray-900">Local-First Inference</h4>
          <p class="text-xs text-gray-600">Command outputs never leave the local environment, preserving complete operational data privacy.</p>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-2">
          <span class="text-xs font-mono font-bold text-[#8b2252]">PRINCIPLE 3</span>
          <h4 class="text-sm font-bold text-gray-900">Real-Time Telemetry</h4>
          <p class="text-xs text-gray-600">Instant WebSocket updates under 100ms for beacon state changes and command execution output.</p>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-2">
          <span class="text-xs font-mono font-bold text-[#8b2252]">PRINCIPLE 4</span>
          <h4 class="text-sm font-bold text-gray-900">Auxiliary Fallback Chain</h4>
          <p class="text-xs text-gray-600">Ollama local LLM → Static Knowledge Base → Configured Cloud Provider with explicit warning.</p>
        </div>
      </div>
    </section>

    <!-- Chapter 7: Tech Stack & System Modules -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">7. Technology Stack &amp; Implementation</h2>
      </div>

      <!-- Tech Stack Table & Logos -->
      <div class="light-card p-6 md:p-8 space-y-6">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-gray-100 pb-4">
          <h3 class="text-xl font-bold text-gray-900 brand-font">Implementation Technology Stack</h3>
          <span class="pill-tag font-mono text-xs">Production Ready Specifications</span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs text-gray-700">
            <thead class="bg-gray-50 font-mono text-gray-900 uppercase border-b border-gray-200">
              <tr>
                <th class="p-3">Technology</th>
                <th class="p-3">Version</th>
                <th class="p-3">Role / Purpose in AGNI C2</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 font-mono">
              <tr><td class="p-3 font-bold text-[#8b2252]">React</td><td class="p-3">18.2</td><td class="p-3 font-sans">Single Page Application UI Framework</td></tr>
              <tr><td class="p-3 font-bold text-[#8b2252]">TypeScript</td><td class="p-3">5.0</td><td class="p-3 font-sans">End-to-End Type Safety</td></tr>
              <tr><td class="p-3 font-bold text-[#8b2252]">Tailwind CSS</td><td class="p-3">3.3</td><td class="p-3 font-sans">Utility-first styling &amp; design system</td></tr>
              <tr><td class="p-3 font-bold text-[#8b2252]">FastAPI</td><td class="p-3">0.100</td><td class="p-3 font-sans">Asynchronous REST &amp; WebSocket API backend</td></tr>
              <tr><td class="p-3 font-bold text-[#8b2252]">Sliver C2</td><td class="p-3">Latest</td><td class="p-3 font-sans">gRPC / mTLS C2 Server Integration</td></tr>
              <tr><td class="p-3 font-bold text-[#8b2252]">Ollama (Qwen2.5)</td><td class="p-3">0.1</td><td class="p-3 font-sans">Local LLM Runtime for embedded cognitive AI</td></tr>
              <tr><td class="p-3 font-bold text-[#8b2252]">SQLite &amp; SQLAlchemy</td><td class="p-3">2.0</td><td class="p-3 font-sans">Persistence ORM for sessions, beacons &amp; loot</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Modules UI Screenshots Showcase -->
      <div class="space-y-12 pt-4">
        <!-- Dashboard UI -->
        <div class="light-card p-6 md:p-8 space-y-4">
          <div class="flex justify-between items-center border-b border-gray-100 pb-3">
            <h3 class="text-xl font-bold text-gray-900 brand-font">Dashboard &amp; Main Overview Interface</h3>
            <span class="pill-tag font-mono text-xs">Figure 4.1</span>
          </div>
          <div class="overflow-hidden rounded-xl border border-gray-200 shadow-md">
            <img src="agni_dashboard_ui.png" alt="AGNI C2 Dashboard Interface" class="w-full h-auto object-cover block">
          </div>
        </div>

        <!-- Operator Panel -->
        <div class="light-card p-6 md:p-8 space-y-4">
          <div class="flex justify-between items-center border-b border-gray-100 pb-3">
            <h3 class="text-xl font-bold text-gray-900 brand-font">Operator Panel &amp; Session Beacon View</h3>
            <span class="pill-tag font-mono text-xs">Figure 4.2</span>
          </div>
          <div class="overflow-hidden rounded-xl border border-gray-200 shadow-md">
            <img src="agni_operator_panel.png" alt="AGNI C2 Operator Panel" class="w-full h-auto object-cover block">
          </div>
        </div>

        <!-- Network Topology Map -->
        <div class="light-card p-6 md:p-8 space-y-4">
          <div class="flex justify-between items-center border-b border-gray-100 pb-3">
            <h3 class="text-xl font-bold text-gray-900 brand-font">Network Visualization &amp; Topology Graph</h3>
            <span class="pill-tag font-mono text-xs">Figure 4.8</span>
          </div>
          <div class="overflow-hidden rounded-xl border border-gray-200 shadow-md">
            <img src="agni_network_topology.png" alt="Network Topology Graph" class="w-full h-auto object-cover block">
          </div>
        </div>

        <!-- Two Column: MITRE ATT&CK & Playbook Builder -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div class="light-card p-6 space-y-4">
            <div class="flex justify-between items-center border-b border-gray-100 pb-3">
              <h3 class="text-lg font-bold text-gray-900 brand-font">MITRE ATT&amp;CK Browser</h3>
              <span class="pill-tag font-mono text-xs">Figure 4.11</span>
            </div>
            <div class="overflow-hidden rounded-xl border border-gray-200">
              <img src="agni_mitre_attack.png" alt="MITRE ATT&CK Browser" class="w-full h-auto object-cover block">
            </div>
          </div>

          <div class="light-card p-6 space-y-4">
            <div class="flex justify-between items-center border-b border-gray-100 pb-3">
              <h3 class="text-lg font-bold text-gray-900 brand-font">Visual Playbook Flow Builder</h3>
              <span class="pill-tag font-mono text-xs">Figure 4.5</span>
            </div>
            <div class="overflow-hidden rounded-xl border border-gray-200">
              <img src="agni_playbook_builder.png" alt="Playbook Builder" class="w-full h-auto object-cover block">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Chapter 9 & 10: 5 Core Algorithms & Results -->
    <section class="gs-reveal space-y-8">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">9. 5 Core Cognitive Intelligence Algorithms</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="light-card p-6 space-y-2 border-t-4 border-t-[#8b2252]">
          <h4 class="text-lg font-bold text-[#8b2252]">1. Command Explanation Engine</h4>
          <p class="text-xs text-gray-600 leading-relaxed">Parses raw terminal flags and translates complex offensive commands into structured human-readable explanations.</p>
        </div>

        <div class="light-card p-6 space-y-2 border-t-4 border-t-indigo-600">
          <h4 class="text-lg font-bold text-indigo-900">2. Command Risk Scoring</h4>
          <p class="text-xs text-gray-600 leading-relaxed">Evaluates OPSEC risk (0-100) before command dispatch based on process creation, network noise, and artifact footprints.</p>
        </div>

        <div class="light-card p-6 space-y-2 border-t-4 border-t-purple-600">
          <h4 class="text-lg font-bold text-purple-900">3. Lateral Movement Suggester</h4>
          <p class="text-xs text-gray-600 leading-relaxed">Analyzes domain trust relationships and credentials to suggest optimal attack paths across the network topology.</p>
        </div>

        <div class="light-card p-6 space-y-2 border-t-4 border-t-[#8b2252]">
          <h4 class="text-lg font-bold text-[#8b2252]">4. Automated Detection Rule Generator</h4>
          <p class="text-xs text-gray-600 leading-relaxed">Generates Sigma and YARA rules automatically for executed commands to facilitate Blue Team defense gap analysis.</p>
        </div>

        <div class="light-card p-6 space-y-2 border-t-4 border-t-indigo-600">
          <h4 class="text-lg font-bold text-indigo-900">5. Intent Compiler</h4>
          <p class="text-xs text-gray-600 leading-relaxed">Translates high-level natural language operator requests into OPSEC-safe low-level terminal commands via Local LLMs.</p>
        </div>

        <div class="light-card p-6 space-y-2 border-t-4 border-t-rose-600 flex flex-col justify-between">
          <div>
            <h4 class="text-lg font-bold text-rose-900">Request Full PDF Thesis</h4>
            <p class="text-xs text-gray-600 leading-relaxed">Request the complete 136-page Anna University B.Tech thesis project report via email.</p>
          </div>
          <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request" class="mt-3 inline-flex items-center gap-2 text-xs font-bold text-rose-700 hover:underline">
            <span>Mail for Full PDF Report ✉</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Chapter 10.3: Future Scope -->
    <section class="gs-reveal space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-1 bg-[#8b2252] rounded-full"></span>
        <h2 class="text-2xl md:text-3xl font-extrabold brand-font text-gray-900">10.3 Future Research Scope</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-1.5">
          <h4 class="text-xs font-mono font-bold text-[#8b2252]">MODEL FINE-TUNING</h4>
          <p class="text-xs text-gray-700 font-bold">Fine-Tuned Qwen2.5 1.5B</p>
          <p class="text-[11px] text-gray-600">Fine-tuning lightweight LLMs specifically on C2 operations and MITRE ATT&amp;CK syntaxes to eliminate hallucinations.</p>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-1.5">
          <h4 class="text-xs font-mono font-bold text-[#8b2252]">PATH PREDICTION</h4>
          <p class="text-xs text-gray-700 font-bold">Graph Neural Networks (GNN)</p>
          <p class="text-[11px] text-gray-600">Replacing LLM path suggestions with GNN models trained on historical red team attack graphs.</p>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-1.5">
          <h4 class="text-xs font-mono font-bold text-[#8b2252]">ACADEMIC CTF</h4>
          <p class="text-xs text-gray-700 font-bold">CTFd &amp; rCTF Integration</p>
          <p class="text-[11px] text-gray-600">Plugins for automated hint generation and student progress tracking during cyber range challenges.</p>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-gray-200/80 shadow-sm space-y-1.5">
          <h4 class="text-xs font-mono font-bold text-[#8b2252]">MULTI-OPERATOR</h4>
          <p class="text-xs text-gray-700 font-bold">Team C2 Synchronization</p>
          <p class="text-[11px] text-gray-600">Shared session graphs, deconfliction controls, and multi-operator coordinated AI reasoning.</p>
        </div>
      </div>
    </section>

  </main>

  <!-- Bottom CTA Footer -->
  <footer class="bg-white py-16 border-t border-gray-200 relative z-20">
    <div class="max-w-7xl mx-auto px-6 md:px-12 text-center space-y-8">
      <h2 class="text-3xl font-extrabold brand-font text-gray-900">
        Request Research Artifacts &amp; Access
      </h2>

      <div class="flex flex-wrap justify-center gap-4">
        <!-- Mail for GitHub Access -->
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Repository%20Access%20Request" class="px-6 py-3.5 bg-[#8b2252] hover:bg-[#721b42] text-white rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-md">
          <i class="fab fa-github text-sm"></i>
          <span>Request GitHub Repo Access (Mail Me)</span>
        </a>

        <!-- Mail for PDF Report -->
        <a href="mailto:srishakthi799@gmail.com?subject=AGNI%20C2%20Technical%20Report%20PDF%20Request" class="px-6 py-3.5 bg-rose-50 border border-rose-200 hover:border-rose-400 text-rose-800 rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
          <i class="fas fa-envelope text-rose-600 text-sm"></i>
          <span>Request Technical Report PDF (Mail Me)</span>
        </a>

        <a href="index.html#projects" class="px-6 py-3.5 bg-gray-100 hover:bg-gray-200 text-gray-900 rounded-xl font-bold text-xs flex items-center gap-2 transition-all hover:scale-105 shadow-sm">
          <i class="fas fa-arrow-left text-xs"></i>
          <span>Back to Main Portfolio</span>
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
    f.write(html_content)

print("SUCCESSFULLY WRITTEN COMPREHENSIVE LIGHT THEME AGNI-C2.HTML PAGE WITH COMPLETE REPORT CONTENT AND MAIL REQUEST BUTTONS!")
