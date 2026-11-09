---
symbol: "XYLB"
type: "gene"
col: 1723
ensembl_id: "ENSG00000093217"
name: "xylulokinase"
location: "3p22.2"
module: 18
arm: "+"
pooled_cpm: 31.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# XYLB

*xylulokinase* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.42× (z +5.8, q 4e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.573× (z -12.6, q 1e-33, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.709× (z -7.7, q 3e-12, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAD]] (+0.69, fdr 7e-06), [[FXN]] (+0.69, fdr 7e-06), [[DKC1]] (+0.69, fdr 7e-06); moves opposite to [[BOLA1]] (-0.61, fdr 2e-05), [[SMIM14]] (-0.56, fdr 2e-05), [[ATOSA]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.8 | 4e-06 | 25/48 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.6 | 0.001 | 20/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.002 | 21/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.4 | 0.002 | 18/48 (NCI-H2347, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.002 | 20/48 (KATO III, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.004 | 17/35 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.28×** | +4.1 | 0.004 | 20/47 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.004 | 16/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.010 | 14/48 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.27×** | +3.8 | 0.010 | 16/46 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.6 | 0.019 | 20/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.019 | 17/48 (KATO III, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.573×** | -12.6 | 1e-33 | 32/48 (SNU-423, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.555×** | -9.3 | 3e-18 | 31/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -7.7 | 3e-12 | 30/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -7.5 | 1e-11 | 34/48 (RPMI-7951, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.640×** | -7.4 | 2e-11 | 32/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.687×** | -6.2 | 6e-08 | 27/46 (NCI-H1792, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -5.1 | 2e-05 | 25/48 (HEC-1-A, C32, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -4.9 | 8e-05 | 26/48 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.788×** | -3.9 | 0.006 | 22/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.638×** | -3.8 | 0.008 | 16/46 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.018 | 17/47 (HEC-1-A, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.018 | 20/48 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.821×** | -3.2 | 0.050 | 12/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 0.05 µM |  | **0.812×** | -3.2 | 0.051 | 13/48 (COLO 205, C-33 A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.822×** | -3.0 | 0.088 | 19/48 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 59.3 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -19.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.9) |
| [[A-172 (line)]] | wt | 35.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0640× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.301× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 6 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.150× (z -18.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 22.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -18.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 27.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[MIA PaCa-2 (line)]] | alt | 41.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -13.2) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SNU-1 (line)]] | wt | 69.1 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.226× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.294× (z -8.5) |
| [[C32 (line)]] | wt | 38.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.249× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.261× (z -8.8) |
| [[J82 (line)]] | alt | 30.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 53.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -19.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -11.0) |
| [[SW1417 (line)]] | alt | 51.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -11.0) |
| [[A-427 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -9.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 8.70 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[RKO (line)]] | wt | 65.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -11.4) |
| [[SW48 (line)]] | wt | 75.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAD]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[FXN]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[DKC1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.67 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MDN1]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SFXN4]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NLE1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TUBGCP4]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ANKRD36]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PUS7]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOLA1]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SMIM14]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ATOSA]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ARID4B]] | -0.55 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[TSPAN31]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[WBP1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MXD1]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ATP5IF1]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SYNRG]] | -0.54 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[CDKL5]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SLU7]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[KDM5A]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises XYLB's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.22× lower at baseline in the lines without NT5M | 0.011 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MCOLN2]] | B | MCOLN2 activity raises XYLB's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.37× lower at baseline in the lines without MCOLN2 | 0.034 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[ADCY3]] | B | ADCY3 activity raises XYLB's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.15× lower at baseline in the lines without ADCY3 | 0.091 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[TSEN2]] | C | TSEN2 activity raises XYLB's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.97× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.6, -38.3); signed map (-6.1, -53.5). **Vector** length 98.1, 23.4% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.0 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.5 | -12.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.3 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | xylulokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,346,760-38,421,348 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10343, FLJ12539 |
| Gene groups (HGNC) | Carbohydrate kinases; FGGY kinase family |
| Reactome | 2 pathways, smallest: Formation of xylulose-5-phosphate; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O75191](https://www.uniprot.org/uniprotkb/O75191) (Xylulose kinase):

> Phosphorylates D-xylulose to produce D-xylulose 5-phosphate, a molecule that may play an important role in the regulation of glucose metabolism and lipogenesis.

**Summary**, from NCBI Gene [9942](https://www.ncbi.nlm.nih.gov/gene/9942):

> The protein encoded by this gene shares 22% sequence identity with Hemophilus influenzae xylulokinase, and even higher identity to other gene products in C.elegans (45%) and yeast (31-35%), which are thought to belong to a family of enzymes that include fucokinase, gluconokinase, glycerokinase and xylulokinase. These proteins play important roles in energy metabolism. [provided by RefSeq, Aug 2009]

**Accessions** — [HGNC:12839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12839) · Entrez [9942](https://www.ncbi.nlm.nih.gov/gene/9942) · UniProt [O75191](https://www.uniprot.org/uniprotkb/O75191) · Ensembl [ENSG00000093217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093217)

## Data

Gene col 1723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1723); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1723]; `tensor/DDL_lfc|DDL_z.npy` [1723]; `embed/gene_vectors.npy` [1723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1723 or target_col == 1723). Every well: [[XYLB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XYLB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
