---
symbol: "NINL"
type: "gene"
col: 2059
ensembl_id: "ENSG00000101004"
name: "ninein like"
location: "20p11.21"
module: 203
arm: "+"
pooled_cpm: 53.18
n_lines_expressing: 40
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# NINL

*ninein like* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.8, q 4e-06, up in 20 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -12.5, q 3e-33, down in 32 of 38 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.244× (z -11.0, q 9e-26, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRFN4]] (+0.58, fdr 5e-05), [[GPR161]] (+0.56, fdr 1e-04), [[PTPN9]] (+0.56, fdr 4e-05); moves opposite to [[ALAD]] (-0.56, fdr 1e-04), [[SKIC3]] (-0.51, fdr 1e-04), [[MPP1]] (-0.50, fdr 1e-04).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 2 go from it, the strongest it → [[LIMCH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.8 | 4e-06 | 20/38 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.7 | 9e-04 | 16/38 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.004 | 17/38 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +3.9 | 0.016 | 17/38 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.030 | 16/37 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.26×** | +3.3 | 0.097 | 14/38 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.24× | +3.2 | 0.11 | 14/38 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.1 | 0.12 | 0/38 | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.33× | +3.0 | 0.16 | 6/38 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.551×** | -12.5 | 3e-33 | 32/38 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.440×** | -11.7 | 2e-29 | 30/38 (PANC-1, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.244×** | -11.0 | 9e-26 | 37/39 (HOP62, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.498×** | -9.6 | 1e-19 | 28/36 (SHP-77, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.549×** | -8.6 | 1e-15 | 22/34 (SHP-77, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.563×** | -8.6 | 1e-15 | 30/38 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.565×** | -8.5 | 2e-15 | 28/38 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.605×** | -7.2 | 5e-11 | 25/37 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.622×** | -7.1 | 1e-10 | 24/38 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.626×** | -7.0 | 2e-10 | 24/38 (NCI-H23, SHP-77, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.630×** | -6.9 | 3e-10 | 28/37 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -6.5 | 3e-09 | 28/38 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.680×** | -5.7 | 4e-07 | 28/38 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.737×** | -4.5 | 2e-04 | 21/38 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.745×** | -4.4 | 5e-04 | 22/38 (AN3 CA, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.612×** | -3.8 | 0.004 | 18/38 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -3.8 | 0.004 | 19/38 (AN3 CA, SHP-77, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.019 | 19/38 (HOP62, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -3.2 | 0.035 | 12/38 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.823×** | -2.9 | 0.083 | 13/38 (SW480, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.814×** | -2.9 | 0.083 | 10/38 (RKO, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 92.3 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.126× (z -11.4) |
| [[A549 (line)]] | wt | 146 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -21.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.111× (z -11.2) |
| [[PANC-1 (line)]] | alt | 121 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -24.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.204× (z -10.8) |
| [[HOP62 (line)]] | alt | 111 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.242× (z -14.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0890× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 76.1 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -14.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.146× (z -9.3) |
| [[SHP-77 (line)]] | alt | 216 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0407× (z -37.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.470× (z -9.1) |
| [[A-172 (line)]] | wt | 90.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -24.1) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.161× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 76.9 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.139× (z -8.7) |
| [[SNU-423 (line)]] | alt | 83.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -18.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.131× (z -8.8) |
| [[A-427 (line)]] | wt | 66.9 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -14.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 154 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.217× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 235 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.439× (z -9.3) |
| [[RKO (line)]] | wt | 60.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.0) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.116× (z -10.0) |
| [[SW480 (line)]] | alt | 46.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.161× (z -10.3) |
| [[A498 (line)]] | wt | 50.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[C-33 A (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.164× (z -10.6) |
| [[SW 1271 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0886× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~90% of this change |
| [[BT-474 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.8) ⚠ cell-cycle shift, explains ~63% of this change |
| [[CFPAC-1 (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -19.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[KATO III (line)]] | alt | 63.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -11.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H661 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0700× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~90% of this change |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.52 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRFN4]] | +0.58 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[GPR161]] | +0.56 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[PTPN9]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[WNT3]] | +0.56 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[ZNF600]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[C12orf56]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[NR2C2]] | +0.54 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[TTC28]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DNMT3A]] | +0.53 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[TRIM65]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[LMO7-AS1]] | +0.53 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[CHMP1B2P]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.56 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.51 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[MPP1]] | -0.50 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[IFT172]] | -0.49 | -0.37 / -0.34 | both halves | 1e-04 | pathway: Assembly of the 9+0 primary cilium |
| [[LONP2]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SAR1B]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TJP3]] | -0.48 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[UFSP2]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[SORL1]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SLC35A3]] | -0.48 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TTC23]] | -0.48 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[MDH1]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises NINL's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without ELFN1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[EBF4]] | B | EBF4 activity raises NINL's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 3.32× lower at baseline in the lines without EBF4 | 0.064 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[LIMCH1]] | B | LIMCH1 activity lowers NINL's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.93× higher at baseline in the lines without LIMCH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[ELFN1]] | B | ELFN1 activity strengthens NINL's drug response | lines that do not express ELFN1 (17) vs lines expressing it (22) | the lines without ELFN1 respond 0.63× as strongly (z diff +2.71); strongest at Dinaciclib 0.5 µM: 0.80x vs 0.43x (z diff +4.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; target measured in part of the lines; artifact flags |
| [[ULK2]] | B | ULK2 activity raises NINL's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.14× lower at baseline in the lines without ULK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIMCH1]] | B | NINL activity lowers LIMCH1's level | lines that do not express NINL (10) vs lines expressing it (40) | 2.30× higher at baseline in the lines without NINL | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZIM2-AS1 |
| [[JADE3]] | B | NINL activity raises JADE3's level | lines that do not express NINL (10) vs lines expressing it (40) | 1.03× lower at baseline in the lines without NINL | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZIM2-AS1 |

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.0, 17.9); signed map (2.5, 9.9). **Vector** length 91.2, 23.9% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +4.1 | -8.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -11.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | -8.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -2.7 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.2 | -7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ninein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,451,594-25,585,531 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0980, NLP |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2I6](https://www.uniprot.org/uniprotkb/Q9Y2I6) (Ninein-like protein):

> Involved in the microtubule organization in interphase cells. Overexpression induces the fragmentation of the Golgi, and causes lysosomes to disperse toward the cell periphery; it also interferes with mitotic spindle assembly. Involved in vesicle transport in photoreceptor cells (By similarity). May play a role in ovarian carcinogenesis.

**Summary**, from NCBI Gene [22981](https://www.ncbi.nlm.nih.gov/gene/22981):

> Predicted to enable calcium ion binding activity. Predicted to be involved in microtubule anchoring at centrosome. Located in centrosome and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29163) · Entrez [22981](https://www.ncbi.nlm.nih.gov/gene/22981) · UniProt [Q9Y2I6](https://www.uniprot.org/uniprotkb/Q9Y2I6) · Ensembl [ENSG00000101004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101004)

## Data

Gene col 2059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2059); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2059]; `tensor/DDL_lfc|DDL_z.npy` [2059]; `embed/gene_vectors.npy` [2059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2059 or target_col == 2059). Every well: [[NINL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NINL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
