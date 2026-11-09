---
symbol: "TRIB1"
type: "gene"
col: 10374
ensembl_id: "ENSG00000173334"
name: "tribbles pseudokinase 1"
location: "8q24.13"
module: 109
arm: "+"
pooled_cpm: 64.26
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 30
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# TRIB1

*tribbles pseudokinase 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.01× (z +14.5, q 7e-45, up in 39 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.429× (z -17.0, q 0e+00, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP5]] (+0.68, fdr 7e-06), [[CSRNP1]] (+0.68, fdr 7e-06), [[SGK1]] (+0.68, fdr 7e-06); moves opposite to [[FHIP2A]] (-0.55, fdr 3e-05), [[NAPB]] (-0.54, fdr 3e-05), [[MFSD8]] (-0.53, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); 30 go from it, the strongest it → [[ST3GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.01×** | +14.5 | 7e-45 | 39/43 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.9 | 7e-13 | 30/42 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 1e-06 | 27/42 (HepG2/C3A, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +5.4 | 8e-06 | 21/42 (NCI-H2030, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 5e-04 | 22/42 (BT-474, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +4.5 | 5e-04 | 22/42 (NCI-H1573, HS-578T, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.006 | 18/41 (LOX-IMVI, RKO, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.020 | 18/43 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.28×** | +3.6 | 0.024 | 15/42 (AsPC-1, NCI-H1573, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.26×** | +3.3 | 0.064 | 14/41 (NCI-H2030, AsPC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.51× | +3.1 | 0.11 | 14/41 (NCI-H2030, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.429×** | -17.0 | 0e+00 | 38/42 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.288×** | -17.0 | 0e+00 | 39/41 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.377×** | -13.3 | 2e-38 | 27/34 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.409×** | -12.2 | 4e-32 | 36/44 (HT-29, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.486×** | -10.2 | 2e-22 | 28/42 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.600×** | -7.2 | 4e-11 | 32/42 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.692×** | -5.2 | 1e-05 | 27/42 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.692×** | -5.2 | 1e-05 | 24/42 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[NG25 (drug)]] 5 µM |  | **0.525×** | -4.8 | 1e-04 | 25/40 (HT-29, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.707×** | -4.6 | 3e-04 | 23/42 (SW48, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.734×** | -4.4 | 6e-04 | 22/42 (RKO, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.736×** | -4.3 | 7e-04 | 22/42 (COLO 205, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.747×** | -4.1 | 0.002 | 20/42 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.1 | 0.002 | 21/41 (LOX-IMVI, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.823×** | -3.9 | 0.004 | 21/42 (J82, RKO, …) | rises with dose | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.004 | 19/42 (CHP-212, HS-578T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.624×** | -3.5 | 0.016 | 16/43 (COLO 205, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.025 | 17/43 (A-172, SW 900, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.045 | 16/42 (HT-29, SW 1088, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.047 | 17/41 (SW48, C32, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **0.809×** | -3.0 | 0.069 | 14/42 (KATO III, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 429 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -20.4) |
| [[NCI-H2030 (line)]] | alt | 63.2 | 6 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 20.9× (z +12.4) | [[Adagrasib (drug)]] 0.05 µM 0.540× (z -17.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 57.9 | 2 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -18.4) |
| [[AsPC-1 (line)]] | alt | 144 | 6 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.7× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.3) |
| [[SW48 (line)]] | wt | 95.8 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 18.8× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -15.4) |
| [[A498 (line)]] | wt | 75.4 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 73.8 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.90× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.1) |
| [[COLO 205 (line)]] | alt | 180 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -12.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.7) |
| [[HS-578T (line)]] | alt | 51.6 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.98× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -12.8) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.5) |
| [[A549 (line)]] | wt | 109 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -15.7) |
| [[C32 (line)]] | wt | 81.0 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 46.2× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -16.4) |
| [[Hs 766T (line)]] | wt | 59.9 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.1× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 72.6 | 4 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 29.7× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 75.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.1) |
| [[RKO (line)]] | wt | 73.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -11.6) |
| [[SW 900 (line)]] | alt | 61.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.5) |
| [[SW1417 (line)]] | alt | 110 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.11× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -20.5) |
| [[BT-474 (line)]] | alt | 85.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 88.5 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 24.2× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.8) |
| [[KATO III (line)]] | alt | 112 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 0.5 µM 0.329× (z -9.0) |
| [[SW480 (line)]] | alt | 67.7 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.32× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.0) |
| [[J82 (line)]] | alt | 47.6 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.247× (z -14.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.0) |
| [[LS 180 (line)]] | wt | 106 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.517× (z -13.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 26.0× (z +10.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -11.7) |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -10.5) |
| [[SHP-77 (line)]] | alt | 47.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.1) |
| [[H4 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.543× (z -12.0) ⚠ position not correctable |
| [[LoVo (line)]] | wt | 43.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 34.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.6) |
| [[A-427 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP5]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 436 |
| [[CSRNP1]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 | STRING 465 |
| [[SGK1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EFNB2]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NFKBIZ]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SOCS3]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IER2]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DUSP1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 571 |
| [[TIPARP]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SGMS2]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[EGR1]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 888 |
| [[JUNB]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 592 |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | -0.55 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NAPB]] | -0.54 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.53 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[GPALPP1]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CDC23]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[NAP1L4]] | -0.51 | -0.32 / -0.59 | both halves | 1e-04 |  |
| [[TIAL1]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CLCC1]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[BMPR1A]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SOS1]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[RAB11FIP2]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises TRIB1's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without CCL20 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises TRIB1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without ST3GAL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[ABTB2]] | B | ABTB2 activity raises TRIB1's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without ABTB2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[ARC]] | B | ARC activity raises TRIB1's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without ARC | 0.058 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[KLF5]] | B | KLF5 activity raises TRIB1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without KLF5 | 0.081 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[TGM2]] | B | TGM2 activity raises TRIB1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without TGM2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[LINC00511]] | C | LINC00511 activity raises TRIB1's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.42× lower at baseline in the lines without LINC00511 | 0.010 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18; co-absent with the target |
| [[ETS2]] | C | ETS2 activity raises TRIB1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.64× lower at baseline in the lines without ETS2 | 0.029 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3; co-absent with the target |
| [[TGFBR2]] | C | TGFBR2 activity raises TRIB1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 3.09× lower at baseline in the lines without TGFBR2 | 0.044 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET; co-absent with the target |
| [[FHL2]] | C | FHL2 activity raises TRIB1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 3.35× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 23, C 7. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | TRIB1 activity raises ST3GAL1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 5.56× lower at baseline in the lines without TRIB1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[EXT1]] | B | TRIB1 activity raises EXT1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without TRIB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[MCL1]] | B | TRIB1 activity raises MCL1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without TRIB1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[ATP2B1]] | B | TRIB1 activity raises ATP2B1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without TRIB1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[LDLR]] | B | TRIB1 activity raises LDLR's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without TRIB1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[PTGER4]] | B | TRIB1 activity raises PTGER4's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.89× lower at baseline in the lines without TRIB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[SLC38A2]] | B | TRIB1 activity lowers SLC38A2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without TRIB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[FHL2]] | B | TRIB1 activity raises FHL2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 3.34× lower at baseline in the lines without TRIB1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[PMEPA1]] | B | TRIB1 activity raises PMEPA1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without TRIB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[MARCHF3]] | B | TRIB1 activity raises MARCHF3's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without TRIB1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[CSRNP1]] | B | TRIB1 activity raises CSRNP1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without TRIB1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[NFKBIZ]] | B | TRIB1 activity raises NFKBIZ's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.60× lower at baseline in the lines without TRIB1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 7.0); signed map (9.8, 29.2). **Vector** length 124, 36.7% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.57 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +14.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -17.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -17.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -7.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | tribbles pseudokinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:125,430,358-125,438,403 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C8FW, GIG2, TRB1 |
| Gene groups (HGNC) | Pseudokinases; Tribbles pseudokinase family |
| Hallmark sets | KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RU8](https://www.uniprot.org/uniprotkb/Q96RU8) (Tribbles homolog 1):

> Adapter protein involved in protein degradation by interacting with COP1 ubiquitin ligase. The COP1-binding motif is masked by autoinhibitory interactions with the protein kinase domain. Serves to alter COP1 substrate specificity by directing the activity of COP1 toward CEBPA. Binds selectively the recognition sequence of CEBPA. Regulates myeloid cell differentiation by altering the expression of CEBPA in a COP1-dependent manner (By similarity). Controls macrophage, eosinophil and neutrophil …

**Summary**, from NCBI Gene [10221](https://www.ncbi.nlm.nih.gov/gene/10221):

> Enables several functions, including mitogen-activated protein kinase kinase binding activity; protein kinase inhibitor activity; and transcription regulator inhibitor activity. Involved in several processes, including negative regulation of signal transduction; negative regulation of smooth muscle cell proliferation; and regulation of MAP kinase activity. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16891) · Entrez [10221](https://www.ncbi.nlm.nih.gov/gene/10221) · UniProt [Q96RU8](https://www.uniprot.org/uniprotkb/Q96RU8) · Ensembl [ENSG00000173334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173334)

## Data

Gene col 10374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10374); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10374]; `tensor/DDL_lfc|DDL_z.npy` [10374]; `embed/gene_vectors.npy` [10374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10374 or target_col == 10374). Every well: [[TRIB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
