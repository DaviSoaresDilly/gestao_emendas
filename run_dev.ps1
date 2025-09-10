# run_dev.ps1
Write-Host "=============================="
Write-Host " Subindo containers do projeto "
Write-Host "=============================="

# Sobe os containers com build
docker compose up --build -d

Write-Host ""
Write-Host "✅ Containers rodando!"
Write-Host "Frontend: http://localhost:3000"
Write-Host "Backend: http://localhost:8000"
Write-Host "PostgreSQL: porta 5432"
Write-Host "MinIO (opcional): http://localhost:9000"
Write-Host "=============================="
