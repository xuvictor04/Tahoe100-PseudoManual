---
symbol: "EIF4ENIF1"
type: "gene"
col: 11569
ensembl_id: "ENSG00000184708"
name: "eukaryotic translation initiation factor 4E nuclear import factor 1"
location: "22q12.2"
module: 15
arm: "+"
pooled_cpm: 28.09
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# EIF4ENIF1

*eukaryotic translation initiation factor 4E nuclear import factor 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +12.8, q 2e-34, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.571× (z -12.9, q 2e-35, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF500]] (+0.69, fdr 1e-05), [[ZNF251]] (+0.68, fdr 1e-05), [[CCT6P3-1]] (+0.66, fdr 1e-05); moves opposite to [[JUNB]] (-0.61, fdr 1e-05), [[ABLIM1]] (-0.58, fdr 2e-05), [[ATP7A]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +12.8 | 2e-34 | 33/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.7 | 5e-09 | 26/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +5.3 | 3e-05 | 21/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.1 | 0.006 | 19/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.8 | 0.016 | 7/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.024 | 9/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.060 | 11/47 (PANC-1, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.068 | 11/48 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.068 | 9/47 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.15× | +3.2 | 0.078 | 12/47 (NCI-H1573, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.078 | 12/48 (SW48, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.1 | 0.10 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.571×** | -12.9 | 2e-35 | 36/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.607×** | -11.1 | 5e-26 | 30/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -10.7 | 3e-24 | 35/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -10.5 | 1e-23 | 22/37 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.651×** | -9.9 | 5e-21 | 30/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -9.8 | 2e-20 | 32/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.777×** | -8.2 | 2e-14 | 27/48 (A-172, SK-MEL-2, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -5.9 | 2e-07 | 18/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.759×** | -5.9 | 3e-07 | 20/40 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -5.7 | 8e-07 | 23/48 (CHP-212, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.783×** | -5.6 | 9e-07 | 20/48 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.785×** | -5.6 | 1e-06 | 20/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.788×** | -5.5 | 2e-06 | 20/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.807×** | -4.9 | 3e-05 | 20/47 (A-172, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.806×** | -4.6 | 2e-04 | 17/47 (A498, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mozavaptan (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.035 | 11/47 (J82, C32, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.913× | -3.0 | 0.085 | 4/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.3 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -10.7) |
| [[HOP62 (line)]] | alt | 21.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.249× (z -11.7) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.297× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 33.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -10.9) |
| [[A498 (line)]] | wt | 44.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -8.5) |
| [[C32 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0771× (z -10.8) |
| [[J82 (line)]] | alt | 26.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.361× (z -8.7) |
| [[LS 180 (line)]] | wt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 1 | — | [[Erdafitinib (drug)]] 0.05 µM 0.0713× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0768× (z -20.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF500]] | +0.69 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[ZNF251]] | +0.68 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | +0.66 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MFSD14CP]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[DEXI]] | +0.64 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.63 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[GLUD1P3]] | +0.63 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[TRAPPC13]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PGS1]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[ZNF398]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.62 | +0.49 / +0.75 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | -0.61 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[ABLIM1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ATP7A]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZFP36]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 | STRING 507 |
| [[SFR1]] | -0.56 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[JUN]] | -0.55 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[FOS]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[AHR]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SPTAN1]] | -0.53 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[CLASP1-AS1]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ARHGAP26]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[USP9X]] | -0.52 | -0.39 / -0.53 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers EIF4ENIF1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR4458HG]] | B | MIR4458HG activity lowers EIF4ENIF1's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.19× higher at baseline in the lines without MIR4458HG | 0.068 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.0, 21.6); signed map (-41.1, 0.5). **Vector** length 99.1, 21.5% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +12.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.6 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -5.5 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.3 | -9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -4.6 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E nuclear import factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,436,977-31,496,108 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 4E-T, FLJ21601, Clast4, 2610509L04Rik |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRA8](https://www.uniprot.org/uniprotkb/Q9NRA8) (Eukaryotic translation initiation factor 4E transporter):

> EIF4E-binding protein that regulates translation and stability of mRNAs in processing bodies (P-bodies). Plays a key role in P-bodies to coordinate the storage of translationally inactive mRNAs in the cytoplasm and prevent their degradation. Acts as a binding platform for multiple RNA-binding proteins: promotes deadenylation of mRNAs via its interaction with the CCR4-NOT complex, and blocks decapping via interaction with eIF4E (EIF4E and EIF4E2), thereby protecting deadenylated and repressed …

**Summary**, from NCBI Gene [56478](https://www.ncbi.nlm.nih.gov/gene/56478):

> The protein encoded by this gene is a nucleocytoplasmic shuttle protein for the translation initiation factor eIF4E. This shuttle protein interacts with the importin alpha-beta complex to mediate nuclear import of eIF4E. It is predominantly cytoplasmic; its own nuclear import is regulated by a nuclear localization signal and nuclear export signals. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2009]

**Accessions** — [HGNC:16687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16687) · Entrez [56478](https://www.ncbi.nlm.nih.gov/gene/56478) · UniProt [Q9NRA8](https://www.uniprot.org/uniprotkb/Q9NRA8) · Ensembl [ENSG00000184708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184708)

## Data

Gene col 11569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11569); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11569]; `tensor/DDL_lfc|DDL_z.npy` [11569]; `embed/gene_vectors.npy` [11569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11569 or target_col == 11569). Every well: [[EIF4ENIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4ENIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
