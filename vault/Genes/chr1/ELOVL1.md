---
symbol: "ELOVL1"
type: "gene"
col: 824
ensembl_id: "ENSG00000066322"
name: "ELOVL fatty acid elongase 1"
location: "1p34.2"
module: 184
arm: "+"
pooled_cpm: 22.23
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# ELOVL1

*ELOVL fatty acid elongase 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.56× (z +5.2, q 1e-04, up in 26 of 44 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.69× (z +4.0, q 0.009, up in 20 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -10.5, q 4e-23, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOC]] (+0.70, fdr 7e-06), [[ORMDL2]] (+0.64, fdr 7e-06), [[S100A16]] (+0.62, fdr 1e-05); moves opposite to [[RPRD2]] (-0.58, fdr 3e-05), [[PNISR]] (-0.56, fdr 2e-05), [[FAM151B-DT]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LAMC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.56×** | +5.2 | 1e-04 | 26/44 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.0 | 2e-04 | 4/47 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.52×** | +4.9 | 2e-04 | 19/38 (A-172, A498, …) | two highest doses | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.009 | 20/42 (A549, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.015 | 21/45 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.38×** | +3.6 | 0.023 | 15/32 (A-172, A498, …) | two highest doses | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.61×** | +3.6 | 0.023 | 11/45 (MIA PaCa-2, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.10 | 17/46 (hTERT-HPNE, H4, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -10.5 | 4e-23 | 35/46 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.269×** | -6.1 | 3e-07 | 36/47 (SNU-1, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -5.1 | 7e-05 | 25/47 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.666×** | -4.6 | 5e-04 | 27/45 (SK-MEL-2, HS-578T, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -4.1 | 0.006 | 23/44 (HS-578T, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.038 | 18/45 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.072 | 18/47 (BT-474, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.763×** | -3.2 | 0.090 | 21/45 (SNU-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 14.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -14.1) |
| [[SNU-1 (line)]] | wt | 43.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.0) |
| [[HS-578T (line)]] | alt | 41.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.4) |
| [[A-172 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[A498 (line)]] | wt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.4) |
| [[A549 (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.9) |
| [[J82 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.0) |
| [[KATO III (line)]] | alt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.3) |
| [[PANC-1 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.166× (z -10.3) |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOC]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ORMDL2]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[S100A16]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SPRYD3]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[KCTD5]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MFSD10]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[IPO13]] | +0.58 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[SLC10A3]] | +0.57 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[BAK1]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PORCN]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPRD2]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PNISR]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[FAM151B-DT]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[MATR3]] | -0.54 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[PPP1R3E]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[HNMT]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RBM33]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[MTERF2]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[MCCC1]] | -0.52 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[LUC7L2]] | -0.51 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SREK1]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[STAG2]] | -0.49 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC2]] | B | LAMC2 activity raises ELOVL1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without LAMC2 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[CD59]] | B | CD59 activity raises ELOVL1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without CD59 | 0.089 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (15.0, -1.0); signed map (-16.1, 18.9). **Vector** length 87.9, 21.6% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.5 | +2.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.2 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.6 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -10.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ELOVL fatty acid elongase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,363,398-43,368,074 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ssc1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; ELOVL fatty acid elongase family |
| Reactome | 7 pathways, smallest: Linoleic acid (LA) metabolism; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism; alpha-linolenic acid (ALA) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW60](https://www.uniprot.org/uniprotkb/Q9BW60) (Very long chain fatty acid elongase 1):

> Catalyzes the first and rate-limiting reaction of the four reactions that constitute the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle. Condensing enzyme that exhibits activity toward saturated and monounsaturated acyl-CoA substrates, with the highest activity towards C22:0 acyl-CoA. May participate in the production of both saturated and …

**Summary**, from NCBI Gene [64834](https://www.ncbi.nlm.nih.gov/gene/64834):

> Enables fatty acid elongase activity. Involved in fatty acid biosynthetic process and sphingolipid biosynthetic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14418) · Entrez [64834](https://www.ncbi.nlm.nih.gov/gene/64834) · UniProt [Q9BW60](https://www.uniprot.org/uniprotkb/Q9BW60) · Ensembl [ENSG00000066322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066322)

## Data

Gene col 824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 824); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 824]; `tensor/DDL_lfc|DDL_z.npy` [824]; `embed/gene_vectors.npy` [824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 824 or target_col == 824). Every well: [[ELOVL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOVL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
