---
symbol: "SPAG7"
type: "gene"
col: 1673
ensembl_id: "ENSG00000091640"
name: "sperm associated antigen 7"
location: "17p13.2"
module: 38
arm: "+"
pooled_cpm: 26.8
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SPAG7

*sperm associated antigen 7* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +10.3, q 5e-22, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.399× (z -11.4, q 4e-27, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC41]] (+0.67, fdr 5e-05), [[ZNF547]] (+0.65, fdr 1e-05), [[TIRAP]] (+0.64, fdr 2e-05); moves opposite to [[PHF6]] (-0.58, fdr 4e-05), [[HLTF]] (-0.57, fdr 2e-04), [[MED14]] (-0.56, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARHGDIB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +10.3 | 5e-22 | 37/48 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.3 | 0.005 | 20/43 (A549, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.7 | 0.043 | 16/46 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.075 | 17/48 (COLO 205, C32, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.4 | 0.082 | 19/48 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 1.60× | +3.0 | 0.21 | 18/47 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.28× | +3.0 | 0.21 | 18/47 (HS-578T, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.399×** | -11.4 | 4e-27 | 45/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.420×** | -10.7 | 2e-24 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.472×** | -9.3 | 3e-18 | 46/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.520×** | -8.1 | 7e-14 | 43/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.684×** | -6.7 | 3e-09 | 34/48 (SW1417, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.438×** | -5.3 | 9e-06 | 34/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.748×** | -5.1 | 3e-05 | 30/47 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.664×** | -5.1 | 3e-05 | 30/48 (CHP-212, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -4.6 | 2e-04 | 30/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.684×** | -4.5 | 3e-04 | 25/47 (A-427, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.755×** | -3.5 | 0.025 | 17/47 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.771×** | -3.2 | 0.056 | 17/48 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 33.8 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.236× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.270× (z -9.2) |
| [[PANC-1 (line)]] | alt | 34.1 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.195× (z -14.9) |
| [[A498 (line)]] | wt | 50.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.276× (z -11.3) |
| [[SW48 (line)]] | wt | 58.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.177× (z -9.5) |
| [[HS-578T (line)]] | alt | 41.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.265× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 26.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.329× (z -8.7) |
| [[A-427 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -11.5) |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0787× (z -8.9) |
| [[HOP62 (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.181× (z -9.0) |
| [[SW480 (line)]] | alt | 37.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.3) | — |
| [[A-172 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC41]] | +0.67 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[ZNF547]] | +0.65 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.64 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NOXRED1]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NRSN2-AS1]] | +0.64 | +0.40 / +0.65 | both halves | 4e-05 |  |
| [[SYCE1L]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TMEM267]] | +0.63 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[TRIM39]] | +0.62 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RAB4B]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PSMB5]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PGLS-DT]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MON1B]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[HLTF]] | -0.57 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[MED14]] | -0.56 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[LIFR]] | -0.55 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TGOLN2]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[HPSE]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PDHB]] | -0.52 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[HDAC1]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[TMX1]] | -0.52 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CDCA7L]] | -0.52 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SLC44A1]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[EFR3A]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity lowers SPAG7's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.40× higher at baseline in the lines without ARHGDIB | 0.036 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[SLC44A1]] | B | SLC44A1 activity lowers SPAG7's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 1.44× higher at baseline in the lines without SLC44A1 | 0.041 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |
| [[ZNF785]] | B | ZNF785 activity lowers SPAG7's level | lines that do not express ZNF785 (9) vs lines expressing it (41) | 1.47× higher at baseline in the lines without ZNF785 | 0.055 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, BDH1, PARP8 |
| [[NUP62CL]] | B | NUP62CL activity lowers SPAG7's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.22× higher at baseline in the lines without NUP62CL | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, -20.9); signed map (5.6, 0.3). **Vector** length 93.6, 22.9% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +10.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.3 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -8.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.0 | -1.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,959,226-4,967,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FSA-1, ACRP, MGC20134 |
| Matched by | ensembl_id |

UniProt [O75391](https://www.uniprot.org/uniprotkb/O75391) carries no function annotation.

**Summary**, from NCBI Gene [9552](https://www.ncbi.nlm.nih.gov/gene/9552):

> Predicted to enable nucleic acid binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11216) · Entrez [9552](https://www.ncbi.nlm.nih.gov/gene/9552) · UniProt [O75391](https://www.uniprot.org/uniprotkb/O75391) · Ensembl [ENSG00000091640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091640)

## Data

Gene col 1673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1673); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1673]; `tensor/DDL_lfc|DDL_z.npy` [1673]; `embed/gene_vectors.npy` [1673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1673 or target_col == 1673). Every well: [[SPAG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
