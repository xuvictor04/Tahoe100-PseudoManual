# Tests


`tahoe test` or `python3 tests/run_smoke.py` (Windows: `C:\tahoe\.venv\Scripts\python.exe tests\run_smoke.py --workdir C:\tahoe\smoke`)
generates a small synthetic Tahoe-100M download with planted effects (well-position artifacts, a plate-2 DMSO
offset, MTAP-null lines, TP53-dependent p53 activation, NRF2 / ISR / iron / GSDME effects, toxic and shutdown drugs,
a failed well) and checks that every script recovers them. No API key is used. Details in `tests/README.md`.
Method v3 adds a planted case for each fix: a noisy plate, an unreliable mixed-dose `plate13`, a strong and an inert
drug sharing one position, a drug at the same position on every plate (not correctable), a composition-shift drug,
a plate row that loses cells (technical, not toxic), and a panel run without an earlier MTAP/Gankyrin output. The
smoke test also checks that the atlas and the panel agree on MTAP and PSMD10, the version stamps, and that
`tahoe status` calls older outputs outdated.
