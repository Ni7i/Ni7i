# Hi, I'm Abdul Kareem 👋

> Senior Software Developer · C# · .NET · Cross-Platform Desktop

---

## 🧑‍💻 About Me

I'm a senior C# developer with a passion for clean architecture, performant desktop applications, and cross-platform engineering. I thrive on technically challenging problems — from real-time simulations to polished, production-ready GUIs.

Currently competing at the **Regional ICT Skills Championship 2026 (Skill 09 – Software Application Development)**, where I'm building a full-featured Population Simulation Prototype from scratch — solo, under time pressure, on a cross-platform constraint.

---

## 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| **Primary Language** | C# (.NET 8) |
| **Desktop UI** | Avalonia UI 11 (cross-platform XAML) |
| **Architecture** | MVVM, ObservableCollections, Data Binding |
| **Serialization** | System.Text.Json |
| **IDE** | JetBrains Rider |
| **Platform** | macOS (Apple Silicon M4) → Windows x64 deployment |
| **Build & Deploy** | `dotnet publish`, self-contained executables |
| **Version Control** | Git |

---

## 🏆 Highlight Project — Population Simulation Prototype

A real-time desktop simulation engine and GUI editor built for competition in under a day.

**What it does:**
- Simulates citizens moving across a 10×10 km map according to daily schedules
- Physics: 5 km/h travel speed, Euclidean distance, 1-min simulation steps
- Full CRUD GUI for locations, citizens, and schedule events
- World state load/save via JSON
- 60+ simulation steps/second with double-buffered custom map rendering

**Technical highlights:**
- Custom `MapControl` using Avalonia's `OnRender` pipeline for flicker-free rendering
- Distance-based arrival timing (not schedule-time-based) — physically accurate
- Conflict validation in the schedule editor before saving
- Self-contained `win-x64` executable published from macOS via `dotnet publish`
- Resolved non-trivial namespace collisions between Avalonia and domain models
- Cross-platform from day one — zero WPF, zero Windows-only APIs

---

## 💡 Engineering Principles

- **Cross-platform by default** — I don't build for one OS; I build for the right abstraction
- **Performance matters** — simulation loops, render pipelines, and data structures all get profiled
- **Clean MVVM** — ViewModels own state, Views own nothing
- **Ship it** — I reserve time for packaging, delivery structure, and documentation

---

## 📫 Get in Touch

| | |
|---|---|
| 📧 Email | `your.email@example.com` |
| 💼 LinkedIn | `linkedin.com/in/yourprofile` |
| 🐙 GitHub | `github.com/yourusername` |
| 📍 Location | *(your city / country)* |

---

*Open to senior C# / .NET roles, desktop application development, and simulation engineering projects.*
