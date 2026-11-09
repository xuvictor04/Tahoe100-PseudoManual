---
symbol: "NSMCE3"
type: "gene"
col: 11628
ensembl_id: "ENSG00000185115"
name: "NSE3 component of SMC5/6 complex"
location: "15q13.1"
module: 11
arm: "+"
pooled_cpm: 7.74
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NSMCE3

*NSE3 component of SMC5/6 complex* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.49× (z +14.3, q 2e-43, up in 38 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0512×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0653×); [[vincristine (drug)]] 0.05 µM in 1 line (Hs 766T 0.0595×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.173×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAX]] (+0.85, fdr 7e-06), [[EID2]] (+0.79, fdr 7e-06), [[MRFAP1L1]] (+0.78, fdr 7e-06); moves opposite to [[TPP2]] (-0.63, fdr 1e-05), [[AP2A1]] (-0.62, fdr 9e-06), [[PMPCA]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KDF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +14.3 | 2e-43 | 38/42 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.26×** | +13.1 | 2e-36 | 43/46 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.20×** | +12.4 | 6e-33 | 43/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.12×** | +12.1 | 1e-31 | 34/36 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +10.4 | 3e-23 | 37/43 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.24×** | +9.0 | 3e-17 | 35/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.86×** | +6.4 | 2e-08 | 26/42 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +5.8 | 3e-07 | 30/46 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.56×** | +5.0 | 4e-05 | 21/36 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +4.9 | 5e-05 | 22/47 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +4.6 | 2e-04 | 20/47 (LOX-IMVI, PANC-1, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.003 | 18/46 (SK-MEL-2, RPMI-7951, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.004 | 20/44 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.011 | 9/47 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.033 | 10/43 (COLO 205, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.046 | 14/47 (SNU-423, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11628.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0512×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0653×); [[vincristine (drug)]] 0.05 µM in 1 line (Hs 766T 0.0595×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.173×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.803× | -3.4 | 0.38 | 10/47 (SW 1271, NCI-H460, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 4.80 | 0 | 2 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0653× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 19.1 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.63× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 6.50 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.7) |
| [[COLO 205 (line)]] | alt | 6.98 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0793× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 5.84 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.106× (z -8.7) |
| [[LoVo (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 4.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 6.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0512× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 6.45 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.43× (z +8.5) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAX]] | +0.85 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[EID2]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 | STRING 424 |
| [[MRFAP1L1]] | +0.78 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[COIL]] | +0.77 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[PPCS]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[RPP38]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[RDH14]] | +0.74 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[ERCC4]] | +0.73 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPP2]] | -0.63 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.62 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[PMPCA]] | -0.61 | -0.67 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDF1]] | B | KDF1 activity lowers NSMCE3's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.32× higher at baseline in the lines without KDF1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[EID2]] | C | EID2 activity raises NSMCE3's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without EID2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.4, 4.9); signed map (1.5, -19.2). **Vector** length 68.2, 11.4% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +14.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.9 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | +0.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Pentagastrin (drug)]] 5 µM |  | -0.7 | -2.4 |
|  | [[Baicalin (drug)]] 5 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NSE3 component of SMC5/6 complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.1 — chr15:29,264,989-29,269,822 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCA4, MAGEG1, MAGEL3, NSE3; previously NDNL2 |
| Gene groups (HGNC) | SMC5/6 complex; MAGE family |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MG7](https://www.uniprot.org/uniprotkb/Q96MG7) (Non-structural maintenance of chromosomes element 3 homolog):

> Component of the SMC5-SMC6 complex, a complex involved in repair of DNA double-strand breaks by homologous recombination. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of shelterin complex (telosome) components which is proposed to lead to shelterin complex …

**Summary**, from NCBI Gene [56160](https://www.ncbi.nlm.nih.gov/gene/56160):

> The protein encoded by this gene is part of the SMC5-6 chromatin reorganizing complex and is a member of the MAGE superfamily. This is an intronless gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:7677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7677) · Entrez [56160](https://www.ncbi.nlm.nih.gov/gene/56160) · UniProt [Q96MG7](https://www.uniprot.org/uniprotkb/Q96MG7) · Ensembl [ENSG00000185115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185115)

## Data

Gene col 11628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11628); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11628]; `tensor/DDL_lfc|DDL_z.npy` [11628]; `embed/gene_vectors.npy` [11628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11628 or target_col == 11628). Every well: [[NSMCE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMCE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
