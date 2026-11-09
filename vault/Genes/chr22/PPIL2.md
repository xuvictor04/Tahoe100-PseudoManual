---
symbol: "PPIL2"
type: "gene"
col: 1844
ensembl_id: "ENSG00000100023"
name: "peptidylprolyl isomerase like 2"
location: "22q11.21"
module: 178
arm: "+"
pooled_cpm: 32.76
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# PPIL2

*peptidylprolyl isomerase like 2* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.26× (z +5.3, q 9e-05, up in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.625× (z -15.4, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGU]] (+0.73, fdr 7e-06), [[DHX57]] (+0.70, fdr 1e-05), [[CDK5RAP1]] (+0.67, fdr 1e-05); moves opposite to [[HIVEP2]] (-0.66, fdr 1e-05), [[PSMD6-AS1]] (-0.66, fdr 3e-05), [[HNRNPK]] (-0.65, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +5.3 | 9e-05 | 23/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.24×** | +4.7 | 9e-04 | 16/48 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.067 | 14/48 (PANC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -15.4 | 0e+00 | 41/48 (SHP-77, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -11.2 | 1e-26 | 36/48 (HS-578T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -10.7 | 1e-24 | 37/48 (RPMI-7951, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.624×** | -10.1 | 1e-21 | 29/42 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.658×** | -9.7 | 4e-20 | 33/46 (HS-578T, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -9.5 | 2e-19 | 29/47 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.764×** | -8.8 | 1e-16 | 26/47 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.699×** | -8.3 | 9e-15 | 31/47 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.741×** | -6.7 | 2e-09 | 27/48 (HS-578T, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -6.6 | 3e-09 | 21/38 (C32, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -6.1 | 4e-08 | 25/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.797×** | -5.2 | 7e-06 | 18/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -5.0 | 2e-05 | 15/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.825×** | -4.4 | 3e-04 | 21/48 (HOP62, HS-578T, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -4.4 | 5e-04 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.019 | 13/48 (RPMI-7951, SW48, …) | all doses, stronger at high dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.880× | -3.0 | 0.092 | 3/48 (NCI-H460, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 45.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -12.8) |
| [[C32 (line)]] | wt | 34.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 48.9 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.4) |
| [[SHP-77 (line)]] | alt | 65.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.4) |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -21.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -8.9) |
| [[SW480 (line)]] | alt | 40.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.9) |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.255× (z -8.9) |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.360× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.9) |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.4) |
| [[KATO III (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 33.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 43.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -10.2) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.199× (z -10.4) |
| [[A-427 (line)]] | wt | 25.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -8.9) |
| [[A498 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.102× (z -9.8) |
| [[COLO 205 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.244× (z -10.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.181× (z -9.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.468× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.306× (z -8.7) ⚠ cell-cycle shift, explains ~96% of this change |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.5) |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGU]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[DHX57]] | +0.70 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.67 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PLD3]] | +0.66 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[EYA3]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MED23]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.65 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TECPR1]] | +0.63 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[TBCE]] | +0.63 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[LCMT1]] | +0.62 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[AARSD1]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.66 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.65 | -0.53 / -0.51 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[EIF4G2]] | -0.64 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[GALNT7-DT]] | -0.63 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[LINC02035]] | -0.61 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TUG1]] | -0.61 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[HIVEP1]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SEPTIN11]] | -0.59 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[IRF2]] | -0.58 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PLSCR2]] | -0.58 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[SLC39A10]] | -0.58 | -0.57 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PPIL2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises PPIL2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.4, -4.2); signed map (-17.7, -18.7). **Vector** length 85.6, 16.7% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.4 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.6 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +0.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.8 | +1.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -15.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:21,666,000-21,700,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBOX7, CYC4, Cyp-60 |
| Gene groups (HGNC) | U-box domain containing; Cyclophilin peptidylprolyl isomerases; Spliceosomal Bact complex |
| Reactome | 7 pathways, smallest: Basigin interactions; Cell surface interactions at the vascular wall; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13356](https://www.uniprot.org/uniprotkb/Q13356) (RING-type E3 ubiquitin-protein ligase PPIL2):

> Has a ubiquitin-protein ligase activity acting as an E3 ubiquitin protein ligase or as an ubiquitin-ubiquitin ligase promoting elongation of ubiquitin chains on substrates. By mediating 'Lys-48'-linked polyubiquitination of proteins could target them for proteasomal degradation. May also function as a chaperone, playing a role in transport to the cell membrane of BSG/Basigin for instance. Probable inactive PPIase with no peptidyl-prolyl cis-trans isomerase activity. As a component of the minor …

**Summary**, from NCBI Gene [23759](https://www.ncbi.nlm.nih.gov/gene/23759):

> This gene is a member of the cyclophilin family of peptidylprolyl isomerases. The cyclophilins are a highly conserved ubiquitous family, members of which play an important role in protein folding, immunosuppression by cyclosporin A, and infection of HIV-1 virions. This protein interacts with the proteinase inhibitor eglin c and is localized in the nucleus. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:9261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9261) · Entrez [23759](https://www.ncbi.nlm.nih.gov/gene/23759) · UniProt [Q13356](https://www.uniprot.org/uniprotkb/Q13356) · Ensembl [ENSG00000100023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100023)

## Data

Gene col 1844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1844); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1844]; `tensor/DDL_lfc|DDL_z.npy` [1844]; `embed/gene_vectors.npy` [1844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1844 or target_col == 1844). Every well: [[PPIL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
