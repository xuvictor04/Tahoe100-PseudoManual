---
symbol: "MFSD8"
type: "gene"
col: 8855
ensembl_id: "ENSG00000164073"
name: "major facilitator superfamily domain containing 8"
location: "4q28.2"
module: 15
arm: "+"
pooled_cpm: 33.44
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MFSD8

*major facilitator superfamily domain containing 8* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +14.7, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.533× (z -9.7, q 1e-19, down in 28 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.337× (z -9.5, q 5e-19, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APTR]] (+0.73, fdr 7e-06), [[WDR20]] (+0.71, fdr 1e-05), [[NUP133]] (+0.70, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.67, fdr 7e-06), [[SRSF3]] (-0.63, fdr 1e-05), [[FAT1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +14.7 | 0e+00 | 44/47 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.1 | 2e-13 | 39/47 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.007 | 22/47 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.021 | 20/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +3.4 | 0.088 | 12/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.23× | +3.2 | 0.12 | 15/47 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.19 | 11/47 (SW480, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -9.7 | 1e-19 | 28/40 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.337×** | -9.5 | 5e-19 | 34/48 (NCI-H1573, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.570×** | -9.4 | 1e-18 | 40/47 (HOP62, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.571×** | -9.4 | 1e-18 | 33/44 (NCI-H1573, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.678×** | -9.2 | 4e-18 | 30/46 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.628×** | -7.5 | 7e-12 | 30/47 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.660×** | -6.7 | 2e-09 | 24/38 (SW480, NCI-H1573, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.695×** | -6.1 | 8e-08 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.701×** | -5.9 | 2e-07 | 30/46 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.713×** | -5.4 | 3e-06 | 27/46 (A549, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -5.3 | 6e-06 | 27/47 (SW48, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -5.0 | 3e-05 | 23/47 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.743×** | -5.0 | 3e-05 | 25/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.004 | 18/47 (H4, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.809×** | -3.5 | 0.015 | 17/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.674×** | -3.5 | 0.019 | 12/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.678×** | -3.4 | 0.019 | 20/45 (SNU-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.874× | -3.2 | 0.037 | 15/47 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.823×** | -3.1 | 0.043 | 18/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 11 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SW480 (line)]] | alt | 26.1 | 2 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -10.2) |
| [[A498 (line)]] | wt | 42.6 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -16.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[PANC-1 (line)]] | alt | 33.5 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HOP62 (line)]] | alt | 35.0 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.283× (z -10.8) |
| [[A-172 (line)]] | wt | 38.3 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.341× (z -9.8) |
| [[A549 (line)]] | wt | 33.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 49.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 54.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 34.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 35.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 35.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LS 180 (line)]] | wt | 41.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.3) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.224× (z -10.7) |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0717× (z -16.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -10.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[BT-474 (line)]] | alt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HCT15 (line)]] | alt | 54.9 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.101× (z -8.9) |
| [[LoVo (line)]] | wt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[Panc 03.27 (line)]] | alt | 37.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SW1417 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.8) | — |
| [[SW48 (line)]] | wt | 37.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTR]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[WDR20]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[NUP133]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[FAHD2A]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TRAPPC13]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[DENND10]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[INTS8]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ORMDL1]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ABHD18]] | +0.64 | +0.68 / +0.66 | both halves | 7e-06 | STRING 524; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PPOX]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IFI27L1]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.67 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[SRSF3]] | -0.63 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[FAT1]] | -0.61 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.60 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[DUSP2]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[JUNB]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[AIG1]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PCNX2]] | -0.57 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[PPP1R10]] | -0.57 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[FGGY]] | -0.57 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CSRNP1]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[GDF11]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MFSD8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.3, 22.8); signed map (-0.2, 0.8). **Vector** length 90.4, 21.4% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | -0.3 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.6 | -0.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -5.6 | -9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | major facilitator superfamily domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:127,917,799-127,966,034 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC74A1, MGC33302; previously CLN7 |
| Gene groups (HGNC) | Solute carrier family 74 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHS3](https://www.uniprot.org/uniprotkb/Q8NHS3) (Major facilitator superfamily domain-containing protein 8):

> Outward-rectifying chloride channel involved in endolysosomal chloride homeostasis, membrane fusion and function. Conducts chloride currents up to hundreds of picoamperes. Regulates lysosomal calcium content by reducing the lysosomal membrane potential, thereby activating TRPML1 channel and further release of lysosomal calcium ions. Regulates the pH in endolysosomal compartments and may contribute to progressive acidification from endosome to lysosome. Permeable to other halides such as iodide …

**Summary**, from NCBI Gene [256471](https://www.ncbi.nlm.nih.gov/gene/256471):

> This gene encodes a ubiquitous integral membrane protein that contains a transporter domain and a major facilitator superfamily (MFS) domain. Other members of the major facilitator superfamily transport small solutes through chemiosmotic ion gradients. The substrate transported by this protein is unknown. The protein likely localizes to lysosomal membranes. Mutations in this gene are correlated with a variant form of late infantile-onset neuronal ceroid lipofuscinoses (vLINCL). [provided by …

**Accessions** — [HGNC:28486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28486) · Entrez [256471](https://www.ncbi.nlm.nih.gov/gene/256471) · UniProt [Q8NHS3](https://www.uniprot.org/uniprotkb/Q8NHS3) · Ensembl [ENSG00000164073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164073)

## Data

Gene col 8855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8855); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8855]; `tensor/DDL_lfc|DDL_z.npy` [8855]; `embed/gene_vectors.npy` [8855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8855 or target_col == 8855). Every well: [[MFSD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
