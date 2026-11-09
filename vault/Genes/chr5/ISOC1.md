---
symbol: "ISOC1"
type: "gene"
col: 832
ensembl_id: "ENSG00000066583"
name: "isochorismatase domain containing 1"
location: "5q23.3"
module: 52
arm: "-"
pooled_cpm: 15.1
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# ISOC1

*isochorismatase domain containing 1* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +20.0, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.904× (z -6.2, q 3e-07, down in 10 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.772× (z -4.6, q 0.001, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (SW48 0.160×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (Hs 766T 0.0963×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf29]] (+0.61, fdr 7e-06), [[ZDHHC23]] (+0.60, fdr 1e-05), [[OGFRL1]] (+0.58, fdr 1e-05); moves opposite to [[EMC3]] (-0.62, fdr 1e-05), [[MEF2B]] (-0.60, fdr 4e-05), [[VRK3]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZDHHC23]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +20.0 | 0e+00 | 38/46 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +12.3 | 1e-32 | 39/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +11.6 | 8e-29 | 37/47 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.80×** | +10.4 | 4e-23 | 29/38 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.69×** | +8.9 | 8e-17 | 18/24 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-13 | 24/48 (PANC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.57×** | +7.6 | 2e-12 | 25/44 (LoVo, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.3 | 2e-11 | 25/47 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.2 | 5e-11 | 23/43 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.48×** | +6.9 | 2e-10 | 22/46 (HepG2/C3A, BT-474, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.41×** | +6.1 | 6e-08 | 24/47 (HepG2/C3A, BT-474, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 9e-06 | 19/47 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.34×** | +5.2 | 1e-05 | 15/42 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.30×** | +4.6 | 2e-04 | 16/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.29×** | +4.4 | 3e-04 | 18/47 (C32, NCI-H23, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 13/48 (C32, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.005 | 9/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.023 | 15/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.038 | 11/48 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.081 | 4/46 (HCT15, A-172, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.19× | +2.9 | 0.081 | 4/47 (HOP62, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 832.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (SW48 0.160×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (Hs 766T 0.0963×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -6.2 | 3e-07 | 10/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.772×** | -4.6 | 0.001 | 15/47 (HEC-1-A, A498, …) | two highest doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.828× | -3.4 | 0.15 | 12/47 (CHP-212, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.828× | -3.2 | 0.15 | 14/47 (NCI-H23, HS-578T, …) | two highest doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.880× | -3.2 | 0.15 | 5/48 (A549, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 23.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 8.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +13.0) | — |
| [[A498 (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.9) | — |
| [[A549 (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 9.72 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0963× (z -8.7) |
| [[HT-29 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.3) | — |
| [[J82 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.4) | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.160× (z -8.8) |
| [[SW480 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf29]] | +0.61 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ZDHHC23]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[OGFRL1]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ARRB1]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 | same gene group |
| [[MTARC2]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CACHD1]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 | same gene group |
| [[RFK]] | +0.56 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TIFA]] | +0.56 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[TMEM64]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AGL]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ALDH9A1]] | +0.55 | +0.64 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[AMACR]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC3]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[MEF2B]] | -0.60 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[VRK3]] | -0.60 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[DRD4]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[APTX]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SAMD4B]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[VPS53]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MARK4]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[UBOX5]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SENP5]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC23]] | B | ZDHHC23 activity raises ISOC1's level | lines that do not express ZDHHC23 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without ZDHHC23 | 0.0998 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.6, -2.2); signed map (23.5, -34.9). **Vector** length 78.7, 14.7% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +20.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | isochorismatase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:129,094,749-129,114,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-111 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

UniProt [Q96CN7](https://www.uniprot.org/uniprotkb/Q96CN7) carries no function annotation.

**Summary**, from NCBI Gene [51015](https://www.ncbi.nlm.nih.gov/gene/51015):

> Predicted to be located in peroxisome. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24254) · Entrez [51015](https://www.ncbi.nlm.nih.gov/gene/51015) · UniProt [Q96CN7](https://www.uniprot.org/uniprotkb/Q96CN7) · Ensembl [ENSG00000066583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066583)

## Data

Gene col 832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 832); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 832]; `tensor/DDL_lfc|DDL_z.npy` [832]; `embed/gene_vectors.npy` [832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 832 or target_col == 832). Every well: [[ISOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
