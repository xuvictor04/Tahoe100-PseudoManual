---
symbol: "SRGAP2C"
type: "gene"
col: 10187
ensembl_id: "ENSG00000171943"
name: "SLIT-ROBO Rho GTPase activating protein 2C"
location: "1p11.2"
module: 145
arm: "+"
pooled_cpm: 37.24
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# SRGAP2C

*SLIT-ROBO Rho GTPase activating protein 2C* — 1p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.44× (z +7.8, q 2e-12, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -17.4, q 0e+00, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP2B]] (+0.88, fdr 7e-06), [[SRGAP2]] (+0.88, fdr 7e-06), [[SRGAP2D]] (+0.66, fdr 7e-06); moves opposite to [[RRAGB]] (-0.61, fdr 4e-05), [[SLC16A9]] (-0.59, fdr 1e-05), [[CCNT2]] (-0.57, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZSCAN12]] → it (grade B ⚠); 2 go from it, the strongest it → [[MAP3K3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +7.8 | 2e-12 | 24/43 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +7.6 | 8e-12 | 25/43 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.5 | 8e-12 | 22/42 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.5 | 8e-12 | 31/43 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.1 | 1e-07 | 23/43 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.4 | 5e-06 | 20/43 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.55×** | +5.0 | 4e-05 | 17/43 (RKO, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.6 | 3e-04 | 13/43 (KATO III, Hs 766T, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.001 | 15/43 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 15/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.005 | 9/43 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.074 | 11/42 (Panc 03.27, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -17.4 | 0e+00 | 32/42 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -12.6 | 4e-34 | 30/42 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.562×** | -12.5 | 2e-33 | 31/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -10.6 | 7e-24 | 33/43 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -9.5 | 3e-19 | 28/43 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -8.3 | 9e-15 | 27/43 (SK-MEL-2, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -8.0 | 1e-13 | 32/43 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -7.3 | 2e-11 | 26/40 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.531×** | -7.1 | 5e-11 | 30/42 (HOP62, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.535×** | -7.1 | 8e-11 | 20/30 (SW 900, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -6.7 | 1e-09 | 27/43 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -6.7 | 1e-09 | 22/43 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -6.5 | 4e-09 | 24/43 (A-427, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -6.1 | 4e-08 | 26/43 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.757×** | -6.0 | 8e-08 | 25/43 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.791×** | -5.1 | 1e-05 | 21/43 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.783×** | -5.0 | 2e-05 | 17/43 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.648×** | -4.9 | 3e-05 | 17/43 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.650×** | -4.9 | 3e-05 | 17/43 (SK-MEL-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 57.6 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -14.8) |
| [[PANC-1 (line)]] | alt | 65.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.400× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.406× (z -13.4) |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.3) |
| [[A-427 (line)]] | wt | 34.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 77.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 49.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -11.3) |
| [[RKO (line)]] | wt | 38.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -13.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 51.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.9) |
| [[SW480 (line)]] | alt | 20.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[A-172 (line)]] | wt | 48.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.8) |
| [[A549 (line)]] | wt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.5) |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.158× (z -10.3) |
| [[HOP62 (line)]] | alt | 71.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.4) |
| [[HS-578T (line)]] | alt | 54.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -13.9) |
| [[J82 (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.8) |
| [[KATO III (line)]] | alt | 19.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 59.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.218× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.7) |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -9.4) |
| [[SW1417 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -10.1) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2B]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | same gene group; STRING 639 |
| [[SRGAP2]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | same gene group; STRING 428 |
| [[SRGAP2D]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PGP]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CENPJ]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[POC1A]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[KMT5A]] | +0.57 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[SNTB2]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[RPS6KA5]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GNA11]] | +0.56 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CMC2]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGB]] | -0.61 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SLC16A9]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CCNT2]] | -0.57 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CC2D2A]] | -0.57 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[LINC01748]] | -0.56 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[MTPAP]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[THUMPD2]] | -0.56 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[POLR2M]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TCTN1]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF317]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CHIC1]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[KCTD14]] | -0.55 | -0.32 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN12 activity raises SRGAP2C's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without ZSCAN12 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SRGAP2C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K3]] | B | SRGAP2C activity raises MAP3K3's level | lines that do not express SRGAP2C (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without SRGAP2C | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, PRDM2, APC; also absent: FAM72B, LINC02798, DNAJB5; its own permutation p |
| [[ARL14EP]] | B | SRGAP2C activity raises ARL14EP's level | lines that do not express SRGAP2C (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without SRGAP2C | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, PRDM2, APC; also absent: FAM72B, LINC02798, DNAJB5 |

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.8, -51.1); signed map (-51.4, -25.4). **Vector** length 92.6, 20.8% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +3.0 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.7 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.5 | -8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.8 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -0.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SLIT-ROBO Rho GTPase activating protein 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p11.2 — chr1:121,184,811-121,392,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SRGAP2P1 |
| Gene groups (HGNC) | F-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DJJ0](https://www.uniprot.org/uniprotkb/P0DJJ0) (SLIT-ROBO Rho GTPase-activating protein 2C):

> Human-specific protein that acts as a key modifier of cortical connectivity in the human brain. Acts by inhibiting the functions of ancestral paralog SRGAP2/SRGAP2A, a postsynaptic protein that regulates excitatory and inhibitory synapse maturation and density in cortical pyramidal neurons. SRGAP2C is unstable but is able to heterodimerize with SRGAP2/SRGAP2A, thereby reducing SRGAP2/SRGAP2A levels through proteasome-dependent degradation. Inhibition of SRGAP2/SRGAP2A by SRGAP2C leads to an …

**Summary**, from NCBI Gene [653464](https://www.ncbi.nlm.nih.gov/gene/653464):

> This locus encodes a member of the SLIT-ROBO Rho GTPase activating protein family. This human-specific locus resulted from segmental duplication of the SLIT-ROBO Rho GTPase activating protein 2B locus. The encoded protein lacks the GTPase activating protein domain compared to proteins encoded by SLIT-ROBO Rho GTPase activating protein 2, and acts antagonistically to these proteins in cortical neuron development. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:30584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30584) · Entrez [653464](https://www.ncbi.nlm.nih.gov/gene/653464) · UniProt [P0DJJ0](https://www.uniprot.org/uniprotkb/P0DJJ0) · Ensembl [ENSG00000171943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171943)

## Data

Gene col 10187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10187); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10187]; `tensor/DDL_lfc|DDL_z.npy` [10187]; `embed/gene_vectors.npy` [10187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10187 or target_col == 10187). Every well: [[SRGAP2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGAP2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
