from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base, validates
from datetime import datetime

Base = declarative_base()

class Scan(Base):
    __tablename__ = 'scans'
    id = Column(Integer, primary_key=True)
    target = Column(String(255), nullable=False)
    scan_type = Column(String(50))
    status = Column(String(20), default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relación: un escaneo tiene muchos hosts
    hosts = relationship('DiscoveredHost', backref='scan', lazy=True, cascade="all, delete-orphan")

class DiscoveredHost(Base):
    __tablename__ = 'discovered_hosts'
    id = Column(Integer, primary_key=True)
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    ip_address = Column(String(45), nullable=False)
    os_name = Column(String(100))
    # Relación: un host tiene muchos puertos
    ports = relationship('DiscoveredPort', backref='host', lazy=True, cascade="all, delete-orphan")

class DiscoveredPort(Base):
    __tablename__ = 'discovered_ports'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('discovered_hosts.id'), nullable=False)
    port_number = Column(Integer, nullable=False)
    service_name = Column(String(100))
    state = Column(String(20)) # open, closed...