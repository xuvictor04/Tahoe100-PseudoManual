---
symbol: "RNASEH1"
type: "gene"
col: 10179
ensembl_id: "ENSG00000171865"
name: "ribonuclease H1"
location: "2p25.3"
module: 5
arm: "+"
pooled_cpm: 35.96
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RNASEH1

*ribonuclease H1* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.82× (z +21.9, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.13× (z +15.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.660× (z -8.8, q 8e-16, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNT1]] (+0.76, fdr 7e-06), [[PSME3]] (+0.69, fdr 7e-06), [[ABCF2]] (+0.69, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.67, fdr 1e-05), [[PLEKHH3]] (-0.67, fdr 1e-05), [[CARHSP1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TNNI3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 25 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.82×** | +21.9 | 0e+00 | 44/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.75×** | +20.5 | 0e+00 | 34/37 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +17.1 | 0e+00 | 37/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +15.9 | 0e+00 | 45/48 (SW480, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +15.9 | 0e+00 | 43/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +11.1 | 8e-27 | 35/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.7 | 1e-24 | 33/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +8.3 | 6e-15 | 29/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.30×** | +7.8 | 4e-13 | 26/47 (HOP62, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +7.8 | 4e-13 | 27/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +6.8 | 5e-10 | 26/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.8 | 6e-10 | 29/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 7e-10 | 26/48 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.39×** | +6.7 | 8e-10 | 22/47 (A-172, RPMI-7951, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +6.0 | 8e-08 | 31/48 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.69×** | +5.8 | 2e-07 | 29/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.1 | 1e-05 | 18/48 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +4.8 | 3e-05 | 18/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.6 | 1e-04 | 18/48 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.4 | 2e-04 | 18/48 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 4e-04 | 18/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.001 | 17/47 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.002 | 20/47 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.004 | 9/48 (C-33 A, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.660×** | -8.8 | 8e-16 | 34/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.9 | 9e-07 | 26/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.815×** | -4.3 | 0.003 | 16/48 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.681×** | -4.3 | 0.003 | 16/47 (LOX-IMVI, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.697×** | -4.0 | 0.007 | 15/47 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.711×** | -3.8 | 0.014 | 13/48 (A-172, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.7 | 0.016 | 1/48 (NCI-H23) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.847× | -3.4 | 0.047 | 11/48 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.900× | -3.2 | 0.096 | 8/48 (CHP-212, NCI-H460, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.867× | -3.0 | 0.13 | 7/48 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.7 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.50× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 28.4 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +12.1) | — |
| [[LoVo (line)]] | wt | 35.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 52.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +13.7) | — |
| [[A498 (line)]] | wt | 63.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.0) | — |
| [[KATO III (line)]] | alt | 41.5 | 3 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.62× (z +11.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 48.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 18.1 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.25× (z +9.2) | — |
| [[A-172 (line)]] | wt | 36.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.89× (z +10.3) | — |
| [[A549 (line)]] | wt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 28.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.07× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 32.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.76× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 86.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.4) | — |
| [[J82 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.52× (z +8.5) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.141× (z -11.9) |
| [[SW 900 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | +0.76 | +0.65 / +0.73 | both halves | 7e-06 | STRING 521 |
| [[PSME3]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DESI1]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[AVEN]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ALG8]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ARMC6]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[AFG3L1P]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PIGW]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ADAT1]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.67 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.67 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.62 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MARCHF9]] | -0.61 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TOMM7]] | -0.61 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ARL3]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[TMEM256]] | -0.61 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[TNNI3]] | -0.60 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[YPEL2]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NRTN]] | -0.60 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FBXO33]] | -0.60 | -0.64 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNI3]] | B | TNNI3 activity raises RNASEH1's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.27× lower at baseline in the lines without TNNI3 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BCL11A]] | B | BCL11A activity lowers RNASEH1's level | lines that do not express BCL11A (20) vs lines expressing it (30) | 1.15× higher at baseline in the lines without BCL11A | 0.094 | ⚠ within organs, on part of the lines; also absent: VWDE, HEYL, HS6ST2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (7.1, -8.5); signed map (-6.5, -41.7). **Vector** length 90.4, 21.8% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +15.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +15.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease H1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:3,541,430-3,558,333 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; DNA Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [O60930](https://www.uniprot.org/uniprotkb/O60930) (Ribonuclease H1):

> Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. Plays a role in RNA polymerase II (RNAp II) transcription termination by degrading R-loop RNA-DNA hybrid formation at G-rich pause sites located downstream of the poly(A) site and behind the elongating RNAp II.

**Summary**, from NCBI Gene [246243](https://www.ncbi.nlm.nih.gov/gene/246243):

> This gene encodes an endonuclease that specifically degrades the RNA of RNA-DNA hybrids and plays a key role in DNA replication and repair. Alternate in-frame start codon initiation results in the production of alternate isoforms that are directed to the mitochondria or to the nucleus. The production of the mitochondrial isoform is modulated by an upstream open reading frame (uORF). Mutations in this gene have been found in individuals with progressive external ophthalmoplegia with …

**Accessions** — [HGNC:18466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18466) · Entrez [246243](https://www.ncbi.nlm.nih.gov/gene/246243) · UniProt [O60930](https://www.uniprot.org/uniprotkb/O60930) · Ensembl [ENSG00000171865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171865)

## Data

Gene col 10179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10179); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10179]; `tensor/DDL_lfc|DDL_z.npy` [10179]; `embed/gene_vectors.npy` [10179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10179 or target_col == 10179). Every well: [[RNASEH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
