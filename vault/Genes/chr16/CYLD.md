---
symbol: "CYLD"
type: "gene"
col: 1379
ensembl_id: "ENSG00000083799"
name: "CYLD lysine 63 deubiquitinase"
location: "16q12.1"
module: 69
arm: "+"
pooled_cpm: 86.62
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 19
n_dd_up_clean: 30
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CYLD

*CYLD lysine 63 deubiquitinase* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.6× (z +45.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.373× (z -12.9, q 2e-35, down in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.396× (z -6.3, q 6e-08, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OPTN]] (+0.72, fdr 7e-06), [[ZBTB10]] (+0.72, fdr 7e-06), [[CREBRF]] (+0.68, fdr 7e-06); moves opposite to [[POLR3H]] (-0.62, fdr 7e-06), [[POP1]] (-0.62, fdr 1e-05), [[RNGTT]] (-0.61, fdr 9e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANXA8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.6×** | +45.5 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.80×** | +23.1 | 0e+00 | 48/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.60×** | +19.3 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +18.4 | 0e+00 | 47/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.51×** | +16.5 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.66×** | +13.0 | 1e-36 | 47/49 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.00×** | +9.1 | 6e-18 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.8 | 8e-17 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +8.7 | 3e-16 | 36/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +7.7 | 7e-13 | 37/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +6.6 | 2e-09 | 39/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.2 | 1e-05 | 27/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 26/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.42×** | +4.9 | 4e-05 | 33/50 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +4.7 | 8e-05 | 29/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.5 | 2e-04 | 25/49 (C32, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.373×** | -12.9 | 2e-35 | 45/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.396×** | -6.3 | 6e-08 | 40/48 (NCI-H460, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.423×** | -5.9 | 7e-07 | 38/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.442×** | -5.6 | 3e-06 | 33/48 (SW1417, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.451×** | -5.5 | 6e-06 | 37/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.9 | 0.009 | 2/50 (SW48, SW 1088) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.583×** | -3.7 | 0.018 | 24/47 (LoVo, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.599×** | -3.5 | 0.032 | 28/48 (KATO III, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.763×** | -3.4 | 0.042 | 25/47 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.774×** | -3.4 | 0.043 | 19/48 (SW 900, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.702×** | -3.3 | 0.043 | 24/49 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.043 | 22/48 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.043 | 25/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.705×** | -3.3 | 0.045 | 22/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.843× | -3.1 | 0.062 | 22/48 (AsPC-1, KATO III, …) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.073 | 22/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.085 | 20/48 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.795×** | -3.0 | 0.085 | 18/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.796×** | -3.0 | 0.085 | 16/48 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.6 | 13 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +46.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -13.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 82.6 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +35.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -10.2) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 43.6 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +44.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.399× (z -9.3) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 68.6 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +29.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -12.9) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 55.2 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +37.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -10.7) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 54.2 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +28.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.185× (z -18.2) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 42.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +28.4) | — |
| [[HEC-1-A (line)]] | alt | 66.5 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +37.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -17.3) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 38.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +31.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -10.0) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 97.8 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +37.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -12.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 46.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +23.2) | — |
| [[C32 (line)]] | wt | 53.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +25.9) | — |
| [[KATO III (line)]] | alt | 55.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +23.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.160× (z -15.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 72.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +32.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 43.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +33.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.381× (z -8.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 64.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +22.1) | — |
| [[HT-29 (line)]] | alt | 46.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +26.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -9.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 103 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +31.1) | — |
| [[NCI-H2030 (line)]] | alt | 102 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +33.2) | — |
| [[SNU-423 (line)]] | alt | 144 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +29.1) | — |
| [[SW48 (line)]] | wt | 40.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +22.7) | — |
| [[A-172 (line)]] | wt | 268 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +28.2) | — |
| [[A498 (line)]] | wt | 208 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +35.0) | — |
| [[AsPC-1 (line)]] | alt | 54.2 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +24.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.210× (z -13.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 91.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +33.2) | — |
| [[H4 (line)]] | wt | 123 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +23.8) | — |
| [[HepG2_C3A (line)]] | wt | 70.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +25.0) | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +29.2) | — |
| [[LOX-IMVI (line)]] | wt | 65.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +24.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -9.2) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 199 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +23.7) | — |
| [[RKO (line)]] | wt | 81.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +28.0) | — |
| [[SK-MEL-2 (line)]] | alt | 90.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +26.4) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 92.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +27.7) | — |
| [[SW1417 (line)]] | alt | 91.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +25.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -13.0) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 156 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +22.3) | — |
| [[LS 180 (line)]] | wt | 41.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 88.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +26.7) | — |
| [[RPMI-7951 (line)]] | alt | 158 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +27.5) | — |
| [[COLO 205 (line)]] | alt | 60.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +23.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.307× (z -9.0) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 135 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 49.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +14.9) | — |
| [[AN3 CA (line)]] | alt | 75.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +14.7) | — |
| [[SNU-1 (line)]] | wt | 75.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +14.3) | — |
| [[SW 1088 (line)]] | alt | 253 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +10.3) | — |
| [[SW 1271 (line)]] | alt | 83.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +12.3) | — |
| [[NCI-H2122 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPTN]] | +0.72 | +0.73 / +0.73 | both halves | 7e-06 | pathway: Death Receptor Signaling; STRING 938 |
| [[ZBTB10]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[PABIR3]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[NUB1]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KMT2A]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[KDM6A]] | +0.63 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[FBXO8]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[PIK3IP1]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[NR1D2]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SMIM14]] | +0.62 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[SLC50A1]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3H]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[POP1]] | -0.62 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.61 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[EIPR1]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[NOP2]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[RRP7BP]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[COX10]] | -0.56 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[NOL10]] | -0.56 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ZNF551]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[RRP1B]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[TBRG4]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA8]] | B | ANXA8 activity raises CYLD's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 1.52× lower at baseline in the lines without ANXA8 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[NOD2]] | B | NOD2 activity raises CYLD's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without NOD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, -39.4); signed map (-10.1, 11.7). **Vector** length 119, 44.5% of its response variance represented; |z| ≥ 3 in 1,490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.2 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.1 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.1 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.3 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.0 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.5 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.3 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.7 | -12.9 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.7 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.1 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.1 | -6.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CYLD lysine 63 deubiquitinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,742,050-50,801,935 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0849, USPL2; previously CYLD1 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; MicroRNA protein coding host genes; Centriolar satellite proteins |
| Hallmark sets | APOPTOSIS |
| Reactome | 12 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQC7](https://www.uniprot.org/uniprotkb/Q9NQC7) (Ubiquitin carboxyl-terminal hydrolase CYLD):

> Deubiquitinase that specifically cleaves 'Lys-63'- and linear 'Met-1'-linked polyubiquitin chains and is involved in NF-kappa-B inhibition and TNF-induced cell death. Negatively regulates NF-kappa-B activation by deubiquitinating upstream signaling factors, thereby preventing recruitment of TAB2 and TAB3. Plays a role in the regulation of cell survival, inflammation and innate immune response, via its effects on NF-kappa-B. Ability to remove linear ('Met-1'-linked) polyubiquitin chains …

**Summary**, from NCBI Gene [1540](https://www.ncbi.nlm.nih.gov/gene/1540):

> This gene is encodes a cytoplasmic protein with three cytoskeletal-associated protein-glycine-conserved (CAP-GLY) domains that functions as a deubiquitinating enzyme. Mutations in this gene have been associated with cylindromatosis, multiple familial trichoepithelioma, and Brooke-Spiegler syndrome. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2584) · Entrez [1540](https://www.ncbi.nlm.nih.gov/gene/1540) · UniProt [Q9NQC7](https://www.uniprot.org/uniprotkb/Q9NQC7) · Ensembl [ENSG00000083799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083799)

## Data

Gene col 1379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1379); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1379]; `tensor/DDL_lfc|DDL_z.npy` [1379]; `embed/gene_vectors.npy` [1379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1379 or target_col == 1379). Every well: [[CYLD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYLD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
