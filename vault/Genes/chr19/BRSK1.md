---
symbol: "BRSK1"
type: "gene"
col: 8354
ensembl_id: "ENSG00000160469"
name: "BR serine/threonine kinase 1"
location: "19q13.42"
module: 103
arm: "+"
pooled_cpm: 8.48
n_lines_expressing: 37
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 28
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# BRSK1

*BR serine/threonine kinase 1* — 19q13.42

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.03×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.335× (z -19.1, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICU3]] (+0.57, fdr 3e-05), [[PAOX]] (+0.55, fdr 3e-05), [[PPFIA3]] (+0.53, fdr 6e-05); moves opposite to [[TJP2]] (-0.54, fdr 4e-05), [[ITFG1]] (-0.49, fdr 4e-05), [[USP6NL]] (-0.47, fdr 5e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ANXA3]] → it (grade B ⚠); 28 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8354.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.03×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.34× | +3.6 | 0.13 | 4/34 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.32× | +3.4 | 0.13 | 11/32 (MIA PaCa-2, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.33× | +3.4 | 0.13 | 11/32 (NCI-H2030, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.31× | +3.3 | 0.13 | 11/33 (SW480, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.335×** | -19.1 | 0e+00 | 27/30 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.353×** | -12.9 | 2e-35 | 28/35 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.359×** | -12.7 | 2e-34 | 27/35 (HS-578T, SW 900, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.388×** | -11.2 | 3e-27 | 26/32 (SW 900, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.404×** | -10.8 | 5e-25 | 24/31 (SW 900, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.418×** | -10.8 | 5e-25 | 27/35 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.504×** | -8.4 | 2e-15 | 22/31 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.649×** | -7.6 | 3e-12 | 26/34 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.543×** | -7.5 | 3e-12 | 24/35 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.536×** | -7.4 | 8e-12 | 19/27 (HS-578T, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.542×** | -7.0 | 1e-10 | 12/18 (NCI-H460, SW 900, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.598×** | -6.3 | 1e-08 | 16/23 (NCI-H1792, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.599×** | -6.3 | 1e-08 | 18/30 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.660×** | -5.1 | 1e-05 | 15/35 (HCT15, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.678×** | -4.8 | 6e-05 | 15/34 (C-33 A, NCI-H1792, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -4.0 | 0.002 | 10/33 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.587×** | -3.4 | 0.018 | 12/34 (HS-578T, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.019 | 8/35 (RPMI-7951, A-172, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.029 | 8/35 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.768×** | -3.3 | 0.029 | 11/32 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.772×** | -3.1 | 0.051 | 13/33 (AN3 CA, NCI-H1573, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.775×** | -3.0 | 0.058 | 10/34 (SK-MEL-2, C-33 A, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.789×** | -2.9 | 0.079 | 6/35 (C-33 A, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 21.1 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0965× (z -21.1) |
| [[SW 900 (line)]] | alt | 29.8 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -20.6) |
| [[A-172 (line)]] | wt | 34.3 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -18.4) |
| [[H4 (line)]] | wt | 35.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 7.52 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0405× (z -15.4) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0540× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -11.5) |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -9.8) |
| [[RKO (line)]] | wt | 19.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -15.2) |
| [[A-427 (line)]] | wt | 11.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.9) |
| [[C32 (line)]] | wt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.104× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 5.47 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -8.5) ⚠ cell-cycle shift, explains ~2% of this change |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -10.7) |
| [[PANC-1 (line)]] | alt | 8.04 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0654× (z -8.5) |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICU3]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PAOX]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PPFIA3]] | +0.53 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[EVC2]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[UPK1A-AS1]] | +0.51 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TMEM132D]] | +0.50 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[ODAD4]] | +0.50 | +0.41 / +0.33 | both halves | 1e-04 |  |
| [[APBB3]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[MIER2]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SULT4A1]] | +0.49 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[RASSF8]] | +0.48 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ZNF555]] | +0.48 | +0.40 / +0.42 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP2]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ITFG1]] | -0.49 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[USP6NL]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[MTUS1]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ANXA11]] | -0.47 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[TMEM123]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[STK24]] | -0.46 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[PPM1B]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SNTB2]] | -0.45 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[GAREM1]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[RAPGEF5]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[HNF4G]] | -0.44 | -0.55 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA3]] | B | ANXA3 activity lowers BRSK1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.29× higher at baseline in the lines without ANXA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[INAVA]] | B | INAVA activity lowers BRSK1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.76× higher at baseline in the lines without INAVA | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[C6orf132]] | B | C6orf132 activity lowers BRSK1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.51× higher at baseline in the lines without C6orf132 | 0.008 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[B3GNT3]] | B | B3GNT3 activity lowers BRSK1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.58× higher at baseline in the lines without B3GNT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TOP2A]] | B | TOP2A activity raises BRSK1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYK]] | B | SYK activity lowers BRSK1's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.70× higher at baseline in the lines without SYK | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[TJP2]] | B | TJP2 activity lowers BRSK1's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.07× higher at baseline in the lines without TJP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[GAREM1]] | B | GAREM1 activity lowers BRSK1's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 1.88× higher at baseline in the lines without GAREM1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | BRSK1 activity lowers ANXA11's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 3.19× higher at baseline in the lines without BRSK1 | 0.003 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[FOXO3B]] | B | BRSK1 activity raises FOXO3B's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without BRSK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[SMG9]] | B | BRSK1 activity raises SMG9's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without BRSK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[RASSF8]] | B | BRSK1 activity raises RASSF8's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 4.16× lower at baseline in the lines without BRSK1 | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[POLI]] | B | BRSK1 activity raises POLI's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BRSK1 | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[CHD1L]] | B | BRSK1 activity raises CHD1L's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without BRSK1 | 0.017 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[TJP2]] | B | BRSK1 activity lowers TJP2's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 3.48× higher at baseline in the lines without BRSK1 | 0.020 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[PGBD1]] | B | BRSK1 activity raises PGBD1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without BRSK1 | 0.025 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[ZNF286A]] | B | BRSK1 activity raises ZNF286A's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without BRSK1 | 0.026 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[C6orf132]] | B | BRSK1 activity lowers C6orf132's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 8.85× higher at baseline in the lines without BRSK1 | 0.027 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[ANXA3]] | B | BRSK1 activity lowers ANXA3's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 6.29× higher at baseline in the lines without BRSK1 | 0.033 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[SYNGAP1]] | B | BRSK1 activity raises SYNGAP1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without BRSK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.405). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-40.9, 27.4); signed map (0.0, 10.3). **Vector** length 68.2, 13.8% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +3.3 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.1 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.0 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BR serine/threonine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,282,072-55,312,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1811, SAD-B |
| Gene groups (HGNC) | BR serine/threonine kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDC3](https://www.uniprot.org/uniprotkb/Q8TDC3) (Serine/threonine-protein kinase BRSK1):

> Serine/threonine-protein kinase that plays a key role in polarization of neurons and centrosome duplication. Phosphorylates CDC25B, CDC25C, MAPT/TAU, RIMS1, TUBG1, TUBG2 and WEE1. Following phosphorylation and activation by STK11/LKB1, acts as a key regulator of polarization of cortical neurons, probably by mediating phosphorylation of microtubule-associated proteins such as MAPT/TAU at 'Thr-529' and 'Ser-579'. Also regulates neuron polarization by mediating phosphorylation of WEE1 at 'Ser-642' …

**Summary**, from NCBI Gene [84446](https://www.ncbi.nlm.nih.gov/gene/84446):

> Enables magnesium ion binding activity and tau-protein kinase activity. Involved in mitotic G2 DNA damage checkpoint signaling and protein phosphorylation. Acts upstream of or within G2/M transition of mitotic cell cycle; peptidyl-serine phosphorylation; and response to UV. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18994) · Entrez [84446](https://www.ncbi.nlm.nih.gov/gene/84446) · UniProt [Q8TDC3](https://www.uniprot.org/uniprotkb/Q8TDC3) · Ensembl [ENSG00000160469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160469)

## Data

Gene col 8354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8354); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8354]; `tensor/DDL_lfc|DDL_z.npy` [8354]; `embed/gene_vectors.npy` [8354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8354 or target_col == 8354). Every well: [[BRSK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRSK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
