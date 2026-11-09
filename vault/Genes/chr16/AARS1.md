---
symbol: "AARS1"
type: "gene"
col: 1639
ensembl_id: "ENSG00000090861"
name: "alanyl-tRNA synthetase 1"
location: "16q22.1"
module: 63
arm: "+"
pooled_cpm: 91.83
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 22
n_dd_up_clean: 32
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# AARS1

*alanyl-tRNA synthetase 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.79× (z +12.5, q 4e-33, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.436× (z -17.7, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.505× (z -11.1, q 4e-26, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPOT]] (+0.91, fdr 7e-06), [[MARS1]] (+0.90, fdr 7e-06), [[ASNS]] (+0.89, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.79×** | +12.5 | 4e-33 | 46/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.00×** | +11.2 | 1e-26 | 47/48 (C-33 A, Hs 766T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.93×** | +10.6 | 4e-24 | 44/48 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.84×** | +9.9 | 8e-21 | 43/48 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +9.2 | 4e-18 | 41/48 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.75×** | +9.0 | 2e-17 | 44/48 (SHP-77, C32, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.48×** | +8.7 | 3e-16 | 38/48 (NCI-H460, LoVo, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.64×** | +8.0 | 1e-13 | 43/47 (C32, SHP-77, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +7.4 | 6e-12 | 36/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 6e-09 | 36/48 (SHP-77, C32, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.49×** | +6.4 | 8e-09 | 37/48 (Hs 766T, NCI-H2030, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +6.0 | 9e-08 | 32/49 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.31×** | +5.8 | 3e-07 | 28/49 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.42×** | +5.7 | 5e-07 | 32/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +5.6 | 8e-07 | 35/50 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.03×** | +5.6 | 9e-07 | 32/48 (LOX-IMVI, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | **1.84×** | +4.8 | 5e-05 | 28/48 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.436×** | -17.7 | 0e+00 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.430×** | -13.1 | 6e-37 | 44/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.505×** | -11.1 | 4e-26 | 43/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.509×** | -10.9 | 1e-25 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.524×** | -10.5 | 2e-23 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.505×** | -10.2 | 1e-22 | 42/47 (SW 900, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.589×** | -8.6 | 8e-16 | 33/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.591×** | -8.5 | 1e-15 | 35/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -8.5 | 1e-15 | 29/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.608×** | -8.1 | 5e-14 | 36/48 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -7.6 | 1e-12 | 35/47 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -7.5 | 3e-12 | 30/49 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.754×** | -6.2 | 2e-08 | 30/48 (SW1417, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -4.6 | 1e-04 | 22/48 (A-427, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.758×** | -4.5 | 3e-04 | 22/49 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.009 | 18/49 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.801×** | -3.4 | 0.017 | 19/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.017 | 19/48 (NCI-H23, SW48, …) | two highest doses |  |
| [[Adenine (drug)]] 5 µM |  | 0.857× | -3.4 | 0.020 | 13/48 (LS 180, NCI-H460, …) | top dose only | position effect removed |
| [[Busulfan (drug)]] 5 µM |  | 0.867× | -2.9 | 0.076 | 13/49 (KATO III, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 208 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -27.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -16.4) |
| [[PANC-1 (line)]] | alt | 129 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -37.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -26.8) |
| [[SW48 (line)]] | wt | 130 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.205× (z -12.1) |
| [[A-172 (line)]] | wt | 120 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -12.8) |
| [[LoVo (line)]] | wt | 130 | 0 | 11 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -21.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.187× (z -17.6) |
| [[KATO III (line)]] | alt | 215 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.306× (z -11.9) |
| [[SW480 (line)]] | alt | 131 | 2 (1 ⚠) | 8 (7 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Artesunate (drug)]] 5 µM 1.83× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.291× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.401× (z -9.5) |
| [[A-427 (line)]] | wt | 161 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -19.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.417× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 53.3 | 3 | 6 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.38× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.184× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.352× (z -10.0) |
| [[RKO (line)]] | wt | 124 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.175× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.1) |
| [[HS-578T (line)]] | alt | 91.1 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -16.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -12.4) |
| [[SNU-1 (line)]] | wt | 106 | 1 | 7 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.49× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0927× (z -16.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -11.3) |
| [[H4 (line)]] | wt | 105 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -19.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.197× (z -12.4) |
| [[SW1417 (line)]] | alt | 101 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.382× (z -8.9) |
| [[BT-474 (line)]] | alt | 101 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 72.5 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.282× (z -8.8) |
| [[A498 (line)]] | wt | 126 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 51.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.297× (z -10.2) |
| [[C-33 A (line)]] | alt | 96.4 | 1 | 2 (1 ⚠) | [[5-Azacytidine (drug)]] 5 µM 3.76× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.5) |
| [[C32 (line)]] | wt | 43.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.30× (z +9.5) ⚠ unreliable plate only · without an alert: [[5-Azacytidine (drug)]] 5 µM 4.27× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 92.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.298× (z -8.8) |
| [[SHP-77 (line)]] | alt | 90.7 | 3 (1 ⚠) | 0 | [[Artesunate (drug)]] 0.5 µM 2.99× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 45.7 | 2 | 0 | [[Artesunate (drug)]] 5 µM 2.49× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 59.3 | 2 | 0 | [[5-Azacytidine (drug)]] 5 µM 3.93× (z +9.9) | — |
| [[J82 (line)]] | alt | 92.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.416× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 60.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.267× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 127 | 2 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.54× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -22.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 46.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.20× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.42× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -9.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -11.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 35.4 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 4.39× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 63.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.156× (z -12.6) |
| [[A549 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPOT]] | +0.91 | +0.89 / +0.92 | both halves | 7e-06 | STRING 401 |
| [[MARS1]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 913 |
| [[ASNS]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 | STRING 840 |
| [[YARS1]] | +0.88 | +0.84 / +0.92 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 996 |
| [[GARS1]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 983 |
| [[SARS1]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 881 |
| [[IARS1]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 980 |
| [[PSAT1]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | STRING 560 |
| [[CARS1]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 872 |
| [[MTHFD2]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[PHGDH]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | STRING 448 |
| [[TARS1]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 929 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises AARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.39× lower at baseline in the lines without ASNSP1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ASNSP1]] | B | ASNSP1 activity strengthens AARS1's drug response | lines that do not express ASNSP1 (35) vs lines expressing it (13) | the lines without ASNSP1 respond 0.99× as strongly (z diff +0.69); strongest at Homoharringtonine 5 µM: 0.46x vs 0.27x (z diff +3.0) | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; target measured in part of the lines; both ways; artifact flags |
| [[LINC00662]] | C | LINC00662 activity weakens AARS1's drug response | lines that do not express LINC00662 (3) vs lines expressing it (45) | the lines without LINC00662 respond 1.38× as strongly (z diff -1.21); strongest at Ouabain (Octahydrate) 5 µM: 0.25x vs 0.54x (z diff -4.7) | 0.083 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.938). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.3, 47.8); signed map (-13.5, 24.3). **Vector** length 165, 61.3% of its response variance represented; |z| ≥ 3 in 1,651 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.78 to 16); *mTORC1 signaling* (hallmark, mean cos +0.71 to 20); *unfolded protein response* (hallmark, mean cos +0.80 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.3 | +10.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +11.2 | +11.2 |
|  | [[Artesunate (drug)]] 5 µM |  | +11.0 | +12.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +9.8 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.9 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.0 | +9.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +7.7 | +9.0 |
| fall | [[Harringtonine (drug)]] 0.05 µM |  | -7.4 | -10.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.4 | -10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.9 | -13.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.0 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.6 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | alanyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,251,983-70,289,707 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CMT2N, AlaRS; previously AARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49588](https://www.uniprot.org/uniprotkb/P49588) (Alanine--tRNA ligase, cytoplasmic):

> Catalyzes the attachment of alanine to tRNA(Ala) in a two-step reaction: alanine is first activated by ATP to form Ala-AMP and then transferred to the acceptor end of tRNA(Ala). Also edits incorrectly charged tRNA(Ala) via its editing domain. In presence of high levels of lactate, also acts as a protein lactyltransferase that mediates lactylation of lysine residues in target proteins, such as TEAD1, TP53/p53 and YAP1. Protein lactylation takes place in a two-step reaction: lactate is first …

**Summary**, from NCBI Gene [16](https://www.ncbi.nlm.nih.gov/gene/16):

> The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes. Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein. tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids to the tRNAs that contain the cognate trinucleotide anticodons. They consist of a catalytic domain …

**Accessions** — [HGNC:20](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20) · Entrez [16](https://www.ncbi.nlm.nih.gov/gene/16) · UniProt [P49588](https://www.uniprot.org/uniprotkb/P49588) · Ensembl [ENSG00000090861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090861)

## Data

Gene col 1639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1639); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1639]; `tensor/DDL_lfc|DDL_z.npy` [1639]; `embed/gene_vectors.npy` [1639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1639 or target_col == 1639). Every well: [[AARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
