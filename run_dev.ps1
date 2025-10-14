# run_dev.ps1
param(
    [string]$mode = "dev"  # dev ou prod
)

Write-Host "=============================="
Write-Host " Subindo containers do projeto "
Write-Host "=============================="
Write-Host "Modo selecionado: $mode"
Write-Host ""

# Verifica se o Docker está a rodar
try {
    docker info | Out-Null
} catch {
    Write-Host "❌ Docker não está a rodar. Inicie o Docker Desktop e tente novamente."
    exit 1
}

if ($mode -eq "prod") {
    Write-Host "🚀 Subindo containers em PRODUÇÃO..."
    # Para produção, usamos apenas o ficheiro principal, ignorando o override.
    docker compose -f docker-compose.yml up --build -d
} else {
    Write-Host "👨‍💻 Subindo containers em DESENVOLVIMENTO..."
    # Para desenvolvimento, o Docker Compose usa docker-compose.yml + docker-compose.override.yml por padrão.
    docker compose up --build -d
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro ao subir os containers."
    exit 1
}

# --- ESTA É A PARTE FINAL DO SCRIPT ---
Write-Host ""
Write-Host "✅ Containers a rodar!"
Write-Host "------------------------------"
# Nota: A porta do frontend pode ser 3001 se a tiver alterado para evitar conflitos.
Write-Host "Frontend:   http://localhost:3001" 
Write-Host "Backend:    http://localhost:8000"
Write-Host "Documentação API: http://localhost:8000/docs"
Write-Host "PostgreSQL: porta 5432"
Write-Host "MinIO API:  http://localhost:9000"
Write-Host "MinIO UI:   http://localhost:9001"
Write-Host "------------------------------"

# Mostra o status dos containers para confirmação
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

Write-Host "=============================="