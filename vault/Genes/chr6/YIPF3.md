---
symbol: "YIPF3"
type: "gene"
col: 5986
ensembl_id: "ENSG00000137207"
name: "Yip1 domain family member 3"
location: "6p21.1"
module: 74
arm: "+"
pooled_cpm: 28.93
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# YIPF3

*Yip1 domain family member 3* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.44× (z +5.5, q 2e-05, up in 29 of 46 measured lines) ⚠ transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.64× (z +4.8, q 4e-04, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.556× (z -8.8, q 7e-16, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUD31]] (+0.70, fdr 9e-06), [[YIPF5]] (+0.65, fdr 7e-06), [[SLU7]] (+0.64, fdr 1e-05); moves opposite to [[UBE2G2]] (-0.59, fdr 1e-05), [[ADAT2]] (-0.59, fdr 1e-05), [[MRPS25]] (-0.54, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.5 | 2e-05 | 29/46 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 4e-04 | 31/48 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.4 | 0.002 | 25/48 (HT-29, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.4 | 0.002 | 22/44 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.022 | 20/46 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.050 | 15/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.066 | 16/48 (J82, A-172, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.085 | 12/48 (NCI-H1792, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.2 | 0.092 | 16/45 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -8.8 | 7e-16 | 45/48 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -8.4 | 9e-15 | 41/48 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.575×** | -8.3 | 2e-14 | 39/48 (NCI-H460, KATO III, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -7.5 | 8e-12 | 38/47 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -6.7 | 2e-09 | 32/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.715×** | -5.0 | 5e-05 | 28/47 (SW 1271, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.735×** | -4.4 | 7e-04 | 24/47 (HepG2/C3A, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -3.2 | 0.093 | 20/48 (HOP62, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.097 | 20/48 (COLO 205, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | 0.671× | -3.1 | 0.10 | 17/48 (COLO 205, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.729× | -3.1 | 0.10 | 13/48 (SHP-77, NCI-H460, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.202× (z -9.1) |
| [[H4 (line)]] | wt | 49.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.244× (z -9.7) |
| [[A-172 (line)]] | wt | 33.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.322× (z -9.6) |
| [[A-427 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.157× (z -11.4) |
| [[Hs 766T (line)]] | wt | 27.7 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0936× (z -8.6) |
| [[HT-29 (line)]] | alt | 34.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.326× (z -9.6) |
| [[KATO III (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.30× (z +8.6) ⚠ transcription drop | — |
| [[SW480 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUD31]] | +0.70 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[YIPF5]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 | same gene group; STRING 746 |
| [[SLU7]] | +0.64 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[GOLGB1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SPTY2D1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[OSER1]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[OTUD5]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[CIR1]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ELOF1]] | +0.61 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[WBP1]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ADAT2]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[MRPS25]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RANBP1]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[XPO5]] | -0.53 | -0.57 / -0.52 | both halves | 1e-05 | ⚠ same locus (5.3 kb, same strand: neighbours can correlate without regulation) |
| [[OTUD6B]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TUBGCP4]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CLN6]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[LAPTM4B]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CMTM4]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[MRPL42]] | -0.53 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[CPSF6]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[VMA21]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.2, -41.3); signed map (-12.4, 5.4). **Vector** length 83.2, 17.8% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.6 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -8.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -8.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -7.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,511,832-43,516,985 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566C243, KLIP1, dJ337H4.3, FinGER3, Yip5b, YIPFbeta2; previously C6orf109 |
| Gene groups (HGNC) | Yip1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZM5](https://www.uniprot.org/uniprotkb/Q9GZM5) (Protein YIPF3):

> Involved in the maintenance of the Golgi structure. May play a role in hematopoiesis.

**Summary**, from NCBI Gene [25844](https://www.ncbi.nlm.nih.gov/gene/25844):

> Predicted to be involved in cell differentiation. Located in Golgi apparatus and transport vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21023) · Entrez [25844](https://www.ncbi.nlm.nih.gov/gene/25844) · UniProt [Q9GZM5](https://www.uniprot.org/uniprotkb/Q9GZM5) · Ensembl [ENSG00000137207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137207)

## Data

Gene col 5986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5986); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5986]; `tensor/DDL_lfc|DDL_z.npy` [5986]; `embed/gene_vectors.npy` [5986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5986 or target_col == 5986). Every well: [[YIPF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
