---
symbol: "NFATC1"
type: "gene"
col: 5185
ensembl_id: "ENSG00000131196"
name: "nuclear factor of activated T cells 1"
location: "18q23"
module: 181
arm: "+"
pooled_cpm: 19.97
n_lines_expressing: 39
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# NFATC1

*nuclear factor of activated T cells 1* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.25× (z +41.1, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.569× (z -8.3, q 8e-14, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELFN1]] (+0.65, fdr 7e-06), [[NPHS1]] (+0.64, fdr 1e-05), [[IL34]] (+0.64, fdr 1e-05); moves opposite to [[VPS33B]] (-0.65, fdr 1e-05), [[MRS2]] (-0.61, fdr 1e-05), [[ATP5F1C]] (-0.59, fdr 1e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PRDM16]] → it (grade B ⚠); 4 go from it, the strongest it → [[NLGN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.25×** | +41.1 | 0e+00 | 33/37 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.78×** | +18.8 | 0e+00 | 28/36 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +12.0 | 5e-31 | 19/35 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +9.8 | 1e-20 | 23/36 (SW480, NCI-H2347, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.4 | 9e-19 | 24/36 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +3.8 | 0.012 | 11/36 (H4, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.016 | 11/36 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.7 | 0.016 | 9/37 (NCI-H1792, J82, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.030 | 11/36 (PANC-1, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.030 | 12/36 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.042 | 13/36 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.048 | 6/34 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +3.1 | 0.091 | 11/35 (SW480, J82, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -8.3 | 8e-14 | 24/36 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[NG25 (drug)]] 5 µM |  | **0.429×** | -6.5 | 2e-08 | 24/34 (NCI-H1792, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.664×** | -6.0 | 4e-07 | 20/36 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.602×** | -3.9 | 0.014 | 11/31 (C-33 A, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.014 | 18/37 (MIA PaCa-2, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.782×** | -3.6 | 0.029 | 9/36 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.785×** | -3.5 | 0.032 | 8/35 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.795×** | -3.4 | 0.054 | 15/36 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.057 | 7/34 (NCI-H23, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.058 | 13/36 (NCI-H2347, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.795×** | -3.2 | 0.066 | 11/31 (A-427, NCI-H2030, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.666×** | -3.1 | 0.088 | 13/32 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.812×** | -3.1 | 0.094 | 12/34 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.094 | 9/35 (NCI-H23, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +22.3) | [[Panobinostat (drug)]] 5 µM 0.161× (z -14.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H460 (line)]] | wt | 23.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +17.0) | — |
| [[A-427 (line)]] | wt | 53.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.4) |
| [[PANC-1 (line)]] | alt | 61.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +39.8) | — |
| [[NCI-H23 (line)]] | alt | 36.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -12.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.323× (z -8.6) |
| [[A-172 (line)]] | wt | 28.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 29.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 42.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 22.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +24.6) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 19.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +19.4) | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.0787× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 15.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +24.2) | — |
| [[A549 (line)]] | wt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +20.6) | — |
| [[BT-474 (line)]] | alt | 31.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.5) | — |
| [[C32 (line)]] | wt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 9.92 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +20.4) | — |
| [[J82 (line)]] | alt | 6.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.5× (z +21.0) | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0707× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 7.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.6× (z +15.8) | — |
| [[SW 900 (line)]] | alt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +14.6) | — |
| [[SW480 (line)]] | alt | 6.48 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -9.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 8.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +23.5) | — |
| [[COLO 205 (line)]] | alt | 6.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.2) | — |
| [[RKO (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 9.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELFN1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NPHS1]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[IL34]] | +0.64 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ABR]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TGIF2-RAB5IF]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[GPR137]] | +0.60 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[COL11A2]] | +0.60 | +0.55 / +0.43 | both halves | 4e-05 |  |
| [[GNG4]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 | pathway: Beta-catenin independent WNT signaling |
| [[MIR9-1HG]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[KDM6B]] | +0.59 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS33B]] | -0.65 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[MRS2]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[JKAMP]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MRPS31P5-1]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[LONP2]] | -0.57 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[GUSBP1]] | -0.57 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[EDEM2]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PXMP4]] | -0.56 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[VDAC3]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MED23]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM16]] | B | PRDM16 activity raises NFATC1's level | lines that do not express PRDM16 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without PRDM16 | 0.006 | ⚠ within organs, on part of the lines; also absent: FBXO2, HAS3, PTPRN2 |
| [[NTN1]] | B | NTN1 activity raises NFATC1's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without NTN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[PXMP4]] | B | PXMP4 activity lowers NFATC1's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.94× higher at baseline in the lines without PXMP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[PALM]] | B | PALM activity raises NFATC1's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without PALM | 0.061 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN |
| [[C11orf96]] | B | C11orf96 activity strengthens NFATC1's drug response | lines that do not express C11orf96 (11) vs lines expressing it (26) | the lines without C11orf96 respond 0.71× as strongly (z diff +1.24); strongest at Homoharringtonine 0.5 µM: 0.90x vs 2.38x (z diff +5.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, ZNF569, PPP1R3C; target measured in part of the lines; artifact flags |
| [[HLA-L-1]] | C | HLA-L-1 activity raises NFATC1's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without HLA-L-1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN3]] | B | NFATC1 activity raises NLGN3's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without NFATC1 | 0.028 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |
| [[DPH1-AS1]] | B | NFATC1 activity raises DPH1-AS1's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 1.02× lower at baseline in the lines without NFATC1 | 0.035 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |
| [[NTN1]] | B | NFATC1 activity raises NTN1's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 2.77× lower at baseline in the lines without NFATC1 | 0.068 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |
| [[AKT1S1]] | B | NFATC1 activity lowers AKT1S1's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without NFATC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.3, -6.1); signed map (23.6, 7.2). **Vector** length 88.9, 20.1% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +41.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +18.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.4 | -8.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.3 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -2.9 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor of activated T cells 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,395,856-79,529,325 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NF-ATC, NFATc, NFAT2 |
| Gene groups (HGNC) | Nuclear factors of activated T-cells; IPT domain containing |
| Reactome | 15 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 1 cells (Th1 cells); Calcineurin activates NFAT; CLEC7A (Dectin-1) induces NFAT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95644](https://www.uniprot.org/uniprotkb/O95644) (Nuclear factor of activated T-cells, cytoplasmic 1):

> Plays a role in the inducible expression of cytokine genes in T-cells, especially in the induction of the IL-2 or IL-4 gene transcription. Also controls gene expression in embryonic cardiac cells. Could regulate not only the activation and proliferation but also the differentiation and programmed death of T-lymphocytes as well as lymphoid and non-lymphoid cells. Required for osteoclastogenesis and regulates many genes important for osteoclast differentiation and function (By similarity).

**Summary**, from NCBI Gene [4772](https://www.ncbi.nlm.nih.gov/gene/4772):

> The product of this gene is a component of the nuclear factor of activated T cells DNA-binding transcription complex. This complex consists of at least two components: a preexisting cytosolic component that translocates to the nucleus upon T cell receptor (TCR) stimulation, and an inducible nuclear component. Proteins belonging to this family of transcription factors play a central role in inducible gene transcription during immune response. The product of this gene is an inducible nuclear …

**Accessions** — [HGNC:7775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7775) · Entrez [4772](https://www.ncbi.nlm.nih.gov/gene/4772) · UniProt [O95644](https://www.uniprot.org/uniprotkb/O95644) · Ensembl [ENSG00000131196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131196)

## Data

Gene col 5185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5185); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5185]; `tensor/DDL_lfc|DDL_z.npy` [5185]; `embed/gene_vectors.npy` [5185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5185 or target_col == 5185). Every well: [[NFATC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFATC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
