---
symbol: "EPOR"
type: "gene"
col: 11908
ensembl_id: "ENSG00000187266"
name: "erythropoietin receptor"
location: "19p13.2"
module: 136
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 14
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# EPOR

*erythropoietin receptor* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +8.9, q 2e-16, up in 17 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.375× (z -12.1, q 4e-31, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA80]] (+0.64, fdr 1e-05), [[TRPT1]] (+0.62, fdr 1e-05), [[EFEMP2]] (+0.62, fdr 7e-06); moves opposite to [[HNF4G]] (-0.60, fdr 3e-05), [[TMEM33]] (-0.59, fdr 1e-05), [[PHACTR2]] (-0.57, fdr 2e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +8.9 | 2e-16 | 17/40 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.1 | 3e-10 | 2/10 (BT-474, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.46×** | +4.9 | 2e-04 | 12/46 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 2e-04 | 16/47 (SW1417, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 0.001 | 5/38 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.002 | 6/45 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.002 | 14/46 (Hs 766T, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.003 | 15/47 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.008 | 11/47 (SW1417, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.008 | 5/39 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.035 | 8/36 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.29×** | +3.3 | 0.038 | 1/47 (PANC-1) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.058 | 5/28 (A-172, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.059 | 3/40 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.1 | 0.073 | 4/13 (PANC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.080 | 3/45 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.100 | 6/38 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.375×** | -12.1 | 4e-31 | 26/38 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -9.9 | 1e-20 | 27/45 (hTERT-HPNE, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -8.6 | 1e-15 | 25/37 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.525×** | -8.3 | 1e-14 | 24/44 (NCI-H460, SK-MEL-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -7.4 | 2e-11 | 21/47 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -7.1 | 1e-10 | 21/45 (NCI-H460, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.581×** | -7.0 | 2e-10 | 23/43 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -6.5 | 7e-09 | 20/46 (NCI-H460, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -5.5 | 2e-06 | 16/43 (J82, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.742×** | -5.4 | 3e-06 | 16/38 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -5.2 | 1e-05 | 12/37 (CFPAC-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -4.7 | 1e-04 | 16/32 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.702×** | -4.6 | 2e-04 | 17/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -4.5 | 3e-04 | 20/42 (PANC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.697×** | -4.4 | 4e-04 | 19/45 (RPMI-7951, HOP62, …) | two highest doses | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.718×** | -4.3 | 7e-04 | 14/47 (NCI-H460, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.721×** | -4.0 | 0.002 | 11/43 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -3.8 | 0.004 | 9/45 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.722×** | -3.0 | 0.073 | 5/48 (AN3 CA, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.073 | 7/46 (NCI-H661, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.98 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.238× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -14.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0440× (z -14.0) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 7.01 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0900× (z -9.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -9.1) |
| [[A-172 (line)]] | wt | 6.71 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0931× (z -9.9) |
| [[A498 (line)]] | wt | 6.26 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0713× (z -12.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 7.60 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0411× (z -10.7) |
| [[J82 (line)]] | alt | 5.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 2.97 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.0673× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 3.27 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0646× (z -8.5) |
| [[A549 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA80]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TRPT1]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[EFEMP2]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TNNT1]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[NAGK]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MEIS3]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[MTMR14]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PC]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[ARID3B]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[OVOL1]] | +0.57 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[FBXL12]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.60 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[TMEM33]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PHACTR2]] | -0.57 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[SYK]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 | STRING 526 |
| [[PPA2]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SLC44A3]] | -0.56 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CHCHD3]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MTA3]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[LARP4]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GFM1]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PLCH1]] | -0.54 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[FUBP1]] | -0.54 | -0.36 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity lowers EPOR's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.66× higher at baseline in the lines without NDRG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[HNF4G]] | B | HNF4G activity weakens EPOR's drug response | lines that do not express HNF4G (16) vs lines expressing it (32) | the lines without HNF4G respond 1.41× as strongly (z diff -1.01); strongest at Homoharringtonine 0.5 µM: 0.21x vs 0.44x (z diff -3.2) | 0.034 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5; target measured in part of the lines; artifact flags |
| [[SMOX]] | B | SMOX activity lowers EPOR's level | lines that do not express SMOX (6) vs lines expressing it (44) | 1.60× higher at baseline in the lines without SMOX | 0.059 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.9, -1.8); signed map (-24.1, 25.1). **Vector** length 58.9, 8.15% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +8.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.2 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | erythropoietin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,377,207-11,384,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPO-R |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Erythropoietin activates Phospholipase C gamma (PLCG); Erythropoietin activates STAT5; Erythropoietin activates Phosphoinositide-3-kinase (PI3K) |
| Matched by | ensembl_id |

**Function**, from UniProt [P19235](https://www.uniprot.org/uniprotkb/P19235) (Erythropoietin receptor):

> Receptor for erythropoietin, which mediates erythropoietin-induced erythroblast proliferation and differentiation. Upon EPO stimulation, EPOR dimerizes triggering the JAK2/STAT5 signaling cascade (By similarity). In some cell types, can also activate STAT1 and STAT3. May also activate the LYN tyrosine kinase (By similarity).; [Isoform EPOR-T]: Acts as a dominant-negative receptor of EPOR-mediated signaling.

**Summary**, from NCBI Gene [2057](https://www.ncbi.nlm.nih.gov/gene/2057):

> This gene encodes the erythropoietin receptor which is a member of the cytokine receptor family. Upon erythropoietin binding, this receptor activates Jak2 tyrosine kinase which activates different intracellular pathways including: Ras/MAP kinase, phosphatidylinositol 3-kinase and STAT transcription factors. The stimulated erythropoietin receptor appears to have a role in erythroid cell survival. Defects in the erythropoietin receptor may produce erythroleukemia and familial erythrocytosis. …

**Accessions** — [HGNC:3416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3416) · Entrez [2057](https://www.ncbi.nlm.nih.gov/gene/2057) · UniProt [P19235](https://www.uniprot.org/uniprotkb/P19235) · Ensembl [ENSG00000187266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187266)

## Data

Gene col 11908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11908); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11908]; `tensor/DDL_lfc|DDL_z.npy` [11908]; `embed/gene_vectors.npy` [11908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11908 or target_col == 11908). Every well: [[EPOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
