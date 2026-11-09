---
symbol: "SEPTIN8"
type: "gene"
col: 8942
ensembl_id: "ENSG00000164402"
name: "septin 8"
location: "5q31.1"
module: 54
arm: "-"
pooled_cpm: 21.21
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SEPTIN8

*septin 8* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +10.4, q 1e-22, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.400× (z -13.5, q 1e-38, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPPL1]] (+0.67, fdr 2e-05), [[RAP2C]] (+0.66, fdr 1e-05), [[OXCT1]] (+0.64, fdr 3e-05); moves opposite to [[RPS5]] (-0.66, fdr 1e-05), [[SNRPD2]] (-0.66, fdr 1e-05), [[RBIS]] (-0.63, fdr 2e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.4 | 1e-22 | 38/47 (A549, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +9.8 | 2e-20 | 23/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +8.1 | 2e-13 | 24/33 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +6.6 | 6e-09 | 23/39 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.4 | 2e-08 | 23/42 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +6.2 | 4e-08 | 24/47 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.5 | 6e-04 | 16/47 (HT-29, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.008 | 16/48 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.7 | 0.015 | 16/48 (CFPAC-1, A-172, …) | top dose only | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.28×** | +3.6 | 0.017 | 14/48 (SNU-423, RKO, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +3.6 | 0.017 | 16/47 (SNU-423, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.3 | 0.043 | 13/47 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.12 | 9/47 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -13.5 | 1e-38 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.419×** | -13.4 | 3e-38 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -12.4 | 3e-33 | 39/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.572×** | -8.1 | 7e-14 | 34/48 (LOX-IMVI, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -7.5 | 8e-12 | 31/46 (Hs 766T, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -6.8 | 7e-10 | 30/48 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -5.9 | 3e-07 | 27/47 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.683×** | -5.9 | 3e-07 | 26/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -4.5 | 3e-04 | 21/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.749×** | -4.4 | 5e-04 | 22/48 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -4.4 | 5e-04 | 20/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -4.4 | 6e-04 | 19/47 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.586×** | -4.3 | 7e-04 | 18/39 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.001 | 18/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.771×** | -4.0 | 0.002 | 18/48 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.700×** | -3.9 | 0.003 | 14/48 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.631×** | -3.7 | 0.007 | 13/46 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.855× | -3.4 | 0.020 | 11/48 (NCI-H2347, SNU-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 49.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.243× (z -14.0) |
| [[LoVo (line)]] | wt | 30.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.5) |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -10.9) |
| [[SW480 (line)]] | alt | 27.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -14.4) |
| [[A549 (line)]] | wt | 20.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -11.0) |
| [[KATO III (line)]] | alt | 20.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.100× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.303× (z -10.2) |
| [[RKO (line)]] | wt | 30.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -10.5) |
| [[A-172 (line)]] | wt | 32.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -8.5) |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.161× (z -8.7) |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0479× (z -9.4) |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -10.5) |
| [[HT-29 (line)]] | alt | 13.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.70× (z +10.0) | — |
| [[J82 (line)]] | alt | 22.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -8.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 9.62 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0605× (z -12.0) |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.260× (z -8.7) |
| [[SW48 (line)]] | wt | 29.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -9.8) |
| [[A-427 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPPL1]] | +0.67 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RAP2C]] | +0.66 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.64 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[SORBS3]] | +0.64 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PSME3IP1]] | +0.63 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SEPTIN11]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 | same gene group; STRING 953 |
| [[EIF4G2]] | +0.63 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[UBQLN4]] | +0.62 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZDHHC23]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MAN2A2]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MTA2]] | +0.62 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[BRPF3]] | +0.61 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS5]] | -0.66 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SNRPD2]] | -0.66 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[RBIS]] | -0.63 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ATP5MJ]] | -0.63 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.62 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RPS14]] | -0.62 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PIBF1]] | -0.62 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[RPS10]] | -0.62 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ELOB]] | -0.61 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RPS25]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.61 | -0.48 / -0.51 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS16]] ⚠ | -0.61 | -0.43 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC27A1]] | -0.61 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[TMEM256]] | -0.60 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SEPTIN8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-4.1, 5.4); signed map (21.6, -34.5). **Vector** length 102, 23.3% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | -0.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -13.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -13.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -8.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | septin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,750,819-132,807,241 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0202, SEP2, Septin-8; previously SEPT8 |
| Gene groups (HGNC) | Septins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92599](https://www.uniprot.org/uniprotkb/Q92599) (Septin-8):

> Filament-forming cytoskeletal GTPase (By similarity). May play a role in platelet secretion. Seems to participate in the process of SNARE complex formation in synaptic vesicles (By similarity).; [Isoform 4]: Stabilizes BACE1 protein levels and promotes the sorting and accumulation of BACE1 to the recycling or endosomal compartments, modulating the beta-amyloidogenic processing of APP.

**Summary**, from NCBI Gene [23176](https://www.ncbi.nlm.nih.gov/gene/23176):

> This gene is a member of the septin family of nucleotide binding proteins, originally described in yeast as cell division cycle regulatory proteins. Septins are highly conserved in yeast, Drosophila, and mouse, and appear to regulate cytoskeletal organization. Disruption of septin function disturbs cytokinesis and results in large multinucleate or polyploid cells. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:16511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16511) · Entrez [23176](https://www.ncbi.nlm.nih.gov/gene/23176) · UniProt [Q92599](https://www.uniprot.org/uniprotkb/Q92599) · Ensembl [ENSG00000164402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164402)

## Data

Gene col 8942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8942); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8942]; `tensor/DDL_lfc|DDL_z.npy` [8942]; `embed/gene_vectors.npy` [8942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8942 or target_col == 8942). Every well: [[SEPTIN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
