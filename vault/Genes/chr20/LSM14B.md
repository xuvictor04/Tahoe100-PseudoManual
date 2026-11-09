---
symbol: "LSM14B"
type: "gene"
col: 7401
ensembl_id: "ENSG00000149657"
name: "LSM family member 14B"
location: "20q13.33"
module: 60
arm: "-"
pooled_cpm: 24.03
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# LSM14B

*LSM family member 14B* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.57× (z +8.6, q 2e-15, up in 30 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.68× (z +5.2, q 3e-05, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.858× (z -4.1, q 0.024, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 0.206×, LOX-IMVI 0.282×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.324×; ⚠ cell-cycle shift, explains ~65% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GID8]] (+0.64, fdr 7e-06), [[PARP6]] (+0.60, fdr 7e-06), [[YY1AP1]] (+0.59, fdr 1e-05); moves opposite to [[PSMD14]] (-0.57, fdr 3e-05), [[ATP13A3-DT]] (-0.57, fdr 2e-05), [[TXN]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASPH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.6 | 2e-15 | 30/43 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +8.6 | 2e-15 | 35/46 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +6.8 | 2e-09 | 26/47 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.3 | 5e-08 | 21/36 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +5.2 | 3e-05 | 20/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +4.8 | 1e-04 | 22/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 2e-04 | 18/45 (hTERT-HPNE, HepG2/C3A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +4.6 | 3e-04 | 18/47 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 4e-04 | 16/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.008 | 16/46 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.21×** | +3.7 | 0.013 | 17/46 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.034 | 10/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +3.0 | 0.11 | 13/48 (RKO, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7401.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 0.206×, LOX-IMVI 0.282×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.324×; ⚠ cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.1 | 0.024 | 17/48 (KATO III, SW480, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.826×** | -3.6 | 0.072 | 13/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.072 | 18/47 (SW480, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.833×** | -3.5 | 0.072 | 13/48 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.839× | -3.3 | 0.098 | 8/47 (KATO III, LS 180, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.11 | 7/48 (SW1417, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -9.1) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GID8]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PARP6]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[YY1AP1]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[NISCH]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[HSDL1]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MAN1B1]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CNTROB]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[HNRNPUL2]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[PPP1R37]] | +0.51 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[ARNT]] | +0.51 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[GET4]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD14]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ATP13A3-DT]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[TXN]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PRDX1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[OAF]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[HSP90AA1]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[HSPE1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CALCRL]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[BICD1]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CCT4]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LINC01204]] | -0.49 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[HSP90AA2P]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASPH]] | B | ASPH activity lowers LSM14B's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without ASPH | 0.008 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[CPT1B]] | C | CPT1B activity lowers LSM14B's level | lines that do not express CPT1B (3) vs lines expressing it (47) | 1.51× higher at baseline in the lines without CPT1B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, FRRS1, ENSG00000266385; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.2, -10.6); signed map (-9.9, 3.1). **Vector** length 69.5, 11.4% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -3.7 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | LSM family member 14B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,122,461-62,135,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FT005, bA11M20.3, FLJ25473, LSM13, RAP55B; previously C20orf40, FAM61B |
| Gene groups (HGNC) | LSm proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX40](https://www.uniprot.org/uniprotkb/Q9BX40) (Protein LSM14 homolog B):

> mRNA-binding protein essential for female fertility, oocyte meiotic maturation and the assembly of MARDO (mitochondria-associated ribonucleoprotein domain), a membraneless compartment that stores maternal mRNAs in oocytes. Ensures the proper accumulation and clearance of mRNAs essential for oocyte meiotic maturation and the normal progression from Meiosis I to Meiosis II in oocytes. Promotes the translation of some oogenesis-related mRNAs. Regulates the expression and/or localization of some …

**Summary**, from NCBI Gene [149986](https://www.ncbi.nlm.nih.gov/gene/149986):

> Enables RNA binding activity. Predicted to be involved in several processes, including maternal mRNA clearance; meiotic cell cycle process involved in oocyte maturation; and ovarian follicle development. Predicted to be located in cytoplasmic ribonucleoprotein granule. Predicted to be part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15887) · Entrez [149986](https://www.ncbi.nlm.nih.gov/gene/149986) · UniProt [Q9BX40](https://www.uniprot.org/uniprotkb/Q9BX40) · Ensembl [ENSG00000149657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149657)

## Data

Gene col 7401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7401); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7401]; `tensor/DDL_lfc|DDL_z.npy` [7401]; `embed/gene_vectors.npy` [7401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7401 or target_col == 7401). Every well: [[LSM14B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM14B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
