---
symbol: "MIA2"
type: "gene"
col: 7441
ensembl_id: "ENSG00000150527"
name: "MIA SH3 domain ER export factor 2"
location: "14q13.2"
module: 133
arm: "+"
pooled_cpm: 94.33
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# MIA2

*MIA SH3 domain ER export factor 2* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.37× (z +8.4, q 3e-14, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Dihydroartemisinin (drug)]] 5 µM: 1.40× (z +7.0, q 6e-10, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.431× (z -17.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMGDH]] (+0.68, fdr 1e-05), [[AARS1]] (+0.68, fdr 7e-06), [[EIF2S2]] (+0.68, fdr 7e-06); moves opposite to [[CD59]] (-0.60, fdr 1e-05), [[RUNX1]] (-0.51, fdr 3e-05), [[FRMD6]] (-0.48, fdr 3e-05).
> It is in [[Module 133]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +8.4 | 3e-14 | 37/48 (BT-474, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.40×** | +7.0 | 6e-10 | 36/47 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.35×** | +6.3 | 7e-08 | 29/48 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.7 | 1e-06 | 32/48 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.2 | 2e-05 | 28/47 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.28×** | +4.9 | 1e-04 | 26/48 (COLO 205, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 6e-04 | 23/48 (BT-474, SNU-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.005 | 18/48 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.21×** | +3.9 | 0.006 | 22/48 (HCT15, A-427, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.027 | 15/49 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.4 | 0.030 | 22/48 (BT-474, LoVo, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.083 | 11/50 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.431×** | -17.6 | 0e+00 | 46/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.493×** | -14.7 | 0e+00 | 46/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.608×** | -10.4 | 6e-23 | 40/48 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.628×** | -9.7 | 5e-20 | 35/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.634×** | -9.5 | 2e-19 | 34/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.710×** | -7.2 | 8e-11 | 30/48 (A498, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.719×** | -6.4 | 2e-08 | 31/47 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.730×** | -6.3 | 2e-08 | 27/43 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.739×** | -6.3 | 2e-08 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -6.3 | 2e-08 | 30/47 (NCI-H2030, A-427, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.776×** | -5.3 | 6e-06 | 26/48 (SW 900, NCI-H1573, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.779×** | -5.2 | 9e-06 | 26/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.770×** | -5.0 | 2e-05 | 23/45 (RKO, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.787×** | -5.0 | 2e-05 | 22/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.791×** | -4.9 | 4e-05 | 24/48 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.002 | 20/47 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.8 | 0.004 | 17/48 (HT-29, HS-578T, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.864× | -3.0 | 0.059 | 13/49 (KATO III, Hs 766T, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.818×** | -3.0 | 0.076 | 12/48 (SW 1271, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.869× | -2.9 | 0.080 | 9/49 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.894× | -2.9 | 0.084 | 11/48 (CHP-212, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.8 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -11.9) |
| [[SW480 (line)]] | alt | 96.7 | 1 (1 ⚠) | 8 (7 ⚠) | [[Artesunate (drug)]] 5 µM 1.70× (z +10.2) ⚠ cell-cycle shift, explains ~22% of this change | [[Belinostat (drug)]] 5 µM 0.270× (z -19.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -16.8) |
| [[A-427 (line)]] | wt | 140 | 1 (1 ⚠) | 6 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.17× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -16.2) |
| [[SW 900 (line)]] | alt | 127 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -13.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -11.8) |
| [[KATO III (line)]] | alt | 157 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 100 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.393× (z -11.5) |
| [[PANC-1 (line)]] | alt | 81.4 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -15.1) |
| [[HT-29 (line)]] | alt | 144 | 1 (1 ⚠) | 4 (3 ⚠) | [[Artesunate (drug)]] 5 µM 1.83× (z +9.1) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 5 µM 0.215× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 225 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -10.4) |
| [[SW48 (line)]] | wt | 143 | 2 (1 ⚠) | 3 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.48× (z +9.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Artesunate (drug)]] 0.5 µM 2.93× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.222× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.1) |
| [[A498 (line)]] | wt | 88.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 4 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.354× (z -10.9) |
| [[COLO 205 (line)]] | alt | 157 | 1 (1 ⚠) | 3 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.34× (z +9.2) ⚠ cell-cycle shift, explains ~54% of this change | [[Panobinostat (drug)]] 5 µM 0.303× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -12.7) |
| [[RKO (line)]] | wt | 78.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -10.6) |
| [[HS-578T (line)]] | alt | 65.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.394× (z -9.8) |
| [[LoVo (line)]] | wt | 147 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -13.7) |
| [[A549 (line)]] | wt | 83.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -12.1) |
| [[BT-474 (line)]] | alt | 42.8 | 2 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 3.39× (z +11.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Dihydroartemisinin (drug)]] 0.5 µM 3.54× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 45.2 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.73× (z +9.8) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.9) |
| [[J82 (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.441× (z -8.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[MIA PaCa-2 (line)]] | alt | 61.8 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.47× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 99.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SNU-1 (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.29× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 96.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0763× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.0799× (z -10.8) |
| [[C-33 A (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[H4 (line)]] | wt | 76.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.474× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 64.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.319× (z -8.9) |
| [[LS 180 (line)]] | wt | 147 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.2) |
| [[NCI-H596 (line)]] | alt | 90.7 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.132× (z -8.8) |
| [[SNU-423 (line)]] | alt | 50.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -9.0) |
| [[A-172 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 165 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMGDH]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[AARS1]] | +0.68 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[EIF2S2]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[XPOT]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[YARS1]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SLC6A9]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MARS1]] | +0.65 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[TARS1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PCK2]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TCEA1]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[IARS1]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD59]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[RUNX1]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[FRMD6]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RP2]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[DKK1]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[HRH1]] | -0.47 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[DCBLD2]] | -0.47 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ARL4C]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[KIRREL1]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SMAD3]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[EIF5A2]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[PSD3]] | -0.45 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.4, 47.3); signed map (-13.4, 23.2). **Vector** length 129, 39.9% of its response variance represented; |z| ≥ 3 in 1,361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.2 | +5.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +6.0 | +8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.9 | +4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.9 | +7.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.9 | +6.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.4 | -14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -17.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -6.1 | -9.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.7 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.6 | -9.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -7.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | MIA SH3 domain ER export factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:39,230,231-39,388,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22404, TALI, MEA6, cTAGE-5A, cTAGE-5B, cTAGE-5C, cTAGE-5D, MGEA11; previously CTAGE5, MGEA, MGEA6 |
| Gene groups (HGNC) | CTAGE family; MIA family; SH3 domain containing |
| Reactome | 6 pathways, smallest: Cargo concentration in the ER; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PC5](https://www.uniprot.org/uniprotkb/Q96PC5) (Melanoma inhibitory activity protein 2):

> Plays a role in the transport of cargos that are too large to fit into COPII-coated vesicles and require specific mechanisms to be incorporated into membrane-bound carriers and exported from the endoplasmic reticulum. Plays a role in the secretion of lipoproteins, pre-chylomicrons and pre-VLDLs, by participating in their export from the endoplasmic reticulum. Thereby, may play a role in cholesterol and triglyceride homeostasis (By similarity). Required for collagen VII (COL7A1) secretion by …

**Summary**, from NCBI Gene [4253](https://www.ncbi.nlm.nih.gov/gene/4253):

> This gene encodes s receptor in the endoplasmic reticulum, which plays a role in the export of large pre-chylomicrons and pre-very low density lipoproteins (pre-VLDLs). Three major classes of transcripts are generated from this gene- melanoma inhibitory activity 2-specific transcripts, cTAGE family member 5-specific transcripts and transcripts that include exons from both these transcript species (TANGO1-like or TALI). Additionally, alternative splicing in these transcripts results in multiple …

**Accessions** — [HGNC:18432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18432) · Entrez [4253](https://www.ncbi.nlm.nih.gov/gene/4253) · UniProt [Q96PC5](https://www.uniprot.org/uniprotkb/Q96PC5) · Ensembl [ENSG00000150527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150527)

## Data

Gene col 7441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7441); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7441]; `tensor/DDL_lfc|DDL_z.npy` [7441]; `embed/gene_vectors.npy` [7441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7441 or target_col == 7441). Every well: [[MIA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
