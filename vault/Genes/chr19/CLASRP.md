---
symbol: "CLASRP"
type: "gene"
col: 2508
ensembl_id: "ENSG00000104859"
name: "CLK4 associating serine/arginine rich protein"
location: "19q13.32"
module: 3
arm: "+"
pooled_cpm: 70.68
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CLASRP

*CLK4 associating serine/arginine rich protein* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +10.9, q 6e-25, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.538× (z -10.7, q 8e-24, down in 34 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HEC-1-A 0.309×, HOP62 0.367×, CHP-212 0.126×, HS-578T 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.0583×, HOP62 0.321×, SW 900 0.285×, SW1417 0.426×; ⚠ toxic; transcription drop); [[Belzutifan (drug)]] 5 µM in 1 line (HCT15 0.0731×); [[Larotrectinib (drug)]] 5 µM in 1 line (H4 0.315×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF500]] (+0.66, fdr 1e-05), [[CHST12]] (+0.65, fdr 1e-05), [[PRPF6]] (+0.64, fdr 2e-05); moves opposite to [[LEPROT]] (-0.59, fdr 1e-05), [[CHRAC1]] (-0.58, fdr 3e-05), [[MOB1A]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +10.9 | 6e-25 | 33/48 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +9.0 | 5e-17 | 40/48 (KATO III, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +8.3 | 1e-14 | 42/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.1 | 1e-07 | 34/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 2e-06 | 35/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +5.6 | 2e-06 | 31/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 4e-04 | 30/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 0.001 | 26/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.25×** | +4.0 | 0.005 | 24/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.9 | 0.005 | 19/37 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.007 | 25/49 (HOP62, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.009 | 23/48 (NCI-H460, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.047 | 20/48 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.069 | 23/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2508.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HEC-1-A 0.309×, HOP62 0.367×, CHP-212 0.126×, HS-578T 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.0583×, HOP62 0.321×, SW 900 0.285×, SW1417 0.426×; ⚠ toxic; transcription drop); [[Belzutifan (drug)]] 5 µM in 1 line (HCT15 0.0731×); [[Larotrectinib (drug)]] 5 µM in 1 line (H4 0.315×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -10.7 | 8e-24 | 34/43 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -8.4 | 1e-14 | 37/48 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.777×** | -4.2 | 0.005 | 24/45 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.830× | -3.3 | 0.12 | 21/48 (BT-474, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.840× | -3.1 | 0.21 | 17/49 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.0 | 0.22 | 12/49 (SK-MEL-2, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 50.1 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.51× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) | — |
| [[SW480 (line)]] | alt | 67.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 97.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 161 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 64.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 46.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 39.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.3) | [[Larotrectinib (drug)]] 5 µM 0.315× (z -10.5) |
| [[HCT15 (line)]] | alt | 70.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.0) | [[Belzutifan (drug)]] 5 µM 0.0731× (z -11.5) |
| [[HS-578T (line)]] | alt | 83.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 70.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.6) | — |
| [[SW 900 (line)]] | alt | 78.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.14× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 78.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0583× (z -22.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 87.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 61.4 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.31× (z +9.2) | — |
| [[LoVo (line)]] | wt | 55.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 69.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.6) | — |
| [[Panc 03.27 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 82.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.7) | — |
| [[SK-MEL-2 (line)]] | alt | 79.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SW48 (line)]] | wt | 80.2 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.45× (z +10.8) | — |
| [[A-427 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF500]] | +0.66 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[CHST12]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.64 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[RANBP10]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DRG1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MIGA2]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[TAF6L]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SNRNP70]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 | STRING 480 |
| [[E4F1]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TARS2]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[RPS26]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SUGP1]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEPROT]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CHRAC1]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NXT2]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[SCRN1]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RO60]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.56 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[STK26]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ZBTB33]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TUG1]] | -0.55 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[PRKAR1A]] | -0.54 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[M6PR]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.1, -6.2); signed map (-34.5, 0.8). **Vector** length 101, 26.6% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +5.3 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +10.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | -0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CLK4 associating serine/arginine rich protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,039,045-45,070,956 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SWAP2, CLASP; previously SFRS16 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2M8](https://www.uniprot.org/uniprotkb/Q8N2M8) (CLK4-associating serine/arginine rich protein):

> Probably functions as an alternative splicing regulator. May regulate the mRNA splicing of genes such as CLK1. May act by regulating members of the CLK kinase family (By similarity).

**Summary**, from NCBI Gene [11129](https://www.ncbi.nlm.nih.gov/gene/11129):

> Predicted to be involved in RNA splicing and mRNA processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17731) · Entrez [11129](https://www.ncbi.nlm.nih.gov/gene/11129) · UniProt [Q8N2M8](https://www.uniprot.org/uniprotkb/Q8N2M8) · Ensembl [ENSG00000104859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104859)

## Data

Gene col 2508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2508); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2508]; `tensor/DDL_lfc|DDL_z.npy` [2508]; `embed/gene_vectors.npy` [2508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2508 or target_col == 2508). Every well: [[CLASRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLASRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
