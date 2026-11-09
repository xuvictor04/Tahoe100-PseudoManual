---
symbol: "GCKR"
type: "gene"
col: 1411
ensembl_id: "ENSG00000084734"
name: "glucokinase regulator"
location: "2p23.3"
module: 81
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 26
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 17
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# GCKR

*glucokinase regulator* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 6.68× (z +13.0, q 4e-36, up in 15 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.598× (z -3.8, q 0.087, down in 11 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0409×, HT-29 0.0547×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HS-578T 0.134×, HT-29 0.0357×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.196×, HS-578T 0.283×); [[Cobimetinib (drug)]] 5 µM in 1 line (HS-578T 0.130×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.281×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGEF1P3]] (+0.65, fdr 1e-05), [[CPA6]] (+0.63, fdr 1e-05), [[DYNC1I1]] (+0.62, fdr 3e-05); moves opposite to [[YAP1]] (-0.55, fdr 2e-05), [[RHOBTB3]] (-0.53, fdr 4e-05), [[STOM]] (-0.52, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PRSS3]] → it (grade B ⚠); 17 go from it, the strongest it → [[DEDD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **6.68×** | +13.0 | 4e-36 | 15/16 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **5.86×** | +12.9 | 2e-35 | 16/17 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.72×** | +11.3 | 3e-27 | 17/19 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.23×** | +10.1 | 9e-22 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +9.4 | 9e-19 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +8.9 | 6e-17 | 3/14 (A498, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +7.6 | 2e-12 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.84×** | +7.0 | 2e-10 | 12/16 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.31×** | +6.0 | 1e-07 | 4/5 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.84×** | +5.4 | 3e-06 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.003 | 3/19 (Panc 03.27, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.0 | 0.004 | 0/10 | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.004 | 1/14 (NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.006 | 4/15 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.010 | 2/17 (A-172, HOP62) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.012 | 5/16 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.012 | 8/13 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.023 | 1/10 (NCI-H1792) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.88×** | +3.3 | 0.032 | 1/12 (Hs 766T) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +3.2 | 0.041 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0409×, HT-29 0.0547×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HS-578T 0.134×, HT-29 0.0357×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.196×, HS-578T 0.283×); [[Cobimetinib (drug)]] 5 µM in 1 line (HS-578T 0.130×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.598×** | -3.8 | 0.087 | 11/18 (A549, HS-578T, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.608× | -3.3 | 0.32 | 3/21 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.645× | -3.1 | 0.35 | 0/15 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 22.9 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0409× (z -16.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.130× (z -10.3) |
| [[HT-29 (line)]] | alt | 4.18 | 3 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 30.9× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.0357× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 15.7 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 9.09× (z +9.7) | [[Adagrasib (drug)]] 0.05 µM 0.522× (z -10.3) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -10.3) |
| [[HOP62 (line)]] | alt | 2.87 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 28.7× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0729× (z -8.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[HepG2_C3A (line)]] | wt | 45.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.69× (z +11.7) | — |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.648 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.650 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.619 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.368 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1P3]] | +0.65 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CPA6]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DYNC1I1]] | +0.62 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[ANXA10]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[C3orf52]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SLC51A]] | +0.58 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SNX29]] | +0.58 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[GIPR]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 | STRING 403 |
| [[DGKG]] | +0.57 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[NRIP3]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.57 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[HSP90AA2P]] | +0.56 | +0.62 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YAP1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RHOBTB3]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[STOM]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CCND3]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SLC35A5]] | -0.48 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[ZNF608]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SF3B3]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PTX3]] | -0.47 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[CAV1]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TMEM123]] | -0.47 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS3]] | B | PRSS3 activity raises GCKR's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.44× lower at baseline in the lines without PRSS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[KCNK1]] | B | KCNK1 activity raises GCKR's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without KCNK1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[LINC01589]] | B | LINC01589 activity raises GCKR's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without LINC01589 | 0.044 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[LINC01605]] | B | LINC01605 activity raises GCKR's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without LINC01605 | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[AADACP1]] | C | AADACP1 activity raises GCKR's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.43× lower at baseline in the lines without AADACP1 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[DHRS9]] | C | DHRS9 activity raises GCKR's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 1.81× lower at baseline in the lines without DHRS9 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[AADAC]] | C | AADAC activity raises GCKR's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.41× lower at baseline in the lines without AADAC | 0.072 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 10, C 7. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEDD2]] | B | GCKR activity raises DEDD2's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without GCKR | 0.006 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[ANKRD39]] | B | GCKR activity lowers ANKRD39's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.20× higher at baseline in the lines without GCKR | 0.018 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[SPSB1]] | B | GCKR activity raises SPSB1's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without GCKR | 0.042 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[LINC01605]] | B | GCKR activity raises LINC01605's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without GCKR | 0.042 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[LINC01705]] | B | GCKR activity raises LINC01705's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without GCKR | 0.045 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[DGKG]] | B | GCKR activity raises DGKG's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without GCKR | 0.058 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[PLAUR]] | B | GCKR activity raises PLAUR's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without GCKR | 0.077 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[GIPR]] | B | GCKR activity raises GIPR's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without GCKR | 0.090 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[PRSS3]] | B | GCKR activity raises PRSS3's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without GCKR | 0.091 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[ATP6V0D2]] | B | GCKR activity raises ATP6V0D2's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.63× lower at baseline in the lines without GCKR | 0.091 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[AADACP1]] | C | GCKR activity raises AADACP1's level | lines that do not express GCKR (24) vs lines expressing it (26) | 4.58× lower at baseline in the lines without GCKR | 0.015 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent; co-absent with the target |
| [[AADAC]] | C | GCKR activity raises AADAC's level | lines that do not express GCKR (24) vs lines expressing it (26) | 3.20× lower at baseline in the lines without GCKR | 0.020 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.8, -2.2); signed map (13.9, 53.9). **Vector** length 46.3, 10.7% of its response variance represented; |z| ≥ 3 in 538 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +11.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.0 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -1.6 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glucokinase regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,496,839-27,523,684 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 7 pathways, smallest: Defective TPR may confer susceptibility towards thyroid papillary carcinoma (TPC); Regulation of Glucokinase by Glucokinase Regulatory Protein; Glycolysis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14397](https://www.uniprot.org/uniprotkb/Q14397) (Glucokinase regulatory protein):

> Regulates glucokinase (GCK) by forming an inactive complex with this enzyme. Acts by promoting GCK recruitment to the nucleus, possibly to provide a reserve of GCK that can be quickly released in the cytoplasm after a meal. The affinity of GCKR for GCK is modulated by fructose metabolites: GCKR with bound fructose 6-phosphate has increased affinity for GCK, while GCKR with bound fructose 1-phosphate has strongly decreased affinity for GCK and does not inhibit GCK activity.

**Summary**, from NCBI Gene [2646](https://www.ncbi.nlm.nih.gov/gene/2646):

> This gene encodes a protein belonging to the GCKR subfamily of the SIS (Sugar ISomerase) family of proteins. The gene product is a regulatory protein that inhibits glucokinase in liver and pancreatic islet cells by binding non-covalently to form an inactive complex with the enzyme. This gene is considered a susceptibility gene candidate for a form of maturity-onset diabetes of the young (MODY). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4196) · Entrez [2646](https://www.ncbi.nlm.nih.gov/gene/2646) · UniProt [Q14397](https://www.uniprot.org/uniprotkb/Q14397) · Ensembl [ENSG00000084734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084734)

## Data

Gene col 1411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1411); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1411]; `tensor/DDL_lfc|DDL_z.npy` [1411]; `embed/gene_vectors.npy` [1411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1411 or target_col == 1411). Every well: [[GCKR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCKR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
