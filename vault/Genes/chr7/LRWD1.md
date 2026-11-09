---
symbol: "LRWD1"
type: "gene"
col: 8412
ensembl_id: "ENSG00000161036"
name: "leucine rich repeats and WD repeat domain containing 1"
location: "7q22.1"
module: 78
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# LRWD1

*leucine rich repeats and WD repeat domain containing 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.76× (z +12.7, q 2e-34, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +9.9, q 1e-20, up in 35 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Flumatinib (mesylate) (drug)]] 5 µM in 1 line (A-172 0.0553×); [[Neratinib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0760×); [[Rifaximin (drug)]] 5 µM in 1 line (A-172 0.0715×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACD]] (+0.63, fdr 1e-05), [[CACTIN]] (+0.62, fdr 7e-06), [[ARHGDIA]] (+0.62, fdr 2e-05); moves opposite to [[ERP29]] (-0.53, fdr 1e-05), [[MBNL2]] (-0.53, fdr 1e-05), [[OSBPL1A]] (-0.52, fdr 5e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.76×** | +12.7 | 2e-34 | 43/47 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.12×** | +10.9 | 2e-25 | 42/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.9 | 1e-20 | 35/39 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.74×** | +9.7 | 4e-20 | 38/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +9.2 | 3e-18 | 25/38 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +7.9 | 4e-13 | 24/36 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.07×** | +7.0 | 3e-10 | 11/24 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.24×** | +6.9 | 3e-10 | 5/10 (SW480, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.89×** | +5.9 | 2e-07 | 1/7 (A498) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.73×** | +5.1 | 2e-05 | 8/25 (BT-474, SW480, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.65×** | +4.6 | 2e-04 | 11/36 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 15/43 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 4e-04 | 14/38 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.58×** | +4.2 | 0.001 | 15/39 (RKO, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.001 | 8/47 (HS-578T, NCI-H2030, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.003 | 14/42 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.018 | 7/44 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.044 | 3/43 (LoVo, C-33 A, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.048 | 6/39 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.067 | 4/46 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.070 | 6/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.80×** | +3.0 | 0.073 | 3/28 (PANC-1, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8412.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Flumatinib (mesylate) (drug)]] 5 µM in 1 line (A-172 0.0553×); [[Neratinib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0760×); [[Rifaximin (drug)]] 5 µM in 1 line (A-172 0.0715×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.740× | -3.1 | 0.80 | 9/47 (NCI-H1573, LS 180, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.19 | 0 | 3 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0553× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 3.67 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0760× (z -10.7) |
| [[SW480 (line)]] | alt | 5.47 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.09× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACD]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CACTIN]] | +0.62 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ARHGDIA]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[KCTD5]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RRP9]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 | same gene group |
| [[FAAP100]] | +0.60 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[SMTN]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZBTB9]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CDC42EP2]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PNP]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[WDR55]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERP29]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MBNL2]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[OSBPL1A]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NUDT13]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PPP1CB]] | -0.51 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MIR3936HG]] | -0.51 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ARL6IP5]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[QPRT]] | -0.49 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[ATP6V1A]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SCP2]] | -0.48 | -0.47 / -0.52 | both halves | 2e-05 | same gene group |
| [[GSTA4]] | -0.47 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRWD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[XKR7]] | B | XKR7 activity raises LRWD1's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.23× lower at baseline in the lines without XKR7 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[ESAM]] | C | ESAM activity raises LRWD1's level | lines that do not express ESAM (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without ESAM | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, -25.2); signed map (-5.2, 30.5). **Vector** length 51.7, 6.61% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +2.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.0 | +12.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.2 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.4 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and WD repeat domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,464,956-102,473,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K1815, ORCA, CENP-33 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UFC0](https://www.uniprot.org/uniprotkb/Q9UFC0) (Leucine-rich repeat and WD repeat-containing protein 1):

> Required for G1/S transition. Recruits and stabilizes the origin recognition complex (ORC) onto chromatin during G1 to establish pre-replication complex (preRC) and to heterochromatic sites in post-replicated cells. Binds a combination of DNA and histone methylation repressive marks on heterochromatin. Binds histone H3 and H4 trimethylation marks H3K9me3, H3K27me3 and H4K20me3 in a cooperative manner with DNA methylation. Required for silencing of major satellite repeats. May be important ORC2, …

**Summary**, from NCBI Gene [222229](https://www.ncbi.nlm.nih.gov/gene/222229):

> The protein encoded by this gene interacts with components of the origin recognition complex (ORC) and regulates the formation of the prereplicative complex. The encoded protein stabilizes the ORC and therefore aids in DNA replication. This protein is required for the G1/S phase transition of the cell cycle. In addition, the encoded protein binds to trimethylated histone H3 in heterochromatin and recruits the ORC and lysine methyltransferases, which help maintain the repressive heterochromatic …

**Accessions** — [HGNC:21769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21769) · Entrez [222229](https://www.ncbi.nlm.nih.gov/gene/222229) · UniProt [Q9UFC0](https://www.uniprot.org/uniprotkb/Q9UFC0) · Ensembl [ENSG00000161036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161036)

## Data

Gene col 8412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8412); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8412]; `tensor/DDL_lfc|DDL_z.npy` [8412]; `embed/gene_vectors.npy` [8412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8412 or target_col == 8412). Every well: [[LRWD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRWD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
