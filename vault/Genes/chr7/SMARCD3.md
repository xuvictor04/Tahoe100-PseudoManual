---
symbol: "SMARCD3"
type: "gene"
col: 1332
ensembl_id: "ENSG00000082014"
name: "SWI/SNF related BAF chromatin remodeling complex subunit D3"
location: "7q36.1"
module: 100
arm: "+"
pooled_cpm: 11.36
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 32
n_dd_up_clean: 14
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 14
direction_downstream: 17
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# SMARCD3

*SWI/SNF related BAF chromatin remodeling complex subunit D3* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.34× (z +19.3, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.387× (z -21.4, q 0e+00, down in 38 of 44 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.353× (z -16.6, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARRB2]] (+0.76, fdr 7e-06), [[FAM234B]] (+0.73, fdr 7e-06), [[KCTD17]] (+0.70, fdr 1e-05); moves opposite to [[RFX3-DT]] (-0.66, fdr 5e-05), [[RAB30-DT]] (-0.65, fdr 3e-05), [[LINC00571]] (-0.64, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ADGRB2]] → it (grade B ⚠); 17 go from it, the strongest it → [[SCPEP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.34×** | +19.3 | 0e+00 | 40/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.26×** | +18.9 | 0e+00 | 40/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.29×** | +18.7 | 0e+00 | 38/44 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +14.4 | 7e-45 | 36/45 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.45×** | +14.3 | 2e-44 | 35/44 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.20×** | +12.6 | 1e-34 | 34/45 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.68×** | +8.3 | 1e-14 | 23/44 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +5.4 | 5e-06 | 14/44 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.9 | 6e-05 | 17/36 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.4 | 5e-04 | 5/24 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 14/43 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.27×** | +3.7 | 0.012 | 10/43 (LoVo, C-33 A, …) | two highest doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.013 | 3/44 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.013 | 7/43 (HOP62, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.024 | 7/44 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.032 | 5/45 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.048 | 11/43 (hTERT-HPNE, A-172, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.387×** | -21.4 | 0e+00 | 38/44 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.353×** | -16.6 | 0e+00 | 35/43 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.442×** | -13.0 | 2e-36 | 33/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -12.1 | 1e-31 | 34/45 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.502×** | -11.0 | 6e-26 | 30/43 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.493×** | -10.8 | 3e-25 | 33/44 (C32, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -9.7 | 3e-20 | 27/42 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.602×** | -8.1 | 5e-14 | 25/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.654×** | -6.7 | 1e-09 | 22/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.753×** | -6.4 | 1e-08 | 23/44 (CFPAC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -6.2 | 4e-08 | 23/44 (A-427, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -6.0 | 7e-08 | 22/38 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.688×** | -5.9 | 1e-07 | 20/43 (H4, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -5.8 | 2e-07 | 21/44 (COLO 205, SW 1088, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.700×** | -5.7 | 6e-07 | 18/44 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.700×** | -5.7 | 6e-07 | 15/44 (C-33 A, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.697×** | -5.5 | 1e-06 | 21/43 (HT-29, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.4 | 2e-06 | 18/45 (NCI-H460, C32, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -5.1 | 8e-06 | 19/44 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -4.7 | 8e-05 | 19/42 (SW 900, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.740×** | -4.5 | 2e-04 | 15/44 (C32, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.05 | 4 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.51× (z +11.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -11.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.205× (z -9.9) |
| [[C32 (line)]] | wt | 67.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -10.6) |
| [[LS 180 (line)]] | wt | 3.78 | 3 | 2 | [[Tucidinostat (drug)]] 5 µM 5.77× (z +8.8) | [[Vilanterol (drug)]] 0.05 µM 0.0726× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 46.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -15.5) |
| [[PANC-1 (line)]] | alt | 8.57 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.98× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -9.2) |
| [[HOP62 (line)]] | alt | 7.08 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.29× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.174× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 7.28 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 6.05× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0771× (z -9.4) |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -19.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 3.82 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.05× (z +9.4) | [[Pimozide (drug)]] 0.05 µM 0.0767× (z -9.3) |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -9.2) |
| [[RKO (line)]] | wt | 32.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 18.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0837× (z -8.8) |
| [[AN3 CA (line)]] | alt | 45.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0923× (z -9.3) |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 3.78 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0469× (z -9.8) |
| [[HT-29 (line)]] | alt | 5.46 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.13 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.05 µM 0.0709× (z -8.7) |
| [[KATO III (line)]] | alt | 6.24 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0576× (z -12.3) |
| [[LoVo (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 8.47 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.37× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 6.65 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0900× (z -9.1) |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -17.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 7.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | +0.76 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[KCTD17]] | +0.70 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[HACE1]] | +0.68 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.68 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.67 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ARL6]] | +0.67 | +0.53 / +0.60 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[CDON]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.65 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[MAST3]] | +0.65 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[WASF3]] | +0.65 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3-DT]] | -0.66 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[RAB30-DT]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.64 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ST7L]] | -0.63 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[WARS2-AS1]] | -0.63 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MIRLET7IHG]] | -0.63 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | -0.63 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[DNAI4]] | -0.63 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[MMADHC-DT]] | -0.63 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[NEK11]] | -0.62 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.62 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[INO80D]] | -0.62 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB2]] | B | ADGRB2 activity raises SMARCD3's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without ADGRB2 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[MPP2]] | B | MPP2 activity raises SMARCD3's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.47× lower at baseline in the lines without MPP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[APLP1]] | B | APLP1 activity raises SMARCD3's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without APLP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[PCED1B]] | B | PCED1B activity lowers SMARCD3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.74× higher at baseline in the lines without PCED1B | 0.009 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises SMARCD3's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.33× lower at baseline in the lines without SEPTIN5 | 0.009 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[SEMA6B]] | B | SEMA6B activity raises SMARCD3's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without SEMA6B | 0.019 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises SMARCD3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without GNAZ | 0.025 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises SMARCD3's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without SLC29A4 | 0.044 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[SNTA1]] | B | SNTA1 activity raises SMARCD3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without SNTA1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers SMARCD3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[GXYLT2]] | B | GXYLT2 activity raises SMARCD3's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without GXYLT2 | 0.063 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[TMEM145]] | B | TMEM145 activity raises SMARCD3's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without TMEM145 | 0.071 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCPEP1]] | C | SMARCD3 activity raises SCPEP1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[ASIC1]] | C | SMARCD3 activity raises ASIC1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[HACE1]] | C | SMARCD3 activity raises HACE1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[ARL6]] | C | SMARCD3 activity raises ARL6's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[MPP2]] | C | SMARCD3 activity raises MPP2's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[LRFN3]] | C | SMARCD3 activity raises LRFN3's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[FADS3]] | C | SMARCD3 activity raises FADS3's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[KRBA1]] | C | SMARCD3 activity raises KRBA1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[SNTA1]] | C | SMARCD3 activity raises SNTA1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[CDR2]] | C | SMARCD3 activity lowers CDR2's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.62× higher at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[FAM168A]] | C | SMARCD3 activity raises FAM168A's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.54× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[SSBP4]] | C | SMARCD3 activity raises SSBP4's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without SMARCD3 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.2, -4.0); signed map (-31.5, 0.8). **Vector** length 80.5, 16.1% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +18.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +14.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +19.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +18.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +12.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.3 | -21.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,238,764-151,277,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAF60C, Rsc6p, CRACD3 |
| Gene groups (HGNC) | BAF complex subunits; PBAF complex subunits; GBAF complex subunits |
| Reactome | 41 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the polybromo-BAF (pBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6STE5](https://www.uniprot.org/uniprotkb/Q6STE5) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily D member 3):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Stimulates nuclear receptor mediated transcription. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and the …

**Summary**, from NCBI Gene [6604](https://www.ncbi.nlm.nih.gov/gene/6604):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and has sequence similarity to the yeast Swp73 protein. Multiple alternatively spliced transcript variants have been found for this gene, but the …

**Accessions** — [HGNC:11108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11108) · Entrez [6604](https://www.ncbi.nlm.nih.gov/gene/6604) · UniProt [Q6STE5](https://www.uniprot.org/uniprotkb/Q6STE5) · Ensembl [ENSG00000082014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082014)

## Data

Gene col 1332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1332); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1332]; `tensor/DDL_lfc|DDL_z.npy` [1332]; `embed/gene_vectors.npy` [1332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1332 or target_col == 1332). Every well: [[SMARCD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
