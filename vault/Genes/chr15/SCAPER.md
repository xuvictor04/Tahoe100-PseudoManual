---
symbol: "SCAPER"
type: "gene"
col: 6399
ensembl_id: "ENSG00000140386"
name: "S-phase cyclin A associated protein in the ER"
location: "15q24.3"
module: 185
arm: "+"
pooled_cpm: 169.57
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# SCAPER

*S-phase cyclin A associated protein in the ER* — 15q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.35× (z +4.8, q 1e-03, up in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 2.97×, hTERT-HPNE 2.53×, NCI-H2347 1.80×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (21 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.354× (z -16.4, q 0e+00, down in 46 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.528× (z -10.4, q 2e-23, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP112]] (+0.61, fdr 1e-05), [[RAD51B]] (+0.60, fdr 3e-05), [[VPS13B]] (+0.60, fdr 1e-05); moves opposite to [[ZNF341]] (-0.48, fdr 3e-05), [[MAP3K14-AS1]] (-0.47, fdr 2e-04), [[MOGS]] (-0.46, fdr 5e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 2.97×, hTERT-HPNE 2.53×, NCI-H2347 1.80×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 1e-03 | 34/47 (HepG2/C3A, C-33 A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 0.002 | 37/47 (HepG2/C3A, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.26×** | +3.7 | 0.040 | 29/50 (C-33 A, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.47× | +3.3 | 0.12 | 25/50 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.1 | 0.17 | 17/48 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.17 | 8/49 (C-33 A, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.18 | 21/49 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.354×** | -16.4 | 0e+00 | 46/47 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.411×** | -14.5 | 1e-45 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.453×** | -12.9 | 5e-36 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.528×** | -10.4 | 2e-23 | 42/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -10.1 | 5e-22 | 37/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.582×** | -8.8 | 9e-17 | 37/49 (A-427, NCI-H1792, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -8.6 | 6e-16 | 40/49 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.609×** | -8.1 | 4e-14 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.593×** | -7.9 | 2e-13 | 32/45 (A-172, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.635×** | -7.4 | 7e-12 | 42/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -6.6 | 2e-09 | 38/48 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -6.6 | 2e-09 | 40/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.676×** | -6.4 | 8e-09 | 34/48 (LOX-IMVI, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.670×** | -6.3 | 1e-08 | 33/44 (AN3 CA, SNU-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -5.2 | 6e-06 | 29/48 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -3.5 | 0.012 | 15/48 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.816×** | -3.3 | 0.019 | 25/48 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.874× | -3.1 | 0.037 | 12/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.833×** | -3.0 | 0.050 | 21/48 (BT-474, AN3 CA, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.882× | -2.9 | 0.065 | 5/49 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.883× | -2.8 | 0.071 | 7/49 (Panc 03.27, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.842× | -2.8 | 0.078 | 21/48 (CFPAC-1, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 230 | 0 | 15 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.291× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 137 | 0 | 11 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -15.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.328× (z -13.5) |
| [[C32 (line)]] | wt | 214 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 176 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.374× (z -10.6) |
| [[SNU-1 (line)]] | wt | 254 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -17.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.9) |
| [[SW480 (line)]] | alt | 141 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -20.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.253× (z -19.9) |
| [[COLO 205 (line)]] | alt | 289 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.200× (z -19.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -11.5) |
| [[HOP62 (line)]] | alt | 161 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.289× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.344× (z -13.2) |
| [[KATO III (line)]] | alt | 232 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -17.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.406× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 186 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.368× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 245 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.331× (z -12.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.435× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 301 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -18.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -16.8) |
| [[A-172 (line)]] | wt | 202 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.2) |
| [[J82 (line)]] | alt | 183 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.252× (z -15.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.5) |
| [[HCT15 (line)]] | alt | 292 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.367× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.1) |
| [[HT-29 (line)]] | alt | 179 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.381× (z -12.2) |
| [[LoVo (line)]] | wt | 213 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.394× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -8.8) |
| [[PANC-1 (line)]] | alt | 182 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.348× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 204 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.232× (z -9.4) |
| [[Hs 766T (line)]] | wt | 136 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -13.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 191 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.310× (z -14.1) |
| [[C-33 A (line)]] | alt | 240 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -8.9) |
| [[A549 (line)]] | wt | 213 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.8) |
| [[BT-474 (line)]] | alt | 156 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.422× (z -9.7) |
| [[CHP-212 (line)]] | wt | 180 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[H4 (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 126 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +16.9) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.257× (z -14.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.446× (z -8.8) |
| [[LS 180 (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.415× (z -8.7) |
| [[RKO (line)]] | wt | 283 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -15.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.490× (z -9.7) |
| [[SNU-423 (line)]] | alt | 193 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.6) |
| [[A-427 (line)]] | wt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 85.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -10.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 266 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[hTERT-HPNE (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.345× (z -10.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -8.9) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.369× (z -11.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -11.6) ⚠ toxic |
| [[A498 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP112]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[RAD51B]] | +0.60 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[VPS13B]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[FER]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[MYO9A]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[LMLN]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NSMCE2]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SUMF1]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GMDS-DT]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PRH1]] | +0.54 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ATP9B]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FAF1]] | +0.53 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 | same gene group |
| [[MAP3K14-AS1]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[MOGS]] | -0.46 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ACSS1]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[SEPTIN7P14]] | -0.45 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[TMEM167A]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CEP295NL]] | -0.44 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[MSTO2P]] | -0.44 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[LINC01409]] | -0.44 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[EXTL3]] | -0.44 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[RWDD4]] | -0.44 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[SEPTIN7P13]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SCAPER's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.0, 30.2); signed map (10.3, -11.2). **Vector** length 100, 39.4% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.5 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +6.1 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.5 | -12.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Thymol (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.2 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.7 | -16.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | S-phase cyclin A associated protein in the ER |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.3 — chr15:76,347,904-76,905,444 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Zfp291; previously ZNF291 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers matrin-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY12](https://www.uniprot.org/uniprotkb/Q9BY12) (S phase cyclin A-associated protein in the endoplasmic reticulum):

> CCNA2/CDK2 regulatory protein that transiently maintains CCNA2 in the cytoplasm.

**Summary**, from NCBI Gene [49855](https://www.ncbi.nlm.nih.gov/gene/49855):

> Predicted to enable nucleic acid binding activity and zinc ion binding activity. Acts upstream of or within retina development in camera-type eye. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13081) · Entrez [49855](https://www.ncbi.nlm.nih.gov/gene/49855) · UniProt [Q9BY12](https://www.uniprot.org/uniprotkb/Q9BY12) · Ensembl [ENSG00000140386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140386)

## Data

Gene col 6399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6399); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6399]; `tensor/DDL_lfc|DDL_z.npy` [6399]; `embed/gene_vectors.npy` [6399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6399 or target_col == 6399). Every well: [[SCAPER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAPER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
