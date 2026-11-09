---
symbol: "VCAN"
type: "gene"
col: 455
ensembl_id: "ENSG00000038427"
name: "versican"
location: "5q14.2-q14.3"
module: 13
arm: "+"
pooled_cpm: 108.29
n_lines_expressing: 22
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# VCAN

*versican* — 5q14.2-q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.42× (z +22.6, q 0e+00, up in 17 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +11.6, q 1e-28, up in 8 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.571× (z -8.5, q 8e-15, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO6]] (+0.61, fdr 1e-05), [[COL4A1]] (+0.60, fdr 7e-06), [[COL7A1]] (+0.59, fdr 1e-05); moves opposite to [[PDPR2P]] (-0.47, fdr 1e-04), [[CDK5RAP1]] (-0.46, fdr 2e-04), [[PPP2R3B]] (-0.45, fdr 3e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KITLG]] → it (grade B ⚠); 7 go from it, the strongest it → [[VCAN-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.42×** | +22.6 | 0e+00 | 17/21 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +15.6 | 0e+00 | 13/19 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +12.4 | 5e-33 | 10/19 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.6 | 1e-28 | 8/21 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.70×** | +11.4 | 6e-28 | 10/20 (A-172, NCI-H2347, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.2 | 7e-08 | 6/22 (A549, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.0 | 2e-07 | 6/19 (A549, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 3/20 (A-172, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.003 | 5/20 (A-427, AsPC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.008 | 16/20 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.013 | 6/21 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.015 | 3/20 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.5 | 0.023 | 7/20 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.025 | 3/21 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.036 | 6/20 (A-172, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 1.16× | +3.2 | 0.051 | 3/20 (CHP-212, HEC-1-A, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.058 | 3/20 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.077 | 7/20 (hTERT-HPNE, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -8.5 | 8e-15 | 18/20 (HepG2/C3A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -6.3 | 7e-08 | 19/20 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.664×** | -6.3 | 8e-08 | 17/20 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.700×** | -5.4 | 8e-06 | 11/20 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.792×** | -5.0 | 5e-05 | 11/20 (A498, CFPAC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.795×** | -5.0 | 7e-05 | 12/20 (CFPAC-1, H4, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -4.3 | 0.002 | 12/20 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.791×** | -3.6 | 0.024 | 2/20 (AsPC-1, CFPAC-1) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.053 | 7/19 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -3.3 | 0.053 | 12/20 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.812×** | -3.2 | 0.077 | 5/20 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.817×** | -3.1 | 0.093 | 3/20 (CFPAC-1, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.2 | 7 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +20.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.306× (z -9.2) |
| [[A549 (line)]] | wt | 40.2 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 170 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -19.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.158× (z -12.9) |
| [[A498 (line)]] | wt | 312 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 953 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.173× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 696 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 351 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -11.0) |
| [[HS-578T (line)]] | alt | 786 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.304× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 30.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +17.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 36.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 95.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -9.4) |
| [[A-427 (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 226 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 234 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.87 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.99 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.77 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO6]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[COL4A1]] | +0.60 | +0.61 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 448 |
| [[COL7A1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ANGPTL2]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TRIM55]] | +0.57 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[VCAN-AS1]] | +0.56 | +0.62 / +0.46 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[COL4A2]] | +0.56 | +0.57 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 433 |
| [[JAG1]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ANGIOGENESIS |
| [[HMCN1]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[HTR1F]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ADAMTS12]] | +0.54 | +0.58 / +0.54 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[LINC01687]] | +0.53 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[LAMC1]] | +0.53 | +0.39 / +0.58 | both halves | 5e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDPR2P]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[CDK5RAP1]] | -0.46 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PPP2R3B]] | -0.45 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[MARCHF2]] | -0.44 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[ADCK2]] | -0.44 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[SELENOO]] | -0.44 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[ZNF500]] | -0.43 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ANKS3]] | -0.43 | -0.26 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KITLG]] | B | KITLG activity raises VCAN's level | lines that do not express KITLG (10) vs lines expressing it (40) | 4.31× lower at baseline in the lines without KITLG | 0.034 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[GALNT5]] | B | GALNT5 activity raises VCAN's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without GALNT5 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[NRP1]] | B | NRP1 activity raises VCAN's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without NRP1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[EDNRA]] | C | EDNRA activity raises VCAN's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 4.37× lower at baseline in the lines without EDNRA | 0.026 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[COL4A2]] | C | COL4A2 activity raises VCAN's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 4.17× lower at baseline in the lines without COL4A2 | 0.068 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises VCAN's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 5.30× lower at baseline in the lines without ITGA4 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VCAN-AS1]] | B | VCAN activity raises VCAN-AS1's level | lines that do not express VCAN (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without VCAN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |
| [[FAP]] | B | VCAN activity raises FAP's level | lines that do not express VCAN (28) vs lines expressing it (22) | 3.06× lower at baseline in the lines without VCAN | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |
| [[GALNT5]] | B | VCAN activity raises GALNT5's level | lines that do not express VCAN (28) vs lines expressing it (22) | 1.12× lower at baseline in the lines without VCAN | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |
| [[ZNF500]] | B | VCAN activity lowers ZNF500's level | lines that do not express VCAN (28) vs lines expressing it (22) | 1.12× higher at baseline in the lines without VCAN | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |
| [[COL4A1]] | C | VCAN activity raises COL4A1's level | lines that do not express VCAN (28) vs lines expressing it (22) | 5.82× lower at baseline in the lines without VCAN | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX; co-absent with the target |
| [[COL4A2]] | C | VCAN activity raises COL4A2's level | lines that do not express VCAN (28) vs lines expressing it (22) | 5.55× lower at baseline in the lines without VCAN | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX; co-absent with the target |
| [[EDNRA]] | C | VCAN activity raises EDNRA's level | lines that do not express VCAN (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without VCAN | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.5, 22.1); signed map (24.2, 42.0). **Vector** length 75.8, 22.0% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +22.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -5.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | versican |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.2-q14.3 — chr5:83,471,618-83,582,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PG-M; previously CSPG2 |
| Gene groups (HGNC) | Hyalectan proteoglycans; V-set domain containing; Sushi domain containing; C-type lectin domain containing |
| Hallmark sets | ANGIOGENESIS, APICAL_JUNCTION, GLYCOLYSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 20 pathways, smallest: Defective CHST14 causes EDS, musculocontractural type; Defective CHST3 causes SEDCJD; Defective CHSY1 causes TPBS |
| Matched by | ensembl_id |

**Function**, from UniProt [P13611](https://www.uniprot.org/uniprotkb/P13611) (Versican core protein):

> May play a role in intercellular signaling and in connecting cells with the extracellular matrix. May take part in the regulation of cell motility, growth and differentiation. Binds hyaluronic acid.

**Summary**, from NCBI Gene [1462](https://www.ncbi.nlm.nih.gov/gene/1462):

> This gene is a member of the aggrecan/versican proteoglycan family. The protein encoded is a large chondroitin sulfate proteoglycan and is a major component of the extracellular matrix. This protein is involved in cell adhesion, proliferation, proliferation, migration and angiogenesis and plays a central role in tissue morphogenesis and maintenance. Mutations in this gene are the cause of Wagner syndrome type 1. Multiple transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:2464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2464) · Entrez [1462](https://www.ncbi.nlm.nih.gov/gene/1462) · UniProt [P13611](https://www.uniprot.org/uniprotkb/P13611) · Ensembl [ENSG00000038427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038427)

## Data

Gene col 455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 455); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 455]; `tensor/DDL_lfc|DDL_z.npy` [455]; `embed/gene_vectors.npy` [455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 455 or target_col == 455). Every well: [[VCAN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCAN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
