# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TapAlert is a marketing landing page for an emergency alert mobile application. This is a **static website** with no build system, backend, or package management. The landing page promotes TapAlert's core features: SMS-based emergency alerts, check-in timers, voice-to-text capabilities, and Android-specific direct SMS functionality.

## Architecture

**Single-file static site:**
- `index.html` - Complete landing page (856 lines) with embedded CSS and vanilla JavaScript
- All styles are inline within `<style>` tags in the HTML head
- All JavaScript is inline within `<script>` tags at the end of the HTML body
- No external dependencies, frameworks, or build tools

**JavaScript functionality:**
- Smooth scrolling for anchor link navigation
- Intersection Observer API for fade-in animations on scroll
- Observes `.feature-card`, `.pricing-card`, and `.use-case` elements

**Unused files:**
- `plane-landing.js` and `plane-landing 2.js` - Lucide icon library exports (not currently used in the HTML)
- These appear to be leftover files and are not referenced by the landing page

## Development Workflow

**Local development:**
```bash
# Open directly in browser (no server required)
open index.html

# Or serve with any HTTP server
python3 -m http.server 8000
# Then visit http://localhost:8000
```

**Deployment:**
This site can be hosted on any static hosting service (GitHub Pages, Netlify, Vercel, S3, etc.) by simply uploading the `index.html` file.

## Content Structure

The landing page follows this structure:
1. Hero section with gradient background
2. Features grid (One-tap alerts, check-in timer, voice-to-text, etc.)
3. Video/demo section
4. Android vs iOS comparison
5. Pricing tiers (Basic free, Standard $15, Premium $40)
6. Use cases (outdoor enthusiasts, solo travelers, etc.)
7. Footer with links

## Editing Guidelines

When modifying this site:
- All changes go in `index.html` (CSS in `<style>`, JS in `<script>`, content in HTML)
- The site uses a purple gradient color scheme (`#667eea` to `#764ba2`) for primary elements
- Android features are highlighted with green (`#3ddc84`)
- Maintain responsive design - grid layouts use `repeat(auto-fit, minmax(...))`
- Keep the inline approach - do not split into separate CSS/JS files unless explicitly requested
