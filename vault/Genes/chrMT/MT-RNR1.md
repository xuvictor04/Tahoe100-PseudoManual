---
symbol: "MT-RNR1"
type: "gene"
col: 13064
ensembl_id: "ENSG00000211459"
name: "mitochondrially encoded 12S rRNA"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 28130.34
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-RNR1

*mitochondrially encoded 12S rRNA* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.73× (z +10.9, q 1e-24, up in 49 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Voriconazole (drug)]] 0.05 µM: 1.85× (z +3.5, q 0.042, up in 48 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 14 lines (MIA PaCa-2 1.81×, NCI-H1792 1.79×, C-33 A 1.85×, SK-MEL-2 1.81×, …; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 6.85×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.100× (z -13.4, q 2e-38, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 0.5 µM: 0.325× (z -6.6, q 1e-08, down in 48 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13064.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 14 lines (MIA PaCa-2 1.81×, NCI-H1792 1.79×, C-33 A 1.85×, SK-MEL-2 1.81×, …; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 6.85×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.73×** | +10.9 | 1e-24 | 49/50 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +7.5 | 1e-11 | 44/44 (AN3 CA, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.54×** | +7.3 | 4e-11 | 49/49 (AN3 CA, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +5.2 | 2e-05 | 45/45 (AN3 CA, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Voriconazole (drug)]] 0.05 µM |  | **1.85×** | +3.5 | 0.042 | 48/48 (HOP62, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.88×** | +3.5 | 0.042 | 47/47 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | 1.80× | +3.2 | 0.12 | 48/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 1.72× | +3.1 | 0.12 | 49/49 (NCI-H2347, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 1.47× | +3.1 | 0.12 | 48/48 (NCI-H460, Panc 03.27, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.100×** | -13.4 | 2e-38 | 48/48 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.325×** | -6.6 | 1e-08 | 48/48 (NCI-H460, LoVo, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.398×** | -5.4 | 1e-05 | 48/48 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.465×** | -4.5 | 9e-04 | 48/48 (HOP62, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.595×** | -4.3 | 0.001 | 49/49 (NCI-H2122, HOP62, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.356×** | -4.3 | 0.001 | 49/49 (KATO III, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.618×** | -4.0 | 0.005 | 41/48 (Panc 03.27, A-427, …) | rises with dose |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.513×** | -3.9 | 0.006 | 48/49 (HOP62, NCI-H1792, …) | rises with dose | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.570×** | -3.3 | 0.057 | 48/48 (SK-MEL-2, SHP-77, …) | rises with dose | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.680×** | -3.2 | 0.069 | 48/49 (NCI-H460, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 14,971 | 3 (3 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +11.2) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -11.8) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 25,680 | 3 (3 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +11.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.116× (z -13.6) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 27,119 | 3 (3 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +11.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0909× (z -15.1) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 15,442 | 3 (3 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.81× (z +12.0) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -12.2) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 26,608 | 3 (3 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +11.2) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0828× (z -15.1) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 23,471 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +11.0) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -12.2) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 22,451 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0832× (z -14.4) ⚠ transcription drop |
| [[A498 (line)]] | wt | 22,958 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.142× (z -11.3) ⚠ transcription drop |
| [[A549 (line)]] | wt | 31,755 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +10.6) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -12.1) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 29,880 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +9.8) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0868× (z -12.9) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 36,328 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +10.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -12.6) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 26,502 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.85× (z +11.8) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0796× (z -14.2) ⚠ transcription drop |
| [[C32 (line)]] | wt | 23,577 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +11.2) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -12.6) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 24,545 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +10.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0957× (z -13.0) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 29,565 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +10.2) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0978× (z -12.9) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 39,810 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +10.5) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0748× (z -15.4) ⚠ transcription drop |
| [[H4 (line)]] | wt | 24,772 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.82× (z +11.5) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0951× (z -13.4) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 20,391 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.76× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -12.3) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 31,670 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.78× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.110× (z -12.2) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 35,963 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +10.3) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.114× (z -12.5) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 51,893 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +9.8) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0676× (z -15.7) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 23,662 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +10.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.141× (z -11.1) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 26,289 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +10.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -11.3) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 27,190 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +10.0) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.119× (z -11.9) ⚠ transcription drop |
| [[J82 (line)]] | alt | 25,707 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +10.6) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0953× (z -13.2) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 29,521 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +10.0) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0969× (z -12.8) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 27,519 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.65× (z +9.5) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -12.9) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 33,288 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +10.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0965× (z -13.0) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 26,071 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.79× (z +11.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -12.7) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 22,965 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.79× (z +11.4) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.142× (z -11.3) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 29,324 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.91× (z +11.6) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0964× (z -12.0) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 33,185 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +9.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0848× (z -13.8) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 25,896 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -13.2) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 34,340 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +9.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0891× (z -13.0) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 23,720 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +10.7) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0963× (z -13.8) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 29,568 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +10.8) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0867× (z -14.4) ⚠ transcription drop |
| [[RKO (line)]] | wt | 26,351 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.75× (z +10.8) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -11.5) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 21,665 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +11.2) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -12.1) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 38,815 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.76× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0871× (z -13.8) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39,475 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.81× (z +11.7) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0552× (z -16.6) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 46,291 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +11.0) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0913× (z -13.3) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 35,170 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +10.3) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -11.7) ⚠ transcription drop |
| [[SW 1088 (line)]] | alt | 26,765 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +9.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0953× (z -13.0) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 17,918 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +10.9) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -13.0) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 30,527 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +11.1) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0998× (z -13.8) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 31,788 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +10.3) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.0907× (z -13.6) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 23,956 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +10.6) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -12.3) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 19,270 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.141× (z -9.2) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 28,648 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31,584 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded 12S rRNA |
| Locus type | RNA, ribosomal (non-coding RNA) |
| Location | mitochondria — chrMT:648-1,601 (+) |
| Ensembl biotype | Mt_rRNA |
| Also known as | 12S, MOTS-c; previously MTRNR1 |
| Gene groups (HGNC) | Mitochondrially encoded ribosomal RNAs |
| Reactome | 14 pathways, smallest: rRNA modification in the mitochondrion; FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A0C5B5G6](https://www.uniprot.org/uniprotkb/A0A0C5B5G6) (Mitochondrial-derived peptide MOTS-c):

> Regulates insulin sensitivity and metabolic homeostasis. Inhibits the folate cycle, thereby reducing de novo purine biosynthesis which leads to the accumulation of the de novo purine synthesis intermediate 5-aminoimidazole-4-carboxamide (AICAR) and the activation of the metabolic regulator 5'-AMP-activated protein kinase (AMPK). Protects against age-dependent and diet-induced insulin resistance as well as diet-induced obesity. In response to metabolic stress, translocates to the nucleus where …

**Summary**, from NCBI Gene [4549](https://www.ncbi.nlm.nih.gov/gene/4549):

> Enables DNA binding activity and DNA-binding transcription factor binding activity. Involved in several processes, including osteoblast proliferation; regulation of phosphorus metabolic process; and skeletal muscle tissue growth. Located in mitochondrion; nucleus; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7470) · Entrez [4549](https://www.ncbi.nlm.nih.gov/gene/4549) · UniProt [A0A0C5B5G6](https://www.uniprot.org/uniprotkb/A0A0C5B5G6) · Ensembl [ENSG00000211459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211459)

## Data

Gene col 13064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13064); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13064, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13064]; `tensor/DDL_lfc|DDL_z.npy` [13064]; `embed/gene_vectors.npy` [13064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13064 or target_col == 13064). Every well: [[MT-RNR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-RNR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
