---
symbol: "INVS"
type: "gene"
col: 4073
ensembl_id: "ENSG00000119509"
name: "inversin"
location: "9q31.1"
module: 185
arm: "+"
pooled_cpm: 118.34
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# INVS

*inversin* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.54× (z +6.8, q 6e-09, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.48× (z +6.5, q 3e-08, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 0.5 µM in 5 lines (NCI-H1573 3.43×, COLO 205 2.72×, LoVo 2.02×, KATO III 2.09×, …); [[Ixazomib citrate (drug)]] 5 µM in 4 lines (COLO 205 3.23×, NCI-H1573 3.18×, A-172 2.08×, LoVo 1.84×; ⚠ cell-cycle shift, explains ~50% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 2.41×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.292× (z -28.9, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.529× (z -10.6, q 3e-24, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP1]] (+0.70, fdr 7e-06), [[TOMM22]] (+0.69, fdr 1e-05), [[LINC00630]] (+0.69, fdr 7e-06); moves opposite to [[PLXNB2]] (-0.52, fdr 3e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDC42BPG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4073.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 0.5 µM in 5 lines (NCI-H1573 3.43×, COLO 205 2.72×, LoVo 2.02×, KATO III 2.09×, …); [[Ixazomib citrate (drug)]] 5 µM in 4 lines (COLO 205 3.23×, NCI-H1573 3.18×, A-172 2.08×, LoVo 1.84×; ⚠ cell-cycle shift, explains ~50% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 2.41×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.54×** | +6.8 | 6e-09 | 37/48 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +6.5 | 3e-08 | 32/48 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.39×** | +5.4 | 1e-05 | 31/48 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +5.2 | 3e-05 | 28/48 (LoVo, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.5 | 0.047 | 23/48 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.074 | 22/48 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.29× | +3.2 | 0.11 | 18/48 (NCI-H1573, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.292×** | -28.9 | 0e+00 | 47/48 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.309×** | -18.7 | 0e+00 | 48/48 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.385×** | -15.8 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -14.3 | 2e-44 | 45/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.432×** | -13.4 | 8e-39 | 45/47 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.487×** | -11.9 | 7e-31 | 41/49 (HCT15, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.507×** | -11.3 | 1e-27 | 40/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -10.7 | 5e-25 | 37/45 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -10.6 | 3e-24 | 40/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.565×** | -9.1 | 5e-18 | 35/44 (SNU-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.578×** | -9.1 | 5e-18 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -7.7 | 9e-13 | 32/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -7.0 | 1e-10 | 38/47 (MIA PaCa-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.674×** | -6.5 | 2e-09 | 33/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.698×** | -6.0 | 1e-07 | 39/48 (SW 1271, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.4 | 4e-04 | 26/50 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.665×** | -3.5 | 0.012 | 21/48 (SW480, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.811×** | -3.5 | 0.015 | 26/48 (LoVo, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.685×** | -3.3 | 0.029 | 25/48 (Panc 03.27, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.876× | -3.1 | 0.052 | 7/49 (C-33 A, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.834× | -3.0 | 0.068 | 20/47 (H4, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.068 | 16/48 (BT-474, AN3 CA, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -2.9 | 0.086 | 11/49 (LOX-IMVI, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 188 | 0 | 16 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -30.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.233× (z -18.2) |
| [[A-172 (line)]] | wt | 210 | 2 (1 ⚠) | 13 (10 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -28.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 185 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -21.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -15.7) |
| [[J82 (line)]] | alt | 148 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -31.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.334× (z -11.6) |
| [[SNU-1 (line)]] | wt | 159 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.289× (z -10.7) |
| [[SW480 (line)]] | alt | 152 | 0 | 11 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.349× (z -14.9) |
| [[H4 (line)]] | wt | 197 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -26.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.357× (z -10.5) |
| [[HOP62 (line)]] | alt | 128 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -26.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.6) |
| [[LoVo (line)]] | wt | 125 | 2 (1 ⚠) | 8 (8 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.02× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -22.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 119 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -28.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.298× (z -13.1) |
| [[COLO 205 (line)]] | alt | 133 | 3 (2 ⚠) | 6 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +11.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.72× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -28.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 154 | 1 | 8 (8 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -19.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 110 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 147 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.452× (z -9.5) |
| [[PANC-1 (line)]] | alt | 73.6 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -24.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.471× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 162 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -21.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 149 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -26.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.318× (z -12.7) |
| [[A498 (line)]] | wt | 127 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -27.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 142 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -23.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 126 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.2) |
| [[HCT15 (line)]] | alt | 182 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -10.0) |
| [[Hs 766T (line)]] | wt | 120 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 46.9 | 1 (1 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 100 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -18.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -17.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 53.6 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.43× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -16.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 89.7 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -17.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 191 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 145 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.387× (z -11.4) |
| [[SW 900 (line)]] | alt | 63.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 49.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.270× (z -10.4) |
| [[C-33 A (line)]] | alt | 148 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 84.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -21.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 82.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 86.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 77.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 88.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -17.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 58.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.174× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H2122 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TOMM22]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[LINC00630]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CDC123]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[FTO]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[KIAA1143]] | +0.66 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[TMEM161A]] | +0.66 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.65 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 | same gene group |
| [[MRPS27]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[VTI1A]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.62 | +0.69 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNB2]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | B | CDC42BPG activity lowers INVS's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.48× higher at baseline in the lines without CDC42BPG | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers INVS's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.6, -12.7); signed map (-21.6, -24.4). **Vector** length 108, 39.6% of its response variance represented; |z| ≥ 3 in 1,249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.9 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +12.8 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | +11.9 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.9 | -28.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.9 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.0 | -11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.7 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | inversin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:100,099,243-100,302,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NPHP2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Inversin complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y283](https://www.uniprot.org/uniprotkb/Q9Y283) (Inversin):

> Required for normal renal development and establishment of left-right axis. Probably acts as a molecular switch between different Wnt signaling pathways. Inhibits the canonical Wnt pathway by targeting cytoplasmic disheveled (DVL1) for degradation by the ubiquitin-proteasome. This suggests that it is required in renal development to oppose the repression of terminal differentiation of tubular epithelial cells by Wnt signaling. Involved in the organization of apical junctions in kidney cells …

**Summary**, from NCBI Gene [27130](https://www.ncbi.nlm.nih.gov/gene/27130):

> This gene encodes a protein containing multiple ankyrin domains and two IQ calmodulin-binding domains. The encoded protein may function in renal tubular development and function, and in left-right axis determination. This protein interacts with nephrocystin and infers a connection between primary cilia function and left-right axis determination. A similar protein in mice interacts with calmodulin. Mutations in this gene have been associated with nephronophthisis type 2. Multiple transcript …

**Accessions** — [HGNC:17870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17870) · Entrez [27130](https://www.ncbi.nlm.nih.gov/gene/27130) · UniProt [Q9Y283](https://www.uniprot.org/uniprotkb/Q9Y283) · Ensembl [ENSG00000119509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119509)

## Data

Gene col 4073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4073); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4073]; `tensor/DDL_lfc|DDL_z.npy` [4073]; `embed/gene_vectors.npy` [4073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4073 or target_col == 4073). Every well: [[INVS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INVS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
