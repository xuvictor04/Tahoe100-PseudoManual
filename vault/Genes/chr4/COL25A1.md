---
symbol: "COL25A1"
type: "gene"
col: 12018
ensembl_id: "ENSG00000188517"
name: "collagen type XXV alpha 1 chain"
location: "4q25"
module: 150
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 48
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# COL25A1

*collagen type XXV alpha 1 chain* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.76× (z +33.4, q 0e+00, up in 26 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.251×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 0.163×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPSE2]] (+0.74, fdr 7e-06), [[CNTN4]] (+0.73, fdr 7e-06), [[PPFIA2]] (+0.73, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.76×** | +33.4 | 0e+00 | 26/28 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.07×** | +20.6 | 0e+00 | 25/31 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.59×** | +13.3 | 7e-38 | 4/10 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.63×** | +12.9 | 8e-36 | 13/23 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +12.7 | 1e-34 | 28/42 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +11.9 | 7e-31 | 1/5 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +11.6 | 6e-29 | 1/5 (HOP62) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.95×** | +11.2 | 2e-27 | 26/38 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +10.4 | 2e-23 | 15/31 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.0 | 9e-18 | 9/42 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +8.5 | 1e-15 | 18/35 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +7.9 | 1e-13 | 15/36 (HOP62, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +6.9 | 2e-10 | 11/29 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **3.26×** | +6.4 | 5e-09 | 13/35 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.001 | 9/36 (C32, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.006 | 14/40 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.007 | 18/42 (CFPAC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.010 | 12/42 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12018.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.251×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 0.163×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.780× | -3.6 | 0.19 | 10/41 (SK-MEL-2, A498, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.801× | -3.2 | 0.39 | 8/42 (HCT15, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.96 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 10.7× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 4.39 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.4) | [[Selinexor (drug)]] 5 µM 0.163× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 3.36 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 11.3× (z +11.6) | — |
| [[C32 (line)]] | wt | 44.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.68× (z +9.9) | — |
| [[J82 (line)]] | alt | 3.55 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 14.6× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 13.8× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +10.2) | — |
| [[A-427 (line)]] | wt | 1.72 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.6× (z +9.4) | — |
| [[A498 (line)]] | wt | 4.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +10.4) | — |
| [[A549 (line)]] | wt | 1.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +8.5) | — |
| [[LoVo (line)]] | wt | 1.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 1.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.908 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPSE2]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CNTN4]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[PPFIA2]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.70 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[GRID2]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PKP4-AS1]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[FAT3]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL25A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[UNC80]] | B | UNC80 activity raises COL25A1's level | lines that do not express UNC80 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without UNC80 | 0.050 | ⚠ within organs, on part of the lines; also absent: PPFIA2, GAS7, COP1-DT; maybe low, not absent |
| [[LINC00871]] | B | LINC00871 activity raises COL25A1's level | lines that do not express LINC00871 (12) vs lines expressing it (38) | 1.71× lower at baseline in the lines without LINC00871 | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.8, 28.7); signed map (33.2, 15.7). **Vector** length 56.7, 8.07% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +33.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +20.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +9.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXV alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:108,808,725-109,302,752 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Membrane associated collagens with interrupted triple helices |
| Reactome | 6 pathways, smallest: Collagen chain trimerization; Collagen degradation; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXS0](https://www.uniprot.org/uniprotkb/Q9BXS0) (Collagen alpha-1(XXV) chain):

> Inhibits fibrillization of amyloid-beta peptide during the elongation phase. Has also been shown to assemble amyloid fibrils into protease-resistant aggregates. Binds heparin.

**Summary**, from NCBI Gene [84570](https://www.ncbi.nlm.nih.gov/gene/84570):

> This gene encodes a brain-specific membrane associated collagen. A product of proteolytic processing of the encoded protein, CLAC (collagenous Alzheimer amyloid plaque component), binds to amyloid beta-peptides found in Alzheimer amyloid plaques but CLAC inhibits rather than facilitates amyloid fibril elongation (PMID: 16300410). A study of over-expression of this collagen in mice, however, found changes in pathology and behavior suggesting that the encoded protein may promote amyloid plaque …

**Accessions** — [HGNC:18603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18603) · Entrez [84570](https://www.ncbi.nlm.nih.gov/gene/84570) · UniProt [Q9BXS0](https://www.uniprot.org/uniprotkb/Q9BXS0) · Ensembl [ENSG00000188517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188517)

## Data

Gene col 12018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12018); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12018]; `tensor/DDL_lfc|DDL_z.npy` [12018]; `embed/gene_vectors.npy` [12018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12018 or target_col == 12018). Every well: [[COL25A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL25A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
