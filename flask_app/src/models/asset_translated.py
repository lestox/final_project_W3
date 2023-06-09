from db import db
from models.base import Base


class AssetTranslated(Base):
    """This class represents the asset translated table"""
    __tablename__ = 'asset_translated'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    music_title = db.Column(db.String(100), nullable=False)

    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False)
    last_assignment_at = db.Column(db.DateTime, nullable=False)
    resumed = db.Column(db.String(5000), nullable=False)

    # FK
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    current_assigned_user_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    composer_id = \
        db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=False)
    speaker_id = \
        db.Column(db.Integer, db.ForeignKey('speaker.id'), nullable=False)
    language_id = \
        db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    step_lifecycle_id = db.Column(
        db.Integer, db.ForeignKey('step_lifecycle.id'), nullable=False)
    status_by_domain_id = db.Column(
        db.Integer, db.ForeignKey('status_by_domain.id'), nullable=False)

    def __init__(self, title, description, music_title, resumed, asset_id,
                 current_assigned_user_id, composer_id, speaker_id,
                 language_id, step_lifecycle_id, status_by_domain_id,
                 created_at=None, updated_at=None, last_assignment_at=None):
        self.title = title
        self.description = description
        self.music_title = music_title
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_assignment_at = last_assignment_at
        self.resumed = resumed
        self.current_assigned_user_id = current_assigned_user_id
        self.composer_id = composer_id
        self.speaker_id = speaker_id
        self.language_id = language_id
        self.step_lifecycle_id = step_lifecycle_id
        self.status_by_domain_id = status_by_domain_id
        self.asset_id = asset_id
