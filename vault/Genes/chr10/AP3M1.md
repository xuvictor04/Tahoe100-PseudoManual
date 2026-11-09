---
symbol: "AP3M1"
type: "gene"
col: 11607
ensembl_id: "ENSG00000185009"
name: "adaptor related protein complex 3 subunit mu 1"
location: "10q22.2"
module: 25
arm: "+"
pooled_cpm: 34.72
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AP3M1

*adaptor related protein complex 3 subunit mu 1* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.29× (z +13.3, q 9e-38, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HCT15 0.117×, SK-MEL-2 0.161×, NCI-H23 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SHP-77 0.208×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.462×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[API5]] (+0.77, fdr 7e-06), [[GPN1]] (+0.75, fdr 7e-06), [[USP5]] (+0.70, fdr 7e-06); moves opposite to [[IRX5]] (-0.59, fdr 3e-05), [[INAFM1]] (-0.59, fdr 7e-06), [[ACAP1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.29×** | +13.3 | 9e-38 | 41/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +10.7 | 2e-24 | 41/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +10.3 | 1e-22 | 44/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.8 | 2e-20 | 29/38 (HCT15, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +9.3 | 2e-18 | 37/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.5 | 6e-12 | 28/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.38×** | +6.9 | 5e-10 | 25/45 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +6.4 | 1e-08 | 24/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +6.1 | 6e-08 | 30/48 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +6.0 | 1e-07 | 27/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 1e-06 | 24/48 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +4.9 | 4e-05 | 22/48 (LoVo, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 22/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.15× | +4.0 | 0.002 | 15/48 (A-427, A498, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.22×** | +3.8 | 0.005 | 20/44 (C32, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.006 | 19/48 (NCI-H2030, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11607.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HCT15 0.117×, SK-MEL-2 0.161×, NCI-H23 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SHP-77 0.208×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.462×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.2 | 0.014 | 14/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.842× | -3.7 | 0.053 | 19/48 (RPMI-7951, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 55.4 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.66× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 40.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.58× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.318× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~68% of this change |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 41.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.18× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[RKO (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.208× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[API5]] | +0.77 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[GPN1]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[USP5]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GFM2]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[STX16]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.65 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[PSMB2]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DLD]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[RPE]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[OPA1]] | +0.63 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[UGGT1]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PPT1]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRX5]] | -0.59 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.59 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.59 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[PIM3]] | -0.58 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[NBPF14]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.57 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[NBPF10]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.55 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.55 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[EFNA2]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[SNHG9]] | -0.55 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[CCNP]] | -0.54 | -0.46 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.8, -13.3); signed map (-29.3, -29.1). **Vector** length 88.1, 17.6% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +10.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.1 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit mu 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:74,120,255-74,150,842 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adaptor related protein complex 3 |
| Reactome | 3 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2T2](https://www.uniprot.org/uniprotkb/Q9Y2T2) (AP-3 complex subunit mu-1):

> Part of the AP-3 complex, an adaptor-related complex which is not clathrin-associated. The complex is associated with the Golgi region as well as more peripheral structures. It facilitates the budding of vesicles from the Golgi membrane and may be directly involved in trafficking to lysosomes. In concert with the BLOC-1 complex, AP-3 is required to target cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals.

**Summary**, from NCBI Gene [26985](https://www.ncbi.nlm.nih.gov/gene/26985):

> The protein encoded by this gene is the medium subunit of AP-3, which is an adaptor-related protein complex associated with the Golgi region as well as more peripheral intracellular structures. AP-3 facilitates the budding of vesicles from the Golgi membrane, and it may directly function in protein sorting to the endosomal/lysosomal system. AP-3 is a heterotetrameric protein complex composed of two large subunits (delta and beta3), a medium subunit (mu3), and a small subunit (sigma 3). …

**Accessions** — [HGNC:569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:569) · Entrez [26985](https://www.ncbi.nlm.nih.gov/gene/26985) · UniProt [Q9Y2T2](https://www.uniprot.org/uniprotkb/Q9Y2T2) · Ensembl [ENSG00000185009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185009)

## Data

Gene col 11607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11607); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11607]; `tensor/DDL_lfc|DDL_z.npy` [11607]; `embed/gene_vectors.npy` [11607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11607 or target_col == 11607). Every well: [[AP3M1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3M1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
