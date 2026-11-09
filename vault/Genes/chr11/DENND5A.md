---
symbol: "DENND5A"
type: "gene"
col: 11484
ensembl_id: "ENSG00000184014"
name: "DENN domain containing 5A"
location: "11p15.4"
module: 214
arm: "+"
pooled_cpm: 172.44
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# DENND5A

*DENN domain containing 5A* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.75× (z +9.2, q 2e-17, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.429× (z -13.8, q 1e-40, down in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.564× (z -9.3, q 1e-18, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRTFA]] (+0.56, fdr 1e-05), [[GABBR1]] (+0.54, fdr 3e-04), [[BLTP3B]] (+0.53, fdr 3e-05); moves opposite to [[PPP2R5C]] (-0.51, fdr 7e-04), [[PRPF38A]] (-0.47, fdr 2e-04), [[ITGB4]] (-0.41, fdr 3e-04).
> It is in [[Module 214]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TCF7L1]] → it (grade B ⚠); 8 go from it, the strongest it → [[TRPC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +9.2 | 2e-17 | 41/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +7.0 | 7e-10 | 36/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +6.9 | 7e-10 | 37/45 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.4 | 2e-08 | 41/45 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.8 | 9e-07 | 34/45 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 7e-06 | 32/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +5.1 | 3e-05 | 30/46 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +5.1 | 3e-05 | 37/45 (LoVo, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 24/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +4.7 | 1e-04 | 33/45 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.7 | 2e-04 | 32/45 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 23/45 (AsPC-1, CFPAC-1, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.002 | 25/45 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +3.5 | 0.021 | 27/44 (H4, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.027 | 23/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.052 | 22/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.065 | 21/45 (HT-29, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.429×** | -13.8 | 1e-40 | 37/46 (C-33 A, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -13.6 | 8e-40 | 41/42 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.516×** | -10.0 | 4e-21 | 38/43 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.564×** | -9.3 | 1e-18 | 41/45 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -7.6 | 4e-12 | 32/46 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.655×** | -6.9 | 5e-10 | 36/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.717×** | -5.4 | 5e-06 | 30/45 (A549, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -5.2 | 1e-05 | 29/44 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.741×** | -4.9 | 7e-05 | 32/45 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.823×** | -4.5 | 4e-04 | 28/45 (A549, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.833×** | -4.2 | 0.001 | 20/45 (A549, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.627×** | -4.0 | 0.003 | 31/44 (NCI-H1792, A-427, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.807×** | -3.5 | 0.020 | 22/45 (A549, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.807×** | -3.5 | 0.020 | 22/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -3.5 | 0.020 | 17/45 (A-172, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.045 | 18/45 (SNU-423, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.828×** | -3.1 | 0.075 | 22/45 (NCI-H1573, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 278 | 8 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.479× (z -10.0) |
| [[SW480 (line)]] | alt | 137 | 8 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.491× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 116 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +13.3) | — |
| [[A549 (line)]] | wt | 246 | 1 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -15.7) |
| [[A-172 (line)]] | wt | 290 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 342 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 242 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -13.8) |
| [[H4 (line)]] | wt | 258 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.1) |
| [[HOP62 (line)]] | alt | 201 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 183 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.8) |
| [[SNU-423 (line)]] | alt | 353 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 138 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 243 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.347× (z -10.1) |
| [[A498 (line)]] | wt | 275 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 229 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.2) |
| [[C32 (line)]] | wt | 198 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 228 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0663× (z -23.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 193 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.7) |
| [[AN3 CA (line)]] | alt | 322 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0841× (z -20.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -21.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 196 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -8.9) |
| [[J82 (line)]] | alt | 290 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.7) |
| [[LoVo (line)]] | wt | 77.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 100 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -10.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 60.3 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.93× (z +8.6) | — |
| [[RKO (line)]] | wt | 197 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 158 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRTFA]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[GABBR1]] | +0.54 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[BLTP3B]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LRRFIP2]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PLPP1]] | +0.52 | +0.37 / +0.46 | both halves | 8e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[FERMT2]] | +0.51 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[USP12]] | +0.50 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[HES4]] | +0.49 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[RHOQ]] | +0.49 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[FSD1L]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ZFAND3]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[CCSER2]] | +0.48 | +0.25 / +0.52 | both halves | 4e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5C]] | -0.51 | -0.21 / -0.54 | both halves | 7e-04 |  |
| [[PRPF38A]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ITGB4]] | -0.41 | -0.27 / -0.32 | both halves | 3e-04 |  |
| [[DUSP4]] | -0.41 | -0.27 / -0.38 | both halves | 3e-04 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ETV1]] | -0.41 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[FAM3C2P]] | -0.40 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[LINC02320]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[ITGA6]] | -0.38 | -0.26 / -0.25 | both halves | 4e-04 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ARHGAP18]] | -0.38 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[HSD17B2]] | -0.37 | -0.20 / -0.47 | both halves | 7e-04 |  |
| [[TBC1D8]] | -0.37 | -0.16 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[LRP5]] | -0.37 | -0.20 / -0.38 | both halves | 7e-04 |  |
| [[TGFBR2]] | -0.36 | -0.43 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF7L1]] | B | TCF7L1 activity raises DENND5A's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.50× lower at baseline in the lines without TCF7L1 | 0.032 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[RNF223]] | B | RNF223 activity lowers DENND5A's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 2.02× higher at baseline in the lines without RNF223 | 0.034 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[FAM3C2P]] | B | FAM3C2P activity raises DENND5A's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without FAM3C2P | 0.039 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity lowers DENND5A's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.80× higher at baseline in the lines without DUSP4 | 0.040 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[EBF4]] | B | EBF4 activity raises DENND5A's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.21× lower at baseline in the lines without EBF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[LINC02320]] | B | LINC02320 activity lowers DENND5A's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.88× higher at baseline in the lines without LINC02320 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[HEG1]] | B | HEG1 activity raises DENND5A's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without HEG1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[BRSK1]] | B | BRSK1 activity raises DENND5A's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without BRSK1 | 0.088 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[FSD1L]] | C | FSD1L activity raises DENND5A's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.80× lower at baseline in the lines without FSD1L | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC1]] | C | DENND5A activity raises TRPC1's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 7.94× lower at baseline in the lines without DENND5A | 0.012 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target |
| [[FSD1L]] | C | DENND5A, [[SPIRE1]] activity raises FSD1L's level | lines that do not express DENND5A, SPIRE1 (3) vs lines expressing them (47) | 4.09× lower at baseline in the lines without DENND5A, SPIRE1 | 0.015 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target; co-absent genes |
| [[LRP12]] | C | DENND5A activity raises LRP12's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 8.15× lower at baseline in the lines without DENND5A | 0.016 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[FERMT2]] | C | DENND5A activity raises FERMT2's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 9.54× lower at baseline in the lines without DENND5A | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[TTC7B]] | C | DENND5A, [[SPIRE1]] activity raises TTC7B's level | lines that do not express DENND5A, SPIRE1 (3) vs lines expressing them (47) | 6.81× lower at baseline in the lines without DENND5A, SPIRE1 | 0.023 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent genes |
| cells under [[Lonafarnib (drug)]] 5 µM | C | DENND5A, [[FRMD6-AS2]], [[SPIRE1]] activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express DENND5A, FRMD6-AS2, SPIRE1 (3) vs lines expressing them (45) | the lines without DENND5A, FRMD6-AS2, SPIRE1: 0.11× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent genes |
| [[TCF7L1]] | C | DENND5A activity raises TCF7L1's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 6.74× lower at baseline in the lines without DENND5A | 0.065 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[RAB32]] | C | DENND5A activity raises RAB32's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 3.75× lower at baseline in the lines without DENND5A | 0.069 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.1, -2.4); signed map (-8.0, 14.4). **Vector** length 81.5, 26.3% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.6 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.1 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +0.2 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | +6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +4.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,138,825-9,265,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1091, FLJ22354, FLJ33829, FLJ43455; previously RAB6IP1 |
| Gene groups (HGNC) | DENN domain containing; RUN domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ26](https://www.uniprot.org/uniprotkb/Q6IQ26) (DENN domain-containing protein 5A):

> Guanine nucleotide exchange factor (GEF) which may activate RAB6A and RAB39A and/or RAB39B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form. Involved in the negative regulation of neurite outgrowth (By similarity).

**Summary**, from NCBI Gene [23258](https://www.ncbi.nlm.nih.gov/gene/23258):

> This gene encodes a DENN-domain-containing protein that functions as a RAB-activating guanine nucleotide exchange factor (GEF). This protein catalyzes the conversion of GDP to GTP and thereby converts inactive GDP-bound Rab proteins into their active GTP-bound form. The encoded protein is recruited by RAB6 onto Golgi membranes and is therefore referred to as RAB6-interacting protein 1. This protein binds with RAB39 as well. Alternative splicing results in multiple transcript variants encoding …

**Accessions** — [HGNC:19344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19344) · Entrez [23258](https://www.ncbi.nlm.nih.gov/gene/23258) · UniProt [Q6IQ26](https://www.uniprot.org/uniprotkb/Q6IQ26) · Ensembl [ENSG00000184014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184014)

## Data

Gene col 11484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11484); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11484]; `tensor/DDL_lfc|DDL_z.npy` [11484]; `embed/gene_vectors.npy` [11484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11484 or target_col == 11484). Every well: [[DENND5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
