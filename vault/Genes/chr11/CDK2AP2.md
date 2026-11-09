---
symbol: "CDK2AP2"
type: "gene"
col: 9544
ensembl_id: "ENSG00000167797"
name: "cyclin dependent kinase 2 associated protein 2"
location: "11q13.2"
module: 40
arm: "+"
pooled_cpm: 30.19
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CDK2AP2

*cyclin dependent kinase 2 associated protein 2* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +10.8, q 2e-24, up in 46 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (A549 6.86×, SW480 5.29×, Panc 03.27 5.32×, CFPAC-1 3.56×, …); [[Panobinostat (drug)]] 0.5 µM in 4 lines (KATO III 4.35×, SW480 6.09×, NCI-H2347 4.42×, LS 180 4.43×); [[Adagrasib (drug)]] 0.05 µM in 3 lines (KATO III 1.48×, NCI-H2030 1.56×, NCI-H1573 1.55×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.644× (z -4.3, q 0.008, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (SW 900 0.199×; ⚠ cell-cycle shift, explains ~64% of this change); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (H4 0.0576×); [[Selinexor (drug)]] 0.5 µM in 1 line (SNU-1 0.0695×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TULP3]] (+0.71, fdr 7e-06), [[CRELD2]] (+0.71, fdr 7e-06), [[MINDY2]] (+0.71, fdr 7e-06); moves opposite to [[MRRF]] (-0.70, fdr 3e-05), [[FKTN]] (-0.68, fdr 1e-05), [[UTP20]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (A549 6.86×, SW480 5.29×, Panc 03.27 5.32×, CFPAC-1 3.56×, …); [[Panobinostat (drug)]] 0.5 µM in 4 lines (KATO III 4.35×, SW480 6.09×, NCI-H2347 4.42×, LS 180 4.43×); [[Adagrasib (drug)]] 0.05 µM in 3 lines (KATO III 1.48×, NCI-H2030 1.56×, NCI-H1573 1.55×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +10.8 | 2e-24 | 46/47 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.98×** | +9.6 | 2e-19 | 47/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.50×** | +9.5 | 2e-19 | 48/48 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.25×** | +5.6 | 3e-06 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.11×** | +5.2 | 3e-05 | 37/43 (KATO III, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.86×** | +4.3 | 0.002 | 35/47 (SW480, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.64× | +3.2 | 0.13 | 28/47 (HOP62, KATO III, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.57× | +3.1 | 0.13 | 21/39 (A-427, LOX-IMVI, …) | two highest doses | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (SW 900 0.199×; ⚠ cell-cycle shift, explains ~64% of this change); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (H4 0.0576×); [[Selinexor (drug)]] 0.5 µM in 1 line (SNU-1 0.0695×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.644×** | -4.3 | 0.008 | 28/48 (SW 900, COLO 205, …) | rises with dose | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.584×** | -3.7 | 0.052 | 28/47 (HT-29, A-172, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.402× | -3.3 | 0.18 | 25/48 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bestatin (drug)]] 5 µM |  | 0.630× | -3.1 | 0.28 | 26/47 (RKO, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +10.2) | — |
| [[J82 (line)]] | alt | 33.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.8) | — |
| [[KATO III (line)]] | alt | 89.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.35× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 73.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +9.1) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 31.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.42× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +11.9) | — |
| [[SW480 (line)]] | alt | 18.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +12.2) | — |
| [[A-427 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.1) | — |
| [[C32 (line)]] | wt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 39.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +10.4) | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0576× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +8.8) | — |
| [[LoVo (line)]] | wt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 41.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.43× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 75.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +9.3) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +8.7) ⚠ position not correctable | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0695× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.199× (z -12.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW1417 (line)]] | alt | 67.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP3]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CRELD2]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.71 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DNAJB9]] | +0.69 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[SYVN1]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SUCO]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[KMT5C]] | +0.66 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NARF]] | +0.66 | +0.43 / +0.72 | both halves | 4e-05 |  |
| [[ERLEC1]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[LGALS1]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRRF]] | -0.70 | -0.43 / -0.75 | both halves | 3e-05 |  |
| [[FKTN]] | -0.68 | -0.49 / -0.75 | both halves | 1e-05 |  |
| [[UTP20]] | -0.67 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[RRP15]] | -0.67 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[TMX3]] | -0.62 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.62 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.61 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[METAP1D]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.60 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[MTMR2]] | -0.60 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[CCT2]] | -0.59 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.59 | -0.42 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CDK2AP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC1A1]] | B | SLC1A1 activity weakens CDK2AP2's drug response | lines that do not express SLC1A1 (11) vs lines expressing it (37) | the lines without SLC1A1 respond 1.00× as strongly (z diff +0.04); strongest at Belinostat 5 µM: 2.63x vs 1.72x (z diff -1.6) | 0.096 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (6.2, -34.2); signed map (-25.1, 15.1). **Vector** length 98.2, 30.4% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.3 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | +2.9 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.6 | +4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.3 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.5 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 2 associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,506,497-67,508,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DOC-1R, p14 |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [O75956](https://www.uniprot.org/uniprotkb/O75956) (Cyclin-dependent kinase 2-associated protein 2):

> Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Inhibits cell cycle G1/S phase transition by repressing CDK2 expression and activation; represses CDK2 activation by inhibiting its interaction with cyclin E and A. Plays a role in regulating the self-renewal of embryonic stem cells (ESCs) and in maintaining cell survival during terminal differentiation of ESCs (By similarity). Regulates microtubule organization of metaphase II oocytes …

**Summary**, from NCBI Gene [10263](https://www.ncbi.nlm.nih.gov/gene/10263):

> This gene encodes a protein that interacts with cyclin-dependent kinase 2 associated protein 1. Pseudogenes associated with this gene are located on chromosomes 7 and 9. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:30833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30833) · Entrez [10263](https://www.ncbi.nlm.nih.gov/gene/10263) · UniProt [O75956](https://www.uniprot.org/uniprotkb/O75956) · Ensembl [ENSG00000167797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167797)

## Data

Gene col 9544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9544); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9544]; `tensor/DDL_lfc|DDL_z.npy` [9544]; `embed/gene_vectors.npy` [9544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9544 or target_col == 9544). Every well: [[CDK2AP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK2AP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
