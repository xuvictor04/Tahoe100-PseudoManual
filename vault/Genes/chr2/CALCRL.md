---
symbol: "CALCRL"
type: "gene"
col: 765
ensembl_id: "ENSG00000064989"
name: "calcitonin receptor like receptor"
location: "2q32.1"
module: 9
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 32
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 25
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CALCRL

*calcitonin receptor like receptor* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.21× (z +16.1, q 0e+00, up in 22 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Abemaciclib (drug)]] 5 µM: 0.445× (z -4.1, q 0.011, down in 7 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFD]] (+0.58, fdr 1e-05), [[PCDH10]] (+0.58, fdr 1e-05), [[PCDH17]] (+0.56, fdr 2e-05); moves opposite to [[LSM14B]] (-0.50, fdr 3e-05), [[CAMKK2]] (-0.43, fdr 1e-04), [[CIAO3]] (-0.43, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CDH8]] → it (grade B ⚠); 3 go from it, the strongest it → [[AOX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.21×** | +16.1 | 0e+00 | 22/28 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.55×** | +12.4 | 1e-32 | 17/25 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +10.2 | 3e-22 | 0/7 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.1 | 1e-21 | 2/7 (CFPAC-1, A498) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.03×** | +9.8 | 2e-20 | 13/28 (A498, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.60×** | +8.8 | 1e-16 | 20/27 (A-172, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.0 | 9e-14 | 6/19 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.95×** | +6.5 | 5e-09 | 13/28 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.0 | 1e-07 | 8/28 (A-172, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.6 | 1e-06 | 3/16 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.1 | 1e-05 | 11/28 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +4.9 | 5e-05 | 13/29 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +4.8 | 6e-05 | 10/27 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 5e-04 | 6/27 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +4.4 | 5e-04 | 2/8 (A498, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 9e-04 | 10/28 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.2 | 9e-04 | 3/20 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +4.2 | 1e-03 | 8/20 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.004 | 0/27 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 5 µM |  | **0.445×** | -4.1 | 0.011 | 7/22 (NCI-H1792, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -4.1 | 0.011 | 8/28 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.493×** | -3.6 | 0.053 | 6/21 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.776×** | -3.5 | 0.053 | 2/28 (A-427, Hs 766T) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -3.5 | 0.053 | 13/27 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -3.4 | 0.060 | 11/28 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.712×** | -3.3 | 0.073 | 9/26 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.529×** | -3.2 | 0.083 | 5/18 (NCI-H1792, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.727× | -3.1 | 0.12 | 3/28 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.802× | -3.1 | 0.13 | 2/28 (Hs 766T, NCI-H460) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 73.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0921× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.54 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0520× (z -9.7) |
| [[SHP-77 (line)]] | alt | 3.93 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0497× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.411 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFD]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PCDH10]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PCDH17]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ADAMTSL3]] | +0.54 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SPOCK3]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[EPHA7]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PCDH18]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[DPY19L2P1]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ECSCR]] | +0.52 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[EPHA6]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ASXL3]] | +0.50 | +0.36 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14B]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CAMKK2]] | -0.43 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CIAO3]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[DNAJC16]] | -0.43 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ATP6V0A2]] | -0.42 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH8]] | B | CDH8 activity raises CALCRL's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without CDH8 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent |
| [[PCDH18]] | B | PCDH18 activity raises CALCRL's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without PCDH18 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[ZNF385D]] | B | ZNF385D activity raises CALCRL's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without ZNF385D | 0.089 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[ADAMTS1]] | C | ADAMTS1 activity raises CALCRL's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 2.36× lower at baseline in the lines without ADAMTS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AOX1]] | B | CALCRL activity raises AOX1's level | lines that do not express CALCRL (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without CALCRL | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000259363, NRG1, SPOCK3 |
| [[AXDND1]] | B | CALCRL activity raises AXDND1's level | lines that do not express CALCRL (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without CALCRL | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000259363, NRG1, SPOCK3 |
| [[DUSP19]] | B | CALCRL activity raises DUSP19's level | lines that do not express CALCRL (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without CALCRL | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000259363, NRG1, SPOCK3 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 30.2); signed map (37.8, 31.3). **Vector** length 45.0, 7.28% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +4.9 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | calcitonin receptor like receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:187,341,964-187,448,460 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGRPR, CRLR |
| Gene groups (HGNC) | Calcitonin receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 10 pathways, smallest: Calcitonin-like ligand receptors; Class B/2 (Secretin family receptors); High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16602](https://www.uniprot.org/uniprotkb/Q16602) (Calcitonin gene-related peptide type 1 receptor):

> G protein-coupled receptor which specificity is determined by its interaction with receptor-activity-modifying proteins (RAMPs). Together with RAMP1, form the receptor complex for calcitonin-gene-related peptides CALCA/CGRP1 and CALCB/CGRP2. Together with RAMP2 or RAMP3, function as receptor complexes for adrenomedullin (ADM and ADM2). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream …

**Summary**, from NCBI Gene [10203](https://www.ncbi.nlm.nih.gov/gene/10203):

> Enables adrenomedullin binding activity; adrenomedullin receptor activity; and calcitonin gene-related peptide receptor activity. Involved in several processes, including G protein-coupled receptor signaling pathway; cellular response to sucrose stimulus; and receptor internalization. Located in several cellular components, including endoplasmic reticulum; endosome; and lysosome. Part of CGRP receptor complex and adrenomedullin receptor complex. Implicated in hereditary lymphedema. [provided by …

**Accessions** — [HGNC:16709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16709) · Entrez [10203](https://www.ncbi.nlm.nih.gov/gene/10203) · UniProt [Q16602](https://www.uniprot.org/uniprotkb/Q16602) · Ensembl [ENSG00000064989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064989)

## Data

Gene col 765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 765); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 765]; `tensor/DDL_lfc|DDL_z.npy` [765]; `embed/gene_vectors.npy` [765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 765 or target_col == 765). Every well: [[CALCRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALCRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
