# run_dev.ps1
param(
    [string]$mode = "dev"  # dev ou prod
)

Write-Host "=============================="
Write-Host " Subindo containers do projeto "
Write-Host "=============================="
Write-Host "Modo selecionado: $mode"
Write-Host ""

# Verifica se o Docker está rodando
try {
    docker info | Out-Null
} catch {
    Write-Host "❌ Docker não está rodando. Inicie o Docker Desktop e tente novamente."
    exit 1
}

if ($mode -eq "prod") {
    Write-Host "🚀 Subindo containers em PRODUÇÃO..."
    docker compose -f docker-compose.yml up --build -d
} else {
    Write-Host "👨‍💻 Subindo containers em DESENVOLVIMENTO..."
    docker compose up --build -d
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro ao subir os containers."
    exit 1
}

Write-Host ""
Write-Host "✅ Containers rodando!"
Write-Host "------------------------------"
Write-Host "Frontend:   http://localhost:3000"
Write-Host "Backend:    http://localhost:8000"
Write-Host "PostgreSQL: porta 5432"
Write-Host "MinIO API:  http://localhost:9000"
Write-Host "MinIO UI:   http://localhost:9001"
Write-Host "------------------------------"

# Mostra status dos containers
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

Write-Host "=============================="
