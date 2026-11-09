---
symbol: "NAE1"
type: "gene"
col: 8263
ensembl_id: "ENSG00000159593"
name: "NEDD8 activating enzyme E1 subunit 1"
location: "16q22.1"
module: 18
arm: "+"
pooled_cpm: 46.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NAE1

*NEDD8 activating enzyme E1 subunit 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +17.1, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.23× (z +3.8, q 0.011, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (MIA PaCa-2 4.21×, PANC-1 3.24×, NCI-H460 3.28×, A498 3.11×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1792 12.9×, HS-578T 3.59×, hTERT-HPNE 4.59×, A498 2.10×); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.35×, SW480 3.37×, NCI-H460 3.23×, A498 2.98×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.555× (z -15.1, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTD2]] (+0.72, fdr 7e-06), [[USP46]] (+0.71, fdr 7e-06), [[ME2]] (+0.69, fdr 7e-06); moves opposite to [[MTHFR]] (-0.66, fdr 7e-06), [[ZNF324]] (-0.62, fdr 9e-06), [[FKBP2]] (-0.61, fdr 1e-05, ⚠ FKBP2 in the vector space only through flagged drug-doses), [[CWC25]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8263.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (MIA PaCa-2 4.21×, PANC-1 3.24×, NCI-H460 3.28×, A498 3.11×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1792 12.9×, HS-578T 3.59×, hTERT-HPNE 4.59×, A498 2.10×); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.35×, SW480 3.37×, NCI-H460 3.23×, A498 2.98×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +17.1 | 0e+00 | 45/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +15.4 | 0e+00 | 37/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +11.3 | 1e-27 | 39/45 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.34×** | +5.1 | 6e-05 | 27/47 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.3 | 0.002 | 18/48 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **1.25×** | +3.9 | 0.007 | 22/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.16× | +3.9 | 0.007 | 12/48 (SW48, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.011 | 19/48 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.062 | 14/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.2 | 0.073 | 12/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.073 | 15/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.19× | +3.0 | 0.11 | 15/47 (NCI-H2030, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.555×** | -15.1 | 0e+00 | 40/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -8.9 | 2e-16 | 9/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -6.7 | 5e-09 | 32/49 (MIA PaCa-2, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -6.0 | 3e-07 | 29/48 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.714×** | -5.7 | 2e-06 | 25/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.603×** | -4.8 | 2e-04 | 25/48 (LOX-IMVI, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.789×** | -4.3 | 0.001 | 25/48 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.785×** | -4.2 | 0.002 | 22/48 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.032 | 15/48 (NCI-H2030, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.878× | -3.3 | 0.045 | 14/48 (SNU-1, A-427, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.045 | 15/47 (KATO III, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.837× | -3.2 | 0.059 | 11/48 (NCI-H2347, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +16.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -23.4) |
| [[NCI-H460 (line)]] | wt | 60.3 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -20.6) |
| [[NCI-H2030 (line)]] | alt | 118 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.6) |
| [[A-172 (line)]] | wt | 27.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.6) |
| [[A498 (line)]] | wt | 52.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 38.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.5) |
| [[PANC-1 (line)]] | alt | 40.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.5) |
| [[Hs 766T (line)]] | wt | 35.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.7) |
| [[LoVo (line)]] | wt | 39.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 34.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 32.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +23.1) | — |
| [[RKO (line)]] | wt | 83.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.0) |
| [[SNU-1 (line)]] | wt | 60.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.5) |
| [[SW480 (line)]] | alt | 88.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 74.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -9.9) |
| [[A549 (line)]] | wt | 41.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.3) |
| [[HCT15 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 27.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 46.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 57.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -8.8) |
| [[C-33 A (line)]] | alt | 76.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.9) |
| [[HS-578T (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.3) | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +13.4) | — |
| [[J82 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.5) |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.6) |
| [[SW48 (line)]] | wt | 61.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTD2]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[USP46]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ME2]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[FAM136A]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[VPS36]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NAA50]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ZC3HAV1L]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[IPO5]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[TMEM209]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ALG6]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[GLO1]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFR]] | -0.66 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ZNF324]] | -0.62 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[FKBP2]] ⚠ | -0.61 | -0.60 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CWC25]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[TTC21A]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ANKHD1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ATP6V0D1]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[NBPF19]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[RAB5A]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 | STRING 495 |
| [[STX5]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[MIDN]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NAE1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ADCY3]] | B | ADCY3 activity raises NAE1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without ADCY3 | 0.097 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-24.5, -29.5); signed map (-12.8, -41.5). **Vector** length 99.8, 25.0% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +15.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | +3.2 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.3 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -15.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -3.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | NEDD8 activating enzyme E1 subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,802,875-66,873,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ula-1, APP-BP1; previously APPBP1 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13564](https://www.uniprot.org/uniprotkb/Q13564) (NEDD8-activating enzyme E1 regulatory subunit):

> Regulatory subunit of the dimeric UBA3-NAE1 E1 enzyme. E1 activates NEDD8 by first adenylating its C-terminal glycine residue with ATP, thereafter linking this residue to the side chain of the catalytic cysteine, yielding a NEDD8-UBA3 thioester and free AMP. E1 finally transfers NEDD8 to the catalytic cysteine of UBE2M. Necessary for cell cycle progression through the S-M checkpoint. Overexpression of NAE1 causes apoptosis through deregulation of NEDD8 conjugation. The covalent attachment of …

**Summary**, from NCBI Gene [8883](https://www.ncbi.nlm.nih.gov/gene/8883):

> The protein encoded by this gene binds to the beta-amyloid precursor protein. Beta-amyloid precursor protein is a cell surface protein with signal-transducing properties, and it is thought to play a role in the pathogenesis of Alzheimer's disease. In addition, the encoded protein can form a heterodimer with UBE1C and bind and activate NEDD8, a ubiquitin-like protein. This protein is required for cell cycle progression through the S/M checkpoint. Three transcript variants encoding different …

**Accessions** — [HGNC:621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:621) · Entrez [8883](https://www.ncbi.nlm.nih.gov/gene/8883) · UniProt [Q13564](https://www.uniprot.org/uniprotkb/Q13564) · Ensembl [ENSG00000159593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159593)

## Data

Gene col 8263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8263); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8263]; `tensor/DDL_lfc|DDL_z.npy` [8263]; `embed/gene_vectors.npy` [8263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8263 or target_col == 8263). Every well: [[NAE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
