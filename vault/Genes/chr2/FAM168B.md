---
symbol: "FAM168B"
type: "gene"
col: 7590
ensembl_id: "ENSG00000152102"
name: "family with sequence similarity 168 member B"
location: "2q21.1"
module: 65
arm: "+"
pooled_cpm: 123.74
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# FAM168B

*family with sequence similarity 168 member B* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.21× (z +13.6, q 3e-39, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.804× (z -5.3, q 8e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RYK]] (+0.57, fdr 7e-06), [[CASC3]] (+0.55, fdr 1e-05), [[ILKAP]] (+0.54, fdr 2e-05); moves opposite to [[SPEN]] (-0.51, fdr 1e-05), [[HES1]] (-0.49, fdr 1e-05), [[TUT7]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +13.6 | 3e-39 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +12.2 | 1e-31 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +8.7 | 4e-16 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +8.6 | 1e-15 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +8.2 | 3e-14 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.4 | 2e-08 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.7 | 2e-04 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.6 | 3e-04 | 33/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +4.6 | 3e-04 | 33/49 (KATO III, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 6e-04 | 35/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.2 | 0.001 | 29/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.003 | 25/48 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.004 | 27/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.006 | 25/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.008 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.025 | 11/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.049 | 21/49 (C-33 A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.804×** | -5.3 | 8e-05 | 29/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -4.8 | 4e-04 | 36/48 (SW 1271, BT-474, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.787×** | -4.1 | 0.008 | 30/48 (J82, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.797×** | -3.7 | 0.026 | 24/44 (NCI-H2347, Panc 03.27, …) | rises with dose | composition shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.807×** | -3.7 | 0.026 | 26/48 (NCI-H1792, HCT15, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.6 | 0.026 | 0/50 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.820×** | -3.4 | 0.055 | 23/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.826×** | -3.3 | 0.071 | 22/48 (NCI-H2347, AsPC-1, …) | two highest doses | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.071 | 22/47 (RPMI-7951, A498, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.12 | 20/49 (LS 180, A498, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.12 | 20/48 (SW 1088, CFPAC-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.838× | -3.0 | 0.12 | 18/48 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 126 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 121 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +19.7) | — |
| [[LoVo (line)]] | wt | 106 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +14.8) | — |
| [[SW480 (line)]] | alt | 126 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +17.4) | — |
| [[BT-474 (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 86.3 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 135 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 71.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.25× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +11.8) | — |
| [[H4 (line)]] | wt | 111 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 123 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.546× (z -9.1) |
| [[HT-29 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[KATO III (line)]] | alt | 66.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 106 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 122 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 82.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.19× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[SW48 (line)]] | wt | 137 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +9.0) | — |
| [[A-427 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A498 (line)]] | wt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.4) | — |
| [[A549 (line)]] | wt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 158 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.9) | — |
| [[J82 (line)]] | alt | 121 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 168 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +10.0) | — |
| [[A-172 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 188 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 105 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYK]] | +0.57 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CASC3]] | +0.55 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ILKAP]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[FIP1L1]] | +0.51 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CLCC1]] | +0.51 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NDUFV2]] | +0.50 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GALNT11]] | +0.50 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SGK3]] | +0.50 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[FAM219B]] | +0.49 | +0.56 / +0.36 | both halves | 9e-05 |  |
| [[GK5]] | +0.49 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MTX2]] | +0.48 | +0.56 / +0.43 | both halves | 4e-05 |  |
| [[HBS1L]] | +0.48 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPEN]] | -0.51 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HES1]] | -0.49 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TUT7]] | -0.49 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[CSNK1A1]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[HAS2]] | -0.46 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[MED1]] | -0.45 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SETX]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[ZNF281]] | -0.45 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TANK]] | -0.45 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ZSWIM6]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CYTOR]] | -0.44 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[HOMER1]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FAM168B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.1, -9.6); signed map (-29.4, -14.0). **Vector** length 75.9, 21.2% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.4 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | +5.3 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | -0.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +0.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.7 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.3 |
|  | [[Thymol (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -5.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 168 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:131,047,876-131,093,460 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0280L, MANI |
| Matched by | ensembl_id |

**Function**, from UniProt [A1KXE4](https://www.uniprot.org/uniprotkb/A1KXE4) (Myelin-associated neurite-outgrowth inhibitor):

> Inhibitor of neuronal axonal outgrowth. Acts as a negative regulator of CDC42 and STAT3 and a positive regulator of STMN2. Positive regulator of CDC27.

**Summary**, from NCBI Gene [130074](https://www.ncbi.nlm.nih.gov/gene/130074):

> Predicted to act upstream of or within axonogenesis and gene expression. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27016) · Entrez [130074](https://www.ncbi.nlm.nih.gov/gene/130074) · UniProt [A1KXE4](https://www.uniprot.org/uniprotkb/A1KXE4) · Ensembl [ENSG00000152102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152102)

## Data

Gene col 7590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7590); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7590]; `tensor/DDL_lfc|DDL_z.npy` [7590]; `embed/gene_vectors.npy` [7590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7590 or target_col == 7590). Every well: [[FAM168B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM168B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
