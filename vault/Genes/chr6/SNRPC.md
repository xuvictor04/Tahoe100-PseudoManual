---
symbol: "SNRPC"
type: "gene"
col: 4541
ensembl_id: "ENSG00000124562"
name: "small nuclear ribonucleoprotein polypeptide C"
location: "6p21.31"
module: 57
arm: "+"
pooled_cpm: 38.44
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# SNRPC

*small nuclear ribonucleoprotein polypeptide C* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +12.4, q 3e-32, up in 33 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.92× (z +12.1, q 4e-31, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSN]] (+0.68, fdr 1e-05), [[TRUB1]] (+0.64, fdr 1e-05), [[NDUFB7]] (+0.62, fdr 7e-06); moves opposite to [[PEAK1]] (-0.51, fdr 4e-05), [[GABBR1]] (-0.48, fdr 3e-05), [[EIF1B]] (-0.48, fdr 7e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.41×** | +12.4 | 3e-32 | 33/39 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.92×** | +12.1 | 4e-31 | 46/48 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.46×** | +9.7 | 8e-20 | 41/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.89×** | +8.6 | 1e-15 | 31/42 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.80×** | +7.8 | 7e-13 | 33/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.6 | 2e-06 | 30/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.39×** | +4.7 | 2e-04 | 28/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.4 | 8e-04 | 26/48 (SK-MEL-2, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +4.4 | 8e-04 | 29/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +4.3 | 0.001 | 29/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 25/48 (COLO 205, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.31×** | +3.9 | 0.004 | 24/46 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **1.32×** | +3.9 | 0.004 | 25/47 (C-33 A, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.26×** | +3.4 | 0.026 | 16/48 (LoVo, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.26×** | +3.4 | 0.028 | 19/47 (J82, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.029 | 20/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.030 | 17/48 (A-172, A549, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.098 | 14/48 (SW1417, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -3.6 | 0.20 | 16/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.861× | -3.1 | 0.54 | 14/48 (A549, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.36× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 52.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.60× (z +8.5) | — |
| [[KATO III (line)]] | alt | 44.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.72× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 29.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.34× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 37.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.89× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSN]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.64 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[NDUFB7]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[MRPL13]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TIMM21]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TMEM9B]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[PARL]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LONP2]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MIGA1]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MRPS35]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TSFM]] | +0.59 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[SF3A3]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 982 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[GABBR1]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[EIF1B]] | -0.48 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.4, -7.0); signed map (-33.0, -25.9). **Vector** length 68.2, 15.1% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +12.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +3.0 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,757,505-34,773,857 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U1-C, Yhc1 |
| Gene groups (HGNC) | Zinc fingers matrin-type; U1 small nuclear ribonucleoprotein |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P09234](https://www.uniprot.org/uniprotkb/P09234) (U1 small nuclear ribonucleoprotein C):

> Component of the spliceosomal U1 snRNP, which is essential for recognition of the pre-mRNA 5' splice-site and the subsequent assembly of the spliceosome. SNRPC/U1-C is directly involved in initial 5' splice-site recognition for both constitutive and regulated alternative splicing. The interaction with the 5' splice-site seems to precede base-pairing between the pre-mRNA and the U1 snRNA. Stimulates commitment or early (E) complex formation by stabilizing the base pairing of the 5' end of the U1 …

**Summary**, from NCBI Gene [6631](https://www.ncbi.nlm.nih.gov/gene/6631):

> This gene encodes one of the specific protein components of the U1 small nuclear ribonucleoprotein (snRNP) particle required for the formation of the spliceosome. The encoded protein participates in the processing of nuclear precursor messenger RNA splicing. snRNP particles are attacked by autoantibodies frequently produced by patients with connective tissue diseases. The genome contains several pseudogenes of this functional gene. Alternative splicing results in a non-coding transcript …

**Accessions** — [HGNC:11157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11157) · Entrez [6631](https://www.ncbi.nlm.nih.gov/gene/6631) · UniProt [P09234](https://www.uniprot.org/uniprotkb/P09234) · Ensembl [ENSG00000124562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124562)

## Data

Gene col 4541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4541); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4541]; `tensor/DDL_lfc|DDL_z.npy` [4541]; `embed/gene_vectors.npy` [4541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4541 or target_col == 4541). Every well: [[SNRPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
