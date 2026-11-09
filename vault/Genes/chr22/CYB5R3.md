---
symbol: "CYB5R3"
type: "gene"
col: 1903
ensembl_id: "ENSG00000100243"
name: "cytochrome b5 reductase 3"
location: "22q13.2"
module: 2
arm: "+"
pooled_cpm: 94.25
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CYB5R3

*cytochrome b5 reductase 3* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.61× (z +13.2, q 1e-36, up in 40 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.49× (z +5.6, q 3e-06, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -12.5, q 2e-33, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTN4]] (+0.63, fdr 1e-05), [[CDC42BPB]] (+0.62, fdr 1e-05), [[TIMP2]] (+0.61, fdr 1e-05); moves opposite to [[TYW3]] (-0.60, fdr 3e-05), [[PBDC1]] (-0.59, fdr 6e-05), [[ARL14EP]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +13.2 | 1e-36 | 40/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +13.0 | 2e-36 | 46/49 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +8.8 | 2e-16 | 38/45 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 3e-06 | 33/48 (COLO 205, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +4.5 | 7e-04 | 30/48 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.001 | 27/48 (LS 180, A498, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +3.6 | 0.027 | 27/48 (COLO 205, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -12.5 | 2e-33 | 39/47 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -8.9 | 1e-16 | 40/47 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.754×** | -5.7 | 2e-06 | 29/48 (SK-MEL-2, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -5.3 | 1e-05 | 36/48 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -4.1 | 0.004 | 27/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.748×** | -4.0 | 0.007 | 29/49 (HepG2/C3A, SW 1088, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.763×** | -3.8 | 0.010 | 32/48 (NCI-H23, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.717×** | -3.7 | 0.013 | 25/48 (A498, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.4 | 0.042 | 23/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.792×** | -3.3 | 0.050 | 23/48 (HEC-1-A, RPMI-7951, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.764×** | -3.3 | 0.050 | 20/48 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.795×** | -3.1 | 0.078 | 21/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.660×** | -3.1 | 0.085 | 21/44 (H4, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.806×** | -3.1 | 0.089 | 21/48 (A498, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 148 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 232 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -23.6) |
| [[A-427 (line)]] | wt | 48.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0656× (z -22.3) |
| [[HEC-1-A (line)]] | alt | 74.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 108 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 44.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.20× (z +10.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 58.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +11.0) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.458× (z -10.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 72.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 60.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 46.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) |
| [[PANC-1 (line)]] | alt | 51.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.0) |
| [[C-33 A (line)]] | alt | 48.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.34× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +12.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 198 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.0) |
| [[HS-578T (line)]] | alt | 246 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 78.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 91.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +13.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.9) |
| [[SNU-423 (line)]] | alt | 89.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -11.4) |
| [[SW 900 (line)]] | alt | 103 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -15.3) |
| [[A-172 (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.5) |
| [[A498 (line)]] | wt | 235 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.487× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 69.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.4) |
| [[COLO 205 (line)]] | alt | 44.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.40× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 86.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.1) |
| [[LS 180 (line)]] | wt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 83.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 54.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 84.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.6) |
| [[RKO (line)]] | wt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +11.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTN4]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CDC42BPB]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TIMP2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[FGFRL1]] | +0.60 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[GNAI2]] | +0.60 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[KANK2]] | +0.59 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[B4GALT1]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ERGIC1]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[NCOR2]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[BCAM]] | +0.58 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[RHOA]] | +0.58 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[AP2A1]] | +0.58 | +0.59 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | -0.60 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PBDC1]] | -0.59 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ARL14EP]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CGAS]] | -0.57 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[MTX3]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[NNT-AS1]] | -0.56 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DUS4L]] | -0.54 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CCDC122]] | -0.54 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[PAAF1]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[METTL18]] | -0.53 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[RPP38]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[AFG1L]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CYB5R3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CYB5R3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HHEX]] | B | HHEX activity strengthens CYB5R3's drug response | lines that do not express HHEX (18) vs lines expressing it (31) | the lines without HHEX respond 0.94× as strongly (z diff +0.19); strongest at Homoharringtonine 5 µM: 0.66x vs 0.46x (z diff +3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL; target measured in part of the lines; both ways; artifact flags |
| [[SERINC2]] | B | SERINC2 activity raises CYB5R3's level | lines that do not express SERINC2 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without SERINC2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC9A3, TESK2, LITAF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.2, 0.7); signed map (-12.6, 36.2). **Vector** length 105, 30.5% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +13.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +13.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.0 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 reductase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,615,730-42,720,870 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B5R; previously DIA1 |
| Gene groups (HGNC) | Cytochrome b5 reductases; Flavoproteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: Vitamin C (ascorbate) metabolism; Phase I - Functionalization of compounds; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P00387](https://www.uniprot.org/uniprotkb/P00387) (NADH-cytochrome b5 reductase 3):

> Catalyzes the reduction of two molecules of cytochrome b5 using NADH as the electron donor.

**Summary**, from NCBI Gene [1727](https://www.ncbi.nlm.nih.gov/gene/1727):

> This gene encodes cytochrome b5 reductase, which includes a membrane-bound form in somatic cells (anchored in the endoplasmic reticulum, mitochondrial and other membranes) and a soluble form in erythrocytes. The membrane-bound form exists mainly on the cytoplasmic side of the endoplasmic reticulum and functions in desaturation and elongation of fatty acids, in cholesterol biosynthesis, and in drug metabolism. The erythrocyte form is located in a soluble fraction of circulating erythrocytes and …

**Accessions** — [HGNC:2873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2873) · Entrez [1727](https://www.ncbi.nlm.nih.gov/gene/1727) · UniProt [P00387](https://www.uniprot.org/uniprotkb/P00387) · Ensembl [ENSG00000100243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100243)

## Data

Gene col 1903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1903); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1903]; `tensor/DDL_lfc|DDL_z.npy` [1903]; `embed/gene_vectors.npy` [1903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1903 or target_col == 1903). Every well: [[CYB5R3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5R3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
