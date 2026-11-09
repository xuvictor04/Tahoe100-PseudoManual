---
symbol: "PCCA"
type: "gene"
col: 10579
ensembl_id: "ENSG00000175198"
name: "propionyl-CoA carboxylase subunit alpha"
location: "13q32.3"
module: 17
arm: "+"
pooled_cpm: 205.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PCCA

*propionyl-CoA carboxylase subunit alpha* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.02× (z +15.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.404× (z -18.9, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.654× (z -8.0, q 2e-13, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX8]] (+0.68, fdr 3e-05), [[MNAT1]] (+0.59, fdr 4e-05), [[SLC2A4RG]] (+0.58, fdr 4e-04); moves opposite to [[MAEA]] (-0.55, fdr 1e-04), [[SYCE2]] (-0.49, fdr 5e-05), [[SPON1-AS1]] (-0.48, fdr 8e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +15.2 | 0e+00 | 48/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +12.8 | 7e-35 | 47/48 (AsPC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +10.1 | 7e-22 | 45/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.58×** | +10.0 | 2e-21 | 47/49 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.29×** | +7.8 | 5e-13 | 31/48 (PANC-1, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +7.5 | 4e-12 | 29/48 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +7.3 | 3e-11 | 43/48 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +7.1 | 1e-10 | 40/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +5.7 | 6e-07 | 26/48 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.2 | 1e-05 | 31/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.2 | 1e-05 | 40/49 (AsPC-1, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.029 | 19/49 (J82, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.087 | 9/48 (A498, SW 1088, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -18.9 | 0e+00 | 40/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -16.2 | 0e+00 | 42/49 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -14.8 | 0e+00 | 45/47 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -11.0 | 4e-26 | 36/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -8.0 | 2e-13 | 43/48 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.711×** | -7.4 | 1e-11 | 37/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -7.3 | 2e-11 | 32/48 (AN3 CA, HCT15, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -6.9 | 3e-10 | 27/49 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.858× | -4.6 | 2e-04 | 14/49 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -4.3 | 9e-04 | 0/50 | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.816×** | -3.8 | 0.006 | 22/47 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.834× | -3.8 | 0.006 | 19/48 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -3.6 | 0.014 | 20/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.848× | -3.3 | 0.040 | 19/48 (SW 900, RKO, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.860× | -3.1 | 0.066 | 19/48 (HOP62, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 138 | 5 (2 ⚠) | 5 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.99× (z +15.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.15× (z +12.0) | [[Docetaxel (drug)]] 0.05 µM 0.408× (z -14.2) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.527× (z -10.2) |
| [[SW1417 (line)]] | alt | 181 | 6 (2 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.89× (z +12.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.38× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 526 | 7 (4 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.17× (z +17.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.67× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.487× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 86.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +17.0) | — |
| [[Hs 766T (line)]] | wt | 260 | 2 | 6 (5 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.24× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.504× (z -8.6) |
| [[KATO III (line)]] | alt | 219 | 3 (1 ⚠) | 5 (4 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.01× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -16.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 168 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -13.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 218 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -14.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 158 | 2 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.97× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 272 | 2 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.97× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 126 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.487× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 219 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -8.8) |
| [[RKO (line)]] | wt | 124 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -13.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 204 | 1 | 5 (4 ⚠) | [[Selinexor (drug)]] 0.05 µM 1.96× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.5) |
| [[SNU-423 (line)]] | alt | 221 | 2 | 4 (4 ⚠) | [[Selinexor (drug)]] 0.05 µM 1.86× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -17.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 458 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.74× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -16.5) |
| [[A549 (line)]] | wt | 158 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -16.2) |
| [[HT-29 (line)]] | alt | 351 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.425× (z -8.5) |
| [[A-172 (line)]] | wt | 239 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -20.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 404 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.289× (z -11.1) |
| [[C-33 A (line)]] | alt | 99.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.08× (z +10.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.53× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 223 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.318× (z -13.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.5) |
| [[HCT15 (line)]] | alt | 222 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 157 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.559× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 105 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -9.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 90.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.9) | — |
| [[SHP-77 (line)]] | alt | 650 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -18.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 155 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 341 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -14.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 222 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 105 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 95.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 237 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.23× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 138 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -16.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.515× (z -8.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 252 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 305 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 109 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.458× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 126 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -24.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 415 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.5) |
| [[H4 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -15.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 203 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX8]] | +0.68 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[MNAT1]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SLC2A4RG]] | +0.58 | +0.26 / +0.66 | both halves | 4e-04 |  |
| [[NDUFB10]] | +0.57 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[ZCRB1]] | +0.57 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[CLN8-AS1]] | +0.56 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[DYNC2H1]] | +0.53 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[UVRAG]] | +0.53 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CAPN5]] | +0.53 | +0.26 / +0.54 | both halves | 4e-04 |  |
| [[SCRN2]] | +0.52 | +0.25 / +0.44 | both halves | 4e-04 |  |
| [[DNAJC19]] | +0.52 | +0.22 / +0.50 | both halves | 6e-04 |  |
| [[DENND4C]] | +0.52 | +0.41 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAEA]] | -0.55 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[SYCE2]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SPON1-AS1]] | -0.48 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ADCY10P1]] | -0.48 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[SLC9A5]] | -0.48 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[CCDC168]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RIPK1]] | -0.47 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[SECISBP2]] | -0.47 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[ZNF546]] | -0.47 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[IDI2-AS1]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[DIDO1]] | -0.46 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[KLRA1P]] | -0.46 | -0.32 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.4, 26.0); signed map (-21.4, -12.0). **Vector** length 116, 40.3% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +9.4 | +7.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +9.3 | +7.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.9 | +10.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.4 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.4 | +0.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.6 | -14.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.7 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | +0.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | propionyl-CoA carboxylase subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:100,089,015-100,530,437 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Propionyl-CoA carboxylase subunits; ATP-grasp fold containing |
| Reactome | 11 pathways, smallest: Propionyl-CoA catabolism; Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P05165](https://www.uniprot.org/uniprotkb/P05165) (Propionyl-CoA carboxylase alpha chain, mitochondrial):

> This is one of the 2 subunits of the biotin-dependent propionyl-CoA carboxylase (PCC), a mitochondrial enzyme involved in the catabolism of odd chain fatty acids, branched-chain amino acids isoleucine, threonine, methionine, and valine and other metabolites. Propionyl-CoA carboxylase catalyzes the carboxylation of propionyl-CoA/propanoyl-CoA to D-methylmalonyl-CoA/(S)-methylmalonyl-CoA. Within the holoenzyme, the alpha subunit catalyzes the ATP-dependent carboxylation of the biotin carried by …

**Summary**, from NCBI Gene [5095](https://www.ncbi.nlm.nih.gov/gene/5095):

> The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:8653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8653) · Entrez [5095](https://www.ncbi.nlm.nih.gov/gene/5095) · UniProt [P05165](https://www.uniprot.org/uniprotkb/P05165) · Ensembl [ENSG00000175198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175198)

## Data

Gene col 10579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10579); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10579]; `tensor/DDL_lfc|DDL_z.npy` [10579]; `embed/gene_vectors.npy` [10579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10579 or target_col == 10579). Every well: [[PCCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
