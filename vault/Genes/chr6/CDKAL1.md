---
symbol: "CDKAL1"
type: "gene"
col: 7051
ensembl_id: "ENSG00000145996"
name: "CDKAL1 threonylcarbamoyladenosine tRNA methylthiotransferase"
location: "6p22.3"
module: 185
arm: "+"
pooled_cpm: 259.66
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# CDKAL1

*CDKAL1 threonylcarbamoyladenosine tRNA methylthiotransferase* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.02× (z +7.9, q 2e-12, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.544× (z -22.9, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO11]] (+0.71, fdr 7e-06), [[ULK4]] (+0.69, fdr 7e-06), [[FTO]] (+0.68, fdr 7e-06); moves opposite to [[CCNYL1]] (-0.60, fdr 1e-05), [[TRIM36]] (-0.56, fdr 2e-05), [[ERF]] (-0.53, fdr 1e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WWOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +7.9 | 2e-12 | 38/49 (LOX-IMVI, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +6.6 | 2e-08 | 29/48 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +6.3 | 4e-08 | 30/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +6.0 | 3e-07 | 34/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +4.8 | 1e-04 | 23/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.008 | 25/47 (LOX-IMVI, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.014 | 24/48 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.10× | +3.6 | 0.021 | 0/48 | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.4 | 0.041 | 10/49 (HepG2/C3A, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.041 | 22/49 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.11 | 2/48 (HT-29, Hs 766T) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.0 | 0.11 | 14/48 (LS 180, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -22.9 | 0e+00 | 47/49 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -19.3 | 0e+00 | 46/47 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -16.7 | 0e+00 | 35/44 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -12.5 | 1e-33 | 39/49 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -12.1 | 9e-32 | 31/45 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.725×** | -12.1 | 1e-31 | 46/48 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.660×** | -11.0 | 2e-26 | 43/48 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.668×** | -10.3 | 4e-23 | 42/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.767×** | -10.0 | 1e-21 | 30/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -8.9 | 4e-17 | 38/48 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.647×** | -8.5 | 1e-15 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.747×** | -7.8 | 4e-13 | 42/49 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.782×** | -6.5 | 3e-09 | 30/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -6.2 | 3e-08 | 37/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.795×** | -6.1 | 4e-08 | 29/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -5.8 | 3e-07 | 28/50 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.816×** | -5.4 | 2e-06 | 27/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.626×** | -5.3 | 4e-06 | 37/48 (HS-578T, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.881× | -4.8 | 5e-05 | 10/49 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.840× | -4.6 | 9e-05 | 20/49 (NCI-H23, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.834× | -4.5 | 2e-04 | 22/47 (CHP-212, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.857× | -4.1 | 1e-03 | 20/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 610 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -29.2) |
| [[HOP62 (line)]] | alt | 243 | 1 | 9 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.72× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -17.6) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -16.2) |
| [[PANC-1 (line)]] | alt | 257 | 1 (1 ⚠) | 9 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.79× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 217 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -16.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -12.1) |
| [[SNU-423 (line)]] | alt | 298 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -20.3) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 289 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -19.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 214 | 3 (1 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.599× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 452 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.241× (z -22.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -15.8) |
| [[A498 (line)]] | wt | 199 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -17.6) |
| [[C32 (line)]] | wt | 254 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 263 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -19.7) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -13.3) |
| [[SW 900 (line)]] | alt | 270 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -15.2) |
| [[KATO III (line)]] | alt | 288 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 227 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.269× (z -20.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -18.5) |
| [[HCT15 (line)]] | alt | 377 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 438 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -13.7) |
| [[RKO (line)]] | wt | 297 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -15.4) |
| [[SW1417 (line)]] | alt | 172 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.288× (z -18.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.0) |
| [[C-33 A (line)]] | alt | 293 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -14.3) |
| [[H4 (line)]] | wt | 242 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -14.9) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.3) |
| [[HT-29 (line)]] | alt | 196 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -18.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -12.5) |
| [[J82 (line)]] | alt | 471 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -18.1) |
| [[LS 180 (line)]] | wt | 255 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -14.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 318 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 166 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.581× (z -12.8) |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.227× (z -10.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 252 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.4) |
| [[CHP-212 (line)]] | wt | 263 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.7) |
| [[COLO 205 (line)]] | alt | 229 | 2 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.69× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -13.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 229 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.372× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.4) |
| [[LoVo (line)]] | wt | 261 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 296 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -31.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -12.7) |
| [[A549 (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -15.2) |
| [[AN3 CA (line)]] | alt | 398 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.396× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -17.7) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.576× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 276 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 214 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.631× (z -9.9) |
| [[BT-474 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.513× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H596 (line)]] | alt | 280 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 2.71× (z +11.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SNU-1 (line)]] | wt | 263 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.226× (z -17.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 238 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.6) |
| [[A-172 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 416 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO11]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ULK4]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FTO]] | +0.68 | +0.65 / +0.74 | both halves | 7e-06 | STRING 872 |
| [[ANAPC10]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[IFT43]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[FARS2]] | +0.65 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[LINC00630]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CWC27]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TTLL5]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RSRC1]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[INVS]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NUP214]] | +0.60 | +0.57 / +0.62 | both halves | 8e-06 | pathway: tRNA processing |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.60 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[TRIM36]] | -0.56 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[ERF]] | -0.53 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CCDC92]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SERTAD2]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TEP1]] | -0.48 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[NR1D1]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[STX11]] | -0.48 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[N4BP3]] | -0.47 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[GLIS2]] | -0.47 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | B | WWOX activity raises CDKAL1's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without WWOX | 0.066 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers CDKAL1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.4, -13.3); signed map (-15.1, -49.2). **Vector** length 125, 44.1% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.9 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.9 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -12.5 | -12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.8 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -19.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -22.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.6 | -8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.0 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.2 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | CDKAL1 threonylcarbamoyladenosine tRNA methylthiotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:20,534,457-21,232,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20342 |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing; DNA/RNA methyltransferases |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VV42](https://www.uniprot.org/uniprotkb/Q5VV42) (Threonylcarbamoyladenosine tRNA methylthiotransferase):

> Catalyzes the methylthiolation of N6-threonylcarbamoyladenosine (t(6)A), leading to the formation of 2-methylthio-N6-threonylcarbamoyladenosine (ms(2)t(6)A) at position 37 in tRNAs that read codons beginning with adenine.

**Summary**, from NCBI Gene [54901](https://www.ncbi.nlm.nih.gov/gene/54901):

> The protein encoded by this gene is a member of the methylthiotransferase family. The function of this gene is not known. Genome-wide association studies have linked single nucleotide polymorphisms in an intron of this gene with susceptibilty to type 2 diabetes. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:21050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21050) · Entrez [54901](https://www.ncbi.nlm.nih.gov/gene/54901) · UniProt [Q5VV42](https://www.uniprot.org/uniprotkb/Q5VV42) · Ensembl [ENSG00000145996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145996)

## Data

Gene col 7051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7051); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7051]; `tensor/DDL_lfc|DDL_z.npy` [7051]; `embed/gene_vectors.npy` [7051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7051 or target_col == 7051). Every well: [[CDKAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
