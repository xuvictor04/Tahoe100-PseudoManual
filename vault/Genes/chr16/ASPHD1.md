---
symbol: "ASPHD1"
type: "gene"
col: 10545
ensembl_id: "ENSG00000174939"
name: "aspartate beta-hydroxylase domain containing 1"
location: "16p11.2"
module: 161
arm: "+"
pooled_cpm: 28.35
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# ASPHD1

*aspartate beta-hydroxylase domain containing 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.44× (z +13.5, q 1e-38, up in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.41× (z +5.2, q 3e-05, up in 19 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.727× (z -4.8, q 7e-04, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL1]] (+0.54, fdr 2e-05), [[TBC1D10A]] (+0.53, fdr 2e-05), [[FPGS]] (+0.53, fdr 5e-05); moves opposite to [[CAVIN2]] (-0.55, fdr 2e-05), [[ZBTB14]] (-0.54, fdr 1e-05), [[ARMC8]] (-0.53, fdr 2e-05).
> It is in [[Module 161]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +13.5 | 1e-38 | 32/37 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.8 | 4e-20 | 19/27 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +9.2 | 5e-18 | 26/34 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.2 | 3e-05 | 19/41 (RKO, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.1 | 0.004 | 20/42 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.007 | 17/41 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.007 | 15/39 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.007 | 18/41 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.008 | 14/41 (SK-MEL-2, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.8 | 0.010 | 19/40 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.013 | 5/40 (HepG2/C3A, A-172, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.019 | 15/42 (A-172, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 1.17× | +3.2 | 0.054 | 9/42 (J82, SNU-1, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.054 | 12/42 (A-427, A-172, …) | top dose only | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.054 | 6/41 (SNU-423, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.056 | 7/41 (RPMI-7951, RKO, …) | two highest doses | position effect removed |
| [[Erythromycin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.077 | 5/42 (Hs 766T, LoVo, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.727×** | -4.8 | 7e-04 | 22/41 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.778×** | -3.8 | 0.036 | 12/42 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.785×** | -3.7 | 0.043 | 17/42 (A549, AsPC-1, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.060 | 11/42 (SW1417, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.659× | -3.3 | 0.11 | 15/40 (Hs 766T, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.809× | -3.2 | 0.12 | 14/42 (NCI-H460, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 0.814× | -3.1 | 0.12 | 10/42 (NCI-H1792, A498, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.803× | -3.1 | 0.12 | 13/41 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.809× | -3.1 | 0.12 | 15/40 (NCI-H23, NCI-H2347, …) | rises with dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.819× | -3.0 | 0.12 | 10/42 (A498, SNU-423, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.821× | -3.0 | 0.12 | 12/42 (NCI-H1792, NCI-H2030, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.5) | — |
| [[A498 (line)]] | wt | 98.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.430× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0485× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.4) | — |
| [[LoVo (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -9.1) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H460 (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +12.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.5) |
| [[SW1417 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.407× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TBC1D10A]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[FPGS]] | +0.53 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[SARM1]] | +0.51 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[SLC35C2]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MIR22HG]] | +0.49 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ASMTL]] | +0.49 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[MEG3]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[GPSM1]] | +0.47 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SAMD4B]] | +0.47 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[WNT9A]] | +0.47 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[COL7A1]] | +0.47 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN2]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZBTB14]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ARMC8]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[THAP11]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[CLASP1]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TNRC6A]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[OSGEPL1]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[PDS5B]] | -0.47 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[VANGL1]] | -0.46 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[NFIA]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[RAD21]] | -0.46 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CAND1]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, -9.8); signed map (-21.5, 27.2). **Vector** length 84.0, 18.3% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | aspartate beta-hydroxylase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,900,375-29,919,864 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Aspartate beta-hydroxylase domain containing |
| Matched by | ensembl_id |

UniProt [Q5U4P2](https://www.uniprot.org/uniprotkb/Q5U4P2) carries no function annotation.

**Summary**, from NCBI Gene [253982](https://www.ncbi.nlm.nih.gov/gene/253982):

> Predicted to enable dioxygenase activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27380) · Entrez [253982](https://www.ncbi.nlm.nih.gov/gene/253982) · UniProt [Q5U4P2](https://www.uniprot.org/uniprotkb/Q5U4P2) · Ensembl [ENSG00000174939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174939)

## Data

Gene col 10545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10545); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10545]; `tensor/DDL_lfc|DDL_z.npy` [10545]; `embed/gene_vectors.npy` [10545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10545 or target_col == 10545). Every well: [[ASPHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASPHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
