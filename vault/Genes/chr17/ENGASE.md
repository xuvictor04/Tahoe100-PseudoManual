---
symbol: "ENGASE"
type: "gene"
col: 9445
ensembl_id: "ENSG00000167280"
name: "endo-beta-N-acetylglucosaminidase"
location: "17q25.3"
module: 2
arm: "+"
pooled_cpm: 10.94
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ENGASE

*endo-beta-N-acetylglucosaminidase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.11× (z +13.8, q 8e-41, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.908× (z -4.1, q 0.020, down in 9 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0998×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.136×; ⚠ toxic; transcription drop); [[Vortioxetine (drug)]] 5 µM in 1 line (HepG2/C3A 0.0780×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGGHG]] (+0.64, fdr 1e-05), [[PLA2G4B]] (+0.57, fdr 1e-05), [[MAP2K2]] (+0.55, fdr 1e-05); moves opposite to [[DUT]] (-0.43, fdr 4e-05), [[ACTR2]] (-0.43, fdr 7e-05), [[USP1]] (-0.42, fdr 9e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DTX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +13.8 | 8e-41 | 37/45 (HEC-1-A, BT-474, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +12.5 | 4e-33 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +10.4 | 7e-23 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +8.6 | 1e-15 | 30/47 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.07×** | +8.4 | 6e-15 | 35/46 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +7.4 | 2e-11 | 28/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.09×** | +6.4 | 1e-08 | 29/40 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +6.1 | 7e-08 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +5.4 | 4e-06 | 24/44 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.23×** | +5.1 | 2e-05 | 14/31 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.0 | 2e-05 | 9/21 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +4.9 | 6e-05 | 16/39 (NCI-H2030, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +4.4 | 6e-04 | 19/47 (SW1417, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.3 | 6e-04 | 20/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.2 | 9e-04 | 11/34 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.002 | 14/47 (A549, H4, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.003 | 17/43 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.004 | 15/46 (A498, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.023 | 14/47 (LoVo, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.034 | 11/44 (H4, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9445.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0998×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.136×; ⚠ toxic; transcription drop); [[Vortioxetine (drug)]] 5 µM in 1 line (HepG2/C3A 0.0780×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.1 | 0.020 | 9/48 (A-427, RPMI-7951, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.727×** | -3.9 | 0.027 | 12/48 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.743×** | -3.6 | 0.051 | 10/47 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.601× | -3.3 | 0.16 | 14/42 (A549, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +13.3) | — |
| [[SW480 (line)]] | alt | 8.48 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.35× (z +10.1) | — |
| [[A-427 (line)]] | wt | 9.80 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.96× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 4.76 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.5× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 9.52 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.59× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 9.24 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0780× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 8.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +10.4) | — |
| [[J82 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +9.2) | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0998× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[PANC-1 (line)]] | alt | 9.30 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +8.9) | — |
| [[A-172 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGHG]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 | same gene group |
| [[PLA2G4B]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MAP2K2]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CACFD1]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[GOLGA6L9]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SGSH]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[AHSA2P]] | +0.52 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.51 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TAF1C]] | +0.50 | +0.51 / +0.47 | both halves | 2e-05 | STRING 469 |
| [[RTN4RL2]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[DDRGK1]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[RHOT2]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUT]] | -0.43 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[ACTR2]] | -0.43 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[USP1]] | -0.42 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[DR1]] | -0.42 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[ACTL6A]] | -0.41 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[PSENEN]] | -0.40 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[TAOK1]] | -0.40 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[FBXO5]] | -0.39 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTX3]] | B | DTX3 activity raises ENGASE's level | lines that do not express DTX3 (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without DTX3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with ARID1A, SETD1B; also absent: NRIP3, UPK1A-AS1, SDK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.336). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.7, -22.9); signed map (-28.0, 1.3). **Vector** length 72.4, 12.7% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +8.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +6.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +3.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.1 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | endo-beta-N-acetylglucosaminidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,074,824-79,088,599 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21865 |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Reactome | 2 pathways, smallest: N-glycan trimming in the ER and Calnexin/Calreticulin cycle; Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFI3](https://www.uniprot.org/uniprotkb/Q8NFI3) (Cytosolic endo-beta-N-acetylglucosaminidase):

> Endoglycosidase that cleaves the beta-1,4-glycosidic bond in the N,N'-diacetylchitobiose core of oligosaccharides. Mainly catalyzes the processing of free oligosaccharides in the cytosol, converting them into molecules bearing a single N-acetylglucosamine (GlcNAc) residue. Also mediates deglycosylation of N-linked glycoproteins: instead of removing the entire N-glycan, cleaves within the glycan structure and leaves behind a single GlcNAc attached to the asparagine residue of the protein. …

**Summary**, from NCBI Gene [64772](https://www.ncbi.nlm.nih.gov/gene/64772):

> This gene encodes a cytosolic enzyme which catalyzes the hydrolysis of peptides and proteins with mannose modifications to produce free oligosaccharides. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:24622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24622) · Entrez [64772](https://www.ncbi.nlm.nih.gov/gene/64772) · UniProt [Q8NFI3](https://www.uniprot.org/uniprotkb/Q8NFI3) · Ensembl [ENSG00000167280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167280)

## Data

Gene col 9445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9445); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9445]; `tensor/DDL_lfc|DDL_z.npy` [9445]; `embed/gene_vectors.npy` [9445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9445 or target_col == 9445). Every well: [[ENGASE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENGASE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
