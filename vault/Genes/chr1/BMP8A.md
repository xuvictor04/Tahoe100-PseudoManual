---
symbol: "BMP8A"
type: "gene"
col: 11435
ensembl_id: "ENSG00000183682"
name: "bone morphogenetic protein 8a"
location: "1p34.3"
module: 47
arm: "+"
pooled_cpm: 3.0
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# BMP8A

*bone morphogenetic protein 8a* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.96× (z +17.1, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.533× (z -6.0, q 1e-06, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A3GALT2]] (+0.79, fdr 7e-06), [[MSANTD1]] (+0.71, fdr 7e-06), [[SPTBN5]] (+0.71, fdr 7e-06); moves opposite to [[CFAP418]] (-0.55, fdr 5e-05), [[CASD1]] (-0.53, fdr 1e-04), [[COQ9]] (-0.51, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KCNK13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.96×** | +17.1 | 0e+00 | 38/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.53×** | +16.3 | 0e+00 | 36/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.48×** | +11.9 | 2e-30 | 33/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +10.5 | 1e-23 | 2/2 (HS-578T, HOP62) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +10.0 | 2e-21 | 4/5 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +9.9 | 5e-21 | 8/15 (HS-578T, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +7.4 | 2e-11 | 23/43 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +7.1 | 8e-11 | 7/17 (RPMI-7951, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +6.4 | 7e-09 | 11/36 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +6.2 | 3e-08 | 22/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.1 | 5e-08 | 13/35 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +4.8 | 7e-05 | 14/46 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.60×** | +4.3 | 9e-04 | 10/40 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +4.1 | 0.001 | 7/43 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.008 | 6/28 (LS 180, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.045 | 5/25 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.070 | 4/31 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.533×** | -6.0 | 1e-06 | 19/44 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -5.1 | 8e-05 | 20/40 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.607×** | -4.8 | 4e-04 | 17/40 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.627×** | -4.5 | 0.001 | 17/38 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.639×** | -4.3 | 0.002 | 12/45 (C-33 A, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.692×** | -3.4 | 0.068 | 10/40 (A-427, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.706×** | -3.3 | 0.073 | 6/40 (C-33 A, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -3.3 | 0.079 | 9/45 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.719× | -3.2 | 0.10 | 13/42 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vandetanib (drug)]] 5 µM |  | 0.725× | -3.1 | 0.12 | 10/43 (NCI-H1573, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.24 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 53.5× (z +13.3) ⚠ toxic; transcription drop | [[Talc (drug)]] 0.05 µM 0.0662× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 5.68 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0866× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~6% of this change · without an alert: [[Penfluridol (drug)]] 0.5 µM 0.116× (z -9.1) |
| [[PANC-1 (line)]] | alt | 1.87 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 17.8× (z +9.8) | — |
| [[SW480 (line)]] | alt | 2.63 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.3× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 2.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.1× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 4.72 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.21× (z +8.6) | — |
| [[A-172 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.930 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A3GALT2]] | +0.79 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MSANTD1]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[PTCH2]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[FERMT3]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.67 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[CSPG5]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[NTRK1]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[LAT2]] | +0.65 | +0.68 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP418]] | -0.55 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CASD1]] | -0.53 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[COQ9]] | -0.51 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK13]] | B | KCNK13 activity raises BMP8A's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without KCNK13 | 0.096 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[ROPN1L]] | C | ROPN1L activity raises BMP8A's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without ROPN1L | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, -15.2); signed map (16.3, 15.2). **Vector** length 62.8, 9.14% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +17.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +16.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 8a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:39,491,636-39,529,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OP-2, Op2 |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5Y6](https://www.uniprot.org/uniprotkb/Q7Z5Y6) (Bone morphogenetic protein 8A):

> Induces cartilage and bone formation. May be the osteoinductive factor responsible for the phenomenon of epithelial osteogenesis. Plays a role in calcium regulation and bone homeostasis (By similarity). Signaling protein involved in regulation of thermogenesis and energy balance. Proposed to increase the peripheral response of brown adipose tissue (BAT) to adrenergic stimulation while acting centrally in the hypothalamus to increase sympathetic output to BAT.; Growth factor of the TGF-beta …

**Summary**, from NCBI Gene [353500](https://www.ncbi.nlm.nih.gov/gene/353500):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. This protein may play a role in development of the reproductive system. This gene may have arose from a gene …

**Accessions** — [HGNC:21650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21650) · Entrez [353500](https://www.ncbi.nlm.nih.gov/gene/353500) · UniProt [Q7Z5Y6](https://www.uniprot.org/uniprotkb/Q7Z5Y6) · Ensembl [ENSG00000183682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183682)

## Data

Gene col 11435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11435); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11435]; `tensor/DDL_lfc|DDL_z.npy` [11435]; `embed/gene_vectors.npy` [11435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11435 or target_col == 11435). Every well: [[BMP8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
