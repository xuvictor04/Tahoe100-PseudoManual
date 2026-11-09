---
symbol: "OGFOD2"
type: "gene"
col: 3219
ensembl_id: "ENSG00000111325"
name: "2-oxoglutarate and iron dependent oxygenase domain containing 2"
location: "12q24.31"
module: 107
arm: "+"
pooled_cpm: 3.71
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# OGFOD2

*2-oxoglutarate and iron dependent oxygenase domain containing 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +8.2, q 9e-14, up in 27 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -9.1, q 4e-17, down in 24 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH6]] (+0.67, fdr 7e-06), [[U2AF1L4]] (+0.65, fdr 2e-05), [[XAB2]] (+0.64, fdr 1e-05); moves opposite to [[NAB1]] (-0.53, fdr 2e-04), [[SERBP1]] (-0.52, fdr 1e-04), [[CPT1A]] (-0.51, fdr 2e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.2 | 9e-14 | 27/37 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.2 | 9e-14 | 3/6 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +6.6 | 9e-09 | 10/22 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +5.3 | 2e-05 | 1/8 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.9 | 1e-04 | 8/19 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.4 | 8e-04 | 12/45 (HOP62, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 1e-03 | 6/31 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.005 | 3/46 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.012 | 13/36 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.012 | 7/36 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +3.6 | 0.016 | 8/31 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.4 | 0.029 | 0/7 | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.029 | 7/36 (PANC-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.029 | 4/21 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.4 | 0.029 | 4/22 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.044 | 6/41 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.058 | 4/43 (A-427, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -9.1 | 4e-17 | 24/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.455×** | -8.1 | 1e-13 | 24/44 (SHP-77, HT-29, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.482×** | -7.5 | 8e-12 | 25/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -5.0 | 8e-05 | 15/34 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.407×** | -4.9 | 1e-04 | 15/41 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -4.8 | 1e-04 | 17/44 (LoVo, Hs 766T, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -4.6 | 4e-04 | 12/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -4.4 | 6e-04 | 18/36 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.652×** | -4.3 | 0.001 | 9/42 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.726× | -3.1 | 0.12 | 9/44 (NCI-H460, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.82 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0401× (z -14.7) |
| [[C-33 A (line)]] | alt | 5.20 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0527× (z -8.6) |
| [[HOP62 (line)]] | alt | 2.78 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0868× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 3.19 | 0 | 1 | — | [[Darolutamide (drug)]] 0.5 µM 0.0517× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 2.94 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0573× (z -9.4) |
| [[PANC-1 (line)]] | alt | 6.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.7) |
| [[SHP-77 (line)]] | alt | 3.62 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0506× (z -8.5) |
| [[SW480 (line)]] | alt | 4.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH6]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[U2AF1L4]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[XAB2]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[GTF3C5]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SPAG4]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[LYSMD1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ABCB6]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[BABAM1]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[VIPAS39]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[EGFL8]] | +0.58 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[TRMT2A]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 | STRING 805 |
| [[FAHD2A]] | +0.57 | +0.39 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAB1]] | -0.53 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[SERBP1]] | -0.52 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[CPT1A]] | -0.51 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[ACOT9]] | -0.50 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[CALM2]] | -0.49 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[CHML]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[JUNB]] | -0.47 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[PTBP3]] | -0.47 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[DNAH14]] | -0.47 | -0.26 / -0.47 | both halves | 3e-04 |  |
| [[ROCK2]] | -0.46 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[BCAP29]] | -0.46 | -0.26 / -0.51 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OGFOD2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.6, -14.8); signed map (-23.1, 0.8). **Vector** length 46.0, 5.22% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | 2-oxoglutarate and iron dependent oxygenase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,974,580-122,980,043 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13491, FLJ37501 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Matched by | ensembl_id |

UniProt [Q6N063](https://www.uniprot.org/uniprotkb/Q6N063) carries no function annotation.

**Summary**, from NCBI Gene [79676](https://www.ncbi.nlm.nih.gov/gene/79676):

> Predicted to enable several functions, including L-ascorbic acid binding activity; dioxygenase activity; and iron ion binding activity. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25823) · Entrez [79676](https://www.ncbi.nlm.nih.gov/gene/79676) · UniProt [Q6N063](https://www.uniprot.org/uniprotkb/Q6N063) · Ensembl [ENSG00000111325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111325)

## Data

Gene col 3219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3219); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3219]; `tensor/DDL_lfc|DDL_z.npy` [3219]; `embed/gene_vectors.npy` [3219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3219 or target_col == 3219). Every well: [[OGFOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGFOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
