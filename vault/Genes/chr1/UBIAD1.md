---
symbol: "UBIAD1"
type: "gene"
col: 4240
ensembl_id: "ENSG00000120942"
name: "UbiA prenyltransferase domain containing 1"
location: "1p36.22"
module: 5
arm: "+"
pooled_cpm: 13.23
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# UBIAD1

*UbiA prenyltransferase domain containing 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.51× (z +6.2, q 3e-07, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.597× (z -7.8, q 3e-12, down in 24 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.714× (z -7.2, q 1e-10, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS1]] (+0.66, fdr 7e-06), [[WDR4]] (+0.66, fdr 7e-06), [[ZNF202]] (+0.64, fdr 7e-06); moves opposite to [[KMT2C]] (-0.59, fdr 1e-05), [[CLU]] (-0.57, fdr 3e-05), [[GRHL1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 3e-07 | 24/47 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.007 | 16/46 (KATO III, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.1 | 0.008 | 17/44 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.036 | 14/46 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.25× | +3.3 | 0.11 | 8/47 (KATO III, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.20 | 9/47 (NCI-H1573, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.597×** | -7.8 | 3e-12 | 24/38 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -7.2 | 1e-10 | 31/48 (SW480, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -6.2 | 1e-07 | 21/47 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.686×** | -5.7 | 2e-06 | 23/46 (KATO III, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -5.5 | 5e-06 | 15/23 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -4.7 | 2e-04 | 19/47 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **0.606×** | -4.0 | 0.006 | 14/44 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.027 | 14/45 (SW48, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.8 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -13.2) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A498 (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.318× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 48.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.178× (z -9.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.38 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -9.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.106× (z -8.6) |
| [[H4 (line)]] | wt | 12.2 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0992× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.22 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0917× (z -10.8) |
| [[J82 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 9.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0517× (z -10.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 8.72 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.210× (z -9.2) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0832× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.71 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0784× (z -9.8) |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[WDR4]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[URB2]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TRNT1]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TWNK]] | +0.61 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ARMC6]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ZNF696]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.60 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[PYCR3]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NOP16]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MECR]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2C]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CLU]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GRHL1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MAPRE2]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[UBR2]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UBIAD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UBIAD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.8, -34.7); signed map (-1.5, -47.8). **Vector** length 71.9, 12.0% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.4 | +6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | UbiA prenyltransferase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,273,198-11,296,049 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TERE1; previously SCCD |
| Reactome | 3 pathways, smallest: Metabolism of vitamin K; Metabolism of fat-soluble vitamins; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Z9](https://www.uniprot.org/uniprotkb/Q9Y5Z9) (UbiA prenyltransferase domain-containing protein 1):

> Prenyltransferase that mediates the formation of menaquinone-4 (MK-4) and coenzyme Q10. MK-4 is a vitamin K2 isoform present at high concentrations in the brain, kidney and pancreas, and is required for endothelial cell development. Mediates the conversion of phylloquinone (PK) into MK-4, probably by cleaving the side chain of phylloquinone (PK) to release 2-methyl-1,4-naphthoquinone (menadione; K3) and then prenylating it with geranylgeranyl pyrophosphate (GGPP) to form MK-4. Also plays a role …

**Summary**, from NCBI Gene [29914](https://www.ncbi.nlm.nih.gov/gene/29914):

> This gene encodes a protein thought to be involved in cholesterol and phospholipid metabolism. Mutations in this gene are associated with Schnyder crystalline corneal dystrophy. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:30791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30791) · Entrez [29914](https://www.ncbi.nlm.nih.gov/gene/29914) · UniProt [Q9Y5Z9](https://www.uniprot.org/uniprotkb/Q9Y5Z9) · Ensembl [ENSG00000120942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120942)

## Data

Gene col 4240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4240); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4240]; `tensor/DDL_lfc|DDL_z.npy` [4240]; `embed/gene_vectors.npy` [4240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4240 or target_col == 4240). Every well: [[UBIAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBIAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
