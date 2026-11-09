---
symbol: "TWF2"
type: "gene"
col: 14500
ensembl_id: "ENSG00000247596"
name: "twinfilin actin binding protein 2"
location: "3p21.2"
module: 124
arm: "-"
pooled_cpm: 10.8
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# TWF2

*twinfilin actin binding protein 2* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.90× (z +7.2, q 4e-10, up in 23 of 32 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.337× (z -12.2, q 2e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTLC2]] (+0.68, fdr 3e-05), [[GNAI3]] (+0.68, fdr 5e-05), [[CARD19]] (+0.65, fdr 3e-05); moves opposite to [[ENOSF1]] (-0.65, fdr 1e-04), [[HEXIM2-AS1]] (-0.64, fdr 4e-04), [[DECR1]] (-0.62, fdr 5e-05).
> It sits in the **-** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FKBP1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.2 | 4e-10 | 23/32 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.9 | 1e-06 | 24/41 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.64×** | +5.3 | 2e-05 | 16/20 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.39×** | +3.4 | 0.081 | 12/28 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.4 | 0.081 | 2/48 (Panc 03.27, NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.337×** | -12.2 | 2e-31 | 40/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.423×** | -9.6 | 2e-19 | 31/44 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.427×** | -9.5 | 3e-19 | 41/47 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.453×** | -8.9 | 9e-17 | 36/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.587×** | -8.5 | 3e-15 | 28/45 (Panc 03.27, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -8.0 | 9e-14 | 30/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.595×** | -5.6 | 2e-06 | 24/47 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -5.4 | 5e-06 | 30/44 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -4.8 | 1e-04 | 22/43 (A-427, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -4.7 | 1e-04 | 23/43 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -4.7 | 1e-04 | 23/46 (Panc 03.27, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.667×** | -4.5 | 3e-04 | 24/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -3.4 | 0.025 | 18/48 (SNU-1, Panc 03.27, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.092 | 16/48 (SK-MEL-2, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -13.1) |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.8) |
| [[J82 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.1) |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.176× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -17.3) |
| [[PANC-1 (line)]] | alt | 8.36 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -13.3) |
| [[SW480 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -9.9) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -9.5) |
| [[C-33 A (line)]] | alt | 7.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.8) |
| [[HT-29 (line)]] | alt | 7.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -9.1) |
| [[KATO III (line)]] | alt | 9.17 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.148× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 7.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0852× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.82 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0383× (z -11.9) |
| [[SW1417 (line)]] | alt | 4.80 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0902× (z -9.0) |
| [[SW48 (line)]] | wt | 8.80 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0727× (z -8.7) |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC2]] | +0.68 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[GNAI3]] | +0.68 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[CARD19]] | +0.65 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.63 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[TBCB]] | +0.62 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[MYG1]] | +0.62 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.62 | +0.49 / +0.27 | both halves | 3e-04 |  |
| [[ATOSB]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[DNAJB1]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SNAPC2]] | +0.61 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[AGPAT2]] | +0.61 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[MBOAT2]] | +0.61 | +0.52 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOSF1]] | -0.65 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[HEXIM2-AS1]] | -0.64 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[DECR1]] | -0.62 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ZNF337-AS1]] | -0.62 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[TTC32]] | -0.62 | -0.56 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANKRD18A]] | -0.61 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[AHI1-DT]] | -0.60 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[UFL1-AS1]] | -0.59 | -0.50 / -0.24 | both halves | 5e-04 |  |
| [[DICER1-AS1]] | -0.59 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[ENTPD3-AS1]] | -0.59 | -0.54 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANXA2R-AS1]] | -0.59 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.58 | -0.49 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[CASD1]] | -0.58 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[ARGLU1]] | -0.58 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[GABPB1-AS1]] | -0.56 | -0.46 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP1B]] | B | FKBP1B activity raises TWF2's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without FKBP1B | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TWF2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **-** arm (projection on the module's main direction -0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (5.5, 3.9); signed map (-28.6, 17.8). **Vector** length 69.3, 12.8% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | -0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -12.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -8.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -9.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | twinfilin actin binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:52,228,612-52,246,788 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A6RP, A6r; previously PTK9L |
| Gene groups (HGNC) | Twinfilin actin binding protein family |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IBS0](https://www.uniprot.org/uniprotkb/Q6IBS0) (Twinfilin-2):

> Actin-binding protein involved in motile and morphological processes. Inhibits actin polymerization, likely by sequestering G-actin. By capping the barbed ends of filaments, it also regulates motility. Seems to play an important role in clathrin-mediated endocytosis and distribution of endocytic organelles. May play a role in regulating the mature length of the middle and short rows of stereocilia (By similarity).

**Summary**, from NCBI Gene [11344](https://www.ncbi.nlm.nih.gov/gene/11344):

> The protein encoded by this gene was identified by its interaction with the catalytic domain of protein kinase C-zeta. The encoded protein contains an actin-binding site and an ATP-binding site. It is most closely related to twinfilin (PTK9), a conserved actin monomer-binding protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9621) · Entrez [11344](https://www.ncbi.nlm.nih.gov/gene/11344) · UniProt [Q6IBS0](https://www.uniprot.org/uniprotkb/Q6IBS0) · Ensembl [ENSG00000247596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247596)

## Data

Gene col 14500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14500); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14500]; `tensor/DDL_lfc|DDL_z.npy` [14500]; `embed/gene_vectors.npy` [14500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14500 or target_col == 14500). Every well: [[TWF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TWF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
