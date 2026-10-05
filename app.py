import requests
import streamlit as st
from utils.document_utils import format_docx, format_pdf, sanitize_text

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide",
)

st.title("⚖️ LegalEase")
st.caption("AI-Powered Legal Document Generator")
st.warning(
    "LegalEase creates AI-generated drafts for educational/general information. "
    "It is not a substitute for advice from a qualified legal professional."
)

BACKEND_URL = st.sidebar.text_input(
    "FastAPI Backend URL",
    "http://127.0.0.1:8000",
)

st.subheader("Document Details")

document_type = st.selectbox(
    "Document Type",
    [
        "Employment Contract",
        "Non-Disclosure Agreement (NDA)",
        "Lease Agreement",
        "Freelance Work Contract",
        "Service Agreement",
        "General Agreement",
    ],
)

parties = st.text_area(
    "Parties Involved",
    placeholder="Example: Jane Doe (Service Provider), TechNova Inc. (Client)",
)

terms = st.text_area(
    "Terms & Conditions",
    placeholder=(
        "Separate each term with a semicolon;\n"
        "Payment within 30 days;\n"
        "Confidentiality must be maintained;\n"
        "Either party may terminate with 15 days notice"
    ),
)

effective_date = st.text_input(
    "Effective Date",
    placeholder="Example: October 5, 2026",
)

if st.button("✨ Generate Document", type="primary"):
    if not parties.strip() or not terms.strip() or not effective_date.strip():
        st.error("Please fill in all required fields.")
    else:
        with st.spinner("Generating your document..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL.rstrip('/')}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "effective_date": effective_date,
                    },
                    timeout=120,
                )
                response.raise_for_status()
                st.session_state["document"] = response.json()["document"]
                st.session_state["doc_type"] = document_type
            except requests.RequestException as exc:
                st.error(f"Could not connect to the FastAPI backend: {exc}")

if "document" in st.session_state:
    st.divider()
    st.subheader("📄 Generated Document")
    edited = st.text_area(
        "Preview / Edit",
        value=st.session_state["document"],
        height=550,
    )
    st.session_state["document"] = edited

    text_bytes = sanitize_text(edited).encode("utf-8")
    docx_bytes = format_docx(edited, st.session_state["doc_type"])
    pdf_bytes = format_pdf(edited, st.session_state["doc_type"])

    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button(
            "⬇️ Download TXT",
            text_bytes,
            file_name="legalease_document.txt",
            mime="text/plain",
        )
    with c2:
        st.download_button(
            "⬇️ Download DOCX",
            docx_bytes,
            file_name="legalease_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    with c3:
        st.download_button(
            "⬇️ Download PDF",
            pdf_bytes,
            file_name="legalease_document.pdf",
            mime="application/pdf",
        )
