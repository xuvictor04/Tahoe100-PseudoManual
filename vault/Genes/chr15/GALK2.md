---
symbol: "GALK2"
type: "gene"
col: 8026
ensembl_id: "ENSG00000156958"
name: "galactokinase 2"
location: "15q21.1-q21.2"
module: 118
arm: "+"
pooled_cpm: 93.1
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 26
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# GALK2

*galactokinase 2* — 15q21.1-q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +10.1, q 4e-21, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.488× (z -11.3, q 9e-27, down in 40 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.695× (z -5.7, q 6e-07, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1HASP]] (+0.65, fdr 1e-05), [[PRPF18]] (+0.63, fdr 6e-05), [[TBCK]] (+0.63, fdr 7e-06); moves opposite to [[DNMT3B]] (-0.58, fdr 5e-05), [[NCK2]] (-0.55, fdr 3e-05), [[FAM20B]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +10.1 | 4e-21 | 44/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.0 | 6e-17 | 37/49 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.0 | 6e-17 | 43/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +8.1 | 5e-14 | 37/48 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +7.4 | 2e-11 | 37/48 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.6 | 3e-09 | 34/50 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.29×** | +5.7 | 1e-06 | 30/48 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.5 | 2e-06 | 39/48 (A-172, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.9 | 6e-05 | 28/48 (SW1417, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 7e-04 | 32/48 (A-172, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 29/47 (SW480, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +3.6 | 0.017 | 24/50 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.021 | 27/48 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.029 | 22/48 (KATO III, H4, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.4 | 0.029 | 15/48 (Panc 03.27, A-427, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.030 | 24/50 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.040 | 18/49 (NCI-H1792, NCI-H1573, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.488×** | -11.3 | 9e-27 | 40/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.510×** | -10.2 | 8e-22 | 42/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.572×** | -8.8 | 3e-16 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -8.0 | 2e-13 | 33/44 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.612×** | -7.7 | 1e-12 | 35/49 (NCI-H23, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.626×** | -7.4 | 2e-11 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.645×** | -6.9 | 4e-10 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.648×** | -6.6 | 4e-09 | 31/42 (A-427, NCI-H23, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -5.7 | 6e-07 | 33/48 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -4.9 | 4e-05 | 30/47 (COLO 205, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.727×** | -4.8 | 8e-05 | 24/48 (A549, NCI-H460, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.572×** | -4.6 | 2e-04 | 22/37 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.588×** | -4.4 | 6e-04 | 28/45 (C-33 A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -4.3 | 9e-04 | 23/49 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.7 | 0.007 | 24/48 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.008 | 26/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.801×** | -3.5 | 0.016 | 25/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.019 | 22/48 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.048 | 20/47 (HT-29, H4, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.686×** | -3.1 | 0.053 | 20/48 (SW480, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.817×** | -3.1 | 0.057 | 21/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.765×** | -3.0 | 0.065 | 16/49 (Hs 766T, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.828×** | -3.0 | 0.065 | 18/48 (NCI-H2030, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 106 | 2 | 9 (9 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.231× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 104 | 2 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.301× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 172 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 108 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.316× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 89.9 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 88.9 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -14.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 68.5 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 63.9 | 3 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -10.2) ⚠ toxic |
| [[J82 (line)]] | alt | 54.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.39× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.314× (z -10.9) |
| [[KATO III (line)]] | alt | 134 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 139 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.106× (z -12.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 75.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 56.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 69.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 198 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.328× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.248× (z -11.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.320× (z -9.9) |
| [[HS-578T (line)]] | alt | 42.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +11.3) | — |
| [[RKO (line)]] | wt | 116 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -9.6) ⚠ toxic |
| [[A498 (line)]] | wt | 114 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 54.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.9) | — |
| [[H4 (line)]] | wt | 90.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Hs 766T (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SHP-77 (line)]] | alt | 87.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 95.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 71.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -10.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.34× (z +8.5) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[CFPAC-1 (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HepG2_C3A (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.124× (z -9.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 94.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 94.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.29× (z +10.4) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[SW48 (line)]] | wt | 56.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 78.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1HASP]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PRPF18]] | +0.63 | +0.71 / +0.38 | both halves | 6e-05 |  |
| [[TBCK]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SYNRG]] | +0.58 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[BET1]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[KIAA0319L]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TOGARAM1]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DNASE1]] | +0.54 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[MBD5]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[USP49]] | +0.53 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[UBE3B]] | +0.52 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[NIFK-AS1]] | +0.52 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT3B]] | -0.58 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[NCK2]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[GPRIN1]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TRAK1]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PRR5]] | -0.52 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[RASGEF1C]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[UNC5A]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ARHGAP8]] | -0.49 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[ZDHHC18]] | -0.48 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[RAP1GAP2]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[FAM124A]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GALK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MGC4859]] | B | MGC4859 activity raises GALK2's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without MGC4859 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[LINC00640]] | C | LINC00640 activity raises GALK2's level | lines that do not express LINC00640 (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without LINC00640 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-20.6, 30.9); signed map (-3.4, -3.5). **Vector** length 85.2, 27.3% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +0.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +4.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.8 | -6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.8 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.2 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | galactokinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1-q21.2 — chr15:49,155,656-49,367,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GK2 |
| Gene groups (HGNC) | Galactokinase family |
| Hallmark sets | GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01415](https://www.uniprot.org/uniprotkb/Q01415) (N-acetylgalactosamine kinase):

> Catalyzes the ATP-dependent phosphorylation of N-acetyl-D-galactosamine (GalNAc) to GalNAc 1-phosphate. Exhibits very low galactokinase activity in vitro.

**Summary**, from NCBI Gene [2585](https://www.ncbi.nlm.nih.gov/gene/2585):

> This gene encodes a highly efficient N-acetylgalactosamine (GalNAc) kinase, which has galactokinase activity when galactose is present at high concentrations. The encoded protein is a member of the GHMP kinase family. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:4119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4119) · Entrez [2585](https://www.ncbi.nlm.nih.gov/gene/2585) · UniProt [Q01415](https://www.uniprot.org/uniprotkb/Q01415) · Ensembl [ENSG00000156958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156958)

## Data

Gene col 8026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8026); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8026]; `tensor/DDL_lfc|DDL_z.npy` [8026]; `embed/gene_vectors.npy` [8026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8026 or target_col == 8026). Every well: [[GALK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
