---
symbol: "MSANTD2"
type: "gene"
col: 4185
ensembl_id: "ENSG00000120458"
name: "Myb/SANT DNA binding domain containing 2"
location: "11q24.2"
module: 124
arm: "+"
pooled_cpm: 41.86
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# MSANTD2

*Myb/SANT DNA binding domain containing 2* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +8.7, q 2e-15, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.568× (z -8.8, q 6e-16, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNT1]] (+0.71, fdr 1e-05), [[PRDM5]] (+0.71, fdr 2e-05), [[AVEN]] (+0.70, fdr 1e-05); moves opposite to [[STARD5]] (-0.66, fdr 3e-05), [[GALM]] (-0.64, fdr 1e-05), [[RAB3A]] (-0.63, fdr 8e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TEC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.7 | 2e-15 | 35/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.5 | 0.002 | 24/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.004 | 23/47 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.4 | 0.099 | 18/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.22× | +3.1 | 0.19 | 8/48 (RKO, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.24× | +3.1 | 0.21 | 18/42 (A498, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -8.8 | 6e-16 | 41/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.632×** | -7.2 | 2e-10 | 40/48 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -6.8 | 3e-09 | 38/48 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.696×** | -5.7 | 2e-06 | 31/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.743×** | -4.6 | 4e-04 | 26/46 (MIA PaCa-2, SW48, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.595×** | -4.2 | 0.002 | 27/44 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.009 | 23/48 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.746× | -3.2 | 0.10 | 15/48 (NCI-H1573, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 79.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.373× (z -8.5) |
| [[PANC-1 (line)]] | alt | 65.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0926× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.118× (z -9.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.293× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 1271 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0639× (z -10.1) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 42.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.2) | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | +0.71 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.71 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[AVEN]] | +0.70 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[DNAAF10]] | +0.69 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[EPM2A]] | +0.68 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[PIGW]] | +0.68 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GABPB1-AS1]] | +0.67 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[CSTF3]] | +0.67 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ALG8]] | +0.67 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ANXA2R-OT1]] | +0.67 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | +0.67 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[PCBP1-AS1]] | +0.65 | +0.35 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD5]] | -0.66 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[GALM]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.63 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[CFD]] | -0.63 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D17]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CDK18]] | -0.62 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[RAB11FIP1]] | -0.62 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[CYB5R1]] | -0.62 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TMEM256]] | -0.61 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[FHIP1A]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ALAD]] | -0.61 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[AHDC1]] | -0.61 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TEC]] | B | TEC activity lowers MSANTD2's level | lines that do not express TEC (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without TEC | 0.060 | ⚠ within organs, on part of the lines; also absent: TXK; maybe low, not absent; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity raises MSANTD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises MSANTD2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.7, -6.6); signed map (23.1, -28.5). **Vector** length 100, 23.3% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -7.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Myb/SANT DNA binding domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,766,498-124,800,706 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23342; previously C11orf61 |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

UniProt [Q6P1R3](https://www.uniprot.org/uniprotkb/Q6P1R3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26266) · Entrez [79684](https://www.ncbi.nlm.nih.gov/gene/79684) · UniProt [Q6P1R3](https://www.uniprot.org/uniprotkb/Q6P1R3) · Ensembl [ENSG00000120458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120458)

## Data

Gene col 4185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4185); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4185]; `tensor/DDL_lfc|DDL_z.npy` [4185]; `embed/gene_vectors.npy` [4185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4185 or target_col == 4185). Every well: [[MSANTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSANTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
