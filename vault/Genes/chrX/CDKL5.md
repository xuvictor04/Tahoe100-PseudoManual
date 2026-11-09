---
symbol: "CDKL5"
type: "gene"
col: 159
ensembl_id: "ENSG00000008086"
name: "cyclin dependent kinase like 5"
location: "Xp22.13"
module: 5
arm: "-"
pooled_cpm: 54.44
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 26
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CDKL5

*cyclin dependent kinase like 5* — Xp22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.31× (z +14.1, q 2e-42, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.409× (z -15.1, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.492× (z -12.0, q 5e-31, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHOC2]] (+0.65, fdr 7e-06), [[WDR44]] (+0.55, fdr 5e-05), [[DLGAP4]] (+0.54, fdr 3e-05); moves opposite to [[TGFBRAP1]] (-0.61, fdr 1e-05), [[FUT10]] (-0.57, fdr 2e-05), [[PEX26]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[XKR9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +14.1 | 2e-42 | 44/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +13.4 | 1e-38 | 33/46 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +12.0 | 5e-31 | 41/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +10.6 | 4e-24 | 36/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +7.4 | 2e-11 | 26/45 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +6.8 | 1e-09 | 29/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.7 | 9e-07 | 25/45 (SW1417, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.1 | 3e-05 | 22/46 (SW1417, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 24/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.5 | 3e-04 | 21/44 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +4.4 | 6e-04 | 22/46 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.003 | 15/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 20/44 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 20/44 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.006 | 15/46 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.017 | 15/47 (CFPAC-1, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -15.1 | 0e+00 | 41/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.420×** | -14.6 | 0e+00 | 37/43 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.403×** | -14.2 | 2e-43 | 35/40 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.447×** | -13.1 | 6e-37 | 30/37 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.492×** | -12.0 | 5e-31 | 41/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.505×** | -11.6 | 7e-29 | 34/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -10.0 | 1e-21 | 32/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.597×** | -8.7 | 2e-16 | 31/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -8.4 | 3e-15 | 36/46 (A-172, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -8.2 | 1e-14 | 35/44 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -8.1 | 3e-14 | 34/45 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -7.6 | 1e-12 | 33/45 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -7.3 | 2e-11 | 24/43 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.441×** | -7.2 | 2e-11 | 22/32 (HOP62, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.469×** | -6.7 | 9e-10 | 28/45 (NCI-H2347, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.742×** | -4.7 | 7e-05 | 24/45 (NCI-H2347, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.584×** | -4.7 | 7e-05 | 26/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.634×** | -4.0 | 0.001 | 19/45 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.005 | 13/45 (SW 1271, HOP62, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.829×** | -3.0 | 0.059 | 13/45 (NCI-H23, NCI-H2347, …) | all doses, flat |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.835× | -2.9 | 0.070 | 10/46 (HOP62, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 101 | 15 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.48× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 49.5 | 7 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.82× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 132 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -29.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.254× (z -14.4) |
| [[A-172 (line)]] | wt | 47.8 | 4 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.383× (z -9.5) |
| [[SW1417 (line)]] | alt | 46.3 | 7 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.58× (z +17.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -12.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 92.7 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 73.1 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.278× (z -10.0) |
| [[HOP62 (line)]] | alt | 44.2 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -10.0) |
| [[LS 180 (line)]] | wt | 38.8 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0765× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 87.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -16.4) |
| [[SNU-423 (line)]] | alt | 74.0 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -13.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 46.6 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.345× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 86.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -15.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -15.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 57.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -14.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.5) | [[Docetaxel (drug)]] 0.05 µM 0.227× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 13.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.96× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.141× (z -8.7) |
| [[A-427 (line)]] | wt | 42.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -15.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -15.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.114× (z -10.8) |
| [[BT-474 (line)]] | alt | 47.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.3) | [[Auranofin (drug)]] 5 µM 0.311× (z -8.7) |
| [[C-33 A (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -14.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 37.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -13.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -20.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 34.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 48.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 47.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -12.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 44.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.4 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0757× (z -9.5) |
| [[COLO 205 (line)]] | alt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 92.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0678× (z -8.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -15.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHOC2]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[WDR44]] | +0.55 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[DLGAP4]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[H3-3B]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ITSN1]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[DAAM1]] | +0.51 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[RAB33B]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[STX12]] | +0.51 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CHCHD7]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[IRF7]] | +0.50 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ZRANB1]] | +0.50 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[CDK2AP2]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBRAP1]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[FUT10]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PEX26]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[NUP210]] | -0.55 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[XYLB]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CNTNAP3P2]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CNNM1]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TFAP4]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TCERG1]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[TMEM33]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[RAD51D]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZP3]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR9]] | B | XKR9 activity raises CDKL5's level | lines that do not express XKR9 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without XKR9 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000285579; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CDKL5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.9, 3.0); signed map (-14.7, 18.7). **Vector** length 86.8, 22.4% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.3 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.6 | -1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.2 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.13 — chrX:18,425,583-18,653,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIEE2, CFAP247; previously STK9 |
| Gene groups (HGNC) | Cilia and flagella associated; Cyclin dependent kinase like family |
| Matched by | ensembl_id |

**Function**, from UniProt [O76039](https://www.uniprot.org/uniprotkb/O76039) (Cyclin-dependent kinase-like 5):

> Serine/threonine-protein kinase involved in neuronal development and function that phosphorylates its substrates exclusively on serine, within an R-P-x-S-A consensus motif. Phosphorylates microtubule-associated proteins (MAP1S, MAPRE2/EB2, ARHGEF2) to regulate microtubule dynamics and centrosome/midbody function and the synaptic adhesion molecule LRRC4C/NGL-1 to promote dendritic spine formation. Recruited to sites of transcription-coupled DNA damage, where it phosphorylates ELOA, contributing …

**Summary**, from NCBI Gene [6792](https://www.ncbi.nlm.nih.gov/gene/6792):

> This gene is a member of Ser/Thr protein kinase family and encodes a phosphorylated protein with protein kinase activity. Mutations in this gene have been associated with X-linked infantile spasm syndrome (ISSX), also known as X-linked West syndrome, and Rett syndrome (RTT). Alternate transcriptional splice variants have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11411) · Entrez [6792](https://www.ncbi.nlm.nih.gov/gene/6792) · UniProt [O76039](https://www.uniprot.org/uniprotkb/O76039) · Ensembl [ENSG00000008086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008086)

## Data

Gene col 159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 159); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 159]; `tensor/DDL_lfc|DDL_z.npy` [159]; `embed/gene_vectors.npy` [159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 159 or target_col == 159). Every well: [[CDKL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
