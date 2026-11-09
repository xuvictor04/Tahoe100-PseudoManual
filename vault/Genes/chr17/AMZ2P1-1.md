---
symbol: "AMZ2P1-1"
type: "gene"
col: 16601
ensembl_id: "ENSG00000291140"
name: ""
location: ""
module: 12
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# AMZ2P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +12.9, q 5e-35, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -8.4, q 3e-14, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK16]] (+0.78, fdr 7e-06), [[SNHG11]] (+0.76, fdr 7e-06), [[AMZ2P1]] (+0.72, fdr 7e-06, ⚠ same locus), [[PEX12]] (+0.72, fdr 7e-06); moves opposite to [[DCAF16]] (-0.60, fdr 2e-05), [[HACD3]] (-0.58, fdr 2e-05), [[NIPA2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NGFR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +12.9 | 5e-35 | 29/37 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +9.7 | 5e-20 | 2/5 (A498, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +7.3 | 4e-11 | 28/43 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +5.7 | 2e-06 | 4/17 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.6 | 2e-06 | 13/35 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +5.6 | 3e-06 | 15/36 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.3 | 8e-06 | 11/45 (SW480, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.1 | 2e-05 | 7/18 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.7 | 1e-04 | 12/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.003 | 6/34 (SW 900, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +4.0 | 0.003 | 2/21 (HOP62, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.003 | 13/44 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.013 | 5/44 (KATO III, SNU-423, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.019 | 8/41 (C32, SW480, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.74×** | +3.4 | 0.027 | 0/37 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.052 | 5/34 (NCI-H23, A498, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.052 | 11/44 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.052 | 6/47 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.086 | 2/44 (HEC-1-A, SK-MEL-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -8.4 | 3e-14 | 30/46 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.456×** | -7.9 | 9e-13 | 29/44 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -7.1 | 3e-10 | 23/43 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.558×** | -5.7 | 1e-06 | 18/43 (A-172, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -5.4 | 9e-06 | 17/33 (MIA PaCa-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -3.7 | 0.023 | 13/43 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.693×** | -3.6 | 0.025 | 14/45 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.62 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0553× (z -10.5) |
| [[A549 (line)]] | wt | 4.32 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0523× (z -11.0) |
| [[J82 (line)]] | alt | 2.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0512× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 3.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 3.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.0) | — |
| [[A-427 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK16]] | +0.78 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.76 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[AMZ2P1]] | +0.72 | +0.80 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PEX12]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[PRR14]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DXO]] | +0.69 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[RAD52]] | +0.68 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[COQ5]] | +0.68 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[METTL25B]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF16]] | -0.60 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[HACD3]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[NIPA2]] | -0.58 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.58 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[CDK2]] | -0.58 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[TXN]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[BCAP31]] | -0.56 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TTL]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SPCS3]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.55 | -0.65 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGFR]] | B | NGFR activity raises AMZ2P1-1's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.18× lower at baseline in the lines without NGFR | 0.065 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[CLIP3]] | C | CLIP3 activity raises AMZ2P1-1's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without CLIP3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.4, 1.8); signed map (5.6, -20.8). **Vector** length 52.0, 7.03% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +5.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -8.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.5 |

## What is on record

> [!warning] No registry record
> AMZ2P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16601); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16601]; `tensor/DDL_lfc|DDL_z.npy` [16601]; `embed/gene_vectors.npy` [16601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16601 or target_col == 16601). Every well: [[AMZ2P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMZ2P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
