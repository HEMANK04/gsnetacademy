# =========================================================
#  GS Net Academy — static site + leads API, ek hi container
#  Ye file repo ROOT me rakhein (index.html ke bagal me)
# =========================================================

# ---------- 1. Static site taiyaar karo ----------
# Poore repo ki copy leke usme se server/ aur dev files hata dete hain.
# Jo bachta hai = pure static site. Isliye html/css/js ke naam
# yahan likhne ki zaroorat nahi.
FROM node:22-alpine AS static
WORKDIR /site
COPY . .
RUN rm -rf server .git .github .vscode \
           package.json package-lock.json tailwind.config.js \
           Dockerfile docker-compose.yml README.txt

# ---------- 2. API dependencies ----------
FROM node:22-alpine AS deps
WORKDIR /app
COPY server/package.json server/package-lock.json* ./
RUN npm ci --omit=dev || npm install --omit=dev

# ---------- 3. Final image ----------
FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=5000

RUN addgroup -g 1001 -S nodejs && adduser -S nodeapp -u 1001

COPY --from=deps   --chown=nodeapp:nodejs /app/node_modules ./node_modules
COPY               --chown=nodeapp:nodejs server/ ./
COPY --from=static --chown=nodeapp:nodejs /site ./public

USER nodeapp
EXPOSE 5000
CMD ["node", "index.js"]