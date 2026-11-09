---
symbol: "SRSF4"
type: "gene"
col: 3791
ensembl_id: "ENSG00000116350"
name: "serine and arginine rich splicing factor 4"
location: "1p35.3"
module: 51
arm: "+"
pooled_cpm: 203.39
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SRSF4

*serine and arginine rich splicing factor 4* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.38× (z +15.5, q 0e+00, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +15.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.390× (z -32.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF8]] (+0.69, fdr 7e-06), [[BAZ1B]] (+0.68, fdr 1e-05), [[ZNF644]] (+0.68, fdr 7e-06); moves opposite to [[PIGF]] (-0.55, fdr 4e-05), [[DHRS1]] (-0.53, fdr 4e-05), [[IDS]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +15.5 | 0e+00 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +15.2 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +11.6 | 1e-28 | 42/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +11.5 | 2e-28 | 38/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +10.7 | 1e-24 | 35/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +9.9 | 5e-21 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +9.6 | 5e-20 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +7.1 | 1e-10 | 27/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +6.5 | 7e-09 | 24/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.18× | +5.5 | 2e-06 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +5.2 | 1e-05 | 24/48 (H4, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.15× | +4.8 | 8e-05 | 16/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.11× | +3.6 | 0.012 | 7/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.07× | +3.4 | 0.027 | 3/48 (SNU-1, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.11× | +3.3 | 0.041 | 14/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.09× | +3.0 | 0.089 | 11/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.07× | +3.0 | 0.089 | 4/48 (hTERT-HPNE, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.390×** | -32.1 | 0e+00 | 48/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.453×** | -27.0 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -25.9 | 0e+00 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -24.7 | 0e+00 | 46/49 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.621×** | -16.3 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -15.2 | 0e+00 | 38/44 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.674×** | -13.5 | 2e-39 | 44/49 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -10.9 | 1e-25 | 34/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -10.3 | 5e-23 | 43/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.583×** | -9.6 | 3e-20 | 45/49 (SW480, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -9.2 | 1e-18 | 26/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.769×** | -8.6 | 3e-16 | 30/50 (HOP62, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.766×** | -8.3 | 4e-15 | 29/45 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -7.9 | 1e-13 | 34/48 (HOP62, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.860× | -7.3 | 9e-12 | 19/48 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.795×** | -6.4 | 5e-09 | 28/49 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -6.3 | 1e-08 | 17/48 (HOP62, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.878× | -4.3 | 6e-04 | 15/48 (HS-578T, C-33 A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.858× | -3.8 | 0.005 | 13/47 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.906× | -3.4 | 0.018 | 7/48 (A498, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 163 | 8 (5 ⚠) | 7 | [[Digitoxin (drug)]] 5 µM 2.39× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.25× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.351× (z -20.1) |
| [[HOP62 (line)]] | alt | 220 | 1 | 11 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.366× (z -20.3) |
| [[SW480 (line)]] | alt | 240 | 6 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.320× (z -26.8) |
| [[LoVo (line)]] | wt | 213 | 5 (2 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.351× (z -21.8) |
| [[HS-578T (line)]] | alt | 228 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -18.8) |
| [[J82 (line)]] | alt | 250 | 1 | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.319× (z -23.6) |
| [[LS 180 (line)]] | wt | 191 | 5 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.407× (z -15.7) |
| [[PANC-1 (line)]] | alt | 208 | 7 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.413× (z -20.5) |
| [[LOX-IMVI (line)]] | wt | 211 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 180 | 2 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.338× (z -19.2) |
| [[NCI-H2030 (line)]] | alt | 241 | 1 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.357× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 253 | 2 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.337× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 187 | 3 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.311× (z -21.5) |
| [[C-33 A (line)]] | alt | 424 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.409× (z -15.3) |
| [[KATO III (line)]] | alt | 180 | 3 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.376× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 156 | 1 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.353× (z -16.3) |
| [[SW1417 (line)]] | alt | 151 | 3 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.390× (z -17.0) |
| [[A-427 (line)]] | wt | 184 | 1 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.90× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.507× (z -12.4) |
| [[C32 (line)]] | wt | 218 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -13.6) |
| [[H4 (line)]] | wt | 172 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.465× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 160 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.397× (z -18.5) |
| [[SHP-77 (line)]] | alt | 281 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.416× (z -16.4) |
| [[A498 (line)]] | wt | 194 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -22.6) |
| [[BT-474 (line)]] | alt | 194 | 1 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 201 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 2.68× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 190 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.375× (z -15.9) |
| [[RKO (line)]] | wt | 244 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.441× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 215 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.08× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.426× (z -13.0) |
| [[SNU-423 (line)]] | alt | 181 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.387× (z -16.4) |
| [[A-172 (line)]] | wt | 111 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -15.7) |
| [[COLO 205 (line)]] | alt | 224 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 2.90× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.374× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.274× (z -18.4) |
| [[HT-29 (line)]] | alt | 214 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -18.1) |
| [[SNU-1 (line)]] | wt | 238 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.435× (z -10.7) |
| [[SW 900 (line)]] | alt | 178 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.384× (z -16.4) |
| [[SW48 (line)]] | wt | 226 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -12.3) |
| [[A549 (line)]] | wt | 156 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.394× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -13.7) |
| [[HCT15 (line)]] | alt | 284 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -14.5) |
| [[Hs 766T (line)]] | wt | 193 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.459× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 300 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.382× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 165 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -16.1) |
| [[AN3 CA (line)]] | alt | 180 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.3) |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF8]] | +0.69 | +0.58 / +0.60 | both halves | 7e-06 | same gene group |
| [[BAZ1B]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SREK1]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 | same gene group; STRING 648 |
| [[SETD2]] | +0.66 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[ZFX]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[GPATCH8]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[NFYC]] | +0.62 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[TLK1]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SENP6]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[UBE3A]] | +0.60 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGF]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DHRS1]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[IDS]] | -0.52 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[VAMP1]] | -0.52 | -0.27 / -0.66 | both halves | 3e-04 |  |
| [[ESYT1]] | -0.52 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MTPN]] | -0.52 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[NTAN1]] | -0.51 | -0.26 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SRSF4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.7, 6.0); signed map (11.7, -33.6). **Vector** length 91.5, 28.2% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.6 | +15.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.0 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.8 | +5.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.4 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.3 | -0.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -16.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.1 | +0.1 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | +0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:29,147,743-29,181,900 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRP75; previously SFRS4 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08170](https://www.uniprot.org/uniprotkb/Q08170) (Serine/arginine-rich splicing factor 4):

> Plays a role in alternative splice site selection during pre-mRNA splicing. Represses the splicing of MAPT/Tau exon 10.

**Summary**, from NCBI Gene [6429](https://www.ncbi.nlm.nih.gov/gene/6429):

> Enables RNA binding activity. Involved in negative regulation of mRNA splicing, via spliceosome. Located in nuclear speck. Biomarker of Down syndrome; acute myeloid leukemia; clear cell renal cell carcinoma; and colon adenocarcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10786) · Entrez [6429](https://www.ncbi.nlm.nih.gov/gene/6429) · UniProt [Q08170](https://www.uniprot.org/uniprotkb/Q08170) · Ensembl [ENSG00000116350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116350)

## Data

Gene col 3791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3791); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3791]; `tensor/DDL_lfc|DDL_z.npy` [3791]; `embed/gene_vectors.npy` [3791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3791 or target_col == 3791). Every well: [[SRSF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
