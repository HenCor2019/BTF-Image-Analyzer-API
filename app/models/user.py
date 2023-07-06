from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    doctors = relationship("Doctor", back_populates="user")

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String)
    carne = Column(String)
    country = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="doctors")

    diagnostics = relationship("Diagnostic", back_populates="doctor")
    patients = relationship("Patient", back_populates="doctor")

    created_date = Column(Date)

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String)
    gender = Column(String)
    birthday = Column(Date)
    email = Column(String, unique=True, index=True)
    country = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("Doctor", back_populates="patients")

    diagnostics = relationship("Diagnostic", back_populates="patient")

class Diagnostic(Base):
    __tablename__ = "diagnostics"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    positive_probability = Column(Float)
    negative_probability = Column(Float)
    result_by_doctor = Column(Integer)
    created_at = Column(Date)
    remark = Column(String)

    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("Doctor", back_populates="diagnostics")

    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship("Patient", back_populates="diagnostics")
