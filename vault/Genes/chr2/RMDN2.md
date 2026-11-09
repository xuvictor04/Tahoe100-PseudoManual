---
symbol: "RMDN2"
type: "gene"
col: 3728
ensembl_id: "ENSG00000115841"
name: "regulator of microtubule dynamics 2"
location: "2p22.2"
module: 137
arm: "+"
pooled_cpm: 10.78
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# RMDN2

*regulator of microtubule dynamics 2* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.58× (z +9.2, q 2e-17, up in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +5.0, q 2e-04, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.515× (z -9.4, q 2e-18, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C6]] (+0.68, fdr 3e-04), [[IDNK]] (+0.67, fdr 1e-04), [[RCBTB2]] (+0.63, fdr 2e-04); moves opposite to [[RRAS]] (-0.61, fdr 5e-04), [[KIAA1328]] (-0.61, fdr 1e-04), [[NBEAL1]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPIN3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.58×** | +9.2 | 2e-17 | 32/46 (A498, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 2e-04 | 20/44 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.007 | 14/46 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.8 | 0.019 | 17/39 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.7 | 0.021 | 10/27 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.052 | 10/45 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.14 | 8/44 (LoVo, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.14 | 7/46 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.24× | +3.0 | 0.16 | 12/46 (SW1417, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.515×** | -9.4 | 2e-18 | 29/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.604×** | -7.2 | 2e-10 | 24/46 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.705×** | -5.0 | 1e-04 | 20/46 (LS 180, LoVo, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -5.0 | 1e-04 | 17/43 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -4.6 | 4e-04 | 18/46 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.735×** | -4.4 | 0.001 | 18/46 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.739×** | -4.3 | 0.001 | 17/41 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.738×** | -4.2 | 0.002 | 17/39 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.763×** | -3.8 | 0.008 | 13/46 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.768×** | -3.8 | 0.010 | 10/45 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.779×** | -3.5 | 0.020 | 15/44 (SW480, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.787×** | -3.4 | 0.031 | 14/43 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -3.4 | 0.035 | 9/46 (AN3 CA, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.854× | -3.2 | 0.058 | 19/44 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.659×** | -3.1 | 0.072 | 11/45 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0842× (z -9.0) |
| [[A-427 (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 9.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 10.5 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0749× (z -10.6) |
| [[SHP-77 (line)]] | alt | 7.19 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0815× (z -10.5) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C6]] | +0.68 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[IDNK]] | +0.67 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[RCBTB2]] | +0.63 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[SPRYD4]] | +0.62 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[FAIM]] | +0.62 | +0.51 / +0.24 | both halves | 4e-04 |  |
| [[TRMT11]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.61 | +0.49 / +0.22 | both halves | 6e-04 |  |
| [[PGGT1B]] | +0.61 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TIRAP-AS1]] | +0.60 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[SPRY3]] | +0.60 | +0.57 / +0.04 | ⚠ one half (not replicated) | 0.005 |  |
| [[LINC01836]] | +0.59 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[FAM169A]] | +0.59 | +0.48 / +0.37 | both halves | 7e-05 |  |
| [[THBS4]] | +0.59 | +0.42 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAS]] | -0.61 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[KIAA1328]] | -0.61 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[NBEAL1]] | -0.61 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[CARD19]] | -0.60 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[DNAAF3]] | -0.59 | -0.39 / -0.21 | both halves | 7e-04 |  |
| [[NPHP4]] | -0.58 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[YIF1B]] | -0.57 | -0.51 / -0.03 | ⚠ one half (not replicated) | 0.006 |  |
| [[GNAI2]] | -0.57 | -0.45 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[PMM1]] | -0.56 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[METTL26]] | -0.55 | -0.46 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[ARHGEF10]] | -0.55 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[NDRG1]] | -0.55 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[SUN1]] | -0.54 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.54 | -0.24 / -0.33 | both halves | 5e-04 |  |
| [[RASSF7]] | -0.54 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPIN3]] | C | SPIN3 activity raises RMDN2's level | lines that do not express SPIN3 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without SPIN3 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IRAK2, EXO5, ZNF567; its own permutation p |
| [[MTX3]] | C | MTX3 activity raises RMDN2's level | lines that do not express MTX3 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without MTX3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.3, 17.5); signed map (30.7, -13.8). **Vector** length 65.0, 10.3% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.6 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.3 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | regulator of microtubule dynamics 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,923,187-38,067,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32954, RMD2; previously FAM82A, FAM82A1 |
| Matched by | ensembl_id |

UniProt [Q96LZ7](https://www.uniprot.org/uniprotkb/Q96LZ7) carries no function annotation.

**Summary**, from NCBI Gene [151393](https://www.ncbi.nlm.nih.gov/gene/151393):

> Enables microtubule binding activity. Located in cytosol; mitotic spindle pole; and spindle microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26567) · Entrez [151393](https://www.ncbi.nlm.nih.gov/gene/151393) · UniProt [Q96LZ7](https://www.uniprot.org/uniprotkb/Q96LZ7) · Ensembl [ENSG00000115841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115841)

## Data

Gene col 3728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3728); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3728]; `tensor/DDL_lfc|DDL_z.npy` [3728]; `embed/gene_vectors.npy` [3728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3728 or target_col == 3728). Every well: [[RMDN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMDN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
