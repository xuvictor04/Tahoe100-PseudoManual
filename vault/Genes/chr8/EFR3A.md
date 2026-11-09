---
symbol: "EFR3A"
type: "gene"
col: 5293
ensembl_id: "ENSG00000132294"
name: "EFR3 homolog A"
location: "8q24.22"
module: 216
arm: "+"
pooled_cpm: 112.66
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# EFR3A

*EFR3 homolog A* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +8.4, q 3e-14, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.544× (z -17.7, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFK]] (+0.67, fdr 8e-06), [[PTAR1]] (+0.65, fdr 7e-06), [[IDH3A]] (+0.61, fdr 8e-06); moves opposite to [[IGBP1]] (-0.65, fdr 1e-05), [[NOXRED1]] (-0.62, fdr 4e-05), [[MED26]] (-0.62, fdr 1e-05).
> It is in [[Module 216]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +8.4 | 3e-14 | 36/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.2 | 2e-10 | 30/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 2e-05 | 28/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 3e-04 | 28/49 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.002 | 27/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 27/49 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.005 | 24/48 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.011 | 20/48 (AsPC-1, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.017 | 19/49 (HCT15, SNU-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.024 | 20/48 (J82, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.033 | 23/48 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.048 | 21/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.059 | 16/48 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -17.7 | 0e+00 | 42/49 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -11.0 | 7e-26 | 46/49 (RKO, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -7.9 | 6e-13 | 2/50 (HCT15, CHP-212) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -7.3 | 4e-11 | 35/47 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -6.5 | 9e-09 | 33/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -6.0 | 2e-07 | 32/50 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.785×** | -5.0 | 6e-05 | 27/48 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -4.9 | 8e-05 | 27/48 (Panc 03.27, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.722×** | -4.2 | 0.002 | 32/48 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.837× | -3.7 | 0.015 | 22/48 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.843× | -3.5 | 0.024 | 20/48 (CHP-212, SNU-1, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | 0.846× | -3.4 | 0.029 | 21/48 (HS-578T, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.889× | -3.4 | 0.030 | 4/48 (NCI-H2030, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.851× | -3.3 | 0.038 | 18/48 (KATO III, MIA PaCa-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.738×** | -3.3 | 0.039 | 18/45 (MIA PaCa-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.837× | -3.2 | 0.039 | 15/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.039 | 16/48 (SW1417, H4, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.900× | -3.0 | 0.071 | 7/49 (RPMI-7951, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 108 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 98.6 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.21× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.3) |
| [[C32 (line)]] | wt | 131 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -16.3) |
| [[A498 (line)]] | wt | 161 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -18.2) |
| [[HT-29 (line)]] | alt | 274 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -13.0) |
| [[LS 180 (line)]] | wt | 99.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -15.1) |
| [[PANC-1 (line)]] | alt | 145 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.8) |
| [[RKO (line)]] | wt | 162 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0924× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 96.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.54× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -12.2) |
| [[Hs 766T (line)]] | wt | 94.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[TAK-901 (drug)]] 5 µM 0.202× (z -9.3) |
| [[HS-578T (line)]] | alt | 160 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.2) |
| [[KATO III (line)]] | alt | 91.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 226 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.8) |
| [[SW 900 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.3) |
| [[SW1417 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -13.3) |
| [[SW480 (line)]] | alt | 66.8 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.57× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.6) |
| [[A-172 (line)]] | wt | 78.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -13.4) |
| [[A-427 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -20.3) |
| [[AsPC-1 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 139 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -16.8) |
| [[COLO 205 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 77.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.9) |
| [[J82 (line)]] | alt | 85.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.2) |
| [[LoVo (line)]] | wt | 96.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 91.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 48.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.8) |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.117× (z -10.9) |
| [[SHP-77 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -11.5) |
| [[SNU-1 (line)]] | wt | 82.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 82.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.7) |
| [[SW 1271 (line)]] | alt | 91.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.112× (z -10.0) |
| [[AN3 CA (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFK]] | +0.67 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[PTAR1]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[IDH3A]] | +0.61 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[PANK3]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[OCRL]] | +0.59 | +0.36 / +0.67 | both halves | 1e-04 |  |
| [[MRPL42]] | +0.56 | +0.31 / +0.65 | both halves | 2e-04 |  |
| [[AKAP11]] | +0.55 | +0.40 / +0.67 | both halves | 4e-05 |  |
| [[GMFB]] | +0.55 | +0.26 / +0.70 | both halves | 3e-04 |  |
| [[TBC1D1]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NHLRC2]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[TMEM106B]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SSX2IP]] | +0.54 | +0.29 / +0.70 | both halves | 3e-04 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGBP1]] | -0.65 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[NOXRED1]] | -0.62 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[MED26]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[ZNF668]] | -0.61 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.61 | -0.40 / -0.74 | both halves | 5e-05 |  |
| [[SPACDR]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[LZTS2]] | -0.60 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[ISY1]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[MARK4]] | -0.58 | -0.34 / -0.76 | both halves | 1e-04 |  |
| [[DEDD2]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RECQL5]] | -0.58 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[RABGEF1]] | -0.58 | -0.39 / -0.65 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EFR3A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.0, -12.4); signed map (-11.6, -39.5). **Vector** length 130, 39.1% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.6 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.5 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.5 | -17.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -9.9 | -11.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.6 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | EFR3 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:131,904,093-132,013,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0143 |
| Gene groups (HGNC) | Armadillo like helical domain containing; EFR3 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14156](https://www.uniprot.org/uniprotkb/Q14156) (Protein EFR3 homolog A):

> Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane. The complex acts as a regulator of phosphatidylinositol 4-phosphate (PtdIns(4)P) synthesis (Probable). In the complex, EFR3A probably acts as the membrane-anchoring component. Also involved in responsiveness to G protein-coupled receptors; it is however unclear whether this role is direct or indirect.

**Summary**, from NCBI Gene [23167](https://www.ncbi.nlm.nih.gov/gene/23167):

> The protein encoded by this gene is part of a complex that plays a role in maintaining an active pool of phosphatidylinositol 4-kinase (PI4K) at the plasma membrane. This protein is thought to be a peripheral membrane protein that associates with the plasma membrane through palmitoylation. Studies indicate that this gene product plays a role in controlling G protein-coupled receptor (GPCR) activity by affecting receptor phosphorylation. Whole exome sequencing studies have implicated mutations …

**Accessions** — [HGNC:28970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28970) · Entrez [23167](https://www.ncbi.nlm.nih.gov/gene/23167) · UniProt [Q14156](https://www.uniprot.org/uniprotkb/Q14156) · Ensembl [ENSG00000132294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132294)

## Data

Gene col 5293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5293); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5293]; `tensor/DDL_lfc|DDL_z.npy` [5293]; `embed/gene_vectors.npy` [5293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5293 or target_col == 5293). Every well: [[EFR3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFR3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
