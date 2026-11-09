---
symbol: "PWWP3A"
type: "gene"
col: 8398
ensembl_id: "ENSG00000160953"
name: "PWWP domain containing 3A, DNA repair factor"
location: "19p13.3"
module: 60
arm: "+"
pooled_cpm: 29.17
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PWWP3A

*PWWP domain containing 3A, DNA repair factor* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.85× (z +17.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.427× (z -19.7, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AB3P]] (+0.70, fdr 7e-06), [[ANKRD39]] (+0.69, fdr 7e-06), [[SAMD4B]] (+0.68, fdr 1e-05); moves opposite to [[NFKB1]] (-0.65, fdr 1e-05), [[TAPBPL]] (-0.62, fdr 3e-05), [[CGGBP1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAT5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.85×** | +17.2 | 0e+00 | 46/48 (LoVo, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +10.6 | 7e-24 | 37/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +10.5 | 1e-23 | 35/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.4 | 4e-19 | 37/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +9.4 | 4e-19 | 37/47 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +8.4 | 3e-15 | 35/48 (KATO III, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +8.3 | 7e-15 | 38/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.4 | 8e-09 | 33/41 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 8e-06 | 30/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.2 | 1e-05 | 22/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.75×** | +4.8 | 8e-05 | 29/48 (LoVo, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 18/48 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **1.26×** | +3.9 | 0.005 | 18/44 (NCI-H1792, SHP-77, …) | two highest doses | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.028 | 14/47 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.22×** | +3.2 | 0.055 | 18/40 (NCI-H23, SHP-77, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.427×** | -19.7 | 0e+00 | 41/47 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.400×** | -15.0 | 0e+00 | 41/47 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.396×** | -14.6 | 0e+00 | 45/48 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.524×** | -10.6 | 5e-24 | 38/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -9.9 | 4e-21 | 36/48 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -9.5 | 2e-19 | 32/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -9.0 | 2e-17 | 35/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -8.0 | 1e-13 | 37/48 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.631×** | -7.5 | 3e-12 | 37/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.436×** | -7.1 | 7e-11 | 36/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -5.7 | 8e-07 | 7/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -5.5 | 2e-06 | 24/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -4.9 | 3e-05 | 23/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.774×** | -4.0 | 0.002 | 21/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -3.7 | 0.008 | 18/48 (A-172, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 42.2 | 3 | 6 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.57× (z +16.1) | [[Harringtonine (drug)]] 5 µM 0.190× (z -14.9) |
| [[SW480 (line)]] | alt | 35.7 | 3 | 6 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.45× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 69.6 | 1 | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.90× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -27.3) |
| [[A-172 (line)]] | wt | 38.9 | 1 | 5 | [[Auranofin (drug)]] 5 µM 4.32× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 31.0 | 2 | 4 | [[Auranofin (drug)]] 5 µM 5.25× (z +15.0) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.0) |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.9) |
| [[A-427 (line)]] | wt | 58.0 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.37× (z +15.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.0644× (z -28.1) |
| [[LOX-IMVI (line)]] | wt | 30.6 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.85× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.192× (z -13.1) |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -14.1) |
| [[LS 180 (line)]] | wt | 34.6 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.66× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0826× (z -16.8) |
| [[PANC-1 (line)]] | alt | 25.7 | 1 | 3 | [[Auranofin (drug)]] 5 µM 4.55× (z +15.0) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -11.5) |
| [[KATO III (line)]] | alt | 18.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.23× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.254× (z -10.9) |
| [[RKO (line)]] | wt | 27.7 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.49× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.248× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 24.4 | 1 | 2 | [[Auranofin (drug)]] 5 µM 5.48× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.101× (z -14.5) |
| [[BT-474 (line)]] | alt | 31.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.57× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.1) |
| [[HT-29 (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.87× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 18.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -10.0) |
| [[SW48 (line)]] | wt | 41.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.107× (z -12.7) |
| [[A498 (line)]] | wt | 35.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -14.6) |
| [[A549 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.9) |
| [[C-33 A (line)]] | alt | 45.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +11.0) | — |
| [[C32 (line)]] | wt | 24.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.08× (z +11.0) | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0697× (z -27.5) |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.5) |
| [[AN3 CA (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB3P]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SAMD4B]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.68 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[SH3PXD2B]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[HSP90AB2P]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[RBAK-RBAKDN]] | +0.65 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[TMEM161A]] | +0.65 | +0.68 / +0.57 | both halves | 8e-06 |  |
| [[DAP3]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[BICD2]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | +0.64 | +0.57 / +0.69 | both halves | 9e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB1]] | -0.65 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TAPBPL]] | -0.62 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.61 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[C5orf15]] | -0.61 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[LATS1]] | -0.61 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SMIM19]] | -0.60 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PATL2]] | -0.59 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[LINC00869-1]] | -0.59 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[CASC9]] | -0.59 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TAPBP]] | -0.59 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[HCP5]] | -0.58 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[RBM26-AS1]] | -0.58 | -0.50 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT5A]] | B | STAT5A activity lowers PWWP3A's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.43× higher at baseline in the lines without STAT5A | 0.075 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.8, -8.1); signed map (-27.2, -26.6). **Vector** length 112, 30.6% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.50 to 9); *Chaperone Mediated Autophagy* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +17.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.8 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.2 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.7 | +8.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.9 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.9 | +2.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.3 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.6 | -19.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -15.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | PWWP domain containing 3A, DNA repair factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,354,711-1,378,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MUM-1, EXPAND1; previously MUM1 |
| Gene groups (HGNC) | PWWP domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAK8](https://www.uniprot.org/uniprotkb/Q2TAK8) (PWWP domain-containing DNA repair factor 3A):

> Involved in the DNA damage response pathway by contributing to the maintenance of chromatin architecture. Recruited to the vicinity of DNA breaks by TP53BP1 and plays an accessory role to facilitate damage-induced chromatin changes and promoting chromatin relaxation. Required for efficient DNA repair and cell survival following DNA damage.

**Summary**, from NCBI Gene [84939](https://www.ncbi.nlm.nih.gov/gene/84939):

> Enables nucleosome binding activity. Involved in DNA repair and chromatin organization. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29641) · Entrez [84939](https://www.ncbi.nlm.nih.gov/gene/84939) · UniProt [Q2TAK8](https://www.uniprot.org/uniprotkb/Q2TAK8) · Ensembl [ENSG00000160953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160953)

## Data

Gene col 8398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8398); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8398]; `tensor/DDL_lfc|DDL_z.npy` [8398]; `embed/gene_vectors.npy` [8398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8398 or target_col == 8398). Every well: [[PWWP3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWWP3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
