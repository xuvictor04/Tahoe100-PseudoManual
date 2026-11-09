---
symbol: "KLF7"
type: "gene"
col: 3977
ensembl_id: "ENSG00000118263"
name: "KLF transcription factor 7"
location: "2q33.3"
module: 13
arm: "+"
pooled_cpm: 214.63
n_lines_expressing: 38
n_dd_up: 5
n_dd_down: 53
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# KLF7

*KLF transcription factor 7* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.65× (z +8.8, q 9e-16, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 53 drug-doses (27 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.240× (z -17.8, q 0e+00, down in 30 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.384× (z -12.4, q 4e-33, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL2]] (+0.66, fdr 7e-06), [[TUBA1A]] (+0.58, fdr 1e-05), [[VEGFC]] (+0.57, fdr 1e-05); moves opposite to [[PHKA1]] (-0.55, fdr 1e-05), [[FAM53B]] (-0.50, fdr 4e-05, ⚠ FAM53B in the vector space only through flagged drug-doses), [[CDH26]] (-0.49, fdr 2e-05), [[RAVER2]] (-0.47, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SLC8A1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RAP1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.65×** | +8.8 | 9e-16 | 33/37 (A-172, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.81×** | +7.4 | 3e-11 | 34/35 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.73×** | +7.1 | 2e-10 | 32/35 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +5.1 | 5e-05 | 21/36 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.073 | 18/38 (HOP62, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.30× | +3.2 | 0.14 | 19/38 (HOP62, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.59× | +3.1 | 0.14 | 18/36 (HOP62, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 28 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 53 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.240×** | -17.8 | 0e+00 | 30/34 (A-172, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.334×** | -13.7 | 6e-40 | 35/35 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.384×** | -12.4 | 4e-33 | 35/36 (SK-MEL-2, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.385×** | -12.4 | 5e-33 | 34/37 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.400×** | -11.4 | 4e-28 | 32/35 (C32, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.411×** | -10.6 | 2e-24 | 31/34 (A-172, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.446×** | -10.4 | 1e-23 | 27/36 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.476×** | -9.6 | 6e-20 | 28/36 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.606×** | -9.1 | 4e-18 | 30/37 (A549, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.516×** | -8.6 | 6e-16 | 29/36 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.541×** | -8.0 | 9e-14 | 28/36 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -7.5 | 3e-12 | 33/36 (SK-MEL-2, H4, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.553×** | -7.4 | 8e-12 | 33/36 (A-172, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.555×** | -7.3 | 1e-11 | 30/38 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -7.1 | 6e-11 | 28/36 (CFPAC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[NG25 (drug)]] 5 µM |  | **0.422×** | -5.8 | 2e-07 | 32/35 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -5.8 | 3e-07 | 27/36 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.694×** | -4.7 | 6e-05 | 22/37 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.507×** | -4.6 | 1e-04 | 28/36 (LoVo, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -4.2 | 4e-04 | 19/36 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.721×** | -4.2 | 4e-04 | 24/36 (A498, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.725×** | -4.1 | 6e-04 | 25/36 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.9 | 0.002 | 21/36 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.735×** | -3.8 | 0.002 | 20/37 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.737×** | -3.8 | 0.002 | 22/37 (A498, SNU-423, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.006 | 19/36 (A498, A549, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.764×** | -3.5 | 0.008 | 20/36 (A498, Hs 766T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.763×** | -3.4 | 0.011 | 22/36 (C32, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.73 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 360 | 3 | 13 (12 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.87× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -18.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 469 | 0 | 15 (13 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.141× (z -15.0) |
| [[A-172 (line)]] | wt | 634 | 2 | 12 (10 ⚠) | [[TAK-901 (drug)]] 5 µM 6.29× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.587× (z -8.7) |
| [[HOP62 (line)]] | alt | 352 | 2 | 12 (11 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.34× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.214× (z -16.5) |
| [[C32 (line)]] | wt | 241 | 1 | 12 (9 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.93× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -22.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.144× (z -19.9) |
| [[NCI-H23 (line)]] | alt | 276 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.194× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 235 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -9.5) |
| [[HS-578T (line)]] | alt | 506 | 1 | 10 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 7.01× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.183× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 305 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -20.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 305 | 1 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) ⚠ cell-cycle shift, explains ~44% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A549 (line)]] | wt | 451 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 6.34× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -19.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 311 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.249× (z -10.4) |
| [[J82 (line)]] | alt | 660 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 213 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.29× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.246× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 236 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -14.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.346× (z -10.3) |
| [[H4 (line)]] | wt | 259 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.170× (z -13.2) |
| [[Hs 766T (line)]] | wt | 290 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 9.16× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 95.8 | 1 | 5 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.38× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.180× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.236× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 262 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.121× (z -22.7) |
| [[SNU-423 (line)]] | alt | 315 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0923× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -13.4) |
| [[C-33 A (line)]] | alt | 140 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.5) ⚠ cell-cycle shift, explains ~44% of this change | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.298× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 219 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.84× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 237 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.272× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -9.4) |
| [[CHP-212 (line)]] | wt | 325 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 134 | 2 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.69× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.345× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -10.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 166 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.55× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 209 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.282× (z -9.0) |
| [[SW 900 (line)]] | alt | 186 | 1 | 2 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.97× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 63.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.307× (z -10.5) |
| [[BT-474 (line)]] | alt | 155 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.299× (z -8.8) |
| [[SW 1088 (line)]] | alt | 386 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW 1271 (line)]] | alt | 195 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.153× (z -8.8) |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 29.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 40.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL2]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TUBA1A]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VEGFC]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[STK10]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.55 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[FERMT2]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF267]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 | same gene group |
| [[NAV1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[ABCA1]] | +0.53 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[HRH1]] | +0.53 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[FRMD6]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA1]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[FAM53B]] ⚠ | -0.50 | -0.50 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDH26]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RAVER2]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[LRP5]] | -0.47 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[NFIA]] | -0.47 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RPH3AL]] | -0.45 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[MYO5C]] | -0.45 | -0.47 / -0.31 | both halves | 2e-04 | same gene group |
| [[ACTR3C]] | -0.44 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[MGST2]] | -0.44 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[DMTN]] | -0.43 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[PROM1]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[FAM217B]] | -0.43 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC8A1]] | B | SLC8A1 activity raises KLF7's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 4.20× lower at baseline in the lines without SLC8A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[SPOCD1]] | B | SPOCD1 activity strengthens KLF7's drug response | lines that do not express SPOCD1 (16) vs lines expressing it (21) | the lines without SPOCD1 respond 0.64× as strongly (z diff +2.66); strongest at Belinostat 5 µM: 0.74x vs 0.36x (z diff +5.7) | 0.034 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; target measured in part of the lines; artifact flags |
| [[DUSP10]] | B | DUSP10 activity raises KLF7's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.40× lower at baseline in the lines without DUSP10 | 0.038 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[F3]] | B | F3 activity raises KLF7's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without F3 | 0.039 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[FAM107B]] | B | FAM107B activity raises KLF7's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without FAM107B | 0.044 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[NFIA]] | B | NFIA activity weakens KLF7's drug response | lines that do not express NFIA (9) vs lines expressing it (28) | the lines without NFIA respond 1.47× as strongly (z diff -2.32); strongest at Belinostat 5 µM: 0.34x vs 0.57x (z diff -4.2) | 0.055 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EXT1]] | C | EXT1 activity raises KLF7's level | lines that do not express EXT1 (3) vs lines expressing it (47) | 4.56× lower at baseline in the lines without EXT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, B4GALT1, RIGI; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAP1B]] | B | KLF7 activity raises RAP1B's level | lines that do not express KLF7 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without KLF7 | 0.046 | ⚠ within organs, on part of the lines; also absent: MYOSLID, CTSF, MPDZ |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.2, 11.6); signed map (21.6, 50.6). **Vector** length 115, 41.8% of its response variance represented; |z| ≥ 3 in 1,641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.6 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.4 | -9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.1 | +7.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.8 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -3.2 | -11.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:207,074,137-207,173,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UKLF |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors; MicroRNA protein coding host genes |
| Hallmark sets | COAGULATION, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [O75840](https://www.uniprot.org/uniprotkb/O75840) (Krueppel-like factor 7):

> Transcriptional factor. Plays a critical role in neuronal morphogenesis and survival of sensory neurons (By similarity). Represses the corneal epithelium differentiation. Also acts as a metabolic regulator, by modulating insulin sensitivity in pancreatic beta cells and skeletal muscle cells. Inhibits transcriptional inducers of adipogenesis and has a repressive role in the expression of several adipokines, including leptin.

**Summary**, from NCBI Gene [8609](https://www.ncbi.nlm.nih.gov/gene/8609):

> The protein encoded by this gene is a member of the Kruppel-like transcriptional regulator family. Members in this family regulate cell proliferation, differentiation and survival and contain three C2H2 zinc fingers at the C-terminus that mediate binding to GC-rich sites. This protein may contribute to the progression of type 2 diabetes by inhibiting insulin expression and secretion in pancreatic beta-cells and by deregulating adipocytokine secretion in adipocytes. A pseudogene of this gene is …

**Accessions** — [HGNC:6350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6350) · Entrez [8609](https://www.ncbi.nlm.nih.gov/gene/8609) · UniProt [O75840](https://www.uniprot.org/uniprotkb/O75840) · Ensembl [ENSG00000118263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118263)

## Data

Gene col 3977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3977); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3977]; `tensor/DDL_lfc|DDL_z.npy` [3977]; `embed/gene_vectors.npy` [3977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3977 or target_col == 3977). Every well: [[KLF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
