---
symbol: "MIX23"
type: "gene"
col: 8302
ensembl_id: "ENSG00000160124"
name: "mitochondrial matrix import factor 23"
location: "3q21.1"
module: 89
arm: "+"
pooled_cpm: 29.79
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# MIX23

*mitochondrial matrix import factor 23* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.76× (z +8.2, q 1e-13, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.615× (z -7.0, q 1e-09, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAAF1]] (+0.71, fdr 7e-06), [[MLH3]] (+0.68, fdr 7e-06), [[TYW3]] (+0.64, fdr 1e-05); moves opposite to [[MAPKAPK2]] (-0.60, fdr 1e-05), [[RALY]] (-0.57, fdr 2e-05), [[RPS6KA5]] (-0.55, fdr 2e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +8.2 | 1e-13 | 37/48 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +8.0 | 4e-13 | 38/47 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +7.9 | 5e-13 | 37/48 (NCI-H23, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +7.2 | 8e-11 | 36/48 (HS-578T, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +6.6 | 5e-09 | 36/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.54×** | +6.3 | 3e-08 | 32/44 (A498, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +6.3 | 3e-08 | 31/48 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +5.6 | 2e-06 | 30/47 (RPMI-7951, CFPAC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +5.5 | 2e-06 | 31/48 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +5.5 | 2e-06 | 35/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +5.4 | 4e-06 | 29/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.2 | 8e-06 | 28/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.9 | 5e-05 | 25/46 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.39×** | +4.8 | 6e-05 | 26/48 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.7 | 1e-04 | 24/48 (NCI-H1573, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.79×** | +4.4 | 3e-04 | 28/46 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.75×** | +4.2 | 7e-04 | 21/47 (NCI-H2347, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.73×** | +4.2 | 9e-04 | 23/46 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 25/48 (Panc 03.27, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.69×** | +4.0 | 0.001 | 21/48 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.615×** | -7.0 | 1e-09 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -5.8 | 2e-06 | 30/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.779×** | -3.6 | 0.047 | 21/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.623×** | -3.6 | 0.047 | 16/48 (NCI-H661, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.656× | -3.2 | 0.15 | 17/48 (NCI-H23, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 0.807× | -3.1 | 0.18 | 15/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.1) |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0751× (z -9.9) |
| [[CHP-212 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0850× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.47× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[A-172 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAAF1]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MLH3]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TYW3]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ALKBH3]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SART3]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[GATB]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.61 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ABRAXAS2]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[METTL22]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[RPAP1]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[RALY]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[RPS6KA5]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MAPK8]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NUP98]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[KLF13]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MYADM]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[SRGAP2]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[STAU1]] | -0.50 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ECE1]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[H2AZ2]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises MIX23's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.34× lower at baseline in the lines without ZNF675 | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.5, 11.1); signed map (7.3, -32.3). **Vector** length 86.0, 19.6% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.9 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.2 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[OTS514 (drug)]] 5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial matrix import factor 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,359,591-122,383,231 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33273; previously CCDC58 |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

UniProt [Q4VC31](https://www.uniprot.org/uniprotkb/Q4VC31) carries no function annotation.

**Summary**, from NCBI Gene [131076](https://www.ncbi.nlm.nih.gov/gene/131076):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31136) · Entrez [131076](https://www.ncbi.nlm.nih.gov/gene/131076) · UniProt [Q4VC31](https://www.uniprot.org/uniprotkb/Q4VC31) · Ensembl [ENSG00000160124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160124)

## Data

Gene col 8302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8302); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8302]; `tensor/DDL_lfc|DDL_z.npy` [8302]; `embed/gene_vectors.npy` [8302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8302 or target_col == 8302). Every well: [[MIX23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIX23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
