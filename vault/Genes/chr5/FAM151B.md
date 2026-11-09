---
symbol: "FAM151B"
type: "gene"
col: 7619
ensembl_id: "ENSG00000152380"
name: "family with sequence similarity 151 member B"
location: "5q14.1"
module: 39
arm: "+"
pooled_cpm: 11.73
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 11
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# FAM151B

*family with sequence similarity 151 member B* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.22× (z +26.0, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.669× (z -5.1, q 2e-04, down in 22 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.473× (z -5.0, q 2e-04, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.85, fdr 7e-06), [[MYOCOS]] (+0.82, fdr 7e-06), [[SLC6A13]] (+0.81, fdr 7e-06); moves opposite to [[SDHAF3]] (-0.67, fdr 7e-05), [[ACTR5]] (-0.66, fdr 1e-04), [[BRAT1]] (-0.66, fdr 2e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.22×** | +26.0 | 0e+00 | 43/46 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +17.9 | 0e+00 | 40/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +11.8 | 9e-30 | 34/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +9.9 | 5e-21 | 29/45 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +8.8 | 2e-16 | 30/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.9 | 3e-13 | 28/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +6.4 | 2e-08 | 23/48 (PANC-1, SW1417, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.1 | 6e-08 | 24/40 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.5 | 2e-06 | 22/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +5.4 | 3e-06 | 19/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.4 | 4e-06 | 17/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +5.3 | 4e-06 | 21/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 2e-05 | 20/47 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +4.8 | 5e-05 | 15/48 (LoVo, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 9e-04 | 19/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.2 | 9e-04 | 20/47 (HT-29, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.001 | 17/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.669×** | -5.1 | 2e-04 | 22/46 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -5.0 | 2e-04 | 16/48 (HepG2/C3A, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.706×** | -4.3 | 0.003 | 19/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.794×** | -4.2 | 0.004 | 15/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.708×** | -4.1 | 0.005 | 14/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.566×** | -3.8 | 0.012 | 16/42 (AN3 CA, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.012 | 13/46 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.755×** | -3.4 | 0.047 | 10/48 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.769×** | -3.4 | 0.047 | 12/47 (AsPC-1, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.770×** | -3.3 | 0.064 | 16/47 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.628×** | -3.1 | 0.095 | 10/42 (NCI-H1573, RKO, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.636× | -3.0 | 0.11 | 11/45 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.783× | -3.0 | 0.11 | 15/43 (A549, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.02 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +19.5) | — |
| [[A-172 (line)]] | wt | 8.08 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +10.4) | [[Ivabradine (hydrochloride) (drug)]] 5 µM 0.0397× (z -12.5) ⚠ unreliable plate only · without an alert: [[Rutin (trihydrate) (drug)]] 5 µM 0.0602× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 13.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +12.9) | — |
| [[SW480 (line)]] | alt | 8.73 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.0573× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.80 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +15.0) | [[Harringtonine (drug)]] 0.05 µM 0.0700× (z -9.1) |
| [[SNU-423 (line)]] | alt | 12.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 7.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 8.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +12.6) | — |
| [[LoVo (line)]] | wt | 16.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 11.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 26.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.0) |
| [[A498 (line)]] | wt | 8.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 4.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 7.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +8.8) | — |
| [[J82 (line)]] | alt | 8.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 8.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 8.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +11.3) | — |
| [[RKO (line)]] | wt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 8.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.1) | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.85 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.82 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.81 | +0.83 / +0.64 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.80 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.80 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.79 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[C21orf91-OT1]] | +0.78 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.78 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.78 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[DPYS]] | +0.77 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[TTC33]] | +0.77 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[LINC02955]] | +0.77 | +0.79 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.67 | -0.65 / -0.37 | both halves | 7e-05 |  |
| [[ACTR5]] | -0.66 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[BRAT1]] | -0.66 | -0.63 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM151B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IMPA1P1]] | B | IMPA1P1 activity raises FAM151B's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without IMPA1P1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, -13.5); signed map (17.9, 8.0). **Vector** length 85.9, 17.6% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +26.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +8.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | +5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 151 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:80,487,969-80,542,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ9217 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXP7](https://www.uniprot.org/uniprotkb/Q6UXP7) (Protein FAM151B):

> Essential for survival of retinal photoreceptor cells.

**Summary**, from NCBI Gene [167555](https://www.ncbi.nlm.nih.gov/gene/167555):

> Predicted to be involved in photoreceptor cell development. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33716) · Entrez [167555](https://www.ncbi.nlm.nih.gov/gene/167555) · UniProt [Q6UXP7](https://www.uniprot.org/uniprotkb/Q6UXP7) · Ensembl [ENSG00000152380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152380)

## Data

Gene col 7619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7619); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7619]; `tensor/DDL_lfc|DDL_z.npy` [7619]; `embed/gene_vectors.npy` [7619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7619 or target_col == 7619). Every well: [[FAM151B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM151B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
