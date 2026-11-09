---
symbol: "MDFIC"
type: "gene"
col: 5674
ensembl_id: "ENSG00000135272"
name: "MyoD family inhibitor domain containing"
location: "7q31.1-q31.2"
module: 143
arm: "+"
pooled_cpm: 34.48
n_lines_expressing: 38
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# MDFIC

*MyoD family inhibitor domain containing* — 7q31.1-q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.38× (z +7.9, q 1e-12, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.324× (z -19.5, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF618]] (+0.64, fdr 1e-05), [[DZIP1L]] (+0.57, fdr 6e-05), [[PRTFDC1]] (+0.57, fdr 4e-05); moves opposite to [[LINC02649]] (-0.61, fdr 1e-05), [[HM13]] (-0.57, fdr 4e-05), [[SLC2A3]] (-0.55, fdr 5e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRC]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01393]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +7.9 | 1e-12 | 23/36 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.1 | 4e-07 | 16/30 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.2 | 3e-05 | 20/36 (C32, NCI-H2030, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.65×** | +4.5 | 8e-04 | 18/35 (C32, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.0 | 0.008 | 12/36 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.23 | 7/36 (C32, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.324×** | -19.5 | 0e+00 | 36/36 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.342×** | -18.6 | 0e+00 | 35/36 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.350×** | -18.2 | 0e+00 | 33/36 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -17.1 | 0e+00 | 21/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.570×** | -9.7 | 3e-20 | 26/36 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.595×** | -9.0 | 2e-17 | 32/36 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -8.4 | 4e-15 | 24/35 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.753×** | -4.9 | 7e-05 | 18/35 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.594×** | -4.7 | 2e-04 | 17/36 (LS 180, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.597×** | -4.7 | 2e-04 | 18/36 (C32, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.768×** | -4.6 | 3e-04 | 15/36 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -4.5 | 4e-04 | 19/36 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.1 | 0.001 | 11/36 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.811×** | -3.6 | 0.012 | 13/36 (SW 1088, LS 180, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.680×** | -3.5 | 0.018 | 14/36 (HEC-1-A, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.687×** | -3.4 | 0.024 | 11/36 (HOP62, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.041 | 9/36 (LoVo, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -15.5) |
| [[A498 (line)]] | wt | 59.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.5) |
| [[C32 (line)]] | wt | 143 | 4 (3 ⚠) | 1 | [[Ponatinib (drug)]] 5 µM 4.18× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.7) |
| [[HOP62 (line)]] | alt | 50.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.5) |
| [[Hs 766T (line)]] | wt | 39.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -12.2) |
| [[J82 (line)]] | alt | 39.8 | 1 | 4 | [[Selinexor (drug)]] 5 µM 2.01× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.219× (z -14.0) |
| [[LoVo (line)]] | wt | 41.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.6) |
| [[LS 180 (line)]] | wt | 71.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 39.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.9) |
| [[A549 (line)]] | wt | 33.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 72.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.214× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 33.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 71.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 49.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 43.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0913× (z -19.5) |
| [[SW 900 (line)]] | alt | 44.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -9.0) |
| [[H4 (line)]] | wt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 9.51 | 0 | 2 | — | [[IQ 1 (drug)]] 0.5 µM 0.0575× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.1) |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -9.2) |
| [[A-172 (line)]] | wt | 30.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.271× (z -9.3) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.366× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 63.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 95.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.2) |
| [[PANC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.84× (z +10.4) | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0435× (z -9.3) |
| [[AN3 CA (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF618]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[DZIP1L]] | +0.57 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[PRTFDC1]] | +0.57 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[CNTLN]] | +0.57 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[USP13]] | +0.57 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ZNF532]] | +0.56 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[SLC35G1]] | +0.55 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[ZNF236]] | +0.54 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FIGN]] | +0.54 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[NNT]] | +0.54 | +0.48 / +0.36 | both halves | 1e-04 |  |
| [[DLG5]] | +0.53 | +0.32 / +0.49 | both halves | 1e-04 |  |
| [[LINC01139]] | +0.52 | +0.47 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02649]] | -0.61 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[HM13]] | -0.57 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SLC2A3]] | -0.55 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SLC35E1]] | -0.54 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[PTPRH]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CFDP1]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TRPT1]] | -0.53 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[ATG101]] | -0.52 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[ARFGEF3]] | -0.52 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[PRKRIP1]] | -0.51 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[COPE]] | -0.51 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[OSBP]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRC]] | B | SRC activity lowers MDFIC's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC01393]] | C | LINC01393 activity raises MDFIC's level | lines that do not express LINC01393 (13) vs lines expressing it (37) | 7.38× lower at baseline in the lines without LINC01393 | 0.004 | ⚠ within organs, on part of the lines; also absent: MDFIC, RGS2, DPYD; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01393]] | C | MDFIC activity raises LINC01393's level | lines that do not express MDFIC (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without MDFIC | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01393, AFAP1L1, CAV1; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.452). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.8, 4.8); signed map (20.1, -33.6). **Vector** length 94.3, 23.3% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.7 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -19.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -18.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -18.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MyoD family inhibitor domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1-q31.2 — chr7:114,922,094-115,019,917 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HIC, MDFIC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1T7](https://www.uniprot.org/uniprotkb/Q9P1T7) (MyoD family inhibitor domain-containing protein):

> Required to control the activity of various transcription factors through their sequestration in the cytoplasm. Retains nuclear Zic proteins ZIC1, ZIC2 and ZIC3 in the cytoplasm and inhibits their transcriptional activation (By similarity). Modulates the expression from cellular promoters. Binds to the axin complex, resulting in an increase in the level of free beta-catenin. Affects axin regulation of the WNT and JNK signaling pathways. Involved in the development of lymphatic vessel valves (By …

**Summary**, from NCBI Gene [29969](https://www.ncbi.nlm.nih.gov/gene/29969):

> This gene product is a member of a family of proteins characterized by a specific cysteine-rich C-terminal domain, which is involved in transcriptional regulation of viral genome expression. Alternative translation initiation from an upstream non-AUG (GUG), and an in-frame, downstream AUG codon, results in the production of two isoforms, p40 and p32, respectively, which have different subcellular localization; p32 is mainly found in the cytoplasm, whereas p40 is targeted to the nucleolus. Both …

**Accessions** — [HGNC:28870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28870) · Entrez [29969](https://www.ncbi.nlm.nih.gov/gene/29969) · UniProt [Q9P1T7](https://www.uniprot.org/uniprotkb/Q9P1T7) · Ensembl [ENSG00000135272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135272)

## Data

Gene col 5674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5674); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5674]; `tensor/DDL_lfc|DDL_z.npy` [5674]; `embed/gene_vectors.npy` [5674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5674 or target_col == 5674). Every well: [[MDFIC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDFIC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
