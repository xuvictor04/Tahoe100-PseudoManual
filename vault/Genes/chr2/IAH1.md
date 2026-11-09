---
symbol: "IAH1"
type: "gene"
col: 5549
ensembl_id: "ENSG00000134330"
name: "isoamyl acetate hydrolyzing esterase 1 (putative)"
location: "2p25.1"
module: 221
arm: "+"
pooled_cpm: 21.49
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# IAH1

*isoamyl acetate hydrolyzing esterase 1 (putative)* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.67× (z +8.5, q 1e-14, up in 27 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -14.1, q 3e-42, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECHDC3]] (+0.64, fdr 1e-05), [[SLC66A3]] (+0.60, fdr 7e-06), [[UBE2Q2P1]] (+0.60, fdr 1e-05); moves opposite to [[CFAP44]] (-0.58, fdr 1e-05), [[NASP]] (-0.52, fdr 3e-05), [[SLC12A2]] (-0.50, fdr 3e-05).
> It is in [[Module 221]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +8.5 | 1e-14 | 27/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.0 | 5e-07 | 19/28 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.7 | 6e-04 | 18/45 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.0 | 0.007 | 14/34 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.007 | 16/48 (LoVo, LS 180, …) | top dose only | low cells (technical?) |
| [[Erythromycin (drug)]] 5 µM |  | 1.21× | +3.2 | 0.15 | 8/48 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.17 | 5/46 (NCI-H23, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -14.1 | 3e-42 | 39/46 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.597×** | -8.5 | 5e-15 | 33/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.607×** | -8.2 | 4e-14 | 34/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -7.9 | 3e-13 | 33/47 (A549, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.670×** | -6.6 | 5e-09 | 30/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -6.4 | 2e-08 | 24/45 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.771×** | -6.1 | 1e-07 | 29/45 (A549, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -4.8 | 1e-04 | 20/48 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.7 | 2e-04 | 18/46 (HCT15, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -4.5 | 5e-04 | 18/48 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.764×** | -4.4 | 5e-04 | 20/48 (HOP62, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.779×** | -4.1 | 0.002 | 16/48 (RPMI-7951, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -4.0 | 0.003 | 16/48 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.797×** | -3.7 | 0.008 | 21/47 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.018 | 15/47 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.635×** | -3.2 | 0.039 | 9/46 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.645×** | -3.1 | 0.055 | 12/47 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 47.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.6) |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.3) |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.6) |
| [[PANC-1 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.7) |
| [[RKO (line)]] | wt | 21.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.2) |
| [[A-172 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC3]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SLC66A3]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[UBE2Q2P1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GALNT11]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[FBXL2]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[STPG1]] | +0.54 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[FAM219B]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SVIL-AS1-1]] | +0.52 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZDHHC24]] | +0.51 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[UBE2Q2P13]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[CSKMT]] | +0.51 | +0.37 / +0.46 | both halves | 9e-05 |  |
| [[BBS7]] | +0.51 | +0.40 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP44]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[NASP]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[SLC12A2]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[CDC6]] | -0.48 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[POU5F1B]] | -0.45 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[SH2D4A]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[DNMT1]] | -0.44 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[HNRNPAB]] | -0.44 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[SMC1A]] | -0.43 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[MYH15]] | -0.43 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[TNFSF15]] | -0.43 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ESCO2]] | -0.43 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.2, -2.8); signed map (-32.3, -5.0). **Vector** length 51.7, 7.38% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.3 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.1 | -14.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -1.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | isoamyl acetate hydrolyzing esterase 1 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,473,658-9,496,543 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAA2](https://www.uniprot.org/uniprotkb/Q2TAA2) (Isoamyl acetate-hydrolyzing esterase 1 homolog):

> Probable lipase.

**Summary**, from NCBI Gene [285148](https://www.ncbi.nlm.nih.gov/gene/285148):

> Enables identical protein binding activity. Predicted to be involved in lipid catabolic process. Predicted to act upstream of or within gene expression. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27696) · Entrez [285148](https://www.ncbi.nlm.nih.gov/gene/285148) · UniProt [Q2TAA2](https://www.uniprot.org/uniprotkb/Q2TAA2) · Ensembl [ENSG00000134330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134330)

## Data

Gene col 5549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5549); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5549]; `tensor/DDL_lfc|DDL_z.npy` [5549]; `embed/gene_vectors.npy` [5549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5549 or target_col == 5549). Every well: [[IAH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IAH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
