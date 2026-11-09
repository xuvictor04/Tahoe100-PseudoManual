---
symbol: "BAG4"
type: "gene"
col: 8011
ensembl_id: "ENSG00000156735"
name: "BAG cochaperone 4"
location: "8p11.23"
module: 30
arm: "+"
pooled_cpm: 35.27
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# BAG4

*BAG cochaperone 4* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.73× (z +17.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.628× (z -8.3, q 5e-14, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tirabrutinib (drug)]] 0.5 µM: 0.815× (z -3.7, q 0.048, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 0.260×, NCI-H2347 0.335×, SW480 0.445×, AsPC-1 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.435×, NCI-H2347 0.427×, LS 180 0.323×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.379×, Panc 03.27 0.389×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.295×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.246×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAF1]] (+0.70, fdr 7e-06), [[DUSP11]] (+0.68, fdr 7e-06), [[ALG9]] (+0.67, fdr 1e-05); moves opposite to [[FKRP]] (-0.69, fdr 1e-05), [[CEACAM19]] (-0.60, fdr 1e-05), [[LINC00513]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CREB5]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Furosemide (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +17.9 | 0e+00 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +16.4 | 0e+00 | 46/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +14.4 | 6e-45 | 46/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.52×** | +11.7 | 1e-29 | 37/49 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.3 | 9e-15 | 29/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +8.0 | 1e-13 | 31/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.4 | 1e-08 | 29/48 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +6.2 | 4e-08 | 29/47 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.28×** | +6.2 | 4e-08 | 27/48 (SW48, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.41×** | +5.9 | 2e-07 | 22/46 (LoVo, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 3e-06 | 29/46 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.2 | 1e-05 | 28/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +4.8 | 6e-05 | 20/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.016 | 14/48 (A-172, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.21×** | +3.4 | 0.022 | 17/48 (SW480, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.031 | 13/46 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8011.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 0.260×, NCI-H2347 0.335×, SW480 0.445×, AsPC-1 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.435×, NCI-H2347 0.427×, LS 180 0.323×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.379×, Panc 03.27 0.389×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.295×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.246×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.628×** | -8.3 | 5e-14 | 31/44 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -6.8 | 3e-09 | 23/38 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.815×** | -3.7 | 0.048 | 14/48 (SW1417, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.823×** | -3.5 | 0.070 | 18/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -3.2 | 0.15 | 14/48 (SW480, BT-474, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.784× | -3.1 | 0.18 | 14/46 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.18 | 8/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.19 | 9/48 (CHP-212, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.2 | 9 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.74× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -12.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 31.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.5) | — |
| [[A549 (line)]] | wt | 29.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +9.4) | — |
| [[J82 (line)]] | alt | 32.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 72.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.4) | — |
| [[RKO (line)]] | wt | 32.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.89× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 35.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +8.7) | [[Lonafarnib (drug)]] 5 µM 0.150× (z -8.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 66.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 67.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 55.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.295× (z -10.1) |
| [[KATO III (line)]] | alt | 38.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +8.5) | — |
| [[LoVo (line)]] | wt | 24.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.246× (z -8.6) |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAF1]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.68 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[ALG9]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[TMUB1]] | +0.66 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ASB7]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.65 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[KIAA2013]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MED23]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.65 | +0.62 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKRP]] | -0.69 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[CEACAM19]] | -0.60 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[LINC00513]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.60 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[SSUH2]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[LINC00641]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SMCO2]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ST7L]] | -0.57 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[GCNT4]] | -0.56 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[DESI1]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB5]] | B | CREB5 activity lowers BAG4's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.35× higher at baseline in the lines without CREB5 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Furosemide (drug)]] 0.5 µM | C | BAG4's natural level raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | BAG4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.304 over the table, 0.053 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | BAG4's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | BAG4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.57 | 0.510 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.4, -11.3); signed map (-31.8, -10.1). **Vector** length 87.0, 20.1% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +14.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +16.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +17.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +6.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.6 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.3 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | BAG cochaperone 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,176,533-38,213,301 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SODD |
| Gene groups (HGNC) | BAG cochaperones |
| Reactome | 11 pathways, smallest: Signaling by plasma membrane FGFR1 fusions; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [O95429](https://www.uniprot.org/uniprotkb/O95429) (BAG family molecular chaperone regulator 4):

> Inhibits the chaperone activity of HSP70/HSC70 by promoting substrate release (By similarity). Prevents constitutive TNFRSF1A signaling. Negative regulator of PRKN translocation to damaged mitochondria.

**Summary**, from NCBI Gene [9530](https://www.ncbi.nlm.nih.gov/gene/9530):

> The protein encoded by this gene is a member of the BAG1-related protein family. BAG1 is an anti-apoptotic protein that functions through interactions with a variety of cell apoptosis and growth related proteins including BCL-2, Raf-protein kinase, steroid hormone receptors, growth factor receptors and members of the heat shock protein 70 kDa family. This protein contains a BAG domain near the C-terminus, which could bind and inhibit the chaperone activity of Hsc70/Hsp70. This protein was found …

**Accessions** — [HGNC:940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:940) · Entrez [9530](https://www.ncbi.nlm.nih.gov/gene/9530) · UniProt [O95429](https://www.uniprot.org/uniprotkb/O95429) · Ensembl [ENSG00000156735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156735)

## Data

Gene col 8011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8011); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8011]; `tensor/DDL_lfc|DDL_z.npy` [8011]; `embed/gene_vectors.npy` [8011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8011 or target_col == 8011). Every well: [[BAG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
