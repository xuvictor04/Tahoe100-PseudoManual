---
symbol: "THNSL1"
type: "gene"
col: 11745
ensembl_id: "ENSG00000185875"
name: "threonine synthase like 1"
location: "10p12.1"
module: 16
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# THNSL1

*threonine synthase like 1* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.70× (z +5.1, q 2e-04, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.50× (z +3.7, q 0.054, up in 11 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.236× (z -14.3, q 8e-44, down in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.259× (z -13.4, q 1e-38, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCF]] (+0.64, fdr 7e-06), [[BBS10]] (+0.62, fdr 7e-06), [[CFAP97]] (+0.62, fdr 1e-05); moves opposite to [[CCDC65]] (-0.57, fdr 5e-05), [[FKBP11]] (-0.56, fdr 3e-05), [[ASB16-AS1]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.1 | 2e-04 | 4/9 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.054 | 11/37 (hTERT-HPNE, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.054 | 8/45 (RKO, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.055 | 9/46 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.055 | 14/43 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.055 | 6/45 (RKO, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.059 | 4/47 (LS 180, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | 1.25× | +3.2 | 0.10 | 7/46 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.40× | +3.2 | 0.10 | 3/14 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.55× | +3.1 | 0.10 | 4/20 (NCI-H1573, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.236×** | -14.3 | 8e-44 | 36/40 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.259×** | -13.4 | 1e-38 | 41/46 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.274×** | -12.8 | 2e-35 | 43/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.327×** | -11.1 | 2e-26 | 38/45 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.509×** | -9.5 | 4e-19 | 33/41 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.459×** | -7.7 | 1e-12 | 31/46 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -7.4 | 1e-11 | 28/45 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -6.1 | 7e-08 | 21/44 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.540×** | -6.1 | 7e-08 | 25/46 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.522×** | -6.1 | 7e-08 | 24/43 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.575×** | -5.5 | 2e-06 | 24/46 (AN3 CA, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.590×** | -5.2 | 9e-06 | 22/45 (RKO, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -4.7 | 1e-04 | 18/40 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -3.8 | 0.006 | 18/36 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -3.7 | 0.010 | 13/44 (LS 180, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.773×** | -3.6 | 0.012 | 15/45 (SNU-1, AN3 CA, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.720×** | -3.2 | 0.038 | 15/40 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 8.17 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0404× (z -13.0) |
| [[PANC-1 (line)]] | alt | 7.07 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0144× (z -26.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0669× (z -17.0) |
| [[LoVo (line)]] | wt | 6.26 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0970× (z -11.4) |
| [[RKO (line)]] | wt | 21.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 4.66 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0902× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -9.1) |
| [[C-33 A (line)]] | alt | 6.24 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0303× (z -10.9) |
| [[C32 (line)]] | wt | 4.67 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0540× (z -9.7) |
| [[Hs 766T (line)]] | wt | 4.60 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0354× (z -10.9) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 5.50 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0612× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 6.01 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.115× (z -10.9) |
| [[A498 (line)]] | wt | 3.05 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0870× (z -8.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 2.97 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0452× (z -8.7) |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0531× (z -10.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 6.14 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0600× (z -10.5) |
| [[SW1417 (line)]] | alt | 5.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCF]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[BBS10]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CFAP97]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TRMT5]] | +0.59 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[TIGD2]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PTCD2]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ZNF770]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[N6AMT1]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[KICS2]] | +0.56 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ZNF816]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC65]] | -0.57 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[FKBP11]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ASB16-AS1]] | -0.54 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[CSNK1G2]] | -0.53 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[PITPNA]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MRPL33]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TMEM259]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[AP2A1]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PDE6D]] | -0.50 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[MAP3K3]] | -0.50 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[NFATC2IP-AS1]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PHF1]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.0, 14.3); signed map (-0.5, -37.0). **Vector** length 57.1, 8.30% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.7 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | -1.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -14.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -11.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | threonine synthase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:25,016,612-25,026,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22002, TSH1 |
| Matched by | ensembl_id |

UniProt [Q8IYQ7](https://www.uniprot.org/uniprotkb/Q8IYQ7) carries no function annotation.

**Summary**, from NCBI Gene [79896](https://www.ncbi.nlm.nih.gov/gene/79896):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26160) · Entrez [79896](https://www.ncbi.nlm.nih.gov/gene/79896) · UniProt [Q8IYQ7](https://www.uniprot.org/uniprotkb/Q8IYQ7) · Ensembl [ENSG00000185875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185875)

## Data

Gene col 11745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11745); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11745]; `tensor/DDL_lfc|DDL_z.npy` [11745]; `embed/gene_vectors.npy` [11745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11745 or target_col == 11745). Every well: [[THNSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THNSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
