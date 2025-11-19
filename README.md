<div align="center">
  <h2>Ni7i – curious mind in code</h2>
</div>

<div align="center" style="max-width: 800px; margin: auto; background-color: #1e1e1e; color: #f0f0f0; padding: 30px; border-radius: 12px; box-shadow: 0 0 15px rgba(255, 255, 255, 0.06); font-family: 'Fira Code', monospace;">

  <blockquote style="color:#aab7c2; margin:0 0 18px 0;">
    just start coding
  </blockquote>

  <!-- Embedded SVG: left = live badges + avatar, right = falling code animation -->
  <div style="width:100%; display:flex; justify-content:center; margin: 12px 0 20px 0;">
    <!-- The SVG is inline so it renders as part of README. Edit URLs inside if you move files. -->
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" style="max-width:1000px; border-radius:8px; background:#0b0f12;">
      <style>
        .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Fira Code", monospace; fill:#e6eef6; }
        .muted { fill:#9aa7b2; font-size:13px; font-family: ui-monospace, monospace; }
        .panel-title { fill:#a7b6c2; font-size:15px; font-weight:600; }
        .stat { font-size:20px; font-weight:700; fill:#cfefff; }
        .matrix { fill:#2ee38a; font-size:12px; letter-spacing:2px; opacity:0.92; font-family: ui-monospace, monospace; }
      </style>

      <!-- left panel -->
      <rect x="20" y="20" rx="10" ry="10" width="520" height="320" fill="#0f1416"/>
      <!-- avatar (local path per your upload) -->
      <defs>
        <pattern id="avatar" patternUnits="userSpaceOnUse" width="120" height="120">
          <image href="/mnt/data/f96c7d98-69b5-4788-bcda-f479fecdbde8.png" width="120" height="120" preserveAspectRatio="xMidYMid slice"/>
        </pattern>
      </defs>
      <circle cx="90" cy="90" r="56" fill="url(#avatar)" stroke="#091012" stroke-width="4"/>

      <text x="170" y="70" class="panel-title mono">Ni7i — curious mind in code</text>
      <text x="170" y="96" class="muted">just start <tspan style="fill:#6be7ff">coding</tspan></text>

      <!-- Live badges embedded as images (they will fetch from vercel) -->
      <g transform="translate(40,140)">
        <image href="https://github-readme-stats.vercel.app/api?username=Ni7i&show_icons=true&theme=tokyonight&hide_title=true" x="0" y="0" width="240" height="92" preserveAspectRatio="xMidYMid slice" />
        <image href="https://github-readme-stats.vercel.app/api/top-langs/?username=Ni7i&layout=compact&theme=tokyonight" x="270" y="0" width="240" height="92" preserveAspectRatio="xMidYMid slice" />
      </g>

      <!-- latest commit / hint -->
      <text x="40" y="260" class="panel-title mono">Latest commit</text>
      <text x="40" y="286" class="muted mono">fetched live by GitHub Action · updated in README</text>

      <!-- big ERROR 404 title centered-left -->
      <text x="40" y="320" class="mono" font-size="28">ERROR <tspan fill="#ffd166">404</tspan> — missing README? we fetched some data instead</text>

      <!-- right side: falling code "matrix" columns -->
      <g transform="translate(620,10)">
        <!-- repeat several columns with slightly different timings -->
        <!-- Column 1 -->
        <g transform="translate(0,-200)">
          <text class="matrix mono" x="0" y="0">
1011010101
var i = 0;
console.log('hi');
while(true){}
for(;;){}
return;
          </text>
          <animateTransform attributeName="transform" attributeType="XML" type="translate"
            from="0,-420" to="0,420" dur="5.4s" repeatCount="indefinite" begin="0s"/>
        </g>

        <!-- Column 2 -->
        <g transform="translate(36,-40)">
          <text class="matrix mono" x="0" y="0">
const ψ = '∞';
fetch('/api/status')
.then(r=>r.json());
await sleep(10);
          </text>
          <animateTransform attributeName="transform" attributeType="XML" type="translate"
            from="0,-420" to="0,420" dur="4.1s" repeatCount="indefinite" begin="0.6s"/>
        </g>

        <!-- Column 3 -->
        <g transform="translate(72,-120)">
          <text class="matrix mono" x="0" y="0">
if (!found) { search(); }
git status
git checkout -
npm run build
          </text>
          <animateTransform attributeName="transform" attributeType="XML" type="translate"
            from="0,-420" to="0,420" dur="6.0s" repeatCount="indefinite" begin="0.2s"/>
        </g>

        <!-- Column 4 -->
        <g transform="translate(108,-260)">
          <text class="matrix mono" x="0" y="0">
404? → try /api/stats
GET /repos/Ni7i/midnight-calculator
stars: ★★★☆☆
          </text>
          <animateTransform attributeName="transform" attributeType="XML" type="translate"
            from="0,-420" to="0,420" dur="5.7s" repeatCount="indefinite" begin="0.9s"/>
        </g>

        <!-- Column 5 -->
        <g transform="translate(144,-10)">
          <text class="matrix mono" x="0" y="0">
⌁ midnight
heartbeat: alive
ping → latency
console.warn('lost');
          </text>
          <animateTransform attributeName="transform" attributeType="XML" type="translate"
            from="0,-420" to="0,420" dur="4.8s" repeatCount="indefinite" begin="0.3s"/>
        </g>
      </g>

      <!-- small footer note inside svg -->
      <text x="620" y="350" class="muted mono" font-size="11">live badges are loaded from github-readme-stats · falling code is animated SVG</text>
    </svg>
  </div>

  <!-- GitHub Stats (backup / visible imgs below the svg for small screens) -->
  <div style="display:flex; gap:12px; justify-content:center; margin-bottom:14px; flex-wrap:wrap;">
    <img src="https://github-readme-stats.vercel.app/api?username=Ni7i&show_icons=true&theme=tokyonight&hide_title=true" width="48%" style="max-width:360px;"/>
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Ni7i&layout=compact&theme=tokyonight" width="48%" style="max-width:360px;"/>
  </div>

  <h3 style="margin-top:0; margin-bottom:8px;">🕒 Coding Activity</h3>
  <a href="https://wakatime.com/@292d7a0b-e3a0-4c49-8ce4-039518824561">
    <img src="https://wakatime.com/badge/user/292d7a0b-e3a0-4c49-8ce4-039518824561.svg" alt="Total time coded since May 1 2025" />
  </a>

  <hr style="border:none; height:1px; background:#121416; margin:18px 0 8px 0;">

  <details style="color:#ccd6dd; background:transparent; border-radius:6px; padding:8px;">
    <summary style="cursor:pointer; font-weight:600; color:#9aa7b2;">Bonus Thought</summary>
    <p style="margin:8px 0 0 0; font-style:italic; color:#9aa7b2;">
      Coding saves lives
    </p>
  </details>

</div>
