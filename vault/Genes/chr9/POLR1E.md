---
symbol: "POLR1E"
type: "gene"
col: 5959
ensembl_id: "ENSG00000137054"
name: "RNA polymerase I subunit E"
location: "9p13.2"
module: 5
arm: "+"
pooled_cpm: 16.01
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# POLR1E

*RNA polymerase I subunit E* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.79× (z +18.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.741× (z -4.1, q 0.020, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1G]] (+0.68, fdr 7e-06), [[PDCD11]] (+0.65, fdr 7e-06), [[NPM3]] (+0.63, fdr 1e-05); moves opposite to [[RAB21]] (-0.59, fdr 7e-05), [[MR1]] (-0.54, fdr 1e-04), [[UBE2A]] (-0.51, fdr 6e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.79×** | +18.9 | 0e+00 | 47/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.33×** | +17.1 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.08×** | +16.0 | 0e+00 | 44/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +14.8 | 0e+00 | 36/47 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.89×** | +8.7 | 3e-16 | 16/23 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +7.9 | 3e-13 | 34/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +6.8 | 6e-10 | 33/46 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +6.5 | 4e-09 | 26/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +6.4 | 8e-09 | 27/46 (PANC-1, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **1.50×** | +5.7 | 5e-07 | 22/40 (KATO III, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 6e-07 | 19/47 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[EX229 (drug)]] 5 µM |  | **1.97×** | +5.0 | 2e-05 | 17/44 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 3e-05 | 20/47 (A498, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.8 | 8e-05 | 16/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +4.6 | 2e-04 | 22/46 (A498, SW 900, …) | two highest doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.84×** | +4.5 | 2e-04 | 14/47 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 6e-04 | 20/46 (NCI-H23, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.009 | 9/46 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.029 | 5/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.031 | 8/43 (LoVo, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.020 | 18/46 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.757×** | -4.0 | 0.020 | 16/47 (SK-MEL-2, NCI-H23, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.027 | 13/47 (SNU-423, SW1417, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.756×** | -3.7 | 0.033 | 9/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.789× | -3.2 | 0.12 | 10/46 (HOP62, SK-MEL-2, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.804× | -3.2 | 0.12 | 10/48 (LoVo, HCT15, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.807× | -3.1 | 0.14 | 9/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.14 | 10/48 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.853× | -3.1 | 0.14 | 7/48 (MIA PaCa-2, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.28× (z +12.6) | [[Lonafarnib (drug)]] 5 µM 0.116× (z -9.8) ⚠ toxic |
| [[RKO (line)]] | wt | 36.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -16.3) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A498 (line)]] | wt | 17.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.2) | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.114× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 12.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +8.7) | — |
| [[KATO III (line)]] | alt | 11.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +9.0) | — |
| [[LoVo (line)]] | wt | 13.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 15.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +8.6) | — |
| [[A-172 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1G]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | same gene group; pathway: B-WICH complex positively regulates rRNA expression; STRING 999 |
| [[PDCD11]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 | STRING 751 |
| [[NPM3]] | +0.63 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LYAR]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 | STRING 652 |
| [[TMEM201]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[NLE1]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 | STRING 762 |
| [[RMND1]] | +0.61 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[BOP1]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 | STRING 880 |
| [[WDR3]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 | STRING 855 |
| [[GEMIN5]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[NOP16]] | +0.59 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 | same gene group; pathway: B-WICH complex positively regulates rRNA expression; STRING 999 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB21]] | -0.59 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[MR1]] | -0.54 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[UBE2A]] | -0.51 | -0.22 / -0.56 | both halves | 6e-04 |  |
| [[DRAM1]] | -0.51 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[TBC1D22B]] | -0.51 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[SMIM14]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[BLOC1S2]] | -0.50 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[RPS27L]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[LINC00938]] | -0.49 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[B2M]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises POLR1E's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[LDLRAD3]] | B | LDLRAD3 activity raises POLR1E's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without LDLRAD3 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.9, -39.6); signed map (-7.8, -50.7). **Vector** length 71.8, 13.3% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +18.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +17.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.5 | +16.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +3.6 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -2.7 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I subunit E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,485,948-37,503,697 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13390, PAF53, FLJ13970, RPA49; previously PRAF1 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 9 pathways, smallest: RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZS1](https://www.uniprot.org/uniprotkb/Q9GZS1) (DNA-directed RNA polymerase I subunit RPA49):

> Component of RNA polymerase I (Pol I), a DNA-dependent RNA polymerase which synthesizes ribosomal RNA precursors using the four ribonucleoside triphosphates as substrates. Appears to be involved in the formation of the initiation complex at the promoter by mediating the interaction between Pol I and UBTF/UBF.

**Summary**, from NCBI Gene [64425](https://www.ncbi.nlm.nih.gov/gene/64425):

> Predicted to enable DNA binding activity and RNA polymerase I general transcription initiation factor binding activity. Involved in nucleolar large rRNA transcription by RNA polymerase I; transcription elongation by RNA polymerase I; and transcription initiation at RNA polymerase I promoter. Located in fibrillar center and nucleoplasm. Part of RNA polymerase I complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17631) · Entrez [64425](https://www.ncbi.nlm.nih.gov/gene/64425) · UniProt [Q9GZS1](https://www.uniprot.org/uniprotkb/Q9GZS1) · Ensembl [ENSG00000137054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137054)

## Data

Gene col 5959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5959); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5959]; `tensor/DDL_lfc|DDL_z.npy` [5959]; `embed/gene_vectors.npy` [5959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5959 or target_col == 5959). Every well: [[POLR1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
