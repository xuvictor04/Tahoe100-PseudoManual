---
symbol: "LPCAT1"
type: "gene"
col: 7719
ensembl_id: "ENSG00000153395"
name: "lysophosphatidylcholine acyltransferase 1"
location: "5p15.33"
module: 77
arm: "+"
pooled_cpm: 59.38
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# LPCAT1

*lysophosphatidylcholine acyltransferase 1* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.35× (z +5.8, q 4e-06, up in 28 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.32× (z +5.5, q 1e-05, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.195× (z -45.0, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6]] (+0.73, fdr 7e-06), [[IMPDH1]] (+0.73, fdr 1e-05), [[ANKRD27]] (+0.71, fdr 1e-05); moves opposite to [[BAZ2B]] (-0.77, fdr 1e-05), [[WAC-AS1]] (-0.72, fdr 3e-05), [[C11orf58]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.8 | 4e-06 | 28/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +5.5 | 1e-05 | 22/47 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.2 | 4e-05 | 22/47 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 4e-04 | 22/47 (LS 180, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.2 | 0.003 | 18/47 (SW1417, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +4.2 | 0.003 | 18/46 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.020 | 21/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.020 | 13/48 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.025 | 15/47 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.195×** | -45.0 | 0e+00 | 46/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.175×** | -32.7 | 0e+00 | 45/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.299×** | -23.4 | 0e+00 | 44/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.448×** | -15.6 | 0e+00 | 41/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.511×** | -13.1 | 5e-37 | 32/47 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -12.4 | 1e-33 | 37/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.666×** | -11.2 | 4e-27 | 37/47 (SW 900, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -10.6 | 3e-24 | 33/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -9.3 | 1e-18 | 31/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -8.6 | 5e-16 | 25/39 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -8.4 | 2e-15 | 31/47 (A-427, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -6.7 | 1e-09 | 26/47 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.690×** | -6.7 | 1e-09 | 25/42 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -6.6 | 2e-09 | 28/46 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.733×** | -6.1 | 5e-08 | 26/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.0 | 5e-08 | 27/48 (A-172, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -5.9 | 1e-07 | 26/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -5.8 | 2e-07 | 25/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.778×** | -4.9 | 4e-05 | 23/47 (SW 900, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.795×** | -4.4 | 2e-04 | 20/47 (A-427, LS 180, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.795×** | -4.4 | 2e-04 | 19/46 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 82.8 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0407× (z -55.7) |
| [[NCI-H460 (line)]] | wt | 65.0 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -37.1) |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.4) |
| [[HT-29 (line)]] | alt | 112 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -33.2) |
| [[H4 (line)]] | wt | 125 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -24.4) |
| [[LoVo (line)]] | wt | 68.5 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -29.6) |
| [[AsPC-1 (line)]] | alt | 66.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -26.8) |
| [[HOP62 (line)]] | alt | 46.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -25.2) |
| [[SW 900 (line)]] | alt | 128 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -25.4) |
| [[A-172 (line)]] | wt | 66.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -26.7) |
| [[A498 (line)]] | wt | 106 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0785× (z -38.9) |
| [[A549 (line)]] | wt | 73.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -30.6) |
| [[Hs 766T (line)]] | wt | 70.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0570× (z -35.5) |
| [[HS-578T (line)]] | alt | 62.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -26.1) |
| [[J82 (line)]] | alt | 38.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.9) |
| [[SNU-1 (line)]] | wt | 62.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -20.0) |
| [[A-427 (line)]] | wt | 52.2 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0144× (z -40.3) |
| [[HEC-1-A (line)]] | alt | 38.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 53.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -22.4) |
| [[SW480 (line)]] | alt | 45.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.5) |
| [[C32 (line)]] | wt | 45.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -23.3) |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0698× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -26.8) |
| [[SNU-423 (line)]] | alt | 57.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.3) |
| [[SW1417 (line)]] | alt | 31.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.4) |
| [[BT-474 (line)]] | alt | 144 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.9) |
| [[COLO 205 (line)]] | alt | 118 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.441× (z -10.0) |
| [[KATO III (line)]] | alt | 26.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.283× (z -8.7) |
| [[LS 180 (line)]] | wt | 36.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 38.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 56.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0986× (z -31.8) |
| [[RKO (line)]] | wt | 49.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 42.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 54.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 55.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.459× (z -9.0) |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -9.4) |
| [[HCT15 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.1) |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.7) |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | +0.73 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[IMPDH1]] | +0.73 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.71 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.70 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 | same gene group |
| [[GNB1L]] | +0.69 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DPH7]] | +0.68 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.67 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.66 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[USP35]] | +0.66 | +0.69 / +0.39 | both halves | 6e-05 |  |
| [[RBAK-RBAKDN]] | +0.66 | +0.66 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.77 | -0.73 / -0.57 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.72 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.69 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[BRAF]] | -0.68 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[TMEM35B]] | -0.67 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PATL2]] | -0.66 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[ZNF518A]] | -0.66 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[CASC9]] | -0.65 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[INO80D]] | -0.65 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[PDCL3P4]] | -0.65 | -0.73 / -0.39 | both halves | 6e-05 |  |
| [[FAM227B]] | -0.65 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[NFYC]] | -0.64 | -0.61 / -0.43 | both halves | 3e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers LPCAT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NIHCOLE]] | B | NIHCOLE activity lowers LPCAT1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.18× higher at baseline in the lines without NIHCOLE | 0.092 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.5, 0.6); signed map (-41.6, -4.3). **Vector** length 113, 30.9% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.0 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -32.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -45.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -23.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.5 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidylcholine acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,456,480-1,523,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12443, AGPAT9, AGPAT10, LPLAT8; previously AYTL2 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; EF-hand domain containing; MicroRNA protein coding host genes; Lysophospholipid acyltransferases |
| Reactome | 9 pathways, smallest: Acyl chain remodelling of PG; Acyl chain remodelling of PC; Synthesis of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NF37](https://www.uniprot.org/uniprotkb/Q8NF37) (Lysophosphatidylcholine acyltransferase 1):

> Exhibits acyltransferase activity. Exhibits acetyltransferase activity (By similarity). Activity is calcium-independent (By similarity). Catalyzes the conversion of lysophosphatidylcholine (1-acyl-sn-glycero-3-phosphocholine or LPC) into phosphatidylcholine (1,2-diacyl-sn-glycero-3-phosphocholine or PC). Catalyzes the conversion 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the …

**Summary**, from NCBI Gene [79888](https://www.ncbi.nlm.nih.gov/gene/79888):

> This gene encodes a member of the 1-acyl-sn-glycerol-3-phosphate acyltransferase family of proteins. The encoded enzyme plays a role in phospholipid metabolism, specifically in the conversion of lysophosphatidylcholine to phosphatidylcholine in the presence of acyl-CoA. This process is important in the synthesis of lung surfactant and platelet-activating factor (PAF). Elevated expression of this gene may contribute to the progression of oral squamous cell, prostate, breast, and other human …

**Accessions** — [HGNC:25718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25718) · Entrez [79888](https://www.ncbi.nlm.nih.gov/gene/79888) · UniProt [Q8NF37](https://www.uniprot.org/uniprotkb/Q8NF37) · Ensembl [ENSG00000153395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153395)

## Data

Gene col 7719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7719); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7719]; `tensor/DDL_lfc|DDL_z.npy` [7719]; `embed/gene_vectors.npy` [7719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7719 or target_col == 7719). Every well: [[LPCAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPCAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
