---
symbol: "ZMYM2"
type: "gene"
col: 4290
ensembl_id: "ENSG00000121741"
name: "zinc finger MYM-type containing 2"
location: "13q12.11"
module: 79
arm: "+"
pooled_cpm: 293.02
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ZMYM2

*zinc finger MYM-type containing 2* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.32× (z +6.9, q 4e-09, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (SW480 2.31×, COLO 205 2.79×, J82 1.80×, HOP62 1.91×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 1.95×, COLO 205 1.92×, LoVo 1.45×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 1.94×, COLO 205 2.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.378× (z -23.7, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.637× (z -11.0, q 5e-26, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R5E]] (+0.69, fdr 7e-06), [[TBC1D12]] (+0.68, fdr 7e-06), [[PDE7A]] (+0.68, fdr 1e-05); moves opposite to [[TMEM185B]] (-0.58, fdr 2e-05), [[ZNF502]] (-0.56, fdr 1e-05), [[ZSCAN22]] (-0.53, fdr 5e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF229]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (SW480 2.31×, COLO 205 2.79×, J82 1.80×, HOP62 1.91×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 1.95×, COLO 205 1.92×, LoVo 1.45×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 1.94×, COLO 205 2.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +6.9 | 4e-09 | 34/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.14× | +4.4 | 0.002 | 3/48 (AsPC-1, AN3 CA, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.4 | 0.002 | 21/48 (SW480, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.024 | 21/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.7 | 0.029 | 17/49 (SNU-423, J82, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.4 | 0.063 | 10/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.094 | 19/48 (J82, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.378×** | -23.7 | 0e+00 | 47/49 (NCI-H23, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -20.6 | 0e+00 | 44/44 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.405×** | -20.3 | 0e+00 | 45/45 (LOX-IMVI, HT-29, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.578×** | -12.8 | 2e-35 | 46/47 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.633×** | -11.1 | 1e-26 | 40/48 (A549, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.637×** | -11.0 | 5e-26 | 42/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.681×** | -9.3 | 7e-19 | 39/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -8.5 | 1e-15 | 36/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.744×** | -7.2 | 5e-11 | 37/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.755×** | -6.8 | 5e-10 | 31/48 (NCI-H23, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.763×** | -6.6 | 3e-09 | 38/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.829×** | -6.4 | 6e-09 | 23/48 (C32, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.785×** | -5.7 | 7e-07 | 28/48 (C32, A-172, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -5.4 | 2e-06 | 30/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.813×** | -5.0 | 2e-05 | 26/48 (NCI-H1573, C32, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.721×** | -4.1 | 0.001 | 28/47 (HCT15, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.9 | 0.003 | 19/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.870× | -3.4 | 0.021 | 12/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.770×** | -3.3 | 0.024 | 22/46 (NCI-H1792, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.025 | 22/49 (C32, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.032 | 22/48 (LoVo, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.781×** | -3.1 | 0.045 | 17/48 (SK-MEL-2, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.048 | 13/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.920× | -2.8 | 0.095 | 7/48 (NCI-H23, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 375 | 0 | 16 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -23.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -18.3) |
| [[SW480 (line)]] | alt | 386 | 4 (3 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -12.0) |
| [[HOP62 (line)]] | alt | 281 | 1 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.493× (z -9.5) |
| [[J82 (line)]] | alt | 380 | 1 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.571× (z -9.2) |
| [[A549 (line)]] | wt | 223 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 467 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.537× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 426 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 330 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.527× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 252 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.349× (z -15.0) |
| [[SW 900 (line)]] | alt | 309 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -11.0) |
| [[COLO 205 (line)]] | alt | 560 | 5 (4 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.94× (z +13.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -16.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 340 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 374 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -29.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 262 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -20.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 368 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.558× (z -9.9) |
| [[PANC-1 (line)]] | alt | 234 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -12.7) |
| [[SNU-423 (line)]] | alt | 214 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -17.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -11.4) |
| [[A-172 (line)]] | wt | 186 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -20.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -16.0) |
| [[A-427 (line)]] | wt | 279 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -23.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 269 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -11.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.538× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -12.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.502× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -10.9) |
| [[KATO III (line)]] | alt | 229 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.568× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 292 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.540× (z -9.3) |
| [[SW1417 (line)]] | alt | 242 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -15.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 472 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -14.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 143 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -12.0) |
| [[HT-29 (line)]] | alt | 537 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.537× (z -9.2) |
| [[LoVo (line)]] | wt | 257 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 195 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.487× (z -9.7) |
| [[A498 (line)]] | wt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 349 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 269 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -13.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 313 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 330 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -15.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 215 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 326 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -17.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 314 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 202 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -13.1) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 254 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 466 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -19.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 358 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -16.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 366 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 387 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 268 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -17.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5E]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TBC1D12]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PDE7A]] | +0.68 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[BRWD1]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[TRIM33]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.65 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FBXO42]] | +0.63 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[BBX]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 | STRING 434 |
| [[HDAC3]] | +0.62 | +0.72 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ZNF502]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZSCAN22]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[POGK]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[NUBP1]] | -0.53 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[SGMS2]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[MAK16]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RRP15]] | -0.52 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[NOL6]] | -0.52 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[SRSF6]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[CHMP6]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF229]] | B | ZNF229 activity lowers ZMYM2's level | lines that do not express ZNF229 (25) vs lines expressing it (25) | 1.22× higher at baseline in the lines without ZNF229 | 0.066 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, STAC, C15orf48 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, -18.3); signed map (-21.2, 16.2). **Vector** length 114, 43.1% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.1 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.8 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.5 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.1 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -20.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -8.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYM-type containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:19,958,677-20,091,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAMP, FIM, MYM; previously ZNF198 |
| Gene groups (HGNC) | Zinc fingers MYM-type |
| Reactome | 16 pathways, smallest: Signaling by FLT3 fusion proteins; Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBW7](https://www.uniprot.org/uniprotkb/Q9UBW7) (Zinc finger MYM-type protein 2):

> Involved in the negative regulation of transcription.

**Summary**, from NCBI Gene [7750](https://www.ncbi.nlm.nih.gov/gene/7750):

> The protein encoded by this gene is a zinc finger protein that may act as a transcription factor. The encoded protein may be part of a BHC histone deacetylase complex. Translocation of this gene with the fibroblast growth factor receptor-1 gene (FGFR1) results in a fusion gene, which may be a cause of stem cell leukemia lymphoma syndrome (SCLL). Several transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:12989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12989) · Entrez [7750](https://www.ncbi.nlm.nih.gov/gene/7750) · UniProt [Q9UBW7](https://www.uniprot.org/uniprotkb/Q9UBW7) · Ensembl [ENSG00000121741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121741)

## Data

Gene col 4290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4290); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4290]; `tensor/DDL_lfc|DDL_z.npy` [4290]; `embed/gene_vectors.npy` [4290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4290 or target_col == 4290). Every well: [[ZMYM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
