---
symbol: "GPAA1"
type: "gene"
col: 12477
ensembl_id: "ENSG00000197858"
name: "glycosylphosphatidylinositol anchor attachment 1"
location: "8q24.3"
module: 20
arm: "+"
pooled_cpm: 10.73
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# GPAA1

*glycosylphosphatidylinositol anchor attachment 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.46× (z +20.3, q 0e+00, up in 32 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +17.0, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.727× (z -4.3, q 0.005, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGA]] (+0.69, fdr 1e-05), [[PPP1CA]] (+0.69, fdr 7e-06), [[DR1]] (+0.66, fdr 9e-06); moves opposite to [[EPB41L4A-AS1]] (-0.71, fdr 7e-06), [[NOL7]] (-0.69, fdr 1e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[SNHG6]] (-0.69, fdr 7e-06), [[SNHG7]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 21 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.46×** | +20.3 | 0e+00 | 32/32 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.44×** | +19.5 | 0e+00 | 20/20 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +17.0 | 0e+00 | 43/45 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.18×** | +14.5 | 1e-45 | 26/28 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.23×** | +10.9 | 1e-25 | 42/47 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.17×** | +10.6 | 4e-24 | 40/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **2.01×** | +9.5 | 2e-19 | 42/47 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.00×** | +9.1 | 9e-18 | 30/38 (SW480, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.91×** | +8.4 | 2e-15 | 28/42 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.82×** | +7.9 | 2e-13 | 29/43 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.4 | 9e-12 | 30/48 (HOP62, SW1417, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.2 | 1e-05 | 5/20 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.45×** | +5.1 | 2e-05 | 23/43 (SW 900, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.39×** | +4.5 | 3e-04 | 17/44 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.38×** | +4.4 | 4e-04 | 15/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 5e-04 | 11/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.018 | 11/46 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.029 | 2/45 (A498, SHP-77) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.082 | 8/43 (RKO, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -4.3 | 0.005 | 17/47 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.717×** | -4.3 | 0.005 | 17/43 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.749×** | -3.9 | 0.013 | 20/45 (COLO 205, SW48, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.742×** | -3.9 | 0.013 | 16/44 (SW 900, HS-578T, …) | top dose only |  |
| [[Bergenin (drug)]] 5 µM |  | 0.834× | -3.5 | 0.052 | 10/47 (PANC-1, NCI-H661, …) | rises with dose | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.065 | 14/45 (Hs 766T, NCI-H2347, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.5 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +8.5) | [[Imiquimod (maleate) (drug)]] 5 µM 0.177× (z -8.5) |
| [[A498 (line)]] | wt | 19.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 11.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HEC-1-A (line)]] | alt | 9.81 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.67× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.10 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.82× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0673× (z -10.8) |
| [[A-427 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.279× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 8.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.5) | — |
| [[C32 (line)]] | wt | 7.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0913× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 5.26 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.39× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 8.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 7.50 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.131× (z -9.6) |
| [[SW480 (line)]] | alt | 6.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AN3 CA (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGA]] | +0.69 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[PPP1CA]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[DR1]] | +0.66 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[PIGT]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 | same gene group; pathway: Attachment of GPI anchor to uPAR; STRING 999 |
| [[PRKACA]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CFL1]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ERLIN2]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[AGPAT1]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CDK2]] | +0.62 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[SUMO3]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[CYB561A3]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | -0.71 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | -0.69 | -0.56 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | -0.69 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[SNHG7]] | -0.68 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SNHG8]] | -0.67 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[NDUFB9]] | -0.67 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[SNHG32]] | -0.66 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TAF1D]] | -0.62 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ATF4]] | -0.62 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[GAS5]] | -0.62 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.62 | -0.53 / -0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBMX2]] | -0.61 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CAMLG]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPAA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises GPAA1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.5, -27.9); signed map (-27.4, -40.0). **Vector** length 69.3, 12.0% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.3 | +20.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +6.1 | +19.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +6.0 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +17.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +4.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.6 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | glycosylphosphatidylinositol anchor attachment 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,082,337-144,093,149 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAA1, hGAA1 |
| Gene groups (HGNC) | Glycosylphosphatidylinositol transamidase complex |
| Reactome | 2 pathways, smallest: Attachment of GPI anchor to uPAR; Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O43292](https://www.uniprot.org/uniprotkb/O43292) (GPI-anchor transamidase component GPAA1):

> Component of the glycosylphosphatidylinositol-anchor (GPI-anchor) transamidase (GPI-T) complex that catalyzes the formation of the linkage between a proprotein and a GPI-anchor and participates in GPI anchored protein biosynthesis. Binds GPI-anchor.

**Summary**, from NCBI Gene [8733](https://www.ncbi.nlm.nih.gov/gene/8733):

> Posttranslational glycosylphosphatidylinositol (GPI) anchor attachment serves as a general mechanism for linking proteins to the cell surface membrane. The protein encoded by this gene presumably functions in GPI anchoring at the GPI transfer step. The mRNA transcript is ubiquitously expressed in both fetal and adult tissues. The anchor attachment protein 1 contains an N-terminal signal sequence, 1 cAMP- and cGMP-dependent protein kinase phosphorylation site, 1 leucine zipper pattern, 2 …

**Accessions** — [HGNC:4446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4446) · Entrez [8733](https://www.ncbi.nlm.nih.gov/gene/8733) · UniProt [O43292](https://www.uniprot.org/uniprotkb/O43292) · Ensembl [ENSG00000197858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197858)

## Data

Gene col 12477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12477); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12477]; `tensor/DDL_lfc|DDL_z.npy` [12477]; `embed/gene_vectors.npy` [12477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12477 or target_col == 12477). Every well: [[GPAA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPAA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
