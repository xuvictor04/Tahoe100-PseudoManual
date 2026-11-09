---
symbol: "CNIH3"
type: "gene"
col: 6803
ensembl_id: "ENSG00000143786"
name: "cornichon family AMPA receptor auxiliary protein 3"
location: "1q42.12"
module: 92
arm: "+"
pooled_cpm: 38.69
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# CNIH3

*cornichon family AMPA receptor auxiliary protein 3* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.40× (z +29.0, q 0e+00, up in 28 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.611× (z -6.8, q 6e-09, down in 24 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.755× (z -5.5, q 8e-06, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02813]] (+0.79, fdr 7e-06, ⚠ same locus), [[SHC3]] (+0.65, fdr 7e-06), [[MANCR]] (+0.64, fdr 7e-06), [[ZNF385D]] (+0.62, fdr 7e-06).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC02813]] → it (grade B ⚠); 3 go from it, the strongest it → [[ARHGAP17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.40×** | +29.0 | 0e+00 | 28/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.63×** | +13.4 | 2e-38 | 28/35 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +8.8 | 4e-16 | 18/35 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.1 | 1e-13 | 17/36 (HEC-1-A, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +7.2 | 7e-11 | 15/36 (NCI-H460, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.27×** | +4.8 | 2e-04 | 14/36 (NCI-H2347, A498, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 14/36 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.004 | 14/36 (C32, NCI-H1792, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.015 | 5/36 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.5 | 0.025 | 9/32 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.4 | 0.037 | 7/36 (NCI-H23, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.611×** | -6.8 | 6e-09 | 24/35 (PANC-1, C32, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.654×** | -5.9 | 1e-06 | 18/36 (PANC-1, C32, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.755×** | -5.5 | 8e-06 | 20/36 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.682×** | -5.3 | 2e-05 | 20/36 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.743×** | -4.9 | 1e-04 | 18/36 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.698×** | -4.5 | 6e-04 | 17/36 (HOP62, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.723×** | -4.5 | 6e-04 | 18/36 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -4.3 | 1e-03 | 16/34 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.748×** | -4.0 | 0.004 | 20/36 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -3.8 | 0.009 | 16/36 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.761×** | -3.8 | 0.009 | 17/35 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.609×** | -3.6 | 0.016 | 15/32 (RPMI-7951, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.775×** | -3.5 | 0.020 | 15/36 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.799×** | -3.5 | 0.020 | 14/36 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.768×** | -3.3 | 0.035 | 19/36 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **0.659×** | -3.0 | 0.091 | 11/34 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 15 (10 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.333× (z -26.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.183× (z -11.8) |
| [[HOP62 (line)]] | alt | 107 | 0 | 8 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.559× (z -13.5) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.144× (z -11.6) |
| [[A-172 (line)]] | wt | 62.7 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.7) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.144× (z -11.3) |
| [[SW 900 (line)]] | alt | 176 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.166× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 111 | 0 | 4 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.431× (z -16.4) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.253× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 12.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.96× (z +20.6) | — |
| [[PANC-1 (line)]] | alt | 35.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +15.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -10.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 33.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 78.5 | 0 | 3 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.196× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.154× (z -9.8) |
| [[SHP-77 (line)]] | alt | 12.7 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +12.6) | [[Saquinavir (drug)]] 0.5 µM 0.0760× (z -12.4) |
| [[SNU-423 (line)]] | alt | 98.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 35.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.61× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 14.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +8.7) | [[Pimozide (drug)]] 0.05 µM 0.0649× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 21.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 317 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.373× (z -9.2) |
| [[A498 (line)]] | wt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +16.7) | — |
| [[BT-474 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +10.6) | — |
| [[C32 (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 49.6 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.301× (z -9.0) |
| [[HCT15 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +9.9) | — |
| [[J82 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.70× (z +13.2) | — |
| [[A-427 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02813]] | +0.79 | +0.76 / +0.86 | both halves | 7e-06 | ⚠ same locus (25.8 kb, same strand: neighbours can correlate without regulation) |
| [[SHC3]] | +0.65 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MANCR]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ZNF385D]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TRBC2]] | +0.62 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[RPSAP52]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[RASGRF2]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[EVA1A]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ADGRL4]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[NTNG2]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[STK32B]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02813]] | B | LINC02813 activity raises CNIH3's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 4.89× lower at baseline in the lines without LINC02813 | 4e-05 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[AFF3]] | B | AFF3 activity raises CNIH3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.22× lower at baseline in the lines without AFF3 | 0.002 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[MIR3681HG]] | B | MIR3681HG activity raises CNIH3's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 3.11× lower at baseline in the lines without MIR3681HG | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CNIH3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CSMD2]] | B | CSMD2 activity raises CNIH3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without CSMD2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[MIR3681HG]] | B | MIR3681HG activity weakens CNIH3's drug response | lines that do not express MIR3681HG (17) vs lines expressing it (19) | the lines without MIR3681HG respond 1.39× as strongly (z diff -0.63); strongest at Idarubicin (hydrochloride) 5 µM: 4.45x vs 1.84x (z diff -5.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CYGB]] | B | CYGB activity raises CNIH3's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.51× lower at baseline in the lines without CYGB | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity strengthens CNIH3's drug response | lines that do not express LINC02813 (14) vs lines expressing it (22) | the lines without LINC02813 respond 0.98× as strongly (z diff -0.24); strongest at Trametinib 0.5 µM: 0.85x vs 0.50x (z diff +3.5) | 0.065 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; target measured in part of the lines; both ways; artifact flags |
| [[ZNF385D]] | B | ZNF385D activity raises CNIH3's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.58× lower at baseline in the lines without ZNF385D | 0.078 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[ARSG]] | B | ARSG activity raises CNIH3's level | lines that do not express ARSG (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without ARSG | 0.084 | ⚠ within organs, on part of the lines; also absent: PHGDH, RNF157, C2orf92; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP17]] | B | CNIH3 activity lowers ARHGAP17's level | lines that do not express CNIH3 (12) vs lines expressing it (38) | 1.32× higher at baseline in the lines without CNIH3 | 0.004 | ⚠ within organs, on part of the lines; also absent: HDGFL3, RIMKLB, ZNF793; maybe low, not absent |
| [[SHC3]] | B | CNIH3 activity raises SHC3's level | lines that do not express CNIH3 (12) vs lines expressing it (38) | 2.33× lower at baseline in the lines without CNIH3 | 0.080 | ⚠ within organs, on part of the lines; also absent: HDGFL3, RIMKLB, ZNF793; maybe low, not absent |
| [[HMGA1]] | B | CNIH3 activity lowers HMGA1's level | lines that do not express CNIH3 (12) vs lines expressing it (38) | 1.56× higher at baseline in the lines without CNIH3 | 0.085 | ⚠ within organs, on part of the lines; also absent: HDGFL3, RIMKLB, ZNF793; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 9.1); signed map (12.0, 50.3). **Vector** length 121, 33.8% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.50 to 8); *MAPK family signaling cascades* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.2 | +13.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +29.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | +1.8 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -6.9 | -4.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.7 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cornichon family AMPA receptor auxiliary protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:224,434,660-224,740,554 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38993, CNIH-3 |
| Gene groups (HGNC) | Cornichon family |
| Reactome | 7 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBE1](https://www.uniprot.org/uniprotkb/Q8TBE1) (Protein cornichon homolog 3):

> Regulates the trafficking and gating properties of AMPA-selective glutamate receptors (AMPARs). Promotes their targeting to the cell membrane and synapses and modulates their gating properties by regulating their rates of activation, deactivation and desensitization.

**Summary**, from NCBI Gene [149111](https://www.ncbi.nlm.nih.gov/gene/149111):

> Predicted to enable signaling receptor binding activity. Involved in regulation of AMPA receptor activity. Predicted to be located in dendritic shaft and postsynaptic membrane. Predicted to be part of AMPA glutamate receptor complex. Predicted to be active in dendrite and synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26802) · Entrez [149111](https://www.ncbi.nlm.nih.gov/gene/149111) · UniProt [Q8TBE1](https://www.uniprot.org/uniprotkb/Q8TBE1) · Ensembl [ENSG00000143786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143786)

## Data

Gene col 6803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6803); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6803]; `tensor/DDL_lfc|DDL_z.npy` [6803]; `embed/gene_vectors.npy` [6803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6803 or target_col == 6803). Every well: [[CNIH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNIH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
