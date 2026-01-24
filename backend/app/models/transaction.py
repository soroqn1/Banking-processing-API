from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Numeric, String, func
from app.core.database import Base
from datetime import datetime
import decimal

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=True)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    transaction_type: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
