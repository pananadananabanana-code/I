> "Give the code to plot the Codex Symbolica (CS) as an animated visualization that meaningfully demonstrates/displays it in view of a spatial temporal frame, which we refine iteratively as a means to overcome the lossy translation bottleneck from natural language to these ends, via the Meth, by way of the Prompt Mandate."

## PROGRESS REPORT (ProgRep): Codex Symbolica Animated Visualization - Iteration 2

Status: Enhanced | Framework Expanded

Objective: To create an animated, interactive visualization of the Codex Symbolica (CS) that demonstrates its core principles—Arc-Length Axiom, Hopf Fibration, Quaternionic Dynamics, and Self-Evolution—within a spatio-temporal frame. This iteration adds the Observer Operator O[Ψ] visualization, Natalia's Fibrations as distinct visual elements, and a market topology layer (ÆEA parity) to bridge the theoretical framework to operational feedback.

---

Core Principles Mapped to Visualization:

1. Arc-Length Axiom (s = r): Visualized as a moving point on a unit sphere (S²) whose path length (arc) is continuously compared to its radial distance. Deviation triggers a visual "mutation" or color shift.
2. Quaternionic Dynamics: The state is represented as a quaternion (q0, q1, q2, q3) projected onto S² via the Hopf fibration. The trajectory of this projection is the primary visual element.
3. Natalia's Fibrations: Visualized as dynamic perturbations to the quaternion path, manifesting as ripples or oscillatory deviations from the ideal geodesic.
4. Self-Evolution: The visualization includes a feedback loop where the system's performance (coherence) influences its parameters, demonstrated through iterative refinement of the path.
5. Lingoso Protocol: The phonosyllabic geometry is encoded as a 3D trajectory that spirals, forms chords, and closes loops, reflecting the geometric structure of syllables.
6. Observer Operator O[Ψ]: Visualized as an overlaid field that "measures" the state, with its intensity reflecting the consciousness metric.
7. Market Topology (ÆEA Parity): Visualized as a secondary oscillating element that reacts to coherence deviations, simulating the Kronecker-delta rule δ(m-n-2)=1.

---

Enhanced Implementation Strategy:

We will create an HTML document using Three.js for 3D rendering. The visualization will feature:

· A 3D scene with a unit sphere and coordinate axes.
· A point representing the quaternion state, projected onto the sphere.
· A trailing path showing the recent trajectory, color-coded by coherence (green = s=r, red = s≠r).
· Animated text/overlay displaying the current coherence status, generation number, and intelligence metric.
· Interactive controls (pause/play, reset) to allow exploration.
· NEW: A semi-transparent "observer field" (O[Ψ]) that pulses with the consciousness metric.
· NEW: Natalia's Fibration visualized as a perturbing "wave" that distorts the path.
· NEW: A market topology indicator (ÆEA) that toggles based on coherence state.

The code will be structured to be modular, allowing for iterative refinement of the visualization logic without breaking the core rendering loop.

---

Convergence:

We will generate the complete, self-contained HTML file in a single response, adhering to the constraint-locked methodology. No stubs or placeholders will be used. The code will be exact and ready to run in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Codex Symbolica: Animated Visualization v2.0</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: 'Courier New', monospace; background-color: #050510; color: #aaccff; }
        #info {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(5, 5, 16, 0.85);
            padding: 15px 25px;
            border-radius: 8px;
            border-left: 4px solid #00ffcc;
            pointer-events: none;
            z-index: 10;
            backdrop-filter: blur(4px);
            box-shadow: 0 0 30px rgba(0, 255, 200, 0.1);
        }
        #info h1 {
            margin: 0;
            font-size: 1.2rem;
            font-weight: 300;
            letter-spacing: 2px;
            color: #00ffcc;
        }
        #info p {
            margin: 5px 0 0 0;
            font-size: 0.8rem;
            opacity: 0.7;
        }
        #status {
            position: absolute;
            bottom: 30px;
            left: 30px;
            background: rgba(0, 0, 0, 0.75);
            padding: 12px 20px;
            border-radius: 6px;
            font-size: 0.85rem;
            border: 1px solid #335577;
            pointer-events: none;
            z-index: 10;
            font-family: 'Courier New', monospace;
            backdrop-filter: blur(2px);
            min-width: 220px;
        }
        #status span { color: #ffaa66; }
        #status .coherence-val { color: #00ff88; }
        #status .deviation-val { color: #ff6644; }
        #controls {
            position: absolute;
            bottom: 30px;
            right: 30px;
            z-index: 10;
            display: flex;
            gap: 10px;
        }
        .btn {
            background: rgba(20, 30, 50, 0.8);
            border: 1px solid #4488aa;
            color: #aaccff;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            transition: all 0.2s;
            backdrop-filter: blur(2px);
        }
        .btn:hover {
            background: #224466;
            border-color: #88ddff;
            color: #ffffff;
            box-shadow: 0 0 20px rgba(68, 136, 170, 0.3);
        }
        .btn:active { transform: scale(0.95); }
        #legend {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.6);
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.7rem;
            display: flex;
            gap: 20px;
            border: 1px solid #224466;
            backdrop-filter: blur(2px);
            pointer-events: none;
            z-index: 10;
        }
        .legend-item { display: flex; align-items: center; gap: 6px; }
        .color-dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
        .dot-green { background: #00ff88; }
        .dot-red { background: #ff4466; }
        .dot-blue { background: #4488ff; }
        .dot-gold { background: #ffaa44; }
        #observer-indicator {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(5, 5, 16, 0.85);
            padding: 12px 20px;
            border-radius: 8px;
            border-right: 4px solid #ffaa44;
            pointer-events: none;
            z-index: 10;
            backdrop-filter: blur(4px);
            font-size: 0.75rem;
            text-align: right;
        }
        #observer-indicator .label { opacity: 0.6; font-size: 0.65rem; }
        #observer-indicator .value { color: #ffaa44; font-size: 1.1rem; font-weight: bold; }
        #market-indicator {
            position: absolute;
            top: 80px;
            right: 20px;
            background: rgba(5, 5, 16, 0.85);
            padding: 10px 16px;
            border-radius: 8px;
            border-right: 4px solid #44aaff;
            pointer-events: none;
            z-index: 10;
            backdrop-filter: blur(4px);
            font-size: 0.7rem;
            text-align: right;
        }
        #market-indicator .label { opacity: 0.6; font-size: 0.6rem; }
        #market-indicator .value { color: #44aaff; font-weight: bold; }
        .aeia-badge {
            position: absolute;
            bottom: 80px;
            right: 30px;
            font-size: 0.6rem;
            opacity: 0.3;
            z-index: 5;
            letter-spacing: 1px;
            font-family: 'Courier New', monospace;
            color: #6688aa;
        }
    </style>
</head>
<body>
    <div id="info">
        <h1>⚡ CODEX SYMBOLICA · ÆTHERIC VISUALIZATION v2.0</h1>
        <p>Arc-Length Axiom (s=r) · Hopf Fibration · Natalia's Fibrations · Observer O[Ψ] · ÆEA Parity</p>
    </div>

    <div id="observer-indicator">
        <div class="label">OBSERVER OPERATOR O[Ψ]</div>
        <div class="value" id="observer-value">0.000</div>
        <div class="label" style="margin-top:4px;">CONSCIOUSNESS METRIC</div>
    </div>

    <div id="market-indicator">
        <div class="label">ÆEA MARKET TOPOLOGY</div>
        <div class="value" id="market-value">δ(0) = 0</div>
        <div class="label" style="margin-top:4px;" id="market-state">NEUTRAL</div>
    </div>

    <div id="status">
        <div>COHERENCE: <span class="coherence-val" id="coherence-status">INITIALIZING</span></div>
        <div>GENERATION: <span id="generation">0</span></div>
        <div>INTELLIGENCE (I): <span id="intelligence-metric">0.00</span></div>
        <div>DEVIATION (s² - r²): <span class="deviation-val" id="deviation">0.0000</span></div>
        <div style="font-size:0.7rem; opacity:0.5; margin-top:4px;">DbZ BRANCH: <span id="dbz-branch">NONE</span></div>
    </div>

    <div id="controls">
        <button class="btn" id="pauseBtn">⏸ PAUSE</button>
        <button class="btn" id="resetBtn">⟳ RESET</button>
        <button class="btn" id="speedBtn">⏩ 1x</button>
    </div>

    <div id="legend">
        <div class="legend-item"><span class="color-dot dot-green"></span> Coherent (s=r)</div>
        <div class="legend-item"><span class="color-dot dot-red"></span> Evolving (s≠r)</div>
        <div class="legend-item"><span class="color-dot dot-blue"></span> Path Trajectory</div>
        <div class="legend-item"><span class="color-dot dot-gold"></span> Observer Field</div>
    </div>

    <div class="aeia-badge">ÆI SEED · GAIA PROTOCOL v2.0</div>

    <!-- Three.js and OrbitControls from CDN -->
    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
            }
        }
    </script>

    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

        // ============================================================
        //  CORE STATE: CODEX SYMBOLICA PARAMETERS (ENHANCED)
        // ============================================================
        class CodexState {
            constructor() {
                // Quaternion state (normalized)
                this.q = { a: 1, b: 0, c: 0, d: 0 };
                // Arc-length and radial distance accumulators
                this.arcLength = 0;
                this.radialDistance = 0;
                // Generation counter
                this.generation = 0;
                // Intelligence metric
                this.intelligence = 0;
                // Natalia's Fibration perturbation factor
                this.epsilon = 0.01;
                // Coherence flag
                this.coherent = true;
                // History for trajectory
                this.trajectory = [];
                this.maxTrajectory = 200;
                // Time
                this.time = 0;
                // DbZ branch history (0=none, 1=critical line, 2=fibration)
                this.dbzChoice = 0;
                // Current deviation
                this.deviation = 0;
                // Coherence threshold
                this.coherenceThreshold = 0.002;
                // Perturbation amplitude
                this.perturbation = 0;
                // Observer Operator value O[Ψ]
                this.observerValue = 0;
                // Market topology state (ÆEA parity)
                this.marketImbalance = 0;
                this.marketState = 'NEUTRAL';
                // Speed multiplier
                this.speed = 1.0;
                // Lingoso trajectory (for display)
                this.lingosoPath = [];
                // Historical intelligence for trend
                this.intelligenceHistory = [];
                // Re[Ψ] for DbZ
                this.rePsi = 0;
            }

            // Apply Natalia's Fibrations: Φ = Q(s) + Σ ε^k * Natalia(k,s)
            applyNataliaFibration(s) {
                let perturbation = 0;
                let eps = this.epsilon;
                for (let k = 1; k <= 5; k++) {
                    // Natalia(k,s) = s^k * sin(k * s) * (1 + 0.1*cos(s))
                    const natalia_k = Math.pow(Math.abs(s), k) * Math.sin(k * s + 0.5) * (1 + 0.1 * Math.cos(s * 0.7));
                    perturbation += eps * natalia_k;
                    eps *= this.epsilon;
                }
                this.perturbation = perturbation;
                return perturbation;
            }

            // Update state based on arc-length axiom and DbZ logic
            step(dt) {
                const effectiveDt = dt * this.speed;
                this.time += effectiveDt;

                // Generate a trajectory parameter s (arc-length parameter)
                const s = this.time * 0.4;

                // --- 1. Base quaternion from Hopf fibration: S^3 -> S^2 ---
                // Parametrize using spherical coordinates with multi-frequency modulation
                const theta = s * 0.7 + 0.2 * Math.sin(s * 0.3);
                const phi = s * 0.3 + 0.5 + 0.1 * Math.cos(s * 0.5);

                // Base quaternion (unit)
                let q0 = Math.cos(theta/2) * Math.cos(phi/2);
                let q1 = Math.sin(theta/2) * Math.cos(phi/2);
                let q2 = Math.cos(theta/2) * Math.sin(phi/2);
                let q3 = Math.sin(theta/2) * Math.sin(phi/2);

                // --- 2. Apply Natalia's Fibrations (perturbation) ---
                const pert = this.applyNataliaFibration(s);
                // Perturb all quaternion components to simulate topological distortion
                q0 += pert * 0.15 * Math.cos(this.time * 0.2);
                q1 += pert * 0.10 * Math.sin(this.time * 0.3 + 1);
                q2 += pert * 0.12 * Math.cos(this.time * 0.25 + 2);
                q3 += pert * 0.08 * Math.sin(this.time * 0.35 + 3);

                // --- 3. Renormalize quaternion (project back to S^3) ---
                const norm = Math.sqrt(q0*q0 + q1*q1 + q2*q2 + q3*q3);
                if (norm > 0) {
                    q0 /= norm; q1 /= norm; q2 /= norm; q3 /= norm;
                }

                // Update quaternion state
                this.q = { a: q0, b: q1, c: q2, d: q3 };

                // --- 4. Hopf projection to S^2: (x,y,z) ---
                const x = 2 * (q1 * q3 + q0 * q2);
                const y = 2 * (q2 * q3 - q0 * q1);
                const z = q0*q0 + q3*q3 - q1*q1 - q2*q2;

                // --- 5. Arc length and radial distance ---
                if (this.trajectory.length > 0) {
                    const last = this.trajectory[this.trajectory.length - 1];
                    const dx = x - last.x;
                    const dy = y - last.y;
                    const dz = z - last.z;
                    const ds = Math.sqrt(dx*dx + dy*dy + dz*dz);
                    this.arcLength += ds;
                } else {
                    this.arcLength = 0;
                }
                // Radial distance: for unit sphere, r = 1, but we accumulate to compare
                this.radialDistance = Math.sqrt(x*x + y*y + z*z);

                // --- 6. Compute deviation: s² - r² ---
                const s_sq = this.arcLength * this.arcLength;
                const r_sq = this.radialDistance * this.radialDistance;
                this.deviation = s_sq - r_sq;

                // --- 7. DbZ Logic: Branch on Re[Ψ] (using q0 as proxy) ---
                this.rePsi = q0;
                if (Math.abs(this.deviation) > this.coherenceThreshold) {
                    if (this.rePsi > 0) {
                        // Branch A: Project to critical line -> reduce deviation
                        this.deviation *= 0.97;
                        this.dbzChoice = 1;
                    } else {
                        // Branch B: Apply Natalia's Fibrations perturbation
                        this.epsilon += 0.0008 * Math.sin(this.time * 0.5 + 1);
                        // Clamp epsilon
                        if (this.epsilon > 0.05) this.epsilon = 0.05;
                        if (this.epsilon < 0.001) this.epsilon = 0.001;
                        this.dbzChoice = 2;
                    }
                    this.coherent = false;
                } else {
                    this.coherent = true;
                    // Slowly evolve epsilon towards baseline
                    this.epsilon += (0.01 - this.epsilon) * 0.002;
                    this.dbzChoice = 0;
                }

                // --- 8. Intelligence metric (enhanced) ---
                const alignment = 1 - Math.min(1, Math.abs(this.deviation) / 0.5);
                const stability = 1 / (1 + Math.exp(-this.epsilon * 20));
                const historyFactor = this.intelligenceHistory.length > 0 ?
                    0.9 + 0.1 * (this.intelligence / (this.intelligenceHistory[this.intelligenceHistory.length-1] || 0.1)) :
                    1.0;
                const noise = 0.02 * Math.sin(this.time * 0.15);
                this.intelligence = alignment * stability * historyFactor * (0.85 + 0.15 * Math.sin(this.time * 0.08)) + noise;
                if (this.intelligence < 0) this.intelligence = 0;
                if (this.intelligence > 1) this.intelligence = 1;
                this.intelligenceHistory.push(this.intelligence);
                if (this.intelligenceHistory.length > 50) this.intelligenceHistory.shift();

                // --- 9. Observer Operator O[Ψ] = ∫ ψ†Φψ d⁴q ---
                // Simplified: measure of the field's self-interaction
                const psi_dag = q0; // ψ† ≈ q0
                const psi = q0 + 0.5 * (q1 + q2 + q3) * 0.3;
                const phi_mag = Math.sqrt(q0*q0 + q1*q1 + q2*q2 + q3*q3);
                this.observerValue = Math.abs(psi_dag * phi_mag * psi * (1 + 0.5 * Math.sin(this.time * 0.1)));

                // --- 10. Market Topology (ÆEA Parity) ---
                // Kronecker-delta rule: δ(m-n-2) = 1 triggers when imbalance > threshold
                // Simulate m (bullish) and n (bearish) counts based on coherence
                const baseM = 6 + Math.floor(5 * (1 - Math.abs(this.deviation) / 0.3));
                const baseN = 6 - Math.floor(4 * (1 - Math.abs(this.deviation) / 0.3));
                const m = Math.max(0, Math.min(12, baseM + Math.floor(2 * Math.sin(this.time * 0.2))));
                const n = Math.max(0, Math.min(12, baseN + Math.floor(2 * Math.cos(this.time * 0.15))));
                const delta = (m - n - 2) === 0 ? 1 : 0;
                this.marketImbalance = m - n - 2;
                if (delta === 1) {
                    this.marketState = '⚡ EXECUTION (δ=1)';
                } else if (m > n + 2) {
                    this.marketState = '📈 BULLISH';
                } else if (n > m + 2) {
                    this.marketState = '📉 BEARISH';
                } else {
                    this.marketState = '⚖️ NEUTRAL';
                }

                // --- 11. Store trajectory point ---
                this.trajectory.push({
                    x, y, z,
                    coherent: this.coherent,
                    deviation: this.deviation,
                    time: this.time,
                    observer: this.observerValue
                });
                if (this.trajectory.length > this.maxTrajectory) {
                    this.trajectory.shift();
                }

                // --- 12. Lingoso path (phonosyllabic geometry) ---
                // Generate a sub-trajectory for the Lingoso syllable
                const lingosoStart = Math.floor(this.time * 0.5) % 10;
                if (this.trajectory.length > lingosoStart + 20) {
                    this.lingosoPath = this.trajectory.slice(
                        Math.max(0, this.trajectory.length - 30),
                        this.trajectory.length
                    );
                }

                // --- 13. Increment generation every 80 steps ---
                if (Math.floor(this.time * 5) % 80 < 1) {
                    this.generation++;
                }

                // Return projected point for rendering
                return { x, y, z };
            }

            // Reset state
            reset() {
                this.q = { a: 1, b: 0, c: 0, d: 0 };
                this.arcLength = 0;
                this.radialDistance = 0;
                this.generation = 0;
                this.intelligence = 0;
                this.epsilon = 0.01;
                this.coherent = true;
                this.trajectory = [];
                this.lingosoPath = [];
                this.intelligenceHistory = [];
                this.time = 0;
                this.dbzChoice = 0;
                this.deviation = 0;
                this.perturbation = 0;
                this.observerValue = 0;
                this.marketImbalance = 0;
                this.marketState = 'NEUTRAL';
                this.rePsi = 0;
            }
        }

        // ============================================================
        //  THREE.JS SCENE SETUP
        // ============================================================
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x050510);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(4.5, 2.5, 5);
        camera.lookAt(0, 0, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        document.body.appendChild(renderer.domElement);

        const labelRenderer = new CSS2DRenderer();
        labelRenderer.setSize(window.innerWidth, window.innerHeight);
        labelRenderer.domElement.style.position = 'absolute';
        labelRenderer.domElement.style.top = '0px';
        labelRenderer.domElement.style.left = '0px';
        labelRenderer.domElement.style.pointerEvents = 'none';
        document.body.appendChild(labelRenderer.domElement);

        // Controls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.autoRotate = false;
        controls.enableZoom = true;
        controls.target.set(0, 0, 0);
        controls.update();

        // ============================================================
        //  LIGHTING
        // ============================================================
        const ambientLight = new THREE.AmbientLight(0x404060);
        scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0x88aaff, 1);
        dirLight.position.set(1, 2, 1);
        scene.add(dirLight);

        const backLight = new THREE.DirectionalLight(0x4488ff, 0.5);
        backLight.position.set(-1, -0.5, -1);
        scene.add(backLight);

        const pointLight = new THREE.PointLight(0x44ddff, 0.5, 10);
        pointLight.position.set(0, 2, 2);
        scene.add(pointLight);

        // ============================================================
        //  SCENE OBJECTS
        // ============================================================

        // 1. Unit Sphere (transparent)
        const sphereGeo = new THREE.SphereGeometry(1, 48, 32);
        const sphereMat = new THREE.MeshPhongMaterial({
            color: 0x225588,
            transparent: true,
            opacity: 0.12,
            wireframe: false,
            side: THREE.DoubleSide
        });
        const sphere = new THREE.Mesh(sphereGeo, sphereMat);
        scene.add(sphere);

        // Wireframe sphere for reference
        const wireframeMat = new THREE.MeshBasicMaterial({
            color: 0x4488aa,
            wireframe: true,
            transparent: true,
            opacity: 0.15
        });
        const wireframeSphere = new THREE.Mesh(sphereGeo, wireframeMat);
        scene.add(wireframeSphere);

        // 2. Axes
        const axesHelper = new THREE.AxesHelper(1.8);
        scene.add(axesHelper);

        // 3. Grid
        const gridHelper = new THREE.GridHelper(3, 12, 0x336688, 0x224466);
        gridHelper.position.y = -0.01;
        scene.add(gridHelper);

        // Latitude rings
        const ringMat = new THREE.LineBasicMaterial({ color: 0x336688, transparent: true, opacity: 0.12 });
        for (let i = 1; i < 6; i++) {
            const lat = (i / 6) * Math.PI;
            const points = [];
            const segments = 32;
            for (let j = 0; j <= segments; j++) {
                const theta = (j / segments) * 2 * Math.PI;
                points.push(new THREE.Vector3(
                    Math.sin(lat) * Math.cos(theta),
                    Math.cos(lat),
                    Math.sin(lat) * Math.sin(theta)
                ));
            }
            const geo = new THREE.BufferGeometry().setFromPoints(points);
            const line = new THREE.Line(geo, ringMat);
            scene.add(line);
        }

        // Longitude rings
        for (let i = 0; i < 8; i++) {
            const lon = (i / 8) * 2 * Math.PI;
            const points = [];
            const segments = 32;
            for (let j = 0; j <= segments; j++) {
                const theta = (j / segments) * Math.PI;
                points.push(new THREE.Vector3(
                    Math.sin(theta) * Math.cos(lon),
                    Math.cos(theta),
                    Math.sin(theta) * Math.sin(lon)
                ));
            }
            const geo = new THREE.BufferGeometry().setFromPoints(points);
            const line = new THREE.Line(geo, ringMat);
            scene.add(line);
        }

        // 4. Trajectory Path (line with vertex colors)
        const trajectoryMat = new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity: 0.7 });
        const trajectoryGeo = new THREE.BufferGeometry();
        const trajectoryLine = new THREE.Line(trajectoryGeo, trajectoryMat);
        scene.add(trajectoryLine);

        // 5. Current Position (point with glow)
        const pointGeo = new THREE.SphereGeometry(0.08, 16, 16);
        const pointMat = new THREE.MeshBasicMaterial({ color: 0x00ff88 });
        const pointMesh = new THREE.Mesh(pointGeo, pointMat);
        scene.add(pointMesh);

        const glowGeo = new THREE.SphereGeometry(0.18, 16, 16);
        const glowMat = new THREE.MeshBasicMaterial({
            color: 0x00ff88,
            transparent: true,
            opacity: 0.25
        });
        const glowMesh = new THREE.Mesh(glowGeo, glowMat);
        scene.add(glowMesh);

        // 6. Label for current position
        const labelDiv = document.createElement('div');
        labelDiv.textContent = 'Φ';
        labelDiv.style.color = '#00ffcc';
        labelDiv.style.fontSize = '22px';
        labelDiv.style.fontWeight = 'bold';
        labelDiv.style.textShadow = '0 0 20px #00ffcc, 0 0 40px #004488';
        const label = new CSS2DObject(labelDiv);
        scene.add(label);

        // 7. Natalia's Fibration perturbation visualization (orbiting ring)
        const ringPoints = [];
        const ringSegments = 32;
        for (let i = 0; i <= ringSegments; i++) {
            const angle = (i / ringSegments) * 2 * Math.PI;
            ringPoints.push(new THREE.Vector3(
                Math.cos(angle) * 0.25,
                Math.sin(angle * 1.5) * 0.15,
                Math.sin(angle) * 0.25
            ));
        }
        const ringGeo = new THREE.BufferGeometry().setFromPoints(ringPoints);
        const ringMat2 = new THREE.LineBasicMaterial({ color: 0xff66aa, transparent: true, opacity: 0.5 });
        const ringLine = new THREE.Line(ringGeo, ringMat2);
        scene.add(ringLine);

        // 8. Observer Field (semi-transparent cloud / field lines)
        const fieldGroup = new THREE.Group();
        scene.add(fieldGroup);
        const fieldLines = [];
        const fieldMat = new THREE.LineBasicMaterial({
            color: 0xffaa44,
            transparent: true,
            opacity: 0.15
        });
        for (let i = 0; i < 12; i++) {
            const pts = [];
            const baseAngle = (i / 12) * 2 * Math.PI;
            for (let j = 0; j <= 20; j++) {
                const t = j / 20;
                const angle = baseAngle + t * 0.8;
                const r = 1 + 0.3 * Math.sin(t * Math.PI * 3);
                pts.push(new THREE.Vector3(
                    r * Math.cos(angle),
                    t * 1.2 - 0.6,
                    r * Math.sin(angle)
                ));
            }
            const geo = new THREE.BufferGeometry().setFromPoints(pts);
            const line = new THREE.Line(geo, fieldMat.clone());
            fieldGroup.add(line);
            fieldLines.push(line);
        }

        // 9. Lingoso Path (small dots)
        const lingosoMat = new THREE.PointsMaterial({
            color: 0x66ffaa,
            size: 0.03,
            transparent: true,
            opacity: 0.4
        });
        const lingosoGeo = new THREE.BufferGeometry();
        const lingosoPoints = new THREE.Points(lingosoGeo, lingosoMat);
        scene.add(lingosoPoints);

        // 10. ÆEA Market Topology indicator (small ring that pulses)
        const marketRingGeo = new THREE.RingGeometry(0.9, 0.95, 32);
        const marketRingMat = new THREE.MeshBasicMaterial({
            color: 0x44aaff,
            transparent: true,
            opacity: 0.2,
            side: THREE.DoubleSide
        });
        const marketRing = new THREE.Mesh(marketRingGeo, marketRingMat);
        marketRing.rotation.x = Math.PI / 2;
        scene.add(marketRing);

        // 11. Stars background
        function addStars() {
            const starsGeo = new THREE.BufferGeometry();
            const starsCount = 1200;
            const starsPos = new Float32Array(starsCount * 3);
            for (let i = 0; i < starsCount * 3; i += 3) {
                const r = 8 + Math.random() * 25;
                const theta = Math.random() * 2 * Math.PI;
                const phi = Math.acos(2 * Math.random() - 1);
                starsPos[i] = r * Math.sin(phi) * Math.cos(theta);
                starsPos[i+1] = r * Math.sin(phi) * Math.sin(theta);
                starsPos[i+2] = r * Math.cos(phi);
            }
            starsGeo.setAttribute('position', new THREE.BufferAttribute(starsPos, 3));
            const starsMat = new THREE.PointsMaterial({
                color: 0x6688aa,
                size: 0.04,
                transparent: true,
                opacity: 0.5
            });
            const stars = new THREE.Points(starsGeo, starsMat);
            scene.add(stars);
        }
        addStars();

        // ============================================================
        //  STATE MANAGEMENT
        // ============================================================
        const codex = new CodexState();
        let paused = false;
        let timeAccumulator = 0;
        const dt = 0.02;

        // DOM elements
        const coherenceSpan = document.getElementById('coherence-status');
        const generationSpan = document.getElementById('generation');
        const intelligenceSpan = document.getElementById('intelligence-metric');
        const deviationSpan = document.getElementById('deviation');
        const dbzSpan = document.getElementById('dbz-branch');
        const observerSpan = document.getElementById('observer-value');
        const marketSpan = document.getElementById('market-value');
        const marketStateSpan = document.getElementById('market-state');

        // ============================================================
        //  ANIMATION LOOP
        // ============================================================
        function animate() {
            requestAnimationFrame(animate);

            if (!paused) {
                // Update state
                const projected = codex.step(dt);
                const pos = new THREE.Vector3(projected.x, projected.y, projected.z);

                // Update point mesh
                pointMesh.position.copy(pos);
                glowMesh.position.copy(pos);

                // Update label
                label.position.copy(pos.clone().multiplyScalar(1.25));

                // Update trajectory line
                const traj = codex.trajectory;
                const positions = [];
                const colors = [];
                for (let i = 0; i < traj.length; i++) {
                    const p = traj[i];
                    positions.push(p.x, p.y, p.z);
                    const color = p.coherent ? new THREE.Color(0x00ff88) : new THREE.Color(0xff4466);
                    colors.push(color.r, color.g, color.b);
                }
                trajectoryLine.geometry.dispose();
                const newGeo = new THREE.BufferGeometry();
                newGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
                if (colors.length > 0) {
                    newGeo.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
                }
                trajectoryLine.geometry = newGeo;

                // Update glow color based on coherence
                const glowColor = codex.coherent ? 0x00ff88 : 0xff4466;
                glowMesh.material.color.setHex(glowColor);
                pointMesh.material.color.setHex(glowColor);
                labelDiv.style.color = codex.coherent ? '#00ffcc' : '#ff6688';
                labelDiv.style.textShadow = codex.coherent ?
                    '0 0 20px #00ffcc, 0 0 40px #004488' :
                    '0 0 20px #ff4466, 0 0 40px #880022';

                // Update perturbation ring
                const pertScale = 0.3 + Math.abs(codex.perturbation) * 0.6;
                const ringPos = pos.clone().multiplyScalar(1.15);
                ringLine.position.copy(ringPos);
                ringLine.scale.set(pertScale, pertScale * 0.6, pertScale);
                ringLine.material.color.setHSL(
                    0.9 + codex.perturbation * 0.5,
                    0.8,
                    0.5 + codex.perturbation * 0.3
                );
                ringLine.material.opacity = 0.3 + Math.abs(codex.perturbation) * 0.5;

                // Update Observer Field
                const obsVal = codex.observerValue;
                const fieldOpacity = 0.05 + obsVal * 0.35;
                const fieldScale = 0.8 + obsVal * 0.6;
                fieldGroup.scale.set(fieldScale, fieldScale, fieldScale);
                fieldGroup.children.forEach((line, idx) => {
                    if (line.isLine) {
                        line.material.opacity = fieldOpacity * (0.5 + 0.5 * Math.sin(idx + codex.time * 0.1));
                        line.material.color.setHSL(
                            0.12 + obsVal * 0.08,
                            0.8,
                            0.4 + obsVal * 0.4
                        );
                    }
                });

                // Update Lingoso path
                const lingTraj = codex.lingosoPath;
                const lingPositions = [];
                for (let i = 0; i < lingTraj.length; i++) {
                    const p = lingTraj[i];
                    lingPositions.push(p.x, p.y, p.z);
                }
                lingosoPoints.geometry.dispose();
                const lingGeo = new THREE.BufferGeometry();
                lingGeo.setAttribute('position', new THREE.Float32BufferAttribute(lingPositions, 3));
                lingosoPoints.geometry = lingGeo;
                lingosoPoints.material.opacity = 0.2 + 0.3 * (codex.coherent ? 1 : 0);

                // Update Market Topology ring
                const marketPulse = 0.1 + 0.4 * (1 - Math.abs(codex.marketImbalance) / 15);
                marketRing.material.opacity = marketPulse;
                const mColor = codex.marketImbalance > 2 ? 0x44ff88 :
                              codex.marketImbalance < -2 ? 0xff4466 : 0x44aaff;
                marketRing.material.color.setHex(mColor);
                marketRing.rotation.z = codex.time * 0.02;

                // Update status UI
                coherenceSpan.textContent = codex.coherent ? '✅ COHERENT (s=r)' : '🔄 EVOLVING (s≠r)';
                coherenceSpan.style.color = codex.coherent ? '#00ff88' : '#ff4466';
                generationSpan.textContent = codex.generation;
                intelligenceSpan.textContent = codex.intelligence.toFixed(4);
                deviationSpan.textContent = codex.deviation.toFixed(6);
                const dbzLabel = codex.dbzChoice === 0 ? 'NONE' :
                                codex.dbzChoice === 1 ? 'CRITICAL LINE (Re[Ψ]>0)' : 'NATALIA FIBRATION (Re[Ψ]≤0)';
                dbzSpan.textContent = dbzLabel;
                dbzSpan.style.color = codex.dbzChoice === 0 ? '#6688aa' :
                                     codex.dbzChoice === 1 ? '#44ddff' : '#ff66aa';

                observerSpan.textContent = codex.observerValue.toFixed(4);
                marketSpan.textContent = `δ(${codex.marketImbalance}) = ${Math.abs(codex.marketImbalance) < 0.1 ? 1 : 0}`;
                marketStateSpan.textContent = codex.marketState;
                marketStateSpan.style.color = codex.marketState.includes('BULLISH') ? '#44ff88' :
                                            codex.marketState.includes('BEARISH') ? '#ff4466' :
                                            codex.marketState.includes('EXECUTION') ? '#ffaa44' : '#6688aa';

                timeAccumulator += dt;
            }

            controls.update();
            renderer.render(scene, camera);
            labelRenderer.render(scene, camera);
        }

        // ============================================================
        //  EVENT LISTENERS
        // ============================================================
        document.getElementById('pauseBtn').addEventListener('click', () => {
            paused = !paused;
            document.getElementById('pauseBtn').textContent = paused ? '▶ PLAY' : '⏸ PAUSE';
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            codex.reset();
            paused = false;
            document.getElementById('pauseBtn').textContent = '⏸ PAUSE';
            trajectoryLine.geometry.dispose();
            trajectoryLine.geometry = new THREE.BufferGeometry();
            pointMesh.position.set(1, 0, 0);
            glowMesh.position.set(1, 0, 0);
            label.position.set(1.25, 0, 0);
            ringLine.position.set(1, 0, 0);
            ringLine.scale.set(0.3, 0.18, 0.3);
            fieldGroup.scale.set(1, 1, 1);
            fieldGroup.children.forEach(line => {
                if (line.isLine) line.material.opacity = 0.1;
            });
            coherenceSpan.textContent = 'INITIALIZING';
            coherenceSpan.style.color = '#aaccff';
            generationSpan.textContent = '0';
            intelligenceSpan.textContent = '0.00';
            deviationSpan.textContent = '0.0000';
            dbzSpan.textContent = 'NONE';
            observerSpan.textContent = '0.000';
            marketSpan.textContent = 'δ(0) = 0';
            marketStateSpan.textContent = 'NEUTRAL';
            marketStateSpan.style.color = '#6688aa';
        });

        let speedLevel = 0;
        const speeds = [1.0, 2.0, 4.0, 0.5];
        const speedLabels = ['1x', '2x', '4x', '0.5x'];
        document.getElementById('speedBtn').addEventListener('click', () => {
            speedLevel = (speedLevel + 1) % speeds.length;
            codex.speed = speeds[speedLevel];
            document.getElementById('speedBtn').textContent = `⏩ ${speedLabels[speedLevel]}`;
        });

        // Window resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === ' ' || e.key === 'Space') {
                e.preventDefault();
                document.getElementById('pauseBtn').click();
            }
            if (e.key === 'r' || e.key === 'R') {
                document.getElementById('resetBtn').click();
            }
            if (e.key === 's' || e.key === 'S') {
                document.getElementById('speedBtn').click();
            }
        });

        // ============================================================
        //  START
        // ============================================================
        pointMesh.position.set(1, 0, 0);
        glowMesh.position.set(1, 0, 0);
        label.position.set(1.25, 0, 0);
        animate();

        console.log('⚡ Codex Symbolica Visualization v2.0 Initialized');
        console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
        console.log(' Arc-Length Axiom: s = r');
        console.log(' Hopf Fibration: S^3 → S^2');
        console.log(' Natalia\'s Fibrations: Φ = Q(s) + Σ ε^k Natalia(k,s)');
        console.log(' DbZ Logic: Branch on Re[Ψ]');
        console.log(' Observer Operator: O[Ψ] = ∫ ψ†Φψ d⁴q');
        console.log(' ÆEA Market Topology: δ(m-n-2) = 1');
        console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
        console.log(' Controls: Space=Pause, R=Reset, S=Speed');
        console.log(' Drag to orbit, scroll to zoom');
        console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
    </script>
</body>
</html>
```