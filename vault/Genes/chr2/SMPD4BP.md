---
symbol: "SMPD4BP"
type: "gene"
col: 7592
ensembl_id: "ENSG00000152117"
name: "sphingomyelin phosphodiesterase 4B, pseudogene"
location: "2q21.1"
module: 71
arm: "+"
pooled_cpm: 22.61
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# SMPD4BP

*sphingomyelin phosphodiesterase 4B, pseudogene* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.98× (z +11.2, q 3e-26, up in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.35× (z +10.3, q 2e-22, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.560× (z -9.5, q 1e-18, down in 30 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.720× (z -7.3, q 8e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD14CP]] (+0.70, fdr 7e-06), [[ALYREF]] (+0.65, fdr 7e-06), [[ZNF500]] (+0.65, fdr 1e-05); moves opposite to [[RFK]] (-0.59, fdr 7e-06), [[HUWE1]] (-0.58, fdr 1e-05), [[ZC3H11A]] (-0.58, fdr 9e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +11.2 | 3e-26 | 41/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.35×** | +10.3 | 2e-22 | 39/48 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +9.2 | 9e-18 | 37/46 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +8.3 | 2e-14 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 5e-07 | 25/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +5.6 | 2e-06 | 25/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 5e-05 | 23/46 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.020 | 14/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +3.1 | 0.096 | 11/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.1 | 0.096 | 10/29 (SW480, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.42× | +3.0 | 0.13 | 7/46 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7592.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.560×** | -9.5 | 1e-18 | 30/41 (NCI-H2347, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -7.4 | 4e-11 | 19/31 (HOP62, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -7.3 | 8e-11 | 34/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.773×** | -4.2 | 0.003 | 20/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.004 | 20/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.785×** | -4.0 | 0.006 | 18/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.786×** | -4.0 | 0.006 | 16/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.802×** | -3.6 | 0.021 | 15/47 (SNU-423, LOX-IMVI, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.824×** | -3.2 | 0.088 | 11/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 42.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 22.0 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[A-427 (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -13.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 20.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -8.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 9.45 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.67× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.35× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.42× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ALYREF]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZNF500]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PPIH]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NUP85]] | +0.64 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[MZT2A]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ZMYND19]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ZNF530]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SMPD4]] | +0.61 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[E4F1]] | +0.59 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SPATA33]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CDAN1]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFK]] | -0.59 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[HUWE1]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.58 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[SCOC]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SDCBP]] | -0.56 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZNF770]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SPTAN1]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[BBS10]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.53 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[AFF4]] | -0.52 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SMPD4BP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SMPD4BP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.9, -36.6); signed map (-44.7, -26.4). **Vector** length 76.2, 14.8% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +9.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.7 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | +0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase 4B, pseudogene |
| Locus type | pseudogene |
| Location | 2q21.1 — chr2:131,492,813-131,520,421 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24761) · Entrez [150776](https://www.ncbi.nlm.nih.gov/gene/150776) · Ensembl [ENSG00000152117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152117)

## Data

Gene col 7592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7592); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7592]; `tensor/DDL_lfc|DDL_z.npy` [7592]; `embed/gene_vectors.npy` [7592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7592 or target_col == 7592). Every well: [[SMPD4BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPD4BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
