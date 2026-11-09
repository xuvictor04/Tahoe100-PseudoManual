---
symbol: "ACOT13"
type: "gene"
col: 3352
ensembl_id: "ENSG00000112304"
name: "acyl-CoA thioesterase 13"
location: "6p22.3"
module: 64
arm: "+"
pooled_cpm: 24.75
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# ACOT13

*acyl-CoA thioesterase 13* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +9.0, q 2e-16, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.65× (z +5.5, q 6e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.497× (z -7.7, q 7e-12, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD4]] (+0.67, fdr 1e-05), [[USP47]] (+0.65, fdr 1e-05), [[TBCA]] (+0.62, fdr 7e-06); moves opposite to [[SPATA33]] (-0.55, fdr 3e-05), [[PMPCA]] (-0.50, fdr 1e-05), [[ZNF749]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FER]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.0 | 2e-16 | 41/44 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +7.8 | 1e-12 | 28/35 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +5.5 | 6e-06 | 31/48 (HOP62, HT-29, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +5.3 | 1e-05 | 33/48 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.002 | 28/47 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.49×** | +4.1 | 0.004 | 24/40 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.23× | +3.2 | 0.12 | 21/47 (HOP62, LoVo, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | 1.33× | +3.1 | 0.12 | 21/45 (AsPC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.32× | +3.1 | 0.12 | 19/47 (COLO 205, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -7.7 | 7e-12 | 42/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -6.6 | 1e-08 | 35/48 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -5.8 | 1e-06 | 26/47 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.633×** | -5.0 | 7e-05 | 33/47 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.548×** | -3.5 | 0.060 | 22/48 (SNU-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -3.4 | 0.071 | 21/47 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 12.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0565× (z -8.6) |
| [[HOP62 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD4]] | +0.67 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[USP47]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TBCA]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MRPL45]] | +0.61 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.58 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[CAPS2]] | +0.55 | +0.75 / +0.40 | both halves | 5e-05 |  |
| [[PFDN4]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DCTN6]] | +0.54 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[NEK1]] | +0.53 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[STYXL1]] | +0.53 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[UBC]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[HSPB1]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA33]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.50 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZNF749]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CDCA7]] | -0.50 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[RFT1]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[DSCC1]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SLC41A3]] | -0.48 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[CDK2]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[CDCA4]] | -0.48 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ZNF530]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[UBE2G2]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RFC4]] | -0.46 | -0.57 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ACOT13's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER]] | C | ACOT13's natural level strengthens FER's drug response | ACOT13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.07; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-20.9, 9.5); signed map (6.9, -30.5). **Vector** length 68.5, 14.5% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.0 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -5.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.0 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,667,035-24,705,065 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT012; previously THEM2 |
| Gene groups (HGNC) | Acyl-CoA thioesterases; Thioester hydrolases |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPJ3](https://www.uniprot.org/uniprotkb/Q9NPJ3) (Acyl-coenzyme A thioesterase 13):

> Catalyzes the hydrolysis of acyl-CoAs into free fatty acids and coenzyme A (CoASH), regulating their respective intracellular levels. Has acyl-CoA thioesterase activity towards medium (C12) and long-chain (C18) fatty acyl-CoA substrates (By similarity). Can also hydrolyze 3-hydroxyphenylacetyl-CoA and 3,4-dihydroxyphenylacetyl-CoA (in vitro) (By similarity). May play a role in controlling adaptive thermogenesis (By similarity).

**Summary**, from NCBI Gene [55856](https://www.ncbi.nlm.nih.gov/gene/55856):

> This gene encodes a member of the thioesterase superfamily. In humans, the protein co-localizes with microtubules and is essential for sustained cell proliferation. The orthologous mouse protein forms a homotetramer and is associated with mitochondria. The mouse protein functions as a medium- and long-chain acyl-CoA thioesterase. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, May 2009]

**Accessions** — [HGNC:20999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20999) · Entrez [55856](https://www.ncbi.nlm.nih.gov/gene/55856) · UniProt [Q9NPJ3](https://www.uniprot.org/uniprotkb/Q9NPJ3) · Ensembl [ENSG00000112304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112304)

## Data

Gene col 3352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3352); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3352]; `tensor/DDL_lfc|DDL_z.npy` [3352]; `embed/gene_vectors.npy` [3352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3352 or target_col == 3352). Every well: [[ACOT13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
