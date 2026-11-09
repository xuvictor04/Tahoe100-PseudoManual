---
symbol: "RRAD"
type: "gene"
col: 9336
ensembl_id: "ENSG00000166592"
name: "RRAD, Ras related glycolysis inhibitor and calcium channel regulator"
location: "16q22.1"
module: 14
arm: "+"
pooled_cpm: 10.98
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 42
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RRAD

*RRAD, Ras related glycolysis inhibitor and calcium channel regulator* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.64× (z +22.7, q 0e+00, up in 17 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.831× (z -5.0, q 4e-04, down in 13 of 17 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SNU-423 0.202×, SW 900 0.182×, NCI-H1792 0.174×, Hs 766T 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (NCI-H1792 0.113×, SNU-423 0.213×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.114×; ⚠ cell-cycle shift, would explain all of this change); [[Budesonide (drug)]] 5 µM in 1 line (NCI-H1792 0.125×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1792 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF9]] (+0.72, fdr 7e-06), [[CADM1]] (+0.70, fdr 7e-06), [[CGNL1]] (+0.67, fdr 7e-06); moves opposite to [[DPY19L3]] (-0.51, fdr 3e-05), [[HMGA2]] (-0.50, fdr 3e-05), [[TOP1]] (-0.50, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[BDKRB2]] → it (grade B ⚠); 42 go from it, the strongest it → [[RASSF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.64×** | +22.7 | 0e+00 | 17/17 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.00×** | +12.0 | 1e-30 | 7/15 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.27×** | +11.9 | 2e-30 | 5/12 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.41×** | +11.0 | 3e-26 | 8/17 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.23×** | +10.3 | 7e-23 | 15/17 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.40×** | +9.1 | 8e-18 | 14/17 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +6.9 | 4e-10 | 12/17 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +6.5 | 5e-09 | 5/13 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +5.7 | 9e-07 | 13/17 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +5.4 | 3e-06 | 7/16 (SNU-423, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.4 | 7e-04 | 4/15 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.005 | 10/17 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.63×** | +3.8 | 0.007 | 1/10 (NCI-H2030) | top dose only | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **2.35×** | +3.3 | 0.035 | 7/15 (NCI-H1792, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.051 | 10/17 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.059 | 10/17 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.065 | 11/17 (HOP62, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.067 | 11/17 (NCI-H2347, HOP62, …) | two highest doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9336.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SNU-423 0.202×, SW 900 0.182×, NCI-H1792 0.174×, Hs 766T 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (NCI-H1792 0.113×, SNU-423 0.213×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.114×; ⚠ cell-cycle shift, would explain all of this change); [[Budesonide (drug)]] 5 µM in 1 line (NCI-H1792 0.125×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1792 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.831×** | -5.0 | 4e-04 | 13/17 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.657× | -3.1 | 0.41 | 9/17 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.664× | -3.1 | 0.41 | 9/16 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 43.5 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.113× (z -10.2) |
| [[SNU-423 (line)]] | alt | 51.5 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.213× (z -8.9) |
| [[HS-578T (line)]] | alt | 4.47 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.69 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 99.0× (z +23.6) | — |
| [[SW 900 (line)]] | alt | 51.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +14.1) | — |
| [[NCI-H2347 (line)]] | alt | 9.92 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +19.8) | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +18.7) | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 9.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.8× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.2× (z +14.9) | — |
| [[J82 (line)]] | alt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 3.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 9.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +11.0) | — |
| [[A-172 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF9]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CADM1]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[CGNL1]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GATA6]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MARCKS]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SLC2A6]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[SHISAL1]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L3]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[HMGA2]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TOP1]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ANPEP]] | -0.49 | -0.51 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 5, C 14. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BDKRB2]] | B | BDKRB2 activity raises RRAD's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without BDKRB2 | 0.028 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[CADM1]] | B | CADM1 activity raises RRAD's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.32× lower at baseline in the lines without CADM1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[C12orf50]] | B | C12orf50 activity raises RRAD's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without C12orf50 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[CXCL3]] | B | CXCL3 activity raises RRAD's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without CXCL3 | 0.074 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[NEURL3]] | B | NEURL3 activity raises RRAD's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without NEURL3 | 0.088 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[TNFAIP6]] | C | TNFAIP6 activity raises RRAD's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without TNFAIP6 | 0.009 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises RRAD's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without ROR1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |
| [[CSF2]] | C | CSF2 activity raises RRAD's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without CSF2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2; co-absent with the target |
| [[MAF]] | C | MAF activity raises RRAD's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without MAF | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; co-absent with the target |
| [[IRAG2]] | C | IRAG2 activity raises RRAD's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.26× lower at baseline in the lines without IRAG2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[ENTHD1]] | C | ENTHD1 activity raises RRAD's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without ENTHD1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |
| [[GBP5]] | C | GBP5 activity raises RRAD's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.81× lower at baseline in the lines without GBP5 | 0.027 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 28, C 14. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF5]] | B | RRAD activity raises RASSF5's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without RRAD | 0.008 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[RIPK2]] | B | RRAD activity raises RIPK2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without RRAD | 0.008 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[DUSP10]] | B | RRAD activity raises DUSP10's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.83× lower at baseline in the lines without RRAD | 0.009 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[BHLHE40]] | B | RRAD activity raises BHLHE40's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without RRAD | 0.012 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[CXCL3]] | B | RRAD activity raises CXCL3's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.50× lower at baseline in the lines without RRAD | 0.016 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[KIAA1217]] | B | RRAD activity raises KIAA1217's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.22× lower at baseline in the lines without RRAD | 0.018 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[GATA6]] | B | RRAD activity raises GATA6's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without RRAD | 0.020 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[GBP2]] | B | RRAD activity raises GBP2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without RRAD | 0.024 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[LINC02605]] | B | RRAD activity raises LINC02605's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without RRAD | 0.026 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[NINJ1]] | B | RRAD activity raises NINJ1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without RRAD | 0.028 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[LMNA]] | B | RRAD activity raises LMNA's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.38× lower at baseline in the lines without RRAD | 0.030 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[SLC41A2]] | B | RRAD activity raises SLC41A2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without RRAD | 0.037 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 1.9); signed map (45.3, 10.8). **Vector** length 64.3, 20.3% of its response variance represented; |z| ≥ 3 in 524 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +22.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +9.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.9 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RRAD, Ras related glycolysis inhibitor and calcium channel regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,921,685-66,925,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REM3, RAD |
| Gene groups (HGNC) | RGK type GTPase family |
| Hallmark sets | UV_RESPONSE_UP, P53_PATHWAY |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [P55042](https://www.uniprot.org/uniprotkb/P55042) (GTP-binding protein RAD):

> May regulate basal voltage-dependent L-type Ca(2+) currents and be required for beta-adrenergic augmentation of Ca(2+) influx in cardiomyocytes, thereby regulating increases in heart rate and contractile force (By similarity). May play an important role in cardiac antiarrhythmia via the strong suppression of voltage-gated L-type Ca(2+) currents (By similarity). Regulates voltage-dependent L-type calcium channel subunit alpha-1C trafficking to the cell membrane (By similarity). Inhibits cardiac …

**Summary**, from NCBI Gene [6236](https://www.ncbi.nlm.nih.gov/gene/6236):

> Predicted to enable GTP binding activity and calcium channel regulator activity. Predicted to be involved in small GTPase-mediated signal transduction. Predicted to be located in T-tubule. Predicted to be active in plasma membrane. Implicated in type 2 diabetes mellitus. Biomarker of congestive heart failure. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10446) · Entrez [6236](https://www.ncbi.nlm.nih.gov/gene/6236) · UniProt [P55042](https://www.uniprot.org/uniprotkb/P55042) · Ensembl [ENSG00000166592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166592)

## Data

Gene col 9336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9336); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9336]; `tensor/DDL_lfc|DDL_z.npy` [9336]; `embed/gene_vectors.npy` [9336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9336 or target_col == 9336). Every well: [[RRAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
