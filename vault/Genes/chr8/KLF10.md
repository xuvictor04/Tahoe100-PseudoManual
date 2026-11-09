---
symbol: "KLF10"
type: "gene"
col: 7867
ensembl_id: "ENSG00000155090"
name: "KLF transcription factor 10"
location: "8q22.3"
module: 14
arm: "+"
pooled_cpm: 109.98
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# KLF10

*KLF transcription factor 10* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 18.9× (z +62.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.611× (z -6.5, q 5e-08, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 0.152×, C-33 A 0.118×, LOX-IMVI 0.213×, HepG2/C3A 0.132×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 3 lines (HOP62 0.221×, LOX-IMVI 0.355×, H4 0.251×; ⚠ cell-cycle shift, explains ~52% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.187×, HOP62 0.249×; ⚠ cell-cycle shift, explains ~56% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GASAL1]] (+0.71, fdr 7e-06), [[BCOR]] (+0.68, fdr 7e-06), [[NFKBIE]] (+0.67, fdr 7e-06); moves opposite to [[TRMT2B]] (-0.60, fdr 1e-05), [[DIP2A]] (-0.60, fdr 1e-05), [[MTFR1]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLEKHG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **18.9×** | +62.8 | 0e+00 | 48/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **19.3×** | +43.0 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **10.1×** | +35.0 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **28.3×** | +26.4 | 0e+00 | 49/49 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.30×** | +25.2 | 0e+00 | 48/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.14×** | +11.5 | 1e-28 | 42/48 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.01×** | +10.6 | 3e-24 | 42/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.95×** | +10.1 | 5e-22 | 46/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.01×** | +9.8 | 9e-21 | 39/45 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.12×** | +9.0 | 1e-17 | 37/48 (LS 180, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.57×** | +6.8 | 5e-10 | 30/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.7 | 8e-10 | 34/48 (AN3 CA, C-33 A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.5 | 4e-09 | 31/49 (COLO 205, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.51×** | +6.0 | 7e-08 | 28/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.48×** | +6.0 | 1e-07 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.72×** | +5.9 | 2e-07 | 32/48 (HEC-1-A, COLO 205, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.5 | 1e-06 | 30/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.003 | 26/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Mifepristone (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.003 | 24/48 (KATO III, LS 180, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.19× | +3.7 | 0.007 | 21/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.026 | 15/48 (AsPC-1, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7867.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 0.152×, C-33 A 0.118×, LOX-IMVI 0.213×, HepG2/C3A 0.132×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 3 lines (HOP62 0.221×, LOX-IMVI 0.355×, H4 0.251×; ⚠ cell-cycle shift, explains ~52% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.187×, HOP62 0.249×; ⚠ cell-cycle shift, explains ~56% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.611×** | -6.5 | 5e-08 | 31/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -5.9 | 1e-06 | 28/44 (Panc 03.27, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.699×** | -5.4 | 1e-05 | 29/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **0.609×** | -3.9 | 0.013 | 24/45 (C32, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.781×** | -3.6 | 0.036 | 21/47 (RKO, H4, …) | rises with dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.810× | -3.2 | 0.14 | 16/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.866× | -3.1 | 0.17 | 11/48 (HOP62, A-172, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.868× | -3.0 | 0.17 | 15/48 (MIA PaCa-2, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.8 | 17 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +40.5) | — |
| [[LOX-IMVI (line)]] | wt | 188 | 6 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +30.8) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -16.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 72.5 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +33.4) | — |
| [[BT-474 (line)]] | alt | 69.8 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.1× (z +36.9) | — |
| [[C32 (line)]] | wt | 184 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 28.3× (z +35.8) | [[Bortezomib (drug)]] 5 µM 0.0804× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[HepG2_C3A (line)]] | wt | 155 | 9 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +35.9) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -15.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 66.4 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +36.0) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 79.5 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +40.4) | — |
| [[NCI-H2347 (line)]] | alt | 130 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +40.5) | — |
| [[SW480 (line)]] | alt | 98.5 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +24.7) | — |
| [[AsPC-1 (line)]] | alt | 95.6 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 45.4× (z +40.7) | — |
| [[PANC-1 (line)]] | alt | 102 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.3× (z +51.3) | — |
| [[A549 (line)]] | wt | 134 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +36.1) | — |
| [[CFPAC-1 (line)]] | alt | 102 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +43.2) | — |
| [[COLO 205 (line)]] | alt | 86.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 91.7× (z +44.8) | — |
| [[HOP62 (line)]] | alt | 184 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +37.5) | [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -15.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[J82 (line)]] | alt | 118 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +33.4) | — |
| [[KATO III (line)]] | alt | 77.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +44.2) | — |
| [[SK-MEL-2 (line)]] | alt | 86.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.2× (z +37.9) | — |
| [[SNU-1 (line)]] | wt | 71.9 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 177 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +43.6) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 81.0 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +31.2) | [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -10.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 69.2 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 31.8× (z +42.6) | [[Ixazomib citrate (drug)]] 5 µM 0.377× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[Panc 03.27 (line)]] | alt | 127 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +43.2) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -17.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 112 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +34.5) | — |
| [[A-427 (line)]] | wt | 62.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +20.9) | — |
| [[AN3 CA (line)]] | alt | 113 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +17.6) | — |
| [[HS-578T (line)]] | alt | 150 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +29.0) | — |
| [[LoVo (line)]] | wt | 35.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +26.9) | — |
| [[NCI-H2030 (line)]] | alt | 49.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +28.4) | — |
| [[RPMI-7951 (line)]] | alt | 114 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +26.9) | — |
| [[SW 900 (line)]] | alt | 122 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +37.3) | — |
| [[SW1417 (line)]] | alt | 159 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +35.9) | — |
| [[SW48 (line)]] | wt | 112 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +22.5) | — |
| [[CHP-212 (line)]] | wt | 103 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +16.8) | — |
| [[HCT15 (line)]] | alt | 119 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +26.4) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 109 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +22.5) | — |
| [[NCI-H1792 (line)]] | alt | 80.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +32.3) | — |
| [[NCI-H23 (line)]] | alt | 109 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +22.8) | — |
| [[RKO (line)]] | wt | 149 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +21.1) | — |
| [[SNU-423 (line)]] | alt | 79.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +34.5) | — |
| [[SW 1088 (line)]] | alt | 155 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.8× (z +18.1) | — |
| [[Hs 766T (line)]] | wt | 103 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +32.6) | — |
| [[SHP-77 (line)]] | alt | 112 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +23.1) | — |
| [[C-33 A (line)]] | alt | 130 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.7× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -16.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 211 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +15.3) | — |
| [[SW 1271 (line)]] | alt | 73.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +15.6) | — |
| [[NCI-H661 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +9.5) | — |
| [[NCI-H2122 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GASAL1]] | +0.71 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[BCOR]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.67 | +0.75 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BHLHE41]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CSRNP1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 | STRING 412 |
| [[TSC22D1]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SKIL]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[HES1]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[NR1D1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PER2]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[JUNB]] | +0.61 | +0.72 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 578 |
| [[BCL9L]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT2B]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[DIP2A]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MTFR1]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SGSM3]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SEC23A]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD39]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[NAP1L4]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[UFD1]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[NAPB]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG2]] | B | PLEKHG2 activity raises KLF10's level | lines that do not express PLEKHG2 (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without PLEKHG2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises KLF10's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, -2.6); signed map (-2.1, 12.9). **Vector** length 125, 40.9% of its response variance represented; |z| ≥ 3 in 1,408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.9 | +25.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +35.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +26.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +43.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.9 | +10.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.3 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -10.8 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -10.8 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.8 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.4 | -2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | -6.0 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.3 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.5 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:102,648,784-102,655,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EGRA, TIEG1; previously TIEG |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | TGF_BETA_SIGNALING, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13118](https://www.uniprot.org/uniprotkb/Q13118) (Krueppel-like factor 10):

> Transcriptional repressor which binds to the consensus sequence 5'-GGTGTG-3'. Plays a role in the regulation of the circadian clock; binds to the GC box sequence in the promoter of the core clock component ARTNL/BMAL1 and represses its transcriptional activity. Regulates the circadian expression of genes involved in lipogenesis, gluconeogenesis, and glycolysis in the liver. Represses the expression of PCK2, a rate-limiting step enzyme of gluconeogenesis (By similarity). May play a role in the …

**Summary**, from NCBI Gene [7071](https://www.ncbi.nlm.nih.gov/gene/7071):

> This gene encodes a member of a family of proteins that feature C2H2-type zinc finger domains. The encoded protein is a transcriptional repressor that acts as an effector of transforming growth factor beta signaling. Activity of this protein may inhibit the growth of cancers, particularly pancreatic cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:11810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11810) · Entrez [7071](https://www.ncbi.nlm.nih.gov/gene/7071) · UniProt [Q13118](https://www.uniprot.org/uniprotkb/Q13118) · Ensembl [ENSG00000155090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155090)

## Data

Gene col 7867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7867); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7867]; `tensor/DDL_lfc|DDL_z.npy` [7867]; `embed/gene_vectors.npy` [7867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7867 or target_col == 7867). Every well: [[KLF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
