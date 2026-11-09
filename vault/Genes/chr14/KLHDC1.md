---
symbol: "KLHDC1"
type: "gene"
col: 12461
ensembl_id: "ENSG00000197776"
name: "kelch domain containing 1"
location: "14q21.3"
module: 10
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KLHDC1

*kelch domain containing 1* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.78× (z +5.0, q 3e-04, up in 3 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +4.7, q 8e-04, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.240× (z -12.9, q 5e-35, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM227B]] (+0.72, fdr 7e-06), [[LRRIQ3]] (+0.69, fdr 1e-05), [[EPM2A-DT]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM9B-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.0 | 3e-04 | 3/13 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.7 | 8e-04 | 18/40 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.6 | 8e-04 | 21/47 (A-172, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.5 | 0.001 | 20/46 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.62×** | +4.4 | 0.001 | 17/45 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.004 | 16/43 (SW480, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.008 | 13/43 (NCI-H2030, NCI-H1792, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.16×** | +3.7 | 0.018 | 5/45 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.018 | 16/44 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.62×** | +3.4 | 0.034 | 8/43 (A-172, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.3 | 0.043 | 12/46 (HT-29, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.48×** | +3.3 | 0.046 | 10/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.53× | +3.0 | 0.11 | 4/44 (NCI-H1573, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.41× | +3.0 | 0.11 | 14/43 (C32, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.240×** | -12.9 | 5e-35 | 41/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.272×** | -11.7 | 3e-29 | 39/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.341×** | -9.7 | 7e-20 | 33/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.362×** | -9.1 | 9e-18 | 36/45 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.386×** | -8.6 | 1e-15 | 37/45 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.450×** | -7.2 | 7e-11 | 32/44 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.508×** | -5.7 | 7e-07 | 24/43 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.528×** | -5.5 | 2e-06 | 20/34 (C32, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.560×** | -5.0 | 3e-05 | 24/44 (COLO 205, PANC-1, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -5.0 | 4e-05 | 21/46 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -4.7 | 2e-04 | 19/40 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.395×** | -4.4 | 6e-04 | 18/43 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.648×** | -3.9 | 0.004 | 17/47 (C32, SW48, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.007 | 21/44 (C32, NCI-H2030, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.486×** | -3.4 | 0.026 | 17/40 (HEC-1-A, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.504×** | -3.2 | 0.040 | 10/43 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.627×** | -3.0 | 0.080 | 4/47 (SNU-423, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0528× (z -19.4) |
| [[NCI-H1573 (line)]] | alt | 8.56 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0197× (z -18.9) |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0850× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 8.72 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0661× (z -10.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[Panc 03.27 (line)]] | alt | 7.01 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0716× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0982× (z -9.0) |
| [[C32 (line)]] | wt | 11.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0640× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 5.27 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0743× (z -9.0) |
| [[A498 (line)]] | wt | 3.14 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0688× (z -9.1) |
| [[H4 (line)]] | wt | 8.64 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0589× (z -8.6) |
| [[HCT15 (line)]] | alt | 8.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0521× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 9.31 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0530× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.124× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 5.24 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0933× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 5.43 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0876× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 3.88 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0674× (z -9.0) |
| [[SW 900 (line)]] | alt | 5.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0359× (z -10.6) |
| [[A-172 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM227B]] | +0.72 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[LRRIQ3]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[EPM2A-DT]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[TAPT1-AS1]] | +0.68 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[ZMAT1]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[C21orf62-AS1]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[TMEM9B-AS1]] | +0.65 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[USP38-DT]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[BDNF-AS]] | +0.65 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[CARF]] | +0.64 | +0.74 / +0.46 | both halves | 3e-05 |  |
| [[ITFG2-AS1]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises KLHDC1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without TMEM9B-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.2, 18.9); signed map (30.9, -8.9). **Vector** length 56.1, 8.45% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -7.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,693,105-49,753,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MST025 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N7A1](https://www.uniprot.org/uniprotkb/Q8N7A1) (Kelch domain-containing protein 1):

> Substrate-recognition component of a Cul5-RING (CRL5) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL5(KLHDC1) complex mediates …

**Summary**, from NCBI Gene [122773](https://www.ncbi.nlm.nih.gov/gene/122773):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Is active in Cul5-RING ubiquitin ligase complex and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19836) · Entrez [122773](https://www.ncbi.nlm.nih.gov/gene/122773) · UniProt [Q8N7A1](https://www.uniprot.org/uniprotkb/Q8N7A1) · Ensembl [ENSG00000197776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197776)

## Data

Gene col 12461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12461); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12461]; `tensor/DDL_lfc|DDL_z.npy` [12461]; `embed/gene_vectors.npy` [12461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12461 or target_col == 12461). Every well: [[KLHDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
