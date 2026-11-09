---
symbol: "RIMKLB"
type: "gene"
col: 9327
ensembl_id: "ENSG00000166532"
name: "ribosomal modification protein rimK like family member B"
location: "12p13.31"
module: 143
arm: "+"
pooled_cpm: 74.65
n_lines_expressing: 37
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# RIMKLB

*ribosomal modification protein rimK like family member B* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.32× (z +5.7, q 8e-06, up in 17 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW 900 3.21×, H4 3.57×, NCI-H23 1.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H2347 2.34×, NCI-H460 1.83×); [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 1.91×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 2.65×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 2.42×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.480× (z -15.0, q 0e+00, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLPP2]] (+0.58, fdr 1e-05), [[SGMS1]] (+0.55, fdr 1e-05), [[JADE3]] (+0.52, fdr 4e-05); moves opposite to [[WDR37]] (-0.50, fdr 6e-05), [[UBE4A]] (-0.48, fdr 4e-05), [[TUBGCP2]] (-0.46, fdr 1e-04).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EPB41L4A]] → it (grade B ⚠); 3 go from it, the strongest it → [[EPB41L4A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9327.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW 900 3.21×, H4 3.57×, NCI-H23 1.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H2347 2.34×, NCI-H460 1.83×); [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 1.91×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 2.65×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 2.42×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.7 | 8e-06 | 17/35 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.026 | 14/35 (SW480, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.7 | 0.049 | 13/35 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.2 | 0.21 | 10/35 (H4, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.26 | 8/34 (CFPAC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.480×** | -15.0 | 0e+00 | 27/35 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.546×** | -12.4 | 1e-32 | 27/35 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -8.8 | 2e-16 | 23/33 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.681×** | -7.8 | 6e-13 | 21/35 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.710×** | -7.0 | 3e-10 | 21/35 (A-427, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.722×** | -6.4 | 1e-08 | 17/33 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -6.3 | 2e-08 | 22/35 (LoVo, AN3 CA, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -5.8 | 4e-07 | 19/34 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.2 | 1e-05 | 3/36 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -4.8 | 1e-04 | 12/35 (J82, A-172, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.830×** | -3.8 | 0.007 | 14/34 (SW480, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -3.6 | 0.015 | 8/35 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.854× | -3.2 | 0.056 | 8/36 (HEC-1-A, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 231 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.435× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 71.2 | 2 (1 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.91× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[GSK1059615 (drug)]] 5 µM 3.84× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 86.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -13.7) |
| [[A549 (line)]] | wt | 146 | 1 | 3 (2 ⚠) | [[Medroxyprogesterone acetate (drug)]] 5 µM 2.25× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -9.6) |
| [[J82 (line)]] | alt | 91.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -14.4) |
| [[A-172 (line)]] | wt | 79.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.382× (z -9.5) |
| [[A498 (line)]] | wt | 63.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.8) |
| [[LoVo (line)]] | wt | 409 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.251× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 166 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -9.0) |
| [[HOP62 (line)]] | alt | 74.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.437× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 50.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 31.5 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.34× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 51.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 262 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 69.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.65× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -8.5) |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -12.3) |
| [[C-33 A (line)]] | alt | 107 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -10.0) |
| [[H4 (line)]] | wt | 60.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 67.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.16 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLPP2]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SGMS1]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[JADE3]] | +0.52 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[OVOL2]] | +0.48 | +0.43 / +0.22 | both halves | 6e-04 |  |
| [[MEMO1]] | +0.47 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[SNX24]] | +0.44 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[PIP5K1A]] | +0.44 | +0.32 / +0.40 | both halves | 2e-04 |  |
| [[NCOA1]] | +0.44 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[DPY19L1P1]] | +0.43 | +0.27 / +0.38 | both halves | 3e-04 |  |
| [[RNF138]] | +0.43 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[TRABD2B]] | +0.43 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[ATXN2]] | +0.42 | +0.43 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR37]] | -0.50 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[UBE4A]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TUBGCP2]] | -0.46 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[SEC13]] | -0.44 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[EDRF1]] | -0.43 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[COPG1]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[LONP2]] | -0.42 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[POLR2C]] | -0.42 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[INTS4]] | -0.41 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[RTF2]] | -0.40 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[COMMD9]] | -0.39 | -0.17 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[COPB1]] | -0.39 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[C1orf52]] | -0.39 | -0.24 / -0.38 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4A]] | B | EPB41L4A activity raises RIMKLB's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without EPB41L4A | 0.059 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[HDAC6]] | B | HDAC6 activity raises RIMKLB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TEAD4]] | C | TEAD4 activity raises RIMKLB's level | lines that do not express TEAD4 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without TEAD4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MMP25, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4A]] | B | RIMKLB activity raises EPB41L4A's level | lines that do not express RIMKLB (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without RIMKLB | 0.058 | ⚠ within organs, on part of the lines; also absent: DNAAF9, GJC1, ANKRD6 |
| [[LATS2]] | B | RIMKLB activity raises LATS2's level | lines that do not express RIMKLB (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without RIMKLB | 0.075 | ⚠ within organs, on part of the lines; also absent: DNAAF9, GJC1, ANKRD6 |
| [[TEAD4]] | B | RIMKLB activity raises TEAD4's level | lines that do not express RIMKLB (13) vs lines expressing it (37) | 1.10× lower at baseline in the lines without RIMKLB | 0.0997 | ⚠ within organs, on part of the lines; also absent: DNAAF9, GJC1, ANKRD6 |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.406). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, -25.0); signed map (9.0, -3.8). **Vector** length 79.2, 17.8% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.1 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.2 | +2.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -15.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal modification protein rimK like family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,681,600-8,783,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1238, NAAGS, NAAGS-I; previously FAM80B |
| Gene groups (HGNC) | ATP-grasp fold containing; Ribosomal modification protein rimK like family |
| Reactome | 2 pathways, smallest: Glutamate and glutamine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULI2](https://www.uniprot.org/uniprotkb/Q9ULI2) (Beta-citrylglutamate synthase B):

> Catalyzes the synthesis of beta-citryl-L-glutamate and N-acetyl-L-aspartyl-L-glutamate. Beta-citryl-L-glutamate is synthesized more efficiently than N-acetyl-L-aspartyl-L-glutamate.

**Summary**, from NCBI Gene [57494](https://www.ncbi.nlm.nih.gov/gene/57494):

> Predicted to enable N-acetyl-L-aspartate-L-glutamate ligase activity and citrate-L-glutamate ligase activity. Predicted to be involved in L-amino acid metabolic process. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29228) · Entrez [57494](https://www.ncbi.nlm.nih.gov/gene/57494) · UniProt [Q9ULI2](https://www.uniprot.org/uniprotkb/Q9ULI2) · Ensembl [ENSG00000166532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166532)

## Data

Gene col 9327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9327); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9327]; `tensor/DDL_lfc|DDL_z.npy` [9327]; `embed/gene_vectors.npy` [9327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9327 or target_col == 9327). Every well: [[RIMKLB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMKLB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
