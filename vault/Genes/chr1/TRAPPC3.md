---
symbol: "TRAPPC3"
type: "gene"
col: 600
ensembl_id: "ENSG00000054116"
name: "trafficking protein particle complex subunit 3"
location: "1p34.3"
module: 7
arm: "+"
pooled_cpm: 20.3
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TRAPPC3

*trafficking protein particle complex subunit 3* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.78× (z +8.4, q 4e-14, up in 32 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.56× (z +6.6, q 4e-09, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.452× (z -6.3, q 2e-07, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAF2]] (+0.64, fdr 1e-05), [[LSM10]] (+0.62, fdr 1e-05), [[MRFAP1]] (+0.62, fdr 7e-06); moves opposite to [[PDIA6]] (-0.54, fdr 3e-05), [[IVNS1ABP]] (-0.52, fdr 3e-05), [[DDOST]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C21orf58]] → it (grade C ⚠); 2 go from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +8.4 | 4e-14 | 32/44 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +7.4 | 4e-11 | 31/44 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +6.6 | 4e-09 | 31/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.58×** | +6.6 | 4e-09 | 28/47 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +5.8 | 8e-07 | 29/48 (CFPAC-1, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.44×** | +5.5 | 4e-06 | 23/41 (A-427, A498, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +5.4 | 6e-06 | 27/48 (SW480, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.1 | 3e-05 | 25/47 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +4.9 | 5e-05 | 24/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 5e-05 | 25/45 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.41×** | +4.9 | 5e-05 | 17/32 (J82, A-172, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.38×** | +4.8 | 6e-05 | 22/48 (Hs 766T, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.6 | 2e-04 | 21/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 20/47 (MIA PaCa-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.23×** | +4.3 | 6e-04 | 20/47 (A-172, SNU-423, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.001 | 21/47 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.008 | 20/48 (HOP62, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 600.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -6.3 | 2e-07 | 31/45 (RKO, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -5.1 | 9e-05 | 28/48 (Hs 766T, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.822×** | -4.2 | 0.005 | 19/48 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.026 | 16/48 (LoVo, KATO III, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | **0.789×** | -3.6 | 0.035 | 15/48 (hTERT-HPNE, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~58% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF2]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[LSM10]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[MRFAP1]] | +0.62 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[PLEKHJ1]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[JAGN1]] | +0.60 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.59 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[DUSP3]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SRRD]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LEMD2]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ERVK3-1]] | +0.57 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SLC66A1]] | +0.57 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[OSGIN1]] | +0.57 | +0.46 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA6]] | -0.54 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[IVNS1ABP]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DDOST]] | -0.52 | -0.40 / -0.60 | both halves | 5e-05 | pathway: Asparagine N-linked glycosylation |
| [[TPP2]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RPN2]] | -0.51 | -0.42 / -0.57 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[PDIA3]] | -0.50 | -0.38 / -0.58 | both halves | 6e-05 | pathway: Asparagine N-linked glycosylation |
| [[SMPD4]] | -0.49 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TM9SF3]] | -0.49 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[STT3B]] | -0.49 | -0.31 / -0.60 | both halves | 2e-04 | pathway: Asparagine N-linked glycosylation |
| [[RPL6]] | -0.48 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GANAB]] | -0.48 | -0.29 / -0.59 | both halves | 2e-04 | pathway: Asparagine N-linked glycosylation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf58]] | C | C21orf58 activity raises TRAPPC3's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 1.41× lower at baseline in the lines without C21orf58 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TRAPPC3's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | TRAPPC3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.043 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Menadione (drug)]] 0.5 µM | C | TRAPPC3's natural level lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | TRAPPC3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.406 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.5, -0.5); signed map (-4.5, -21.1). **Vector** length 65.8, 11.9% of its response variance represented; |z| ≥ 3 in 694 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Rifaximin (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,136,570-36,156,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BET3 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O43617](https://www.uniprot.org/uniprotkb/O43617) (Trafficking protein particle complex subunit 3):

> May play a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [27095](https://www.ncbi.nlm.nih.gov/gene/27095):

> This gene encodes a component of the trafficking protein particle complex, which tethers transport vesicles to the cis-Golgi membrane. The encoded protein participates in the regulation of transport from the endoplasmic reticulum to the Golgi apparatus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:19942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19942) · Entrez [27095](https://www.ncbi.nlm.nih.gov/gene/27095) · UniProt [O43617](https://www.uniprot.org/uniprotkb/O43617) · Ensembl [ENSG00000054116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054116)

## Data

Gene col 600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 600); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 600]; `tensor/DDL_lfc|DDL_z.npy` [600]; `embed/gene_vectors.npy` [600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 600 or target_col == 600). Every well: [[TRAPPC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
