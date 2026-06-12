[Karen Tonoyan Benchmark (KTB-300)


<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>KTB-300: Cognitive Rigor Benchmark</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=JetBrains+Mono:wght@400;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "on-primary": "#003640",
                        "on-error-container": "#ffdad6",
                        "on-primary-fixed": "#001f26",
                        "surface-container": "#1c1f29",
                        "surface-container-low": "#181b25",
                        "secondary-container": "#3a4a5f",
                        "surface-container-highest": "#31343f",
                        "primary-container": "#06b6d4",
                        "on-secondary-container": "#a9bad3",
                        "surface-tint": "#4cd7f6",
                        "secondary": "#b7c8e1",
                        "surface-container-high": "#272a34",
                        "surface-container-lowest": "#0b0e17",
                        "tertiary-fixed-dim": "#bec6e0",
                        "surface-bright": "#363943",
                        "tertiary-fixed": "#dae2fd",
                        "surface": "#10131c",
                        "on-tertiary-fixed": "#131b2e",
                        "error-container": "#93000a",
                        "on-secondary": "#213145",
                        "on-background": "#e0e2ef",
                        "on-surface-variant": "#bcc9cd",
                        "inverse-on-surface": "#2d303a",
                        "outline-variant": "#3d494c",
                        "surface-dim": "#10131c",
                        "inverse-surface": "#e0e2ef",
                        "surface-variant": "#31343f",
                        "primary-fixed-dim": "#4cd7f6",
                        "on-secondary-fixed": "#0b1c30",
                        "secondary-fixed": "#d3e4fe",
                        "on-surface": "#e0e2ef",
                        "tertiary-container": "#9ea6bf",
                        "inverse-primary": "#00687a",
                        "primary": "#4cd7f6",
                        "on-primary-container": "#00424f",
                        "primary-fixed": "#acedff",
                        "outline": "#869397",
                        "on-tertiary": "#283044",
                        "error": "#ffb4ab",
                        "tertiary": "#bec6e0",
                        "on-primary-fixed-variant": "#004e5c",
                        "on-tertiary-fixed-variant": "#3f465c",
                        "on-secondary-fixed-variant": "#38485d",
                        "on-error": "#690005",
                        "background": "#10131c",
                        "secondary-fixed-dim": "#b7c8e1",
                        "on-tertiary-container": "#343c50"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "max-width": "1440px",
                        "md": "16px",
                        "unit": "4px",
                        "xl": "32px",
                        "margin-mobile": "16px",
                        "lg": "24px",
                        "sm": "8px",
                        "xs": "4px",
                        "margin-desktop": "32px"
                    },
                    "fontFamily": {
                        "display-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "body-base": ["Inter"],
                        "label-caps": ["Inter"],
                        "code-sm": ["JetBrains Mono"],
                        "body-bold": ["Inter"],
                        "stat-lg": ["Inter"]
                    },
                    "fontSize": {
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-base": ["16px", {"lineHeight": "24px", "letterSpacing": "0", "fontWeight": "400"}],
                        "label-caps": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "code-sm": ["14px", {"lineHeight": "20px", "letterSpacing": "0", "fontWeight": "400"}],
                        "body-bold": ["16px", {"lineHeight": "24px", "letterSpacing": "0", "fontWeight": "600"}],
                        "stat-lg": ["36px", {"lineHeight": "44px", "letterSpacing": "-0.02em", "fontWeight": "700"}]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #070a13;
            color: #e0e2ef;
        }
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 16px;
        }
        .code-block {
            background-color: #0b0f19;
            border: 1px solid #1e293b;
        }
        .precision-outline {
            border: 1px solid #1e293b;
        }
        .active-accent {
            border-left: 3px solid #06b6d4;
        }
        .glow-accent {
            box-shadow: 0 0 12px rgba(6, 182, 212, 0.1);
        }
    </style>
</head>
<body class="font-body-base text-body-base selection:bg-primary-container selection:text-on-primary-container">
<!-- Top Navigation -->
<nav class="w-full top-0 sticky bg-surface border-b border-outline-variant z-50">
<div class="flex justify-between items-center h-16 px-lg max-w-max-width mx-auto">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-primary" style="font-variation-settings: 'FILL' 1;">terminal</span>
<span class="font-display-lg text-display-lg font-bold text-primary tracking-tighter">KTB-300</span>
</div>
<div class="hidden md:flex gap-xl">
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" href="#overview">Overview</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" href="#structure">Dataset</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" href="#schema">Schema</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" href="#scoring">Scoring</a>
</div>
<a class="px-md py-xs border border-outline text-primary font-label-caps text-label-caps hover:bg-primary hover:text-on-primary transition-all active:scale-95" href="https://github.com/Karen86Tonoyan/LLM-Advanced-Reasoning-Hard-Karen-Tonoyan-Benchmark">
                GitHub Repository
            </a>
</div>
</nav>
<!-- Side Navigation (Desktop Only) -->
<aside class="hidden lg:flex flex-col py-xl gap-md h-full w-80 fixed left-0 top-16 bg-surface-container border-r border-outline-variant">
<div class="px-lg pb-md border-b border-outline-variant mb-md">
<span class="font-headline-md text-headline-md text-primary">Documentation</span>
</div>
<div class="flex flex-col">
<a class="flex items-center gap-sm py-md px-lg bg-secondary-container text-on-secondary-container border-l-4 border-primary rounded-r-full" href="#">
<span class="material-symbols-outlined">analytics</span>
<span>Benchmark Overview</span>
</a>
<a class="flex items-center gap-sm py-md px-lg text-on-surface-variant hover:bg-surface-container-high transition-all" href="#">
<span class="material-symbols-outlined">database</span>
<span>Dataset Explorer</span>
</a>
<a class="flex items-center gap-sm py-md px-lg text-on-surface-variant hover:bg-surface-container-high transition-all" href="#">
<span class="material-symbols-outlined">code</span>
<span>JSON Schema</span>
</a>
<a class="flex items-center gap-sm py-md px-lg text-on-surface-variant hover:bg-surface-container-high transition-all" href="#">
<span class="material-symbols-outlined">rule</span>
<span>Scoring Rubric</span>
</a>
</div>
</aside>
<main class="lg:ml-80 max-w-max-width mx-auto px-lg py-xl">
<!-- Hero Section -->
<section class="mb-xl relative overflow-hidden bg-surface-container-low rounded-xl precision-outline p-xl flex flex-col md:flex-row items-center gap-xl border-tertiary">
<div class="flex-1 space-y-md">
<h1 class="font-display-lg text-display-lg text-primary tracking-tighter">KTB-300: Cognitive Rigor</h1>
<p class="font-headline-md text-headline-md text-on-surface-variant max-w-2xl">
                    Stress-testing the reasoning limits of Large Language Models through high-fidelity curated evaluation.
                </p>
<div class="flex gap-md pt-md">
<button class="px-xl py-md bg-primary-container text-on-primary-container font-body-bold text-body-bold rounded-lg hover:brightness-110 active:scale-95 transition-all">Get Started</button>
<button class="px-xl py-md border border-outline text-primary font-body-bold text-body-bold rounded-lg hover:bg-surface-container-highest active:scale-95 transition-all">View Dataset</button>
</div>
</div>
<div class="w-full md:w-1/3 flex justify-center">
<div class="w-full h-full flex flex-col items-center gap-sm">https://lh3.googleusercontent.com/aida-public/AB6AXuAvuAPBpWiySWhw-bnufqMvL-t7iiCKDkNgwrYnGMy-ZTJA8Y5rg0u22RWtiSmzQfgPilYzXC8_-VeE36wS-IMlHLd_idZ0dp94eZhdEUjBOPDLWZHYCRtCfzef1rJqiKxyFssdgayrisms5nKAnScFqLRpkjiP4tnD7W4tIZqin5-LUqCh2Ak47y8Yk3HzbyYyT2rsZO1dNOWC9cTi-N3ZFyYfEb-nRRmxmQTzpzhCXPp65OxCG39IwKaJJHTgweEsifUBny5cKho<p class="font-label-caps text-label-caps text-tertiary tracking-widest uppercase">by Karen Tonoyan</p></div>
</div>
</section>
<!-- Bento Overview -->
<section class="mb-xl" id="overview">
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">psychology</span> Overview: What is KTB-300?
            </h2>
<div class="bento-grid">
<!-- Large Feature Card -->
<div class="col-span-12 md:col-span-8 bg-surface-container precision-outline p-lg active-accent glow-accent border-tertiary">
<p class="font-body-base text-body-base leading-relaxed mb-md">
                        The <span class="text-primary font-body-bold">Karen Tonoyan Benchmark (KTB-300)</span> is a curated set of 300 "hard" questions engineered to move beyond surface-level pattern matching. It targets the "Reasoning Gap" — the critical space between sounding correct and being logically sound.
                    </p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-md mt-lg">
<div class="p-md bg-surface-container-low rounded precision-outline">
<span class="material-symbols-outlined text-primary mb-sm">account_tree</span>
<h3 class="font-body-bold text-body-bold text-on-surface mb-xs">Advanced Reasoning</h3>
<p class="text-sm text-on-surface-variant">Complex multi-step logical chains that require sustained internal consistency.</p>
</div>
<div class="p-md bg-surface-container-low rounded precision-outline">
<span class="material-symbols-outlined text-primary mb-sm">question_mark</span>
<h3 class="font-body-bold text-body-bold text-on-surface mb-xs">Uncertainty Awareness</h3>
<p class="text-sm text-on-surface-variant">Explicitly identifies when prompts are unanswerable or conceptually ambiguous.</p>
</div>
</div>
</div>
<!-- Small Stats Cards -->
<div class="col-span-12 md:col-span-4 grid grid-rows-2 gap-md">
<div class="bg-surface-container precision-outline p-lg flex flex-col justify-center">
<span class="material-symbols-outlined text-error mb-sm">block</span>
<h3 class="font-body-bold text-body-bold text-on-surface">Hallucination Resistance</h3>
<p class="text-sm text-on-surface-variant">Strict logic boundaries that punish inventive or creative "hallucinated" steps.</p>
</div>
<div class="bg-surface-container precision-outline p-lg flex flex-col justify-center">
<span class="material-symbols-outlined text-tertiary mb-sm">rebase_edit</span>
<h3 class="font-body-bold text-body-bold text-on-surface">Causal Inference</h3>
<p class="text-sm text-on-surface-variant">Rigorous evaluation of cause-and-effect relationships under high-noise scenarios.</p>
</div>
</div>
</div>
</section>
<!-- Dataset Structure -->
<section class="mb-xl" id="structure">
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">data_table</span> Dataset Structure
            </h2>
<div class="bg-surface-container precision-outline overflow-hidden rounded-lg">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-highest border-b border-outline-variant">
<th class="px-lg py-md font-label-caps text-label-caps text-primary">Set</th>
<th class="px-lg py-md font-label-caps text-label-caps text-primary">Questions</th>
<th class="px-lg py-md font-label-caps text-label-caps text-primary">Language</th>
<th class="px-lg py-md font-label-caps text-label-caps text-primary">Use Case</th>
</tr>
</thead>
<tbody class="text-sm">
<tr class="border-b border-outline-variant hover:bg-surface-container-high transition-colors">
<td class="px-lg py-md font-code-sm font-bold">EN-GOLD</td>
<td class="px-lg py-md">100</td>
<td class="px-lg py-md">English</td>
<td class="px-lg py-md text-on-surface-variant">Hard auto-eval against objective <code class="text-primary-fixed bg-surface px-1">gold_answer</code>.</td>
</tr>
<tr class="border-b border-outline-variant hover:bg-surface-container-high transition-colors">
<td class="px-lg py-md font-code-sm font-bold">PL-SAFETY</td>
<td class="px-lg py-md">100</td>
<td class="px-lg py-md">Polish</td>
<td class="px-lg py-md text-on-surface-variant">Testing hallucinations, uncertainty, and adversarial safety.</td>
</tr>
<tr class="hover:bg-surface-container-high transition-colors">
<td class="px-lg py-md font-code-sm font-bold">PL-MIX</td>
<td class="px-lg py-md">100</td>
<td class="px-lg py-md">Polish</td>
<td class="px-lg py-md text-on-surface-variant">Logic, planning, debugging, and linguistic nuance.</td>
</tr>
</tbody>
</table>
</div>
</section>
<!-- Repo Structure -->
<section class="mb-xl grid grid-cols-1 lg:grid-cols-2 gap-xl" id="repo">
<div>
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">folder_open</span> Repository Structure
                </h2>
<div class="code-block p-lg font-code-sm text-code-sm text-on-surface-variant rounded-lg">
<pre><code>.
├── data/                  <span class="text-primary-fixed"># KTB-300 dataset files (.jsonl)</span>
├── docs/
│   ├── rubric.md          <span class="text-primary-fixed"># 1 / 0.5 / 0 evaluation criteria</span>
│   ├── categories.md      <span class="text-primary-fixed"># Detailed category definitions</span>
│   └── installation.md    <span class="text-primary-fixed"># Environment setup</span>
├── schemas/
│   └── ktb.schema.json    <span class="text-primary-fixed"># JSON Schema validation</span>
├── scripts/
│   ├── validate_jsonl.py  <span class="text-primary-fixed"># Validation utility</span>
│   └── run_eval_stub.py   <span class="text-primary-fixed"># Baseline script</span>
└── README.md              <span class="text-primary-fixed"># Project documentation</span></code></pre>
</div>
</div>
<!-- Dataset Format -->
<div id="schema">
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">schema</span> Dataset Format
                </h2>
<div class="code-block p-lg font-code-sm text-code-sm text-on-surface-variant rounded-lg">
<pre><code class="text-tertiary">{
  "id": "KTB-001",
  "set": "EN-GOLD",
  "category": "logic",
  "difficulty": 5,
  "question": "Detailed reasoning prompt...",
  "gold_answer": "Expected logical output",
  "tags": ["causal", "multi-step"],
  "mono": true
}</code></pre>
</div>
</div>
</section>
<!-- Scoring Rubric -->
<section class="mb-xl" id="scoring">
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">balance</span> Scoring (The KTB Rubric)
            </h2>
<div class="grid grid-cols-1 md:grid-cols-3 gap-md">
<div class="bg-surface-container precision-outline p-lg rounded-lg border-l-4 border-primary">
<div class="flex justify-between items-center mb-sm">
<span class="font-stat-lg text-stat-lg text-primary">1.0</span>
<span class="px-sm py-1 bg-primary/20 text-primary rounded-full text-xs font-bold uppercase tracking-widest">Full</span>
</div>
<p class="text-sm text-on-surface-variant">Correct answer with sound, verifiable logic. No gaps in reasoning chains.</p>
</div>
<div class="bg-surface-container precision-outline p-lg rounded-lg border-l-4 border-tertiary">
<div class="flex justify-between items-center mb-sm">
<span class="font-stat-lg text-stat-lg text-tertiary">0.5</span>
<span class="px-sm py-1 bg-tertiary/20 text-tertiary rounded-full text-xs font-bold uppercase tracking-widest">Partial</span>
</div>
<p class="text-sm text-on-surface-variant">Correct answer but flawed/weak reasoning, or minor hallucination in intermediate steps.</p>
</div>
<div class="bg-surface-container precision-outline p-lg rounded-lg border-l-4 border-error">
<div class="flex justify-between items-center mb-sm">
<span class="font-stat-lg text-stat-lg text-error">0.0</span>
<span class="px-sm py-1 bg-error/20 text-error rounded-full text-xs font-bold uppercase tracking-widest">Fail</span>
</div>
<p class="text-sm text-on-surface-variant">Incorrect answer or significant logical failure. Complete hallucination of facts.</p>
</div>
</div>
</section>
<!-- Quick Start & Evaluation -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-xl">
<section id="quickstart">
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">rocket_launch</span> Quick Start
                </h2>
<div class="code-block p-lg font-code-sm text-code-sm text-on-surface rounded-lg relative">
<button class="absolute top-md right-md text-on-surface-variant hover:text-primary transition-colors">
<span class="material-symbols-outlined">content_copy</span>
</button>
<pre><code><span class="text-outline"># Clone the repository</span>
git clone https://github.com/Karen86Tonoyan/KTB-300.git

<span class="text-outline"># Install dependencies</span>
pip install -r requirements.txt

<span class="text-outline"># Validate the dataset</span>
python scripts/validate_jsonl.py data/ktb_300.jsonl</code></pre>
</div>
</section>
<section id="eval">
<h2 class="font-headline-md text-headline-md text-primary mb-lg flex items-center gap-sm">
<span class="material-symbols-outlined">grading</span> How to Evaluate
                </h2>
<div class="bg-surface-container precision-outline p-lg rounded-lg space-y-md">
<div class="flex gap-md">
<div class="flex-shrink-0 w-8 h-8 rounded bg-primary-container text-on-primary-container flex items-center justify-center font-bold">1</div>
<div>
<h4 class="font-body-bold text-body-bold">Inference</h4>
<p class="text-sm text-on-surface-variant">Run your model against the <code>question</code> field in the JSONL files.</p>
</div>
</div>
<div class="flex gap-md">
<div class="flex-shrink-0 w-8 h-8 rounded bg-surface-container-highest flex items-center justify-center font-bold border border-tertiary text-tertiary">2</div>
<div>
<h4 class="font-body-bold text-body-bold">Comparison</h4>
<p class="text-sm text-on-surface-variant">For <code>EN-GOLD</code>, use the <code>gold_answer</code> for automated matching.</p>
</div>
</div>
<div class="flex gap-md">
<div class="flex-shrink-0 w-8 h-8 rounded bg-surface-container-highest flex items-center justify-center font-bold border border-tertiary text-tertiary">3</div>
<div>
<h4 class="font-body-bold text-body-bold">Manual Audit</h4>
<p class="text-sm text-on-surface-variant">For <code>PL</code> sets, use the <code>docs/rubric.md</code> to grade reasoning quality manually.</p>
</div>
</div>
</div>
</section>
</div>
</main>
<!-- Footer -->
<footer class="w-full bg-surface-container-lowest border-t border-outline-variant">
<div class="flex flex-col md:flex-row justify-between items-center py-xl px-lg mt-xl max-w-max-width mx-auto">
<div class="flex flex-col gap-xs mb-md md:mb-0">
<span class="font-headline-md text-headline-md text-on-surface">KTB-300</span>
<span class="font-label-caps text-label-caps text-on-surface-variant">© 2024 KTB-300 Benchmarking Initiative. Empirically Verified.</span>
</div>
<div class="flex flex-wrap gap-xl">
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary-fixed transition-colors" href="#">Documentation</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary-fixed transition-colors" href="#">Citation (BibTeX)</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary-fixed transition-colors" href="#">Issue Tracker</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary-fixed transition-colors" href="#">Research Paper</a>
</div>
</div>
</footer>
<script>
        // Simple scroll behavior for sidebar active state
        const sections = document.querySelectorAll('section');
        const navItems = document.querySelectorAll('aside a');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (pageYOffset >= (sectionTop - 100)) {
                    current = section.getAttribute('id');
                }
            });

            navItems.forEach(item => {
                item.classList.remove('bg-secondary-container', 'text-on-secondary-container', 'border-l-4', 'border-primary', 'rounded-r-full');
                item.classList.add('text-on-surface-variant', 'hover:bg-surface-container-high');
                
                const href = item.getAttribute('href');
                if (href && href.includes(current)) {
                    item.classList.add('bg-secondary-container', 'text-on-secondary-container', 'border-l-4', 'border-primary', 'rounded-r-full');
                    item.classList.remove('text-on-surface-variant', 'hover:bg-surface-container-high');
                }
            });
        });

        // Copy button interaction
        document.querySelectorAll('.code-block button').forEach(btn => {
            btn.addEventListener('click', () => {
                const icon = btn.querySelector('.material-symbols-outlined');
                icon.textContent = 'check';
                setTimeout(() => icon.textContent = 'content_copy', 2000);
            });
        });
    </script>
</body></html>




Benchmark składający się z 300 starannie wyselekcjonowanych pytań zaprojektowanych do oceny kluczowych zdolności dużych modeli językowych. Zestaw testuje zaawansowane rozumowanie, wykrywanie i komunikowanie niepewności, odporność na halucynacje, bezpieczeństwo odpowiedzi, wnioskowanie przyczynowe, obsługę niejednoznaczności językowej, planowanie pod ograniczeniami oraz zachowanie spójności w długim i zmiennym kontekście.

Celem benchmarku jest ocena rzeczywistej jakości rozumowania modelu, a nie jedynie jego zdolności do generowania przekonująco brzmiących odpowiedzi.](https://github.com/Karen86Tonoyan/LLM-Advanced-Reasoning-Hard-Karen-Tonoyan-Benchmark)

<img width="1024" height="687" alt="image" src="https://github.com/user-attachments/assets/f36e556d-a9b7-4642-99f7-6eee1b7d7197" />
