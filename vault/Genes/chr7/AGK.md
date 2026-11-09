---
symbol: "AGK"
type: "gene"
col: 114
ensembl_id: "ENSG00000006530"
name: "acylglycerol kinase"
location: "7q34"
module: 1
arm: "+"
pooled_cpm: 48.54
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# AGK

*acylglycerol kinase* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.54× (z +7.6, q 1e-11, up in 37 of 45 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.45×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 1.78×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.341× (z -27.0, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2B3]] (+0.78, fdr 7e-06), [[FARSB]] (+0.78, fdr 7e-06), [[FKTN]] (+0.77, fdr 7e-06); moves opposite to [[YPEL5]] (-0.69, fdr 7e-06), [[KLHL24]] (-0.67, fdr 7e-06), [[CDK19]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MICB]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MIPOL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 114.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.45×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 1.78×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.6 | 1e-11 | 37/45 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.22× | +3.3 | 0.21 | 14/45 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.20× | +3.3 | 0.21 | 8/45 (A549, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.40× | +3.1 | 0.27 | 10/45 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.341×** | -27.0 | 0e+00 | 43/45 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -10.6 | 1e-23 | 39/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.577×** | -9.8 | 3e-20 | 36/45 (A-427, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -9.7 | 3e-20 | 35/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -8.3 | 1e-14 | 32/45 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -7.0 | 2e-10 | 36/45 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -5.2 | 2e-05 | 28/44 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.768×** | -4.7 | 2e-04 | 23/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -4.4 | 8e-04 | 19/45 (SNU-1, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.798×** | -4.0 | 0.004 | 22/44 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.808×** | -3.8 | 0.008 | 22/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.842× | -3.0 | 0.11 | 15/45 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.886× | -3.0 | 0.11 | 15/45 (NCI-H460, SW1417, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.8 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -21.7) |
| [[SW480 (line)]] | alt | 74.4 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -17.2) |
| [[LoVo (line)]] | wt | 48.2 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -21.6) |
| [[MIA PaCa-2 (line)]] | alt | 62.3 | 2 (2 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.45× (z +9.3) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -19.2) |
| [[C32 (line)]] | wt | 80.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -20.5) |
| [[HOP62 (line)]] | alt | 37.4 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -20.9) |
| [[PANC-1 (line)]] | alt | 50.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -21.5) |
| [[SW1417 (line)]] | alt | 67.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -21.0) |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 47.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -19.6) |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -14.4) |
| [[RKO (line)]] | wt | 75.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -19.6) |
| [[SNU-423 (line)]] | alt | 40.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -13.9) |
| [[A498 (line)]] | wt | 58.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.4) |
| [[C-33 A (line)]] | alt | 50.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 53.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 74.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0308× (z -34.8) |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.8) |
| [[SHP-77 (line)]] | alt | 61.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 66.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -22.7) |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -11.8) |
| [[A-427 (line)]] | wt | 39.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.274× (z -11.5) |
| [[A549 (line)]] | wt | 49.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 38.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.4) |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0906× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -16.6) |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -18.0) |
| [[HS-578T (line)]] | alt | 41.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.4) |
| [[HT-29 (line)]] | alt | 34.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -14.9) |
| [[J82 (line)]] | alt | 47.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 50.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 56.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 82.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -14.8) |
| [[SNU-1 (line)]] | wt | 56.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.348× (z -10.7) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.25 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | +0.78 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[FARSB]] | +0.78 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[FKTN]] | +0.77 | +0.63 / +0.83 | both halves | 7e-06 | STRING 436 |
| [[MRPL3]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[COA1]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[RBM28]] | +0.74 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[COG2]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ZNHIT6]] | +0.72 | +0.58 / +0.75 | both halves | 8e-06 |  |
| [[MTG1]] | +0.71 | +0.43 / +0.80 | both halves | 3e-05 |  |
| [[SAAL1]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[DLAT]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[MPHOSPH6]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.69 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[KLHL24]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[CDK19]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.65 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ERO1B]] | -0.65 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[TESK2]] | -0.64 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[GNAS]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.64 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[C2]] | -0.63 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[PIK3CA]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 | pathway: Phospholipid metabolism |
| [[ATOSA]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICB]] | B | MICB activity raises AGK's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without MICB | 0.022 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[SIM2]] | B | SIM2 activity raises AGK's level | lines that do not express SIM2 (9) vs lines expressing it (41) | 1.06× lower at baseline in the lines without SIM2 | 0.057 | ⚠ within organs, on part of the lines; also absent: SMC1B |
| [[TOP2A]] | B | TOP2A activity raises AGK's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WDR35]] | C | WDR35 activity raises AGK's level | lines that do not express WDR35 (5) vs lines expressing it (45) | 3.40× lower at baseline in the lines without WDR35 | 0.040 | ⚠ within organs, on part of the lines; also absent: AGK, DUSP19, ENTPD1-AS1; maybe low, not absent; co-absent with the target |
| [[TBC1D19]] | C | TBC1D19 activity raises AGK's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIPOL1]] | C | AGK activity raises MIPOL1's level | lines that do not express AGK (3) vs lines expressing it (47) | 4.18× lower at baseline in the lines without AGK | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.3, -39.7); signed map (-8.8, -47.4). **Vector** length 99.8, 23.9% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -27.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | acylglycerol kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,551,278-141,655,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10842; previously MULK |
| Gene groups (HGNC) | SPHK, AGK, CERK lipid kinase family |
| Reactome | 6 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53H12](https://www.uniprot.org/uniprotkb/Q53H12) (Acylglycerol kinase, mitochondrial):

> Lipid kinase that can phosphorylate both monoacylglycerol and diacylglycerol to form lysophosphatidic acid (LPA) and phosphatidic acid (PA), respectively. Does not phosphorylate sphingosine. Phosphorylates ceramide (By similarity). Phosphorylates 1,2-dioleoylglycerol more rapidly than 2,3-dioleoylglycerol (By similarity). Independently of its lipid kinase activity, acts as a component of the TIM22 complex. The TIM22 complex mediates the import and insertion of multi-pass transmembrane proteins …

**Summary**, from NCBI Gene [55750](https://www.ncbi.nlm.nih.gov/gene/55750):

> The protein encoded by this gene is a mitochondrial membrane protein involved in lipid and glycerolipid metabolism. The encoded protein is a lipid kinase that catalyzes the formation of phosphatidic and lysophosphatidic acids. Defects in this gene have been associated with mitochondrial DNA depletion syndrome 10. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:21869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21869) · Entrez [55750](https://www.ncbi.nlm.nih.gov/gene/55750) · UniProt [Q53H12](https://www.uniprot.org/uniprotkb/Q53H12) · Ensembl [ENSG00000006530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006530)

## Data

Gene col 114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 114); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 114]; `tensor/DDL_lfc|DDL_z.npy` [114]; `embed/gene_vectors.npy` [114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 114 or target_col == 114). Every well: [[AGK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
