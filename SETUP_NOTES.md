# Restructuring Notes: Professional Course Website

## 🎯 Objective Completed

Transform `curso-ia-web` from a basic documentation site into a **professional, university-level course website** (inspired by Berkeley/Stanford/NYU models) with:

- ✅ Comprehensive curriculum structure for 8 sessions
- ✅ Professional course organization with theory and practical components
- ✅ Pre-configured labs with Jupyter Notebook approach (no "learn to code from scratch")
- ✅ Group project guidelines and evaluations (T1=30%, T2=30%, T3=40%)
- ✅ Gradual content release (unreleased content marked as locked)
- ✅ Centralized configuration for easy date management

## 📊 What Was Created

### Core Infrastructure

1. **config/course.yaml** - Centralized course configuration
   - All 8 session dates and times (modifiable in one place)
   - Contact information
   - Grading formula and breakdown
   - Prerequisites and learning outcomes
   - Course metadata

2. **Updated mkdocs.yml** - Comprehensive navigation structure
   - ~8 main sections with subsections
   - Proper organization for materials
   - Material theme with Spanish language support

### Content Pages Created (21 markdown files)

#### Course Information (3 pages)
- `docs/curso/syllabus.md` - Full course syllabus with policies
- `docs/curso/cronograma.md` - Detailed schedule with all 8 sessions
- `docs/curso/calificacion.md` - Grading system with rubrics and formulas

#### Sessions (5 pages)
- `docs/sesiones/sesion1.md` - **Available** - Intro to AI in Civil Engineering (with full content)
- `docs/sesiones/sesion2.md` - **Locked** - Big Data and Real Cases
- `docs/sesiones/sesion3.md` - **Locked** - ML Models
- `docs/sesiones/sesion5.md` - **Locked** - Signal Processing and Clustering
- `docs/sesiones/sesion6.md` - **Locked** - Future Models and Trends

#### Laboratories (4 pages)
- `docs/labs/index.md` - Lab overview and professional approach explanation
- `docs/labs/lab1.md` - **Available** - ML Fundamentals lab (detailed with tasks)
- `docs/labs/lab2.md` - **Locked** - Structural Health Monitoring
- `docs/labs/lab3.md` - **Locked** - Clustering and Signal Processing

#### Group Projects (4 pages)
- `docs/trabajos/guia.md` - General guidelines for all group projects
- `docs/trabajos/trabajo1.md` - **Available** - T1 Group Project (30%)
- `docs/trabajos/trabajo2.md` - **Locked** - T2 Group Project (30%)
- `docs/trabajos/trabajo3.md` - **Locked** - T3 Group Project (40%)

#### Resources (3 pages)
- `docs/recursos/herramientas.md` - Setup guide, Python, Jupyter, tools
- `docs/recursos/librerias.md` - Python libraries (NumPy, Pandas, Scikit-learn, etc.)
- `docs/recursos/referencias.md` - Books, papers, courses, blogs

#### Other (1 page)
- `docs/faq.md` - Comprehensive FAQ with 50+ questions

### Home Page Enhancement
- Professional course overview with table of course structure
- Learning objectives and program approach
- Call-to-action buttons
- Visual hierarchy inspired by university course pages

## 🔑 Key Features

### 1. **Professional Approach**
- Pre-configured Jupyter Notebooks (not learning to code from scratch)
- Real data from structural sensors (bridges, buildings, tunnels)
- Professional-level exercises (modify hyperparameters, analyze outputs)
- Real-world cases: Structural Health Monitoring (SHM), Digital Twins, etc.

### 2. **Gradual Content Release**
- Unreleased content marked with `!!! warning` boxes
- Clear indication of when content becomes available
- Example: "🔒 Próxima Sesión - Disponible desde: Fecha"
- Users know exactly when to come back

### 3. **Centralized Configuration**
- All course dates in `config/course.yaml`
- Modify once, used everywhere
- Dates for all 8 sessions, 3 evaluations, meeting times

### 4. **University-Level Structure**
- Comprehensive syllabus with policies
- Professional grading system with rubrics
- Learning outcomes clearly defined
- Prerequisite requirements
- Course policies on plagiarism, late submissions, etc.

### 5. **Professional Labs**
- Professional approach explained clearly
- No "learn to code from scratch"
- Focus on: modify, analyze, interpret, decide
- Pre-configured notebooks ready to use

## 📁 Directory Structure

```
curso-ia-web/
├── config/
│   └── course.yaml              # Centralized course config
├── docs/
│   ├── index.md                 # Home page
│   ├── faq.md                   # FAQ
│   ├── curso/
│   │   ├── syllabus.md
│   │   ├── cronograma.md
│   │   └── calificacion.md
│   ├── sesiones/
│   │   ├── sesion1.md           # Available
│   │   ├── sesion2-6.md         # Locked (coming soon)
│   ├── labs/
│   │   ├── index.md
│   │   ├── lab1.md              # Available
│   │   └── lab2-3.md            # Locked (coming soon)
│   ├── trabajos/
│   │   ├── guia.md
│   │   ├── trabajo1.md          # Available
│   │   └── trabajo2-3.md        # Locked (coming soon)
│   └── recursos/
│       ├── herramientas.md
│       ├── librerias.md
│       └── referencias.md
├── .github/workflows/
│   └── deploy.yml               # GitHub Pages deployment
├── mkdocs.yml                   # MkDocs configuration
└── requirements.txt             # Python dependencies
```

## 🚀 How to Use

### Update Course Dates
Edit `config/course.yaml` and change dates under `course.sessions`. All pages will automatically reflect the changes.

```yaml
sessions:
  - number: 1
    date: "2026-08-05"    # Change this date
    day: "Martes"
    time: "09:00 - 12:00"
    title: "Introducción a la IA..."
```

### Enable New Content
When ready to release a session, replace the `!!! warning` placeholder in the corresponding `.md` file with actual content.

Before:
```markdown
!!! warning "🔒 Próxima Sesión"
    **Disponible desde:** Jueves, 7 de Agosto de 2026
```

After: Add full content

### Build Locally
```bash
pip install -r requirements.txt
mkdocs serve   # Preview at http://localhost:8000
mkdocs build   # Build static site in site/
```

### Deploy to GitHub Pages
Automatic via GitHub Actions:
- Push to `main` branch
- Workflow triggers automatically
- Site deployed to `gh-pages` branch
- Live at: `https://ia-estructuras-diplomado.github.io/curso-ia-web/`

## 📈 Curriculum Overview

| Session | Date | Type | Topic | Evaluation |
|---------|------|------|-------|-----------|
| 1 | Aug 5 | Theory + Practice | Intro to AI in Civil Eng | - |
| 2 | Aug 7 | Theory + Practice | Big Data & Real Cases | - |
| 3 | Aug 12 | Theory + Practice | ML Models | - |
| 4 | Aug 14 | Evaluation | Group Work 1 | T1 (30%) |
| 5 | Aug 19 | Theory + Practice | Signals & Clustering | - |
| 6 | Aug 21 | Theory + Practice | Future & Trends | - |
| 7 | Aug 26 | Evaluation | Group Work 2 | T2 (30%) |
| 8 | Aug 28 | Evaluation | Group Work 3 | T3 (40%) |

## 🎓 Professional Focus

This course emphasizes **application, not learning to program**:

✅ **What Students Do:**
- Work with pre-configured Jupyter Notebooks
- Modify hyperparameters and datasets
- Analyze results and interpret outputs
- Make decisions based on data
- Solve real structural engineering problems

❌ **What They Don't Do:**
- Learn Python from scratch
- Build algorithms from zero
- Debug complex code

## 📋 Next Steps for Maintenance

1. **Fill in future sessions** as they approach (Sesiones 2-6)
2. **Add Lab 2 & 3** content with actual notebook links
3. **Develop full requirements** for Trabajos 2 & 3
4. **Add sample datasets** to repository (if needed)
5. **Create Jupyter Notebooks** to link from labs
6. **Record session videos** and link in future sections

## ✅ Testing Performed

- ✓ MkDocs build successful
- ✓ All pages render correctly
- ✓ Navigation menu complete
- ✓ Spanish language support enabled
- ✓ Responsive design tested
- ✓ Site deployed successfully
- ✓ File structure organized

## 🔗 Key Links

- **Home:** `/` - Course overview
- **Schedule:** `/curso/cronograma.md` - All 8 sessions
- **Grading:** `/curso/calificacion.md` - Evaluation details
- **Labs:** `/labs/` - Practical exercises
- **Group Work:** `/trabajos/` - Project guidelines
- **FAQ:** `/faq.md` - Common questions

---

**Created:** May 27, 2026  
**Last Updated:** May 27, 2026  
**Status:** Ready for production
