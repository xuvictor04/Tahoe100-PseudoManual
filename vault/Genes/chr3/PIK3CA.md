---
symbol: "PIK3CA"
type: "gene"
col: 4300
ensembl_id: "ENSG00000121879"
name: "phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha"
location: "3q26.32"
module: 69
arm: "+"
pooled_cpm: 158.03
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 20
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PIK3CA

*phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha* — 3q26.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.17× (z +4.4, q 0.003, up in 21 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 1.16× (z +4.3, q 0.003, up in 15 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 1.70×, NCI-H1792 1.75×, SW 900 2.11×, A549 1.82×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 2.16×, BT-474 2.32×, SW480 1.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 1.83×, NCI-H2347 1.65×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.401× (z -27.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREBRF]] (+0.77, fdr 7e-06), [[KLHL24]] (+0.76, fdr 7e-06), [[ELF2]] (+0.75, fdr 7e-06); moves opposite to [[AGK]] (-0.61, fdr 7e-06), [[EIPR1]] (-0.61, fdr 1e-05), [[EFTUD2]] (-0.61, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[REPS2]] → it (grade B ⚠); 20 go from it, the strongest it → [[KLF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4300.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 1.70×, NCI-H1792 1.75×, SW 900 2.11×, A549 1.82×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 2.16×, BT-474 2.32×, SW480 1.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 1.83×, NCI-H2347 1.65×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 0.003 | 21/47 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.3 | 0.003 | 23/48 (PANC-1, NCI-H1792, …) | top dose only | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +4.3 | 0.003 | 15/49 (A-427, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.9 | 0.015 | 19/48 (SW480, NCI-H2347, …) | top dose only | composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.074 | 20/48 (BT-474, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.12× | +3.4 | 0.075 | 5/48 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.12× | +3.1 | 0.14 | 8/47 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.15 | 9/47 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.15× | +3.0 | 0.16 | 4/48 (A-427, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.401×** | -27.0 | 0e+00 | 47/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.417×** | -25.9 | 0e+00 | 46/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.484×** | -21.4 | 0e+00 | 48/49 (A-427, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.474×** | -20.4 | 0e+00 | 43/45 (Panc 03.27, A-427, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.501×** | -20.4 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.505×** | -20.2 | 0e+00 | 47/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.513×** | -19.0 | 0e+00 | 43/44 (NCI-H2347, SNU-1, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.457×** | -12.1 | 8e-32 | 48/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.495×** | -10.9 | 1e-25 | 46/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.502×** | -10.7 | 1e-24 | 46/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.521×** | -10.1 | 4e-22 | 44/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.525×** | -9.9 | 1e-21 | 45/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.740×** | -8.9 | 3e-17 | 33/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -7.7 | 4e-13 | 24/48 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.785×** | -7.1 | 5e-11 | 28/48 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.753×** | -6.0 | 8e-08 | 29/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.769×** | -5.5 | 1e-06 | 32/49 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.831×** | -5.5 | 1e-06 | 24/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -5.4 | 2e-06 | 14/48 (A-172, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.835× | -5.3 | 3e-06 | 22/48 (A-427, PANC-1, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.726×** | -4.9 | 2e-05 | 26/47 (C-33 A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.806×** | -4.5 | 1e-04 | 19/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.852× | -4.3 | 3e-04 | 12/47 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 261 | 1 (1 ⚠) | 13 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -31.9) |
| [[PANC-1 (line)]] | alt | 221 | 1 (1 ⚠) | 12 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 1.70× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.436× (z -16.0) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 164 | 1 (1 ⚠) | 11 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.232× (z -20.6) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 146 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -21.3) |
| [[A-172 (line)]] | wt | 236 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -15.3) |
| [[A-427 (line)]] | wt | 303 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.481× (z -12.0) |
| [[A549 (line)]] | wt | 110 | 1 (1 ⚠) | 8 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 1.82× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.310× (z -17.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 179 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -19.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 170 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.5) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -12.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.510× (z -11.2) |
| [[HS-578T (line)]] | alt | 193 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -13.6) |
| [[KATO III (line)]] | alt | 192 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 84.7 | 1 (1 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.16× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.458× (z -12.0) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -11.7) |
| [[SW480 (line)]] | alt | 153 | 2 (2 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.366× (z -19.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -18.3) |
| [[BT-474 (line)]] | alt | 121 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.6) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -13.2) |
| [[HT-29 (line)]] | alt | 128 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 257 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -22.7) |
| [[SK-MEL-2 (line)]] | alt | 219 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -14.7) |
| [[SW1417 (line)]] | alt | 163 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -17.3) |
| [[C32 (line)]] | wt | 112 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.484× (z -8.5) |
| [[HCT15 (line)]] | alt | 182 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -11.1) |
| [[HOP62 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -13.0) |
| [[LoVo (line)]] | wt | 113 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.415× (z -13.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.307× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 165 | 1 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.75× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -20.9) |
| [[NCI-H2030 (line)]] | alt | 90.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.412× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 186 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.417× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -12.6) |
| [[SNU-1 (line)]] | wt | 125 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -11.2) |
| [[SNU-423 (line)]] | alt | 160 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -17.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -16.6) |
| [[SW 900 (line)]] | alt | 127 | 1 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.11× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -12.3) |
| [[H4 (line)]] | wt | 157 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.404× (z -11.2) |
| [[LS 180 (line)]] | wt | 116 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 119 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -12.5) |
| [[RKO (line)]] | wt | 147 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -13.3) |
| [[A498 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -10.6) |
| [[CHP-212 (line)]] | wt | 196 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[vincristine (drug)]] 5 µM 0.0575× (z -11.9) |
| [[COLO 205 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.434× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -9.2) |
| [[J82 (line)]] | alt | 135 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.27× (z +11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 183 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.443× (z -10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.0) |
| [[AN3 CA (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -12.6) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.397× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREBRF]] | +0.77 | +0.59 / +0.84 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[ELF2]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.74 | +0.62 / +0.83 | both halves | 7e-06 |  |
| [[HBP1]] | +0.72 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.69 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CERT1]] | +0.68 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.67 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[UBN2]] | +0.67 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[ARID4A]] | +0.67 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CDK19]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGK]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 | pathway: Phospholipid metabolism |
| [[EIPR1]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.61 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[POLR1A]] | -0.59 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[DCAF1]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NOC2L]] | -0.58 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[GCN1]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CLPB]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[COA1]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[FARSB]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REPS2]] | B | REPS2 activity raises PIK3CA's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.12× lower at baseline in the lines without REPS2 | 0.077 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF3]] | B | PIK3CA activity lowers KLF3's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[SUV39H2]] | B | PIK3CA activity raises SUV39H2's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[TCERG1]] | B | PIK3CA activity raises TCERG1's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[CP]] | B | PIK3CA activity lowers CP's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[CUTALP]] | B | PIK3CA activity lowers CUTALP's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TRAF3]] | B | PIK3CA activity raises TRAF3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ELAVL1]] | B | PIK3CA activity raises ELAVL1's level | compounds that target PIK3CA: 2 of 4 lower it (Alpelisib, Bimiralisib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds |
| [[RSRC1]] | B | PIK3CA activity lowers RSRC1's level | compounds that target PIK3CA: 2 of 4 raise it (Bimiralisib, GSK1059615) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ACER3]] | B | PIK3CA activity raises ACER3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[RXRB]] | B | PIK3CA activity lowers RXRB's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[TNFSF10]] | B | PIK3CA activity lowers TNFSF10's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[E2F3]] | B | PIK3CA activity raises E2F3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.6, -43.9); signed map (-13.8, 9.8). **Vector** length 127, 42.2% of its response variance represented; |z| ≥ 3 in 1,535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.7 | +0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.1 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.7 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.0 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.9 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.6 | -20.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.7 | -12.1 |
|  | [[EX229 (drug)]] 5 µM |  | -9.6 | -10.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.5 | -10.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.2 | -9.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.5 | -10.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.32 — chr3:179,148,114-179,240,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PI3K |
| Gene groups (HGNC) | Phosphatidylinositol 3-kinase family |
| Hallmark sets | COMPLEMENT |
| Reactome | 132 pathways, smallest: Activated NTRK2 signals through PI3K; Activated NTRK3 signals through PI3K; Co-stimulation by ICOS |
| Matched by | ensembl_id |

**Function**, from UniProt [P42336](https://www.uniprot.org/uniprotkb/P42336) (Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform):

> Phosphoinositide-3-kinase (PI3K) phosphorylates phosphatidylinositol (PI) and its phosphorylated derivatives at position 3 of the inositol ring to produce 3-phosphoinositides. Uses ATP and PtdIns(4,5)P2 (phosphatidylinositol 4,5-bisphosphate) to generate phosphatidylinositol 3,4,5-trisphosphate (PIP3). PIP3 plays a key role by recruiting PH domain-containing proteins to the membrane, including AKT1 and PDPK1, activating signaling cascades involved in cell growth, survival, proliferation, …

**Summary**, from NCBI Gene [5290](https://www.ncbi.nlm.nih.gov/gene/5290):

> Phosphatidylinositol 3-kinase is composed of an 85 kDa regulatory subunit and a 110 kDa catalytic subunit. The protein encoded by this gene represents the catalytic subunit, which uses ATP to phosphorylate PtdIns, PtdIns4P and PtdIns(4,5)P2. This gene has been found to be oncogenic and has been implicated in cervical cancers. A pseudogene of this gene has been defined on chromosome 22. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:8975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8975) · Entrez [5290](https://www.ncbi.nlm.nih.gov/gene/5290) · UniProt [P42336](https://www.uniprot.org/uniprotkb/P42336) · Ensembl [ENSG00000121879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121879)

## Data

Gene col 4300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4300); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4300]; `tensor/DDL_lfc|DDL_z.npy` [4300]; `embed/gene_vectors.npy` [4300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4300 or target_col == 4300). Every well: [[PIK3CA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3CA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
