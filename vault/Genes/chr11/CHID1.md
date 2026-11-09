---
symbol: "CHID1"
type: "gene"
col: 10867
ensembl_id: "ENSG00000177830"
name: "chitinase domain containing 1"
location: "11p15.5"
module: 18
arm: "+"
pooled_cpm: 19.1
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CHID1

*chitinase domain containing 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +20.7, q 0e+00, up in 36 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.15× (z +3.8, q 0.011, up in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 2.30×, HOP62 3.94×, HS-578T 3.89×, C32 4.49×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 3.29×, KATO III 5.65×, A498 2.75×, LoVo 4.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.57×; ⚠ cell-cycle shift, explains ~68% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.496× (z -19.1, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFTUD2]] (+0.76, fdr 7e-06), [[NOC2L]] (+0.75, fdr 7e-06), [[URB1]] (+0.75, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.69, fdr 7e-06), [[ATF4]] (-0.67, fdr 7e-06), [[PNRC1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10867.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 2.30×, HOP62 3.94×, HS-578T 3.89×, C32 4.49×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 3.29×, KATO III 5.65×, A498 2.75×, LoVo 4.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.57×; ⚠ cell-cycle shift, explains ~68% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.94×** | +20.7 | 0e+00 | 36/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.78×** | +18.9 | 0e+00 | 30/30 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.13×** | +13.4 | 9e-39 | 32/37 (SW1417, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.74×** | +10.6 | 4e-24 | 38/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +7.9 | 4e-13 | 28/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.41×** | +6.5 | 6e-09 | 28/47 (LoVo, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.28×** | +4.5 | 5e-04 | 16/43 (HT-29, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.16× | +4.0 | 0.004 | 18/47 (NCI-H2347, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.011 | 10/48 (A-172, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.22×** | +3.7 | 0.013 | 14/46 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.035 | 7/45 (C32, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.20×** | +3.3 | 0.039 | 10/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.2 | 0.067 | 10/47 (RKO, Panc 03.27, …) | top dose only |  |
| [[Brimonidine (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.077 | 3/46 (SW48, C32, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.086 | 3/45 (SW480, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.496×** | -19.1 | 0e+00 | 45/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.587×** | -9.9 | 1e-20 | 29/47 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -9.7 | 4e-20 | 29/47 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.776×** | -6.9 | 6e-10 | 28/48 (J82, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.776×** | -4.9 | 1e-04 | 17/47 (BT-474, SNU-1, …) | all doses, flat |  |
| [[Penfluridol (drug)]] 5 µM |  | **0.789×** | -4.4 | 9e-04 | 9/47 (BT-474, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.680×** | -3.9 | 0.008 | 9/46 (J82, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.831×** | -3.6 | 0.024 | 10/47 (hTERT-HPNE, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.846× | -3.2 | 0.076 | 4/48 (HEC-1-A, SW 1088, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.894× | -3.1 | 0.11 | 5/48 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.851× | -3.0 | 0.13 | 7/48 (J82, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.4) |
| [[PANC-1 (line)]] | alt | 45.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.7) |
| [[A498 (line)]] | wt | 25.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 28.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0850× (z -19.7) |
| [[HOP62 (line)]] | alt | 18.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.0) |
| [[J82 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.8) |
| [[SW48 (line)]] | wt | 19.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0844× (z -10.4) |
| [[A-172 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -16.0) |
| [[BT-474 (line)]] | alt | 8.71 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0982× (z -9.8) |
| [[C32 (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.324× (z -9.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HS-578T (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.65× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.236× (z -9.0) |
| [[RKO (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.9) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.5) |
| [[SW480 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -8.6) |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | +0.76 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.75 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[URB1]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[QSOX2]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[INTS1]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[EMC1]] | +0.72 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[NOP9]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[NUTF2]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.69 | -0.74 / -0.59 | both halves | 7e-06 |  |
| [[ATF4]] | -0.67 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[PNRC1]] | -0.65 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[MITD1]] | -0.64 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[GATAD1]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[PIM3]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[WHAMM]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[BTN2A3P-1]] | -0.63 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[REST]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.63 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[GGNBP2]] | -0.62 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.62 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises CHID1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without PODXL2 | 0.044 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-19.7, -28.2); signed map (-24.4, -44.7). **Vector** length 84.7, 16.7% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.8 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.8 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.3 | +13.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.0 | +10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.6 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.4 | +0.1 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -19.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -9.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.6 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | chitinase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:867,859-915,058 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3234, FLJ42707, SI-CLP |
| Gene groups (HGNC) | Chitinases |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWS9](https://www.uniprot.org/uniprotkb/Q9BWS9) (Chitinase domain-containing protein 1):

> Saccharide- and LPS-binding protein with possible roles in pathogen sensing and endotoxin neutralization. Ligand-binding specificity relates to the length of the oligosaccharides, with preference for chitotetraose (in vitro).

**Summary**, from NCBI Gene [66005](https://www.ncbi.nlm.nih.gov/gene/66005):

> Enables oligosaccharide binding activity. Involved in negative regulation of cytokine production involved in inflammatory response. Located in several cellular components, including late endosome; obsolete extracellular space; and trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28474) · Entrez [66005](https://www.ncbi.nlm.nih.gov/gene/66005) · UniProt [Q9BWS9](https://www.uniprot.org/uniprotkb/Q9BWS9) · Ensembl [ENSG00000177830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177830)

## Data

Gene col 10867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10867); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10867]; `tensor/DDL_lfc|DDL_z.npy` [10867]; `embed/gene_vectors.npy` [10867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10867 or target_col == 10867). Every well: [[CHID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
