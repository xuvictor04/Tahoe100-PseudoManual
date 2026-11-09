---
symbol: "RAB24"
type: "gene"
col: 9777
ensembl_id: "ENSG00000169228"
name: "RAB24, member RAS oncogene family"
location: "5q35.3"
module: 24
arm: "+"
pooled_cpm: 8.71
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RAB24

*RAB24, member RAS oncogene family* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.17× (z +5.3, q 6e-05, up in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +5.0, q 1e-04, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.567× (z -5.7, q 6e-06, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WBP1]] (+0.64, fdr 7e-06), [[RPAIN]] (+0.64, fdr 1e-05), [[APBA3]] (+0.62, fdr 7e-06); moves opposite to [[IPO5]] (-0.61, fdr 1e-05), [[TARDBP]] (-0.60, fdr 3e-05), [[PRKDC]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NEURL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.3 | 6e-05 | 11/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.68×** | +5.2 | 6e-05 | 18/32 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.0 | 1e-04 | 21/43 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.62×** | +4.6 | 5e-04 | 5/18 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.6 | 6e-04 | 20/39 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +4.2 | 0.003 | 18/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +3.7 | 0.016 | 15/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.020 | 16/42 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.020 | 13/42 (A-172, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.026 | 13/48 (H4, KATO III, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.41×** | +3.4 | 0.029 | 17/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.08×** | +3.4 | 0.031 | 10/41 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.07×** | +3.4 | 0.031 | 4/44 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.043 | 10/42 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.01×** | +3.3 | 0.043 | 9/44 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.052 | 10/42 (NCI-H1573, HS-578T, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.053 | 10/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -5.7 | 6e-06 | 24/47 (H4, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -5.2 | 4e-05 | 26/48 (LoVo, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.676×** | -3.7 | 0.047 | 14/47 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -3.5 | 0.059 | 16/41 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.710×** | -3.5 | 0.059 | 11/48 (Hs 766T, J82, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -3.4 | 0.070 | 18/47 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.27 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.196× (z -8.6) |
| [[BT-474 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 7.71 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0723× (z -8.5) |
| [[LoVo (line)]] | wt | 5.89 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 5.39 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0729× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 7.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 9.04 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 9.93 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0782× (z -8.7) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RPAIN]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[APBA3]] | +0.62 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[GALT]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ENKD1]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[VPS37D]] | +0.60 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[SAT2]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PEX16]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[NFKBIL1]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[NAT14]] | +0.58 | +0.38 / +0.61 | both halves | 6e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.61 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.60 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.60 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[NUP155]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.57 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[CCT5]] | -0.57 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[DARS2]] | -0.56 | -0.37 / -0.64 | both halves | 7e-05 |  |
| [[MOB1A]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[VMA21]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ACTR2]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL3]] | B | NEURL3 activity raises RAB24's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without NEURL3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.9, -30.1); signed map (-15.9, -1.2). **Vector** length 61.8, 10.8% of its response variance represented; |z| ≥ 3 in 630 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB24, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,301,198-177,303,744 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 3 pathways, smallest: RAB geranylgeranylation; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969Q5](https://www.uniprot.org/uniprotkb/Q969Q5) (Ras-related protein Rab-24):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB24 is an atypical RAB protein that presents low GTPase activity and thereby exists predominantly in the GTP-bound …

**Summary**, from NCBI Gene [53917](https://www.ncbi.nlm.nih.gov/gene/53917):

> RAB24 is a small GTPase of the Rab subfamily of Ras-related proteins that regulate intracellular protein trafficking (Olkkonen et al., 1993 [PubMed 8126105]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:9765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9765) · Entrez [53917](https://www.ncbi.nlm.nih.gov/gene/53917) · UniProt [Q969Q5](https://www.uniprot.org/uniprotkb/Q969Q5) · Ensembl [ENSG00000169228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169228)

## Data

Gene col 9777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9777); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9777]; `tensor/DDL_lfc|DDL_z.npy` [9777]; `embed/gene_vectors.npy` [9777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9777 or target_col == 9777). Every well: [[RAB24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
