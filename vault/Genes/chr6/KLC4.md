---
symbol: "KLC4"
type: "gene"
col: 5979
ensembl_id: "ENSG00000137171"
name: "kinesin light chain 4"
location: "6p21.1"
module: 41
arm: "+"
pooled_cpm: 25.11
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# KLC4

*kinesin light chain 4* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +12.7, q 2e-34, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.524× (z -12.2, q 2e-31, down in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.678× (z -7.0, q 5e-10, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG7]] (+0.75, fdr 7e-06), [[ZNF547]] (+0.70, fdr 7e-06), [[ERCC5]] (+0.70, fdr 7e-06); moves opposite to [[VMA21]] (-0.66, fdr 7e-06), [[ATIC]] (-0.66, fdr 7e-06), [[RUVBL1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +12.7 | 2e-34 | 37/48 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 2e-04 | 23/46 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.9 | 2e-04 | 19/47 (NCI-H23, LOX-IMVI, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.005 | 18/48 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.0 | 0.007 | 18/45 (LOX-IMVI, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.12 | 13/47 (C-33 A, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.17 | 7/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.524×** | -12.2 | 2e-31 | 41/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.678×** | -7.0 | 5e-10 | 30/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -6.8 | 2e-09 | 31/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.690×** | -6.7 | 2e-09 | 27/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -6.6 | 5e-09 | 26/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.726×** | -6.0 | 2e-07 | 22/48 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -5.8 | 4e-07 | 25/48 (HS-578T, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.727×** | -5.8 | 6e-07 | 20/35 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.761×** | -5.1 | 2e-05 | 23/47 (C-33 A, NCI-H1792, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -4.6 | 3e-04 | 17/48 (SW1417, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -4.4 | 5e-04 | 17/47 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.639×** | -4.4 | 5e-04 | 21/48 (SW 900, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.810×** | -4.0 | 0.003 | 20/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.818×** | -3.8 | 0.006 | 21/48 (CFPAC-1, SNU-423, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.812×** | -3.8 | 0.006 | 19/47 (hTERT-HPNE, A-427, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.683×** | -3.7 | 0.006 | 11/48 (CFPAC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.841× | -3.2 | 0.033 | 10/48 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.037 | 14/47 (SW48, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.045 | 17/47 (SW 900, A498, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.056 | 16/48 (HCT15, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.892× | -3.0 | 0.062 | 11/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.062 | 6/48 (H4, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.112× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 21.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.118× (z -8.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 23.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A549 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.106× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -8.8) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -9.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[LOX-IMVI (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0623× (z -8.8) |
| [[SW480 (line)]] | alt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.0) | — |
| [[A-172 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[ZNF547]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ERCC5]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CCDC115]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ZNF490]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.68 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[CWC25]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[TNXB]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.66 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[ATIC]] | -0.66 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[RUVBL1]] | -0.65 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[DPH6]] | -0.63 | -0.60 / -0.57 | both halves | 8e-06 |  |
| [[IDH3A]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[WDR77]] | -0.63 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[FARSB]] | -0.63 | -0.45 / -0.70 | both halves | 3e-05 |  |
| [[CMSS1]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[DDX10]] | -0.62 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[SLC35B4]] | -0.62 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.61 | -0.41 / -0.68 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity raises KLC4's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without HOXA3 | 0.051 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[TPK1]] | C | TPK1 activity lowers KLC4's level | lines that do not express TPK1 (3) vs lines expressing it (47) | 1.66× higher at baseline in the lines without TPK1 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: NMRAL1, CYP2R1, PPP1R26; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.7, -38.8); signed map (-11.2, 3.7). **Vector** length 106, 24.6% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kinesin light chain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,040,777-43,075,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA387M24.3; previously KNSL8 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 17 pathways, smallest: RHO GTPases activate KTN1; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSK0](https://www.uniprot.org/uniprotkb/Q9NSK0) (Kinesin light chain 4):

> Kinesin is a microtubule-associated force-producing protein that may play a role in organelle transport. The light chain may function in coupling of cargo to the heavy chain or in the modulation of its ATPase activity (By similarity).

**Summary**, from NCBI Gene [89953](https://www.ncbi.nlm.nih.gov/gene/89953):

> Predicted to enable kinesin binding activity. Predicted to be involved in microtubule-based movement. Predicted to be located in microtubule. Predicted to be part of kinesin complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21624) · Entrez [89953](https://www.ncbi.nlm.nih.gov/gene/89953) · UniProt [Q9NSK0](https://www.uniprot.org/uniprotkb/Q9NSK0) · Ensembl [ENSG00000137171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137171)

## Data

Gene col 5979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5979); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5979]; `tensor/DDL_lfc|DDL_z.npy` [5979]; `embed/gene_vectors.npy` [5979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5979 or target_col == 5979). Every well: [[KLC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
