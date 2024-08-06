"""Reflex custom component Giscus."""
import reflex as rx


class Giscus(rx.Component):
    """Giscus component."""
    library = "@giscus/react"
    tag = 'Giscus'
    is_default = True
    _id: rx.Var[str] = 'comments'
    repo: rx.Var[str] = 'itsmeadarsh2008/reflex-giscus'
    repo_id: rx.Var[str] = 'R_kgDOMf2dhw'
    category: rx.Var[str] = 'Announcements'
    category_id: rx.Var[str] = 'DIC_kwDOMf2dh84ChbWN'
    mapping: rx.Var[str] = 'specific'
    term: rx.Var[str] = 'Welcome to Reflex Giscus!'
    reactions_enabled: rx.Var[str] = '1'
    emit_metadata: rx.Var[str] = '0'
    input_position: rx.Var[str] = 'top'
    theme: rx.Var[str] = 'light'
    lang: rx.Var[str] = 'en'
    loading: rx.Var[str] = 'lazy'
    
giscus = Giscus.create
