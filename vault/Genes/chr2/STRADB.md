---
symbol: "STRADB"
type: "gene"
col: 1336
ensembl_id: "ENSG00000082146"
name: "STE20 related adaptor beta"
location: "2q33.1"
module: 29
arm: "+"
pooled_cpm: 10.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# STRADB

*STE20 related adaptor beta* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.48× (z +13.6, q 3e-39, up in 28 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.2, q 2e-22, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.556× (z -12.1, q 1e-30, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSL3]] (+0.68, fdr 1e-05), [[PDIA3P1]] (+0.67, fdr 1e-05), [[MOB1A]] (+0.65, fdr 1e-05); moves opposite to [[PILRB]] (-0.63, fdr 1e-05), [[MIDN]] (-0.58, fdr 3e-05), [[ZNF503]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +13.6 | 3e-39 | 28/33 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.5 | 2e-23 | 19/23 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.2 | 2e-22 | 32/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +7.8 | 1e-12 | 18/29 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 1e-05 | 18/47 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +5.3 | 1e-05 | 19/47 (C32, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.6 | 3e-04 | 15/44 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.004 | 13/48 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.010 | 12/47 (A-427, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.23× | +3.1 | 0.11 | 13/41 (SW 900, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.11 | 5/47 (SW480, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 1.47× | +3.0 | 0.11 | 0/41 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.556×** | -12.1 | 1e-30 | 39/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -9.6 | 2e-19 | 35/46 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -8.6 | 2e-15 | 32/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -7.9 | 5e-13 | 28/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -7.7 | 2e-12 | 26/47 (AN3 CA, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -7.1 | 1e-10 | 23/44 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -6.6 | 3e-09 | 25/46 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -5.9 | 2e-07 | 23/47 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.479×** | -5.8 | 5e-07 | 22/42 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.701×** | -5.3 | 6e-06 | 21/44 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -4.6 | 2e-04 | 18/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -4.2 | 0.001 | 19/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -3.5 | 0.021 | 12/46 (H4, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.807×** | -3.2 | 0.053 | 8/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.745×** | -3.2 | 0.060 | 3/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.4) |
| [[A549 (line)]] | wt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -12.7) |
| [[LS 180 (line)]] | wt | 9.26 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0667× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.3) |
| [[PANC-1 (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -9.3) |
| [[A-172 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.9) |
| [[HCT15 (line)]] | alt | 7.06 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0581× (z -8.6) |
| [[KATO III (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 8.53 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -9.3) |
| [[SHP-77 (line)]] | alt | 8.85 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.120× (z -8.9) |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -8.7) |
| [[SW 900 (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSL3]] | +0.68 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PDIA3P1]] | +0.67 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RAB11FIP2]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SCARB2]] | +0.65 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[TWF1]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PCGF5]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ERAP1]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.62 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CIPC]] | +0.62 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[EEF1A1P5]] | +0.62 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[SETD7]] | +0.62 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRB]] | -0.63 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MIDN]] | -0.58 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ZNF503]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ZNF316]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MAP1S]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FBXO46]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SRSF9]] ⚠ | -0.55 | -0.54 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHMP1A]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[NTMT1]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[GGT7]] | -0.54 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PIAS4]] | -0.54 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ABAT]] | -0.53 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[VPS37C]] | -0.53 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STRADB's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-11.6, 15.1); signed map (-18.1, -36.1). **Vector** length 57.3, 7.98% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -7.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.5 | +0.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.2 | +0.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | STE20 related adaptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,387,858-201,480,846 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STLK6, CALS-21, PAPK, ILPIPA, ILPIP; previously ALS2CR2 |
| Gene groups (HGNC) | Pseudokinases |
| Reactome | 2 pathways, smallest: Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0K7](https://www.uniprot.org/uniprotkb/Q9C0K7) (STE20-related kinase adapter protein beta):

> Pseudokinase which, in complex with CAB39/MO25 (CAB39/MO25alpha or CAB39L/MO25beta), binds to and activates STK11/LKB1. Adopts a closed conformation typical of active protein kinases and binds STK11/LKB1 as a pseudosubstrate, promoting conformational change of STK11/LKB1 in an active conformation (By similarity).

**Summary**, from NCBI Gene [55437](https://www.ncbi.nlm.nih.gov/gene/55437):

> This gene encodes a protein that belongs to the serine/threonine protein kinase STE20 subfamily. One of the active site residues in the protein kinase domain of this protein is altered, and it is thus a pseudokinase. This protein is a component of a complex involved in the activation of serine/threonine kinase 11, a master kinase that regulates cell polarity and energy-generating metabolism. This complex regulates the relocation of this kinase from the nucleus to the cytoplasm, and it is …

**Accessions** — [HGNC:13205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13205) · Entrez [55437](https://www.ncbi.nlm.nih.gov/gene/55437) · UniProt [Q9C0K7](https://www.uniprot.org/uniprotkb/Q9C0K7) · Ensembl [ENSG00000082146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082146)

## Data

Gene col 1336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1336); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1336]; `tensor/DDL_lfc|DDL_z.npy` [1336]; `embed/gene_vectors.npy` [1336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1336 or target_col == 1336). Every well: [[STRADB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRADB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
