---
symbol: "MAP2K7"
type: "gene"
col: 1169
ensembl_id: "ENSG00000076984"
name: "mitogen-activated protein kinase kinase 7"
location: "19p13.2"
module: 24
arm: "+"
pooled_cpm: 35.36
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MAP2K7

*mitogen-activated protein kinase kinase 7* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.22× (z +9.6, q 6e-19, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.81× (z +7.1, q 3e-10, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.300× (z -20.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIAS4]] (+0.81, fdr 7e-06), [[SMIM26]] (+0.68, fdr 3e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SETDB1]] (+0.67, fdr 1e-05), [[CROCCP2-1]] (+0.66, fdr 4e-05); moves opposite to [[FH]] (-0.68, fdr 7e-06), [[DR1]] (-0.67, fdr 1e-05), [[EDEM1]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.6 | 6e-19 | 45/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.81×** | +7.1 | 3e-10 | 42/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +5.9 | 8e-07 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 2e-04 | 33/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.5 | 0.053 | 0/49 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.2 | 0.12 | 22/47 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.300×** | -20.5 | 0e+00 | 47/48 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.380×** | -11.2 | 1e-26 | 44/47 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.405×** | -10.9 | 3e-25 | 45/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.433×** | -10.1 | 1e-21 | 46/48 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -8.9 | 5e-17 | 45/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -8.6 | 7e-16 | 39/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.609×** | -8.4 | 3e-15 | 41/48 (SW1417, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.562×** | -6.9 | 3e-10 | 45/48 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.501×** | -4.3 | 9e-04 | 36/48 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.709×** | -4.1 | 0.002 | 31/48 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.020 | 20/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.735×** | -3.4 | 0.028 | 23/45 (SNU-1, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.819×** | -3.4 | 0.030 | 24/48 (SNU-423, A-427, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.756×** | -3.4 | 0.031 | 29/47 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -3.2 | 0.051 | 22/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **0.832×** | -3.1 | 0.061 | 18/48 (SW1417, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.1 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -11.3) |
| [[PANC-1 (line)]] | alt | 30.1 | 3 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.38× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.99× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 30.2 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.88× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -17.6) |
| [[SW480 (line)]] | alt | 44.9 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.89× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -15.3) |
| [[C32 (line)]] | wt | 24.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -14.3) |
| [[H4 (line)]] | wt | 53.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.2) |
| [[HS-578T (line)]] | alt | 47.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -18.8) |
| [[LS 180 (line)]] | wt | 37.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 40.4 | 1 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.20× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.247× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 43.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -13.9) |
| [[SNU-1 (line)]] | wt | 46.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.4) |
| [[SNU-423 (line)]] | alt | 46.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -16.3) |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -13.5) |
| [[A-172 (line)]] | wt | 39.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 37.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -14.6) |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.6) |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.8) |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -16.1) |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 28.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 26.6 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.14× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 35.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.378× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 38.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -17.2) |
| [[RKO (line)]] | wt | 46.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.1) |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.5) |
| [[A-427 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.20× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -12.9) |
| [[COLO 205 (line)]] | alt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -14.0) |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 34.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -13.0) |
| [[J82 (line)]] | alt | 28.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.6) |
| [[KATO III (line)]] | alt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.1) |
| [[LoVo (line)]] | wt | 34.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -14.1) |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS4]] | +0.81 | +0.68 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SMIM26]] ⚠ | +0.68 | +0.46 / +0.77 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SETDB1]] | +0.67 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.66 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[RPL36AL]] ⚠ | +0.66 | +0.56 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | +0.66 | +0.44 / +0.65 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAT2]] | +0.66 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[ATP5MC2]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.65 | +0.47 / +0.64 | both halves | 2e-05 | pathway: MyD88 cascade initiated on plasma membrane |
| [[TIMM29]] | +0.64 | +0.39 / +0.73 | both halves | 5e-05 |  |
| [[LSM7]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[YBEY]] | +0.63 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[INAFM1]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[RPP21]] | +0.62 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[POLR2J4]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FH]] | -0.68 | -0.74 / -0.60 | both halves | 7e-06 |  |
| [[DR1]] | -0.67 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[EDEM1]] | -0.64 | -0.33 / -0.68 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.61 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.61 | -0.39 / -0.71 | both halves | 5e-05 |  |
| [[PGRMC1]] | -0.61 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[TWF1]] | -0.61 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.60 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[ADAM9]] | -0.59 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[PNPO]] | -0.59 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[ACTR3]] | -0.58 | -0.37 / -0.59 | both halves | 9e-05 |  |
| [[UCHL5]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAP2K7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.3, -23.0); signed map (-17.3, -0.4). **Vector** length 92.3, 25.8% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.7 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.8 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | -8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +0.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -20.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | -4.4 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | +0.0 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,903,843-7,914,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MKK7, Jnkk2, SAPKK4; previously PRKMK7 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases |
| Reactome | 31 pathways, smallest: Uptake and function of anthrax toxins; JNK (c-Jun kinases) phosphorylation and  activation mediated by activated human TAK1; Uptake and actions of bacterial toxins |
| Matched by | ensembl_id |

**Function**, from UniProt [O14733](https://www.uniprot.org/uniprotkb/O14733) (Dual specificity mitogen-activated protein kinase kinase 7):

> Dual specificity protein kinase which acts as an essential component of the MAP kinase signal transduction pathway. Essential component of the stress-activated protein kinase/c-Jun N-terminal kinase (SAP/JNK) signaling pathway. With MAP2K4/MKK4, is the one of the only known kinase to directly activate the stress-activated protein kinase/c-Jun N-terminal kinases MAPK8/JNK1, MAPK9/JNK2 and MAPK10/JNK3. MAP2K4/MKK4 and MAP2K7/MKK7 both activate the JNKs by phosphorylation, but they differ in their …

**Summary**, from NCBI Gene [5609](https://www.ncbi.nlm.nih.gov/gene/5609):

> The protein encoded by this gene is a dual specificity protein kinase that belongs to the MAP kinase kinase family. This kinase specifically activates MAPK8/JNK1 and MAPK9/JNK2, and this kinase itself is phosphorylated and activated by MAP kinase kinase kinases including MAP3K1/MEKK1, MAP3K2/MEKK2,MAP3K3/MEKK5, and MAP4K2/GCK. This kinase is involved in the signal transduction mediating the cell responses to proinflammatory cytokines, and environmental stresses. Alternative splicing results in …

**Accessions** — [HGNC:6847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6847) · Entrez [5609](https://www.ncbi.nlm.nih.gov/gene/5609) · UniProt [O14733](https://www.uniprot.org/uniprotkb/O14733) · Ensembl [ENSG00000076984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076984)

## Data

Gene col 1169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1169); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1169]; `tensor/DDL_lfc|DDL_z.npy` [1169]; `embed/gene_vectors.npy` [1169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1169 or target_col == 1169). Every well: [[MAP2K7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
