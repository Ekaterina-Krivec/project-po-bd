import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db_setup import Base

__all__ = ['Painting', 'Exhibition', 'Auction', 'PotentialBuyer']


class Painting(Base):
    __tablename__ = 'paintings'

    id_painting = sa.Column('idPainting', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String)
    id_artist = sa.Column('idArtist', sa.Integer)
    price = sa.Column('price', sa.Float)
    id_owner = sa.Column('idOwner', sa.Integer)
    characteristics_code = sa.Column('Characteristics_code', sa.Integer)

    def __repr__(self):
        return f'{self.name}'


class Exhibition(Base):
    __tablename__ = 'exhibitions'

    id_exhibition = sa.Column('idExhibition', sa.Integer, primary_key=True)
    id_painting = sa.Column('idPainting', sa.Integer, sa.ForeignKey('paintings.idPainting'))
    name = sa.Column('name', sa.String)
    ticket_price = sa.Column('ticket_price', sa.Float)
    date_start = sa.Column('date_start', sa.Date)
    date_end = sa.Column('date_end', sa.Date)
    category = sa.Column('category', sa.Text)
    painting = relationship('Painting')


class Auction(Base):
    __tablename__ = 'auctions'

    id_auction = sa.Column('idAuction', sa.Integer, primary_key=True)
    id_painting = sa.Column('idPainting', sa.Integer, sa.ForeignKey('paintings.idPainting'))
    name = sa.Column('name', sa.String)
    datetime = sa.Column('datetime', sa.DateTime)
    tid = sa.Column('tid', sa.Float)
    painting = relationship('Painting')


class PotentialBuyer(Base):
    __tablename__ = 'potential_buyers'

    id_buyer = sa.Column('idBuyer', sa.Integer, primary_key=True)
    id_painting = sa.Column('idPainting', sa.Integer, sa.ForeignKey('paintings.idPainting'))
    full_name = sa.Column('full_name', sa.String)
    contacts = sa.Column('contacts', sa.String)
    address = sa.Column('address', sa.String)
    painting = relationship('Painting')
