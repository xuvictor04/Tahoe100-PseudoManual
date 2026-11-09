---
symbol: "CACNA1A"
type: "gene"
col: 6575
ensembl_id: "ENSG00000141837"
name: "calcium voltage-gated channel subunit alpha1 A"
location: "19p13.13"
module: 165
arm: "+"
pooled_cpm: 17.62
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# CACNA1A

*calcium voltage-gated channel subunit alpha1 A* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.68× (z +19.8, q 0e+00, up in 8 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.78× (z +19.3, q 0e+00, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.659× (z -5.6, q 1e-05, down in 17 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIRC3-AS1]] (+0.67, fdr 7e-06), [[ADAMTS18]] (+0.65, fdr 1e-05), [[ADAMTSL1]] (+0.64, fdr 7e-06); moves opposite to [[ARMC8]] (-0.49, fdr 3e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HGF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.68×** | +19.8 | 0e+00 | 8/16 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.78×** | +19.3 | 0e+00 | 27/35 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.64×** | +17.2 | 0e+00 | 15/23 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +16.5 | 0e+00 | 16/30 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.70×** | +13.2 | 5e-38 | 25/33 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +9.9 | 4e-21 | 13/32 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +8.9 | 4e-17 | 6/19 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +7.6 | 2e-12 | 14/35 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +7.3 | 2e-11 | 16/33 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.4 | 9e-09 | 12/35 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +5.9 | 2e-07 | 12/35 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.50×** | +5.4 | 3e-06 | 12/35 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.001 | 12/35 (C-33 A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.37×** | +4.0 | 0.002 | 10/30 (AsPC-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.018 | 10/35 (C32, SW1417, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.058 | 3/33 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.073 | 2/31 (SW1417, C32) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.087 | 1/28 (HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.659×** | -5.6 | 1e-05 | 17/33 (SHP-77, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.690×** | -4.9 | 2e-04 | 13/35 (SHP-77, H4, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.663×** | -4.6 | 9e-04 | 10/32 (SHP-77, COLO 205, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.730×** | -4.2 | 0.004 | 11/34 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.811×** | -4.0 | 0.009 | 12/35 (SNU-423, C32, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.762×** | -3.6 | 0.027 | 14/33 (SHP-77, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.739×** | -3.5 | 0.036 | 9/34 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.772×** | -3.5 | 0.039 | 13/32 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.747×** | -3.4 | 0.041 | 8/33 (SHP-77, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.776×** | -3.4 | 0.041 | 12/33 (hTERT-HPNE, SHP-77, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.780×** | -3.3 | 0.048 | 9/33 (SHP-77, H4, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.054 | 10/33 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -3.2 | 0.054 | 11/35 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.797×** | -3.0 | 0.099 | 17/35 (SHP-77, H4, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 219 | 0 | 28 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0737× (z -23.9) |
| [[AsPC-1 (line)]] | alt | 17.3 | 3 (2 ⚠) | 2 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.75× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.8) |
| [[A498 (line)]] | wt | 5.17 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.84× (z +10.3) | — |
| [[H4 (line)]] | wt | 42.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0313× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -9.2) |
| [[HOP62 (line)]] | alt | 5.39 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.5× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.34× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.82× (z +9.6) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.159× (z -8.6) |
| [[C32 (line)]] | wt | 16.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.21× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 25.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 13.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.3× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 4.51× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 39.1 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.158× (z -11.7) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 6.02 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.94× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 6.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.01× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 6.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 85.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.8) |
| [[KATO III (line)]] | alt | 5.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.03× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 5.43 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.02× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 4.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.0× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 4.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +9.0) | — |
| [[A-172 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIRC3-AS1]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS18]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ADAMTSL1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RYR3]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 | STRING 490 |
| [[ATP8A2]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ABCA13]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SLC8A1-AS1]] | +0.62 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[COL23A1]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RETREG1-AS1]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[LINC01060]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGF]] | B | HGF activity raises CACNA1A's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without HGF | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[HGF]] | B | HGF activity weakens CACNA1A's drug response | lines that do not express HGF (27) vs lines expressing it (8) | (z diff -3.79); strongest at Dinaciclib 5 µM: 2.89x vs 0.59x (z diff -6.6) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; target measured in part of the lines; artifact flags |
| [[DSCAM]] | B | DSCAM activity raises CACNA1A's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.33× lower at baseline in the lines without DSCAM | 0.011 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers CACNA1A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[NETO1]] | B | NETO1 activity raises CACNA1A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.41× lower at baseline in the lines without NETO1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[TOP2A]] | B | TOP2A activity lowers CACNA1A's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCAM]] | B | DSCAM activity weakens CACNA1A's drug response | lines that do not express DSCAM (24) vs lines expressing it (11) | the lines without DSCAM respond 10.06× as strongly (z diff -2.64); strongest at Panobinostat 5 µM: 1.73x vs 0.61x (z diff -4.8) | 0.096 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.7, 12.6); signed map (32.8, 27.6). **Vector** length 81.6, 17.4% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.3 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +17.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +1.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -4.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel subunit alpha1 A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,206,442-13,624,489 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cav2.1, EA2, APCA, HPCA, FHM; previously CACNL1A4, SCA6, MHP1, MHP |
| Gene groups (HGNC) | Calcium voltage-gated channel alpha1 subunits |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 5 pathways, smallest: Presynaptic depolarization and calcium channel opening; Regulation of insulin secretion; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00555](https://www.uniprot.org/uniprotkb/O00555) (Voltage-dependent P/Q-type calcium channel subunit alpha-1A):

> Voltage-sensitive calcium channels (VSCC) mediate the entry of calcium ions into excitable cells and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, gene expression, cell motility, cell division and cell death. The isoform alpha-1A gives rise to P and/or Q-type calcium currents. P/Q-type calcium channels belong to the 'high-voltage activated' (HVA) group and are specifically blocked by the spider …

**Summary**, from NCBI Gene [773](https://www.ncbi.nlm.nih.gov/gene/773):

> Voltage-dependent calcium channels mediate the entry of calcium ions into excitable cells, and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, and gene expression. Calcium channels are multisubunit complexes composed of alpha-1, beta, alpha-2/delta, and gamma subunits. The channel activity is directed by the pore-forming alpha-1 subunit, whereas, the others act as auxiliary subunits regulating this activity. The …

**Accessions** — [HGNC:1388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1388) · Entrez [773](https://www.ncbi.nlm.nih.gov/gene/773) · UniProt [O00555](https://www.uniprot.org/uniprotkb/O00555) · Ensembl [ENSG00000141837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141837)

## Data

Gene col 6575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6575); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6575]; `tensor/DDL_lfc|DDL_z.npy` [6575]; `embed/gene_vectors.npy` [6575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6575 or target_col == 6575). Every well: [[CACNA1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
