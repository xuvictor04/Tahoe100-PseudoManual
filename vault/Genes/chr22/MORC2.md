---
symbol: "MORC2"
type: "gene"
col: 5447
ensembl_id: "ENSG00000133422"
name: "MORC family CW-type zinc finger 2"
location: "22q12.2"
module: 5
arm: "+"
pooled_cpm: 34.87
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MORC2

*MORC family CW-type zinc finger 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.01× (z +9.4, q 2e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.412× (z -12.0, q 3e-30, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.441× (z -11.1, q 5e-26, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2S1]] (+0.66, fdr 1e-05), [[EIF4G1]] (+0.65, fdr 7e-06), [[DHX34]] (+0.64, fdr 7e-06); moves opposite to [[SIRT2]] (-0.59, fdr 1e-05), [[MPC2]] (-0.57, fdr 2e-05), [[MBIP]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +9.4 | 2e-18 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +8.5 | 8e-15 | 39/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.4 | 2e-11 | 32/48 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +5.8 | 1e-06 | 32/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.5 | 3e-06 | 29/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.5 | 3e-06 | 29/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.3 | 8e-06 | 29/48 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 0.002 | 27/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.009 | 24/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.3 | 0.054 | 23/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.066 | 20/47 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | 1.54× | +3.1 | 0.11 | 14/48 (RKO, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.25× | +3.0 | 0.11 | 11/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -12.0 | 3e-30 | 43/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.441×** | -11.1 | 5e-26 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -8.3 | 3e-14 | 36/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -6.9 | 7e-10 | 32/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.679×** | -4.7 | 3e-04 | 22/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.771×** | -3.3 | 0.081 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.789× | -3.2 | 0.11 | 22/48 (PANC-1, AN3 CA, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.796× | -3.1 | 0.15 | 17/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.4 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.276× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.354× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.180× (z -11.2) |
| [[PANC-1 (line)]] | alt | 48.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -20.8) |
| [[A-427 (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.230× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 50.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -14.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 46.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.290× (z -10.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -9.0) |
| [[SW1417 (line)]] | alt | 52.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.2) |
| [[SW48 (line)]] | wt | 24.4 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.171× (z -9.3) ⚠ toxic · without an alert: [[Apalutamide (drug)]] 0.05 µM 0.162× (z -8.9) |
| [[A549 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -10.3) |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -15.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0533× (z -16.2) |
| [[A-172 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S1]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[DHX34]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CDK9]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ABCF2]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[NOM1]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NOLC1]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TWNK]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[MYBBP1A]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[EIF3D]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[DDX21]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 | pathway: Epigenetic regulation of gene expression |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MPC2]] | -0.57 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MBIP]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[CRY2]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[DPM3]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ABCA5]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CENPC]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SPATA7]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MORC2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.1, -33.0); signed map (-4.8, -45.5). **Vector** length 86.9, 20.7% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -11.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | +0.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.9 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | MORC family CW-type zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,925,130-30,968,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZCW3, KIAA0852, AC004542.C22.1; previously ZCWCC1 |
| Gene groups (HGNC) | Zinc fingers CW-type |
| Reactome | 6 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Fatty acyl-CoA biosynthesis; Regulation of endogenous retroelements |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X9](https://www.uniprot.org/uniprotkb/Q9Y6X9) (ATPase MORC2):

> ATP-dependent chromatin remodeler essential for epigenetic silencing by the HUSH (human silencing hub) complex. Recruited by HUSH to target site in heterochromatin, the ATPase activity and homodimerization are critical for HUSH-mediated silencing. Represses germ cell-related genes and L1 retrotransposons in collaboration with SETDB1 and the HUSH complex, the silencing is dependent of repressive epigenetic modifications, such as H3K9me3 mark. Silencing events often occur within introns of …

**Summary**, from NCBI Gene [22880](https://www.ncbi.nlm.nih.gov/gene/22880):

> This gene encodes a member of the Microrchidia (MORC) protein superfamily. The encoded protein is known to regulate the condensation of heterochromatin in response to DNA damage and play a role in repressing transcription. The protein has been found to regulate the activity of ATP citrate lyase via specific interaction with this enzyme in the cytosol of lipogenic breast cancer cells. The protein also plays a role in lipogenesis and adipocyte differentiation. Alternative splicing results in …

**Accessions** — [HGNC:23573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23573) · Entrez [22880](https://www.ncbi.nlm.nih.gov/gene/22880) · UniProt [Q9Y6X9](https://www.uniprot.org/uniprotkb/Q9Y6X9) · Ensembl [ENSG00000133422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133422)

## Data

Gene col 5447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5447); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5447]; `tensor/DDL_lfc|DDL_z.npy` [5447]; `embed/gene_vectors.npy` [5447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5447 or target_col == 5447). Every well: [[MORC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
