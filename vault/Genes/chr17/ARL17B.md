---
symbol: "ARL17B"
type: "gene"
col: 13666
ensembl_id: "ENSG00000228696"
name: "ARF like GTPase 17B"
location: "17q21.31"
module: 4
arm: "-"
pooled_cpm: 40.88
n_lines_expressing: 25
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ARL17B

*ARF like GTPase 17B* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +11.6, q 4e-28, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.684× (z -5.7, q 7e-06, down in 12 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNAU1AP]] (+0.57, fdr 3e-05), [[KDM2A]] (+0.56, fdr 1e-05), [[KANSL1]] (+0.54, fdr 2e-05, ⚠ same locus), [[KPNB1-DT]] (+0.51, fdr 3e-05); moves opposite to [[PRELID3B]] (-0.54, fdr 4e-05), [[PRPF19]] (-0.52, fdr 4e-05), [[PDHA1]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[CCDC65]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +11.6 | 4e-28 | 9/22 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.0 | 7e-07 | 2/20 (LoVo, HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.0 | 1e-04 | 6/22 (hTERT-HPNE, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 3/22 (HT-29, LoVo, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.007 | 2/22 (hTERT-HPNE, SNU-423) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.013 | 3/22 (HCT15, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.053 | 0/23 | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.061 | 4/23 (SNU-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.3 | 0.063 | 2/19 (LoVo, SNU-423) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.22× | +3.1 | 0.12 | 6/22 (SHP-77, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 1.23× | +3.1 | 0.12 | 5/22 (A498, SHP-77, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.13 | 0/22 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.684×** | -5.7 | 7e-06 | 12/23 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.728×** | -4.9 | 2e-04 | 15/22 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.742×** | -4.7 | 6e-04 | 16/23 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.762×** | -4.2 | 0.003 | 12/22 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -4.0 | 0.006 | 11/22 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.808×** | -3.3 | 0.075 | 15/23 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.666×** | -3.3 | 0.075 | 12/23 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.812×** | -3.2 | 0.082 | 12/23 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.1 | 0.11 | 1/23 (AN3 CA) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.822× | -3.1 | 0.11 | 5/22 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.11 | 6/22 (HCT15, KATO III, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -27.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 244 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0313× (z -29.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -12.1) |
| [[HOP62 (line)]] | alt | 99.1 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -19.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 113 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -22.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -15.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 82.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0399× (z -29.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 110 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0857× (z -24.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 64.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -13.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 48.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -14.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 62.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -17.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 10.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.16× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0843× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 1271 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNAU1AP]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[KDM2A]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[KANSL1]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 | STRING 768; ⚠ same locus (49.4 kb, same strand: neighbours can correlate without regulation) |
| [[KPNB1-DT]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[CLDN18]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CSTB]] | +0.51 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[MRPS36]] ⚠ | +0.50 | +0.45 / +0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID4B]] | +0.49 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[ZNF345]] | +0.49 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[MICU1]] | +0.49 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[LINC00685]] | +0.49 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[ING2]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[PPP1R14B]] | +0.49 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[LINC02210-CRHR1]] | +0.49 | +0.46 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.54 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PRPF19]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PDHA1]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[OCRL]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ENTPD6]] | -0.51 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[RPE]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[RABGGTB]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MPV17L]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[SOAT1]] | -0.46 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[NONO]] | -0.46 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[ATP13A1]] | -0.46 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[LIN7C]] | -0.45 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL17B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ARL17B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC65]] | B | ARL17B activity raises CCDC65's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.11× lower at baseline in the lines without ARL17B | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |
| [[KANSL1]] | B | ARL17B activity raises KANSL1's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without ARL17B | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |
| [[PDHA1]] | B | ARL17B activity lowers PDHA1's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without ARL17B | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |
| [[ECT2L]] | B | ARL17B activity raises ECT2L's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.26× lower at baseline in the lines without ARL17B | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |
| [[KPNB1-DT]] | B | ARL17B activity raises KPNB1-DT's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.17× lower at baseline in the lines without ARL17B | 0.0998 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-39.2, -34.0); signed map (-30.9, 25.8). **Vector** length 63.9, 16.4% of its response variance represented; |z| ≥ 3 in 494 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +5.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +4.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.1 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.0 | +0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 17B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:46,274,784-46,361,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARL17 |
| Gene groups (HGNC) | ARF GTPase family; Proteins encoded by multiple genes |
| Matched by | ensembl_id |

**Function**, from UniProt [I3L3L1](https://www.uniprot.org/uniprotkb/I3L3L1) (Putative ADP-ribosylation factor-like protein 17B):

> Putative small GTP-binding protein cycling between an inactive GDP-bound and an active GTP-bound form.

**Summary**, from NCBI Gene [100506084](https://www.ncbi.nlm.nih.gov/gene/100506084):

> Predicted to enable GTP binding activity. Predicted to be involved in intracellular protein transport and vesicle-mediated transport. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32387) · Entrez [100506084](https://www.ncbi.nlm.nih.gov/gene/100506084) · UniProt [I3L3L1](https://www.uniprot.org/uniprotkb/I3L3L1) · Ensembl [ENSG00000228696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228696)

## Data

Gene col 13666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13666); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13666]; `tensor/DDL_lfc|DDL_z.npy` [13666]; `embed/gene_vectors.npy` [13666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13666 or target_col == 13666). Every well: [[ARL17B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL17B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
