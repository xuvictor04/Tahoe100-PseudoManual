---
symbol: "GNE"
type: "gene"
col: 8288
ensembl_id: "ENSG00000159921"
name: "glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase"
location: "9p13.3"
module: 40
arm: "+"
pooled_cpm: 45.68
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# GNE

*glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.29× (z +5.0, q 3e-04, up in 22 of 44 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Berbamine (dihydrochloride) (drug)]] 5 µM: 1.24× (z +4.2, q 0.005, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -19.3, q 0e+00, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM53]] (+0.53, fdr 3e-05), [[CCDC127]] (+0.52, fdr 4e-05), [[FBXL12]] (+0.51, fdr 1e-05); moves opposite to [[SLC26A2]] (-0.45, fdr 8e-05), [[LEPROT]] (-0.45, fdr 7e-05), [[SEPTIN11]] (-0.43, fdr 6e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PAK2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +5.0 | 3e-04 | 22/44 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.005 | 13/45 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.005 | 19/44 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.13× | +3.7 | 0.026 | 16/45 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.040 | 10/45 (COLO 205, HT-29, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.17× | +3.4 | 0.069 | 15/45 (BT-474, HCT15, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.097 | 7/45 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.11× | +3.2 | 0.11 | 9/46 (NCI-H23, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 22 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -19.3 | 0e+00 | 38/45 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.500×** | -14.5 | 3e-45 | 37/45 (HCT15, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.500×** | -14.5 | 3e-45 | 38/45 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.474×** | -14.5 | 3e-45 | 36/45 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.529×** | -13.3 | 2e-38 | 40/45 (PANC-1, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -12.7 | 3e-35 | 33/44 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.548×** | -12.6 | 3e-34 | 30/43 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.546×** | -11.7 | 7e-30 | 23/35 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.582×** | -11.3 | 9e-28 | 36/45 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.592×** | -10.1 | 2e-22 | 25/38 (A549, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -9.5 | 1e-19 | 31/45 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.644×** | -9.2 | 2e-18 | 30/45 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -8.8 | 4e-17 | 32/45 (PANC-1, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.749×** | -8.5 | 8e-16 | 25/45 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.655×** | -8.2 | 1e-14 | 32/45 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -7.1 | 4e-11 | 25/45 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -5.3 | 2e-06 | 23/45 (CFPAC-1, Panc 03.27, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.814×** | -4.0 | 0.001 | 15/45 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -3.5 | 0.011 | 16/45 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.855× | -3.2 | 0.023 | 6/44 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.029 | 11/45 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.749×** | -3.1 | 0.029 | 12/45 (SW1417, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.764×** | -2.9 | 0.055 | 10/45 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.859× | -2.9 | 0.056 | 12/44 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.861× | -2.9 | 0.068 | 10/44 (J82, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 95.0 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -23.5) |
| [[PANC-1 (line)]] | alt | 99.2 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.555× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 86.8 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.254× (z -11.0) |
| [[HOP62 (line)]] | alt | 52.3 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.0) |
| [[Hs 766T (line)]] | wt | 96.4 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0332× (z -31.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.318× (z -16.3) |
| [[H4 (line)]] | wt | 77.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 39.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.450× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -23.0) |
| [[NCI-H460 (line)]] | wt | 34.6 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.440× (z -8.9) |
| [[SW1417 (line)]] | alt | 58.6 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.0) |
| [[COLO 205 (line)]] | alt | 51.0 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -12.9) |
| [[A-172 (line)]] | wt | 52.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.6) |
| [[A549 (line)]] | wt | 61.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HS-578T (line)]] | alt | 43.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 59.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H23 (line)]] | alt | 72.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.467× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.471× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -9.3) |
| [[SW 900 (line)]] | alt | 48.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.3) |
| [[A498 (line)]] | wt | 79.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.603× (z -9.1) |
| [[AN3 CA (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.138× (z -9.2) |
| [[HCT15 (line)]] | alt | 60.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.129× (z -14.9) |
| [[J82 (line)]] | alt | 41.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.320× (z -11.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.9) |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.0) |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM53]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CCDC127]] | +0.52 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[FBXL12]] | +0.51 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[FBXO34]] | +0.50 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB3]] | +0.50 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[NPRL2]] | +0.49 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[KANSL3]] | +0.49 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[NCK1]] | +0.48 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[TMOD1]] | +0.47 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[TTI2]] | +0.47 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[RNASE4]] | +0.47 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[DRG1]] | +0.47 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A2]] | -0.45 | -0.43 / -0.37 | both halves | 8e-05 | pathway: Diseases of glycosylation |
| [[LEPROT]] | -0.45 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[SEPTIN11]] | -0.43 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[RAP2C-AS1]] | -0.43 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[FRG1-DT]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[OSTM1]] | -0.43 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[TBC1D5]] | -0.42 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[THBS1]] | -0.42 | -0.31 / -0.44 | both halves | 2e-04 | pathway: Diseases of glycosylation |
| [[SPCS3]] | -0.42 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[CDH2]] | -0.42 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[PARD3B]] | -0.41 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TWF1]] | -0.41 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GNE's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAK2]] | C | GNE activity raises PAK2's level | lines that do not express GNE (3) vs lines expressing it (47) | 1.41× lower at baseline in the lines without GNE | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF222, ATL3; its own permutation p |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.376). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-39.1, -13.5); signed map (-37.8, 3.9). **Vector** length 79.0, 17.5% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | +3.5 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +2.8 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -14.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.9 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -2.7 | -12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.5 | -10.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:36,214,441-36,277,042 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Uae1; previously IBM2 |
| Gene groups (HGNC) | Carbohydrate kinases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Diseases associated with glycosylation precursor biosynthesis; Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y223](https://www.uniprot.org/uniprotkb/Q9Y223) (Bifunctional UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase):

> Bifunctional enzyme that possesses both UDP-N-acetylglucosamine 2-epimerase and N-acetylmannosamine kinase activities, and serves as the initiator of the biosynthetic pathway leading to the production of N-acetylneuraminic acid (NeuAc), a critical precursor in the synthesis of sialic acids. By catalyzing this pivotal and rate-limiting step in sialic acid biosynthesis, this enzyme assumes a pivotal role in governing the regulation of cell surface sialylation, playing a role in embryonic …

**Summary**, from NCBI Gene [10020](https://www.ncbi.nlm.nih.gov/gene/10020):

> The protein encoded by this gene is a bifunctional enzyme that initiates and regulates the biosynthesis of N-acetylneuraminic acid (NeuAc), a precursor of sialic acids. It is a rate-limiting enzyme in the sialic acid biosynthetic pathway. Sialic acid modification of cell surface molecules is crucial for their function in many biologic processes, including cell adhesion and signal transduction. Differential sialylation of cell surface molecules is also implicated in the tumorigenicity and …

**Accessions** — [HGNC:23657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23657) · Entrez [10020](https://www.ncbi.nlm.nih.gov/gene/10020) · UniProt [Q9Y223](https://www.uniprot.org/uniprotkb/Q9Y223) · Ensembl [ENSG00000159921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159921)

## Data

Gene col 8288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8288); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8288]; `tensor/DDL_lfc|DDL_z.npy` [8288]; `embed/gene_vectors.npy` [8288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8288 or target_col == 8288). Every well: [[GNE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
