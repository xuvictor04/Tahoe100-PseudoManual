---
symbol: "ANO8"
type: "gene"
col: 1094
ensembl_id: "ENSG00000074855"
name: "anoctamin 8"
location: "19p13.11"
module: 100
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ANO8

*anoctamin 8* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +7.8, q 4e-12, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.38× (z +3.9, q 0.018, up in 9 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.509× (z -11.9, q 1e-29, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEDS1]] (+0.67, fdr 1e-05), [[OSBPL7]] (+0.66, fdr 1e-05), [[MPND]] (+0.66, fdr 1e-05); moves opposite to [[TFAM]] (-0.62, fdr 2e-05), [[ENOX2]] (-0.61, fdr 3e-05), [[KRR1]] (-0.58, fdr 2e-05).
> It is in [[Module 100]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.8 | 4e-12 | 8/10 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.7 | 9e-04 | 7/28 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.018 | 9/43 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.022 | 11/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.6 | 0.039 | 6/20 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.048 | 7/36 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.4 | 0.048 | 11/36 (BT-474, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.048 | 10/45 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.048 | 8/47 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.048 | 8/45 (HOP62, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.083 | 3/47 (SW48, H4, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 4/48 (AsPC-1, A-427, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.509×** | -11.9 | 1e-29 | 32/40 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -11.3 | 3e-27 | 33/47 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.410×** | -11.1 | 3e-26 | 32/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.422×** | -10.7 | 1e-24 | 27/40 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -9.5 | 3e-19 | 30/45 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.492×** | -8.8 | 1e-16 | 33/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.551×** | -7.4 | 1e-11 | 25/47 (C32, NCI-H460, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -7.3 | 2e-11 | 24/41 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.9 | 4e-10 | 24/43 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -6.3 | 1e-08 | 24/47 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -6.2 | 2e-08 | 21/46 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.607×** | -6.2 | 3e-08 | 22/46 (C-33 A, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.664×** | -5.1 | 2e-05 | 19/47 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.705×** | -4.3 | 6e-04 | 19/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -4.3 | 6e-04 | 14/42 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -4.2 | 8e-04 | 13/44 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 11.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0587× (z -11.1) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.160× (z -11.0) |
| [[A549 (line)]] | wt | 4.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -8.6) |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 6.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.7) |
| [[PANC-1 (line)]] | alt | 3.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -9.5) |
| [[SW 900 (line)]] | alt | 7.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -8.5) |
| [[SW1417 (line)]] | alt | 6.06 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.110× (z -9.2) |
| [[A-427 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEDS1]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MPND]] | +0.66 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[C2CD2L]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ADGRB2]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.64 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[RAB3A]] | +0.64 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.64 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MAP4K2]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PDZD7]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[KIFC2]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAM]] | -0.62 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[ENOX2]] | -0.61 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[KRR1]] | -0.58 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.57 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NIPAL2]] | -0.56 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[DPH5-DT]] | -0.56 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[LINC01340]] | -0.55 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RGS5]] | -0.55 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[E2F3]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.54 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MSRA]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TRMT5]] | -0.54 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.5, -4.6); signed map (-30.0, -1.4). **Vector** length 60.2, 8.53% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,323,223-17,334,855 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1623, TMEM16H |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 10 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCE9](https://www.uniprot.org/uniprotkb/Q9HCE9) (Anoctamin-8):

> Does not exhibit calcium-activated chloride channel (CaCC) activity.

**Summary**, from NCBI Gene [57719](https://www.ncbi.nlm.nih.gov/gene/57719):

> Enables intracellularly calcium-gated chloride channel activity. Involved in chloride transmembrane transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29329) · Entrez [57719](https://www.ncbi.nlm.nih.gov/gene/57719) · UniProt [Q9HCE9](https://www.uniprot.org/uniprotkb/Q9HCE9) · Ensembl [ENSG00000074855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074855)

## Data

Gene col 1094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1094); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1094]; `tensor/DDL_lfc|DDL_z.npy` [1094]; `embed/gene_vectors.npy` [1094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1094 or target_col == 1094). Every well: [[ANO8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
