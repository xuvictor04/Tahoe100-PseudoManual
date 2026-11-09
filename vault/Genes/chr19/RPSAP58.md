---
symbol: "RPSAP58"
type: "gene"
col: 16392
ensembl_id: "ENSG00000288920"
name: "ribosomal protein SA 2"
location: "19p12"
module: 6
arm: "+"
pooled_cpm: 19.83
n_lines_expressing: 28
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RPSAP58

*ribosomal protein SA 2* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +5.9, q 3e-06, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.740× (z -4.3, q 0.008, down in 13 of 26 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3C]] (+0.53, fdr 3e-05), [[TGFB2]] (+0.50, fdr 5e-05), [[ATAD2]] (+0.48, fdr 5e-05); moves opposite to [[DENND2A]] (-0.47, fdr 5e-05), [[ZNF25]] (-0.46, fdr 4e-05), [[PARVB]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF682]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.9 | 3e-06 | 13/26 (BT-474, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +5.7 | 3e-06 | 13/26 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.6 | 4e-06 | 14/26 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.0 | 8e-05 | 11/26 (HOP62, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +4.5 | 6e-04 | 12/26 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +4.3 | 0.002 | 11/26 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.002 | 10/26 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +4.0 | 0.005 | 8/24 (HOP62, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.006 | 13/26 (BT-474, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.006 | 11/26 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.007 | 10/26 (SNU-423, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.008 | 10/26 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +3.7 | 0.011 | 10/26 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.016 | 11/26 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.024 | 6/26 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.050 | 9/26 (SNU-423, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.050 | 8/26 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.059 | 9/26 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -4.3 | 0.008 | 13/26 (COLO 205, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.768×** | -3.8 | 0.029 | 10/26 (COLO 205, A-427, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -3.8 | 0.029 | 13/26 (A-427, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.5 | 0.078 | 10/26 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.798× | -3.3 | 0.12 | 9/25 (HS-578T, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 88.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.0) |
| [[COLO 205 (line)]] | alt | 65.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.1) |
| [[BT-474 (line)]] | alt | 80.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 24.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 79.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 7.84 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0836× (z -9.3) |
| [[RKO (line)]] | wt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.110× (z -10.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3C]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TGFB2]] | +0.50 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ATAD2]] | +0.48 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[SLC6A14]] | +0.47 | +0.44 / +0.31 | both halves | 2e-04 |  |
| [[FIGN]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[E2F8]] | +0.46 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[RHOBTB3]] | +0.46 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[SLFN13]] | +0.45 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[NFIB]] | +0.45 | +0.42 / +0.39 | both halves | 6e-05 |  |
| [[SYNE2]] | +0.45 | +0.43 / +0.37 | both halves | 9e-05 |  |
| [[SLC44A3]] | +0.45 | +0.41 / +0.37 | both halves | 7e-05 |  |
| [[CSGALNACT1]] | +0.44 | +0.42 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2A]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ZNF25]] | -0.46 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PARVB]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[SYNDIG1]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SLC15A4]] | -0.45 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[NAV1]] | -0.45 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[GPR173]] | -0.45 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SH3BP5]] | -0.44 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[FIBCD1]] | -0.44 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[EFL1]] | -0.44 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[PCYT1A]] | -0.43 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[FAM156A]] | -0.42 | -0.28 / -0.39 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises RPSAP58's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF682]] | B | RPSAP58 activity raises ZNF682's level | lines that do not express RPSAP58 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without RPSAP58 | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF681, ENSG00000268119, ANOS1 |
| [[PCYT1A]] | B | RPSAP58 activity raises PCYT1A's level | lines that do not express RPSAP58 (22) vs lines expressing it (28) | 1.08× lower at baseline in the lines without RPSAP58 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF681, ENSG00000268119, ANOS1 |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.332). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (34.0, 21.1); signed map (47.9, 20.2). **Vector** length 51.0, 10.3% of its response variance represented; |z| ≥ 3 in 594 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | +3.5 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.3 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.8 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +0.2 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein SA 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:23,762,944-23,871,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RPSAP58 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A8I5KQE6](https://www.uniprot.org/uniprotkb/A0A8I5KQE6) (Small ribosomal subunit protein uS2B):

> Required for the assembly and/or stability of the 40S ribosomal subunit. Required for the processing of the 20S rRNA-precursor to mature 18S rRNA in a late step of the maturation of 40S ribosomal subunits. Also functions as a cell surface receptor for laminin. Plays a role in cell adhesion to the basement membrane and in the consequent activation of signaling transduction pathways. May play a role in cell fate determination and tissue morphogenesis. Also acts as a receptor for several other …

**Summary**, from NCBI Gene [388524](https://www.ncbi.nlm.nih.gov/gene/388524):

> Predicted to be a structural constituent of ribosome. Predicted to be involved in cytoplasmic translation and ribosomal small subunit assembly. Predicted to be located in several cellular components, including nucleus; plasma membrane; and ribosome. Predicted to be part of cytosolic small ribosomal subunit. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:36809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:36809) · Entrez [388524](https://www.ncbi.nlm.nih.gov/gene/388524) · UniProt [A0A8I5KQE6](https://www.uniprot.org/uniprotkb/A0A8I5KQE6) · Ensembl [ENSG00000288920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000288920)

## Data

Gene col 16392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16392); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16392]; `tensor/DDL_lfc|DDL_z.npy` [16392]; `embed/gene_vectors.npy` [16392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16392 or target_col == 16392). Every well: [[RPSAP58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPSAP58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
