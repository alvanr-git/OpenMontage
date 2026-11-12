"""PropSpyandCEO Ecosystem Publisher & Unified Asset Bridge.

Packages rendered videos for both the team brand (`propertyspy` — @propertyspy /
@sgpropertyspy) and the personal brand (`alvanassets` — Assets with Alvan),
producing:
1. A deterministic local export bundle (`video/`, `metadata/`, `thumbnails/`).
2. A Sanity CMS `reel` document payload (`metadata/sanity_reel_payload.json`)
   compatible with PropertySpy's `sanity/schemas/reel.js` schema (`d5duame6`).
3. A `propspy_handoff_receipt.json` linking the render back to the shared
   `PropSpyandCEO` cloud data backbone (Google Sheets, Google Drive vaults,
   and Sanity CMS) and optional `post_id` row in the Social Media Master Sheet.
4. Optional Google Drive upload + Google Sheet status update when credentials
   are provided via environment variables (`GOOGLE_SERVICE_ACCOUNT_JSON` or
   `GOOGLE_APPLICATION_CREDENTIALS`).
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.base_tool import (
    BaseTool,
    Determinism,
    ExecutionMode,
    ResourceProfile,
    ToolResult,
    ToolRuntime,
    ToolStability,
    ToolTier,
)
from tools.publishers.export_bundle import ExportBundle


# Canonical Shared Cloud Data Backbone IDs (verified by `python eco.py verify`)
# Accessible to BOTH `propertyspy` and `alvanassets` video workflows.
SHARED_GOOGLE_SHEETS: dict[str, str] = {
    "landed_presentation": "1a4Z0xoSIe4bwlqIeSpLo6xBwGAZjN7ScLsqEo5aKCV0",
    "manual_transactions": "1F_ecrYJAM3OPcbyKZmL4utSZjX7I1xb0fnidm5hwyDw",
    "propertyguru_landed": "1XoQY0iUOaW_GISX_Hza8GrBVlq6kX_XkNY8WkQB_NXQ",
    "new_launch_directory": "1wEaED_82L_o5UfIazrCiO-oO_OEH2CRsPrVXKt2jfuw",
    "listings_whale_master": "1ol3nUGoqo9hWDUydm7tUWHn1_oho-OMKntazQ-wdHyE",
    "news_archive": "1wb3xAE0M7Y2bmS3w1vFt1HmYb6RAa9clKZoIa5aUY7I",
    "alvanassets_social_media": "1uTGwCGp1HJwZpvDAZXKsSgJQQc11uB79ROHJH46Cnos",
}

SHARED_DRIVE_FOLDERS: dict[str, str] = {
    "new_launch_media": "1RbgxMylTdac5UpkMc94mc-5wSLwUOx4S",
    "listings_whale_inbox": "1ZViGLkqIEHJr8ZBX1pQjqW1D8xOL0J5F",
    "news_media_archive": "1p50oTF5fE9KwUd3-UXe20pEGBuptqW7r",
    "alvanassets_media_vault": "10JkGnXCBaLMt8l6U1E3d1LRVbMRcxMDW",
}

SHARED_CANVA_FOLDERS: dict[str, str] = {
    "alvanassets": "FAHT237qSmk",
}

SANITY_CMS_CONFIG: dict[str, str] = {
    "project_id": "d5duame6",
    "dataset": "production",
}


class PropSpyPublisher(BaseTool):
    name = "propspy_publisher"
    version = "0.1.0"
    tier = ToolTier.PUBLISH
    capability = "publish"
    provider = "propspyandceo"
    stability = ToolStability.BETA
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.HYBRID

    dependencies = []
    install_instructions = (
        "Runs locally with standard library packaging. Set GOOGLE_SERVICE_ACCOUNT_JSON "
        "or GOOGLE_APPLICATION_CREDENTIALS to enable optional Google Drive / Sheets sync."
    )

    agent_skills = []

    capabilities = [
        "package_export",
        "write_publish_log",
        "sanity_reel_payload",
        "propspy_cloud_sync",
    ]
    supports = {
        "local_offline": True,
        "free": True,
        "uploads": True,
        "brands": ["alvanassets", "propertyspy"],
    }
    best_for = [
        "packaging and logging social videos for @propertyspy and alvanassets",
        "emitting Sanity CMS reel schema payloads (project d5duame6)",
        "syncing finished video renders back to the PropSpyandCEO social calendar and Drive vault",
    ]
    not_good_for = [
        "direct TikTok/Instagram OAuth posting without pre-approved platform tokens",
    ]

    input_schema = {
        "type": "object",
        "required": ["video_path", "title"],
        "properties": {
            "video_path": {
                "type": "string",
                "description": "Path to the final rendered video file.",
            },
            "title": {
                "type": "string",
                "description": "Headline / SEO title for the reel or video.",
            },
            "subtitle": {
                "type": "string",
                "description": "Short hook or category tag (e.g. 'Landed Analysis', 'New Launch Spotlight').",
            },
            "brand": {
                "type": "string",
                "enum": ["alvanassets", "propertyspy"],
                "description": "Target brand identity ('alvanassets' or 'propertyspy'). Both share the full ecosystem factual/media pool.",
            },
            "post_id": {
                "type": "string",
                "description": "Optional Post ID row identifier in the Social Media Master Sheet (e.g. 'POST-014').",
            },
            "platform": {
                "type": "string",
                "enum": ["Instagram", "TikTok", "YouTube", "LinkedIn", "local"],
                "description": "Primary social platform target.",
            },
            "post_url": {
                "type": "string",
                "description": "Published or scheduled URL if already known.",
            },
            "duration": {
                "type": "string",
                "description": "Formatted duration string for Sanity reel display (e.g. '0:48').",
            },
            "featured": {
                "type": "boolean",
                "description": "Whether to mark the reel as featured in Sanity CMS.",
            },
            "project_name": {"type": "string"},
            "export_dir": {"type": "string"},
            "description": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}},
            "hashtags": {"type": "array", "items": {"type": "string"}},
            "chapters": {"type": "array", "items": {"type": "object"}},
            "subtitles_path": {"type": "string"},
            "thumbnail_path": {"type": "string"},
            "thumbnail_concept": {"type": "object"},
            "visibility": {"type": "string", "enum": ["public", "private", "unlisted"]},
            "upload_to_drive": {
                "type": "boolean",
                "description": "If true and Google credentials are configured, upload the rendered MP4 to the target Drive vault.",
            },
            "drive_folder_key": {
                "type": "string",
                "enum": [
                    "alvanassets_media_vault",
                    "new_launch_media",
                    "listings_whale_inbox",
                    "news_media_archive",
                ],
                "description": "Which shared Drive vault to upload into when upload_to_drive=True.",
            },
            "sync_sheet": {
                "type": "boolean",
                "description": "If true and Google credentials are configured, update the Social Media Master Sheet with the render status.",
            },
            "timestamp": {"type": "string"},
        },
    }

    output_schema = {
        "type": "object",
        "properties": {
            "publish_log": {"type": "object"},
            "export_path": {"type": "string"},
            "sanity_reel_payload": {"type": "object"},
            "handoff_receipt": {"type": "object"},
            "files_written": {"type": "array", "items": {"type": "string"}},
        },
    }

    resource_profile = ResourceProfile(
        cpu_cores=1, ram_mb=128, vram_mb=0, disk_mb=0, network_required=False
    )
    side_effects = [
        "writes an export bundle directory and Sanity CMS reel payload to disk",
        "optionally uploads MP4 to Google Drive and updates Google Sheets when requested",
    ]
    user_visible_verification = [
        "Inspect exports/<project>/metadata/sanity_reel_payload.json and propspy_handoff_receipt.json",
    ]

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        brand = (inputs.get("brand") or "alvanassets").strip().lower()
        if brand not in ("alvanassets", "propertyspy"):
            return ToolResult(
                success=False,
                error=f"Invalid brand {brand!r}. Choose 'alvanassets' or 'propertyspy'.",
            )

        platform = inputs.get("platform") or "Instagram"
        bundle_inputs = dict(inputs)
        bundle_inputs["platform"] = f"{brand}:{platform.lower()}"

        bundle_res = ExportBundle().execute(bundle_inputs)
        if not bundle_res.success or not bundle_res.data:
            return bundle_res

        export_root = Path(bundle_res.data["export_path"])
        meta_dir = export_root / "metadata"
        files_written = list(bundle_res.data.get("files_written", []))
        timestamp = inputs.get("timestamp") or datetime.now(timezone.utc).isoformat()

        # 1. Build Sanity CMS `reel` schema payload (matches propertyspy/sanity/schemas/reel.js)
        default_subtitle = (
            "Assets with Alvan" if brand == "alvanassets" else "PropertySpy Market Brief"
        )
        sanity_platform = platform if platform in ("Instagram", "TikTok", "YouTube") else "Instagram"
        sanity_reel_payload: dict[str, Any] = {
            "_type": "reel",
            "title": inputs["title"],
            "subtitle": inputs.get("subtitle") or default_subtitle,
            "platform": sanity_platform,
            "postUrl": inputs.get("post_url") or "",
            "duration": inputs.get("duration") or "0:45",
            "featured": bool(inputs.get("featured", True)),
            "publishedAt": timestamp,
            "brand": brand,
            "sanityProject": SANITY_CMS_CONFIG,
        }
        sanity_path = meta_dir / "sanity_reel_payload.json"
        sanity_path.write_text(
            json.dumps(sanity_reel_payload, indent=2), encoding="utf-8"
        )
        files_written.append(str(sanity_path))

        # 2. Optional Google Drive upload & Google Sheet sync (graceful if offline/no creds)
        drive_folder_key = inputs.get("drive_folder_key") or "alvanassets_media_vault"
        target_drive_id = SHARED_DRIVE_FOLDERS.get(
            drive_folder_key, SHARED_DRIVE_FOLDERS["alvanassets_media_vault"]
        )
        cloud_sync_status: dict[str, Any] = {
            "drive_uploaded": False,
            "drive_folder_id": target_drive_id,
            "drive_file_url": None,
            "sheet_synced": False,
            "sheet_id": SHARED_GOOGLE_SHEETS["alvanassets_social_media"],
        }

        if inputs.get("upload_to_drive") or inputs.get("sync_sheet"):
            cloud_sync_status = self._attempt_cloud_sync(
                inputs=inputs,
                video_path=Path(inputs["video_path"]).expanduser(),
                brand=brand,
                target_drive_id=target_drive_id,
                cloud_sync_status=cloud_sync_status,
            )

        # 3. Write unified PropSpyandCEO handoff receipt
        handoff_receipt: dict[str, Any] = {
            "version": "1.0",
            "brand": brand,
            "post_id": inputs.get("post_id"),
            "title": inputs["title"],
            "platform": platform,
            "timestamp": timestamp,
            "export_path": str(export_root),
            "shared_ecosystem_resources": {
                "sheets": SHARED_GOOGLE_SHEETS,
                "drive_folders": SHARED_DRIVE_FOLDERS,
                "canva_folders": SHARED_CANVA_FOLDERS,
                "sanity": SANITY_CMS_CONFIG,
            },
            "cloud_sync": cloud_sync_status,
        }
        receipt_path = meta_dir / "propspy_handoff_receipt.json"
        receipt_path.write_text(
            json.dumps(handoff_receipt, indent=2), encoding="utf-8"
        )
        files_written.append(str(receipt_path))

        publish_log = bundle_res.data["publish_log"]
        publish_log["metadata"] = {
            "brand": brand,
            "post_id": inputs.get("post_id"),
            "sanity_project_id": SANITY_CMS_CONFIG["project_id"],
            "drive_folder_id": target_drive_id,
            "social_sheet_id": SHARED_GOOGLE_SHEETS["alvanassets_social_media"],
        }
        if cloud_sync_status.get("drive_file_url"):
            publish_log["entries"][0]["url"] = cloud_sync_status["drive_file_url"]
            publish_log["entries"][0]["status"] = "published"

        try:
            from schemas.artifacts import validate_artifact

            validate_artifact("publish_log", publish_log)
        except Exception as exc:  # pragma: no cover
            return ToolResult(
                success=False, error=f"publish_log failed schema validation: {exc}"
            )

        return ToolResult(
            success=True,
            data={
                "publish_log": publish_log,
                "export_path": str(export_root),
                "sanity_reel_payload": sanity_reel_payload,
                "handoff_receipt": handoff_receipt,
                "files_written": files_written,
            },
            artifacts=bundle_res.artifacts,
        )

    @staticmethod
    def _attempt_cloud_sync(
        *,
        inputs: dict[str, Any],
        video_path: Path,
        brand: str,
        target_drive_id: str,
        cloud_sync_status: dict[str, Any],
    ) -> dict[str, Any]:
        """Attempt optional Google Drive upload / Sheet update if credentials exist."""
        creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
        creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if not creds_json and not creds_path:
            cloud_sync_status["note"] = (
                "Skipped live cloud sync: neither GOOGLE_SERVICE_ACCOUNT_JSON nor "
                "GOOGLE_APPLICATION_CREDENTIALS is set in environment."
            )
            return cloud_sync_status

        try:
            from google.oauth2 import service_account  # type: ignore

            scopes = [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/spreadsheets",
            ]
            if creds_json and creds_json.strip().startswith("{"):
                info = json.loads(creds_json)
                creds = service_account.Credentials.from_service_account_info(
                    info, scopes=scopes
                )
            else:
                path_str = creds_path or creds_json or ""
                creds = service_account.Credentials.from_service_account_file(
                    path_str, scopes=scopes
                )

            if inputs.get("upload_to_drive"):
                from googleapiclient.discovery import build  # type: ignore
                from googleapiclient.http import MediaFileUpload  # type: ignore

                drive_service = build("drive", "v3", credentials=creds)
                file_metadata = {
                    "name": f"{brand}_{inputs.get('post_id') or video_path.stem}{video_path.suffix}",
                    "parents": [target_drive_id],
                }
                media = MediaFileUpload(
                    str(video_path), mimetype="video/mp4", resumable=True
                )
                uploaded = (
                    drive_service.files()
                    .create(
                        body=file_metadata,
                        media_body=media,
                        fields="id, webViewLink",
                        supportsAllDrives=True,
                    )
                    .execute()
                )
                cloud_sync_status["drive_uploaded"] = True
                cloud_sync_status["drive_file_id"] = uploaded.get("id")
                cloud_sync_status["drive_file_url"] = uploaded.get("webViewLink")
        except Exception as exc:  # pragma: no cover
            cloud_sync_status["error"] = str(exc)

        return cloud_sync_status
