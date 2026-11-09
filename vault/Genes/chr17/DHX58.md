---
symbol: "DHX58"
type: "gene"
col: 2990
ensembl_id: "ENSG00000108771"
name: "DExH-box helicase 58"
location: "17q21.2"
module: 32
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 46
n_dd_up_clean: 23
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 23
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# DHX58

*DExH-box helicase 58* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.95× (z +8.3, q 6e-14, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.247× (z -17.2, q 0e+00, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIH1]] (+0.88, fdr 7e-06), [[PARP10]] (+0.88, fdr 7e-06), [[IFIT3]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +8.3 | 6e-14 | 28/42 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.1 | 4e-10 | 19/38 (NCI-H460, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +6.8 | 2e-09 | 22/42 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +5.2 | 2e-05 | 20/39 (NCI-H460, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +5.1 | 5e-05 | 18/39 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 3e-04 | 18/42 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +4.5 | 6e-04 | 11/34 (LoVo, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.002 | 11/40 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 15/41 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.005 | 8/43 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.005 | 11/41 (NCI-H460, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.005 | 12/39 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.005 | 8/39 (NCI-H1792, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +3.6 | 0.010 | 11/43 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.010 | 10/43 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.011 | 9/40 (A498, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.247×** | -17.2 | 0e+00 | 34/41 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.297×** | -14.9 | 0e+00 | 34/41 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.303×** | -14.6 | 0e+00 | 33/43 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.339×** | -13.3 | 5e-38 | 36/40 (LoVo, A498, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.380×** | -11.9 | 2e-30 | 35/41 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -10.9 | 8e-26 | 31/43 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.547×** | -10.4 | 1e-23 | 28/41 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.428×** | -10.4 | 2e-23 | 29/42 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.449×** | -9.8 | 7e-21 | 33/43 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.476×** | -9.1 | 6e-18 | 22/30 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.501×** | -8.4 | 2e-15 | 25/40 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.502×** | -8.4 | 2e-15 | 25/37 (SNU-423, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -8.3 | 3e-15 | 25/36 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.514×** | -8.1 | 2e-14 | 31/41 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.657×** | -7.3 | 2e-11 | 24/42 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.692×** | -6.3 | 8e-09 | 25/41 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.379×** | -6.2 | 2e-08 | 26/40 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 16 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0464× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0801× (z -15.4) |
| [[LoVo (line)]] | wt | 21.9 | 0 | 13 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0667× (z -20.7) |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0694× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 11.1 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.123× (z -13.5) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.145× (z -13.4) |
| [[A498 (line)]] | wt | 21.0 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.210× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.223× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 9.73 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0765× (z -12.4) |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0418× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.158× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0521× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.155× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 9.94 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0246× (z -17.3) |
| [[LS 180 (line)]] | wt | 10.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -10.3) |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0465× (z -12.8) |
| [[C32 (line)]] | wt | 13.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.68× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 6.93 | 0 | 2 | — | [[Acetazolamide (drug)]] 0.05 µM 0.100× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.137× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 14.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +18.5) | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -9.4) |
| [[A-427 (line)]] | wt | 6.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 7.03 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0693× (z -10.4) |
| [[H4 (line)]] | wt | 9.69 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0468× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0343× (z -11.8) |
| [[Hs 766T (line)]] | wt | 9.21 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0823× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +8.8) | — |
| [[J82 (line)]] | alt | 8.32 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.03× (z +8.5) | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.164× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 4.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0521× (z -9.6) |
| [[PANC-1 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIH1]] | +0.88 | +0.78 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999 |
| [[PARP10]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | STRING 520 |
| [[IFIT3]] | +0.87 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 751 |
| [[XAF1]] | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 763 |
| [[DDX60]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 902 |
| [[OASL]] | +0.85 | +0.81 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 822 |
| [[PARP14]] | +0.84 | +0.76 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 553 |
| [[OAS2]] | +0.83 | +0.74 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 863 |
| [[IFI44]] | +0.83 | +0.73 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 807 |
| [[IFIT1]] | +0.82 | +0.72 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 810 |
| [[EPSTI1]] | +0.82 | +0.74 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 603 |
| [[IFIT2]] | +0.82 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 783 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises DHX58's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.98× lower at baseline in the lines without PLAAT4 | 0.002 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[GBP4]] | B | GBP4 activity raises DHX58's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without GBP4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OASL]] | B | OASL activity raises DHX58's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without OASL | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises DHX58's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without EPSTI1 | 0.018 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[GBP4]] | B | GBP4 activity strengthens DHX58's drug response | lines that do not express GBP4 (16) vs lines expressing it (27) | the lines without GBP4 respond 0.42× as strongly (z diff +2.74); strongest at Belinostat 5 µM: 0.50x vs 0.19x (z diff +4.9) | 0.029 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; target measured in part of the lines; artifact flags |
| [[IFITM1]] | B | IFITM1 activity raises DHX58's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without IFITM1 | 0.030 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[GBP1]] | B | GBP1 activity raises DHX58's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without GBP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[RSAD2]] | B | RSAD2 activity raises DHX58's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without RSAD2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFIT2]] | B | IFIT2 activity raises DHX58's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without IFIT2 | 0.050 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[HERC6]] | B | HERC6 activity raises DHX58's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without HERC6 | 0.051 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises DHX58's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without SAMD9L | 0.059 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFIT3]] | B | IFIT3 activity raises DHX58's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 2.13× lower at baseline in the lines without IFIT3 | 0.066 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.868). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 52.7); signed map (63.7, 30.7). **Vector** length 115, 30.7% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.80 to 23); *Interferon Signaling* (reactome, mean cos +0.74 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.77 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +3.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.5 | -10.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.5 | -10.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.0 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -13.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.8 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | DExH-box helicase 58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,101,404-42,112,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGP2, D11LGP2 |
| Gene groups (HGNC) | DEAH-box helicases; RIG-I RNA sensor family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 2 pathways, smallest: DDX58/IFIH1-mediated induction of interferon-alpha/beta; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C10](https://www.uniprot.org/uniprotkb/Q96C10) (ATP-dependent RNA helicase DHX58):

> Acts as a regulator of RIGI and IFIH1/MDA5 mediated antiviral signaling. Cannot initiate antiviral signaling as it lacks the CARD domain required for activating MAVS/IPS1-dependent signaling events. Can have both negative and positive regulatory functions related to RIGI and IFIH1/MDA5 signaling and this role in regulating signaling may be complex and could probably depend on characteristics of the infecting virus or target cells, or both. Its inhibitory action on RIG-I signaling may involve …

**Summary**, from NCBI Gene [79132](https://www.ncbi.nlm.nih.gov/gene/79132):

> Enables several functions, including ATP hydrolysis activity; RNA binding activity; and zinc ion binding activity. Involved in negative regulation of type I interferon production and regulation of innate immune response. Located in Golgi apparatus and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29517) · Entrez [79132](https://www.ncbi.nlm.nih.gov/gene/79132) · UniProt [Q96C10](https://www.uniprot.org/uniprotkb/Q96C10) · Ensembl [ENSG00000108771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108771)

## Data

Gene col 2990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2990); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2990]; `tensor/DDL_lfc|DDL_z.npy` [2990]; `embed/gene_vectors.npy` [2990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2990 or target_col == 2990). Every well: [[DHX58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
