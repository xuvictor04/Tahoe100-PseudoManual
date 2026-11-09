---
symbol: "GBA2"
type: "gene"
col: 957
ensembl_id: "ENSG00000070610"
name: "glucosylceramidase beta 2"
location: "9p13.3"
module: 174
arm: "+"
pooled_cpm: 24.53
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# GBA2

*glucosylceramidase beta 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.36× (z +5.6, q 8e-06, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.28× (z +4.5, q 0.002, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -15.8, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STARD3]] (+0.66, fdr 1e-05), [[PHC2]] (+0.65, fdr 1e-05), [[ZNF496]] (+0.64, fdr 1e-05); moves opposite to [[CFL2]] (-0.64, fdr 8e-06), [[LSMEM1]] (-0.60, fdr 1e-05), [[PAXIP1-AS2]] (-0.60, fdr 2e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.36×** | +5.6 | 8e-06 | 24/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +5.6 | 8e-06 | 23/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 0.002 | 21/47 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.27×** | +4.2 | 0.003 | 20/48 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.013 | 11/48 (LOX-IMVI, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.041 | 4/47 (NCI-H1573, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -15.8 | 0e+00 | 39/47 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -8.3 | 2e-14 | 32/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -5.6 | 5e-06 | 24/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.756×** | -5.3 | 1e-05 | 23/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.744×** | -5.3 | 1e-05 | 18/48 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.746×** | -5.3 | 1e-05 | 21/47 (SW48, SHP-77, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.742×** | -5.2 | 2e-05 | 22/47 (A549, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.772×** | -4.3 | 0.001 | 16/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.848× | -4.1 | 0.002 | 12/48 (HT-29, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.834× | -4.1 | 0.003 | 16/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.799×** | -4.0 | 0.003 | 16/42 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.003 | 18/48 (NCI-H23, SW 1088, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.802×** | -3.8 | 0.006 | 16/33 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | 0.864× | -3.4 | 0.027 | 15/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.050 | 12/48 (A-172, SHP-77, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.861× | -3.2 | 0.050 | 13/48 (C32, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.843× | -3.1 | 0.068 | 14/47 (NCI-H23, SW48, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.891× | -2.9 | 0.096 | 6/48 (A549, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 29.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.5) |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.8) |
| [[SW48 (line)]] | wt | 25.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0401× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.6) |
| [[A-427 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.180× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -13.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.8) |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0612× (z -21.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.6) |
| [[PANC-1 (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.4) |
| [[SW480 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -14.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD3]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[PHC2]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CSK]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TECPR1]] | +0.62 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF18]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CAP1]] | +0.61 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[DAP3]] | +0.61 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[FBXW2]] | +0.60 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[LSMEM1]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | -0.60 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[NR1D2]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RAB21]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[MATCAP2]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[APOLD1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TAF9B]] | -0.59 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[MATR3]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[FMR1]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[LGALS3]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CILK1]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GBA2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.4, -8.2); signed map (-47.4, -19.4). **Vector** length 94.9, 19.9% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.6 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.2 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.9 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +3.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.9 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -8.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glucosylceramidase beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,736,866-35,749,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1605, AD035, DKFZp762K054; previously SPG46 |
| Gene groups (HGNC) | Glycoside hydrolase family; Glucosylceramidases |
| Reactome | 4 pathways, smallest: Glycosphingolipid catabolism; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCG7](https://www.uniprot.org/uniprotkb/Q9HCG7) (Non-lysosomal glucosylceramidase):

> Non-lysosomal glucosylceramidase that catalyzes the hydrolysis of glucosylceramides/GlcCers (such as beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine) to free glucose and ceramides (such as N-acylsphing-4-enine). GlcCers are membrane glycosphingolipids that have a wide intracellular distribution (By similarity). They are the main precursors of more complex glycosphingolipids that play a role in cellular growth, differentiation, adhesion, signaling, cytoskeletal dynamics and membrane properties (By …

**Summary**, from NCBI Gene [57704](https://www.ncbi.nlm.nih.gov/gene/57704):

> This gene encodes a microsomal beta-glucosidase that catalyzes the hydrolysis of bile acid 3-O-glucosides as endogenous compounds. Studies to determine subcellular localization of this protein in the liver indicated that the enzyme was mainly enriched in the microsomal fraction where it appeared to be confined to the endoplasmic reticulum. This putative transmembrane protein is thought to play a role in carbohydrate transport and metabolism. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18986) · Entrez [57704](https://www.ncbi.nlm.nih.gov/gene/57704) · UniProt [Q9HCG7](https://www.uniprot.org/uniprotkb/Q9HCG7) · Ensembl [ENSG00000070610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070610)

## Data

Gene col 957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 957); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 957]; `tensor/DDL_lfc|DDL_z.npy` [957]; `embed/gene_vectors.npy` [957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 957 or target_col == 957). Every well: [[GBA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
