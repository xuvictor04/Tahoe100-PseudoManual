---
symbol: "ANKRD39"
type: "gene"
col: 13095
ensembl_id: "ENSG00000213337"
name: "ankyrin repeat domain 39"
location: "2q11.2"
module: 72
arm: "+"
pooled_cpm: 6.37
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ANKRD39

*ankyrin repeat domain 39* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.88× (z +11.8, q 4e-29, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.482× (z -11.5, q 7e-28, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM161A]] (+0.80, fdr 7e-06), [[HIBCH]] (+0.76, fdr 7e-06), [[CACYBP]] (+0.74, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.65, fdr 1e-05), [[HIVEP2]] (-0.59, fdr 3e-05), [[LEKR1]] (-0.59, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GCKR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.88×** | +11.8 | 4e-29 | 41/45 (HEC-1-A, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.74×** | +11.2 | 1e-26 | 40/47 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.88×** | +11.0 | 7e-26 | 36/43 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.83×** | +6.7 | 2e-09 | 18/29 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +6.5 | 9e-09 | 19/34 (LS 180, J82, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.74×** | +5.9 | 3e-07 | 8/13 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.89×** | +4.7 | 2e-04 | 17/47 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.004 | 12/46 (PANC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.9 | 0.005 | 8/27 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.39×** | +3.7 | 0.014 | 11/47 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.39×** | +3.6 | 0.015 | 12/47 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.37×** | +3.1 | 0.082 | 6/20 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +3.1 | 0.093 | 7/47 (AsPC-1, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.482×** | -11.5 | 7e-28 | 34/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -8.2 | 5e-14 | 30/47 (NCI-H2030, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -7.4 | 2e-11 | 29/41 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.384×** | -5.6 | 4e-06 | 22/45 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -5.4 | 7e-06 | 21/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -5.4 | 7e-06 | 20/41 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -5.3 | 1e-05 | 17/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -5.1 | 3e-05 | 21/42 (A-172, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -4.7 | 1e-04 | 21/46 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -3.7 | 0.011 | 12/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -3.7 | 0.012 | 15/46 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.735×** | -3.4 | 0.029 | 8/45 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.59 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.72× (z +9.9) | — |
| [[A-172 (line)]] | wt | 8.31 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0276× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 9.34 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 7.84 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 4.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -8.9) |
| [[HOP62 (line)]] | alt | 4.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -11.6) |
| [[HS-578T (line)]] | alt | 4.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0834× (z -9.7) |
| [[KATO III (line)]] | alt | 4.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0982× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 6.40 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0833× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 6.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -13.0) |
| [[SHP-77 (line)]] | alt | 8.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0307× (z -13.2) |
| [[A-427 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM161A]] | +0.80 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[HIBCH]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.74 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD23]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 | same gene group; STRING 773; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[EPS15L1]] | +0.72 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[FLYWCH1]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 | STRING 554 |
| [[PWWP3A]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[FAM241B]] | +0.69 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[MED31]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ZFAND2A]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.65 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.59 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[LEKR1]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[BMI1]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 | STRING 540 |
| [[FOSL2]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SKIL]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC13]] | -0.57 | -0.46 / -0.51 | both halves | 2e-05 | STRING 543 |
| [[SLC35A5]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[VEZF1]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[KLF10]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCKR]] | B | GCKR activity lowers ANKRD39's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.20× higher at baseline in the lines without GCKR | 0.018 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers ANKRD39's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ANKRD39's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM219A]] | C | FAM219A activity lowers ANKRD39's level | lines that do not express FAM219A (3) vs lines expressing it (47) | 1.67× higher at baseline in the lines without FAM219A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SH3PXD2A, METRNL; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.867). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, -8.5); signed map (-26.9, -26.1). **Vector** length 70.2, 12.1% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.54 to 12); *proteasome* (control, mean cos +0.55 to 11); *NIK-->noncanonical NF-kB signaling* (reactome, mean cos +0.55 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.1 | +11.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.9 | +11.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.1 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | +0.9 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.05 µM |  | +0.8 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -11.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,836,611-96,858,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC41816 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q53RE8](https://www.uniprot.org/uniprotkb/Q53RE8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28640) · Entrez [51239](https://www.ncbi.nlm.nih.gov/gene/51239) · UniProt [Q53RE8](https://www.uniprot.org/uniprotkb/Q53RE8) · Ensembl [ENSG00000213337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213337)

## Data

Gene col 13095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13095); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13095]; `tensor/DDL_lfc|DDL_z.npy` [13095]; `embed/gene_vectors.npy` [13095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13095 or target_col == 13095). Every well: [[ANKRD39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
