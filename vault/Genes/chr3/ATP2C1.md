---
symbol: "ATP2C1"
type: "gene"
col: 301
ensembl_id: "ENSG00000017260"
name: "ATPase secretory pathway Ca2+ transporting 1"
location: "3q22.1"
module: 60
arm: "+"
pooled_cpm: 207.33
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# ATP2C1

*ATPase secretory pathway Ca2+ transporting 1* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.10× (z +17.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.658× (z -14.1, q 1e-42, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACYBP]] (+0.74, fdr 7e-06), [[AHSA1]] (+0.72, fdr 7e-06), [[TMEM161A]] (+0.68, fdr 1e-05); moves opposite to [[HELQ]] (-0.65, fdr 7e-06), [[RELB]] (-0.65, fdr 1e-05), [[TXNIP]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CTH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.10×** | +17.7 | 0e+00 | 48/48 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.04×** | +17.0 | 0e+00 | 47/48 (A498, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.07×** | +16.4 | 0e+00 | 48/48 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +11.3 | 2e-27 | 39/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +8.6 | 6e-16 | 38/45 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +6.9 | 6e-10 | 40/49 (MIA PaCa-2, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.1 | 2e-05 | 26/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.7 | 2e-04 | 24/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 28/48 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.9 | 0.006 | 17/49 (A-172, SNU-423, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.5 | 0.024 | 11/49 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.090 | 16/47 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.14× | +3.0 | 0.10 | 16/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -14.1 | 1e-42 | 33/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -11.5 | 4e-28 | 43/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -8.4 | 1e-14 | 37/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -7.3 | 5e-11 | 33/47 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.759×** | -6.3 | 3e-08 | 32/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.782×** | -5.9 | 4e-07 | 29/48 (HOP62, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.785×** | -5.4 | 6e-06 | 25/45 (A549, SW48, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.804×** | -5.2 | 1e-05 | 27/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.806×** | -5.1 | 2e-05 | 31/48 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -4.4 | 7e-04 | 20/48 (A-172, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.842× | -4.1 | 0.002 | 21/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.856× | -3.7 | 0.009 | 20/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.859× | -3.7 | 0.011 | 13/49 (BT-474, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.5 | 0.020 | 15/48 (NCI-H1792, HS-578T, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.904× | -3.4 | 0.024 | 2/48 (H4, CHP-212) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 230 | 3 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 266 | 5 (1 ⚠) | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.38× (z +16.1) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 247 | 6 (1 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 3.10× (z +17.2) | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -11.2) |
| [[HOP62 (line)]] | alt | 287 | 4 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.15× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -11.1) |
| [[KATO III (line)]] | alt | 174 | 4 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.59× (z +15.7) | [[Homoharringtonine (drug)]] 5 µM 0.660× (z -9.8) |
| [[LoVo (line)]] | wt | 175 | 4 (1 ⚠) | 2 | [[Bortezomib (drug)]] 0.05 µM 2.29× (z +13.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.425× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 146 | 4 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +16.8) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 261 | 4 | 2 | [[Bortezomib (drug)]] 0.05 µM 2.09× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -11.9) |
| [[RKO (line)]] | wt | 206 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +14.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -10.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 312 | 3 | 3 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -11.9) |
| [[A-427 (line)]] | wt | 281 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +17.0) | — |
| [[A498 (line)]] | wt | 175 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.42× (z +18.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -10.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 125 | 3 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.13× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 78.1 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.44× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 217 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.33× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 230 | 3 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.81× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -11.5) |
| [[H4 (line)]] | wt | 348 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -12.3) |
| [[HT-29 (line)]] | alt | 127 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.02× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 188 | 2 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -16.0) |
| [[J82 (line)]] | alt | 193 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 196 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 266 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +14.6) | — |
| [[SNU-423 (line)]] | alt | 209 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -16.1) |
| [[SW1417 (line)]] | alt | 212 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +14.9) | — |
| [[SW48 (line)]] | wt | 218 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -10.5) |
| [[SW480 (line)]] | alt | 151 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.27× (z +17.1) | — |
| [[C-33 A (line)]] | alt | 183 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.69× (z +13.4) | — |
| [[C32 (line)]] | wt | 219 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.00× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.600× (z -9.5) |
| [[Hs 766T (line)]] | wt | 101 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.94× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 367 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.90× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 247 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 1.92× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 283 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -28.5) |
| [[NCI-H2030 (line)]] | alt | 116 | 2 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.13× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.607× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 277 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.441× (z -12.6) |
| [[SNU-1 (line)]] | wt | 210 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.415× (z -9.5) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 138 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.49× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 185 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 200 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.13× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 309 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 197 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -15.7) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACYBP]] | +0.74 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[HSP90AB3P]] | +0.67 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[OTULIN]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.66 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.66 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[CNIH1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HSP90AB2P]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TCP1]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[HSPD1]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELQ]] | -0.65 | -0.74 / -0.64 | both halves | 7e-06 |  |
| [[RELB]] | -0.65 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[TXNIP]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[LIPT1]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[EP300]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TGIF2]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.60 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.60 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[PRPF38B]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[PER2]] | -0.58 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTH]] | B | CTH activity raises ATP2C1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without CTH | 0.024 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers ATP2C1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.772). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.5, -11.7); signed map (-26.7, -28.2). **Vector** length 124, 40.3% of its response variance represented; |z| ≥ 3 in 1,238 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.57 to 4); *MYC targets v1* (hallmark, mean cos +0.58 to 9); *Chaperone Mediated Autophagy* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +13.2 | +17.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +12.3 | +16.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.9 | +17.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.6 | +11.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +9.1 | +8.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.5 | -11.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -7.4 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -6.5 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase secretory pathway Ca2+ transporting 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:130,850,595-131,016,712 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1347, ATP2C1A, PMR1, SPCA1; previously BCPM |
| Gene groups (HGNC) | ATPases Ca2+ transporting |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P98194](https://www.uniprot.org/uniprotkb/P98194) (Calcium-transporting ATPase type 2C member 1):

> ATP-driven pump that supplies the Golgi apparatus with Ca(2+) and Mn(2+) ions, both essential cofactors for processing and trafficking of newly synthesized proteins in the secretory pathway. Within a catalytic cycle, acquires Ca(2+) or Mn(2+) ions on the cytoplasmic side of the membrane and delivers them to the lumenal side. The transfer of ions across the membrane is coupled to ATP hydrolysis and is associated with a transient phosphorylation that shifts the pump conformation from …

**Summary**, from NCBI Gene [27032](https://www.ncbi.nlm.nih.gov/gene/27032):

> The protein encoded by this gene belongs to the family of P-type cation transport ATPases. This magnesium-dependent enzyme catalyzes the hydrolysis of ATP coupled with the transport of calcium ions. Defects in this gene cause Hailey-Hailey disease, an autosomal dominant disorder. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:13211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13211) · Entrez [27032](https://www.ncbi.nlm.nih.gov/gene/27032) · UniProt [P98194](https://www.uniprot.org/uniprotkb/P98194) · Ensembl [ENSG00000017260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000017260)

## Data

Gene col 301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 301); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 301]; `tensor/DDL_lfc|DDL_z.npy` [301]; `embed/gene_vectors.npy` [301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 301 or target_col == 301). Every well: [[ATP2C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
