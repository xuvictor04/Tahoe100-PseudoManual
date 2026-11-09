---
symbol: "SKIC2"
type: "gene"
col: 12856
ensembl_id: "ENSG00000204351"
name: "SKI2 subunit of superkiller complex"
location: "6p21.33"
module: 2
arm: "+"
pooled_cpm: 15.22
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SKIC2

*SKI2 subunit of superkiller complex* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.15× (z +16.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.726× (z -4.5, q 0.004, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGCX]] (+0.70, fdr 7e-06), [[TCIRG1]] (+0.67, fdr 1e-05), [[OSBPL7]] (+0.66, fdr 1e-05); moves opposite to [[MED13]] (-0.58, fdr 4e-05), [[CCDC122]] (-0.55, fdr 6e-05), [[ST7L]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.15×** | +16.8 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.54×** | +13.6 | 9e-40 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +9.6 | 2e-19 | 37/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.69×** | +7.5 | 6e-12 | 33/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +5.3 | 1e-05 | 23/45 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.6 | 3e-04 | 11/27 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.5 | 6e-04 | 20/47 (SNU-1, C-33 A, …) | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.1 | 0.003 | 11/32 (J82, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.7 | 0.015 | 16/48 (SK-MEL-2, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.083 | 14/45 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -4.5 | 0.004 | 20/47 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -4.4 | 0.004 | 18/46 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -4.0 | 0.011 | 21/46 (H4, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.765×** | -3.9 | 0.015 | 11/47 (AN3 CA, RPMI-7951, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.773×** | -3.7 | 0.021 | 15/47 (NCI-H2347, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.056 | 10/47 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.851× | -3.3 | 0.083 | 17/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.799× | -3.1 | 0.12 | 12/47 (A498, A549, …) | rises with dose | position effect removed |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 0.812× | -3.0 | 0.16 | 15/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.02× (z +13.8) | — |
| [[H4 (line)]] | wt | 22.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0686× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 10.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.99× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.105× (z -9.1) |
| [[J82 (line)]] | alt | 28.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +8.7) | — |
| [[KATO III (line)]] | alt | 16.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +9.1) | — |
| [[LoVo (line)]] | wt | 10.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 17.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.24× (z +9.0) | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.107× (z -8.6) |
| [[A-172 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGCX]] | +0.70 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TCIRG1]] | +0.67 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PLPPR2]] | +0.63 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ESS2]] | +0.63 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[MATCAP1]] | +0.63 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[APBB3]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ABHD17A]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FCHSD1]] | +0.61 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[STEEP1]] | +0.61 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[INTS11]] | +0.60 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[BAP1]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13]] | -0.58 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CCDC122]] | -0.55 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ST7L]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[CPSF2]] | -0.53 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[GABPB1]] | -0.52 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[HACD1]] | -0.52 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[KDSR]] | -0.52 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[UEVLD]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[UBXN2A]] | -0.50 | -0.50 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SKIC2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SMARCD3]] | C | SMARCD3 activity raises SKIC2's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.33× lower at baseline in the lines without SMARCD3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (5.9, -5.1); signed map (-30.7, 0.2). **Vector** length 91.0, 18.5% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +16.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +13.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +9.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.7 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | SKI2 subunit of superkiller complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,959,116-31,969,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HLP, DDX13, SKI2W, 170A, SKIV2L1, SKI2; previously SKIV2, SKIV2L |
| Gene groups (HGNC) | Ski2 like RNA helicases; SKI complex subunits |
| Reactome | 6 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Association of TriC/CCT with target proteins during biosynthesis; Deadenylation-dependent mRNA decay |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15477](https://www.uniprot.org/uniprotkb/Q15477) (Superkiller complex protein 2):

> Helicase component of the SKI complex, a multiprotein complex that assists the RNA-degrading exosome during the mRNA decay and quality-control pathways. The SKI complex catalyzes mRNA extraction from 80S ribosomal complexes in the 3'-5' direction and channels mRNA to the cytosolic exosome for degradation. SKI-mediated extraction of mRNA from stalled ribosomes allow binding of the Pelota-HBS1L complex and subsequent ribosome disassembly by ABCE1 for ribosome recycling. In the nucleus, the SKI …

**Summary**, from NCBI Gene [6499](https://www.ncbi.nlm.nih.gov/gene/6499):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:10898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10898) · Entrez [6499](https://www.ncbi.nlm.nih.gov/gene/6499) · UniProt [Q15477](https://www.uniprot.org/uniprotkb/Q15477) · Ensembl [ENSG00000204351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204351)

## Data

Gene col 12856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12856); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12856]; `tensor/DDL_lfc|DDL_z.npy` [12856]; `embed/gene_vectors.npy` [12856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12856 or target_col == 12856). Every well: [[SKIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
