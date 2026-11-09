---
symbol: "MCC"
type: "gene"
col: 10108
ensembl_id: "ENSG00000171444"
name: "MCC regulator of Wnt signaling pathway"
location: "5q22.2"
module: 9
arm: "+"
pooled_cpm: 52.26
n_lines_expressing: 36
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MCC

*MCC regulator of Wnt signaling pathway* — 5q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.99× (z +15.8, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.607× (z -8.2, q 9e-14, down in 24 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.684× (z -6.3, q 8e-08, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMD]] (+0.57, fdr 1e-05), [[PURPL]] (+0.52, fdr 3e-05), [[MAPK10]] (+0.51, fdr 1e-05); moves opposite to [[MIGA2]] (-0.44, fdr 3e-04), [[EFCAB11]] (-0.43, fdr 9e-05), [[RAB40B]] (-0.43, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FRMPD4]] → it (grade B ⚠); 3 go from it, the strongest it → [[KCNMB2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +15.8 | 0e+00 | 31/34 (CFPAC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +13.0 | 6e-36 | 25/34 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +11.8 | 1e-29 | 27/33 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +10.5 | 1e-23 | 24/34 (A-172, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +9.2 | 5e-18 | 18/33 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +9.1 | 1e-17 | 22/34 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +9.0 | 3e-17 | 23/34 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +6.9 | 5e-10 | 24/33 (LoVo, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +6.7 | 1e-09 | 20/34 (A-172, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.47×** | +6.3 | 2e-08 | 22/34 (SK-MEL-2, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +5.9 | 2e-07 | 15/33 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +5.8 | 3e-07 | 19/36 (LoVo, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +5.6 | 9e-07 | 13/33 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.5 | 1e-06 | 20/33 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.37×** | +5.1 | 1e-05 | 15/34 (CFPAC-1, A-427, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +5.1 | 1e-05 | 14/35 (HOP62, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.014 | 12/34 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.043 | 12/33 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.047 | 11/34 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.054 | 8/34 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.054 | 13/36 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.0 | 0.062 | 12/34 (LS 180, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.607×** | -8.2 | 9e-14 | 24/33 (LoVo, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -6.3 | 8e-08 | 24/33 (SW480, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.757×** | -4.6 | 6e-04 | 19/33 (AN3 CA, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -4.6 | 6e-04 | 17/32 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -4.4 | 0.001 | 14/35 (SNU-1, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.789×** | -3.9 | 0.008 | 13/34 (C-33 A, NCI-H2030, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.800×** | -3.7 | 0.016 | 9/33 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.021 | 13/33 (CHP-212, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.812×** | -3.5 | 0.030 | 16/34 (SHP-77, LoVo, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **0.812×** | -3.5 | 0.030 | 12/33 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 81.6 | 4 (2 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.324× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -9.2) |
| [[HOP62 (line)]] | alt | 23.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +15.1) | — |
| [[SK-MEL-2 (line)]] | alt | 93.0 | 6 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.72× (z +11.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.34× (z +9.7) | — |
| [[A-427 (line)]] | wt | 21.4 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.22× (z +10.4) | [[AZD2858 (drug)]] 0.5 µM 0.0748× (z -11.8) ⚠ toxic |
| [[C32 (line)]] | wt | 114 | 3 | 0 | [[Ponatinib (drug)]] 5 µM 3.62× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +14.6) | — |
| [[J82 (line)]] | alt | 65.3 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.45× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 42.0 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 213 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.7) |
| [[A-172 (line)]] | wt | 37.6 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.17× (z +11.4) | — |
| [[A498 (line)]] | wt | 122 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.94× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 2 (1 ⚠) | — | [[Bimatoprost (drug)]] 0.5 µM 0.0661× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 57.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 62.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0564× (z -9.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 52.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.90× (z +10.3) | — |
| [[SW480 (line)]] | alt | 183 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.350× (z -10.0) |
| [[A549 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.66 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMD]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PURPL]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[MAPK10]] | +0.51 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[EGFEM1P]] | +0.51 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ADAMTS19]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CASC15]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[CCN3]] | +0.50 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[PDZRN3]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[LINC00882]] | +0.49 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[DSEL]] | +0.49 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[ARHGAP10]] | +0.49 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[ROBO1]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIGA2]] | -0.44 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[EFCAB11]] | -0.43 | -0.37 / -0.45 | both halves | 9e-05 | same gene group |
| [[RAB40B]] | -0.43 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[NUP88]] | -0.42 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ORC3]] | -0.42 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[FN3KRP]] | -0.42 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.42 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[FARP2]] | -0.41 | -0.30 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMPD4]] | B | FRMPD4 activity raises MCC's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.88× lower at baseline in the lines without FRMPD4 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[TOP2A]] | B | TOP2A activity lowers MCC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNMB2-AS1]] | B | KCNMB2-AS1 activity raises MCC's level | lines that do not express KCNMB2-AS1 (14) vs lines expressing it (36) | 2.29× lower at baseline in the lines without KCNMB2-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: FIRRE, STXBP6, LINC01980; maybe low, not absent |
| [[RORB]] | B | RORB activity raises MCC's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without RORB | 0.077 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent |
| [[LINC01151]] | B | LINC01151 activity raises MCC's level | lines that do not express LINC01151 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without LINC01151 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, DNER, ENSG00000225330; maybe low, not absent |
| [[CPA4]] | B | CPA4 activity raises MCC's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without CPA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MCC's level | compounds that target MAP2K1: 3 of 4 raise it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[EGFEM1P]] | C | EGFEM1P activity raises MCC's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without EGFEM1P | 0.052 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2-AS1]] | B | MCC activity raises KCNMB2-AS1's level | lines that do not express MCC (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without MCC | 0.045 | ⚠ within organs, on part of the lines; also absent: CAMK4, EGFEM1P, DYNC1I1 |
| [[ORC3]] | B | MCC activity lowers ORC3's level | lines that do not express MCC (14) vs lines expressing it (36) | 1.18× higher at baseline in the lines without MCC | 0.067 | ⚠ within organs, on part of the lines; also absent: CAMK4, EGFEM1P, DYNC1I1 |
| [[FAM13C]] | B | MCC activity raises FAM13C's level | lines that do not express MCC (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without MCC | 0.076 | ⚠ within organs, on part of the lines; also absent: CAMK4, EGFEM1P, DYNC1I1 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 31.1); signed map (41.2, 31.2). **Vector** length 94.6, 23.7% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.9 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.2 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.8 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.6 | +5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.1 | -4.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MCC regulator of Wnt signaling pathway |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.2 — chr5:113,022,106-113,488,823 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P23508](https://www.uniprot.org/uniprotkb/P23508) (Colorectal mutant cancer protein):

> Candidate for the putative colorectal tumor suppressor gene located at 5q21. Suppresses cell proliferation and the Wnt/b-catenin pathway in colorectal cancer cells. Inhibits DNA binding of b-catenin/TCF/LEF transcription factors. Involved in cell migration independently of RAC1, CDC42 and p21-activated kinase (PAK) activation. Represses the beta-catenin pathway (canonical Wnt signaling pathway) in a CCAR2-dependent manner by sequestering CCAR2 to the cytoplasm, thereby impairing its ability to …

**Summary**, from NCBI Gene [4163](https://www.ncbi.nlm.nih.gov/gene/4163):

> This gene is a candidate colorectal tumor suppressor gene that is thought to negatively regulate cell cycle progression. The orthologous gene in the mouse expresses a phosphoprotein associated with the plasma membrane and membrane organelles, and overexpression of the mouse protein inhibits entry into S phase. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6935) · Entrez [4163](https://www.ncbi.nlm.nih.gov/gene/4163) · UniProt [P23508](https://www.uniprot.org/uniprotkb/P23508) · Ensembl [ENSG00000171444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171444)

## Data

Gene col 10108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10108); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10108]; `tensor/DDL_lfc|DDL_z.npy` [10108]; `embed/gene_vectors.npy` [10108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10108 or target_col == 10108). Every well: [[MCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
