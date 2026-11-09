---
symbol: "MAP3K14"
type: "gene"
col: 102
ensembl_id: "ENSG00000006062"
name: "mitogen-activated protein kinase kinase kinase 14"
location: "17q21.31"
module: 162
arm: "+"
pooled_cpm: 73.11
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# MAP3K14

*mitogen-activated protein kinase kinase kinase 14* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +21.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.499× (z -10.0, q 1e-20, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.654× (z -8.6, q 2e-15, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP3]] (+0.63, fdr 1e-05), [[DUSP2]] (+0.62, fdr 2e-05), [[EGR2]] (+0.61, fdr 7e-06); moves opposite to [[LINC02680]] (-0.56, fdr 4e-05), [[CIAO2A]] (-0.55, fdr 5e-05), [[ORMDL1]] (-0.55, fdr 6e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +21.3 | 0e+00 | 45/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +13.0 | 5e-36 | 42/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +12.9 | 5e-36 | 42/48 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +12.0 | 8e-31 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +10.6 | 4e-24 | 40/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +8.7 | 2e-16 | 40/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.2 | 4e-08 | 29/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 1e-04 | 31/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.90×** | +4.8 | 1e-04 | 34/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.002 | 22/48 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 24/48 (HEC-1-A, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.499×** | -10.0 | 1e-20 | 39/49 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -9.8 | 3e-20 | 36/44 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.654×** | -8.6 | 2e-15 | 34/48 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -7.7 | 1e-12 | 33/44 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -7.5 | 6e-12 | 28/48 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -6.4 | 1e-08 | 28/47 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -5.8 | 6e-07 | 29/50 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -5.7 | 1e-06 | 28/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.695×** | -5.2 | 1e-05 | 34/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.773×** | -5.2 | 1e-05 | 25/49 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.724×** | -4.6 | 2e-04 | 29/48 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.726×** | -4.6 | 2e-04 | 27/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -4.5 | 3e-04 | 25/48 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.738×** | -4.2 | 0.001 | 27/48 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -3.6 | 0.011 | 25/48 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.847× | -3.4 | 0.027 | 16/48 (SW48, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.029 | 19/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.030 | 19/48 (A-172, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | 0.854× | -3.2 | 0.032 | 15/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.047 | 18/48 (hTERT-HPNE, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.807×** | -3.0 | 0.067 | 22/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.814×** | -2.9 | 0.067 | 16/48 (C-33 A, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 206 | 1 | 12 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 58.8 | 9 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +33.1) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -13.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 236 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0518× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 54.5 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0933× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.379× (z -12.4) |
| [[SNU-1 (line)]] | wt | 255 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -16.9) |
| [[NCI-H2347 (line)]] | alt | 22.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +22.6) | — |
| [[A-427 (line)]] | wt | 152 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 91.8 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -11.6) |
| [[KATO III (line)]] | alt | 52.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.0778× (z -19.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +16.3) | — |
| [[A549 (line)]] | wt | 67.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.7) | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +18.7) | — |
| [[CFPAC-1 (line)]] | alt | 61.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +25.9) | — |
| [[HOP62 (line)]] | alt | 75.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 90.3 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.399× (z -11.5) |
| [[A-172 (line)]] | wt | 88.3 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.81× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.2) |
| [[BT-474 (line)]] | alt | 52.5 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +15.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -12.0) |
| [[C32 (line)]] | wt | 50.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 99.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 140 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -13.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 87.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 69.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[IQ 1 (drug)]] 5 µM 0.0549× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 37.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 75.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 57.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.5) | [[Selinexor (drug)]] 0.5 µM 0.325× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 43.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 94.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.466× (z -8.9) |
| [[SW480 (line)]] | alt | 74.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +20.0) | — |
| [[COLO 205 (line)]] | alt | 43.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +19.7) | — |
| [[H4 (line)]] | wt | 56.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0648× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 52.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 73.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.447× (z -8.5) |
| [[SW 900 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +18.1) | — |
| [[LOX-IMVI (line)]] | wt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -10.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 54.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +14.2) | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP3]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[EGR2]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[VCL]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PILRB]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SPATA32]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 | ⚠ **readthrough risk**: SPATA32 lies 1.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[EGR3]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[NTMT1]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[IER2]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[EGR1]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CCDC57]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TRAF2]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 | pathway: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; STRING 995 |
| [[EML4]] | +0.56 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02680]] | -0.56 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.55 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ORMDL1]] | -0.55 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SAP30L-AS1]] | -0.53 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[SMPDL3A]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[HSPE1-MOB4]] | -0.52 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TMPRSS5]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NADSYN1]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CLCC1]] | -0.50 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[SH3BGR]] | -0.50 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[RAB18]] | -0.50 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[GARS1-DT]] | -0.49 | -0.41 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MAP3K14's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MAP3K14's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.5, -1.3); signed map (6.6, 29.8). **Vector** length 135, 43.1% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.7 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +21.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +10.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +13.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +8.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.5 | +2.1 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +1.1 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -11.5 | -8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.7 | -9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.5 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.9 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.7 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,263,119-45,317,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIK, HSNIK, FTDCR1B, HS |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE-unique family |
| Reactome | 12 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; CD28 dependent PI3K/Akt signaling; Co-stimulation by CD28 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99558](https://www.uniprot.org/uniprotkb/Q99558) (Mitogen-activated protein kinase kinase kinase 14):

> Lymphotoxin beta-activated kinase which seems to be exclusively involved in the activation of NF-kappa-B and its transcriptional activity. Phosphorylates CHUK/IKKA, thereby promoting proteolytic processing of NFKB2/P100, which leads to NF-kappa-B activation via the non-canonical pathway. Has an essential role in the non-canonical NF-kappa-B signaling that regulates genes encoding molecules involved in B-cell survival, lymphoid organogenesis, and immune response. Could act in a …

**Summary**, from NCBI Gene [9020](https://www.ncbi.nlm.nih.gov/gene/9020):

> This gene encodes mitogen-activated protein kinase kinase kinase 14, which is a serine/threonine protein-kinase. This kinase binds to TRAF2 and stimulates NF-kappaB activity. It shares sequence similarity with several other MAPKK kinases. It participates in an NF-kappaB-inducing signalling cascade common to receptors of the tumour-necrosis/nerve-growth factor (TNF/NGF) family and to the interleukin-1 type-I receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6853) · Entrez [9020](https://www.ncbi.nlm.nih.gov/gene/9020) · UniProt [Q99558](https://www.uniprot.org/uniprotkb/Q99558) · Ensembl [ENSG00000006062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006062)

## Data

Gene col 102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 102); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 102]; `tensor/DDL_lfc|DDL_z.npy` [102]; `embed/gene_vectors.npy` [102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 102 or target_col == 102). Every well: [[MAP3K14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
