---
symbol: "METAP1D"
type: "gene"
col: 10308
ensembl_id: "ENSG00000172878"
name: "methionyl aminopeptidase type 1D, mitochondrial"
location: "2q31.1"
module: 1
arm: "+"
pooled_cpm: 15.59
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# METAP1D

*methionyl aminopeptidase type 1D, mitochondrial* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.55× (z +5.1, q 2e-04, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -10.2, q 1e-21, down in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.485× (z -8.4, q 9e-15, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZZZ3]] (+0.76, fdr 7e-06), [[UTP20]] (+0.76, fdr 7e-06), [[ABCE1]] (+0.73, fdr 7e-06); moves opposite to [[CARD19]] (-0.62, fdr 1e-05), [[CDK2AP2]] (-0.61, fdr 1e-05), [[PHF1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FTCDNL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +5.1 | 2e-04 | 28/46 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.9 | 3e-04 | 15/30 (LoVo, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +4.5 | 0.001 | 16/46 (LoVo, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.003 | 22/47 (SW 900, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.29×** | +4.2 | 0.003 | 19/47 (HS-578T, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.004 | 16/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.4 | 0.047 | 3/47 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.061 | 10/47 (CFPAC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.064 | 19/46 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.31× | +3.1 | 0.10 | 5/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.31× | +3.1 | 0.10 | 13/46 (NCI-H1573, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.535×** | -10.2 | 1e-21 | 30/46 (PANC-1, SW1417, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.453×** | -9.2 | 2e-17 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.477×** | -8.6 | 2e-15 | 32/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.485×** | -8.4 | 9e-15 | 31/46 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.545×** | -7.0 | 3e-10 | 30/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.552×** | -6.9 | 6e-10 | 30/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -5.5 | 2e-06 | 26/46 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.634×** | -5.3 | 9e-06 | 25/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.643×** | -5.1 | 2e-05 | 23/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.647×** | -4.8 | 7e-05 | 23/46 (PANC-1, A-427, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.680×** | -4.5 | 4e-04 | 22/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.677×** | -4.3 | 7e-04 | 22/43 (RKO, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.692×** | -4.3 | 9e-04 | 24/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.503×** | -4.2 | 0.001 | 21/45 (HCT15, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.700×** | -4.1 | 0.001 | 20/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.705×** | -4.1 | 0.002 | 18/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -4.0 | 0.002 | 21/46 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -3.2 | 0.034 | 14/44 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -3.1 | 0.053 | 13/46 (SW480, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.3 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.256× (z -11.5) |
| [[PANC-1 (line)]] | alt | 22.7 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.9) |
| [[A-427 (line)]] | wt | 29.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.221× (z -11.6) |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.142× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.234× (z -9.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A549 (line)]] | wt | 15.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.8) |
| [[A498 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0590× (z -10.1) |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0908× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -9.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0722× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW 900 (line)]] | alt | 6.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -8.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZZZ3]] | +0.76 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[UTP20]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MRRF]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[LTV1]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[COX10]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[DPH6]] | +0.70 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NAA25]] | +0.70 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[TCERG1]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[RRP15]] | +0.69 | +0.73 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD19]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CDK2AP2]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PHF1]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[NDRG1]] | -0.60 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[APAF1]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.60 | -0.54 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FTCDNL1]] | B | FTCDNL1 activity raises METAP1D's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without FTCDNL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity lowers METAP1D's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.06× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[SLC17A7]] | B | SLC17A7 activity raises METAP1D's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without SLC17A7 | 0.037 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity weakens METAP1D's drug response | lines that do not express NDRG1 (6) vs lines expressing it (41) | the lines without NDRG1 respond 1.79× as strongly (z diff -2.58); strongest at Idarubicin (hydrochloride) 5 µM: 0.52x vs 0.80x (z diff -4.2) | 0.071 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1; target measured in part of the lines; artifact flags |
| [[MVB12B]] | B | MVB12B activity raises METAP1D's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without MVB12B | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[ENTPD1-AS1]] | C | ENTPD1-AS1 activity raises METAP1D's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[LINC01341]] | C | LINC01341 activity raises METAP1D's level | lines that do not express LINC01341 (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without LINC01341 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HHAT, IMPG2, PHC1; maybe low, not absent; its own permutation p |
| [[ZNF32]] | C | ZNF32 activity raises METAP1D's level | lines that do not express ZNF32 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without ZNF32 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF221, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.4, -33.8); signed map (2.6, -41.6). **Vector** length 88.5, 19.7% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial mRNA modification* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +3.8 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.6 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.9 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | methionyl aminopeptidase type 1D, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:171,999,943-172,082,430 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAP1D, Metap1l |
| Gene groups (HGNC) | Aminopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UB28](https://www.uniprot.org/uniprotkb/Q6UB28) (Methionine aminopeptidase 1D, mitochondrial):

> Removes the N-terminal methionine from nascent proteins. The N-terminal methionine is often cleaved when the second residue in the primary sequence is small and uncharged (Met-Ala-, Cys, Gly, Pro, Ser, Thr, or Val). Requires deformylation of the N(alpha)-formylated initiator methionine before it can be hydrolyzed (By similarity). May play a role in colon tumorigenesis.

**Summary**, from NCBI Gene [254042](https://www.ncbi.nlm.nih.gov/gene/254042):

> The N-terminal methionine excision pathway is an essential process in which the N-terminal methionine is removed from many proteins, thus facilitating subsequent protein modification. In mitochondria, enzymes that catalyze this reaction are celled methionine aminopeptidases (MetAps, or MAPs; EC 3.4.11.18) (Serero et al., 2003 [PubMed 14532271]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:32583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32583) · Entrez [254042](https://www.ncbi.nlm.nih.gov/gene/254042) · UniProt [Q6UB28](https://www.uniprot.org/uniprotkb/Q6UB28) · Ensembl [ENSG00000172878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172878)

## Data

Gene col 10308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10308); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10308]; `tensor/DDL_lfc|DDL_z.npy` [10308]; `embed/gene_vectors.npy` [10308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10308 or target_col == 10308). Every well: [[METAP1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METAP1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
