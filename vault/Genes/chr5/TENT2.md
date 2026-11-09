---
symbol: "TENT2"
type: "gene"
col: 8930
ensembl_id: "ENSG00000164329"
name: "terminal nucleotidyltransferase 2"
location: "5q14.1"
module: 178
arm: "+"
pooled_cpm: 189.32
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# TENT2

*terminal nucleotidyltransferase 2* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.96× (z +12.2, q 1e-31, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.288× (z -20.3, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.763× (z -6.5, q 1e-08, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED23]] (+0.75, fdr 7e-06), [[KLHDC10]] (+0.72, fdr 7e-06), [[RELCH]] (+0.71, fdr 7e-06); moves opposite to [[AGO2]] (-0.66, fdr 1e-05), [[TNFRSF12A]] (-0.63, fdr 1e-05), [[SKIL]] (-0.60, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.96×** | +12.2 | 1e-31 | 48/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.07×** | +10.0 | 7e-21 | 46/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +8.7 | 7e-16 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +7.8 | 1e-12 | 42/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.6 | 3e-12 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +6.7 | 2e-09 | 44/48 (LOX-IMVI, HT-29, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 1e-06 | 34/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 7e-06 | 36/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 1e-04 | 31/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +4.0 | 0.004 | 13/48 (J82, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.054 | 27/48 (COLO 205, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.2 | 0.056 | 27/45 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.056 | 23/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.056 | 19/48 (RKO, PANC-1, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.1 | 0.077 | 20/38 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.288×** | -20.3 | 0e+00 | 44/44 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.335×** | -18.6 | 0e+00 | 49/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.447×** | -12.6 | 2e-34 | 43/45 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -6.5 | 1e-08 | 28/49 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.692×** | -6.2 | 5e-08 | 41/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -5.1 | 4e-05 | 29/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -4.3 | 0.001 | 30/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.789×** | -4.0 | 0.004 | 27/48 (A-172, A549, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.852× | -3.8 | 0.007 | 17/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.798×** | -3.8 | 0.008 | 27/48 (CFPAC-1, H4, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.820×** | -3.4 | 0.036 | 20/48 (CFPAC-1, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -3.4 | 0.036 | 25/49 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.829×** | -3.2 | 0.062 | 24/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.833×** | -3.1 | 0.074 | 22/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.833×** | -3.1 | 0.074 | 22/48 (A-172, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 166 | 8 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 215 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -17.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 114 | 5 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.66× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 206 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -17.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 216 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -17.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 176 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 228 | 2 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 125 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 346 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 223 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -17.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 177 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 148 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.63× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -17.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 165 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.38× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 226 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.81× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -17.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 210 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -16.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 152 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.30× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 196 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 175 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.40× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -22.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 250 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -20.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 220 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -18.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 123 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 183 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.38× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 174 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 325 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -20.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 126 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.10× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 189 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 222 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.91× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -11.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 232 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 184 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -16.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 152 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.74× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -14.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -13.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 150 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -17.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 172 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.75× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 179 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 207 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 188 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -16.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 260 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -12.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -11.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -13.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 307 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 306 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED23]] | +0.75 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.72 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[RELCH]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ZNF148]] | +0.71 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ASB7]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.70 | +0.80 / +0.54 | both halves | 1e-05 |  |
| [[RTCA]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[PSMA6]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CWC15]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[NUP54]] | +0.67 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO2]] | -0.66 | -0.65 / -0.55 | both halves | 1e-05 | STRING 463 |
| [[TNFRSF12A]] | -0.63 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[SKIL]] | -0.60 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[CCND1]] | -0.60 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[THOC6]] | -0.58 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[KDM6B]] | -0.56 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SLC4A7]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MAMLD1]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.6, -12.7); signed map (-32.9, -9.9). **Vector** length 89.8, 35.2% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +5.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | -0.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.8 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | terminal nucleotidyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,612,120-79,688,246 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38499, GLD2, TUT2; previously PAPD4 |
| Gene groups (HGNC) | Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIY7](https://www.uniprot.org/uniprotkb/Q6PIY7) (Poly(A) RNA polymerase GLD2):

> Cytoplasmic poly(A) RNA polymerase that adds successive AMP monomers to the 3'-end of specific RNAs, forming a poly(A) tail. In contrast to the canonical nuclear poly(A) RNA polymerase, it only adds poly(A) to selected cytoplasmic mRNAs. Does not play a role in replication-dependent histone mRNA degradation. Adds a single nucleotide to the 3' end of specific miRNAs, monoadenylation stabilizes and prolongs the activity of some but not all miRNAs.

**Summary**, from NCBI Gene [167153](https://www.ncbi.nlm.nih.gov/gene/167153):

> Enables poly(A) RNA polymerase activity. Involved in histone mRNA catabolic process; mRNA 3'-end processing; and negative regulation of miRNA catabolic process. Predicted to be located in cytoplasm and nucleus. Predicted to be part of nuclear RNA-directed RNA polymerase complex. Predicted to be active in glutamatergic synapse; perforant pathway to dendrate granule cell synapse; and postsynapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26776) · Entrez [167153](https://www.ncbi.nlm.nih.gov/gene/167153) · UniProt [Q6PIY7](https://www.uniprot.org/uniprotkb/Q6PIY7) · Ensembl [ENSG00000164329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164329)

## Data

Gene col 8930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8930); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8930]; `tensor/DDL_lfc|DDL_z.npy` [8930]; `embed/gene_vectors.npy` [8930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8930 or target_col == 8930). Every well: [[TENT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
