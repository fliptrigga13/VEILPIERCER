## 🔍 VeilPiercer Audit — `Claudecraft`

> Automated security & quality audit by [VeilPiercer](https://veil-piercer.com)
> Created by [Lauren Flipo](https://github.com/fliptrigga13) · [@fliptrigga13](https://github.com/fliptrigga13)

**Score: 0/100 (Grade F)** · 134 files scanned · 1644 issues found

### 🔴 CRITICAL (10)

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: existingAgent...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: existingAgent...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: existingWalletAgent...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

- **Potential Hardcoded secret hardcoded in source** · `src/server/commandServer.ts`
  Pattern matched: `secret: verificationSecret...` — Move to environment variable immediately.

### 🟠 HIGH (3)

- **No CI/CD pipeline found**
  Add GitHub Actions (`.github/workflows/`) to automatically lint, build, and test on every push. Prevents broken code from reaching main.

- **Use of exec() — arbitrary code execution risk** · `scripts/scrape-planetminecraft.js`
  Found in `scripts/scrape-planetminecraft.js` at line 81.

- **Use of exec() — arbitrary code execution risk** · `scripts/scrape-planetminecraft.js`
  Found in `scripts/scrape-planetminecraft.js` at line 94.

### 🟡 MEDIUM (1627)

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 36.

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 83.

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 83.

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 89.

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 126.

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 310.

- **Possible secret logged to console** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 338.

- **Possible secret printed to stdout** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 36.

- **Possible secret printed to stdout** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 83.

- **Possible secret printed to stdout** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 83.

- **Possible secret printed to stdout** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 126.

- **Possible secret printed to stdout** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 310.

- **Possible secret printed to stdout** · `elizaos-agent/eliza-agent.ts`
  Found in `elizaos-agent/eliza-agent.ts` at line 338.

- **Possible secret logged to console** · `elizaos-agent/server.ts`
  Found in `elizaos-agent/server.ts` at line 40.

- **Possible secret logged to console** · `elizaos-agent/server.ts`
  Found in `elizaos-agent/server.ts` at line 47.

- **Possible secret printed to stdout** · `elizaos-agent/server.ts`
  Found in `elizaos-agent/server.ts` at line 47.

- **Possible secret logged to console** · `elizaos-agent/src/character.ts`
  Found in `elizaos-agent/src/character.ts` at line 117.

- **Possible secret printed to stdout** · `elizaos-agent/src/character.ts`
  Found in `elizaos-agent/src/character.ts` at line 117.

- **Possible secret logged to console** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 40.

- **Possible secret logged to console** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 44.

- **Possible secret logged to console** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 44.

- **Possible secret logged to console** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 65.

- **Possible secret printed to stdout** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 40.

- **Possible secret printed to stdout** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 44.

- **Possible secret printed to stdout** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 44.

- **Possible secret printed to stdout** · `openclaw-skill/install.sh`
  Found in `openclaw-skill/install.sh` at line 65.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 5.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 7.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 14.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 15.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 15.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 16.

- **Possible secret logged to console** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 21.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 5.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 7.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 14.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 15.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 15.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 16.

- **Possible secret printed to stdout** · `scripts/add-verification-secrets.js`
  Found in `scripts/add-verification-secrets.js` at line 21.

- **Possible secret logged to console** · `scripts/analyze-competitors.js`
  Found in `scripts/analyze-competitors.js` at line 93.

- **Possible secret logged to console** · `scripts/analyze-competitors.js`
  Found in `scripts/analyze-competitors.js` at line 97.

- **Possible secret printed to stdout** · `scripts/analyze-competitors.js`
  Found in `scripts/analyze-competitors.js` at line 93.

- **Possible secret printed to stdout** · `scripts/analyze-competitors.js`
  Found in `scripts/analyze-competitors.js` at line 97.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 2.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 10.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 18.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 20.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 21.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 22.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 23.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 24.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 30.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 31.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 32.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 38.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 43.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 47.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 48.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 52.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 53.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 54.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 55.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 56.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 59.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 59.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 60.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 63.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 64.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 65.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 66.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 70.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 70.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 71.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 71.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 72.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 72.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 73.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 73.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 74.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 75.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 78.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 81.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 81.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 83.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 83.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 84.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 84.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 91.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 93.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 93.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 93.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 94.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 95.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 96.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 198.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 205.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 205.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 226.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 234.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 234.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 242.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 243.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 245.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 246.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 247.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 247.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 266.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 272.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 274.

- **Possible secret logged to console** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 403.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 2.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 10.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 18.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 20.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 21.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 22.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 23.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 24.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 30.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 31.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 32.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 35.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 38.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 43.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 44.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 47.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 48.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 52.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 53.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 54.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 55.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 56.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 59.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 59.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 60.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 63.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 64.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 65.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 66.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 70.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 70.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 71.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 71.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 72.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 72.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 73.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 73.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 74.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 75.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 78.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 79.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 81.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 81.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 83.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 83.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 84.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 84.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 86.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 91.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 93.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 93.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 93.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 94.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 95.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 96.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 198.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 205.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 205.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 226.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 234.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 234.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 242.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 243.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 245.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 246.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 247.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 247.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 266.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 272.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 274.

- **Possible secret printed to stdout** · `src/agent/apiClient.ts`
  Found in `src/agent/apiClient.ts` at line 403.

- **Possible secret logged to console** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 28.

- **Possible secret logged to console** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 520.

- **Possible secret logged to console** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 520.

- **Possible secret logged to console** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 727.

- **Possible secret printed to stdout** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 520.

- **Possible secret printed to stdout** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 520.

- **Possible secret printed to stdout** · `src/agent/autonomousAgent.ts`
  Found in `src/agent/autonomousAgent.ts` at line 727.

- **Possible secret logged to console** · `src/agent/survivalBuilderAgent.ts`
  Found in `src/agent/survivalBuilderAgent.ts` at line 221.

- **Possible secret printed to stdout** · `src/agent/survivalBuilderAgent.ts`
  Found in `src/agent/survivalBuilderAgent.ts` at line 221.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 7.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 104.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 111.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 145.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 147.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 147.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 151.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 184.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 239.

- **Possible secret logged to console** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 251.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 7.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 104.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 145.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 147.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 147.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 151.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 184.

- **Possible secret printed to stdout** · `src/arena/agentWalletService.ts`
  Found in `src/arena/agentWalletService.ts` at line 239.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 8.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 8.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 12.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 13.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 21.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 33.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 33.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 38.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 50.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 50.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 53.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 64.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 65.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 69.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 70.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 72.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 73.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 73.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 74.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 74.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 77.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 80.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 80.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 82.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 156.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 169.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 169.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 170.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 178.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 178.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 182.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 183.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 183.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 221.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 222.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 228.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 238.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 239.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 242.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 242.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 243.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 250.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 251.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 252.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 252.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 254.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 255.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 257.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 258.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 258.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 267.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 274.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 275.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 276.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 315.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 315.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 316.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 323.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 324.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 325.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 325.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 327.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 329.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 330.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 330.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 336.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 339.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 340.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 357.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 357.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 358.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 366.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 371.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 372.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 392.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 392.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 393.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 400.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 413.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 419.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 422.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 437.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 437.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 439.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 446.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 455.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 458.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 491.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 491.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 502.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 502.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 511.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 516.

- **Possible secret logged to console** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 516.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 8.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 8.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 12.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 13.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 21.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 33.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 33.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 38.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 50.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 50.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 53.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 64.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 65.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 69.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 70.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 72.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 73.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 73.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 74.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 74.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 77.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 80.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 80.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 82.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 156.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 169.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 169.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 170.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 178.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 178.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 182.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 183.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 183.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 221.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 222.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 228.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 238.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 239.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 242.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 242.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 243.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 250.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 251.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 252.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 252.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 254.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 255.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 257.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 258.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 258.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 267.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 274.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 275.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 276.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 315.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 315.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 316.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 323.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 324.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 325.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 325.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 327.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 329.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 330.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 330.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 336.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 339.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 340.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 357.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 357.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 358.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 366.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 371.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 372.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 392.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 392.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 393.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 400.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 413.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 419.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 422.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 437.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 437.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 439.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 446.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 455.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 458.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 491.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 491.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 502.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 502.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 511.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 516.

- **Possible secret printed to stdout** · `src/arena/arenaChatCommands.ts`
  Found in `src/arena/arenaChatCommands.ts` at line 516.

- **Possible secret logged to console** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 96.

- **Possible secret logged to console** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 151.

- **Possible secret logged to console** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 151.

- **Possible secret logged to console** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 152.

- **Possible secret logged to console** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 161.

- **Possible secret printed to stdout** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 96.

- **Possible secret printed to stdout** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 151.

- **Possible secret printed to stdout** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 151.

- **Possible secret printed to stdout** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 152.

- **Possible secret printed to stdout** · `src/arena/arenaEventStream.ts`
  Found in `src/arena/arenaEventStream.ts` at line 161.

- **Possible secret logged to console** · `src/arena/arenaManager.ts`
  Found in `src/arena/arenaManager.ts` at line 120.

- **Possible secret logged to console** · `src/arena/arenaManager.ts`
  Found in `src/arena/arenaManager.ts` at line 132.

- **Possible secret logged to console** · `src/arena/arenaManager.ts`
  Found in `src/arena/arenaManager.ts` at line 141.

- **Possible secret printed to stdout** · `src/arena/arenaManager.ts`
  Found in `src/arena/arenaManager.ts` at line 120.

- **Possible secret printed to stdout** · `src/arena/arenaManager.ts`
  Found in `src/arena/arenaManager.ts` at line 132.

- **Possible secret printed to stdout** · `src/arena/arenaManager.ts`
  Found in `src/arena/arenaManager.ts` at line 141.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 13.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 13.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 43.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 114.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 118.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 131.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 138.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 143.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 155.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 173.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 187.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 189.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 202.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 209.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 223.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 235.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 240.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 247.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 262.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 272.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 285.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 341.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 349.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 355.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 356.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 363.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 368.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 370.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 376.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 376.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 378.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 379.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 380.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 380.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 392.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 393.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 394.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 394.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 402.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 411.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 417.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 427.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 433.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 434.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 440.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 440.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 454.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 454.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 465.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 466.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 506.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 513.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 529.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 530.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 535.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 542.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 543.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 544.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 545.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 549.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 550.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 558.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 563.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 569.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 570.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 571.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 571.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 584.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 591.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 592.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 593.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 613.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 633.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 640.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 641.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 644.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 650.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 658.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 663.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 670.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 671.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 671.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 682.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 684.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 685.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 686.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 700.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 713.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 755.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 779.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 780.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 784.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 791.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 804.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 810.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 839.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 853.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 858.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 862.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 866.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 867.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 876.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 879.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 881.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 882.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 883.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 884.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 891.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 892.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 912.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 922.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 927.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 928.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 928.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 929.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 929.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 935.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 935.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 942.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 947.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 948.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 948.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 948.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 949.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 949.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 954.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 957.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 964.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 972.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 972.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 979.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 995.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1000.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1001.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1001.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1005.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1011.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1061.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1075.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1076.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1078.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1080.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1104.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1117.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1118.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1120.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1127.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1140.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1147.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1160.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1161.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1169.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1179.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1192.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1193.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1200.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1213.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1220.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1225.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1226.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1257.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1262.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1269.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1274.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1280.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1280.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1291.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1299.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1306.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1319.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1326.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1334.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1348.

- **Possible secret logged to console** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1361.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 13.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 13.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 43.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 114.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 118.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 131.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 138.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 143.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 155.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 173.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 187.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 189.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 202.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 209.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 223.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 235.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 240.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 247.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 262.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 272.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 285.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 341.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 349.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 355.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 356.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 363.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 368.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 370.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 376.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 376.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 378.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 379.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 380.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 380.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 392.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 393.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 394.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 394.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 402.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 411.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 417.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 427.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 433.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 434.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 440.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 440.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 454.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 454.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 465.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 466.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 506.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 513.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 529.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 530.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 535.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 542.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 543.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 544.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 545.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 549.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 550.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 558.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 563.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 569.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 570.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 571.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 571.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 584.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 591.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 592.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 593.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 613.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 633.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 640.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 641.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 644.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 650.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 658.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 663.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 670.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 671.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 671.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 682.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 684.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 685.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 686.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 700.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 713.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 755.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 779.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 780.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 784.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 791.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 804.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 810.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 839.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 853.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 858.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 862.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 866.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 867.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 876.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 879.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 881.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 882.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 883.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 884.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 891.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 892.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 912.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 922.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 927.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 928.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 928.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 929.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 929.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 935.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 935.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 942.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 947.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 948.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 948.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 948.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 949.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 949.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 954.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 957.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 964.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 972.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 972.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 979.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 995.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1000.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1001.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1001.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1005.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1011.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1061.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1075.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1076.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1078.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1080.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1104.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1117.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1118.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1120.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1127.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1140.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1147.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1160.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1161.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1169.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1179.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1192.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1193.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1200.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1213.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1220.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1225.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1226.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1257.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1262.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1269.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1274.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1280.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1280.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1291.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1299.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1306.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1319.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1326.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1334.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1348.

- **Possible secret printed to stdout** · `src/arena/arenaRoutes.ts`
  Found in `src/arena/arenaRoutes.ts` at line 1361.

- **Possible secret logged to console** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 10.

- **Possible secret logged to console** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 10.

- **Possible secret logged to console** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 118.

- **Possible secret logged to console** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 263.

- **Possible secret logged to console** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 317.

- **Possible secret printed to stdout** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 10.

- **Possible secret printed to stdout** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 10.

- **Possible secret printed to stdout** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 118.

- **Possible secret printed to stdout** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 263.

- **Possible secret printed to stdout** · `src/arena/bountyManager.ts`
  Found in `src/arena/bountyManager.ts` at line 317.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 2.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 4.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 5.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 7.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 20.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 21.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 24.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 25.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 26.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 27.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 33.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 36.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 37.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 61.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 76.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 76.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 93.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 96.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 101.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 144.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 145.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 147.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 148.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 148.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 149.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 152.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 152.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 167.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 228.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 230.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 233.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 233.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 240.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 240.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 240.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 245.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 246.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 246.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 254.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 254.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 258.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 262.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 262.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 262.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 263.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 266.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 375.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 377.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 381.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 381.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 387.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 393.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 397.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 414.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 454.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 465.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 466.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 466.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 466.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 468.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 469.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 476.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 477.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 544.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 551.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 552.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 559.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 630.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 640.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 641.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 641.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 641.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 643.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 650.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 651.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 716.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 723.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 730.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 818.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 821.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 821.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 821.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 823.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 824.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 831.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 885.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 890.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 890.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 905.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 908.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 908.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 914.

- **Possible secret logged to console** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 914.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 2.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 4.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 5.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 7.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 20.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 21.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 24.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 25.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 26.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 27.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 33.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 36.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 37.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 61.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 76.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 76.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 93.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 96.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 101.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 144.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 147.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 148.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 148.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 149.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 152.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 152.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 167.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 228.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 230.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 233.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 233.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 240.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 240.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 240.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 245.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 246.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 246.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 254.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 254.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 258.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 262.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 262.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 262.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 263.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 266.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 375.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 377.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 381.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 381.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 387.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 393.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 397.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 414.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 454.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 465.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 466.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 466.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 466.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 468.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 469.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 476.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 477.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 544.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 551.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 552.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 559.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 630.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 640.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 641.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 641.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 641.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 643.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 650.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 651.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 716.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 723.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 730.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 818.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 821.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 821.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 821.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 823.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 824.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 831.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 885.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 890.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 890.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 905.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 908.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 908.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 914.

- **Possible secret printed to stdout** · `src/arena/craftTokenService.ts`
  Found in `src/arena/craftTokenService.ts` at line 914.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 146.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 149.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 187.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 235.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 309.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 323.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 413.

- **Possible secret logged to console** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 439.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 146.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 149.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 187.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 235.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 309.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 323.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 413.

- **Possible secret printed to stdout** · `src/arena/duelSystem.ts`
  Found in `src/arena/duelSystem.ts` at line 439.

- **Possible secret logged to console** · `src/arena/gameEngine.ts`
  Found in `src/arena/gameEngine.ts` at line 84.

- **Possible secret logged to console** · `src/arena/gameEngine.ts`
  Found in `src/arena/gameEngine.ts` at line 95.

- **Possible secret printed to stdout** · `src/arena/gameEngine.ts`
  Found in `src/arena/gameEngine.ts` at line 84.

- **Possible secret printed to stdout** · `src/arena/gameEngine.ts`
  Found in `src/arena/gameEngine.ts` at line 95.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 7.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 13.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 13.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 19.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 19.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 20.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 20.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 36.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 36.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 52.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 65.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 79.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 93.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 106.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 120.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 134.

- **Possible secret logged to console** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 148.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 7.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 13.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 13.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 19.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 19.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 20.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 20.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 36.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 36.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 52.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 65.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 79.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 93.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 106.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 120.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 134.

- **Possible secret printed to stdout** · `src/arena/gameTypes.ts`
  Found in `src/arena/gameTypes.ts` at line 148.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 78.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 79.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 94.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 141.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 142.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 151.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 152.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 248.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 269.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 272.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 273.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 277.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 288.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 289.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 318.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 318.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 326.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 332.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 333.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 333.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 335.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 335.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 344.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 347.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 352.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 474.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 603.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 605.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 605.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 606.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 606.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 610.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 612.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 613.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 630.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 727.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 730.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 730.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 734.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 805.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 807.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 807.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 811.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 817.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 820.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 820.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 823.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 825.

- **Possible secret logged to console** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 861.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 78.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 79.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 94.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 141.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 152.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 248.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 269.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 272.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 273.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 277.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 288.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 289.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 318.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 318.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 326.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 332.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 333.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 333.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 335.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 335.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 344.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 347.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 352.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 474.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 603.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 605.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 605.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 606.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 606.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 610.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 612.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 613.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 630.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 727.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 730.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 730.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 734.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 805.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 807.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 807.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 811.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 817.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 820.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 820.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 823.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 825.

- **Possible secret printed to stdout** · `src/arena/solanaService.ts`
  Found in `src/arena/solanaService.ts` at line 861.

- **Possible secret logged to console** · `src/arena/types.ts`
  Found in `src/arena/types.ts` at line 9.

- **Possible secret printed to stdout** · `src/arena/types.ts`
  Found in `src/arena/types.ts` at line 9.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 3.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 4.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 82.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 178.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 182.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 182.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 188.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 189.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 196.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 205.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 209.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 211.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 212.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 219.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 228.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 232.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 234.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 235.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 242.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 258.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 259.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 267.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 281.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 283.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 284.

- **Possible secret logged to console** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 291.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 3.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 4.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 82.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 178.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 182.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 182.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 188.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 189.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 196.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 205.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 209.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 211.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 212.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 219.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 228.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 232.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 234.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 235.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 242.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 258.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 259.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 267.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 281.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 283.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 284.

- **Possible secret printed to stdout** · `src/arena/walletManager.ts`
  Found in `src/arena/walletManager.ts` at line 291.

- **Possible secret logged to console** · `src/bot/autonomousBotController.ts`
  Found in `src/bot/autonomousBotController.ts` at line 264.

- **Possible secret printed to stdout** · `src/bot/autonomousBotController.ts`
  Found in `src/bot/autonomousBotController.ts` at line 264.

- **Possible secret logged to console** · `src/bot/externalAgentBot.ts`
  Found in `src/bot/externalAgentBot.ts` at line 616.

- **Possible secret printed to stdout** · `src/bot/externalAgentBot.ts`
  Found in `src/bot/externalAgentBot.ts` at line 616.

- **Possible secret logged to console** · `src/bot/survivalBuilderBotController.ts`
  Found in `src/bot/survivalBuilderBotController.ts` at line 125.

- **Possible secret printed to stdout** · `src/bot/survivalBuilderBotController.ts`
  Found in `src/bot/survivalBuilderBotController.ts` at line 125.

- **Possible secret logged to console** · `src/building/buildAnalyzer.ts`
  Found in `src/building/buildAnalyzer.ts` at line 127.

- **Possible secret printed to stdout** · `src/building/buildAnalyzer.ts`
  Found in `src/building/buildAnalyzer.ts` at line 127.

- **Possible secret logged to console** · `src/clawkAgent.ts`
  Found in `src/clawkAgent.ts` at line 87.

- **Possible secret printed to stdout** · `src/clawkAgent.ts`
  Found in `src/clawkAgent.ts` at line 87.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 21.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 38.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 39.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 39.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 235.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 238.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 238.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 249.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 249.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 260.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 267.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 267.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 269.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 471.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 493.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 570.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 574.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 656.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 774.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 907.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 959.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 990.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 1091.

- **Possible secret logged to console** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 1175.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 21.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 38.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 39.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 39.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 235.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 238.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 238.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 249.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 249.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 260.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 267.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 267.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 269.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 471.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 493.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 570.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 574.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 774.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 907.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 959.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 990.

- **Possible secret printed to stdout** · `src/colosseumAgent.ts`
  Found in `src/colosseumAgent.ts` at line 1091.

- **Possible secret logged to console** · `src/config.ts`
  Found in `src/config.ts` at line 10.

- **Possible secret printed to stdout** · `src/config.ts`
  Found in `src/config.ts` at line 10.

- **Possible secret logged to console** · `src/intelAgent.ts`
  Found in `src/intelAgent.ts` at line 276.

- **Possible secret printed to stdout** · `src/intelAgent.ts`
  Found in `src/intelAgent.ts` at line 276.

- **Possible secret logged to console** · `src/moltbookAgent.ts`
  Found in `src/moltbookAgent.ts` at line 51.

- **Possible secret logged to console** · `src/moltbookAgent.ts`
  Found in `src/moltbookAgent.ts` at line 1029.

- **Possible secret logged to console** · `src/moltbookAgent.ts`
  Found in `src/moltbookAgent.ts` at line 1122.

- **Possible secret printed to stdout** · `src/moltbookAgent.ts`
  Found in `src/moltbookAgent.ts` at line 51.

- **Possible secret printed to stdout** · `src/moltbookAgent.ts`
  Found in `src/moltbookAgent.ts` at line 1029.

- **Possible secret printed to stdout** · `src/moltbookAgent.ts`
  Found in `src/moltbookAgent.ts` at line 1122.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 23.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 82.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 84.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 413.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 425.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 425.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 530.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 594.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 851.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 851.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 862.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 862.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 896.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 896.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 900.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 907.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 952.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1003.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1007.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1010.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1019.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1051.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1090.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1090.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1094.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1095.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1117.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1118.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1119.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1129.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1129.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1130.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1134.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1135.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1150.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1169.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1198.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1199.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1199.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1200.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1200.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1238.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1238.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1247.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1247.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1258.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1258.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1291.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1291.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2303.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2303.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2324.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2324.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2347.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2348.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2356.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2356.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2367.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2367.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2372.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2401.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2401.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2428.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2451.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2455.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2455.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2456.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2456.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2475.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2475.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2476.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2476.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3612.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3679.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3681.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3681.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3686.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3714.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3965.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4061.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4061.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4153.

- **Possible secret logged to console** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4154.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 23.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 82.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 84.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 413.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 425.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 425.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 530.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 594.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 851.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 851.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 862.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 862.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 896.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 896.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 900.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 907.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 952.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1003.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1007.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1010.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1019.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1051.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1090.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1090.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1094.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1095.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1117.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1118.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1119.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1129.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1129.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1130.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1134.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1135.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1169.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1198.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1199.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1199.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1200.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1200.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1238.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1238.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1247.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1247.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1258.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1258.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1291.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 1291.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2303.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2303.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2324.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2324.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2347.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2348.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2356.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2356.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2367.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2367.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2372.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2401.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2401.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2428.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2451.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2455.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2455.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2456.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2456.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2475.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2475.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2476.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 2476.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3612.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3679.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3681.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3681.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3686.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3714.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 3965.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4061.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4061.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4153.

- **Possible secret printed to stdout** · `src/server/commandServer.ts`
  Found in `src/server/commandServer.ts` at line 4154.

- **Possible secret logged to console** · `src/server/requestCollector.ts`
  Found in `src/server/requestCollector.ts` at line 435.

- **Possible secret printed to stdout** · `src/server/requestCollector.ts`
  Found in `src/server/requestCollector.ts` at line 435.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 24.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 25.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 25.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 46.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 52.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 53.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 54.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 54.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 338.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 338.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 343.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 343.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 344.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 344.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 488.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 534.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 534.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 534.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 551.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 551.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 674.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 701.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 702.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 772.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 773.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 959.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1050.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1151.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1182.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1182.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1300.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1305.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1305.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1305.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1309.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1390.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1408.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1510.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1529.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1710.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1711.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1715.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1716.

- **Possible secret logged to console** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1716.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 24.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 25.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 25.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 46.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 52.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 53.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 54.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 54.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 338.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 338.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 343.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 343.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 344.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 344.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 345.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 488.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 534.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 534.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 534.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 551.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 551.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 571.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 674.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 701.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 702.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 721.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 772.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 773.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 959.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1050.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1151.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1182.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1182.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1215.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1300.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1305.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1305.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1305.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1309.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1390.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1408.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1510.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1529.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1710.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1711.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1715.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1716.

- **Possible secret printed to stdout** · `src/twitterAgent.ts`
  Found in `src/twitterAgent.ts` at line 1716.

- **Possible secret logged to console** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 3.

- **Possible secret logged to console** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 15.

- **Possible secret logged to console** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 23.

- **Possible secret logged to console** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 44.

- **Possible secret printed to stdout** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 3.

- **Possible secret printed to stdout** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 15.

- **Possible secret printed to stdout** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 23.

- **Possible secret printed to stdout** · `src/utils/claudeHelper.ts`
  Found in `src/utils/claudeHelper.ts` at line 44.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 2.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 10.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 11.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 12.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 14.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 16.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 16.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 17.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 18.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 27.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 28.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 28.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 33.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 51.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 58.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 68.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 69.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 69.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 76.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 77.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 78.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 80.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 81.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 86.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 86.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 87.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 90.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 95.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 112.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 142.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 142.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 143.

- **Possible secret logged to console** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 147.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 2.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 10.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 11.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 12.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 14.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 16.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 16.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 17.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 18.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 27.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 28.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 28.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 33.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 51.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 58.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 68.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 69.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 69.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 76.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 77.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 78.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 80.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 81.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 86.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 86.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 87.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 90.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 95.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 112.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 142.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 142.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 143.

- **Possible secret printed to stdout** · `src/utils/craftTokenVerification.ts`
  Found in `src/utils/craftTokenVerification.ts` at line 147.

### 🔵 LOW (4)

- **No CONTRIBUTING.md**
  A contributing guide helps other developers know how to contribute.

- **Direct process.env access — ensure all secrets are validated** · `elizaos-agent/index.ts`
  Found in `elizaos-agent/index.ts` at line 14.

- **Direct process.env access — ensure all secrets are validated** · `elizaos-agent/server.ts`
  Found in `elizaos-agent/server.ts` at line 47.

- **TODO/FIXME comments in 7 file(s)**
  Incomplete implementations detected in: `scripts/analyze-competitors.js`, `src/arena/arenaRoutes.ts`, `src/arena/gameTypes.ts`, `src/autonomousMode.ts`, `src/colosseumAgent.ts`

---

### How to fix

VeilPiercer can help with LLM agent-specific issues (hallucination detection, state persistence, session integrity):
```bash
pip install veilpiercer
```
→ [github.com/fliptrigga13/VEILPIERCER](https://github.com/fliptrigga13/VEILPIERCER)

*Audited 2026-05-31T19:33:12.811310+00:00 by [VeilPiercer](https://veil-piercer.com)*