---
symbol: "MAST3"
type: "gene"
col: 1792
ensembl_id: "ENSG00000099308"
name: "microtubule associated serine/threonine kinase 3"
location: "19p13.11"
module: 85
arm: "+"
pooled_cpm: 13.09
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 36
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# MAST3

*microtubule associated serine/threonine kinase 3* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 5.20× (z +26.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.369× (z -16.0, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.79, fdr 1e-05), [[FBXL16]] (+0.76, fdr 1e-05), [[ANKRD27]] (+0.74, fdr 3e-05); moves opposite to [[PBLD]] (-0.81, fdr 1e-05), [[PKN2-AS1]] (-0.76, fdr 4e-05), [[MMADHC-DT]] (-0.76, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **5.20×** | +26.5 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.09×** | +26.1 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.83×** | +21.5 | 0e+00 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +11.0 | 3e-26 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +10.9 | 1e-25 | 40/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +7.5 | 8e-12 | 37/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 2e-10 | 26/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.6 | 2e-09 | 26/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.31×** | +4.3 | 0.001 | 12/48 (NCI-H2347, HS-578T, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.31×** | +4.2 | 0.001 | 11/47 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.5 | 0.021 | 16/48 (A498, H4, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.068 | 7/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +3.1 | 0.089 | 10/47 (NCI-H1573, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.369×** | -16.0 | 0e+00 | 37/47 (CFPAC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -14.7 | 0e+00 | 37/47 (Panc 03.27, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.562×** | -13.1 | 1e-36 | 31/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.439×** | -12.7 | 1e-34 | 32/47 (A-172, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.497×** | -11.2 | 5e-27 | 34/48 (SNU-423, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.526×** | -10.3 | 9e-23 | 31/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -9.8 | 6e-21 | 28/46 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.543×** | -9.8 | 1e-20 | 29/41 (Panc 03.27, NCI-H460, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -9.3 | 6e-19 | 28/47 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.572×** | -8.3 | 8e-15 | 19/33 (NCI-H2030, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -8.2 | 2e-14 | 27/48 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.610×** | -7.6 | 1e-12 | 13/24 (SW1417, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -7.6 | 2e-12 | 25/44 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.629×** | -7.4 | 5e-12 | 26/47 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.735×** | -7.0 | 1e-10 | 24/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -6.6 | 1e-09 | 26/47 (LS 180, A-427, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -5.2 | 5e-06 | 19/45 (SNU-423, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.732×** | -5.0 | 2e-05 | 19/48 (SW48, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.0 | 0.002 | 14/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.783×** | -3.7 | 0.004 | 12/47 (CFPAC-1, HT-29, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.5 | 0.009 | 11/45 (H4, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.014 | 15/47 (LS 180, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.802×** | -3.4 | 0.016 | 8/48 (MIA PaCa-2, AN3 CA, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.2 | 2 | 8 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.77× (z +10.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.42× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -12.3) |
| [[PANC-1 (line)]] | alt | 12.4 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.307× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 23.9 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.64× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0800× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 7.03 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 8.93× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.184× (z -9.6) |
| [[A498 (line)]] | wt | 19.6 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.233× (z -11.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 9.20 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.28× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0842× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 15.7 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -10.9) |
| [[LoVo (line)]] | wt | 11.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.58× (z +9.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -10.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 17.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.07× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -9.9) |
| [[SNU-423 (line)]] | alt | 12.4 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 8.69× (z +11.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0793× (z -12.8) |
| [[HOP62 (line)]] | alt | 7.78 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 9.15× (z +11.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0561× (z -13.9) |
| [[Hs 766T (line)]] | wt | 10.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.67× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -14.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.75 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 13.2× (z +9.0) | [[Vilanterol (drug)]] 0.5 µM 0.0856× (z -8.6) |
| [[KATO III (line)]] | alt | 5.84 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 8.77 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.144× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 8.86 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 8.93× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.0924× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW1417 (line)]] | alt | 18.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 11.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.25× (z +15.6) | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.9) |
| [[A549 (line)]] | wt | 8.22 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.52× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 9.57 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.85× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -9.8) |
| [[H4 (line)]] | wt | 13.4 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0584× (z -9.9) |
| [[HS-578T (line)]] | alt | 13.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.36× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 14.0 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.52× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 7.27 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.37× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -8.8) |
| [[RKO (line)]] | wt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0618× (z -11.8) |
| [[SHP-77 (line)]] | alt | 13.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.97× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 2 (1 ⚠) | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0747× (z -10.1) |
| [[SW48 (line)]] | wt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -11.6) |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -10.3) |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0595× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.79 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[FBXL16]] | +0.76 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.74 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[FCHO1]] | +0.74 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.73 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.72 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.72 | +0.60 / +0.30 | both halves | 2e-04 |  |
| [[FAM118A]] | +0.72 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CABLES2]] | +0.71 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[DOK4]] | +0.71 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[KLHL26]] | +0.71 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[LRFN3]] | +0.71 | +0.63 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | -0.81 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | -0.76 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | -0.76 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | -0.74 | -0.67 / -0.20 | both halves | 7e-04 |  |
| [[MCTS1]] | -0.74 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.74 | -0.68 / -0.33 | both halves | 1e-04 |  |
| [[MZF1-AS1]] | -0.73 | -0.66 / -0.31 | both halves | 2e-04 |  |
| [[RFX3-DT]] | -0.73 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | -0.73 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.72 | -0.66 / -0.21 | both halves | 6e-04 |  |
| [[ZNF337-AS1]] | -0.72 | -0.66 / -0.21 | both halves | 7e-04 |  |
| [[PPP3CB-AS1]] | -0.72 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAST3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MAST3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MAST3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.880). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.4, -1.6); signed map (-39.5, -4.6). **Vector** length 96.5, 23.2% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.4 | +26.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.8 | +26.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.4 | +21.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +10.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +7.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.5 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -14.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -16.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.2 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated serine/threonine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,097,778-18,151,692 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0561 |
| Gene groups (HGNC) | PDZ domain containing; Microtubule associated serine/threonine kinase family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [O60307](https://www.uniprot.org/uniprotkb/O60307) (Microtubule-associated serine/threonine-protein kinase 3):

> Serine/threonine kinase that phosphorylates ARPP19 at 'Ser-62', resulting in protein phosphatase 2A (PP2A) inhibition by ARPP19.

**Summary**, from NCBI Gene [23031](https://www.ncbi.nlm.nih.gov/gene/23031):

> Predicted to enable protein serine/threonine kinase activity. Predicted to be involved in cytoskeleton organization and intracellular signal transduction. Predicted to be located in cytoplasm. Predicted to be active in microtubule cytoskeleton. Implicated in developmental and epileptic encephalopathy 108. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19036) · Entrez [23031](https://www.ncbi.nlm.nih.gov/gene/23031) · UniProt [O60307](https://www.uniprot.org/uniprotkb/O60307) · Ensembl [ENSG00000099308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099308)

## Data

Gene col 1792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1792); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1792]; `tensor/DDL_lfc|DDL_z.npy` [1792]; `embed/gene_vectors.npy` [1792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1792 or target_col == 1792). Every well: [[MAST3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAST3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
