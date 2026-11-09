---
symbol: "SLCO2A1"
type: "gene"
col: 10510
ensembl_id: "ENSG00000174640"
name: "solute carrier organic anion transporter family member 2A1"
location: "3q22.1-q22.2"
module: 98
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 34
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# SLCO2A1

*solute carrier organic anion transporter family member 2A1* — 3q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +11.3, q 7e-27, up in 6 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.593× (z -4.8, q 8e-04, down in 8 of 25 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -4.1, q 0.012, down in 7 of 27 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HTRA3]] (+0.55, fdr 1e-05), [[FSTL3]] (+0.55, fdr 2e-05), [[VSTM2L]] (+0.54, fdr 1e-05); moves opposite to [[ARMC9]] (-0.47, fdr 1e-04), [[TMEM158]] (-0.47, fdr 5e-05), [[GPR157]] (-0.42, fdr 4e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL1R1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ADAMTSL4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +11.3 | 7e-27 | 6/22 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +9.6 | 2e-19 | 19/28 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +9.2 | 7e-18 | 1/7 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +8.5 | 2e-15 | 3/10 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +7.6 | 2e-12 | 1/9 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +7.4 | 9e-12 | 7/24 (HepG2/C3A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +6.2 | 5e-08 | 12/23 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.66×** | +4.6 | 3e-04 | 6/25 (HS-578T, PANC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 9/26 (A-172, HEC-1-A, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +4.0 | 0.004 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.79×** | +3.8 | 0.008 | 1/14 (HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.5 | 0.019 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.020 | 7/25 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.4 | 0.026 | 1/8 (LoVo) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.033 | 4/30 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.039 | 9/25 (PANC-1, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.044 | 7/25 (PANC-1, HS-578T, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.088 | 4/28 (HEC-1-A, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.593×** | -4.8 | 8e-04 | 8/25 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -4.1 | 0.012 | 7/27 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.667×** | -3.8 | 0.032 | 10/30 (LoVo, A-427, …) | inconsistent across doses | composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.671×** | -3.7 | 0.032 | 11/25 (SW480, HOP62, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.691×** | -3.4 | 0.072 | 12/21 (NCI-H1792, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 24.5 | 0 | 13 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0703× (z -16.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0727× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0556× (z -12.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0886× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 2.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.03× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0648× (z -8.8) |
| [[A-172 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTRA3]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[FSTL3]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[VSTM2L]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ROS1]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PHLDB2]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[IL1R1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LINC02015]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ABCA6]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[SVEP1]] | +0.52 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[B4GALT1]] | +0.51 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[DSEL]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[MAFB]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC9]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TMEM158]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[GPR157]] | -0.42 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[VIM]] | -0.41 | -0.52 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[HSDL1]] | -0.40 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1R1]] | B | IL1R1 activity raises SLCO2A1's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without IL1R1 | 0.061 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[HDAC6]] | B | HDAC6 activity raises SLCO2A1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TLR2]] | B | TLR2 activity raises SLCO2A1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.04× lower at baseline in the lines without TLR2 | 0.084 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTSL4]] | B | SLCO2A1 activity raises ADAMTSL4's level | lines that do not express SLCO2A1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without SLCO2A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: FHL1, CYS1, LIMS2 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 18.8); signed map (20.3, 29.0). **Vector** length 57.4, 11.4% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.2 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.2 | -3.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 2A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1-q22.2 — chr3:133,932,701-134,052,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGT, OATP2A1; previously SLC21A2, MATR1 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Hallmark sets | ANGIOGENESIS |
| Reactome | 6 pathways, smallest: Organic anion transport by SLCO transporters; SLC-mediated transport of organic anions; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92959](https://www.uniprot.org/uniprotkb/Q92959) (Solute carrier organic anion transporter family member 2A1):

> Mediates the transport of prostaglandins (PGs, mainly PGE2, PGE1, PGE3, PGF2alpha, PGD2, PGH2) and thromboxanes (thromboxane B2) across the cell membrane. PGs and thromboxanes play fundamental roles in diverse functions such as intraocular pressure, gastric acid secretion, renal salt and water transport, vascular tone, and fever. Plays a role in the clearance of PGs from the circulation through cellular uptake, which allows cytoplasmic oxidation and PG signal termination. PG uptake is dependent …

**Summary**, from NCBI Gene [6578](https://www.ncbi.nlm.nih.gov/gene/6578):

> This gene encodes a prostaglandin transporter that is a member of the 12-membrane-spanning superfamily of transporters. The encoded protein may be involved in mediating the uptake and clearance of prostaglandins in numerous tissues. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:10955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10955) · Entrez [6578](https://www.ncbi.nlm.nih.gov/gene/6578) · UniProt [Q92959](https://www.uniprot.org/uniprotkb/Q92959) · Ensembl [ENSG00000174640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174640)

## Data

Gene col 10510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10510); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10510]; `tensor/DDL_lfc|DDL_z.npy` [10510]; `embed/gene_vectors.npy` [10510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10510 or target_col == 10510). Every well: [[SLCO2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
