---
symbol: "LRRC45"
type: "gene"
col: 9835
ensembl_id: "ENSG00000169683"
name: "leucine rich repeat containing 45"
location: "17q25.3"
module: 6
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# LRRC45

*leucine rich repeat containing 45* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.26× (z +11.1, q 5e-26, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.38× (z +3.6, q 0.026, up in 11 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.320× (z -8.8, q 7e-16, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PASK]] (+0.66, fdr 9e-06), [[RECQL4]] (+0.64, fdr 1e-05), [[FANCG]] (+0.64, fdr 9e-06); moves opposite to [[XIAP]] (-0.53, fdr 2e-05), [[DYNLRB1]] (-0.53, fdr 4e-05), [[ATG12]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SARDH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.26×** | +11.1 | 5e-26 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.79×** | +10.6 | 6e-24 | 13/15 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.34×** | +8.9 | 1e-16 | 5/5 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.91×** | +5.2 | 3e-05 | 11/44 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.6 | 5e-04 | 7/17 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.9 | 0.008 | 10/47 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.026 | 11/39 (LoVo, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.026 | 9/44 (KATO III, NCI-H1792, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.028 | 4/44 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.53×** | +3.4 | 0.043 | 5/42 (NCI-H1573, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.081 | 4/46 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.086 | 9/41 (HepG2/C3A, RKO, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.70× | +3.0 | 0.11 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.320×** | -8.8 | 7e-16 | 29/38 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.383×** | -7.7 | 3e-12 | 27/41 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.384×** | -7.7 | 3e-12 | 26/38 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.386×** | -7.6 | 3e-12 | 26/45 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -6.9 | 4e-10 | 23/32 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -6.5 | 5e-09 | 20/30 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.474×** | -6.0 | 2e-07 | 22/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -4.3 | 0.001 | 11/24 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -4.1 | 0.003 | 10/35 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.605×** | -4.0 | 0.003 | 9/44 (SNU-1, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.606×** | -4.0 | 0.003 | 13/42 (KATO III, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.628×** | -3.7 | 0.009 | 14/40 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.634×** | -3.7 | 0.010 | 13/43 (Panc 03.27, RKO, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.725×** | -3.7 | 0.010 | 12/44 (LOX-IMVI, LS 180, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.650×** | -3.5 | 0.020 | 8/44 (SW480, CHP-212, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.025 | 12/41 (NCI-H23, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -3.3 | 0.028 | 13/38 (A-427, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -3.1 | 0.065 | 6/28 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.65 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0570× (z -11.9) |
| [[J82 (line)]] | alt | 3.68 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0550× (z -14.3) |
| [[SW480 (line)]] | alt | 4.96 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -11.8) |
| [[A-427 (line)]] | wt | 4.31 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0678× (z -8.9) |
| [[HOP62 (line)]] | alt | 2.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0464× (z -9.7) |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0277× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0310× (z -10.4) |
| [[A-172 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASK]] | +0.66 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[RECQL4]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FANCG]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PCYOX1L]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 | STRING 424 |
| [[TONSL]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SAPCD1]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DDX12P]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SHMT1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SLC37A4]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RAD54L]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XIAP]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[DYNLRB1]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ATG12]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ARHGAP5]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CPEB4]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SARDH]] | B | SARDH activity raises LRRC45's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.29× lower at baseline in the lines without SARDH | 0.040 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises LRRC45's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without TCF19 | 0.057 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PRR36]] | B | PRR36 activity raises LRRC45's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.33× lower at baseline in the lines without PRR36 | 0.088 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[YBX2]] | B | YBX2 activity raises LRRC45's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.17× lower at baseline in the lines without YBX2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[GSTM4]] | C | GSTM4 activity raises LRRC45's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without GSTM4 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises LRRC45's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.04× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.3, -43.7); signed map (-34.2, -38.6). **Vector** length 58.4, 8.75% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.5 | +10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.8 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,023,305-82,031,151 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20806 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CN5](https://www.uniprot.org/uniprotkb/Q96CN5) (Leucine-rich repeat-containing protein 45):

> Component of the proteinaceous fiber-like linker between two centrioles, required for centrosome cohesion. Is probably involved in the early stages of ciliogenesis. Plays a role in the organization of centriolar satellites, likely by regulating the accumulation of centriolar satellite proteins, such as PCM1 and SSX2IP, at the centrosome.

**Summary**, from NCBI Gene [201255](https://www.ncbi.nlm.nih.gov/gene/201255):

> Involved in cilium assembly and protein localization to centriolar satellite. Located in centriole; centrosome; and ciliary basal body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28302) · Entrez [201255](https://www.ncbi.nlm.nih.gov/gene/201255) · UniProt [Q96CN5](https://www.uniprot.org/uniprotkb/Q96CN5) · Ensembl [ENSG00000169683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169683)

## Data

Gene col 9835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9835); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9835]; `tensor/DDL_lfc|DDL_z.npy` [9835]; `embed/gene_vectors.npy` [9835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9835 or target_col == 9835). Every well: [[LRRC45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
