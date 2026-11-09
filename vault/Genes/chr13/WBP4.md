---
symbol: "WBP4"
type: "gene"
col: 4204
ensembl_id: "ENSG00000120688"
name: "WW domain binding protein 4"
location: "13q14.11"
module: 20
arm: "-"
pooled_cpm: 43.71
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# WBP4

*WW domain binding protein 4* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +14.6, q 1e-45, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.748× (z -4.3, q 0.009, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNK]] (+0.71, fdr 7e-06), [[ANKRD49]] (+0.69, fdr 7e-06), [[UBXN2A]] (+0.68, fdr 1e-05); moves opposite to [[BLTP2]] (-0.67, fdr 1e-05), [[TMED7]] (-0.67, fdr 7e-06), [[GNB1L]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SHOX2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[N4BP2L2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +14.6 | 1e-45 | 45/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.6 | 9e-29 | 40/48 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +11.3 | 4e-27 | 45/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +10.1 | 6e-22 | 43/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.1 | 1e-10 | 34/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +6.9 | 4e-10 | 37/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.7 | 1e-06 | 31/47 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 3e-06 | 34/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.47×** | +5.5 | 3e-06 | 26/41 (Panc 03.27, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.0 | 3e-05 | 30/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.39×** | +4.8 | 7e-05 | 26/48 (J82, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 28/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 27/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 21/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.3 | 0.031 | 20/47 (KATO III, H4, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.039 | 22/48 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.066 | 19/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.748×** | -4.3 | 0.009 | 30/48 (A498, Hs 766T, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.2 | 0.39 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.0) | — |
| [[KATO III (line)]] | alt | 48.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 42.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.3) | — |
| [[A498 (line)]] | wt | 35.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.7) | — |
| [[J82 (line)]] | alt | 56.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 37.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.1) | — |
| [[A-172 (line)]] | wt | 49.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.4) | — |
| [[C32 (line)]] | wt | 36.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.6) | — |
| [[SW48 (line)]] | wt | 32.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +13.5) | — |
| [[A-427 (line)]] | wt | 52.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[A549 (line)]] | wt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 92.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.7) | — |
| [[H4 (line)]] | wt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 57.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.7) | — |
| [[LoVo (line)]] | wt | 37.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.56× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 59.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 66.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.0) | — |
| [[RKO (line)]] | wt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +12.3) | — |
| [[SW480 (line)]] | alt | 58.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[UBXN2A]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[UPF3B]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ITSN2]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.66 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TCEAL4]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RSF1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP2]] | -0.67 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[TMED7]] | -0.67 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[GNB1L]] | -0.64 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[ST6GALNAC4]] | -0.62 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[GGCT]] | -0.62 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[DCAF13]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.61 | -0.76 / -0.65 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TRAP1]] | -0.60 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[TTLL12]] | -0.60 | -0.63 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHOX2]] | B | SHOX2 activity raises WBP4's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without SHOX2 | 0.085 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[N4BP2L2]] | C | WBP4's natural level strengthens N4BP2L2's drug response | WBP4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.14; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.2, -25.2); signed map (3.8, -12.0). **Vector** length 102, 27.8% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +11.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | WW domain binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,061,509-41,084,006 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBP21, MGC117310 |
| Gene groups (HGNC) | Zinc fingers matrin-type; Spliceosomal B complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O75554](https://www.uniprot.org/uniprotkb/O75554) (WW domain-binding protein 4):

> Involved in pre-mRNA splicing as a component of the spliceosome. May play a role in cross-intron bridging of U1 and U2 snRNPs in the mammalian A complex.

**Summary**, from NCBI Gene [11193](https://www.ncbi.nlm.nih.gov/gene/11193):

> This gene encodes WW domain-containing binding protein 4. The WW domain represents a small and compact globular structure that interacts with proline-rich ligands. This encoded protein is a general spliceosomal protein that may play a role in cross-intron bridging of U1 and U2 snRNPs in the spliceosomal complex A. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12739) · Entrez [11193](https://www.ncbi.nlm.nih.gov/gene/11193) · UniProt [O75554](https://www.uniprot.org/uniprotkb/O75554) · Ensembl [ENSG00000120688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120688)

## Data

Gene col 4204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4204); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4204]; `tensor/DDL_lfc|DDL_z.npy` [4204]; `embed/gene_vectors.npy` [4204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4204 or target_col == 4204). Every well: [[WBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
