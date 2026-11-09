---
symbol: "WDR82"
type: "gene"
col: 8864
ensembl_id: "ENSG00000164091"
name: "WD repeat domain 82"
location: "3p21.2"
module: 16
arm: "+"
pooled_cpm: 51.34
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# WDR82

*WD repeat domain 82* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.66× (z +11.3, q 6e-27, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.638× (z -9.6, q 3e-19, down in 30 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.713× (z -7.5, q 1e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP62]] (+0.73, fdr 7e-06), [[SRCAP]] (+0.68, fdr 7e-06), [[FEM1A]] (+0.67, fdr 7e-06); moves opposite to [[RAB8B]] (-0.59, fdr 1e-05), [[SRP54-AS1]] (-0.58, fdr 1e-05), [[MINDY3]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +11.3 | 6e-27 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +9.4 | 1e-18 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +9.2 | 9e-18 | 38/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +9.0 | 2e-17 | 35/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.3 | 1e-14 | 34/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.3 | 2e-08 | 29/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +6.3 | 3e-08 | 27/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.2 | 3e-08 | 0/49 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 4e-07 | 27/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 2e-06 | 25/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 15/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.061 | 15/48 (NCI-H2347, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -9.6 | 3e-19 | 30/42 (C32, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.713×** | -7.5 | 1e-11 | 35/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -6.8 | 2e-09 | 30/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -6.5 | 8e-09 | 28/48 (AN3 CA, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.828×** | -5.9 | 3e-07 | 21/48 (A498, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.776×** | -5.7 | 2e-06 | 26/48 (HEC-1-A, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -4.6 | 4e-04 | 14/48 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.826×** | -4.2 | 0.002 | 20/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.875× | -4.2 | 0.002 | 16/48 (SW480, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.829×** | -4.2 | 0.002 | 20/47 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.786×** | -3.8 | 0.009 | 21/45 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.851× | -3.4 | 0.027 | 18/48 (SW 1088, AN3 CA, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.765×** | -3.1 | 0.074 | 13/35 (HS-578T, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.865× | -3.1 | 0.074 | 20/48 (SNU-423, A-427, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.874× | -3.0 | 0.098 | 10/48 (AN3 CA, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.493× (z -8.7) |
| [[SW480 (line)]] | alt | 76.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.24× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 33.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -13.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 60.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 52.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0681× (z -24.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 71.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.2) |
| [[PANC-1 (line)]] | alt | 50.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -15.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 76.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.7) |
| [[COLO 205 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 69.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.1) ⚠ cell-cycle shift, explains ~2% of this change |
| [[HS-578T (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0674× (z -13.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 68.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 51.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.0) ⚠ cell-cycle shift, explains ~2% of this change |
| [[NCI-H460 (line)]] | wt | 41.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.3) ⚠ cell-cycle shift, explains ~2% of this change |
| [[SNU-423 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.4) ⚠ cell-cycle shift, explains ~2% of this change |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 66.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP62]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[FEM1A]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MED1]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[REXO1]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 | same gene group |
| [[ZBTB40]] | +0.65 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[INO80]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NIP7]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[COA7]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[EXOSC6]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | pathway: Nuclear RNA decay |
| [[OPA3]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[UBQLN2]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB8B]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.58 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[LINC00674]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[FIG4]] | -0.56 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[DPM1]] | -0.55 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[C20orf96]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SNX1]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NPTN]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[FHIP1A]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[APAF1]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises WDR82's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.8, -1.3); signed map (2.3, -33.0). **Vector** length 96.5, 22.3% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.4 | +9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +1.7 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +2.3 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.5 | -0.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 82 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:52,254,434-52,288,020 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2730, MST107, MSTP107, PRO34047, WDR82A, SWD2; previously TMEM113 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Nuclear RNA decay; Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXN9](https://www.uniprot.org/uniprotkb/Q6UXN9) (WD repeat-containing protein 82):

> Regulatory component of the SET1/COMPASS complex implicated in the tethering of this complex to transcriptional start sites of active genes. Facilitates histone H3 'Lys-4' methylation (H3K4me) via recruitment of the SETD1A or SETD1B to the 'Ser-5' phosphorylated C-terminal domain (CTD) of RNA polymerase II large subunit (POLR2A). Component of the PNUTS-PP1 protein phosphatase complex, a protein phosphatase 1 (PP1) complex that promotes RNA polymerase II transcription pause-release, allowing …

**Summary**, from NCBI Gene [80335](https://www.ncbi.nlm.nih.gov/gene/80335):

> TMEM113 (WDR82) is a component of the mammalian SET1A (MIM 611052)/SET1B (MIM 611055) histone H3-Lys4 methyltransferase complexes (Lee and Skalnik, 2005 [PubMed 16253997]; Lee et al., 2007 [PubMed 17355966]).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:28826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28826) · Entrez [80335](https://www.ncbi.nlm.nih.gov/gene/80335) · UniProt [Q6UXN9](https://www.uniprot.org/uniprotkb/Q6UXN9) · Ensembl [ENSG00000164091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164091)

## Data

Gene col 8864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8864); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8864]; `tensor/DDL_lfc|DDL_z.npy` [8864]; `embed/gene_vectors.npy` [8864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8864 or target_col == 8864). Every well: [[WDR82 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR82.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
