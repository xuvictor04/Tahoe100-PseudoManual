---
symbol: "BORCS7-ASMT"
type: "gene"
col: 15661
ensembl_id: "ENSG00000270316"
name: "BORCS7-ASMT readthrough (NMD candidate)"
location: "10q24.32"
module: 15
arm: "+"
pooled_cpm: 7.85
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# BORCS7-ASMT

*BORCS7-ASMT readthrough (NMD candidate)* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +15.1, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.427× (z -11.6, q 2e-28, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AS3MT]] (+0.77, fdr 7e-06, ⚠ same locus), [[ZNF460-AS1]] (+0.71, fdr 3e-05), [[CASS4]] (+0.69, fdr 3e-05), [[ADCY10]] (+0.69, fdr 1e-05); moves opposite to [[BCKDK]] (-0.63, fdr 4e-05), [[STUB1]] (-0.59, fdr 6e-04), [[TTLL12]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +15.1 | 0e+00 | 39/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +7.6 | 6e-12 | 25/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.4 | 3e-08 | 19/39 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.8 | 9e-07 | 14/47 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.32×** | +5.5 | 4e-06 | 14/48 (A549, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.4 | 7e-06 | 18/45 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +4.5 | 5e-04 | 14/47 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +4.5 | 5e-04 | 10/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 5e-04 | 12/46 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 7e-04 | 16/47 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.1 | 0.002 | 16/45 (C32, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.026 | 15/43 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.026 | 15/43 (LoVo, SK-MEL-2, …) | top dose only | composition shift; position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.045 | 5/45 (A498, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.076 | 8/48 (SW1417, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.427×** | -11.6 | 2e-28 | 36/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.469×** | -10.3 | 1e-22 | 30/43 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.550×** | -8.1 | 7e-14 | 27/47 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.606×** | -6.8 | 1e-09 | 22/47 (H4, PANC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -6.5 | 7e-09 | 23/47 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.618×** | -6.3 | 3e-08 | 21/45 (SNU-423, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.731×** | -4.3 | 0.002 | 17/33 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.731×** | -4.2 | 0.002 | 13/46 (RKO, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.718×** | -4.2 | 0.002 | 8/19 (NCI-H460, SNU-423, …) | inconsistent across doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.590×** | -3.8 | 0.010 | 9/48 (C32, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.598×** | -3.7 | 0.011 | 14/46 (NCI-H1573, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.599×** | -3.6 | 0.011 | 9/44 (NCI-H2030, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.764×** | -3.6 | 0.011 | 15/36 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.600×** | -3.6 | 0.011 | 8/38 (NCI-H1573, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.778×** | -3.4 | 0.026 | 10/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.028 | 13/47 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.786×** | -3.3 | 0.035 | 10/46 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.791×** | -3.2 | 0.046 | 7/47 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.05 µM |  | **0.780×** | -3.1 | 0.052 | 11/46 (AN3 CA, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.138× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.122× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 15.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.07 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0884× (z -9.5) |
| [[A-172 (line)]] | wt | 7.36 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -8.6) |
| [[A498 (line)]] | wt | 6.39 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.225× (z -8.8) |
| [[BT-474 (line)]] | alt | 4.65 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0651× (z -8.9) |
| [[C32 (line)]] | wt | 10.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.151× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 5.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.75 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0662× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 5.27 | 0 | 1 | — | [[palbociclib (drug)]] 0.05 µM 0.0850× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.222× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 6.48 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.122× (z -8.6) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.268× (z -8.8) |
| [[RKO (line)]] | wt | 8.66 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0518× (z -11.5) |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.105× (z -9.2) |
| [[A-427 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AS3MT]] | +0.77 | +0.75 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF460-AS1]] | +0.71 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[CASS4]] | +0.69 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ADCY10]] | +0.69 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[UPP2]] | +0.69 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.68 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[CCDC62]] | +0.67 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[KLRD1]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | +0.67 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[DARS1-AS1]] | +0.67 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[BORCS7]] | +0.66 | +0.62 / +0.45 | both halves | 3e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[USP34-DT]] | +0.66 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[DDX59-AS1]] | +0.66 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCKDK]] | -0.63 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[STUB1]] | -0.59 | -0.37 / -0.22 | both halves | 6e-04 |  |
| [[TTLL12]] | -0.58 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PDHA1]] | -0.58 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BORCS7-ASMT's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DDX3Y]] | B | DDX3Y activity raises BORCS7-ASMT's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without DDX3Y | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (0.4, 22.1); signed map (10.9, 3.7). **Vector** length 82.9, 14.9% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +15.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.1 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.8 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -6.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | BORCS7-ASMT readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 10q24.32 — chr10:102,854,272-102,901,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C10orf32-ASMT |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100528007](https://www.ncbi.nlm.nih.gov/gene/100528007):

> This locus represents naturally occurring read-through transcription between the neighboring C10orf32 (chromosome 10 open reading frame 32) and AS3MT (arsenic, +3 oxidation state, methyltransferase) genes. The read-through transcript is a candidate for nonsense-mediated mRNA decay (NMD), and is therefore unlikely to produce a protein product. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:49183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49183) · Entrez [100528007](https://www.ncbi.nlm.nih.gov/gene/100528007) · Ensembl [ENSG00000270316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270316)

## Data

Gene col 15661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15661); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15661]; `tensor/DDL_lfc|DDL_z.npy` [15661]; `embed/gene_vectors.npy` [15661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15661 or target_col == 15661). Every well: [[BORCS7-ASMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BORCS7-ASMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
