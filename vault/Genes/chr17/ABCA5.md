---
symbol: "ABCA5"
type: "gene"
col: 7792
ensembl_id: "ENSG00000154265"
name: "ATP binding cassette subfamily A member 5"
location: "17q24.3"
module: 59
arm: "+"
pooled_cpm: 88.07
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 29
n_dd_up_clean: 15
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ABCA5

*ATP binding cassette subfamily A member 5* — 17q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.31× (z +39.3, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.404× (z -14.5, q 7e-45, down in 34 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.616× (z -8.1, q 1e-13, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF821]] (+0.71, fdr 7e-06), [[TXNDC16]] (+0.69, fdr 7e-06), [[KMT2E]] (+0.67, fdr 1e-05); moves opposite to [[EIPR1]] (-0.75, fdr 7e-06), [[BLTP2]] (-0.69, fdr 7e-06), [[PSMD1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DNAJC12]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF385C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.31×** | +39.3 | 0e+00 | 44/44 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.69×** | +20.9 | 0e+00 | 41/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +11.0 | 6e-26 | 33/44 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +5.8 | 8e-07 | 25/44 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 23/45 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.8 | 2e-04 | 21/44 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 6e-04 | 26/45 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 7e-04 | 23/43 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +4.3 | 0.001 | 24/46 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.3 | 0.001 | 21/44 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.28×** | +4.2 | 0.002 | 26/44 (SNU-1, Hs 766T, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.006 | 20/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.25×** | +3.7 | 0.010 | 21/44 (J82, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.011 | 23/46 (HepG2/C3A, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.16× | +3.5 | 0.015 | 19/44 (LoVo, C32, …) | all doses, flat | low cells (technical?) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.015 | 19/44 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.019 | 22/44 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.019 | 21/44 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.019 | 21/44 (RKO, NCI-H460, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.042 | 15/45 (HepG2/C3A, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -14.5 | 7e-45 | 34/40 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.450×** | -13.3 | 9e-38 | 34/45 (NCI-H23, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.489×** | -11.0 | 6e-26 | 33/41 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -8.1 | 1e-13 | 36/44 (SNU-423, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -6.1 | 1e-07 | 29/44 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.509×** | -5.9 | 4e-07 | 31/41 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.516×** | -5.7 | 7e-07 | 33/44 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.697×** | -5.7 | 7e-07 | 28/44 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.531×** | -5.5 | 2e-06 | 21/35 (H4, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -5.5 | 2e-06 | 30/44 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -5.4 | 3e-06 | 29/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.797×** | -5.3 | 5e-06 | 31/44 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -5.0 | 2e-05 | 20/44 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.584×** | -4.7 | 1e-04 | 28/44 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.760×** | -4.4 | 5e-04 | 26/44 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.769×** | -4.2 | 0.001 | 27/44 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.762×** | -4.1 | 0.002 | 23/43 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -3.7 | 0.006 | 21/44 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.678×** | -3.4 | 0.022 | 21/44 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.026 | 17/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.812×** | -3.3 | 0.026 | 16/45 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.817×** | -3.2 | 0.034 | 16/44 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.035 | 16/44 (HEC-1-A, J82, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.047 | 17/43 (HOP62, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 124 | 1 | 12 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.413× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 103 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +38.7) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 202 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -10.1) |
| [[BT-474 (line)]] | alt | 63.2 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +29.7) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 274 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 63.6 | 4 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +28.7) | [[Bortezomib (drug)]] 5 µM 0.0719× (z -11.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.349× (z -9.1) |
| [[A498 (line)]] | wt | 85.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 163 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 80.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +26.6) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 56.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +35.0) | — |
| [[hTERT-HPNE (line)]] | wt | 176 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +26.9) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 42.5 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +35.0) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 143 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +30.0) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 130 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 135 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +24.7) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 218 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0469× (z -24.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 101 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +19.0) | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -17.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +30.7) | — |
| [[H4 (line)]] | wt | 84.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +32.6) | [[Lonafarnib (drug)]] 5 µM 0.0693× (z -9.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 87.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +19.6) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 126 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 77.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +23.6) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 74.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 36.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +32.2) | — |
| [[RKO (line)]] | wt | 94.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +24.3) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 120 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 58.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +21.6) | — |
| [[COLO 205 (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 85.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +22.7) | [[PH-797804 (drug)]] 5 µM 0.161× (z -10.5) |
| [[HT-29 (line)]] | alt | 70.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +27.4) | [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -10.1) |
| [[J82 (line)]] | alt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +27.8) | — |
| [[LS 180 (line)]] | wt | 55.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -15.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 42.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +21.8) | — |
| [[CHP-212 (line)]] | wt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +22.2) | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 57.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +21.4) | — |
| [[NCI-H1573 (line)]] | alt | 48.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +18.0) | — |
| [[Panc 03.27 (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +18.8) | [[Lonafarnib (drug)]] 5 µM 0.156× (z -9.2) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 93.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +12.2) | — |
| [[SW 1271 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.3) | — |
| [[SW48 (line)]] | wt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +14.2) | — |
| [[A-172 (line)]] | wt | 6.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | +0.71 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[KMT2E]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SNX2]] | +0.64 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ZFYVE1]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PIK3IP1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CHMP2B]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LCA5]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[STAP2]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIPR1]] | -0.75 | -0.72 / -0.68 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.69 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[PSMD1]] | -0.67 | -0.63 / -0.61 | both halves | 7e-06 | pathway: ABC-family protein mediated transport |
| [[NIPA2]] | -0.67 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[HERC2]] | -0.67 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[CHCHD6]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[CCT5]] | -0.65 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[STIP1]] | -0.65 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.65 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[TCOF1]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[PGAM5]] | -0.63 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[CCT6A]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC12]] | B | DNAJC12 activity raises ABCA5's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without DNAJC12 | 0.036 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[GIHCG]] | B | GIHCG activity raises ABCA5's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without GIHCG | 0.064 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[NEURL3]] | B | NEURL3 activity raises ABCA5's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without NEURL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[PSTPIP2]] | B | PSTPIP2 activity strengthens ABCA5's drug response | lines that do not express PSTPIP2 (18) vs lines expressing it (27) | the lines without PSTPIP2 respond 0.84× as strongly (z diff +0.85); strongest at Dinaciclib 5 µM: 0.59x vs 0.33x (z diff +4.1) | 0.080 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1; target measured in part of the lines; artifact flags |
| [[ZNF385C]] | C | ZNF385C activity raises ABCA5's level | lines that do not express ZNF385C (4) vs lines expressing it (46) | 3.75× lower at baseline in the lines without ZNF385C | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: SMC1B, ARG2, SPRY1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385C]] | C | ABCA5 activity raises ZNF385C's level | lines that do not express ABCA5 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without ABCA5 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: ABCA10, TRIM47, GPAT3 |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.1, -38.3); signed map (-8.7, 3.6). **Vector** length 134, 44.7% of its response variance represented; |z| ≥ 3 in 1,482 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members* (reactome, mean cos +0.50 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +20.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +39.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.9 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.1 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.3 — chr17:69,244,311-69,327,244 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST90625 |
| Gene groups (HGNC) | ATP binding cassette subfamily A |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: ABC transporters in lipid homeostasis; ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWZ7](https://www.uniprot.org/uniprotkb/Q8WWZ7) (Cholesterol transporter ABCA5):

> Cholesterol efflux transporter in macrophages that is responsible for APOAI/high-density lipoproteins (HDL) formation at the plasma membrane under high cholesterol levels and participates in reverse cholesterol transport. May play a role in the processing of autolysosomes (By similarity).

**Summary**, from NCBI Gene [23461](https://www.ncbi.nlm.nih.gov/gene/23461):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, and White). This encoded protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. This gene …

**Accessions** — [HGNC:35](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35) · Entrez [23461](https://www.ncbi.nlm.nih.gov/gene/23461) · UniProt [Q8WWZ7](https://www.uniprot.org/uniprotkb/Q8WWZ7) · Ensembl [ENSG00000154265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154265)

## Data

Gene col 7792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7792); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7792]; `tensor/DDL_lfc|DDL_z.npy` [7792]; `embed/gene_vectors.npy` [7792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7792 or target_col == 7792). Every well: [[ABCA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
