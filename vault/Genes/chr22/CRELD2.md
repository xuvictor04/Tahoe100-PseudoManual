---
symbol: "CRELD2"
type: "gene"
col: 11497
ensembl_id: "ENSG00000184164"
name: "CRELD disulfide isomerase 2"
location: "22q13.33"
module: 42
arm: "+"
pooled_cpm: 19.77
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CRELD2

*CRELD disulfide isomerase 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.42× (z +14.2, q 3e-43, up in 45 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H1792 7.77×, SW480 5.45×, Hs 766T 6.29×, CFPAC-1 5.78×, …); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 8.82×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 7.47×; ⚠ cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.578× (z -6.4, q 1e-07, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (LS 180 0.191×, NCI-H1573 0.341×; ⚠ cell-cycle shift, explains ~38% of this change); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (A549 0.0481×); [[TAK-901 (drug)]] 0.05 µM in 1 line (RPMI-7951 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK2AP2]] (+0.71, fdr 7e-06), [[MANF]] (+0.70, fdr 7e-06), [[SYVN1]] (+0.66, fdr 7e-06); moves opposite to [[TGFBRAP1]] (-0.54, fdr 3e-05), [[FKTN]] (-0.54, fdr 1e-04), [[POLR1F]] (-0.53, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H1792 7.77×, SW480 5.45×, Hs 766T 6.29×, CFPAC-1 5.78×, …); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 8.82×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 7.47×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +14.2 | 3e-43 | 45/45 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.66×** | +10.6 | 6e-24 | 38/39 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.30×** | +9.8 | 2e-20 | 46/47 (SW480, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **3.01×** | +9.0 | 2e-17 | 46/47 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.47×** | +7.1 | 1e-10 | 26/30 (SW480, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.39×** | +6.6 | 4e-09 | 28/34 (J82, A-172, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +6.0 | 2e-07 | 36/47 (SW480, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.04×** | +5.8 | 4e-07 | 37/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.88×** | +5.0 | 5e-05 | 34/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.77×** | +4.5 | 4e-04 | 24/41 (SW480, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.68×** | +4.1 | 0.002 | 28/45 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.49×** | +3.3 | 0.053 | 20/43 (SW48, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Lipoic acid (drug)]] 5 µM |  | 1.30× | +3.0 | 0.10 | 16/47 (PANC-1, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (LS 180 0.191×, NCI-H1573 0.341×; ⚠ cell-cycle shift, explains ~38% of this change); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (A549 0.0481×); [[TAK-901 (drug)]] 0.05 µM in 1 line (RPMI-7951 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.578×** | -6.4 | 1e-07 | 34/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.597×** | -4.3 | 0.006 | 26/47 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.467× | -3.3 | 0.16 | 17/47 (SHP-77, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.469× | -3.3 | 0.16 | 22/45 (H4, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.771× | -3.0 | 0.24 | 19/47 (C32, CHP-212, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.496× | -3.0 | 0.24 | 15/47 (HS-578T, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.56 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.0) | [[Selinexor (drug)]] 5 µM 0.341× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 26.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.2) | — |
| [[A549 (line)]] | wt | 8.41 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +9.3) | [[Hydroxyurea (drug)]] 0.5 µM 0.0481× (z -12.1) |
| [[PANC-1 (line)]] | alt | 17.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 66.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 6.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +12.5) | — |
| [[J82 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.3) | — |
| [[KATO III (line)]] | alt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.8) | — |
| [[LoVo (line)]] | wt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.191× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.46× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 7.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.102× (z -9.3) |
| [[SHP-77 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-423 (line)]] | alt | 8.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +9.1) | — |
| [[A-172 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2AP2]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[MANF]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 | STRING 936 |
| [[SYVN1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 | STRING 426 |
| [[GMPPB]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 | STRING 755 |
| [[CALR]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | STRING 519 |
| [[PDIA4]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | STRING 819 |
| [[TMEM50B]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[HYOU1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 | STRING 800 |
| [[TMED9]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.63 | +0.57 / +0.63 | both halves | 8e-06 | STRING 511 |
| [[DNAJC3]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 | STRING 479 |
| [[P4HB]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | STRING 437 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBRAP1]] | -0.54 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[FKTN]] | -0.54 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[POLR1F]] | -0.53 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[DNAH14]] | -0.52 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[SLC25A13]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SSB]] | -0.51 | -0.21 / -0.59 | both halves | 7e-04 |  |
| [[ZNF354B]] | -0.51 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ZNF260]] | -0.50 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[POGK]] | -0.50 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[ZNF507]] | -0.50 | -0.29 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CRELD2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -31.7); signed map (-53.7, 8.4). **Vector** length 92.0, 23.5% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Maturation of DENV proteins* (reactome, mean cos +0.53 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.52 to 12); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.6 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.2 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.0 | +10.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.5 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.5 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | CRELD disulfide isomerase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:49,918,167-49,927,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11256 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXH1](https://www.uniprot.org/uniprotkb/Q6UXH1) (Protein disulfide isomerase CRELD2):

> Protein disulfide isomerase (By similarity). Might play a role in the unfolded protein response (By similarity). May regulate transport of alpha4-beta2 neuronal acetylcholine receptor.

**Summary**, from NCBI Gene [79174](https://www.ncbi.nlm.nih.gov/gene/79174):

> Predicted to enable calcium ion binding activity and protein disulfide isomerase activity. Predicted to be located in Golgi apparatus and endoplasmic reticulum. Predicted to be active in extracellular matrix and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28150) · Entrez [79174](https://www.ncbi.nlm.nih.gov/gene/79174) · UniProt [Q6UXH1](https://www.uniprot.org/uniprotkb/Q6UXH1) · Ensembl [ENSG00000184164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184164)

## Data

Gene col 11497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11497); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11497]; `tensor/DDL_lfc|DDL_z.npy` [11497]; `embed/gene_vectors.npy` [11497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11497 or target_col == 11497). Every well: [[CRELD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRELD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
