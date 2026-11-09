---
symbol: "NOPCHAP1"
type: "gene"
col: 7487
ensembl_id: "ENSG00000151131"
name: "NOP protein chaperone 1"
location: "12q23.3"
module: 62
arm: "+"
pooled_cpm: 22.04
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# NOPCHAP1

*NOP protein chaperone 1* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.53× (z +34.7, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.427×); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0985×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM68]] (+0.76, fdr 7e-06), [[DCP1B]] (+0.63, fdr 1e-05), [[FBXO22]] (+0.62, fdr 1e-05); moves opposite to [[H2AZ2]] (-0.57, fdr 4e-05), [[GDF11]] (-0.55, fdr 3e-04), [[UBE2S]] (-0.51, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[FBXO22]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.53×** | +34.7 | 0e+00 | 47/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.99×** | +18.8 | 0e+00 | 44/46 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.04×** | +16.3 | 0e+00 | 42/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.97×** | +12.7 | 1e-34 | 45/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.77×** | +12.3 | 6e-33 | 46/47 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.44×** | +10.8 | 3e-25 | 43/47 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +10.4 | 2e-23 | 38/48 (A-172, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.26×** | +9.9 | 4e-21 | 43/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +9.8 | 5e-21 | 42/46 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +8.8 | 5e-17 | 40/47 (LoVo, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +8.6 | 5e-16 | 42/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +7.5 | 3e-12 | 31/47 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.85×** | +7.2 | 3e-11 | 18/32 (SW480, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +7.0 | 1e-10 | 30/48 (A549, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +6.5 | 3e-09 | 30/47 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +6.0 | 8e-08 | 29/47 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 1e-06 | 26/47 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +4.9 | 3e-05 | 27/48 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.6 | 1e-04 | 22/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +4.1 | 1e-03 | 19/48 (A549, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.427×); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0985×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.762× | -3.1 | 0.96 | 5/48 (SW 1088, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.5 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +18.3) | — |
| [[SW480 (line)]] | alt | 25.3 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +16.1) | — |
| [[A549 (line)]] | wt | 32.2 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +18.2) | — |
| [[HT-29 (line)]] | alt | 15.3 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +17.7) | — |
| [[NCI-H460 (line)]] | wt | 31.8 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +27.2) | — |
| [[SNU-423 (line)]] | alt | 15.1 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.12× (z +16.9) | — |
| [[A-172 (line)]] | wt | 16.6 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +20.8) | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +23.5) | — |
| [[LoVo (line)]] | wt | 26.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +27.8) | — |
| [[LOX-IMVI (line)]] | wt | 50.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +27.2) | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +16.7) | — |
| [[A498 (line)]] | wt | 19.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +21.5) | — |
| [[KATO III (line)]] | alt | 13.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +15.6) | — |
| [[C32 (line)]] | wt | 15.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +19.2) | — |
| [[H4 (line)]] | wt | 12.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.5× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 14.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.85× (z +16.0) | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +20.3) | — |
| [[LS 180 (line)]] | wt | 18.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +18.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 37.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.2) |
| [[RKO (line)]] | wt | 30.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +21.1) | — |
| [[SNU-1 (line)]] | wt | 31.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.69× (z +15.5) | — |
| [[SW48 (line)]] | wt | 28.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +15.3) | — |
| [[A-427 (line)]] | wt | 40.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +17.5) | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0985× (z -8.8) |
| [[BT-474 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +14.9) | — |
| [[C-33 A (line)]] | alt | 37.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 8.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +22.5) | — |
| [[Hs 766T (line)]] | wt | 9.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +10.3) | — |
| [[J82 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +14.8) | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 9.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +17.4) | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM68]] | +0.76 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[DCP1B]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[FBXO22]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PAM16]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.56 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[ZC3H8]] | +0.56 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RNF135]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ZNF343]] | +0.54 | +0.53 / +0.31 | both halves | 2e-04 |  |
| [[MRPL32]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PANK1]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ACTA2]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[FAM185A]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H2AZ2]] | -0.57 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[GDF11]] | -0.55 | -0.37 / -0.26 | both halves | 3e-04 |  |
| [[UBE2S]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NRM]] | -0.50 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[ANLN]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[H2AX]] | -0.50 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[MAGT1]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[HMG20B]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TOP2A]] | -0.49 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[LMCD1-AS1]] | -0.49 | -0.14 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[CLTC]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CHP1]] | -0.48 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[RALY]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NOPCHAP1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises NOPCHAP1's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.27× lower at baseline in the lines without EDA2R | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[PINCR]] | B | PINCR activity raises NOPCHAP1's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.28× lower at baseline in the lines without PINCR | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PINCR]] | B | PINCR activity strengthens NOPCHAP1's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.91× as strongly (z diff +0.23); strongest at Doxorubicin (hydrochloride) 5 µM: 3.63x vs 8.20x (z diff +2.2) | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[TP53]] | C | TP53 activity strengthens NOPCHAP1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.93× as strongly (z diff +0.19); strongest at Epirubicin (hydrochloride) 5 µM: 3.18x vs 6.89x (z diff +2.7) | 0.127 over the table, 0.004 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO22]] | C | NOPCHAP1's natural level strengthens FBXO22's drug response | NOPCHAP1's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.13; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RACGAP1]] | C | NOPCHAP1's natural level strengthens RACGAP1's drug response | NOPCHAP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.06; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.4, 34.7); signed map (42.2, -26.2). **Vector** length 83.8, 21.5% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +18.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +16.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +34.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +10.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -3.5 | +7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.2 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | -3.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NOP protein chaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,986,316-105,074,197 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40397, DDSR1; previously C12orf45 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5I9](https://www.uniprot.org/uniprotkb/Q8N5I9) (NOP protein chaperone 1):

> Client-loading PAQosome/R2TP complex cofactor that selects NOP58 to promote box C/D small nucleolar ribonucleoprotein (snoRNP) assembly. Acts as a bridge between NOP58 and the R2TP complex via RUVBL1:RUVBL2.

**Summary**, from NCBI Gene [121053](https://www.ncbi.nlm.nih.gov/gene/121053):

> Enables box C/D methylation guide snoRNP complex binding activity. Involved in box C/D snoRNP assembly. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28628) · Entrez [121053](https://www.ncbi.nlm.nih.gov/gene/121053) · UniProt [Q8N5I9](https://www.uniprot.org/uniprotkb/Q8N5I9) · Ensembl [ENSG00000151131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151131)

## Data

Gene col 7487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7487); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7487]; `tensor/DDL_lfc|DDL_z.npy` [7487]; `embed/gene_vectors.npy` [7487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7487 or target_col == 7487). Every well: [[NOPCHAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOPCHAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
