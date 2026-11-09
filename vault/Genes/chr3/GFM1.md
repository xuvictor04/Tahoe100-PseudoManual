---
symbol: "GFM1"
type: "gene"
col: 9708
ensembl_id: "ENSG00000168827"
name: "G elongation factor mitochondrial 1"
location: "3q25.32"
module: 4
arm: "+"
pooled_cpm: 54.33
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GFM1

*G elongation factor mitochondrial 1* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +19.6, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.832× (z -4.2, q 0.017, down in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.784× (z -3.9, q 0.024, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.129×, SK-MEL-2 0.379×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (CHP-212 0.0742×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.533×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM33]] (+0.75, fdr 7e-06), [[EFTUD2]] (+0.74, fdr 1e-05), [[MRPL42]] (+0.73, fdr 7e-06); moves opposite to [[RSRP1]] (-0.69, fdr 8e-06), [[TESK2]] (-0.67, fdr 7e-06), [[AAMDC]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +19.6 | 0e+00 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.30×** | +18.7 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.09×** | +16.5 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +15.8 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +15.7 | 0e+00 | 46/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.93×** | +14.7 | 0e+00 | 45/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +14.4 | 3e-45 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +14.0 | 6e-43 | 38/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +13.7 | 8e-41 | 40/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +12.8 | 8e-36 | 39/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +12.8 | 1e-35 | 45/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +12.8 | 1e-35 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.76×** | +12.7 | 3e-35 | 42/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.71×** | +12.0 | 1e-31 | 32/48 (LoVo, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.68×** | +11.2 | 1e-27 | 31/43 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +10.3 | 2e-23 | 39/49 (HEC-1-A, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 6e-12 | 33/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +7.1 | 3e-11 | 29/48 (KATO III, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +5.6 | 4e-07 | 26/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.2 | 5e-06 | 17/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 6e-06 | 21/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.129×, SK-MEL-2 0.379×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (CHP-212 0.0742×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.533×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.832×** | -4.2 | 0.017 | 19/48 (SW 1088, SNU-423, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.784×** | -3.9 | 0.024 | 16/48 (LS 180, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.853× | -3.6 | 0.040 | 13/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.853× | -3.6 | 0.040 | 15/48 (SW 1088, KATO III, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.710×** | -3.6 | 0.040 | 16/48 (LS 180, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.866× | -3.3 | 0.096 | 11/48 (A498, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.825× | -3.1 | 0.15 | 12/48 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 39.3 | 12 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 33.1 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +18.1) | — |
| [[SW480 (line)]] | alt | 75.6 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 35.7 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 65.0 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 39.0 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +12.3) | — |
| [[A549 (line)]] | wt | 47.0 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 40.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.3) | — |
| [[KATO III (line)]] | alt | 57.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 94.6 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 36.2 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 45.2 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.73× (z +8.7) | — |
| [[A-427 (line)]] | wt | 105 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.59× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 51.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 26.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 29.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 59.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.1) | — |
| [[A-172 (line)]] | wt | 41.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.7) | — |
| [[J82 (line)]] | alt | 106 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 65.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 32.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.82× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[BT-474 (line)]] | alt | 83.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +10.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0742× (z -11.2) |
| [[H4 (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 65.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 41.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.80× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 60.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 56.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.9) | — |
| [[RKO (line)]] | wt | 66.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 68.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.80× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.7) | — |
| [[SW48 (line)]] | wt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM33]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.74 | +0.56 / +0.76 | both halves | 1e-05 | same gene group |
| [[MRPL42]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | pathway: Mitochondrial translation; STRING 831 |
| [[ANAPC7]] | +0.71 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[FARSB]] | +0.70 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | pathway: Mitochondrial translation; STRING 884 |
| [[NAA15]] | +0.68 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 | STRING 744 |
| [[ELAC2]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CLPB]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 | STRING 438 |
| [[NUP42]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[COA1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.69 | -0.57 / -0.70 | both halves | 8e-06 |  |
| [[TESK2]] | -0.67 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.64 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 | STRING 447 |
| [[STX5-DT]] | -0.63 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.63 | -0.47 / -0.72 | both halves | 2e-05 |  |
| [[DEDD2]] | -0.61 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[GTF2B]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[FAM53C]] | -0.61 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[SPACDR]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.59 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[DHDH]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.2, -33.3); signed map (-9.7, -45.7). **Vector** length 88.5, 25.2% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +5.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.7 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.6 | +11.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +12.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.7 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | G elongation factor mitochondrial 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,644,527-158,695,581 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EF-G1mt, mtEFG1, EFGM, GFM, EGF1, mtEF-G1 |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 3 pathways, smallest: Mitochondrial translation elongation; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RP9](https://www.uniprot.org/uniprotkb/Q96RP9) (Elongation factor G, mitochondrial):

> Mitochondrial GTPase that catalyzes the GTP-dependent ribosomal translocation step during translation elongation. During this step, the ribosome changes from the pre-translocational (PRE) to the post-translocational (POST) state as the newly formed A-site-bound peptidyl-tRNA and P-site-bound deacylated tRNA move to the P and E sites, respectively. Catalyzes the coordinated movement of the two tRNA molecules, the mRNA and conformational changes in the ribosome. Does not mediate the disassembly …

**Summary**, from NCBI Gene [85476](https://www.ncbi.nlm.nih.gov/gene/85476):

> Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongation factors. Its role in the regulation of normal mitochondrial function and in different disease …

**Accessions** — [HGNC:13780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13780) · Entrez [85476](https://www.ncbi.nlm.nih.gov/gene/85476) · UniProt [Q96RP9](https://www.uniprot.org/uniprotkb/Q96RP9) · Ensembl [ENSG00000168827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168827)

## Data

Gene col 9708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9708); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9708]; `tensor/DDL_lfc|DDL_z.npy` [9708]; `embed/gene_vectors.npy` [9708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9708 or target_col == 9708). Every well: [[GFM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
