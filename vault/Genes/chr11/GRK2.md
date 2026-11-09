---
symbol: "GRK2"
type: "gene"
col: 10330
ensembl_id: "ENSG00000173020"
name: "G protein-coupled receptor kinase 2"
location: "11q13.2"
module: 126
arm: "+"
pooled_cpm: 19.58
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# GRK2

*G protein-coupled receptor kinase 2* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.56× (z +7.0, q 1e-09, up in 20 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.53× (z +6.8, q 2e-09, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.458× (z -12.7, q 6e-34, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8]] (+0.64, fdr 7e-06), [[AKT1]] (+0.63, fdr 7e-06), [[MAN2A2]] (+0.61, fdr 4e-05); moves opposite to [[SMIM30]] (-0.50, fdr 3e-05), [[SNRPB2]] (-0.45, fdr 5e-05), [[NOL7]] (-0.44, fdr 3e-04, ⚠ NOL7 in the vector space only through flagged drug-doses), [[CCSER2]] (-0.44, fdr 8e-05).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.0 | 1e-09 | 20/31 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.0 | 1e-09 | 23/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +6.8 | 2e-09 | 27/48 (SHP-77, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +5.2 | 4e-05 | 19/43 (AsPC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.7 | 2e-04 | 20/46 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.003 | 13/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.1 | 0.004 | 16/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.020 | 13/44 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mozavaptan (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.062 | 3/47 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.070 | 9/47 (NCI-H2030, A-172, …) | top dose only |  |
| [[Erythromycin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.083 | 11/47 (SW 900, LS 180, …) | rises with dose | position effect removed |
| [[Erythromycin (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.094 | 7/47 (SW48, AsPC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.458×** | -12.7 | 6e-34 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.466×** | -12.4 | 1e-32 | 44/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.511×** | -10.9 | 3e-25 | 40/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -8.4 | 5e-15 | 30/47 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -6.6 | 6e-09 | 34/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.726×** | -5.0 | 5e-05 | 23/46 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.742×** | -4.7 | 3e-04 | 21/46 (SW480, HCT15, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.820×** | -4.6 | 3e-04 | 19/45 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.766×** | -4.1 | 0.003 | 15/46 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.631×** | -3.9 | 0.005 | 13/48 (A-172, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -3.4 | 0.030 | 14/48 (LS 180, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.034 | 16/47 (SHP-77, SW 900, …) | two highest doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.813×** | -3.2 | 0.054 | 9/47 (SK-MEL-2, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 0.870× | -3.2 | 0.055 | 10/48 (C32, SHP-77, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.871× | -3.2 | 0.058 | 10/48 (SW 1271, LS 180, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.873× | -3.1 | 0.065 | 12/48 (HT-29, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -13.2) |
| [[C32 (line)]] | wt | 21.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.7) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.0) |
| [[A-427 (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -10.4) |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.7) |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0474× (z -17.1) |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.265× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -8.8) |
| [[PANC-1 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[AKT1]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 778 |
| [[MAN2A2]] | +0.61 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[CNNM3]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ULK3]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 | pathway: Hedgehog 'on' state |
| [[PCGF2]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[DAZAP1]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TLE5]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ADCY6]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 | pathway: Ca-dependent events |
| [[PLXNB1]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CCNL2]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[LLGL1]] | +0.57 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | -0.50 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SNRPB2]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[NOL7]] ⚠ | -0.44 | -0.28 / -0.45 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CCSER2]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[KLHL9]] | -0.44 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, -23.7); signed map (-25.5, -1.3). **Vector** length 72.3, 12.6% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | -1.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,266,473-67,286,556 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BARK1; previously ADRBK1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; G protein-coupled receptor kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 20 pathways, smallest: Activation of SMO; CaM pathway; Calmodulin induced events |
| Matched by | ensembl_id |

**Function**, from UniProt [P25098](https://www.uniprot.org/uniprotkb/P25098) (G protein-coupled receptor kinase 2):

> Specifically phosphorylates the activated forms of G protein-coupled receptors. Such receptor phosphorylation initiates beta-arrestin-mediated receptor internalization, and signaling events leading to their desensitization. Phosphorylates the agonist-occupied form of the beta-adrenergic and closely related receptors, probably inducing a desensitization of them. Phosphorylates catecholamine-activated ADRB2 to regulate physiological cardiomyocyte contraction rate responses (By similarity). Also …

**Summary**, from NCBI Gene [156](https://www.ncbi.nlm.nih.gov/gene/156):

> This gene encodes a member of the G protein-coupled receptor kinase family of proteins. The encoded protein phosphorylates the beta-adrenergic receptor as well as a wide range of other substrates including non-GPCR cell surface receptors, and cytoskeletal, mitochondrial, and transcription factor proteins. Data from rodent models supports a role for this gene in embryonic development, heart function and metabolism. Elevated expression of this gene has been observed in human patients with heart …

**Accessions** — [HGNC:289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:289) · Entrez [156](https://www.ncbi.nlm.nih.gov/gene/156) · UniProt [P25098](https://www.uniprot.org/uniprotkb/P25098) · Ensembl [ENSG00000173020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173020)

## Data

Gene col 10330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10330); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10330]; `tensor/DDL_lfc|DDL_z.npy` [10330]; `embed/gene_vectors.npy` [10330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10330 or target_col == 10330). Every well: [[GRK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
