---
symbol: "SULT4A1"
type: "gene"
col: 5079
ensembl_id: "ENSG00000130540"
name: "sulfotransferase family 4A member 1"
location: "22q13.31"
module: 132
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 21
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SULT4A1

*sulfotransferase family 4A member 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.05× (z +11.9, q 6e-30, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +6.9, q 9e-10, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.589× (z -4.1, q 0.028, down in 3 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.161×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.139×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H2030 0.101×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRSK2]] (+0.68, fdr 7e-06), [[PDZD4]] (+0.66, fdr 1e-05), [[MAP6]] (+0.64, fdr 7e-06); moves opposite to [[RFX3]] (-0.49, fdr 1e-04), [[LEPROT]] (-0.48, fdr 2e-04), [[MCTS1]] (-0.47, fdr 8e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KCNQ2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.05×** | +11.9 | 6e-30 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.22×** | +10.2 | 6e-22 | 2/4 (NCI-H1792, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +10.0 | 3e-21 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.9 | 9e-10 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +6.7 | 2e-09 | 2/8 (PANC-1, A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +6.2 | 5e-08 | 9/18 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.43×** | +6.0 | 2e-07 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +5.9 | 3e-07 | 1/17 (PANC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.10×** | +5.7 | 7e-07 | 2/9 (A-172, NCI-H1792) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.10×** | +5.7 | 7e-07 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.6 | 1e-06 | 1/14 (C-33 A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.72×** | +4.8 | 6e-05 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +4.5 | 2e-04 | 2/9 (SW 900, NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.5 | 3e-04 | 0/12 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 1/13 (BT-474) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.004 | 2/18 (HOP62, SW 900) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.62×** | +3.7 | 0.007 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.021 | 1/12 (NCI-H1573) | two highest doses |  |
| [[Talc (drug)]] 0.05 µM |  | **1.54×** | +3.3 | 0.023 | 0/15 | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.030 | 0/12 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.053 | 1/14 (NCI-H23) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +2.9 | 0.091 | 0/11 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5079.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.161×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.139×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H2030 0.101×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.589×** | -4.1 | 0.028 | 3/16 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.630× | -3.2 | 0.29 | 1/15 (CHP-212) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.661× | -3.2 | 0.29 | 5/16 (A-172, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.74 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -9.1) |
| [[PANC-1 (line)]] | alt | 8.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.145 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.149 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.174 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.146 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.159 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.154 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.151 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.170 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.163 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK2]] | +0.68 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PDZD4]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MAP6]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RASSF2]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 | STRING 431 |
| [[RAB6B]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.60 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[CRMP1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SEPTIN5]] | +0.57 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[SYT7]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[LHX6]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.49 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[LEPROT]] | -0.48 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[MCTS1]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[UFL1-AS1]] | -0.47 | -0.44 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ2]] | C | KCNQ2 activity raises SULT4A1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without KCNQ2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises SULT4A1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without JAKMIP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[RASGEF1A]] | C | RASGEF1A activity raises SULT4A1's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without RASGEF1A | 0.096 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.8, 40.5); signed map (25.8, 29.2). **Vector** length 26.7, 4.77% of its response variance represented; |z| ≥ 3 in 341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | sulfotransferase family 4A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:43,824,509-43,862,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SULTX3, hBR-STL-1 |
| Gene groups (HGNC) | Sulfotransferases, cytosolic |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BR01](https://www.uniprot.org/uniprotkb/Q9BR01) (Sulfotransferase 4A1):

> Atypical sulfotransferase family member with very low affinity for 3'-phospho-5'-adenylyl sulfate (PAPS) and very low catalytic activity towards L-triiodothyronine, thyroxine, estrone, p-nitrophenol, 2-naphthylamine, and 2-beta-naphthol. May have a role in the metabolism of drugs and neurotransmitters in the CNS.

**Summary**, from NCBI Gene [25830](https://www.ncbi.nlm.nih.gov/gene/25830):

> This gene encodes a member of the sulfotransferase family. The encoded protein is a brain-specific sulfotransferase believed to be involved in the metabolism of neurotransmitters. Polymorphisms in this gene may be associated with susceptibility to schizophrenia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14903) · Entrez [25830](https://www.ncbi.nlm.nih.gov/gene/25830) · UniProt [Q9BR01](https://www.uniprot.org/uniprotkb/Q9BR01) · Ensembl [ENSG00000130540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130540)

## Data

Gene col 5079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5079); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5079]; `tensor/DDL_lfc|DDL_z.npy` [5079]; `embed/gene_vectors.npy` [5079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5079 or target_col == 5079). Every well: [[SULT4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SULT4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
