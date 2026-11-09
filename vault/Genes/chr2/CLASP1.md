---
symbol: "CLASP1"
type: "gene"
col: 1068
ensembl_id: "ENSG00000074054"
name: "cytoplasmic linker associated protein 1"
location: "2q14.2-q14.3"
module: 169
arm: "+"
pooled_cpm: 248.81
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# CLASP1

*cytoplasmic linker associated protein 1* — 2q14.2-q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.24× (z +7.3, q 1e-10, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.452× (z -15.4, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.616× (z -9.4, q 6e-19, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA6]] (+0.66, fdr 1e-05), [[PPP2R5E]] (+0.64, fdr 1e-05), [[ASCC1]] (+0.63, fdr 1e-05); moves opposite to [[LIF]] (-0.59, fdr 1e-05), [[IER2]] (-0.57, fdr 1e-05), [[LINC00973]] (-0.56, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +7.3 | 1e-10 | 46/49 (SW480, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.3 | 4e-05 | 39/48 (C32, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.2 | 4e-05 | 31/48 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +3.8 | 0.017 | 26/48 (A498, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.031 | 24/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.1 | 0.19 | 1/48 (SW 1271) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.452×** | -15.4 | 0e+00 | 48/49 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.461×** | -14.5 | 4e-45 | 44/44 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.480×** | -13.2 | 2e-37 | 42/45 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.635×** | -12.5 | 1e-33 | 38/48 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -9.4 | 6e-19 | 42/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.632×** | -8.9 | 4e-17 | 45/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -8.1 | 5e-14 | 43/47 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -7.8 | 5e-13 | 43/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.686×** | -7.3 | 1e-11 | 39/48 (A-172, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.698×** | -6.7 | 1e-09 | 34/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.713×** | -6.6 | 3e-09 | 41/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.797×** | -6.2 | 2e-08 | 30/49 (A549, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.737×** | -5.9 | 2e-07 | 37/48 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.758×** | -5.4 | 3e-06 | 32/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.821×** | -3.8 | 0.005 | 25/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.893× | -3.1 | 0.067 | 3/49 (COLO 205, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 356 | 1 | 12 (10 ⚠) | [[PH-797804 (drug)]] 5 µM 4.37× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 314 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -20.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.341× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 306 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -10.5) |
| [[A-172 (line)]] | wt | 263 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -22.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 295 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -17.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -12.4) |
| [[SW 900 (line)]] | alt | 446 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -10.2) |
| [[HT-29 (line)]] | alt | 277 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.498× (z -9.4) |
| [[J82 (line)]] | alt | 227 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -14.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LOX-IMVI (line)]] | wt | 244 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.526× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 144 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -22.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 319 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -15.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 261 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -15.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 243 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0458× (z -38.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.396× (z -12.0) |
| [[AN3 CA (line)]] | alt | 348 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.293× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 234 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -13.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 490 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -9.8) |
| [[HS-578T (line)]] | alt | 188 | 2 | 3 (2 ⚠) | [[Budesonide (drug)]] 5 µM 1.79× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.530× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 304 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.550× (z -8.9) |
| [[PANC-1 (line)]] | alt | 225 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -13.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 211 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -24.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.497× (z -9.8) |
| [[SW480 (line)]] | alt | 254 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.73× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.483× (z -12.0) |
| [[A549 (line)]] | wt | 229 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.37× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -13.8) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HCT15 (line)]] | alt | 299 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -14.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 307 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -13.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 238 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.99× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 357 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CHP-212 (line)]] | wt | 329 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 173 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 258 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0712× (z -16.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -12.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[KATO III (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.99× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.473× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 267 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 273 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 225 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 306 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.199× (z -11.0) |
| [[H4 (line)]] | wt | 286 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 245 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA6]] | +0.66 | +0.72 / +0.52 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PPP2R5E]] | +0.64 | +0.69 / +0.57 | both halves | 1e-05 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[ASCC1]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.62 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.61 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[AGTPBP1]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[UGP2]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ZNF148]] | +0.59 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[STRN3]] | +0.59 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[PHB2]] | +0.58 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[RSRC1]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ZDHHC7]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIF]] | -0.59 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[IER2]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[LINC00973]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[IL11]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TRAF1]] | -0.55 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.54 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[SYNJ2]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[FZD8]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ACTN2]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[HMGN2P46]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PHLDA1]] | -0.52 | -0.54 / -0.40 | both halves | 4e-05 | pathway: G2/M Transition |
| [[INHBA]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers CLASP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, -10.5); signed map (-35.5, -7.2). **Vector** length 108, 42.4% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | +6.4 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +1.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.5 | +1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.5 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -8.3 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.4 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.8 | -0.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic linker associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2-q14.3 — chr2:121,337,776-121,649,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0622, MAST1 |
| Gene groups (HGNC) | TOG domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 34 pathways, smallest: Role of ABL in ROBO-SLIT signaling; Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z460](https://www.uniprot.org/uniprotkb/Q7Z460) (CLIP-associating protein 1):

> Microtubule plus-end tracking protein that promotes the stabilization of dynamic microtubules. Involved in the nucleation of noncentrosomal microtubules originating from the trans-Golgi network (TGN). Required for the polarization of the cytoplasmic microtubule arrays in migrating cells towards the leading edge of the cell. May act at the cell cortex to enhance the frequency of rescue of depolymerizing microtubules by attaching their plus-ends to cortical platforms composed of ERC1 and PHLDB2. …

**Summary**, from NCBI Gene [23332](https://www.ncbi.nlm.nih.gov/gene/23332):

> CLASPs, such as CLASP1, are nonmotor microtubule-associated proteins that interact with CLIPs (e.g., CLIP170; MIM 179838). CLASP1 is involved in the regulation of microtubule dynamics at the kinetochore and throughout the spindle (Maiato et al., 2003 [PubMed 12837247]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17088) · Entrez [23332](https://www.ncbi.nlm.nih.gov/gene/23332) · UniProt [Q7Z460](https://www.uniprot.org/uniprotkb/Q7Z460) · Ensembl [ENSG00000074054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074054)

## Data

Gene col 1068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1068); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1068]; `tensor/DDL_lfc|DDL_z.npy` [1068]; `embed/gene_vectors.npy` [1068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1068 or target_col == 1068). Every well: [[CLASP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLASP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
