---
symbol: "RNPC3-DT"
type: "gene"
col: 13408
ensembl_id: "ENSG00000224613"
name: "RNPC3 divergent transcript"
location: "1p21.1"
module: 35
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RNPC3-DT

*RNPC3 divergent transcript* — 1p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.88× (z +22.0, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.538× (z -5.7, q 9e-06, down in 17 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0789×, NCI-H23 0.0948×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Belinostat (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0381×, NCI-H23 0.0647×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.129×; ⚠ cell-cycle shift, explains ~50% of this change); [[Mebendazole (drug)]] 0.05 µM in 1 line (SW480 0.0719×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK4]] (+0.77, fdr 1e-05), [[MMADHC-DT]] (+0.76, fdr 9e-05), [[PBLD]] (+0.75, fdr 1e-04); moves opposite to [[GRAMD4]] (-0.64, fdr 6e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANKRD20A21P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.88×** | +22.0 | 0e+00 | 34/35 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.0 | 5e-21 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.96×** | +9.3 | 2e-18 | 23/45 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +8.3 | 1e-14 | 17/32 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +7.1 | 1e-10 | 17/38 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.0 | 6e-05 | 3/18 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.71×** | +4.9 | 8e-05 | 10/42 (LoVo, NCI-H1573, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.4 | 7e-04 | 13/42 (RKO, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.4 | 7e-04 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.37×** | +4.3 | 9e-04 | 11/45 (NCI-H460, RKO, …) | rises with dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.2 | 0.001 | 3/19 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.002 | 7/45 (HEC-1-A, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 9/42 (NCI-H23, SHP-77, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.007 | 8/42 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.007 | 4/41 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.007 | 4/47 (PANC-1, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.018 | 5/45 (SK-MEL-2, C32, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.030 | 7/46 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.048 | 7/35 (LoVo, SK-MEL-2, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.073 | 4/44 (NCI-H23, A-172, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13408.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0789×, NCI-H23 0.0948×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Belinostat (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0381×, NCI-H23 0.0647×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.129×; ⚠ cell-cycle shift, explains ~50% of this change); [[Mebendazole (drug)]] 0.05 µM in 1 line (SW480 0.0719×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.538×** | -5.7 | 9e-06 | 17/35 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.671×** | -3.9 | 0.015 | 11/27 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.671×** | -3.9 | 0.015 | 12/47 (PANC-1, SW480, …) | top dose only | composition shift |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.700× | -3.3 | 0.14 | 9/44 (hTERT-HPNE, NCI-H661, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.722× | -3.2 | 0.14 | 10/43 (CFPAC-1, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.57 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0647× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 3.24 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0381× (z -12.3) |
| [[PANC-1 (line)]] | alt | 5.79 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0789× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 2.58 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +9.1) | [[Mebendazole (drug)]] 0.05 µM 0.0719× (z -9.5) |
| [[BT-474 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 4.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +12.0) | — |
| [[LoVo (line)]] | wt | 4.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +10.0) | — |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK4]] | +0.77 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.76 | +0.73 / +0.36 | both halves | 9e-05 | same gene group |
| [[PBLD]] | +0.75 | +0.69 / +0.34 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | +0.75 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[CIBAR1-DT]] | +0.73 | +0.64 / +0.57 | both halves | 1e-05 | same gene group |
| [[SPRY3]] | +0.73 | +0.72 / +0.24 | both halves | 5e-04 |  |
| [[ERMAP]] | +0.71 | +0.70 / +0.31 | both halves | 2e-04 |  |
| [[TMEM202-AS1]] | +0.70 | +0.64 / +0.28 | both halves | 3e-04 |  |
| [[RAD9B]] | +0.69 | +0.63 / +0.37 | both halves | 9e-05 |  |
| [[MFF-DT]] | +0.69 | +0.60 / +0.34 | both halves | 1e-04 | same gene group |
| [[SRRM2-AS1]] | +0.68 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.68 | +0.65 / +0.36 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRAMD4]] | -0.64 | -0.62 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises RNPC3-DT's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.39× lower at baseline in the lines without ANKRD20A21P | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[TOP2A]] | B | TOP2A activity lowers RNPC3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.7, 11.7); signed map (25.0, -5.6). **Vector** length 56.8, 7.46% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +22.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RNPC3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.1 — chr1:103,415,980-103,525,511 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55855) · Entrez [101928436](https://www.ncbi.nlm.nih.gov/gene/101928436) · Ensembl [ENSG00000224613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224613)

## Data

Gene col 13408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13408); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13408]; `tensor/DDL_lfc|DDL_z.npy` [13408]; `embed/gene_vectors.npy` [13408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13408 or target_col == 13408). Every well: [[RNPC3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNPC3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
