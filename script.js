const projectsFiles = ['CMU projects/projects.json', 'projects.json'];
const codeBaseFolder = 'CMU projects/';

const themeToggle = document.getElementById('themeToggle');

// Embed modal elements
const embedModal = document.getElementById('embedModal');
const embedBackdrop = document.getElementById('embedBackdrop');
const embedClose = document.getElementById('embedClose');
const embedIframe = document.getElementById('embedIframe');

// Code modal elements
const codeModal = document.getElementById('codeModal');
const codeBackdrop = document.getElementById('codeBackdrop');
const codeClose = document.getElementById('codeClose');
const codeTitle = document.getElementById('codeTitle');
const codeContent = document.getElementById('codeContent');

function getTheme() {
  return localStorage.getItem('cmu_theme') || 'light';
}

function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('cmu_theme', theme);
  themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
}

// ── Embed modal ──

function openEmbedModal(src, title) {
  if (!src) {
    alert('No embed URL for this project.');
    return;
  }
  embedIframe.title = `${title || 'CMU Academy'} embed`;
  embedIframe.src = src;
  embedModal.classList.add('open');
  embedModal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  embedClose.focus();
}

function closeEmbedModal() {
  embedModal.classList.remove('open');
  embedModal.setAttribute('aria-hidden', 'true');
  embedIframe.src = '';
  document.body.style.overflow = '';
}

embedBackdrop.addEventListener('click', closeEmbedModal);
embedClose.addEventListener('click', closeEmbedModal);

// ── Code modal ──

async function openCodeModal(project) {
  if (!project.codeFile) {
    alert('No code file was provided for this project.');
    return;
  }
  codeTitle.textContent = `${project.title} code`;
  codeContent.textContent = 'Loading code…';
  codeModal.classList.add('open');
  codeModal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  codeClose.focus();

  try {
    const codeCandidates = project.codeFile.includes('/')
      ? [project.codeFile]
      : [`${codeBaseFolder}${project.codeFile}`, project.codeFile];

    let sourceText = null;
    for (const candidate of codeCandidates) {
      const response = await fetch(candidate);
      if (response.ok) {
        sourceText = await response.text();
        break;
      }
    }

    if (sourceText === null) {
      throw new Error('Code file was not found in configured locations.');
    }

    codeContent.textContent = sourceText;
  } catch (error) {
    codeContent.textContent = `Unable to load ${project.codeFile}.\n\n${error.message}`;
    console.error(error);
  }
}

function closeCodeModal() {
  codeModal.classList.remove('open');
  codeModal.setAttribute('aria-hidden', 'true');
  codeContent.textContent = '';
  document.body.style.overflow = '';
}

codeBackdrop.addEventListener('click', closeCodeModal);
codeClose.addEventListener('click', closeCodeModal);

// ── Escape key closes whichever is open ──

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeEmbedModal();
    closeCodeModal();
  }
});

// ── Grid ──

function renderGrid(projects) {
  const grid = document.getElementById('projectsGrid');
  grid.innerHTML = '';

  projects.forEach((project) => {
    const card = document.createElement('div');
    card.className = 'project-card';
    card.innerHTML = `
      <div class="project-icon">${project.icon || '🔗'}</div>
      <h3 class="project-title">${project.title}</h3>
      <p class="project-desc">${project.description || ''}</p>
      <div class="project-tags">${(project.tags || []).slice(0, 3).map((tag) => `<span class="tag">${tag}</span>`).join('')}</div>
    `;

    const controls = document.createElement('div');
    controls.className = 'card-controls';

    const startBtn = document.createElement('button');
    startBtn.className = 'launch-btn';
    startBtn.textContent = 'Start';
    startBtn.addEventListener('click', () => openEmbedModal(project.embedUrl || project.url, project.title));

    const openLink = document.createElement('a');
    openLink.className = 'open-link';
    openLink.textContent = 'Open';
    openLink.href = project.url || '#';
    openLink.target = '_blank';

    const codeBtn = document.createElement('button');
    codeBtn.className = 'code-btn';
    codeBtn.textContent = 'View Code';
    codeBtn.disabled = !project.codeFile;
    codeBtn.addEventListener('click', () => openCodeModal(project));

    controls.appendChild(startBtn);
    controls.appendChild(openLink);
    controls.appendChild(codeBtn);
    card.appendChild(controls);
    grid.appendChild(card);
  });
}

async function loadProjects() {
  try {
    let projects = null;

    for (const filePath of projectsFiles) {
      const response = await fetch(filePath);
      if (!response.ok) {
        continue;
      }
      projects = await response.json();
      break;
    }

    if (!projects) {
      throw new Error('No projects file found.');
    }

    renderGrid(projects);
  } catch (error) {
    document.getElementById('projectsGrid').innerHTML = '<p class="error">Failed to load projects.json</p>';
    console.error(error);
  }
}

themeToggle.addEventListener('click', () => {
  setTheme(getTheme() === 'dark' ? 'light' : 'dark');
});

setTheme(getTheme());
loadProjects();