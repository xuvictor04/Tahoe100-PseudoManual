---
symbol: "MEIS1"
type: "gene"
col: 6831
ensembl_id: "ENSG00000143995"
name: "Meis homeobox 1"
location: "2p14"
module: 152
arm: "+"
pooled_cpm: 35.71
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 33
n_dd_up_clean: 17
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 12
direction_downstream: 9
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# MEIS1

*Meis homeobox 1* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.86× (z +19.1, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.428× (z -15.4, q 0e+00, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACKR3]] (+0.60, fdr 2e-05), [[SFMBT2]] (+0.60, fdr 2e-05), [[TCIM]] (+0.59, fdr 3e-05); moves opposite to [[ECPAS]] (-0.52, fdr 3e-05), [[TMEM11-DT]] (-0.50, fdr 4e-05), [[METTL4]] (-0.49, fdr 4e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[NDNF]] → it (grade B ⚠); 9 go from it, the strongest it → [[AHR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.86×** | +19.1 | 0e+00 | 32/37 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +16.0 | 0e+00 | 32/37 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +15.0 | 0e+00 | 31/37 (NCI-H460, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +14.8 | 0e+00 | 30/37 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.95×** | +12.1 | 1e-31 | 32/37 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +10.2 | 1e-22 | 26/37 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +7.3 | 2e-11 | 24/38 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +6.7 | 1e-09 | 21/38 (NCI-H460, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +6.0 | 1e-07 | 16/36 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 3e-05 | 15/36 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 14/37 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 17/38 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.27×** | +4.3 | 6e-04 | 15/37 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 6e-04 | 13/37 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.002 | 13/36 (A-427, LS 180, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.005 | 13/37 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.016 | 12/37 (A-172, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -15.4 | 0e+00 | 28/37 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.474×** | -13.6 | 2e-39 | 35/37 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -13.0 | 4e-36 | 31/37 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.537×** | -11.3 | 2e-27 | 30/37 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.542×** | -11.1 | 9e-27 | 25/37 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.516×** | -10.9 | 8e-26 | 28/37 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -9.4 | 5e-19 | 25/37 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -9.2 | 2e-18 | 24/35 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -8.7 | 2e-16 | 25/37 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -8.7 | 2e-16 | 19/29 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -7.3 | 2e-11 | 21/35 (hTERT-HPNE, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -7.1 | 4e-11 | 22/38 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.707×** | -6.3 | 1e-08 | 21/36 (C32, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.701×** | -6.2 | 2e-08 | 20/36 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.520×** | -6.2 | 2e-08 | 18/37 (NCI-H1792, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.731×** | -5.7 | 4e-07 | 18/37 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.757×** | -5.1 | 1e-05 | 18/37 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.736×** | -5.0 | 2e-05 | 16/36 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.778×** | -4.4 | 3e-04 | 15/37 (NCI-H2030, SHP-77, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.673×** | -3.8 | 0.004 | 10/37 (NCI-H1792, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 220 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.227× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 417 | 1 | 9 (8 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0802× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.178× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.303× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 39.2 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.17× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.275× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.358× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 16.2 | 6 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.58× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.209× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 28.0 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.39× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0816× (z -17.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.223× (z -10.6) |
| [[SHP-77 (line)]] | alt | 135 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -9.9) |
| [[SW480 (line)]] | alt | 26.0 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.192× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.242× (z -13.3) |
| [[SW 900 (line)]] | alt | 55.6 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.189× (z -12.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.230× (z -11.4) |
| [[A-172 (line)]] | wt | 56.9 | 4 | 0 | [[Ponatinib (drug)]] 5 µM 3.37× (z +9.3) | — |
| [[A-427 (line)]] | wt | 23.4 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.64× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.5) |
| [[A498 (line)]] | wt | 19.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.53× (z +13.2) | — |
| [[A549 (line)]] | wt | 29.9 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -11.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.236× (z -8.9) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0495× (z -16.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 43.7 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0695× (z -15.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 44.6 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.22× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 23.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.235× (z -9.2) |
| [[Hs 766T (line)]] | wt | 44.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.34× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.271× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 35.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.7 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.06× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 41.2 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.46× (z +8.9) | [[Ixazomib citrate (drug)]] 5 µM 0.241× (z -9.9) |
| [[HOP62 (line)]] | alt | 25.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.189× (z -8.7) |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0589× (z -10.3) |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACKR3]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[SFMBT2]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TCIM]] | +0.59 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SNAP25]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[LRCH2]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PDGFRL]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TMEM178B]] | +0.55 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[CDH12]] | +0.53 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[BASP1]] | +0.53 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[DNAJC12]] | +0.52 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[EYA1]] | +0.52 | +0.39 / +0.50 | both halves | 6e-05 | STRING 715 |
| [[RORB]] | +0.52 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECPAS]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.50 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[METTL4]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZNF731P]] | -0.49 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[KLC1]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[KCTD15]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PTPDC1]] | -0.48 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.47 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[KCNIP2]] | -0.47 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[TMCO3]] | -0.47 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[GLRX3]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[EXD3]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDNF]] | B | NDNF activity raises MEIS1's level | lines that do not express NDNF (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without NDNF | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[PEX5L]] | B | PEX5L activity raises MEIS1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 3.16× lower at baseline in the lines without PEX5L | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[CD38]] | B | CD38 activity raises MEIS1's level | lines that do not express CD38 (35) vs lines expressing it (15) | 3.03× lower at baseline in the lines without CD38 | 0.022 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent |
| [[SNAP25]] | B | SNAP25 activity raises MEIS1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.52× lower at baseline in the lines without SNAP25 | 0.022 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[GNG2]] | B | GNG2 activity raises MEIS1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without GNG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[BICC1]] | B | BICC1 activity raises MEIS1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without BICC1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[AGTR1]] | B | AGTR1 activity raises MEIS1's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.41× lower at baseline in the lines without AGTR1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN |
| [[PDE4D]] | B | PDE4D activity raises MEIS1's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 2.62× lower at baseline in the lines without PDE4D | 0.060 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[BDKRB2]] | B | BDKRB2 activity raises MEIS1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.91× lower at baseline in the lines without BDKRB2 | 0.074 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[PALMD]] | B | PALMD activity raises MEIS1's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without PALMD | 0.094 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[DNAJC12]] | B | DNAJC12 activity raises MEIS1's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without DNAJC12 | 0.097 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[RGL1]] | C | RGL1 activity raises MEIS1's level | lines that do not express RGL1 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without RGL1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01138, CDK6, IGF2BP3; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | MEIS1 activity raises AHR's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 3.30× lower at baseline in the lines without MEIS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[PDE4D]] | B | MEIS1 activity raises PDE4D's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without MEIS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[BICC1]] | B | MEIS1 activity raises BICC1's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 5.00× lower at baseline in the lines without MEIS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[PLA2G4A]] | B | MEIS1 activity raises PLA2G4A's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 3.54× lower at baseline in the lines without MEIS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[SFTA3-1]] | B | MEIS1 activity lowers SFTA3-1's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 1.61× higher at baseline in the lines without MEIS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[SFMBT2]] | B | MEIS1 activity raises SFMBT2's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 2.97× lower at baseline in the lines without MEIS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[NDNF]] | B | MEIS1 activity raises NDNF's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without MEIS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[NOVA1]] | B | MEIS1 activity raises NOVA1's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without MEIS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[PTGS2]] | B | MEIS1 activity raises PTGS2's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 4.21× lower at baseline in the lines without MEIS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.9, 31.4); signed map (38.3, 39.0). **Vector** length 79.7, 16.9% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | -7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.0 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | -1.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -13.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -11.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -11.3 |

## What is on record

|  |  |
|---|---|
| Name | Meis homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:66,433,452-66,573,869 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O00470](https://www.uniprot.org/uniprotkb/O00470) (Homeobox protein Meis1):

> Acts as a transcriptional regulator of PAX6. Acts as a transcriptional activator of PF4 in complex with PBX1 or PBX2. Required for hematopoiesis, megakaryocyte lineage development and vascular patterning. May function as a cofactor for HOXA7 and HOXA9 in the induction of myeloid leukemias.

**Summary**, from NCBI Gene [4211](https://www.ncbi.nlm.nih.gov/gene/4211):

> Homeobox genes, of which the most well-characterized category is represented by the HOX genes, play a crucial role in normal development. In addition, several homeoproteins are involved in neoplasia. This gene encodes a homeobox protein belonging to the TALE ('three amino acid loop extension') family of homeodomain-containing proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7000) · Entrez [4211](https://www.ncbi.nlm.nih.gov/gene/4211) · UniProt [O00470](https://www.uniprot.org/uniprotkb/O00470) · Ensembl [ENSG00000143995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143995)

## Data

Gene col 6831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6831); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6831]; `tensor/DDL_lfc|DDL_z.npy` [6831]; `embed/gene_vectors.npy` [6831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6831 or target_col == 6831). Every well: [[MEIS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEIS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
