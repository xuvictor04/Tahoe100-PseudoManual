---
symbol: "UBE4B"
type: "gene"
col: 5146
ensembl_id: "ENSG00000130939"
name: "ubiquitination factor E4B"
location: "1p36.22"
module: 72
arm: "+"
pooled_cpm: 131.07
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# UBE4B

*ubiquitination factor E4B* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.06× (z +19.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.585× (z -20.6, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCD4]] (+0.70, fdr 7e-06), [[UBR2]] (+0.70, fdr 7e-06), [[CRYZL1]] (+0.66, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.61, fdr 8e-06), [[TTPAL]] (-0.61, fdr 1e-05), [[CHAMP1]] (-0.61, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +19.6 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +17.6 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +15.4 | 0e+00 | 46/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +7.8 | 1e-12 | 43/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +5.0 | 6e-05 | 31/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.36×** | +4.2 | 0.002 | 26/45 (PANC-1, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +4.1 | 0.004 | 18/47 (SW48, NCI-H2030, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.25× | +3.1 | 0.15 | 15/50 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.0 | 0.17 | 14/48 (LoVo, LS 180, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -20.6 | 0e+00 | 40/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -18.7 | 0e+00 | 45/48 (AN3 CA, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.500×** | -17.4 | 0e+00 | 41/45 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -15.0 | 0e+00 | 43/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.575×** | -15.0 | 0e+00 | 43/49 (NCI-H1573, HCT15, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.609×** | -13.5 | 3e-39 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.651×** | -11.2 | 3e-27 | 34/44 (SK-MEL-2, C-33 A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -11.2 | 4e-27 | 40/48 (SW480, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -10.8 | 3e-25 | 33/49 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.697×** | -9.8 | 7e-21 | 42/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -9.4 | 4e-19 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.727×** | -8.7 | 2e-16 | 41/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.755×** | -7.6 | 1e-12 | 36/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -7.4 | 7e-12 | 32/47 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.785×** | -6.6 | 2e-09 | 27/48 (SW480, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.818×** | -5.4 | 2e-06 | 26/49 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.696×** | -5.0 | 2e-05 | 25/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.822×** | -4.9 | 2e-05 | 25/47 (HEC-1-A, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -4.8 | 3e-05 | 10/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.710×** | -4.7 | 6e-05 | 26/48 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.787×** | -4.5 | 2e-04 | 25/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.852× | -4.3 | 3e-04 | 22/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.730×** | -4.3 | 3e-04 | 25/46 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 158 | 4 | 11 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +19.3) | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -23.7) |
| [[SW480 (line)]] | alt | 128 | 3 | 9 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.13× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 191 | 2 | 9 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.50× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -19.3) |
| [[C32 (line)]] | wt | 165 | 3 | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 223 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 144 | 2 | 8 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -16.6) |
| [[A549 (line)]] | wt | 81.9 | 1 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +10.5) | [[Harringtonine (drug)]] 5 µM 0.338× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 203 | 1 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.88× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 189 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 103 | 3 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.97× (z +11.4) | [[Harringtonine (drug)]] 0.5 µM 0.452× (z -13.3) |
| [[SW 900 (line)]] | alt | 129 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 114 | 3 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -18.9) |
| [[HepG2_C3A (line)]] | wt | 198 | 3 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.59× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -14.7) |
| [[HOP62 (line)]] | alt | 150 | 2 | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -27.8) |
| [[HS-578T (line)]] | alt | 178 | 2 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -13.5) |
| [[HT-29 (line)]] | alt | 150 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.40× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 100 | 4 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -14.1) |
| [[LS 180 (line)]] | wt | 146 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.650× (z -9.1) |
| [[A-427 (line)]] | wt | 176 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -12.2) |
| [[A498 (line)]] | wt | 82.2 | 2 | 3 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.12× (z +8.9) | [[Harringtonine (drug)]] 0.5 µM 0.468× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 83.7 | 1 | 4 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.38× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -10.0) |
| [[C-33 A (line)]] | alt | 200 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -13.2) |
| [[COLO 205 (line)]] | alt | 136 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +12.4) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.131× (z -11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.5) |
| [[H4 (line)]] | wt | 151 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -10.0) |
| [[Hs 766T (line)]] | wt | 174 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.98× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.484× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 122 | 2 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.481× (z -9.3) |
| [[SW48 (line)]] | wt | 114 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -14.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 141 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -12.0) |
| [[AN3 CA (line)]] | alt | 173 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0746× (z -21.6) |
| [[HCT15 (line)]] | alt | 180 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.4) |
| [[KATO III (line)]] | alt | 117 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 96.0 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 83.1 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.184× (z -10.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 76.8 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.55× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 84.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.147× (z -10.3) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 141 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.0) |
| [[SHP-77 (line)]] | alt | 120 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.15× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 157 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.59× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 87.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -9.6) |
| [[J82 (line)]] | alt | 98.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.84× (z +9.0) | — |
| [[RKO (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCD4]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[UBR2]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 | STRING 417 |
| [[CRYZL1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[MED31]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MYL6B]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[HMBOX1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[EGFL8]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PPP1R12B]] | +0.63 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FTL]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.61 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[TTPAL]] | -0.61 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[CHAMP1]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[ETS1]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[CSRNP1]] | -0.57 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[TOMM34]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CDC42EP2]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CDC42EP1]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ARHGDIA]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[RAPH1]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UBE4B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, -11.7); signed map (-21.7, 3.9). **Vector** length 131, 44.4% of its response variance represented; |z| ≥ 3 in 1,439 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +14.2 | +15.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +13.9 | +19.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.8 | +17.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +7.3 | +7.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | +5.4 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.2 | -18.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.0 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -20.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.7 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.2 | -17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -11.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitination factor E4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,032,832-10,181,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBOX3, E4, UFD2, KIAA0684 |
| Gene groups (HGNC) | U-box domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95155](https://www.uniprot.org/uniprotkb/O95155) (Ubiquitin conjugation factor E4 B):

> Acts as an E3 ubiquitin ligase and E4 ubiquitin chain elongation enzyme specifically involved in polyubiquitin chain assembly. Plays an essential role in cardiac development and in the protection of neurons from degeneration evoked by ER stress (By similarity). Is recruited to early endosomes via interaction with the ESCRT-0 component HGS, where it ubiquitinates membrane protein cargo such as EGFR and APP to promote their sorting into multivesicular bodies and subsequent lysosomal degradation. …

**Summary**, from NCBI Gene [10277](https://www.ncbi.nlm.nih.gov/gene/10277):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes an additional conjugation factor, E4, which is involved in multiubiquitin chain assembly. This gene is also the strongest candidate in the neuroblastoma tumor …

**Accessions** — [HGNC:12500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12500) · Entrez [10277](https://www.ncbi.nlm.nih.gov/gene/10277) · UniProt [O95155](https://www.uniprot.org/uniprotkb/O95155) · Ensembl [ENSG00000130939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130939)

## Data

Gene col 5146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5146); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5146]; `tensor/DDL_lfc|DDL_z.npy` [5146]; `embed/gene_vectors.npy` [5146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5146 or target_col == 5146). Every well: [[UBE4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
