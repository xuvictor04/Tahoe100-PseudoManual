---
symbol: "ELP4"
type: "gene"
col: 3091
ensembl_id: "ENSG00000109911"
name: "elongator acetyltransferase complex subunit 4"
location: "11p13"
module: 213
arm: "+"
pooled_cpm: 107.17
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# ELP4

*elongator acetyltransferase complex subunit 4* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +9.5, q 8e-19, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.242× (z -15.6, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC17]] (+0.67, fdr 7e-06), [[METTL15]] (+0.58, fdr 3e-05), [[PDSS2]] (+0.55, fdr 4e-05); moves opposite to [[CACNB1]] (-0.51, fdr 3e-05), [[MAP6]] (-0.50, fdr 1e-04), [[ENTREP1]] (-0.49, fdr 1e-04).
> It is in [[Module 213]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +9.5 | 8e-19 | 42/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.6 | 8e-12 | 30/48 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +6.3 | 4e-08 | 33/48 (HT-29, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +5.7 | 2e-06 | 28/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.5 | 6e-04 | 19/48 (SW1417, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.005 | 23/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.11 | 15/48 (HOP62, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.242×** | -15.6 | 0e+00 | 49/49 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.257×** | -14.9 | 0e+00 | 41/48 (RPMI-7951, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.534×** | -12.2 | 8e-32 | 39/45 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -11.3 | 2e-27 | 39/49 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.594×** | -10.5 | 1e-23 | 31/43 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -9.6 | 1e-19 | 30/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.748×** | -5.9 | 4e-07 | 25/48 (A-427, A549, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.761×** | -5.7 | 7e-07 | 27/48 (CHP-212, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.653×** | -4.7 | 2e-04 | 21/38 (LOX-IMVI, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.818×** | -4.2 | 0.001 | 22/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -3.8 | 0.006 | 12/49 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.836× | -3.6 | 0.014 | 23/49 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.4 | 0.031 | 19/48 (C-33 A, SW48, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.852× | -3.3 | 0.031 | 15/47 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.853× | -3.3 | 0.031 | 15/48 (AN3 CA, AsPC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.848× | -3.3 | 0.031 | 13/48 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.904× | -3.0 | 0.085 | 10/48 (SW480, A-427, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 283 | 0 | 9 (7 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.110× (z -16.8) |
| [[SNU-423 (line)]] | alt | 129 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.131× (z -13.0) |
| [[SW480 (line)]] | alt | 215 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.180× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 6 (4 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0898× (z -16.1) |
| [[PANC-1 (line)]] | alt | 116 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.184× (z -13.6) |
| [[RKO (line)]] | wt | 100 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.141× (z -11.1) |
| [[A549 (line)]] | wt | 83.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.205× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 82.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.147× (z -12.6) |
| [[J82 (line)]] | alt | 123 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.242× (z -9.4) |
| [[LoVo (line)]] | wt | 101 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.279× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0816× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 72.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.241× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 129 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -13.3) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.150× (z -11.5) |
| [[SW1417 (line)]] | alt | 121 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.84× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.215× (z -8.6) |
| [[HCT15 (line)]] | alt | 174 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 116 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.128× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.181× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 78.7 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.466× (z -9.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.254× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 87.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.111× (z -12.3) |
| [[SW48 (line)]] | wt | 99.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0722× (z -10.5) |
| [[H4 (line)]] | wt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.181× (z -12.6) |
| [[Hs 766T (line)]] | wt | 98.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.202× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 91.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.382× (z -10.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.205× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 84.7 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0333× (z -16.7) |
| [[SHP-77 (line)]] | alt | 97.3 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.151× (z -10.6) |
| [[A-172 (line)]] | wt | 70.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[A498 (line)]] | wt | 97.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 123 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0713× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 74.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 53.2 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0649× (z -12.9) |
| [[COLO 205 (line)]] | alt | 102 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0886× (z -13.5) |
| [[HT-29 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -16.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 110 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.134× (z -11.9) |
| [[SNU-1 (line)]] | wt | 57.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC17]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[METTL15]] | +0.58 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[PDSS2]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[RAB28]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[IFT43]] | +0.53 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PRH1]] | +0.52 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[FAM120B]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GIGYF2]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[UMAD1]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[LINC01572]] | +0.49 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TAS2R14]] | +0.49 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[LIN52]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNB1]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MAP6]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ENTREP1]] | -0.49 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[OTULINL]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SNPH]] | -0.47 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[TP53BP2]] | -0.46 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[RNF2]] | -0.46 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[SNX18]] | -0.46 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PGBD2]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[BRSK2]] | -0.45 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[C15orf39]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[QDPR]] | -0.44 | -0.40 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ELP4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CENPP]] | C | CENPP activity raises ELP4's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without CENPP | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-24.3, 28.6); signed map (-20.2, 1.7). **Vector** length 106, 32.1% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +8.2 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.3 | +3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | -0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +5.6 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.5 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.4 | -0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.3 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.5 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.1 | -15.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.1 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.9 | -12.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.8 | -14.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.3 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | +2.4 |

## What is on record

|  |  |
|---|---|
| Name | elongator acetyltransferase complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:31,509,755-31,790,324 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAXNEB; previously C11orf19 |
| Gene groups (HGNC) | Elongator acetyltransferase complex |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EB1](https://www.uniprot.org/uniprotkb/Q96EB1) (Elongator complex protein 4):

> Component of the elongator complex which is required for multiple tRNA modifications, including mcm5U (5-methoxycarbonylmethyl uridine), mcm5s2U (5-methoxycarbonylmethyl-2-thiouridine), and ncm5U (5-carbamoylmethyl uridine). The elongator complex catalyzes the formation of carboxymethyluridine in the wobble base at position 34 in tRNAs.

**Summary**, from NCBI Gene [26610](https://www.ncbi.nlm.nih.gov/gene/26610):

> This gene encodes a component of the six subunit elongator complex, a histone acetyltransferase complex that associates directly with RNA polymerase II during transcriptional elongation. The human gene can partially complement sensitivity phenotypes of yeast ELP4 deletion mutants. This gene has also been associated with Rolandic epilepsy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:1171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1171) · Entrez [26610](https://www.ncbi.nlm.nih.gov/gene/26610) · UniProt [Q96EB1](https://www.uniprot.org/uniprotkb/Q96EB1) · Ensembl [ENSG00000109911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109911)

## Data

Gene col 3091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3091); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3091]; `tensor/DDL_lfc|DDL_z.npy` [3091]; `embed/gene_vectors.npy` [3091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3091 or target_col == 3091). Every well: [[ELP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
