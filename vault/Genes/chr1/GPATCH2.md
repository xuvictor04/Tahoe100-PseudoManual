---
symbol: "GPATCH2"
type: "gene"
col: 1716
ensembl_id: "ENSG00000092978"
name: "G-patch domain containing 2"
location: "1q41"
module: 26
arm: "+"
pooled_cpm: 96.27
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# GPATCH2

*G-patch domain containing 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +18.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.690× (z -7.0, q 1e-09, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.872× (z -3.9, q 0.016, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.175×, LS 180 0.287×, SK-MEL-2 0.332×, SHP-77 0.383×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 0.406×, LS 180 0.413×, HT-29 0.397×, LoVo 0.466×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.407×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0866×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FTX]] (+0.69, fdr 1e-05), [[NEK11]] (+0.69, fdr 1e-05), [[FBXO30]] (+0.65, fdr 3e-04); moves opposite to [[FOXO6]] (-0.65, fdr 7e-05), [[NRTN]] (-0.62, fdr 1e-04), [[CFD]] (-0.60, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +18.2 | 0e+00 | 47/48 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +15.0 | 0e+00 | 47/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +13.6 | 6e-40 | 46/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +13.5 | 4e-39 | 45/48 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +13.4 | 1e-38 | 44/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +12.5 | 6e-34 | 44/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +12.5 | 9e-34 | 46/48 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +10.7 | 1e-24 | 39/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.1 | 2e-22 | 42/50 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.60×** | +9.3 | 6e-19 | 42/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.35×** | +8.3 | 6e-15 | 38/48 (SNU-423, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +7.7 | 6e-13 | 39/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +7.5 | 4e-12 | 38/48 (SW480, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.77×** | +5.9 | 1e-07 | 37/45 (NCI-H1792, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.6 | 7e-07 | 29/48 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.4 | 2e-06 | 29/48 (C32, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.8 | 5e-05 | 32/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 3e-04 | 29/48 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.001 | 26/47 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1716.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.175×, LS 180 0.287×, SK-MEL-2 0.332×, SHP-77 0.383×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 0.406×, LS 180 0.413×, HT-29 0.397×, LoVo 0.466×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.407×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0866×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.690×** | -7.0 | 1e-09 | 37/49 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -6.9 | 2e-09 | 29/44 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.722×** | -6.5 | 2e-08 | 32/48 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.9 | 0.016 | 13/48 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | **0.831×** | -3.5 | 0.040 | 22/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.040 | 21/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.843× | -3.4 | 0.056 | 24/49 (SW 1088, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.889× | -3.3 | 0.064 | 16/49 (SNU-1, KATO III, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | 0.740× | -3.1 | 0.11 | 19/46 (KATO III, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.11 | 16/48 (PANC-1, NCI-H1792, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 169 | 6 | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.407× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 99.4 | 8 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.63× (z +15.4) | — |
| [[HEC-1-A (line)]] | alt | 101 | 5 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 117 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 131 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -20.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 96.5 | 6 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.30× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 66.1 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +15.9) | — |
| [[HS-578T (line)]] | alt | 76.5 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +12.6) | — |
| [[LoVo (line)]] | wt | 84.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 105 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +17.8) | — |
| [[NCI-H1792 (line)]] | alt | 75.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 80.5 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.7) | [[Lonafarnib (drug)]] 5 µM 0.177× (z -10.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 156 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +12.8) | — |
| [[SW480 (line)]] | alt | 94.5 | 5 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +14.5) | — |
| [[A-172 (line)]] | wt | 94.2 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.54× (z +9.4) | — |
| [[A498 (line)]] | wt | 118 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 79.8 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.5) | — |
| [[H4 (line)]] | wt | 68.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 102 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 84.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.2) | — |
| [[A-427 (line)]] | wt | 75.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 97.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 72.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.0) | — |
| [[RKO (line)]] | wt | 136 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 120 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 52.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.7) | — |
| [[A549 (line)]] | wt | 73.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 99.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 96.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 82.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 92.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 68.7 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.10× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 55.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -8.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 79.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.8) | — |
| [[J82 (line)]] | alt | 78.8 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[KATO III (line)]] | alt | 78.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0866× (z -10.4) |
| [[SW48 (line)]] | wt | 78.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTX]] | +0.69 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NEK11]] | +0.69 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FBXO30]] | +0.65 | +0.68 / +0.27 | both halves | 3e-04 |  |
| [[YIPF7]] | +0.64 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[ENOX2]] | +0.64 | +0.71 / +0.31 | both halves | 2e-04 |  |
| [[RCC1L]] | +0.63 | +0.61 / +0.29 | both halves | 3e-04 |  |
| [[CSTF3]] | +0.62 | +0.67 / +0.33 | both halves | 1e-04 |  |
| [[ATXN10]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[RNF6]] | +0.61 | +0.71 / +0.26 | both halves | 3e-04 |  |
| [[IREB2]] | +0.60 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[SLC38A6]] | +0.59 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PSMB6]] | +0.59 | +0.67 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO6]] | -0.65 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[NRTN]] | -0.62 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[CFD]] | -0.60 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[SLC66A2]] | -0.57 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[SLC25A23]] | -0.57 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[SMARCD3]] | -0.57 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[PADI2]] | -0.57 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ARRB2]] | -0.56 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[NOVA2]] | -0.56 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[HMGN3]] | -0.56 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[TNK2]] | -0.56 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[SEMA6B]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPATCH2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TP53]] | C | TP53 activity weakens GPATCH2's drug response | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | the TP53-altered lines respond 0.95× as strongly (z diff -0.18); strongest at Idarubicin (hydrochloride) 5 µM: 1.79x vs 1.45x (z diff -2.4) | 0.728 over the table, 0.047 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.5, 4.2); signed map (21.6, -26.0). **Vector** length 106, 33.8% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.8 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.5 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.4 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -7.2 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.7 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.2 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.2 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.8 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.2 | -1.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:217,426,992-217,631,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10252, CT110, PPP1R30, Pfa1; previously GPATC2 |
| Gene groups (HGNC) | G-patch domain containing; Protein phosphatase 1 regulatory subunits; SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NW75](https://www.uniprot.org/uniprotkb/Q9NW75) (G patch domain-containing protein 2):

> Enhances the ATPase activity of DHX15 in vitro.

**Summary**, from NCBI Gene [55105](https://www.ncbi.nlm.nih.gov/gene/55105):

> The gene encodes a nuclear factor that may play a role in spermatogenesis and in tumor growth during breast cancer. The encoded protein contains a G-patch domain with an RNA binding motif. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:25499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25499) · Entrez [55105](https://www.ncbi.nlm.nih.gov/gene/55105) · UniProt [Q9NW75](https://www.uniprot.org/uniprotkb/Q9NW75) · Ensembl [ENSG00000092978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092978)

## Data

Gene col 1716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1716); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1716]; `tensor/DDL_lfc|DDL_z.npy` [1716]; `embed/gene_vectors.npy` [1716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1716 or target_col == 1716). Every well: [[GPATCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
