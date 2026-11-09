---
symbol: "CARM1"
type: "gene"
col: 6623
ensembl_id: "ENSG00000142453"
name: "coactivator associated arginine methyltransferase 1"
location: "19p13.2"
module: 2
arm: "+"
pooled_cpm: 32.01
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CARM1

*coactivator associated arginine methyltransferase 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +12.5, q 7e-33, up in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.51× (z +4.4, q 0.001, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.688× (z -5.8, q 3e-06, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP2A2]] (+0.61, fdr 1e-05), [[KLHL17]] (+0.61, fdr 1e-05), [[DVL1]] (+0.60, fdr 1e-05); moves opposite to [[CPT2]] (-0.54, fdr 1e-04), [[ZMAT2]] (-0.51, fdr 4e-05), [[IFNAR1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +12.5 | 7e-33 | 36/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.9 | 2e-25 | 34/37 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +8.1 | 7e-14 | 30/43 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.7 | 2e-09 | 39/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.1 | 4e-05 | 30/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.4 | 0.001 | 21/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 0.001 | 21/48 (SW480, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.002 | 23/45 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.013 | 17/46 (SHP-77, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.014 | 21/48 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.016 | 16/45 (H4, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.26×** | +3.6 | 0.016 | 20/46 (Panc 03.27, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.26×** | +3.6 | 0.016 | 18/48 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.048 | 16/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.062 | 10/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 1.15× | +3.1 | 0.063 | 6/48 (SNU-1, hTERT-HPNE, …) | rises with dose |  |
| [[Erythromycin (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.098 | 12/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.32×** | +2.9 | 0.098 | 12/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.688×** | -5.8 | 3e-06 | 28/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.694×** | -5.7 | 4e-06 | 26/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -5.2 | 4e-05 | 29/48 (SW1417, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.809×** | -4.7 | 4e-04 | 24/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.739×** | -4.5 | 7e-04 | 24/47 (J82, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.830×** | -4.1 | 0.004 | 22/48 (LS 180, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -4.0 | 0.006 | 20/48 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.786×** | -3.7 | 0.013 | 21/48 (J82, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.793×** | -3.6 | 0.020 | 23/48 (SW 1088, RKO, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.783×** | -3.5 | 0.025 | 16/47 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.797×** | -3.3 | 0.057 | 6/48 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.814×** | -3.2 | 0.063 | 18/48 (A-172, LoVo, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.817× | -3.0 | 0.11 | 16/48 (LS 180, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 58.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-427 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[KATO III (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.86× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 45.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.89× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0901× (z -13.9) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2A2]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[DVL1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 | STRING 471 |
| [[UCKL1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[AMFR]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MAZ]] | +0.58 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[BRF1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TRABD]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TCF3]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ZDHHC18]] | +0.56 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ZDHHC8]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 | pathway: Mitochondrial biogenesis; STRING 921 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT2]] | -0.54 | -0.55 / -0.33 | both halves | 1e-04 | pathway: PPARA activates gene expression; STRING 439 |
| [[ZMAT2]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[IFNAR1]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RRAGA]] | -0.47 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[GPANK1]] | -0.45 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[SCOC]] | -0.44 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[ZNF341-AS1]] | -0.44 | -0.44 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises CARM1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without NCS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[LRP3]] | B | LRP3 activity raises CARM1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without LRP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CARM1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.1, -24.6); signed map (-40.8, -27.8). **Vector** length 68.6, 13.7% of its response variance represented; |z| ≥ 3 in 694 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +12.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.2 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | coactivator associated arginine methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,871,553-10,923,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRMT4 |
| Gene groups (HGNC) | 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Reactome | 29 pathways, smallest: TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest; BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X55](https://www.uniprot.org/uniprotkb/Q86X55) (Histone-arginine methyltransferase CARM1):

> Methylates (mono- and asymmetric dimethylation) the guanidino nitrogens of arginyl residues in several proteins involved in DNA packaging, transcription regulation, pre-mRNA splicing, and mRNA stability. Recruited to promoters upon gene activation together with histone acetyltransferases from EP300/P300 and p160 families, methylates histone H3 at 'Arg-17' (H3R17me), forming mainly asymmetric dimethylarginine (H3R17me2a), leading to activation of transcription via chromatin remodeling. During …

**Summary**, from NCBI Gene [10498](https://www.ncbi.nlm.nih.gov/gene/10498):

> This gene belongs to the protein arginine methyltransferase (PRMT) family. The encoded enzyme catalyzes the methylation of guanidino nitrogens of arginyl residues of proteins. The enzyme acts specifically on histones and other chromatin-associated proteins and is involved in regulation of gene expression. The enzyme may act in association with other proteins or within multi-protein complexes and may play a role in cell type-specific functions and cell lineage specification. A related pseudogene …

**Accessions** — [HGNC:23393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23393) · Entrez [10498](https://www.ncbi.nlm.nih.gov/gene/10498) · UniProt [Q86X55](https://www.uniprot.org/uniprotkb/Q86X55) · Ensembl [ENSG00000142453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142453)

## Data

Gene col 6623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6623); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6623]; `tensor/DDL_lfc|DDL_z.npy` [6623]; `embed/gene_vectors.npy` [6623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6623 or target_col == 6623). Every well: [[CARM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
