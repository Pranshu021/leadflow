from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from database import Base

from sqlalchemy import (
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    func,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class LeadPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class LeadStatus(str, Enum):
    NEW = "New"
    CONTACTED = "Contacted"
    QUALIFIED = "Qualified"
    MEETING_SCHEDULED = "Meeting Scheduled"
    PROPOSAL_SENT = "Proposal Sent"
    NEGOTIATION = "Negotiation"
    WON = "Won"
    LOST = "Lost"
    ON_HOLD = "On Hold"


class MeetingType(str, Enum):
    CALL = "Call"
    EMAIL = "Email"
    LINKEDIN = "LinkedIn"
    WHATSAPP = "WhatsApp"
    MEETING = "Meeting"
    DEMO = "Demo"
    FOLLOW_UP = "Follow Up"
    OTHER = "Other"


class ActivityStatus(str, Enum):
    COMPLETED = "Completed"
    PENDING = "Pending"
    CANCELLED = "Cancelled"
    RESCHEDULED = "Rescheduled"


class Lead(Base):
    __tablename__ = "leads"

    __table_args__ = (
        UniqueConstraint("company_name", "website", name="uq_company_website"),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    industry: Mapped[Optional[str]] = mapped_column(
        String(120)
    )

    website: Mapped[Optional[str]] = mapped_column(
        String(255),
        index=True,
    )

    linkedin: Mapped[Optional[str]] = mapped_column(
        String(255),
        unique=True,
    )

    country: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    city: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    company_size: Mapped[Optional[str]] = mapped_column(
        String(50)
    )

    lead_source: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    primary_service: Mapped[Optional[str]] = mapped_column(
        String(150)
    )

    priority: Mapped[LeadPriority] = mapped_column(
        SQLEnum(LeadPriority),
        default=LeadPriority.MEDIUM,
        nullable=False,
        index=True,
    )

    current_status: Mapped[LeadStatus] = mapped_column(
        SQLEnum(LeadStatus),
        default=LeadStatus.NEW,
        nullable=False,
        index=True,
    )

    notes: Mapped[Optional[str]] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # One Lead -> Many Activities
    activities: Mapped[List["Activity"]] = relationship(
        back_populates="lead",
        cascade="all, delete-orphan",
        order_by="Activity.created_at.desc()",
    )


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    lead_id: Mapped[int] = mapped_column(
        ForeignKey("leads.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    meeting_type: Mapped[MeetingType] = mapped_column(
        SQLEnum(MeetingType),
        nullable=False,
    )

    contact_person: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    designation: Mapped[Optional[str]] = mapped_column(
        String(150)
    )

    email: Mapped[Optional[str]] = mapped_column(
        String(255)
    )

    phone: Mapped[Optional[str]] = mapped_column(
        String(30)
    )

    contact_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    follow_up_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        index=True,
    )

    status: Mapped[ActivityStatus] = mapped_column(
        SQLEnum(ActivityStatus),
        default=ActivityStatus.COMPLETED,
        nullable=False,
        index=True,
    )

    quotation_amount: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(12, 2)
    )

    currency: Mapped[Optional[str]] = mapped_column(
        String(10)
    )

    proposal_summary: Mapped[Optional[str]] = mapped_column(
        Text
    )

    meeting_notes: Mapped[Optional[str]] = mapped_column(
        Text
    )

    follow_up_action: Mapped[Optional[str]] = mapped_column(
        Text
    )

    created_by: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    lead: Mapped["Lead"] = relationship(
        back_populates="activities"
    )