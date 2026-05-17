-- 1. Tabla de Escaneos (La cabecera de cada auditoría)
CREATE TABLE scans (
    id SERIAL PRIMARY KEY,
    target VARCHAR(255) NOT NULL,       -- IP o Rango (ej. 192.168.1.1)
    scan_type VARCHAR(50),              -- Tipo (SYN, Connect, etc.)
    timing_level VARCHAR(5) DEFAULT 'T4',
    status VARCHAR(20) DEFAULT 'pending', -- pending, running, completed, failed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    raw_results JSONB                   -- Guardamos el JSON completo de Nmap por si acaso
);

-- 2. Tabla de Hosts Encontrados (Relacionada con un escaneo)
CREATE TABLE discovered_hosts (
    id SERIAL PRIMARY KEY,
    scan_id INTEGER REFERENCES scans(id) ON DELETE CASCADE,
    ip_address VARCHAR(45) NOT NULL,
    hostname VARCHAR(255),
    os_name VARCHAR(100),               -- Resultado del flag -O
    state VARCHAR(20)                   -- up / down
);

-- 3. Tabla de Puertos y Servicios (Detalle máximo)
CREATE TABLE discovered_ports (
    id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES discovered_hosts(id) ON DELETE CASCADE,
    port_number INTEGER NOT NULL,
    protocol VARCHAR(10),               -- TCP / UDP
    service_name VARCHAR(100),          -- ej. ssh, http
    service_version VARCHAR(255),       -- Resultado del flag -sV (ej. Apache 2.4.41)
    state VARCHAR(20)                   -- open / closed / filtered
);