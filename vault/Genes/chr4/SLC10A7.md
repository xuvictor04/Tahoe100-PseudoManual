---
symbol: "SLC10A7"
type: "gene"
col: 4188
ensembl_id: "ENSG00000120519"
name: "solute carrier family 10 member 7"
location: "4q31.22"
module: 72
arm: "+"
pooled_cpm: 53.71
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 39
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# SLC10A7

*solute carrier family 10 member 7* — 4q31.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.18× (z +11.7, q 8e-29, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.358× (z -15.4, q 0e+00, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.473× (z -11.3, q 3e-27, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRF2]] (+0.66, fdr 1e-05), [[PLAA]] (+0.65, fdr 1e-05), [[ZW10]] (+0.64, fdr 1e-05); moves opposite to [[YPEL1]] (-0.49, fdr 8e-05), [[EP300]] (-0.49, fdr 5e-05), [[KBTBD2]] (-0.47, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[DGKG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.18×** | +11.7 | 8e-29 | 42/47 (HOP62, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.27×** | +11.6 | 8e-29 | 43/47 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.04×** | +10.7 | 1e-24 | 41/47 (HOP62, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.080 | 20/46 (NCI-H23, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.080 | 19/47 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.080 | 17/47 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.3 | 0.086 | 13/47 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +3.2 | 0.099 | 18/48 (NCI-H23, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.099 | 16/47 (NCI-H1573, SHP-77, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4188.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -15.4 | 0e+00 | 41/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.398×** | -13.9 | 3e-41 | 41/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.439×** | -12.4 | 8e-33 | 36/46 (LoVo, NCI-H1792, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -11.3 | 3e-27 | 43/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.507×** | -10.2 | 2e-22 | 40/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -9.0 | 3e-17 | 35/47 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.561×** | -8.4 | 5e-15 | 34/46 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -8.0 | 1e-13 | 30/43 (HEC-1-A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -6.9 | 2e-10 | 28/47 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.633×** | -6.9 | 4e-10 | 33/45 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.649×** | -6.2 | 2e-08 | 24/39 (NCI-H460, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.757×** | -5.9 | 2e-07 | 26/47 (NCI-H1792, RPMI-7951, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.668×** | -5.8 | 2e-07 | 27/47 (hTERT-HPNE, A498, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.685×** | -5.7 | 5e-07 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.686×** | -5.7 | 6e-07 | 32/47 (A498, hTERT-HPNE, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -5.5 | 1e-06 | 28/48 (A498, SW 1271, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.691×** | -5.1 | 9e-06 | 26/46 (H4, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -5.1 | 9e-06 | 26/47 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -4.4 | 3e-04 | 24/47 (LoVo, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.751×** | -4.3 | 4e-04 | 21/46 (H4, HOP62, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.595×** | -4.1 | 0.001 | 21/47 (HT-29, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.001 | 24/47 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.691×** | -3.9 | 0.002 | 20/47 (HS-578T, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.009 | 19/47 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.013 | 15/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 76.7 | 3 | 11 (9 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.360× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 39.2 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.163× (z -17.0) |
| [[A498 (line)]] | wt | 95.4 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.242× (z -13.2) |
| [[HOP62 (line)]] | alt | 47.9 | 3 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.82× (z +13.9) | [[Digitoxin (drug)]] 5 µM 0.253× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.270× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -22.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -15.0) |
| [[KATO III (line)]] | alt | 71.4 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.248× (z -12.2) |
| [[HS-578T (line)]] | alt | 55.0 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 76.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.262× (z -9.3) |
| [[J82 (line)]] | alt | 58.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.9) |
| [[SHP-77 (line)]] | alt | 76.6 | 3 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.02× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.270× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 38.2 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.87× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.166× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 88.4 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.08× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 65.7 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.27× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 58.6 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 57.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 87.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.233× (z -9.6) |
| [[HCT15 (line)]] | alt | 87.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -13.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 34.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.05× (z +11.1) | — |
| [[A549 (line)]] | wt | 27.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.254× (z -10.1) |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.200× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 71.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -14.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.69× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0993× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 79.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.319× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 32.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 52.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 62.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRF2]] | +0.66 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[PLAA]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ZW10]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GPX8]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PHKB]] | +0.62 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[PSMD13]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PSMC1]] | +0.59 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[PCYT1A]] | +0.59 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[FAM98A]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PSMC4]] | +0.58 | +0.66 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL1]] | -0.49 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[EP300]] | -0.49 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[KBTBD2]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKG]] | B | DGKG activity raises SLC10A7's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without DGKG | 0.012 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[EGF]] | B | EGF activity raises SLC10A7's level | lines that do not express EGF (23) vs lines expressing it (27) | 1.43× lower at baseline in the lines without EGF | 0.021 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[DGKG]] | B | DGKG activity strengthens SLC10A7's drug response | lines that do not express DGKG (13) vs lines expressing it (35) | the lines without DGKG respond 0.76× as strongly (z diff +1.13); strongest at Dinaciclib 0.5 µM: 0.68x vs 0.40x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises SLC10A7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers SLC10A7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SLC10A7's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.0, -8.3); signed map (-28.1, -24.4). **Vector** length 116, 37.3% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.50 to 12); *proteasome* (control, mean cos +0.52 to 11); *Proteasome assembly* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +13.3 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.8 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.0 | +11.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.6 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.05 µM |  | +1.3 | +1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.3 | +1.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -5.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -11.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -9.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 10 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.22 — chr4:146,253,975-146,522,372 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC25043, DKFZp566M114, DKFZp313H0531, DKFZp779O2438; previously C4orf13 |
| Gene groups (HGNC) | Solute carrier family 10 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0GE19](https://www.uniprot.org/uniprotkb/Q0GE19) (Sodium/bile acid cotransporter 7):

> Involved in teeth and skeletal development. Has an essential role in the biosynthesis and trafficking of glycosaminoglycans and glycoproteins, to produce a proper functioning extracellular matrix. Required for extracellular matrix mineralization. Also involved in the regulation of cellular calcium homeostasis. Does not show transport activity towards bile acids or steroid sulfates (including taurocholate, cholate, chenodeoxycholate, estrone-3-sulfate, dehydroepiandrosterone sulfate (DHEAS) and …

**Summary**, from NCBI Gene [84068](https://www.ncbi.nlm.nih.gov/gene/84068):

> Predicted to enable symporter activity. Involved in bone development; heparin proteoglycan biosynthetic process; and intracellular calcium ion homeostasis. Located in Golgi apparatus; endoplasmic reticulum; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23088) · Entrez [84068](https://www.ncbi.nlm.nih.gov/gene/84068) · UniProt [Q0GE19](https://www.uniprot.org/uniprotkb/Q0GE19) · Ensembl [ENSG00000120519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120519)

## Data

Gene col 4188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4188); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4188]; `tensor/DDL_lfc|DDL_z.npy` [4188]; `embed/gene_vectors.npy` [4188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4188 or target_col == 4188). Every well: [[SLC10A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC10A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
