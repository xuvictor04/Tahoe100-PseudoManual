---
symbol: "TBX1"
type: "gene"
col: 11487
ensembl_id: "ENSG00000184058"
name: "T-box transcription factor 1"
location: "22q11.21"
module: 128
arm: "+"
pooled_cpm: 3.47
n_lines_expressing: 27
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# TBX1

*T-box transcription factor 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +9.7, q 1e-19, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.393× (z -7.0, q 2e-09, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYS1]] (+0.64, fdr 7e-06), [[PRRX2]] (+0.60, fdr 2e-05), [[SEC14L4]] (+0.57, fdr 1e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TNFSF12]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC4A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +9.7 | 1e-19 | 8/20 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +9.2 | 7e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.3 | 2e-05 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +5.3 | 2e-05 | 1/4 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.34×** | +4.7 | 3e-04 | 1/6 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +4.4 | 8e-04 | 2/10 (A-427, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.038 | 1/14 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.048 | 2/19 (NCI-H2030, LoVo) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.12 | 2/17 (A-172, C-33 A) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.73× | +3.0 | 0.13 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.73× | +3.0 | 0.13 | 1/14 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.393×** | -7.0 | 2e-09 | 18/20 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.563×** | -6.3 | 8e-08 | 19/19 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.456×** | -6.1 | 2e-07 | 16/24 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -5.7 | 2e-06 | 15/24 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -5.1 | 4e-05 | 13/23 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -3.4 | 0.061 | 10/17 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.649×** | -3.4 | 0.064 | 13/24 (PANC-1, C-33 A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.1 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -29.4) |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 3.42 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0772× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.1) |
| [[A-172 (line)]] | wt | 7.45 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0397× (z -18.2) |
| [[A-427 (line)]] | wt | 4.68 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0795× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 2.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -9.1) |
| [[A498 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYS1]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[PRRX2]] | +0.60 | +0.49 / +0.61 | both halves | 2e-05 | **novel candidate** |
| [[SEC14L4]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[B4GALNT4]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CHD5]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[BARX1]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[BOLA3-DT]] | +0.54 | +0.55 / +0.37 | both halves | 7e-05 |  |
| [[PDZD4]] | +0.54 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[JPH3]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ZFP69]] | +0.52 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[ELFN1]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[KLHL14]] | +0.51 | +0.38 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF12]] | B | TNFSF12 activity raises TBX1's level | lines that do not express TNFSF12 (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without TNFSF12 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with ARID1A |
| [[HDAC6]] | B | HDAC6 activity raises TBX1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BRSK2]] | B | BRSK2 activity raises TBX1's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without BRSK2 | 0.099 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[PALM]] | C | PALM activity raises TBX1's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without PALM | 0.054 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[HES2]] | C | HES2 activity raises TBX1's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without HES2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | TBX1 activity raises SLC4A3's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without TBX1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[PKN3]] | B | TBX1 activity raises PKN3's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without TBX1 | 0.030 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[ST6GALNAC2]] | B | TBX1 activity raises ST6GALNAC2's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without TBX1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[FAXC]] | B | TBX1 activity raises FAXC's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TBX1 | 0.048 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[DUSP9]] | B | TBX1 activity raises DUSP9's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.35× lower at baseline in the lines without TBX1 | 0.072 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[NRG2]] | B | TBX1 activity raises NRG2's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without TBX1 | 0.092 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[HES2]] | C | TBX1 activity raises HES2's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without TBX1 | 0.024 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1; co-absent with the target |
| [[PALM]] | C | TBX1 activity raises PALM's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.86× lower at baseline in the lines without TBX1 | 0.034 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1; co-absent with the target |
| [[MSI1]] | C | TBX1 activity raises MSI1's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.46× lower at baseline in the lines without TBX1 | 0.075 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.6, 39.9); signed map (22.8, 25.4). **Vector** length 39.8, 7.17% of its response variance represented; |z| ≥ 3 in 562 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +9.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.3 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.1 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | -1.1 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,756,703-19,783,593 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CATCH22; previously VCF |
| Gene groups (HGNC) | T-box transcription factors |
| Reactome | 1 pathways, smallest: Cardiogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43435](https://www.uniprot.org/uniprotkb/O43435) (T-box transcription factor TBX1):

> Transcription factor that plays a key role in cardiovascular development by promoting pharyngeal arch segmentation during embryonic development (By similarity). Also involved in craniofacial muscle development (By similarity). Together with NKX2-5, acts as a regulator of asymmetric cardiac morphogenesis by promoting expression of PITX2 (By similarity). Acts upstream of TBX1 for the formation of the thymus and parathyroid glands from the third pharyngeal pouch (By similarity). Required for hair …

**Summary**, from NCBI Gene [6899](https://www.ncbi.nlm.nih.gov/gene/6899):

> This gene is a member of a phylogenetically conserved family of genes that share a common DNA-binding domain, the T-box. T-box genes encode transcription factors involved in the regulation of developmental processes. This gene product shares 98% amino acid sequence identity with the mouse ortholog. DiGeorge syndrome (DGS)/velocardiofacial syndrome (VCFS), a common congenital disorder characterized by neural-crest-related developmental defects, has been associated with deletions of chromosome …

**Accessions** — [HGNC:11592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11592) · Entrez [6899](https://www.ncbi.nlm.nih.gov/gene/6899) · UniProt [O43435](https://www.uniprot.org/uniprotkb/O43435) · Ensembl [ENSG00000184058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184058)

## Data

Gene col 11487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11487); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11487]; `tensor/DDL_lfc|DDL_z.npy` [11487]; `embed/gene_vectors.npy` [11487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11487 or target_col == 11487). Every well: [[TBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
