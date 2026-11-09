---
symbol: "SRA1"
type: "gene"
col: 13110
ensembl_id: "ENSG00000213523"
name: "steroid receptor RNA activator 1"
location: "5q31.3"
module: 52
arm: "+"
pooled_cpm: 38.82
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SRA1

*steroid receptor RNA activator 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.15× (z +10.3, q 3e-22, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.694× (z -6.6, q 2e-08, down in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.605× (z -6.5, q 2e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF4]] (+0.72, fdr 7e-06), [[GOSR2]] (+0.69, fdr 7e-06), [[C11orf24]] (+0.69, fdr 7e-06); moves opposite to [[USP24]] (-0.63, fdr 1e-05), [[SLC25A13]] (-0.54, fdr 1e-05), [[NCKAP1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TAF13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.15×** | +10.3 | 3e-22 | 44/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.38×** | +6.0 | 6e-07 | 27/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.3 | 2e-05 | 26/48 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +5.2 | 3e-05 | 30/49 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 3e-05 | 27/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.0 | 6e-05 | 26/47 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.44×** | +4.6 | 4e-04 | 23/42 (A498, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.74×** | +3.9 | 0.006 | 28/48 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.16 | 0/49 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.694×** | -6.6 | 2e-08 | 34/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.605×** | -6.5 | 2e-08 | 32/48 (J82, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -5.3 | 2e-05 | 27/40 (SK-MEL-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.768×** | -4.9 | 1e-04 | 27/48 (A549, SHP-77, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.721×** | -4.3 | 0.002 | 28/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -4.2 | 0.002 | 25/48 (HS-578T, AsPC-1, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.552×** | -4.2 | 0.002 | 26/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.563×** | -4.1 | 0.004 | 27/48 (HS-578T, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.745×** | -4.0 | 0.005 | 25/48 (SW 900, A-427, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.006 | 24/47 (A498, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.734×** | -3.9 | 0.006 | 23/48 (A-427, NCI-H1573, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -3.8 | 0.007 | 21/47 (H4, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.014 | 19/48 (SW 1088, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.767×** | -3.6 | 0.014 | 23/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.733×** | -3.5 | 0.021 | 19/48 (AsPC-1, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 49.6 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.12× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.02× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +13.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.57× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 41.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 36.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[A-427 (line)]] | wt | 58.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.405× (z -11.9) |
| [[A498 (line)]] | wt | 53.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.98× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AsPC-1 (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.476× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.245× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.24× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.48× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 29.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.83× (z +10.1) | — |
| [[A549 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF4]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[C11orf24]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ATG101]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[HM13]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[TAF13]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TRIM3]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TMEM104]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[COQ10B]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PRKAG1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FOXRED1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[NCKAP1]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 | STRING 900 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAF13]] | C | SRA1's natural level weakens TAF13's drug response | SRA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.03; direction clear | 0.018 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (12.2, -27.6); signed map (-49.6, 6.0). **Vector** length 121, 34.6% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.1 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.0 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.6 | -6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.6 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | steroid receptor RNA activator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,537,340-140,557,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRA, STRAA1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD15](https://www.uniprot.org/uniprotkb/Q9HD15) (Steroid receptor RNA activator 1):

> Functional RNA which acts as a transcriptional coactivator that selectively enhances steroid receptor-mediated transactivation ligand-independently through a mechanism involving the modulating N-terminal domain (AF-1) of steroid receptors. Also mediates transcriptional coactivation of steroid receptors ligand-dependently through the steroid-binding domain (AF-2). Enhances cellular proliferation and differentiation and promotes apoptosis in vivo. May play a role in tumorigenesis.

**Summary**, from NCBI Gene [10011](https://www.ncbi.nlm.nih.gov/gene/10011):

> Both long non-coding and protein-coding RNAs are transcribed from this gene, and they represent alternatively spliced transcript variants. This gene was initially defined as a non-coding RNA, which is a coactivator for several nuclear receptors (NRs) and is associated with breast cancer. It has now been found that this gene is involved in the regulation of many NR and non-NR activities, including metabolism, adipogenesis and chromatin organization. The long non-coding RNA transcripts interact …

**Accessions** — [HGNC:11281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11281) · Entrez [10011](https://www.ncbi.nlm.nih.gov/gene/10011) · UniProt [Q9HD15](https://www.uniprot.org/uniprotkb/Q9HD15) · Ensembl [ENSG00000213523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213523)

## Data

Gene col 13110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13110); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13110]; `tensor/DDL_lfc|DDL_z.npy` [13110]; `embed/gene_vectors.npy` [13110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13110 or target_col == 13110). Every well: [[SRA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
