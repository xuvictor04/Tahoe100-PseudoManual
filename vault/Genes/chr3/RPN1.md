---
symbol: "RPN1"
type: "gene"
col: 8804
ensembl_id: "ENSG00000163902"
name: "ribophorin I"
location: "3q21.3"
module: 20
arm: "+"
pooled_cpm: 92.36
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPN1

*ribophorin I* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.55× (z +18.6, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.61× (z +7.3, q 5e-11, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.622× (z -10.3, q 3e-22, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.89, fdr 7e-06), [[STT3A]] (+0.80, fdr 7e-06), [[CMPK1]] (+0.77, fdr 7e-06); moves opposite to [[PPP1R35]] (-0.71, fdr 1e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[CROCCP2-1]] (-0.70, fdr 7e-06), [[MRPL46]] (-0.69, fdr 1e-05), [[EID2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +18.6 | 0e+00 | 44/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +17.9 | 0e+00 | 48/49 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +11.8 | 7e-30 | 40/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +7.3 | 5e-11 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +6.2 | 6e-08 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.2 | 6e-08 | 41/48 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +4.9 | 7e-05 | 39/49 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +4.3 | 0.002 | 35/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.0 | 0.003 | 23/38 (C32, HS-578T, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.0 | 0.003 | 31/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.004 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.006 | 26/47 (C-33 A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.029 | 17/49 (SW480, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.053 | 24/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.064 | 22/48 (LoVo, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.622×** | -10.3 | 3e-22 | 40/48 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.628×** | -7.1 | 3e-10 | 38/48 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.682×** | -5.6 | 4e-06 | 34/48 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.776×** | -5.5 | 4e-06 | 39/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -5.4 | 7e-06 | 32/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -5.3 | 1e-05 | 34/48 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -4.9 | 6e-05 | 35/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.756×** | -4.3 | 0.001 | 28/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.029 | 22/48 (SW 1088, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.041 | 23/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.074 | 24/48 (RPMI-7951, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.751×** | -3.1 | 0.077 | 23/48 (NCI-H1792, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.678×** | -3.1 | 0.080 | 24/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 103 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -13.3) |
| [[A498 (line)]] | wt | 109 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +15.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.4) |
| [[HOP62 (line)]] | alt | 115 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +16.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 96.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.8) |
| [[J82 (line)]] | alt | 105 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 123 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -15.8) |
| [[A-427 (line)]] | wt | 99.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -12.3) |
| [[A549 (line)]] | wt | 50.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +12.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +15.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.66× (z +19.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 63.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +14.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 94.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.02× (z +21.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 56.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 64.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 62.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +14.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 82.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +16.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 67.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.23× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 60.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 67.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +15.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 70.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +14.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +10.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 70.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.38× (z +15.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +14.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 166 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 99.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.4) |
| [[KATO III (line)]] | alt | 173 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 50.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.4) |
| [[SW 900 (line)]] | alt | 97.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +15.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 77.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.0) |
| [[RKO (line)]] | wt | 82.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0804× (z -9.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW1417 (line)]] | alt | 94.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[STT3A]] | +0.80 | +0.76 / +0.86 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[CMPK1]] | +0.77 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.76 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[DDOST]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[TMED2]] | +0.76 | +0.81 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 698 |
| [[DNAJB11]] | +0.76 | +0.78 / +0.78 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 561 |
| [[UGGT1]] | +0.75 | +0.64 / +0.81 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 657 |
| [[FKBP9]] | +0.75 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[TMED7]] | +0.75 | +0.77 / +0.84 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDIA3]] | +0.74 | +0.81 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 521 |
| [[DHFR]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R35]] ⚠ | -0.71 | -0.53 / -0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.70 | -0.64 / -0.72 | both halves | 7e-06 |  |
| [[MRPL46]] | -0.69 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.65 | -0.39 / -0.71 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EID2]] | -0.65 | -0.59 / -0.77 | both halves | 7e-06 |  |
| [[ZNF503]] | -0.64 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[METTL23]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.64 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.63 | -0.44 / -0.73 | both halves | 3e-05 |  |
| [[NT5C]] | -0.62 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[CEBPZ]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[COIL]] | -0.61 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[PDRG1]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.809). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.2, -22.4); signed map (-24.1, -39.4). **Vector** length 132, 44.2% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.52 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.52 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.0 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.6 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.9 | +1.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.8 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.6 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ribophorin I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,619,969-128,681,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OST1 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Hallmark sets | UV_RESPONSE_UP, MTORC1_SIGNALING |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [P04843](https://www.uniprot.org/uniprotkb/P04843) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit 1):

> Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates protein …

**Summary**, from NCBI Gene [6184](https://www.ncbi.nlm.nih.gov/gene/6184):

> This gene encodes a type I integral membrane protein found only in the rough endoplasmic reticulum. The encoded protein is part of an N-oligosaccharyl transferase complex that links high mannose oligosaccharides to asparagine residues found in the Asn-X-Ser/Thr consensus motif of nascent polypeptide chains. This protein forms part of the regulatory subunit of the 26S proteasome and may mediate binding of ubiquitin-like domains to this proteasome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10381) · Entrez [6184](https://www.ncbi.nlm.nih.gov/gene/6184) · UniProt [P04843](https://www.uniprot.org/uniprotkb/P04843) · Ensembl [ENSG00000163902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163902)

## Data

Gene col 8804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8804); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8804]; `tensor/DDL_lfc|DDL_z.npy` [8804]; `embed/gene_vectors.npy` [8804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8804 or target_col == 8804). Every well: [[RPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
