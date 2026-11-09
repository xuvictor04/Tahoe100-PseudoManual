---
symbol: "EFHD2"
type: "gene"
col: 6640
ensembl_id: "ENSG00000142634"
name: "EF-hand domain family member D2"
location: "1p36.21"
module: 112
arm: "+"
pooled_cpm: 75.04
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# EFHD2

*EF-hand domain family member D2* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +12.5, q 6e-33, up in 36 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 1.34× (z +4.5, q 5e-04, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -10.4, q 8e-23, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMIP]] (+0.54, fdr 3e-05), [[PICALM]] (+0.53, fdr 3e-05), [[ACTN4]] (+0.50, fdr 9e-05); moves opposite to [[PSMC2]] (-0.47, fdr 1e-04), [[ZNF528-AS1]] (-0.46, fdr 2e-04), [[ZNF737]] (-0.46, fdr 5e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.25×** | +12.5 | 6e-33 | 36/44 (RKO, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +9.5 | 6e-19 | 30/38 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.79×** | +8.6 | 1e-15 | 27/36 (LoVo, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.51×** | +6.3 | 3e-08 | 25/45 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.43×** | +5.5 | 4e-06 | 31/45 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.35×** | +4.6 | 3e-04 | 24/46 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 5e-04 | 28/45 (HOP62, SW 900, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.010 | 24/46 (KATO III, J82, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.28×** | +3.8 | 0.010 | 22/46 (NCI-H460, Hs 766T, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.011 | 22/45 (NCI-H460, A549, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.58×** | +3.7 | 0.012 | 22/47 (Hs 766T, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +3.5 | 0.019 | 20/46 (A549, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.024 | 15/46 (PANC-1, A-172, …) | two highest doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.060 | 14/46 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -10.4 | 8e-23 | 29/45 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.712×** | -7.3 | 6e-11 | 31/46 (A549, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.480×** | -5.9 | 8e-07 | 34/47 (A498, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.759×** | -4.2 | 0.004 | 23/46 (HCT15, J82, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -3.6 | 0.034 | 22/47 (HCT15, LS 180, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.850× | -3.5 | 0.044 | 14/47 (NCI-H460, A498, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.797×** | -3.5 | 0.044 | 21/46 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.792×** | -3.3 | 0.059 | 16/46 (NCI-H1573, BT-474, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.3 | 0.059 | 4/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.778×** | -3.3 | 0.059 | 17/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -3.3 | 0.059 | 11/46 (A498, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 168 | 0 | 8 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.1) |
| [[Hs 766T (line)]] | wt | 385 | 2 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.9) ⚠ cell-cycle shift, explains ~84% of this change | [[Panobinostat (drug)]] 5 µM 0.363× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 162 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -19.8) |
| [[A549 (line)]] | wt | 125 | 1 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.54× (z +9.4) ⚠ cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.487× (z -10.2) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H460 (line)]] | wt | 105 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +10.6) ⚠ cell-cycle shift, explains ~84% of this change | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.9) |
| [[LoVo (line)]] | wt | 21.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.61× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 59.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 89.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.0) |
| [[COLO 205 (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.1) |
| [[HOP62 (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.89× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 56.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 38.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.431× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.2) |
| [[HCT15 (line)]] | alt | 69.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -15.1) |
| [[HepG2_C3A (line)]] | wt | 82.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.266× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 55.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.1) | — |
| [[J82 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -8.6) |
| [[KATO III (line)]] | alt | 72.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 65.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.6) |
| [[LS 180 (line)]] | wt | 77.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.02× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0845× (z -9.6) |
| [[SW1417 (line)]] | alt | 55.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.3) |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PICALM]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[ACTN4]] | +0.50 | +0.51 / +0.37 | both halves | 9e-05 |  |
| [[SDC4]] | +0.50 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[SBNO2]] | +0.49 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[C12orf75]] | +0.48 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[PPP4R4]] | +0.48 | +0.45 / +0.34 | both halves | 1e-04 |  |
| [[MIR155HG]] | +0.48 | +0.42 / +0.39 | both halves | 6e-05 |  |
| [[RUNX1]] | +0.47 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ITPR3]] | +0.47 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[AGRN]] | +0.47 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[MAP2K3]] | +0.46 | +0.44 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC2]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ZNF528-AS1]] | -0.46 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[ZNF737]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[KAT6B]] | -0.45 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[TXNL1]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[TXNDC15]] | -0.45 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[PSMB5]] | -0.45 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[SPART-AS1]] | -0.44 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[UFC1]] | -0.44 | -0.45 / -0.23 | both halves | 5e-04 |  |
| [[NGDN]] | -0.43 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[SMIM10L1]] | -0.43 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[DHRS4]] | -0.43 | -0.36 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises EFHD2's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without TGM2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[SMAD4]] | C | SMAD4 activity lowers EFHD2's level | lines that do not express SMAD4 (4) vs lines expressing it (46) | 3.44× higher at baseline in the lines without SMAD4 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC26A11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.350). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.9, 29.5); signed map (-13.7, 31.4). **Vector** length 95.6, 23.2% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -6.4 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.9 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand domain family member D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,409,888-15,430,339 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4342 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: RHOD GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C19](https://www.uniprot.org/uniprotkb/Q96C19) (EF-hand domain-containing protein D2):

> May regulate B-cell receptor (BCR)-induced immature and primary B-cell apoptosis. Plays a role as negative regulator of the canonical NF-kappa-B-activating branch. Controls spontaneous apoptosis through the regulation of BCL2L1 abundance.

**Summary**, from NCBI Gene [79180](https://www.ncbi.nlm.nih.gov/gene/79180):

> Enables actin filament binding activity and calcium ion sensor activity. Involved in actin crosslink formation. Is active in lamellipodium. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28670) · Entrez [79180](https://www.ncbi.nlm.nih.gov/gene/79180) · UniProt [Q96C19](https://www.uniprot.org/uniprotkb/Q96C19) · Ensembl [ENSG00000142634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142634)

## Data

Gene col 6640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6640); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6640]; `tensor/DDL_lfc|DDL_z.npy` [6640]; `embed/gene_vectors.npy` [6640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6640 or target_col == 6640). Every well: [[EFHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
