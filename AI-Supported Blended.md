<!--

author:   Masub Makhdoom
email:    masub.makhdoom@ovgu.de
date:     09/04/2026
version:  30.0.0
language: en
narrator: UK English Female

repository: https://github.com/LiaScript/docs

logo:     img/logo.png

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css

link: https://raw.githubusercontent.com/OVGU-VET-TechEd/Integrating_AI_in_TVET_UNESCO/refs/heads/main/VorlageUN.css

link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css

import:   https://raw.githubusercontent.com/liaTemplates/ABCjs/main/README.md

link:     https://fonts.googleapis.com/css2?family=Noto+Sans+Egyptian+Hieroglyphs
          https://fonts.googleapis.com/css2?family=Noto+Sans+Ogham

font:     Noto Sans Egyptian Hieroglyphs, Noto Sans Ogham

-->
# Welcome
<svg viewBox="0 0 1600 900" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="35%" stop-color="#2563eb"/>
      <stop offset="70%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1600" height="900" fill="url(#bg1)"/>

  <!-- Decorative circles -->
  <circle cx="220" cy="140" r="95" fill="#22d3ee" opacity="0.15"/>
  <circle cx="1420" cy="180" r="120" fill="#f9a8d4" opacity="0.15"/>
  <circle cx="1350" cy="760" r="150" fill="#fde68a" opacity="0.12"/>
  <circle cx="220" cy="760" r="130" fill="#c4b5fd" opacity="0.15"/>

  <!-- Glass container -->
  <rect x="120" y="130" width="1360" height="640" rx="34"
        fill="rgba(255,255,255,0.12)"
        stroke="rgba(255,255,255,0.28)"/>

  <!-- Subtitle -->
  <text x="180" y="240"
        font-size="34"
        fill="#dbeafe"
        font-family="Arial"
        font-weight="700">
    SUITABLE LEARNING METHOD FOR FUTURE TVET
  </text>

  <!-- Title -->
  <text x="180" y="350"
        font-size="68"
        fill="white"
        font-family="Arial"
        font-weight="800">
    AI-Supported Blended
  </text>

  <text x="180" y="435"
        font-size="68"
        fill="white"
        font-family="Arial"
        font-weight="800">
    Competency-Based Learning
  </text>

  <!-- Description -->
  <text x="180" y="520"
        font-size="28"
        fill="#e2e8f0"
        font-family="Arial">
    Combining digital learning, AI support, practical training,
  </text>

  <text x="180" y="560"
        font-size="28"
        fill="#e2e8f0"
        font-family="Arial">
    industry projects, and competency-based assessment.
  </text>

  <!-- Name box -->
  <rect x="180" y="625" width="500" height="58" rx="29" fill="#22d3ee"/>

  <text x="430" y="662"
        text-anchor="middle"
        font-size="24"
        fill="#083344"
        font-family="Arial"
        font-weight="700">
    Masub Makhdoom & Ashika
  </text>

</svg>

<style>
:root{
  --blue:#2563eb;
  --purple:#7c3aed;
  --pink:#ec4899;
  --cyan:#06b6d4;
  --orange:#f59e0b;
  --light:#f8fafc;
  --soft:#eef2ff;
  --soft2:#ecfeff;
  --soft3:#fff7ed;
  --text:#1e293b;
}

body {
  font-family: "Segoe UI", Arial, sans-serif;
}

h1, h2, h3 {
  color: var(--text);
}

.box{
  background:white;
  border-radius:18px;
  padding:18px;
  box-shadow:0 8px 22px rgba(0,0,0,0.08);
  margin:12px 0;
  border-left:8px solid var(--blue);
}

.box2{
  background:linear-gradient(135deg,#eef2ff,#ffffff);
  border-radius:18px;
  padding:18px;
  box-shadow:0 8px 22px rgba(0,0,0,0.08);
  margin:12px 0;
  border-left:8px solid var(--purple);
}

.box3{
  background:linear-gradient(135deg,#ecfeff,#ffffff);
  border-radius:18px;
  padding:18px;
  box-shadow:0 8px 22px rgba(0,0,0,0.08);
  margin:12px 0;
  border-left:8px solid var(--cyan);
}

.box4{
  background:linear-gradient(135deg,#fff7ed,#ffffff);
  border-radius:18px;
  padding:18px;
  box-shadow:0 8px 22px rgba(0,0,0,0.08);
  margin:12px 0;
  border-left:8px solid var(--orange);
}

.grid2{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:16px;
}

.grid3{
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  gap:16px;
}

.card{
  background:white;
  border-radius:18px;
  padding:18px;
  box-shadow:0 6px 18px rgba(0,0,0,0.08);
  border:1px solid #e2e8f0;
}

.center{text-align:center;}

.cite{
  margin-top:12px;
  font-size:14px;
  color:#475569;
  font-style:italic;
}

.tag{
  display:inline-block;
  background:linear-gradient(90deg,#dbeafe,#ede9fe);
  color:#1e3a8a;
  padding:6px 12px;
  border-radius:999px;
  font-size:14px;
  font-weight:700;
  margin:4px 6px 4px 0;
}

.big{
  font-size:22px;
  font-weight:700;
}

.small{
  font-size:15px;
  color:#475569;
}
</style>

# AI-Supported Blended Competency-Based Learning for Future TVET

<svg viewBox="0 0 1600 900" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="35%" stop-color="#2563eb"/>
      <stop offset="70%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="900" fill="url(#bg1)"/>
  <circle cx="220" cy="140" r="95" fill="#22d3ee" opacity="0.15"/>
  <circle cx="1420" cy="180" r="120" fill="#f9a8d4" opacity="0.15"/>
  <circle cx="1350" cy="760" r="150" fill="#fde68a" opacity="0.12"/>
  <circle cx="220" cy="760" r="130" fill="#c4b5fd" opacity="0.15"/>

  <rect x="120" y="130" width="1360" height="640" rx="34" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.28)"/>

  <text x="180" y="240" font-size="34" fill="#dbeafe" font-family="Arial" font-weight="700">
    SUITABLE LEARNING METHOD FOR FUTURE TVET
  </text>

  <text x="180" y="350" font-size="68" fill="white" font-family="Arial" font-weight="800">
    AI-Supported Blended
  </text>

  <text x="180" y="435" font-size="68" fill="white" font-family="Arial" font-weight="800">
    Competency-Based Learning
  </text>

  <text x="180" y="520" font-size="28" fill="#e2e8f0" font-family="Arial">
    Combining digital learning, AI support, practical training,
  </text>
  <text x="180" y="560" font-size="28" fill="#e2e8f0" font-family="Arial">
    industry projects, and competency-based assessment.
  </text>

  <rect x="180" y="625" width="220" height="58" rx="29" fill="#22d3ee"/>
  <text x="290" y="662" text-anchor="middle" font-size="24" fill="#083344" font-family="Arial" font-weight="700">
    Future Skills
  </text>

  <rect x="420" y="625" width="220" height="58" rx="29" fill="#c4b5fd"/>
  <text x="530" y="662" text-anchor="middle" font-size="24" fill="#3b0764" font-family="Arial" font-weight="700">
    AI + TVET
  </text>

  <rect x="660" y="625" width="260" height="58" rx="29" fill="#f9a8d4"/>
  <text x="790" y="662" text-anchor="middle" font-size="24" fill="#831843" font-family="Arial" font-weight="700">
    Practical Learning
  </text>

  <text x="180" y="730" font-size="24" fill="#dbeafe" font-family="Arial">
    Citation: (UNESCO, 2023; OECD, 2021)
  </text>
</svg>

---

# Why Do We Need a New Method?

<div class="grid2">
  <div class="card">
    <h3>🌍 Changing Industry</h3>
    <p>Technology is evolving rapidly, and workplaces now demand new technical and digital competencies.</p>
  </div>

  <div class="card">
    <h3>📉 Skills Gap</h3>
    <p>Many learners need stronger practical skills, digital competence, and flexible ways of learning.</p>
  </div>

  <div class="card">
    <h3>💻 Digital Transformation</h3>
    <p>TVET must respond to automation, AI, smart systems, and Industry 4.0 requirements.</p>
  </div>

  <div class="card">
    <h3>🎯 Need for Personalization</h3>
    <p>Learners progress differently, so training should adapt to individual strengths and gaps.</p>
  </div>
</div>

<div class="cite">Citation: (World Economic Forum, 2023; ILO, 2022)</div>

---

# Method Overview

<div class="box">
  <div class="big">🎯 Proposed Method</div>
  AI-Supported Blended Competency-Based Learning
</div>

<div class="grid2">
  <div class="card">
    <h3>💻 Blended Learning</h3>
    <p>Combines online learning with face-to-face practical training.</p>
  </div>

  <div class="card">
    <h3>🛠 Competency-Based Training</h3>
    <p>Focuses on what learners can do in real situations.</p>
  </div>

  <div class="card">
    <h3>🤖 AI Support</h3>
    <p>Provides guidance, tutoring, feedback, and adaptive learning support.</p>
  </div>

  <div class="card">
    <h3>🏭 Industry Projects</h3>
    <p>Connects training with real workplace tasks and expectations.</p>
  </div>
</div>

<div class="box2">
  It also promotes <b>self-regulated learning</b>, where learners take more responsibility for their progress.
</div>

<div class="cite">Citation: (UNESCO-UNEVOC, 2021; European Commission, 2020)</div>

---

# How It Works

<div class="grid3">
  <div class="card center">
    <div class="big">1️⃣</div>
    <p><b>Online Theory</b><br>Students learn concepts through digital materials.</p>
  </div>

  <div class="card center">
    <div class="big">2️⃣</div>
    <p><b>AI-Guided Practice</b><br>Students receive support and instant feedback.</p>
  </div>

  <div class="card center">
    <div class="big">3️⃣</div>
    <p><b>Workshop Training</b><br>Students practice skills in labs and workshops.</p>
  </div>

  <div class="card center">
    <div class="big">4️⃣</div>
    <p><b>Industry Project</b><br>Students solve authentic tasks from the world of work.</p>
  </div>

  <div class="card center">
    <div class="big">5️⃣</div>
    <p><b>Assessment</b><br>Competence is demonstrated through performance.</p>
  </div>

  <div class="card center">
    <div class="big">🚀</div>
    <p><b>Outcome</b><br>Industry-ready learners with future skills.</p>
  </div>
</div>

<div class="cite">Citation: (UNESCO, 2023)</div>

---

# Learning Structure

<div class="box4">
  <div class="big">🧩 Five Learning Phases</div>
</div>

<div class="grid2">
  <div class="card">
    <h3>Phase 1: Digital Learning</h3>
    <p>Students study concepts through videos, slides, and interactive materials.</p>
  </div>

  <div class="card">
    <h3>Phase 2: Simulation Practice</h3>
    <p>Students practice in a safe digital environment before real application.</p>
  </div>

  <div class="card">
    <h3>Phase 3: Workshop Training</h3>
    <p>Students apply learning in hands-on workshop activities.</p>
  </div>

  <div class="card">
    <h3>Phase 4: Real Industry Task</h3>
    <p>Students work on authentic tasks linked to workplace needs.</p>
  </div>

  <div class="card" style="grid-column:1 / span 2;">
    <h3>Phase 5: Competency Assessment</h3>
    <p>Assessment measures real competence, not only memorized knowledge.</p>
  </div>
</div>

<div class="cite">Citation: (OECD, 2021; ILO, 2022)</div>

---

# Role of AI in This Method

<div class="grid2">
  <div class="card">
    <h3>🤖 Personalized Learning Path</h3>
    <p>AI can adapt learning materials to individual learner needs.</p>
  </div>

  <div class="card">
    <h3>⚡ Instant Feedback</h3>
    <p>Learners receive quick responses to improve faster.</p>
  </div>

  <div class="card">
    <h3>📊 Skill Gap Analysis</h3>
    <p>AI identifies strengths and weaknesses to guide improvement.</p>
  </div>

  <div class="card">
    <h3>🧪 Virtual Simulations</h3>
    <p>AI-enhanced simulations support safe and repeated practice.</p>
  </div>

  <div class="card" style="grid-column:1 / span 2;">
    <h3>💬 AI Tutor / Chatbot</h3>
    <p>Students can ask questions anytime and receive learning support.</p>
  </div>
</div>

<div class="cite">Citation: (UNESCO, 2023; World Economic Forum, 2023)</div>

---

# Role of the Teacher

<div class="box2">
  <div class="big">👩‍🏫 From Lecturer to Learning Facilitator</div>
</div>

<div class="grid2">
  <div class="card">
    <h3>Facilitator</h3>
    <p>Guides learning rather than only delivering content.</p>
  </div>

  <div class="card">
    <h3>Skills Coach</h3>
    <p>Supports students during practice and competence development.</p>
  </div>

  <div class="card">
    <h3>Industry Mentor</h3>
    <p>Links learning activities with workplace expectations.</p>
  </div>

  <div class="card">
    <h3>Assessment Guide</h3>
    <p>Helps learners demonstrate real performance and progress.</p>
  </div>
</div>

<div class="cite">Citation: (European Commission, 2020)</div>

---

# Role of the Learner

<div class="box3">
  <div class="big">👨‍🎓 Learner as Active Participant</div>
</div>

<div class="grid2">
  <div class="card">
    <h3>🕒 Self-Paced Learning</h3>
    <p>Learners progress according to their pace and needs.</p>
  </div>

  <div class="card">
    <h3>🛠 Practice-Based Learning</h3>
    <p>Learning is closely connected with practical application.</p>
  </div>

  <div class="card">
    <h3>📁 Project-Based Learning</h3>
    <p>Learners solve problems through meaningful projects.</p>
  </div>

  <div class="card">
    <h3>🤝 Collaborative Learning</h3>
    <p>Students learn through teamwork and communication.</p>
  </div>
</div>

<div class="cite">Citation: (OECD, 2021)</div>

---

# Tools Used in This Method

<div class="grid3">
  <div class="card center">
    <div class="big">📚</div>
    <p><b>Moodle / LMS</b><br>Manage content and learning progress</p>
  </div>

  <div class="card center">
    <div class="big">🧩</div>
    <p><b>LiaScript</b><br>Create interactive learning materials</p>
  </div>

  <div class="card center">
    <div class="big">🤖</div>
    <p><b>AI Chatbot</b><br>Provide guidance and feedback</p>
  </div>

  <div class="card center">
    <div class="big">🥽</div>
    <p><b>VR / AR</b><br>Enable immersive simulations</p>
  </div>

  <div class="card center">
    <div class="big">📁</div>
    <p><b>Digital Portfolio</b><br>Collect evidence of competence</p>
  </div>

  <div class="card center">
    <div class="big">📝</div>
    <p><b>Assessment Tools</b><br>Support continuous evaluation</p>
  </div>
</div>

<div class="cite">Citation: (UNESCO-UNEVOC, 2021)</div>

---

# Benefits for TVET

<div class="grid2">
  <div class="card">
    <h3>🎯 Industry-Ready Graduates</h3>
    <p>Learners are better prepared for real jobs.</p>
  </div>

  <div class="card">
    <h3>🔧 Strong Practical Skills</h3>
    <p>The method focuses on doing and performing.</p>
  </div>

  <div class="card">
    <h3>🔄 Flexible Learning</h3>
    <p>Students can learn in different places and formats.</p>
  </div>

  <div class="card">
    <h3>🚀 Faster Skill Development</h3>
    <p>AI support helps learners improve more efficiently.</p>
  </div>

  <div class="card" style="grid-column:1 / span 2;">
    <h3>💻 Better Digital Competence</h3>
    <p>Learners gain skills required in modern workplaces.</p>
  </div>
</div>

<div class="cite">Citation: (World Economic Forum, 2023; ILO, 2022)</div>

---

# Example from TVET Practice

<div class="box4">
  <div class="big">⚡ Electrical Student Example</div>
</div>

<div class="grid2">
  <div class="card">
    <h3>Step 1</h3>
    <p>Learn electrical theory online.</p>
  </div>

  <div class="card">
    <h3>Step 2</h3>
    <p>Practice safely in a simulation.</p>
  </div>

  <div class="card">
    <h3>Step 3</h3>
    <p>Wire a real circuit in the workshop.</p>
  </div>

  <div class="card">
    <h3>Step 4</h3>
    <p>Complete a mini industry project.</p>
  </div>

  <div class="card" style="grid-column:1 / span 2;">
    <h3>Step 5</h3>
    <p>Take a competency-based test and demonstrate skills.</p>
  </div>
</div>

<div class="cite">Citation: (UNESCO, 2023)</div>

---

# Assessment Method

<div class="box">
  <div class="big">✅ Focus on Real Competence</div>
  Assessment should measure what learners can actually do.
</div>

<div class="grid2">
  <div class="card">🛠 Practical demonstration</div>
  <div class="card">📁 Digital portfolio</div>
  <div class="card">📌 Project evaluation</div>
  <div class="card">🔄 Continuous feedback</div>
</div>

<div class="box2">
  This makes assessment more authentic, fair, and relevant for TVET.
</div>

<div class="cite">Citation: (OECD, 2021; European Commission, 2020)</div>

---

# Why Is This Suitable for Future TVET?

<div>
  <span class="tag">Industry 4.0</span>
  <span class="tag">AI in Learning</span>
  <span class="tag">Flexibility</span>
  <span class="tag">Skills Focus</span>
  <span class="tag">Lifelong Learning</span>
</div>

<div class="grid2">
  <div class="card">
    <h3>🌐 Future-Oriented</h3>
    <p>It matches the changing needs of work and technology.</p>
  </div>

  <div class="card">
    <h3>📈 Scalable</h3>
    <p>It can be used across different TVET contexts and institutions.</p>
  </div>

  <div class="card">
    <h3>🧠 Learner-Centered</h3>
    <p>It supports individual progress and personalized development.</p>
  </div>

  <div class="card">
    <h3>🏭 Practice-Oriented</h3>
    <p>It keeps learning strongly linked with industry needs.</p>
  </div>
</div>

<div class="cite">Citation: (World Economic Forum, 2023; UNESCO-UNEVOC, 2021)</div>

---

# Conclusion

<div class="box3">
  <div class="big">Final Message</div>
  AI-supported blended competency-based learning is a strong method for future TVET because it combines digital learning, practical training, AI support, industry relevance, and competency-based assessment.
</div>

<div class="box">
  It prepares learners for the changing demands of work, technology, and society.
</div>

<div class="cite">Citation: (UNESCO, 2023; OECD, 2021; ILO, 2022)</div>

---

# Short Presentation Summary

<div class="box2">
  Today, we propose AI-supported blended competency-based learning as a suitable method for future TVET. It combines online learning, AI guidance, practical workshop training, and industry projects. This method helps learners build both technical and digital competencies. Teachers act as facilitators, and learners become more active and independent. Therefore, this method is suitable for preparing students for future workplaces.
</div>

---

# References

<div class="card">
  <p><b>UNESCO.</b> (2023). <i>AI Competency Framework for Teachers</i>. Paris: UNESCO.</p>
  <p><b>UNESCO-UNEVOC.</b> (2021). <i>TVET and the Future of Work</i>. Bonn: UNESCO-UNEVOC.</p>
  <p><b>European Commission.</b> (2020). <i>Vocational Education and Training for the Future</i>. Brussels: European Commission.</p>
  <p><b>OECD.</b> (2021). <i>Skills for Jobs and Future Learning</i>. Paris: OECD Publishing.</p>
  <p><b>World Economic Forum.</b> (2023). <i>The Future of Jobs Report</i>. Geneva: World Economic Forum.</p>
  <p><b>International Labour Organization (ILO).</b> (2022). <i>Skills and Lifelong Learning for Future TVET</i>. Geneva: ILO.</p>
</div>

---

# Thank You

<svg viewBox="0 0 1600 900" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="40%" stop-color="#2563eb"/>
      <stop offset="75%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="900" fill="url(#bg2)"/>
  <circle cx="220" cy="150" r="100" fill="#ffffff" opacity="0.08"/>
  <circle cx="1400" cy="180" r="110" fill="#ffffff" opacity="0.08"/>
  <circle cx="1340" cy="760" r="120" fill="#ffffff" opacity="0.08"/>

  <rect x="190" y="190" width="1220" height="500" rx="36" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.28)"/>

  <text x="800" y="360" text-anchor="middle" font-size="86" fill="white" font-family="Arial" font-weight="800">
    Thank You
  </text>

  <text x="800" y="450" text-anchor="middle" font-size="38" fill="#e0f2fe" font-family="Arial">
    Questions and Discussion
  </text>

  <text x="800" y="540" text-anchor="middle" font-size="28" fill="#dbeafe" font-family="Arial">
    AI-Supported Blended Competency-Based Learning for Future TVET
  </text>

  <rect x="560" y="590" width="120" height="58" rx="29" fill="#22d3ee"/>
  <text x="620" y="627" text-anchor="middle" font-size="28" font-family="Arial">💡</text>

  <rect x="740" y="590" width="120" height="58" rx="29" fill="#c4b5fd"/>
  <text x="800" y="627" text-anchor="middle" font-size="28" font-family="Arial">🤖</text>

  <rect x="920" y="590" width="120" height="58" rx="29" fill="#f9a8d4"/>
  <text x="980" y="627" text-anchor="middle" font-size="28" font-family="Arial">🎓</text>
</svg>