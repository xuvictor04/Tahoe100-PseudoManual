---
symbol: "ZBTB8A"
type: "gene"
col: 8295
ensembl_id: "ENSG00000160062"
name: "zinc finger and BTB domain containing 8A"
location: "1p35.1"
module: 46
arm: "+"
pooled_cpm: 25.87
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ZBTB8A

*zinc finger and BTB domain containing 8A* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +10.9, q 7e-25, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.352× (z -16.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD1]] (+0.67, fdr 5e-05), [[HACD1]] (+0.67, fdr 3e-05), [[RNF115]] (+0.67, fdr 3e-05); moves opposite to [[ALDOA]] (-0.64, fdr 4e-05), [[PGK1]] (-0.63, fdr 3e-05), [[MATCAP1]] (-0.59, fdr 5e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COBLL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.9 | 7e-25 | 35/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.7 | 4e-12 | 30/48 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.6 | 8e-04 | 23/48 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.1 | 0.005 | 19/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.011 | 18/46 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.011 | 22/47 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +3.8 | 0.011 | 16/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.5 | 0.037 | 12/48 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.037 | 17/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.037 | 14/47 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +3.3 | 0.049 | 10/48 (RPMI-7951, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.11 | 15/47 (Hs 766T, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -16.5 | 0e+00 | 44/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.372×** | -15.7 | 0e+00 | 42/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.396×** | -14.7 | 0e+00 | 42/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.466×** | -6.3 | 4e-08 | 26/48 (HS-578T, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.686×** | -6.0 | 3e-07 | 26/48 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -5.8 | 7e-07 | 30/48 (NCI-H2030, A-427, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -5.5 | 3e-06 | 30/48 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[NG25 (drug)]] 5 µM |  | **0.561×** | -4.8 | 1e-04 | 25/45 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.005 | 20/47 (HEC-1-A, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.622×** | -3.9 | 0.005 | 19/46 (NCI-H1573, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.781×** | -3.9 | 0.005 | 20/42 (Panc 03.27, NCI-H2030, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.7 | 0.009 | 18/48 (A498, LS 180, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.791×** | -3.7 | 0.010 | 23/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.795×** | -3.6 | 0.012 | 22/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.797×** | -3.6 | 0.013 | 20/47 (NCI-H23, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.9 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.6) |
| [[LoVo (line)]] | wt | 49.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -20.2) |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -13.6) |
| [[A-427 (line)]] | wt | 38.8 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -15.0) |
| [[A498 (line)]] | wt | 23.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.3) |
| [[SW480 (line)]] | alt | 24.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -15.5) |
| [[A549 (line)]] | wt | 24.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.167× (z -13.3) |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.214× (z -11.4) |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -11.0) |
| [[KATO III (line)]] | alt | 23.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.213× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.300× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 24.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.9) |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -10.4) |
| [[AN3 CA (line)]] | alt | 56.4 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.0759× (z -11.3) |
| [[J82 (line)]] | alt | 30.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -11.3) |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.251× (z -9.7) |
| [[H4 (line)]] | wt | 18.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.135× (z -8.7) |
| [[HOP62 (line)]] | alt | 31.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -8.8) |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.261× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.205× (z -8.9) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -9.7) |
| [[RKO (line)]] | wt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD1]] | +0.67 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[HACD1]] | +0.67 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[RNF115]] | +0.67 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[MTG2]] | +0.66 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZNF425]] | +0.66 | +0.60 / +0.48 | both halves | 2e-05 | same gene group |
| [[STARD7-AS1]] | +0.66 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[HOXC8]] | +0.65 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RNF135]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF785]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 | same gene group |
| [[LARP1B]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.65 | +0.55 / +0.35 | both halves | 1e-04 | same gene group |
| [[ATE1OSP]] | +0.65 | +0.59 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDOA]] | -0.64 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[PGK1]] | -0.63 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[MATCAP1]] | -0.59 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[RALGAPA2]] | -0.57 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[KCTD17]] | -0.56 | -0.40 / -0.28 | both halves | 3e-04 | same gene group |
| [[HDAC1]] | -0.56 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[TGOLN2]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CYB5R4]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[FCHO1]] | -0.55 | -0.45 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[CDK18]] | -0.55 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[HPSE]] | -0.55 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[BAIAP2-DT]] | -0.54 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[AGO1]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COBLL1]] | B | COBLL1 activity lowers ZBTB8A's level | lines that do not express COBLL1 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without COBLL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LRRCC1, DSG2; maybe low, not absent |
| [[HACD1]] | B | HACD1 activity raises ZBTB8A's level | lines that do not express HACD1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without HACD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLSTN3, CDR2L, PIM1; its own permutation p |
| [[LRFN4]] | B | LRFN4 activity raises ZBTB8A's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without LRFN4 | 0.078 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[SLC2A1]] | C | SLC2A1 activity lowers ZBTB8A's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.8, 15.6); signed map (22.5, -20.1). **Vector** length 110, 27.5% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +3.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.1 | -16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.6 | -15.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.7 | -14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,539,427-32,605,941 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BOZF1, FLJ90065, ZNF916A; previously ZBTB8 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BR9](https://www.uniprot.org/uniprotkb/Q96BR9) (Zinc finger and BTB domain-containing protein 8A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [653121](https://www.ncbi.nlm.nih.gov/gene/653121):

> Enables several functions, including DNA-binding transcription repressor activity, RNA polymerase II-specific; RNA polymerase II-specific DNA-binding transcription factor binding activity; and transcription coactivator binding activity. Involved in negative regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24172) · Entrez [653121](https://www.ncbi.nlm.nih.gov/gene/653121) · UniProt [Q96BR9](https://www.uniprot.org/uniprotkb/Q96BR9) · Ensembl [ENSG00000160062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160062)

## Data

Gene col 8295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8295); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8295]; `tensor/DDL_lfc|DDL_z.npy` [8295]; `embed/gene_vectors.npy` [8295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8295 or target_col == 8295). Every well: [[ZBTB8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
