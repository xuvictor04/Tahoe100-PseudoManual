---
symbol: "ACADS"
type: "gene"
col: 4392
ensembl_id: "ENSG00000122971"
name: "acyl-CoA dehydrogenase short chain"
location: "12q24.31"
module: 24
arm: "+"
pooled_cpm: 5.48
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ACADS

*acyl-CoA dehydrogenase short chain* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.48× (z +4.7, q 0.001, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.65× (z +4.5, q 0.001, up in 7 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.402× (z -11.4, q 4e-27, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX11B]] (+0.57, fdr 4e-05), [[ZNF500]] (+0.57, fdr 1e-04), [[TMEM134]] (+0.55, fdr 6e-05); moves opposite to [[GSPT1]] (-0.49, fdr 9e-05), [[REEP3]] (-0.48, fdr 5e-05), [[ARAP2]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.7 | 0.001 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +4.6 | 0.001 | 8/46 (LS 180, PANC-1, …) | top dose only | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 0.001 | 7/34 (A498, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.2 | 0.004 | 7/28 (LoVo, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.004 | 17/41 (LOX-IMVI, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.006 | 6/31 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.0 | 0.006 | 4/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.006 | 9/42 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.026 | 4/44 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.026 | 4/44 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.026 | 2/13 (NCI-H2030, SW480) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.036 | 5/40 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.1 | 0.094 | 5/33 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -11.4 | 4e-27 | 40/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -9.7 | 5e-20 | 34/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.459×** | -9.7 | 5e-20 | 25/38 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.583×** | -6.7 | 2e-09 | 22/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -6.3 | 4e-08 | 22/43 (A549, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -6.1 | 1e-07 | 19/44 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.740×** | -5.3 | 1e-05 | 20/39 (CFPAC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -4.9 | 6e-05 | 12/44 (NCI-H460, RKO, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.758×** | -4.9 | 7e-05 | 18/47 (NCI-H460, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -4.7 | 2e-04 | 16/33 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.5 | 4e-04 | 15/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.704×** | -4.4 | 6e-04 | 12/47 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.2 | 0.001 | 16/39 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -3.9 | 0.004 | 12/39 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.009 | 12/46 (HS-578T, NCI-H661, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.773×** | -3.2 | 0.050 | 6/44 (MIA PaCa-2, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0654× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 8.08 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -10.5) |
| [[HCT15 (line)]] | alt | 7.97 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0610× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0645× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 5.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX11B]] | +0.57 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[ZNF500]] | +0.57 | +0.33 / +0.71 | both halves | 1e-04 |  |
| [[TMEM134]] | +0.55 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[CLASRP]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[NSUN5P1-1]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[CDAN1]] | +0.53 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[VPS37D]] | +0.53 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[KLHL12]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RNF7]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[IL17RA]] | +0.52 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[SUGP1]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[CCDC115]] | +0.52 | +0.41 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT1]] | -0.49 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[REEP3]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ARAP2]] | -0.47 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[CDC42BPA]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[EIF4G1]] | -0.46 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[CHML]] | -0.46 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[YWHAZ]] | -0.46 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[NRDC]] | -0.45 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[SLC35F6]] | -0.45 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[MAPRE1]] | -0.45 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.8, -19.3); signed map (-26.5, 5.9). **Vector** length 48.1, 5.69% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.3 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -6.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.6 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -4.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -0.4 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase short chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,725,774-120,740,008 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCAD, ACAD3 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Beta oxidation of butanoyl-CoA to acetyl-CoA; Beta oxidation of hexanoyl-CoA to butanoyl-CoA; mitochondrial fatty acid beta-oxidation of saturated fatty acids |
| Matched by | ensembl_id |

**Function**, from UniProt [P16219](https://www.uniprot.org/uniprotkb/P16219) (Short-chain specific acyl-CoA dehydrogenase, mitochondrial):

> Short-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA dehydrogenases that catalyze the first step of mitochondrial fatty acid beta-oxidation, an aerobic process breaking down fatty acids into acetyl-CoA and allowing the production of energy from fats (By similarity). The first step of fatty acid beta-oxidation consists in the removal of one hydrogen from C-2 and C-3 of the straight-chain fatty acyl-CoA thioester, resulting in the formation of trans-2-enoyl-CoA (By similarity). …

**Summary**, from NCBI Gene [35](https://www.ncbi.nlm.nih.gov/gene/35):

> This gene encodes a tetrameric mitochondrial flavoprotein, which is a member of the acyl-CoA dehydrogenase family. This enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Mutations in this gene have been associated with short-chain acyl-CoA dehydrogenase (SCAD) deficiency. Alternative splicing results in two variants which encode different isoforms. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:90](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:90) · Entrez [35](https://www.ncbi.nlm.nih.gov/gene/35) · UniProt [P16219](https://www.uniprot.org/uniprotkb/P16219) · Ensembl [ENSG00000122971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122971)

## Data

Gene col 4392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4392); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4392]; `tensor/DDL_lfc|DDL_z.npy` [4392]; `embed/gene_vectors.npy` [4392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4392 or target_col == 4392). Every well: [[ACADS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACADS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
