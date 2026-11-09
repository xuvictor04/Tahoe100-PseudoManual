---
symbol: "NLN"
type: "gene"
col: 4417
ensembl_id: "ENSG00000123213"
name: "neurolysin"
location: "5q12.3"
module: 18
arm: "+"
pooled_cpm: 85.11
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NLN

*neurolysin* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.39× (z +9.7, q 1e-19, up in 33 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.16× (z +6.2, q 7e-08, up in 18 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.304× (z -50.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARNL3]] (+0.72, fdr 7e-06), [[RAP1GDS1]] (+0.72, fdr 7e-06), [[PUS7]] (+0.67, fdr 7e-06); moves opposite to [[TNFRSF14]] (-0.56, fdr 1e-05), [[FMO4]] (-0.54, fdr 3e-05), [[KMT2E]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +9.7 | 1e-19 | 33/48 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +7.5 | 2e-11 | 25/44 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +7.4 | 4e-11 | 25/48 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +6.2 | 7e-08 | 18/49 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +5.7 | 1e-06 | 21/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +4.9 | 8e-05 | 21/48 (BT-474, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.6 | 4e-04 | 14/48 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.16× | +4.5 | 4e-04 | 13/47 (BT-474, Panc 03.27, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.17× | +4.5 | 5e-04 | 18/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.16× | +4.4 | 5e-04 | 12/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.33×** | +4.4 | 6e-04 | 12/46 (hTERT-HPNE, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +4.3 | 7e-04 | 20/47 (BT-474, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 13/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.10× | +4.0 | 0.003 | 5/48 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.9 | 0.004 | 5/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.009 | 15/47 (BT-474, Panc 03.27, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.013 | 6/48 (HCT15, NCI-H2030, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.08× | +3.4 | 0.018 | 3/48 (A549, hTERT-HPNE, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.12× | +3.4 | 0.021 | 13/48 (SNU-423, LOX-IMVI, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.023 | 14/48 (MIA PaCa-2, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.026 | 12/48 (BT-474, COLO 205, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.031 | 11/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.304×** | -50.1 | 0e+00 | 47/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.420×** | -24.8 | 0e+00 | 44/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.306×** | -18.4 | 0e+00 | 45/49 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -16.5 | 0e+00 | 37/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -15.9 | 0e+00 | 38/48 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -14.2 | 7e-44 | 32/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -11.5 | 1e-28 | 34/48 (SNU-1, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -9.7 | 3e-20 | 31/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.758×** | -7.9 | 2e-13 | 27/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -7.4 | 8e-12 | 25/48 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.784×** | -7.2 | 2e-11 | 23/48 (C-33 A, BT-474, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.858× | -6.4 | 6e-09 | 16/48 (A498, J82, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.664×** | -6.4 | 8e-09 | 21/47 (RKO, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.820×** | -5.7 | 6e-07 | 23/47 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -4.0 | 0.002 | 12/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.911× | -3.9 | 0.003 | 6/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.887× | -3.3 | 0.026 | 7/47 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 0.5 µM |  | 0.898× | -3.2 | 0.036 | 7/49 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.895× | -3.1 | 0.039 | 15/47 (SW48, HCT15, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.896× | -3.1 | 0.039 | 13/48 (AN3 CA, CHP-212, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.899× | -3.0 | 0.056 | 5/49 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 178 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -25.2) |
| [[HEC-1-A (line)]] | alt | 81.8 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -28.3) |
| [[LoVo (line)]] | wt | 63.7 | 3 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.10× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 118 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -24.6) |
| [[PANC-1 (line)]] | alt | 147 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -31.3) |
| [[MIA PaCa-2 (line)]] | alt | 168 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -30.2) |
| [[RKO (line)]] | wt | 83.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -24.5) |
| [[HS-578T (line)]] | alt | 99.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -21.7) |
| [[J82 (line)]] | alt | 133 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -27.7) |
| [[A-172 (line)]] | wt | 116 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -16.6) |
| [[A498 (line)]] | wt | 108 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -28.5) |
| [[SNU-1 (line)]] | wt | 89.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0770× (z -19.1) |
| [[SW48 (line)]] | wt | 86.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.5) |
| [[AN3 CA (line)]] | alt | 169 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0716× (z -26.8) |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -17.5) |
| [[C-33 A (line)]] | alt | 125 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.4) |
| [[H4 (line)]] | wt | 99.5 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0790× (z -11.7) |
| [[HOP62 (line)]] | alt | 28.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.5) |
| [[HT-29 (line)]] | alt | 33.6 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 58.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 92.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 60.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -19.6) |
| [[A549 (line)]] | wt | 111 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -15.2) |
| [[BT-474 (line)]] | alt | 82.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.3) |
| [[C32 (line)]] | wt | 42.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.2) |
| [[Hs 766T (line)]] | wt | 42.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 79.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -25.2) |
| [[LS 180 (line)]] | wt | 50.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -17.2) |
| [[NCI-H2347 (line)]] | alt | 85.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 47.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.9) |
| [[SNU-423 (line)]] | alt | 63.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.4) |
| [[SW 1088 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.213× (z -8.6) |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.7) |
| [[SW480 (line)]] | alt | 90.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -21.0) |
| [[CFPAC-1 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +11.7) | — |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -8.8) |
| [[HCT15 (line)]] | alt | 72.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.6) |
| [[KATO III (line)]] | alt | 48.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.3) |
| [[SW 900 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.30× (z +8.7) ⚠ unreliable plate only | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARNL3]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[RAP1GDS1]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PUS7]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ABCC4]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[DKC1]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SHLD2]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MPP3]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SUPT3H]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PUM3]] | +0.61 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[POLR3E]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF14]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FMO4]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[KMT2E]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HNMT]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[EFNA1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[C4orf33]] | -0.52 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[BCL3]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises NLN's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without ADCY3 | 0.037 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ABCA3]] | B | ABCA3 activity raises NLN's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.71× lower at baseline in the lines without ABCA3 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[TNFRSF14]] | B | TNFRSF14 activity lowers NLN's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 1.75× higher at baseline in the lines without TNFRSF14 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.7, -35.7); signed map (-4.1, -53.1). **Vector** length 133, 41.2% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.2 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.0 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.7 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.4 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -50.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -18.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -24.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | -4.3 | -3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -7.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.6 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | neurolysin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,722,205-65,871,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1226; previously AGTBP |
| Gene groups (HGNC) | M3 metallopeptidase family |
| Reactome | 4 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYT8](https://www.uniprot.org/uniprotkb/Q9BYT8) (Neurolysin, mitochondrial):

> Hydrolyzes oligopeptides such as neurotensin, bradykinin and dynorphin A (By similarity). Acts as a regulator of cannabinoid signaling pathway by mediating degradation of hemopressin, an antagonist peptide of the cannabinoid receptor CNR1 (By similarity).

**Summary**, from NCBI Gene [57486](https://www.ncbi.nlm.nih.gov/gene/57486):

> This gene encodes a member of the metallopeptidase M3 protein family that cleaves neurotensin at the Pro10-Tyr11 bond, leading to the formation of neurotensin(1-10) and neurotensin(11-13). The encoded protein is likely involved in the termination of the neurotensinergic signal in the central nervous system and in the gastrointestinal tract.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:16058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16058) · Entrez [57486](https://www.ncbi.nlm.nih.gov/gene/57486) · UniProt [Q9BYT8](https://www.uniprot.org/uniprotkb/Q9BYT8) · Ensembl [ENSG00000123213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123213)

## Data

Gene col 4417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4417); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4417]; `tensor/DDL_lfc|DDL_z.npy` [4417]; `embed/gene_vectors.npy` [4417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4417 or target_col == 4417). Every well: [[NLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
