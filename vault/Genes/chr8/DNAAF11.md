---
symbol: "DNAAF11"
type: "gene"
col: 4963
ensembl_id: "ENSG00000129295"
name: "dynein axonemal assembly factor 11"
location: "8q24.22"
module: 155
arm: "+"
pooled_cpm: 8.59
n_lines_expressing: 43
n_dd_up: 27
n_dd_down: 16
n_dd_up_clean: 21
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# DNAAF11

*dynein axonemal assembly factor 11* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.92× (z +10.9, q 9e-25, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.449× (z -8.1, q 3e-13, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCDC1]] (+0.65, fdr 7e-06), [[DNAH7]] (+0.53, fdr 1e-05), [[SERPINB3]] (+0.53, fdr 3e-05); moves opposite to [[ACSS1]] (-0.47, fdr 5e-04), [[KLHL8]] (-0.47, fdr 6e-05), [[ITPK1]] (-0.43, fdr 6e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02015]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC25A15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +10.9 | 9e-25 | 30/40 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.76×** | +10.3 | 2e-22 | 29/40 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +10.1 | 8e-22 | 33/40 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +7.9 | 4e-13 | 6/12 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +7.5 | 9e-12 | 27/40 (HT-29, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.8 | 1e-09 | 19/36 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +6.1 | 8e-08 | 19/36 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.9 | 2e-07 | 11/26 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.03×** | +5.9 | 3e-07 | 16/39 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.43×** | +5.2 | 1e-05 | 16/39 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 3e-04 | 6/17 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 17/38 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +4.4 | 4e-04 | 17/40 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.4 | 4e-04 | 8/41 (SHP-77, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 11/34 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 12/37 (SW 900, SK-MEL-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.017 | 4/40 (CFPAC-1, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.048 | 10/38 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.061 | 9/38 (AsPC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -8.1 | 3e-13 | 28/40 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -7.8 | 2e-12 | 24/39 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -6.7 | 3e-09 | 24/35 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -5.3 | 2e-05 | 22/38 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.628×** | -4.7 | 3e-04 | 14/40 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.619×** | -4.5 | 6e-04 | 15/40 (BT-474, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -4.5 | 7e-04 | 18/40 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.0 | 0.005 | 18/32 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.760×** | -3.9 | 0.005 | 18/39 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.680×** | -3.9 | 0.005 | 15/40 (BT-474, RKO, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.500×** | -3.7 | 0.012 | 13/34 (NCI-H23, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -3.5 | 0.022 | 13/40 (BT-474, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.690×** | -3.5 | 0.022 | 12/40 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.719×** | -3.3 | 0.033 | 11/40 (C-33 A, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.736×** | -3.1 | 0.070 | 14/40 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.652×** | -3.1 | 0.070 | 8/40 (HEC-1-A, CHP-212, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 40.5 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0176× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0234× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 35.0 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0785× (z -16.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0416× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -13.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.0) |
| [[RKO (line)]] | wt | 12.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -10.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0792× (z -14.5) |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 2.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCDC1]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[DNAH7]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 | STRING 599 |
| [[SERPINB3]] | +0.53 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[ST8SIA6-AS1]] | +0.51 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[DNAI7]] | +0.51 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[RIMS2]] | +0.50 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[SERPINB4]] | +0.50 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[DRC3]] | +0.48 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[LMLN]] | +0.47 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[FANK1]] | +0.47 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ADAM28]] | +0.47 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[GUSBP1-1]] | +0.46 | +0.47 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSS1]] | -0.47 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[KLHL8]] | -0.47 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ITPK1]] | -0.43 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[SLC25A15]] | -0.41 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[ASB13]] | -0.40 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[SLC29A3]] | -0.39 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[ZYG11A]] | -0.37 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[CRYL1]] | -0.37 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ARHGEF26]] | -0.37 | -0.47 / -0.22 | both halves | 6e-04 |  |
| [[DCTD]] | -0.36 | -0.48 / -0.21 | both halves | 6e-04 |  |
| [[SLC35A1]] | -0.36 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[JDP2]] | -0.36 | -0.36 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02015]] | B | LINC02015 activity raises DNAAF11's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without LINC02015 | 0.035 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[ST8SIA6-AS1]] | B | ST8SIA6-AS1 activity raises DNAAF11's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without ST8SIA6-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[ADAM28]] | B | ADAM28 activity raises DNAAF11's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without ADAM28 | 0.095 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[MAP2K1]] | B | MAP2K1 activity lowers DNAAF11's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A15]] | B | DNAAF11 activity lowers SLC25A15's level | lines that do not express DNAAF11 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without DNAAF11 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SPEF2]] | B | DNAAF11 activity raises SPEF2's level | lines that do not express DNAAF11 (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without DNAAF11 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, 47.0); signed map (54.5, 20.5). **Vector** length 73.7, 14.2% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.2 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.9 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:132,570,416-132,675,592 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSLRP, LRTP, CILD19, tilB; previously LRRC6 |
| Gene groups (HGNC) | Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X45](https://www.uniprot.org/uniprotkb/Q86X45) (Dynein axonemal assembly factor 11):

> Involved in dynein arm assembly, is important for expression and transporting outer dynein arm (ODA) proteins from the cytoplasm to the cilia. Acts as a crucial component in the formation and motility of spermatozoal flagella.

**Summary**, from NCBI Gene [23639](https://www.ncbi.nlm.nih.gov/gene/23639):

> The protein encoded by this gene contains several leucine-rich repeat domains and appears to be involved in the motility of cilia. Defects in this gene are a cause of primary ciliary dyskinesia-19 (CILD19). Alternative splicing of this gene results in multiple transcript variants. Related pseudogenes have been identified on chromosomes 4, 11 and 22. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:16725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16725) · Entrez [23639](https://www.ncbi.nlm.nih.gov/gene/23639) · UniProt [Q86X45](https://www.uniprot.org/uniprotkb/Q86X45) · Ensembl [ENSG00000129295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129295)

## Data

Gene col 4963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4963); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4963]; `tensor/DDL_lfc|DDL_z.npy` [4963]; `embed/gene_vectors.npy` [4963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4963 or target_col == 4963). Every well: [[DNAAF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
