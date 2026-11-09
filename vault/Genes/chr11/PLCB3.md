---
symbol: "PLCB3"
type: "gene"
col: 7408
ensembl_id: "ENSG00000149782"
name: "phospholipase C beta 3"
location: "11q13.1"
module: 2
arm: "+"
pooled_cpm: 28.3
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PLCB3

*phospholipase C beta 3* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.25× (z +11.4, q 1e-27, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +7.4, q 2e-11, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.590× (z -7.7, q 5e-12, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHBP1L1]] (+0.73, fdr 7e-06), [[SBF1]] (+0.69, fdr 7e-06), [[AKT1]] (+0.69, fdr 7e-06); moves opposite to [[PIGBOS1]] (-0.62, fdr 7e-06), [[ZNF644]] (-0.61, fdr 3e-05), [[COIL]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LAMA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +11.4 | 1e-27 | 28/34 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +11.4 | 1e-27 | 33/41 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.4 | 2e-11 | 26/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.61×** | +7.0 | 4e-10 | 37/48 (RKO, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.67×** | +6.9 | 5e-10 | 27/36 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.58×** | +6.7 | 2e-09 | 32/48 (SW480, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.56×** | +6.5 | 7e-09 | 30/48 (RKO, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.7 | 6e-07 | 36/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.5 | 2e-06 | 29/48 (SW480, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +4.3 | 0.001 | 24/46 (LS 180, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +3.8 | 0.008 | 22/46 (A-427, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.6 | 0.014 | 16/48 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.037 | 15/47 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.590×** | -7.7 | 5e-12 | 30/47 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -7.7 | 5e-12 | 28/47 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -4.3 | 0.002 | 20/48 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.736×** | -4.3 | 0.002 | 24/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.779×** | -3.6 | 0.030 | 18/48 (A-172, SW 1088, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.054 | 18/48 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.797×** | -3.3 | 0.074 | 17/48 (PANC-1, BT-474, …) | inconsistent across doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.089 | 12/47 (AsPC-1, H4, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.663× | -3.1 | 0.11 | 18/48 (SNU-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.811× | -3.1 | 0.12 | 13/48 (CHP-212, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.812× | -3.0 | 0.12 | 19/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 40.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -19.4) |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.7) |
| [[LoVo (line)]] | wt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.4) |
| [[LS 180 (line)]] | wt | 40.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.3) |
| [[A498 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.0) |
| [[KATO III (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.0) |
| [[SW480 (line)]] | alt | 19.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +11.0) | — |
| [[A-172 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1L1]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[SBF1]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[AKT1]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 | pathway: G-protein beta:gamma signalling; STRING 537 |
| [[LLGL1]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ITPR3]] | +0.65 | +0.72 / +0.59 | both halves | 7e-06 | pathway: Beta-catenin independent WNT signaling; STRING 967 |
| [[SUN1]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CAPN10]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ESYT1]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SH3GLB2]] | +0.64 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ABHD17A]] | +0.64 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[NRBP2]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGBOS1]] | -0.62 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[ZNF644]] | -0.61 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[COIL]] | -0.61 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[RPP38]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.59 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[ARL14EP]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[SETD2]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[USP47]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[WARS2]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NIPBL]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[NSUN3]] | -0.58 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[EPC1]] | -0.58 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA5]] | B | LAMA5 activity raises PLCB3's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without LAMA5 | 0.052 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[PLEC]] | C | PLEC activity raises PLCB3's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.1, -22.3); signed map (-46.3, -10.4). **Vector** length 110, 27.3% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.3 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.1 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.9 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.8 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,251,530-64,269,150 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases |
| Reactome | 24 pathways, smallest: Fatty Acids bound to GPR40 (FFAR1) regulate insulin secretion; Acetylcholine regulates insulin secretion; Free fatty acids regulate insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01970](https://www.uniprot.org/uniprotkb/Q01970) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase beta-3):

> Catalyzes the production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3). Key transducer of G protein-coupled receptor signaling: activated by G(q)/G(11) G alpha proteins downstream of G protein-coupled receptors activation. In neutrophils, participates in a phospholipase C-activating N-formyl peptide-activated GPCR (G protein-coupled receptor) signaling pathway by promoting RASGRP4 activation by DAG, to promote neutrophil functional responses (By …

**Summary**, from NCBI Gene [5331](https://www.ncbi.nlm.nih.gov/gene/5331):

> This gene encodes a member of the phosphoinositide phospholipase C beta enzyme family that catalyze the production of the secondary messengers diacylglycerol and inositol 1,4,5-triphosphate from phosphatidylinositol in G-protein-linked receptor-mediated signal transduction. Alternative splicing results in multiple transcript variants.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:9056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9056) · Entrez [5331](https://www.ncbi.nlm.nih.gov/gene/5331) · UniProt [Q01970](https://www.uniprot.org/uniprotkb/Q01970) · Ensembl [ENSG00000149782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149782)

## Data

Gene col 7408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7408); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7408]; `tensor/DDL_lfc|DDL_z.npy` [7408]; `embed/gene_vectors.npy` [7408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7408 or target_col == 7408). Every well: [[PLCB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
