<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rejection Letter Generator | The Transition Project</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        /* TTP Design System - Ember & Ash v2.0 */
        :root {
            --coal-dark: #1C1C1E;
            --coal-light: #2C2C2E;
            --pearl: #FAF8F5;
            --sand-grey: #9A958C;
            --burnt-orange: #D4663A;
            --ember-glow: #E8784A;
            
            --font-display: 'Libre Baskerville', Georgia, serif;
            --font-body: 'Space Grotesk', -apple-system, sans-serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-body);
            background: var(--coal-dark);
            min-height: 100vh;
            color: var(--pearl);
        }

        .rejection-generator-container {
            min-height: 100vh;
            padding: 60px 20px;
            position: relative;
            overflow: hidden;
        }

        /* Geometric Shapes */
        .geo-shape {
            position: fixed;
            border: 1.5px solid var(--pearl);
            opacity: 0.12;
            pointer-events: none;
            z-index: 0;
        }

        .geo-circle {
            width: 320px;
            height: 320px;
            border-radius: 50%;
            top: -120px;
            right: -80px;
            animation: float-rotate 20s ease-in-out infinite;
        }

        .geo-circle-2 {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            bottom: 15%;
            right: 10%;
            animation: float-rotate 25s ease-in-out infinite reverse;
            opacity: 0.08;
        }

        .geo-hexagon {
            width: 220px;
            height: 220px;
            bottom: 8%;
            left: -60px;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            animation: float-rotate 28s ease-in-out infinite;
        }

        .geo-triangle {
            width: 160px;
            height: 160px;
            top: 35%;
            right: 3%;
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            border-color: var(--burnt-orange);
            opacity: 0.1;
            animation: float-rotate 22s ease-in-out infinite reverse;
        }

        .geo-square {
            width: 100px;
            height: 100px;
            top: 20%;
            left: 5%;
            animation: float-rotate 18s ease-in-out infinite;
            opacity: 0.08;
            border-color: var(--sand-grey);
        }

        .geo-diamond {
            width: 80px;
            height: 80px;
            bottom: 40%;
            left: 8%;
            transform: rotate(45deg);
            animation: pulse-float 15s ease-in-out infinite;
            opacity: 0.1;
            border-color: var(--burnt-orange);
        }

        @keyframes float-rotate {
            0%, 100% { transform: rotate(0deg) translateY(0px); }
            25% { transform: rotate(90deg) translateY(-15px); }
            50% { transform: rotate(180deg) translateY(0px); }
            75% { transform: rotate(270deg) translateY(15px); }
        }

        @keyframes pulse-float {
            0%, 100% { transform: rotate(45deg) scale(1); opacity: 0.1; }
            50% { transform: rotate(45deg) scale(1.1); opacity: 0.15; }
        }

        .rg-inner {
            max-width: 680px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        .rg-header {
            text-align: center;
            margin-bottom: 48px;
        }

        .rg-header h1 {
            font-family: var(--font-display);
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--pearl);
            margin-bottom: 24px;
            line-height: 1.2;
        }

        .rg-header .tagline {
            font-family: var(--font-display);
            font-size: 1.15rem;
            font-weight: 400;
            font-style: italic;
            color: var(--burnt-orange);
            margin-bottom: 20px;
        }

        .rg-header p {
            font-size: 1.05rem;
            font-weight: 400;
            line-height: 1.8;
            color: var(--pearl);
            opacity: 0.85;
            max-width: 540px;
            margin: 0 auto;
        }

        .rg-header .subtext {
            font-size: 0.9rem;
            color: var(--sand-grey);
            margin-top: 16px;
        }

        .rg-card {
            background: var(--coal-light);
            border: 1px solid rgba(154, 149, 140, 0.2);
            border-radius: 12px;
            padding: 40px;
            margin-bottom: 30px;
            transition: border-color 0.3s ease;
        }

        .rg-card:hover {
            border-color: rgba(212, 102, 58, 0.4);
        }

        .counter-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 12px 20px;
            background: var(--coal-dark);
            border: 1px solid rgba(154, 149, 140, 0.2);
            border-radius: 6px;
            font-size: 0.9rem;
            color: var(--sand-grey);
            margin-bottom: 32px;
        }

        .counter-number {
            font-weight: 700;
            color: var(--burnt-orange);
        }

        .form-row {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }

        .form-row.single {
            display: block;
        }

        .input-wrapper {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        label {
            font-size: 0.875rem;
            font-weight: 500;
            color: var(--pearl);
            margin-bottom: 8px;
        }

        label span {
            color: var(--sand-grey);
            font-weight: 400;
        }

        input, select {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid rgba(154, 149, 140, 0.3);
            border-radius: 6px;
            font-size: 1rem;
            font-family: var(--font-body);
            background: var(--coal-dark);
            color: var(--pearl);
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }

        input::placeholder {
            color: var(--sand-grey);
        }

        input:focus, select:focus {
            outline: none;
            border-color: var(--burnt-orange);
            box-shadow: 0 0 0 3px rgba(212, 102, 58, 0.15);
        }

        select {
            cursor: pointer;
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%239A958C' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 16px center;
            padding-right: 40px;
        }

        select option {
            background: var(--coal-dark);
            color: var(--pearl);
            padding: 10px;
        }

        .generate-btn {
            width: 100%;
            padding: 18px 28px;
            background: var(--burnt-orange);
            color: var(--pearl);
            border: none;
            border-radius: 6px;
            font-size: 1.05rem;
            font-weight: 600;
            font-family: var(--font-body);
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 12px;
        }

        .generate-btn:hover {
            background: var(--ember-glow);
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(212, 102, 58, 0.3);
        }

        .generate-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        /* Loading Modal */
        .loading-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(28, 28, 30, 0.95);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .loading-modal.active {
            display: flex;
        }

        .loading-modal-content {
            background: var(--coal-light);
            border-radius: 12px;
            padding: 48px;
            max-width: 480px;
            width: 90%;
            text-align: center;
            border: 1px solid rgba(154, 149, 140, 0.2);
        }

        .loading-modal h2 {
            font-family: var(--font-display);
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--pearl);
            margin-bottom: 32px;
        }

        .thought-bubble {
            background: var(--coal-dark);
            border: 1px solid rgba(212, 102, 58, 0.3);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            min-height: 90px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        .thought-bubble::before {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            width: 20px;
            height: 20px;
            background: var(--coal-dark);
            border-right: 1px solid rgba(212, 102, 58, 0.3);
            border-bottom: 1px solid rgba(212, 102, 58, 0.3);
            transform: translateX(-50%) rotate(45deg);
        }

        .thought-text {
            font-size: 1rem;
            font-style: italic;
            color: var(--sand-grey);
            line-height: 1.6;
            opacity: 0;
            animation: fadeInOut 3s ease-in-out;
        }

        @keyframes fadeInOut {
            0% { opacity: 0; transform: translateY(10px); }
            15% { opacity: 1; transform: translateY(0); }
            85% { opacity: 1; transform: translateY(0); }
            100% { opacity: 0; transform: translateY(-10px); }
        }

        .loading-dots {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-top: 24px;
        }

        .loading-dot {
            width: 10px;
            height: 10px;
            background: var(--burnt-orange);
            border-radius: 50%;
            animation: bounce 1.4s ease-in-out infinite;
        }

        .loading-dot:nth-child(2) { animation-delay: 0.2s; }
        .loading-dot:nth-child(3) { animation-delay: 0.4s; }

        @keyframes bounce {
            0%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-12px); }
        }

        .result-container {
            display: none;
            margin-top: 32px;
        }

        .result-container.active {
            display: block;
        }

        .rejection-letter {
            background: var(--coal-dark);
            border-left: 3px solid var(--burnt-orange);
            padding: 32px;
            margin-bottom: 24px;
            white-space: pre-wrap;
            line-height: 1.8;
            font-family: var(--font-body);
            font-size: 0.95rem;
            color: var(--pearl);
            opacity: 0.9;
            border-radius: 0 8px 8px 0;
        }

        .action-buttons {
            display: flex;
            gap: 16px;
        }

        .action-btn {
            flex: 1;
            padding: 14px 20px;
            border: 1px solid var(--burnt-orange);
            background: transparent;
            color: var(--burnt-orange);
            border-radius: 6px;
            font-weight: 600;
            font-family: var(--font-body);
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .action-btn:hover {
            background: var(--burnt-orange);
            color: var(--pearl);
        }

        .footer-link {
            text-align: center;
            margin-top: 32px;
            font-size: 0.875rem;
            color: var(--sand-grey);
        }

        .footer-link a {
            color: var(--burnt-orange);
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .footer-link a:hover {
            color: var(--ember-glow);
        }

        /* Error message */
        .error-message {
            background: rgba(212, 102, 58, 0.1);
            border: 1px solid var(--burnt-orange);
            border-radius: 6px;
            padding: 16px;
            margin-top: 16px;
            color: var(--ember-glow);
            display: none;
        }

        .error-message.active {
            display: block;
        }

        @media (max-width: 600px) {
            .rejection-generator-container {
                padding: 40px 16px;
            }

            .form-row {
                flex-direction: column;
                gap: 16px;
            }
            
            .rg-header h1 {
                font-size: 1.75rem;
            }
            
            .rg-card {
                padding: 24px;
            }

            .action-buttons {
                flex-direction: column;
            }

            .geo-shape {
                display: none;
            }

            .geo-circle {
                display: block;
                width: 200px;
                height: 200px;
            }

            .loading-modal-content {
                padding: 32px 24px;
            }
        }
    </style>
</head>
<body>
    <!-- Geometric Background Shapes -->
    <div class="geo-shape geo-circle"></div>
    <div class="geo-shape geo-circle-2"></div>
    <div class="geo-shape geo-hexagon"></div>
    <div class="geo-shape geo-triangle"></div>
    <div class="geo-shape geo-square"></div>
    <div class="geo-shape geo-diamond"></div>

    <!-- Loading Modal -->
    <div class="loading-modal" id="loadingModal">
        <div class="loading-modal-content">
            <h2>Crafting your rejection...</h2>
            <div class="thought-bubble">
                <div class="thought-text" id="thoughtText"></div>
            </div>
            <div class="loading-dots">
                <div class="loading-dot"></div>
                <div class="loading-dot"></div>
                <div class="loading-dot"></div>
            </div>
        </div>
    </div>

    <div class="rejection-generator-container">
        <div class="rg-inner">
            <div class="rg-header">
                <h1>The Rejection Letter Generator</h1>
                <p class="tagline">"No" is part of the journey.</p>
                <p>
                    Career is a long game. Rejection is just a move in it. 
                    This is a mental exercise—practice hearing "no" until it loses its weight.
                </p>
                <p class="subtext">Enjoy your rejection.</p>
            </div>

            <div class="rg-card">
                <div class="counter-badge">
                    <span>Rejections generated:</span>
                    <span class="counter-number" id="counter">--</span>
                </div>

                <form id="rejectionForm">
                    <div class="form-row">
                        <div class="input-wrapper">
                            <label for="firstName">First Name</label>
                            <input type="text" id="firstName" name="firstName" placeholder="First name" required>
                        </div>
                        <div class="input-wrapper">
                            <label for="lastName">Last Name</label>
                            <input type="text" id="lastName" name="lastName" placeholder="Family name" required>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="input-wrapper">
                            <label for="company">Company Name</label>
                            <input type="text" id="company" name="company" placeholder="Company name" required>
                        </div>
                        <div class="input-wrapper">
                            <label for="role">Role</label>
                            <select id="role" name="role" required>
                                <option value="">Select a role...</option>
                                <optgroup label="Product & Design">
                                    <option value="Product Manager">Product Manager</option>
                                    <option value="Senior Product Manager">Senior Product Manager</option>
                                    <option value="Associate Product Manager">Associate Product Manager</option>
                                    <option value="Product Owner">Product Owner</option>
                                    <option value="UX Designer">UX Designer</option>
                                    <option value="UI Designer">UI Designer</option>
                                    <option value="Product Designer">Product Designer</option>
                                </optgroup>
                                <optgroup label="Engineering">
                                    <option value="Software Engineer">Software Engineer</option>
                                    <option value="Frontend Developer">Frontend Developer</option>
                                    <option value="Backend Developer">Backend Developer</option>
                                    <option value="Full Stack Developer">Full Stack Developer</option>
                                    <option value="DevOps Engineer">DevOps Engineer</option>
                                    <option value="Data Engineer">Data Engineer</option>
                                    <option value="QA Engineer">QA Engineer</option>
                                </optgroup>
                                <optgroup label="Data & Analytics">
                                    <option value="Data Analyst">Data Analyst</option>
                                    <option value="Data Scientist">Data Scientist</option>
                                    <option value="Business Analyst">Business Analyst</option>
                                    <option value="BI Analyst">BI Analyst</option>
                                </optgroup>
                                <optgroup label="Sales & Business Development">
                                    <option value="Sales Development Representative">Sales Development Representative (SDR)</option>
                                    <option value="Business Development Representative">Business Development Representative (BDR)</option>
                                    <option value="Account Executive">Account Executive</option>
                                    <option value="Account Manager">Account Manager</option>
                                    <option value="Business Development Manager">Business Development Manager</option>
                                    <option value="Sales Manager">Sales Manager</option>
                                    <option value="Partnerships Manager">Partnerships Manager</option>
                                </optgroup>
                                <optgroup label="Marketing">
                                    <option value="Marketing Manager">Marketing Manager</option>
                                    <option value="Growth Manager">Growth Manager</option>
                                    <option value="Content Manager">Content Manager</option>
                                    <option value="Social Media Manager">Social Media Manager</option>
                                    <option value="SEO Specialist">SEO Specialist</option>
                                    <option value="Performance Marketing Manager">Performance Marketing Manager</option>
                                </optgroup>
                                <optgroup label="Customer Success & Support">
                                    <option value="Customer Success Manager">Customer Success Manager</option>
                                    <option value="Customer Support Specialist">Customer Support Specialist</option>
                                    <option value="Implementation Specialist">Implementation Specialist</option>
                                    <option value="Technical Account Manager">Technical Account Manager</option>
                                </optgroup>
                                <optgroup label="HR & Recruiting">
                                    <option value="Recruiter">Recruiter</option>
                                    <option value="Technical Recruiter">Technical Recruiter</option>
                                    <option value="Talent Acquisition Specialist">Talent Acquisition Specialist</option>
                                    <option value="HR Business Partner">HR Business Partner</option>
                                    <option value="People Operations Manager">People Operations Manager</option>
                                    <option value="HR Manager">HR Manager</option>
                                </optgroup>
                                <optgroup label="Operations & Strategy">
                                    <option value="Operations Manager">Operations Manager</option>
                                    <option value="Project Manager">Project Manager</option>
                                    <option value="Program Manager">Program Manager</option>
                                    <option value="Strategy Associate">Strategy Associate</option>
                                    <option value="Chief of Staff">Chief of Staff</option>
                                </optgroup>
                                <optgroup label="Finance & Legal">
                                    <option value="Financial Analyst">Financial Analyst</option>
                                    <option value="Accountant">Accountant</option>
                                    <option value="Legal Counsel">Legal Counsel</option>
                                </optgroup>
                            </select>
                        </div>
                    </div>

                    <div class="form-row single">
                        <div class="input-wrapper">
                            <label for="email">Your Email <span>(optional - to receive a copy)</span></label>
                            <input type="email" id="email" name="email" placeholder="your@email.com">
                        </div>
                    </div>

                    <button type="submit" class="generate-btn" id="generateBtn">
                        Generate My Rejection Letter
                    </button>

                    <div class="error-message" id="errorMessage"></div>
                </form>

                <div class="result-container" id="resultContainer">
                    <div class="rejection-letter" id="rejectionLetter"></div>
                    <div class="action-buttons">
                        <button class="action-btn" onclick="copyToClipboard(event)">Copy to Clipboard</button>
                        <button class="action-btn" onclick="generateAnother()">Generate Another</button>
                    </div>
                </div>
            </div>

            <div class="footer-link">
                Part of <a href="https://www.nevoalmog.com">The Transition Project</a>
            </div>
        </div>
    </div>

    <script>
        // IMPORTANT: Use HTTPS!
        const API_URL = 'https://melodious-dedication-production-6d65.up.railway.app';
        const BASE_COUNT = 142;
        
        const thoughts = [
            "Hmm, how many ways can I say 'you're great, but...'?",
            "Should I mention the 847 other applicants? Nah, too honest.",
            "Let me consult my thesaurus for 'unfortunately'...",
            "Drafting... deleting... drafting again...",
            "Is 'We'll keep your resume on file' too cruel?",
            "Trying to sound human... is this human enough?",
            "Considering whether to use 'Dear' or 'Hi'... big decision.",
            "Adding a touch of corporate warmth... oxymoron detected.",
            "Searching for the perfect way to say nothing at all...",
            "Calculating the optimal amount of false hope...",
            "Wondering if anyone actually reads these...",
            "Inserting mandatory 'talented pool of candidates' phrase...",
            "Debating semicolon usage... this is important.",
            "Sprinkling in some strategic vagueness...",
            "Almost there... just need one more buzzword...",
            "Proofreading for accidentally honest sentences..."
        ];

        let currentRejection = '';
        let thoughtInterval;
        let currentThoughtIndex = 0;

        // Load counter on page load
        async function loadCounter() {
            try {
                const response = await fetch(`${API_URL}/api/counter`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                    }
                });
                
                if (!response.ok) throw new Error('Counter fetch failed');
                
                const data = await response.json();
                const displayCount = BASE_COUNT + (data.count || 0);
                document.getElementById('counter').textContent = displayCount.toLocaleString();
            } catch (error) {
                console.error('Counter error:', error);
                document.getElementById('counter').textContent = BASE_COUNT.toLocaleString();
            }
        }

        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        function showNextThought() {
            const thoughtEl = document.getElementById('thoughtText');
            
            if (currentThoughtIndex === 0) {
                shuffleArray(thoughts);
            }
            
            thoughtEl.style.animation = 'none';
            thoughtEl.offsetHeight;
            thoughtEl.textContent = thoughts[currentThoughtIndex];
            thoughtEl.style.animation = 'fadeInOut 3s ease-in-out';
            
            currentThoughtIndex = (currentThoughtIndex + 1) % thoughts.length;
        }

        function showLoadingModal() {
            document.getElementById('loadingModal').classList.add('active');
            currentThoughtIndex = 0;
            showNextThought();
            thoughtInterval = setInterval(showNextThought, 3000);
        }

        function hideLoadingModal() {
            document.getElementById('loadingModal').classList.remove('active');
            clearInterval(thoughtInterval);
        }

        function showError(message) {
            const errorEl = document.getElementById('errorMessage');
            errorEl.textContent = message;
            errorEl.classList.add('active');
            setTimeout(() => errorEl.classList.remove('active'), 5000);
        }

        document.getElementById('rejectionForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(e.target);
            const data = {
                firstName: formData.get('firstName'),
                lastName: formData.get('lastName'),
                company: formData.get('company'),
                role: formData.get('role'),
                email: formData.get('email') || null
            };

            document.getElementById('generateBtn').disabled = true;
            document.getElementById('resultContainer').classList.remove('active');
            document.getElementById('errorMessage').classList.remove('active');
            showLoadingModal();

            try {
                const response = await fetch(`${API_URL}/api/generate`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    throw new Error(`Server responded with ${response.status}`);
                }

                const result = await response.json();

                if (result.success) {
                    currentRejection = result.rejection_letter;
                    document.getElementById('rejectionLetter').textContent = currentRejection;
                    
                    const displayCount = BASE_COUNT + (result.count || 0);
                    document.getElementById('counter').textContent = displayCount.toLocaleString();
                    
                    hideLoadingModal();
                    document.getElementById('resultContainer').classList.add('active');
                    
                    document.getElementById('resultContainer').scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start' 
                    });
                } else {
                    throw new Error(result.error || 'Generation failed');
                }
            } catch (error) {
                console.error('Error:', error);
                hideLoadingModal();
                showError(`Failed to generate: ${error.message}. Please try again.`);
            } finally {
                document.getElementById('generateBtn').disabled = false;
            }
        });

        function copyToClipboard(event) {
            navigator.clipboard.writeText(currentRejection);
            const btn = event.target;
            const originalText = btn.textContent;
            btn.textContent = 'Copied!';
            setTimeout(() => {
                btn.textContent = originalText;
            }, 2000);
        }

        function generateAnother() {
            document.getElementById('resultContainer').classList.remove('active');
            document.getElementById('rejectionForm').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start' 
            });
            
            setTimeout(() => {
                document.getElementById('rejectionForm').dispatchEvent(new Event('submit'));
            }, 500);
        }

        // Initialize
        loadCounter();
    </script>
</body>
</html>
