---
symbol: "LONRF1"
type: "gene"
col: 7802
ensembl_id: "ENSG00000154359"
name: "LON peptidase N-terminal domain and ring finger 1"
location: "8p23.1"
module: 24
arm: "+"
pooled_cpm: 35.46
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# LONRF1

*LON peptidase N-terminal domain and ring finger 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +8.2, q 1e-13, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.391× (z -18.7, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.582× (z -10.8, q 5e-25, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D12]] (+0.59, fdr 1e-05), [[LNX2]] (+0.58, fdr 3e-05), [[PDCD5]] (+0.54, fdr 1e-05); moves opposite to [[RANBP6]] (-0.56, fdr 1e-05), [[SRPX2]] (-0.55, fdr 2e-05), [[ERGIC2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.2 | 1e-13 | 28/46 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.1 | 9e-05 | 22/44 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.0 | 1e-04 | 17/46 (A498, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.012 | 12/46 (HCT15, C-33 A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.20× | +3.7 | 0.025 | 12/46 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.043 | 10/46 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.074 | 9/46 (H4, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.074 | 9/45 (LOX-IMVI, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Berbamine (drug)]] 5 µM |  | 1.12× | +3.2 | 0.080 | 8/47 (NCI-H23, C-33 A, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | 1.34× | +3.1 | 0.12 | 8/45 (A498, SW 900, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.391×** | -18.7 | 0e+00 | 40/45 (C-33 A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.437×** | -16.5 | 0e+00 | 45/46 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.451×** | -15.3 | 0e+00 | 30/38 (A-427, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.497×** | -13.9 | 5e-42 | 43/46 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.497×** | -12.9 | 7e-36 | 31/41 (A-427, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -10.8 | 5e-25 | 33/45 (HS-578T, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.585×** | -10.7 | 1e-24 | 36/46 (A-427, A549, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.693×** | -10.2 | 2e-22 | 38/46 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -9.3 | 6e-19 | 35/46 (C32, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.701×** | -7.0 | 1e-10 | 27/46 (HS-578T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.713×** | -6.7 | 1e-09 | 24/45 (LoVo, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.549×** | -6.2 | 2e-08 | 29/47 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.721×** | -6.2 | 2e-08 | 26/45 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.742×** | -5.9 | 1e-07 | 23/46 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -5.8 | 2e-07 | 22/46 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -4.9 | 3e-05 | 21/46 (A-427, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.624×** | -4.9 | 3e-05 | 19/44 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.8 | 5e-05 | 19/46 (A498, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.777×** | -4.7 | 7e-05 | 19/45 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -4.4 | 3e-04 | 23/46 (A498, SW 900, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.657×** | -4.4 | 3e-04 | 19/44 (SNU-423, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -4.0 | 0.002 | 18/46 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.875× | -3.6 | 0.006 | 11/46 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.824×** | -3.6 | 0.006 | 17/46 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 87.3 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0956× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.571× (z -9.5) |
| [[A498 (line)]] | wt | 41.7 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.5) ⚠ cell-cycle shift, explains ~73% of this change | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.469× (z -9.6) |
| [[A549 (line)]] | wt | 56.6 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.474× (z -9.9) |
| [[HS-578T (line)]] | alt | 54.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -17.0) |
| [[LoVo (line)]] | wt | 31.5 | 2 (1 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -15.2) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A-172 (line)]] | wt | 89.3 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0730× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.488× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 45.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 39.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 41.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -17.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -11.5) |
| [[RKO (line)]] | wt | 38.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 47.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 31.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.5) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.0) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.9) ⚠ cell-cycle shift, explains ~73% of this change |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.5) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 77.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 47.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -8.8) |
| [[SW480 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.273× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[KATO III (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.340× (z -11.0) |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D12]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LNX2]] | +0.58 | +0.44 / +0.49 | both halves | 3e-05 | same gene group |
| [[PDCD5]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TRIM36]] | +0.53 | +0.38 / +0.43 | both halves | 6e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[COMTD1]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[SNHG7]] | +0.52 | +0.37 / +0.50 | both halves | 7e-05 |  |
| [[PRKRA]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[HABP4]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[TRIM52-AS1]] | +0.51 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[ZC2HC1A]] | +0.51 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[MAP3K21]] | +0.51 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[RAB6A]] | +0.50 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP6]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SRPX2]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ERGIC2]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[NORAD]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[LINC00641]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[RIN2]] | -0.52 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[USP16]] | -0.51 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[EID1]] | -0.51 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[DPP8]] | -0.50 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[RAB1B]] | -0.50 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[ATXN7L3B]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.8, -25.3); signed map (-22.1, 15.7). **Vector** length 104, 26.4% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +8.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.1 | -12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.9 | -15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -10.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | LON peptidase N-terminal domain and ring finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:12,721,906-12,756,073 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23749, RNF191 |
| Gene groups (HGNC) | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

UniProt [Q17RB8](https://www.uniprot.org/uniprotkb/Q17RB8) carries no function annotation.

**Summary**, from NCBI Gene [91694](https://www.ncbi.nlm.nih.gov/gene/91694):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26302) · Entrez [91694](https://www.ncbi.nlm.nih.gov/gene/91694) · UniProt [Q17RB8](https://www.uniprot.org/uniprotkb/Q17RB8) · Ensembl [ENSG00000154359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154359)

## Data

Gene col 7802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7802); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7802]; `tensor/DDL_lfc|DDL_z.npy` [7802]; `embed/gene_vectors.npy` [7802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7802 or target_col == 7802). Every well: [[LONRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LONRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
