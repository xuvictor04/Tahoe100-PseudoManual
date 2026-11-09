---
symbol: "SEMA6C"
type: "gene"
col: 6742
ensembl_id: "ENSG00000143434"
name: "semaphorin 6C"
location: "1q21.3"
module: 76
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# SEMA6C

*semaphorin 6C* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.19× (z +15.1, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.505× (z -7.2, q 3e-10, down in 18 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.532× (z -6.7, q 8e-09, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADIPOR1]] (+0.71, fdr 1e-05), [[FCHSD1]] (+0.69, fdr 1e-05), [[LMBR1L]] (+0.67, fdr 1e-05); moves opposite to [[MCTS1]] (-0.71, fdr 8e-06), [[CPSF2]] (-0.69, fdr 1e-05), [[CYREN]] (-0.67, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.19×** | +15.1 | 0e+00 | 41/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.97×** | +14.5 | 3e-45 | 41/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +9.6 | 1e-19 | 35/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.68×** | +7.7 | 3e-12 | 11/45 (A-172, SHP-77, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.2 | 7e-08 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.0 | 2e-07 | 14/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +5.2 | 1e-05 | 9/32 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.65×** | +5.2 | 1e-05 | 7/27 (SHP-77, HOP62, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.6 | 3e-04 | 16/44 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.006 | 10/42 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.008 | 5/47 (A-427, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.008 | 12/36 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 7/45 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.5 | 0.019 | 2/16 (NCI-H23, SW480) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.39×** | +3.5 | 0.020 | 2/29 (J82, A-427) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.022 | 5/46 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.034 | 4/23 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +3.0 | 0.070 | 1/42 (NCI-H2347) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.095 | 2/44 (SW 900, MIA PaCa-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.505×** | -7.2 | 3e-10 | 18/45 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.532×** | -6.7 | 8e-09 | 21/44 (HT-29, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -6.1 | 2e-07 | 15/32 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.588×** | -5.4 | 1e-05 | 17/43 (NCI-H23, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -4.9 | 9e-05 | 14/41 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.648×** | -4.6 | 4e-04 | 14/42 (A-172, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.691×** | -3.9 | 0.008 | 17/44 (SW1417, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.795×** | -3.4 | 0.042 | 16/36 (SNU-423, A-172, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -10.1) |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 1 | — | [[Indacaterol (maleate) (drug)]] 0.5 µM 0.0499× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 3.80 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0836× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 6.25 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -8.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0923× (z -8.9) ⚠ toxic; unreliable plate only |
| [[A-427 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADIPOR1]] | +0.71 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.69 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LMBR1L]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[GDPD3]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.66 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SEZ6L2]] | +0.65 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CD81]] | +0.65 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MOSPD3]] | +0.64 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KLC3]] | +0.63 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[MYPOP]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.62 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[MAST3]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.71 | -0.57 / -0.60 | both halves | 8e-06 |  |
| [[CPSF2]] | -0.69 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[CYREN]] | -0.67 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[FH]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.60 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TASOR]] | -0.60 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MAGOHB]] | -0.60 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NEK9]] | -0.59 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ANAPC13]] | -0.59 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.58 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MRPS16]] | -0.58 | -0.49 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises SEMA6C's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without STARD9 | 0.038 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.3, -5.0); signed map (-34.3, 13.5). **Vector** length 49.8, 5.89% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.1 | +7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.8 | +9.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +5.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.9 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.0 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 6C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,131,685-151,146,631 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1869, Sema-Y |
| Gene groups (HGNC) | Semaphorins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3T2](https://www.uniprot.org/uniprotkb/Q9H3T2) (Semaphorin-6C):

> Shows growth cone collapsing activity on dorsal root ganglion (DRG) neurons in vitro. May be a stop signal for the DRG neurons in their target areas, and possibly also for other neurons. May also be involved in the maintenance and remodeling of neuronal connections.

**Summary**, from NCBI Gene [10500](https://www.ncbi.nlm.nih.gov/gene/10500):

> This gene encodes a member of the semaphorin family. Semaphorins represent important molecular signals controlling multiple aspects of the cellular response that follows CNS injury, and thus may play an important role in neural regeneration. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:10740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10740) · Entrez [10500](https://www.ncbi.nlm.nih.gov/gene/10500) · UniProt [Q9H3T2](https://www.uniprot.org/uniprotkb/Q9H3T2) · Ensembl [ENSG00000143434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143434)

## Data

Gene col 6742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6742); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6742]; `tensor/DDL_lfc|DDL_z.npy` [6742]; `embed/gene_vectors.npy` [6742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6742 or target_col == 6742). Every well: [[SEMA6C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA6C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
