---
symbol: "ENTPD1"
type: "gene"
col: 6141
ensembl_id: "ENSG00000138185"
name: "ectonucleoside triphosphate diphosphohydrolase 1"
location: "10q24.1"
module: 90
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# ENTPD1

*ectonucleoside triphosphate diphosphohydrolase 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.67× (z +22.5, q 0e+00, up in 21 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0876×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW480 0.0837×); [[Ritonavir (drug)]] 5 µM in 1 line (NCI-H23 0.0845×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.69, fdr 1e-05), [[MYT1L]] (+0.68, fdr 7e-06), [[SLC26A5]] (+0.68, fdr 1e-05).
> It is in [[Module 090]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.67×** | +22.5 | 0e+00 | 21/23 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +12.3 | 4e-32 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +9.5 | 3e-19 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +8.9 | 7e-17 | 3/7 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +8.7 | 4e-16 | 23/39 (SW1417, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +6.2 | 4e-08 | 13/30 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +6.0 | 2e-07 | 17/43 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +5.8 | 4e-07 | 1/9 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +4.5 | 4e-04 | 10/37 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.58×** | +4.2 | 0.001 | 7/40 (PANC-1, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.001 | 4/21 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.59×** | +4.1 | 0.002 | 1/9 (A-172) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +4.0 | 0.002 | 2/41 (LoVo, SK-MEL-2) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +3.9 | 0.003 | 4/15 (NCI-H460, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.51×** | +3.8 | 0.006 | 7/42 (PANC-1, A-427, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.031 | 6/39 (A549, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.037 | 5/40 (HEC-1-A, A-172, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.037 | 1/27 (A549) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.037 | 1/13 (SHP-77) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.037 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Berbamine (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.082 | 7/43 (A549, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0876×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW480 0.0837×); [[Ritonavir (drug)]] 5 µM in 1 line (NCI-H23 0.0845×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.696× | -3.2 | 0.75 | 7/34 (A498, PANC-1, …) | top dose only | composition shift |
| [[Pimozide (drug)]] 5 µM |  | 0.721× | -3.0 | 0.75 | 6/41 (HOP62, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 1.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 1.74 | 0 | 1 | — | [[Ritonavir (drug)]] 5 µM 0.0845× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0876× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 1.84 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0837× (z -9.0) |
| [[A-172 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.903 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.700 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.909 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.832 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.69 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[MYT1L]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[SLC26A5]] | +0.68 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[LINC00578]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[GLRA3]] | +0.68 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.67 | +0.45 / +0.78 | both halves | 3e-05 |  |
| [[SORCS1]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[LINC02208]] | +0.67 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[LINC00861]] | +0.66 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ADAMTS19]] | +0.65 | +0.47 / +0.65 | both halves | 2e-05 | **novel candidate** |
| [[CLVS1]] | +0.64 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[SLC35F4]] | +0.64 | +0.42 / +0.71 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.1, 30.2); signed map (34.3, 16.0). **Vector** length 38.0, 4.25% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +22.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleoside triphosphate diphosphohydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:95,711,779-95,877,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATP-DPH, NTPDase-1, ATPDase, SPG64; previously CD39 |
| Gene groups (HGNC) | CD molecules; Ectonucleoside triphosphate diphosphohydrolase family |
| Reactome | 7 pathways, smallest: Phosphate bond hydrolysis by NTPDase proteins; Cell recruitment (pro-inflammatory response); Purinergic signaling in leishmaniasis infection |
| Matched by | ensembl_id |

**Function**, from UniProt [P49961](https://www.uniprot.org/uniprotkb/P49961) (Ectonucleoside triphosphate diphosphohydrolase 1):

> Catalyzes the hydrolysis of nucleoside triphosphates (NTPs) and diphosphates (NDPs) (Probable). The enzyme sequentially removes phosphate groups in two successive steps, converting NTPs to nucleoside monophosphates (NMPs) via NDP intermediates (Probable). This activity contributes to the regulation of extracellular levels of nucleotides (Probable). By hydrolyzing pro-inflammatory ATP and platelet-activating ADP to AMP, it blocks platelet aggregation and supports blood flow.

**Summary**, from NCBI Gene [953](https://www.ncbi.nlm.nih.gov/gene/953):

> The protein encoded by this gene is a plasma membrane protein that hydrolyzes extracellular ATP and ADP to AMP. Inhibition of this protein's activity may confer anticancer benefits. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:3363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3363) · Entrez [953](https://www.ncbi.nlm.nih.gov/gene/953) · UniProt [P49961](https://www.uniprot.org/uniprotkb/P49961) · Ensembl [ENSG00000138185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138185)

## Data

Gene col 6141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6141); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6141]; `tensor/DDL_lfc|DDL_z.npy` [6141]; `embed/gene_vectors.npy` [6141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6141 or target_col == 6141). Every well: [[ENTPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
