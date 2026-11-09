---
symbol: "DYNLT2B"
type: "gene"
col: 13083
ensembl_id: "ENSG00000213123"
name: "dynein light chain Tctex-type 2B"
location: "3q29"
module: 37
arm: "+"
pooled_cpm: 17.18
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DYNLT2B

*dynein light chain Tctex-type 2B* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.94× (z +7.5, q 3e-11, up in 33 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.63× (z +5.8, q 1e-06, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.553× (z -9.9, q 2e-20, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM4SF19-DYNLT2B]] (+0.76, fdr 7e-06, ⚠ same locus), [[TM4SF19]] (+0.64, fdr 1e-05, ⚠ same locus), [[DCAF4L1]] (+0.61, fdr 1e-05), [[CCDC62]] (+0.59, fdr 1e-05), [[CRYM]] (+0.57, fdr 1e-05); moves opposite to [[FAM234A]] (-0.49, fdr 5e-05), [[RNF26]] (-0.48, fdr 5e-05), [[ATP5F1B]] (-0.47, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +7.5 | 3e-11 | 33/42 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.3 | 9e-11 | 25/35 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.8 | 1e-06 | 28/47 (A-172, CFPAC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.2 | 3e-05 | 18/32 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.5 | 9e-04 | 15/27 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.0 | 0.007 | 15/46 (CFPAC-1, SW48, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.048 | 14/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.048 | 16/47 (C-33 A, A-172, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.2 | 0.081 | 13/46 (HepG2/C3A, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.553×** | -9.9 | 2e-20 | 35/46 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -6.3 | 8e-08 | 27/43 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.400×** | -5.7 | 3e-06 | 32/47 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.0 | 0.008 | 6/48 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.714×** | -4.0 | 0.008 | 19/48 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.727×** | -3.8 | 0.015 | 19/48 (PANC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.048 | 22/47 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.762×** | -3.2 | 0.090 | 18/48 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 2 (2 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM 0.0573× (z -10.9) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 26.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.4) |
| [[A-172 (line)]] | wt | 36.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.45× (z +9.0) | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.3) |
| [[H4 (line)]] | wt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.2) |
| [[HOP62 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.7) |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.0) |
| [[LoVo (line)]] | wt | 7.07 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0462× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0928× (z -14.4) ⚠ transcription drop; cell-cycle shift, explains ~10% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.1) |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF19-DYNLT2B]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TM4SF19]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 | STRING 519; ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[DCAF4L1]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CRYM]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MAFG]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[PHKG1]] | +0.56 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ACVR1C]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[FBXO10]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ZNNT1]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FRZB]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CDC20-DT]] | +0.52 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[CHMP1B-AS1]] | +0.52 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[CFAP53]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM234A]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RNF26]] | -0.48 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ATP5F1B]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 | pathway: Organelle biogenesis and maintenance |
| [[PCIF1]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ZMYM3]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PRPF8]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[DAG1]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MED20]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TMEM123]] | -0.45 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[ACTB]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TTC31]] | -0.44 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[LANCL1]] | -0.44 | -0.36 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAT]] | B | LAT activity raises DYNLT2B's level | lines that do not express LAT (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without LAT | 0.038 | ⚠ within organs, on part of the lines; also absent: FRG1BP; maybe low, not absent |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises DYNLT2B's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.45× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[LINC02934]] | B | LINC02934 activity lowers DYNLT2B's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 1.51× higher at baseline in the lines without LINC02934 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.7, -3.9); signed map (14.3, 52.2). **Vector** length 69.6, 12.5% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.9 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain Tctex-type 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,291,219-196,318,299 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33212; previously TCTEX1D2 |
| Gene groups (HGNC) | Dynein 2 complex subunits; Dyneins, axonemal inner arm I1/f complex subunits; Dynein light chain Tctex-type family |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WW35](https://www.uniprot.org/uniprotkb/Q8WW35) (Dynein light chain Tctex-type protein 2B):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 2 complex (dynein-2 complex), a motor protein complex that drives the movement of cargos along microtubules within cilia and flagella in concert with the intraflagellar transport (IFT) system. Required for proper retrograde ciliary transport.

**Summary**, from NCBI Gene [255758](https://www.ncbi.nlm.nih.gov/gene/255758):

> Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polypeptides and a number of intermediate and light chains. This gene encodes a subunit of the human …

**Accessions** — [HGNC:28482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28482) · Entrez [255758](https://www.ncbi.nlm.nih.gov/gene/255758) · UniProt [Q8WW35](https://www.uniprot.org/uniprotkb/Q8WW35) · Ensembl [ENSG00000213123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213123)

## Data

Gene col 13083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13083); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13083]; `tensor/DDL_lfc|DDL_z.npy` [13083]; `embed/gene_vectors.npy` [13083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13083 or target_col == 13083). Every well: [[DYNLT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
