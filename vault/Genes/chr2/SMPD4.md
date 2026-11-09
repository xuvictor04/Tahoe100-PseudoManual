---
symbol: "SMPD4"
type: "gene"
col: 5889
ensembl_id: "ENSG00000136699"
name: "sphingomyelin phosphodiesterase 4"
location: "2q21.1"
module: 71
arm: "+"
pooled_cpm: 29.96
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# SMPD4

*sphingomyelin phosphodiesterase 4* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.39× (z +13.3, q 1e-37, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.724× (z -7.9, q 2e-12, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIDO1]] (+0.76, fdr 7e-06), [[SENP3]] (+0.69, fdr 7e-06), [[ELAVL1]] (+0.69, fdr 7e-06); moves opposite to [[BTG1]] (-0.70, fdr 1e-05), [[USP53]] (-0.60, fdr 2e-05), [[DYNLL1]] (-0.58, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.39×** | +13.3 | 1e-37 | 46/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.61×** | +11.5 | 3e-28 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +10.7 | 3e-24 | 38/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +10.4 | 4e-23 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +7.4 | 2e-11 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.5 | 9e-09 | 29/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +6.0 | 2e-07 | 24/42 (SW 900, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +5.9 | 2e-07 | 26/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.8 | 5e-07 | 25/48 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.5 | 3e-06 | 17/33 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.3 | 9e-04 | 23/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.7 | 0.010 | 20/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.044 | 6/48 (BT-474, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.20× | +3.0 | 0.094 | 15/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.100 | 5/48 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5889.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.724×** | -7.9 | 2e-12 | 39/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -4.3 | 0.006 | 24/48 (CHP-212, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.789×** | -4.1 | 0.008 | 20/48 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.799×** | -3.9 | 0.014 | 22/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.813×** | -3.6 | 0.040 | 15/48 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.824×** | -3.4 | 0.075 | 13/47 (SW 900, A-172, …) | two highest doses |  |
| [[Mozavaptan (drug)]] 0.05 µM |  | **0.814×** | -3.3 | 0.079 | 14/47 (BT-474, HS-578T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.880× | -3.2 | 0.11 | 12/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.3 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.21× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.07× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 25.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 48.3 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.48× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.09× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 59.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -9.0) |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0919× (z -11.4) |
| [[HCT15 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.224× (z -9.6) |
| [[LoVo (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[LOX-IMVI (line)]] | wt | 25.2 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.27× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.09× (z +9.5) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.2) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A-172 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIDO1]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[SENP3]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ELAVL1]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RBM14-RBM4]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[RNPS1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[NDOR1]] | +0.64 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[CCAR2]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 | STRING 445 |
| [[TOPBP1]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[CENPO]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NCAPH2]] | +0.62 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[TMEM248]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | -0.70 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[USP53]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[DYNLL1]] | -0.58 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[RALGAPA1]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.57 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.57 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[ATF4]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[METTL23]] | -0.57 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.57 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[H3-3B]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[SOX4]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TMEM205]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SMPD4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[BMP2]] | B | BMP2 activity lowers SMPD4's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.14× higher at baseline in the lines without BMP2 | 0.071 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[MIR4307HG]] | B | MIR4307HG activity lowers SMPD4's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.29× higher at baseline in the lines without MIR4307HG | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.5, -29.4); signed map (-25.0, -45.6). **Vector** length 77.7, 15.6% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.5 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,151,392-130,182,750 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20297, FLJ20756, nSMase-3, KIAA1418, NSMASE3, NET13 |
| Reactome | 4 pathways, smallest: Glycosphingolipid catabolism; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXE4](https://www.uniprot.org/uniprotkb/Q9NXE4) (Sphingomyelin phosphodiesterase 4):

> Catalyzes the hydrolysis of membrane sphingomyelin to form phosphorylcholine and ceramide. It has a relevant role in the homeostasis of membrane sphingolipids, thereby influencing membrane integrity, and endoplasmic reticulum organization and function. May sensitize cells to DNA damage-induced apoptosis. In skeletal muscle, mediates TNF-stimulated oxidant production (By similarity).

**Summary**, from NCBI Gene [55627](https://www.ncbi.nlm.nih.gov/gene/55627):

> The protein encoded by this gene is a sphingomyelinase that catalyzes the hydrolysis of membrane sphingomyelin to form phosphorylcholine and ceramide. This gene is activated by DNA damage, cellular stress, and tumor necrosis factor, but it is downregulated by wild-type p53. The encoded protein localizes to the endoplasmic reticulum and Golgi network. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:32949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32949) · Entrez [55627](https://www.ncbi.nlm.nih.gov/gene/55627) · UniProt [Q9NXE4](https://www.uniprot.org/uniprotkb/Q9NXE4) · Ensembl [ENSG00000136699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136699)

## Data

Gene col 5889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5889); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5889]; `tensor/DDL_lfc|DDL_z.npy` [5889]; `embed/gene_vectors.npy` [5889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5889 or target_col == 5889). Every well: [[SMPD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
