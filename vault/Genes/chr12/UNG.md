---
symbol: "UNG"
type: "gene"
col: 1147
ensembl_id: "ENSG00000076248"
name: "uracil DNA glycosylase"
location: "12q24.11"
module: 6
arm: "+"
pooled_cpm: 11.86
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# UNG

*uracil DNA glycosylase* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.31× (z +15.4, q 0e+00, up in 14 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +6.2, q 5e-08, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 5.00×, A549 7.59×, MIA PaCa-2 4.80×, PANC-1 3.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 6.23×, SW480 4.74×, PANC-1 3.70×, HT-29 8.68×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 4.89×, SW480 4.04×; ⚠ toxic; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -11.9, q 4e-30, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3]] (+0.75, fdr 7e-06), [[CASP2]] (+0.71, fdr 7e-06), [[CDCA7]] (+0.71, fdr 7e-06); moves opposite to [[ACAP1]] (-0.55, fdr 2e-05), [[HMGCL]] (-0.54, fdr 1e-05), [[MAP1LC3B]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1147.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 5.00×, A549 7.59×, MIA PaCa-2 4.80×, PANC-1 3.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 6.23×, SW480 4.74×, PANC-1 3.70×, HT-29 8.68×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 4.89×, SW480 4.04×; ⚠ toxic; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +15.4 | 0e+00 | 14/16 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +15.2 | 0e+00 | 32/36 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +10.5 | 1e-23 | 23/26 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.79×** | +7.5 | 8e-12 | 23/41 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +6.2 | 5e-08 | 20/48 (SNU-423, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.4 | 0.001 | 15/47 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.35×** | +4.0 | 0.005 | 13/47 (PANC-1, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.36×** | +4.0 | 0.005 | 15/40 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.6 | 0.020 | 8/20 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.30×** | +3.5 | 0.027 | 10/47 (PANC-1, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -11.9 | 4e-30 | 35/45 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -7.6 | 7e-12 | 29/46 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -6.4 | 3e-08 | 23/45 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.664×** | -5.5 | 6e-06 | 20/46 (J82, HOP62, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.678×** | -5.2 | 2e-05 | 18/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.714×** | -4.4 | 0.001 | 20/47 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.9 | 0.007 | 14/48 (J82, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.751×** | -3.8 | 0.008 | 19/47 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.751×** | -3.8 | 0.008 | 16/47 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.822×** | -3.7 | 0.011 | 16/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.699×** | -3.4 | 0.029 | 8/48 (RPMI-7951, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.029 | 19/47 (A-427, SHP-77, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.777×** | -3.4 | 0.030 | 13/47 (H4, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.784×** | -3.3 | 0.044 | 17/45 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.786×** | -3.2 | 0.045 | 11/47 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.784×** | -3.1 | 0.059 | 18/45 (COLO 205, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -3.1 | 0.072 | 16/48 (RKO, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.2) |
| [[A-427 (line)]] | wt | 29.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 18.2 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.89× (z +10.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 26.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.5) |
| [[PANC-1 (line)]] | alt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.107× (z -8.5) |
| [[A498 (line)]] | wt | 13.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.9) |
| [[A549 (line)]] | wt | 9.58 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.59× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 6.88 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0969× (z -8.5) |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.9) |
| [[HT-29 (line)]] | alt | 7.05 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.68× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 5.15 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0534× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 7.58 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.31× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 6.91 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0844× (z -8.9) |
| [[A-172 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3]] | +0.75 | +0.78 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 490 |
| [[CASP2]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.71 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[MCM2]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 401 |
| [[MTHFD1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[NUP155]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MCM5]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM6]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 415 |
| [[DDX11]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[MSH2]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 701 |
| [[POLA1]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 | STRING 435 |
| [[TFDP1]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 | STRING 458 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[HMGCL]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | -0.54 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MAPK6]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[EIF1]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises UNG's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without E2F2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[NUP210]] | B | NUP210 activity raises UNG's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without NUP210 | 0.080 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.6, -42.5); signed map (-34.2, -44.3). **Vector** length 89.3, 18.1% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.52 to 28); *Activation of the pre-replicative complex* (reactome, mean cos +0.53 to 22); *Activation of ATR in response to replication stress* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +15.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +4.1 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +3.9 | +7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -0.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.8 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | uracil DNA glycosylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,097,597-109,126,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UDG, UNG1, UNG2, HIGM4; previously DGU |
| Gene groups (HGNC) | DNA glycosylases |
| Hallmark sets | MYC_TARGETS_V2, MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 15 pathways, smallest: Displacement of DNA glycosylase by APEX1; Somatic hypermutation of immunoglobulin genes by error-prone base excision repair (BER); Chromatin modifications during the maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [P13051](https://www.uniprot.org/uniprotkb/P13051) (Uracil-DNA glycosylase):

> Uracil-DNA glycosylase that hydrolyzes the N-glycosidic bond between uracil and deoxyribose in single- and double-stranded DNA (ssDNA and dsDNA) to release a free uracil residue and form an abasic (apurinic/apyrimidinic; AP) site. Excises uracil residues arising as a result of misincorporation of dUMP residues by DNA polymerase during replication or due to spontaneous or enzymatic deamination of cytosine. Mediates error-free base excision repair (BER) of uracil at replication forks. According …

**Summary**, from NCBI Gene [7374](https://www.ncbi.nlm.nih.gov/gene/7374):

> This gene encodes one of several uracil-DNA glycosylases. One important function of uracil-DNA glycosylases is to prevent mutagenesis by eliminating uracil from DNA molecules by cleaving the N-glycosylic bond and initiating the base-excision repair (BER) pathway. Uracil bases occur from cytosine deamination or misincorporation of dUMP residues. Alternative promoter usage and splicing of this gene leads to two different isoforms: the mitochondrial UNG1 and the nuclear UNG2. The UNG2 term was …

**Accessions** — [HGNC:12572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12572) · Entrez [7374](https://www.ncbi.nlm.nih.gov/gene/7374) · UniProt [P13051](https://www.uniprot.org/uniprotkb/P13051) · Ensembl [ENSG00000076248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076248)

## Data

Gene col 1147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1147); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1147]; `tensor/DDL_lfc|DDL_z.npy` [1147]; `embed/gene_vectors.npy` [1147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1147 or target_col == 1147). Every well: [[UNG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
