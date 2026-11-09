---
symbol: "RSPH3"
type: "gene"
col: 5059
ensembl_id: "ENSG00000130363"
name: "radial spoke head 3"
location: "6q25.3"
module: 20
arm: "-"
pooled_cpm: 52.76
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RSPH3

*radial spoke head 3* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.40× (z +6.6, q 3e-08, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.595× (z -10.0, q 8e-21, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD11]] (+0.58, fdr 1e-05), [[DDI2]] (+0.58, fdr 1e-05), [[MYO9A]] (+0.55, fdr 1e-05); moves opposite to [[PTGFRN]] (-0.59, fdr 1e-05), [[KAT2A]] (-0.56, fdr 2e-05), [[NUP205]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF674]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +6.6 | 3e-08 | 39/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +5.8 | 2e-06 | 27/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.9 | 2e-04 | 27/47 (COLO 205, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 2e-04 | 22/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 22/48 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.010 | 16/48 (KATO III, PANC-1, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.014 | 14/48 (SW48, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.022 | 14/48 (NCI-H2030, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.026 | 17/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.039 | 16/47 (SW48, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.049 | 11/48 (RKO, C-33 A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.18× | +3.1 | 0.083 | 9/47 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +3.1 | 0.097 | 14/48 (RKO, A-427, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.097 | 11/48 (SNU-423, HT-29, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.097 | 11/48 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -10.0 | 8e-21 | 35/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -9.2 | 1e-17 | 43/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -8.3 | 2e-14 | 33/47 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -8.3 | 2e-14 | 34/48 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -7.1 | 2e-10 | 35/48 (MIA PaCa-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -6.8 | 1e-09 | 28/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.712×** | -6.6 | 5e-09 | 26/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -6.4 | 1e-08 | 29/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.735×** | -5.9 | 2e-07 | 25/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -5.8 | 4e-07 | 28/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -4.6 | 2e-04 | 18/37 (NCI-H1573, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -4.5 | 4e-04 | 21/48 (SNU-423, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.689×** | -3.8 | 0.007 | 21/44 (HCT15, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.013 | 15/48 (NCI-H2030, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.021 | 17/49 (MIA PaCa-2, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.723×** | -3.3 | 0.036 | 11/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.839× | -3.2 | 0.044 | 17/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.890× | -3.2 | 0.046 | 9/49 (SK-MEL-2, SW 900, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.079 | 11/48 (NCI-H23, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.05 µM |  | 0.857× | -3.0 | 0.079 | 7/48 (PANC-1, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.9 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 0 | 5 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.149× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 44.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.303× (z -10.0) |
| [[HCT15 (line)]] | alt | 134 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -11.0) |
| [[HT-29 (line)]] | alt | 56.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.367× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.383× (z -8.9) |
| [[A-172 (line)]] | wt | 64.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[H4 (line)]] | wt | 47.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0916× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -8.8) |
| [[SNU-423 (line)]] | alt | 115 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.438× (z -9.2) |
| [[SW480 (line)]] | alt | 106 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.487× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD11]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DDI2]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MYO9A]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SERTAD1]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ARRDC4]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[BTG1]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[H3-3B]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ZKSCAN1]] | +0.53 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[METTL23]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF699]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[HMGCL]] | +0.51 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GALE]] | +0.51 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGFRN]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[KAT2A]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[NUP205]] | -0.54 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ILF3]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ASIC1]] | -0.54 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MSI2]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[STT3B]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[PON2]] | -0.51 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[TTPA]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[LIG3]] | -0.51 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[GPC4]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF674]] | C | ZNF674's natural level strengthens RSPH3's drug response | ZNF674's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.04; direction clear | 0.085 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.4, -23.0); signed map (-2.1, 10.2). **Vector** length 92.6, 22.6% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.4 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.7 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.2 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.8 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.3 | -2.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | radial spoke head 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,972,871-159,000,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ111C20.1, RSP3; previously RSHL2 |
| Gene groups (HGNC) | Axonemal radial spoke subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UC2](https://www.uniprot.org/uniprotkb/Q86UC2) (Radial spoke head protein 3 homolog):

> Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia (By similarity). Functions as a protein kinase A-anchoring protein that scaffolds the cAMP-dependent protein kinase holoenzyme. May serve as a point of convergence for MAPK and PKA signaling in cilia.

**Summary**, from NCBI Gene [83861](https://www.ncbi.nlm.nih.gov/gene/83861):

> The protein encoded by this gene acts as a protein kinase A anchoring protein. Mutations in this gene cause primary ciliary dyskinesia; a disorder characterized by defects of the axoneme in motile cilia and sperm flagella. The homolog of this gene was first identified in the blue-green algae Chlamydomonas as encoding a radial spoke protein that formed a structural component of motile cilia and flagella. Alternate splicing results in multiple transcript variants encoding distinct isoforms. …

**Accessions** — [HGNC:21054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21054) · Entrez [83861](https://www.ncbi.nlm.nih.gov/gene/83861) · UniProt [Q86UC2](https://www.uniprot.org/uniprotkb/Q86UC2) · Ensembl [ENSG00000130363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130363)

## Data

Gene col 5059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5059); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5059]; `tensor/DDL_lfc|DDL_z.npy` [5059]; `embed/gene_vectors.npy` [5059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5059 or target_col == 5059). Every well: [[RSPH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSPH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
