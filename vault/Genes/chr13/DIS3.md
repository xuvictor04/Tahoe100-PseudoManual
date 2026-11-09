---
symbol: "DIS3"
type: "gene"
col: 1372
ensembl_id: "ENSG00000083520"
name: "DIS3 exosome endoribonuclease and 3'-5' exoribonuclease"
location: "13q21.33"
module: 41
arm: "+"
pooled_cpm: 123.75
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# DIS3

*DIS3 exosome endoribonuclease and 3'-5' exoribonuclease* — 13q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +17.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.692× (z -6.7, q 1e-08, down in 29 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.752× (z -5.2, q 5e-05, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTY2D1]] (+0.77, fdr 7e-06), [[SRP54]] (+0.73, fdr 7e-06), [[ACBD3]] (+0.73, fdr 7e-06); moves opposite to [[TULP4]] (-0.60, fdr 1e-05), [[LARP1]] (-0.58, fdr 1e-05), [[ATE1]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +17.3 | 0e+00 | 42/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +8.7 | 8e-16 | 39/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +8.1 | 1e-13 | 39/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +8.0 | 2e-13 | 38/48 (HT-29, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 2e-13 | 36/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +6.9 | 4e-10 | 42/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +5.1 | 3e-05 | 26/49 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.090 | 22/48 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.19× | +3.2 | 0.090 | 22/48 (MIA PaCa-2, A-427, …) | top dose only | composition shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.090 | 6/49 (SW 900, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -6.7 | 1e-08 | 29/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.726×** | -6.0 | 4e-07 | 28/49 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -5.2 | 5e-05 | 32/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.839× | -4.6 | 6e-04 | 22/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -4.5 | 7e-04 | 25/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.781×** | -4.5 | 7e-04 | 31/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.793×** | -4.4 | 1e-03 | 29/48 (J82, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.803×** | -4.0 | 0.005 | 25/48 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.804×** | -3.8 | 0.009 | 23/45 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.833× | -3.4 | 0.034 | 21/47 (RKO, A498, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.837× | -3.4 | 0.039 | 19/49 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.039 | 19/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.879× | -3.3 | 0.044 | 7/48 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.060 | 15/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.063 | 17/49 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.063 | 17/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.063 | 17/49 (SW480, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 106 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 166 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.2) | [[Auranofin (drug)]] 5 µM 0.500× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 84.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +18.1) | — |
| [[NCI-H460 (line)]] | wt | 73.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 168 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.6) | [[Lonafarnib (drug)]] 5 µM 0.107× (z -14.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 206 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 193 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -13.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 122 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 93.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -19.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +9.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C32 (line)]] | wt | 83.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 103 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.6) | — |
| [[hTERT-HPNE (line)]] | wt | 142 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 162 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 143 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.5) | — |
| [[RKO (line)]] | wt | 159 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 151 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.6) | [[Lonafarnib (drug)]] 5 µM 0.172× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 76.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.7) | — |
| [[A549 (line)]] | wt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 97.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 302 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 82.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.2) | — |
| [[J82 (line)]] | alt | 190 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 71.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +18.8) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.547× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 89.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -19.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 90.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.216× (z -8.5) |
| [[SW 900 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.8) | — |
| [[SW48 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 267 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTY2D1]] | +0.77 | +0.86 / +0.66 | both halves | 7e-06 |  |
| [[SRP54]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[COG6]] | +0.71 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 | pathway: Unfolded Protein Response (UPR) |
| [[ARF4]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.69 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[PGM3]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.69 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[RARS1]] | +0.68 | +0.74 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP4]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[LARP1]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ATE1]] | -0.57 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[MGST1]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DIS3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GLRX]] | B | GLRX activity raises DIS3's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without GLRX | 0.085 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.1, -35.0); signed map (-50.3, 12.8). **Vector** length 124, 40.1% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.52 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.57 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.5 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.1 | +8.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.9 | +5.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -0.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.6 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | DIS3 exosome endoribonuclease and 3'-5' exoribonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.33 — chr13:72,752,169-72,782,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dis3p, RRP44, EXOSC11; previously KIAA1008 |
| Gene groups (HGNC) | Exosome complex; Endoribonucleases; PIN-like domain superfamily |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2L1](https://www.uniprot.org/uniprotkb/Q9Y2L1) (Exosome complex exonuclease RRP44):

> Putative catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with …

**Summary**, from NCBI Gene [22894](https://www.ncbi.nlm.nih.gov/gene/22894):

> Enables 3'-5'-RNA exonuclease activity; endonuclease activity; and guanyl-nucleotide exchange factor activity. Involved in CUT catabolic process; RNA processing; and rRNA catabolic process. Located in cytosol and nucleoplasm. Part of nuclear exosome (RNase complex). Implicated in primary ovarian insufficiency. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20604) · Entrez [22894](https://www.ncbi.nlm.nih.gov/gene/22894) · UniProt [Q9Y2L1](https://www.uniprot.org/uniprotkb/Q9Y2L1) · Ensembl [ENSG00000083520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083520)

## Data

Gene col 1372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1372); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1372]; `tensor/DDL_lfc|DDL_z.npy` [1372]; `embed/gene_vectors.npy` [1372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1372 or target_col == 1372). Every well: [[DIS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
