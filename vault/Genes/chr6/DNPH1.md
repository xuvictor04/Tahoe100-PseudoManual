---
symbol: "DNPH1"
type: "gene"
col: 3392
ensembl_id: "ENSG00000112667"
name: "2'-deoxynucleoside 5'-phosphate N-hydrolase 1"
location: "6p21.1"
module: 4
arm: "+"
pooled_cpm: 12.0
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DNPH1

*2'-deoxynucleoside 5'-phosphate N-hydrolase 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.27× (z +8.2, q 2e-13, up in 30 of 33 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -5.1, q 2e-04, down in 30 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.166×, A-427 0.236×, SW480 0.211×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.186×).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL12]] (+0.63, fdr 2e-05), [[DMAC1]] (+0.63, fdr 6e-05), [[ATP5MC1]] (+0.62, fdr 1e-05); moves opposite to [[TMCO3]] (-0.48, fdr 3e-05), [[TLN1]] (-0.47, fdr 4e-04), [[HAPSTR1]] (-0.45, fdr 1e-03, ⚠ one half only (not replicated)), [[GOLGA3]] (-0.44, fdr 6e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADRA2C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.27×** | +8.2 | 2e-13 | 30/33 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.93×** | +7.4 | 5e-11 | 18/19 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +6.2 | 1e-07 | 25/27 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.1 | 0.007 | 24/38 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **2.00×** | +3.9 | 0.012 | 21/36 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3392.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.166×, A-427 0.236×, SW480 0.211×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.528×** | -5.1 | 2e-04 | 30/44 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.485×** | -4.1 | 0.013 | 28/46 (SW48, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.282× | -3.4 | 0.14 | 29/45 (KATO III, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | 0.561× | -3.3 | 0.16 | 25/46 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.577× | -3.1 | 0.17 | 19/42 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.560× | -3.1 | 0.17 | 26/44 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.316× | -3.1 | 0.17 | 19/47 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.4) |
| [[KATO III (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.0) |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -8.9) |
| [[SW480 (line)]] | alt | 9.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -8.8) |
| [[A-172 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 17 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL12]] | +0.63 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[DMAC1]] | +0.63 | +0.39 / +0.73 | both halves | 6e-05 |  |
| [[ATP5MC1]] | +0.62 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[TIMM13]] | +0.61 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[NDUFAF8]] | +0.59 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[MFSD3]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[CISD3]] | +0.57 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[MRPL57]] | +0.57 | +0.18 / +0.75 | ⚠ one half (not replicated) | 9e-04 |  |
| [[UQCC2]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MRPL24]] | +0.55 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[AGMAT]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ARL2]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SNRPF]] | +0.54 | +0.46 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCO3]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TLN1]] | -0.47 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[HAPSTR1]] | -0.45 | -0.18 / -0.59 | ⚠ one half (not replicated) | 1e-03 |  |
| [[GOLGA3]] | -0.44 | -0.22 / -0.49 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA2C]] | B | ADRA2C activity raises DNPH1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without ADRA2C | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[NME3]] | B | NME3 activity lowers DNPH1's level | lines that do not express NME3 (5) vs lines expressing it (45) | 1.24× higher at baseline in the lines without NME3 | 0.066 | ⚠ within organs, on part of the lines; also absent: TACC2 |
| [[HSD11B2]] | B | HSD11B2 activity raises DNPH1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.41× lower at baseline in the lines without HSD11B2 | 0.098 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.206). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-50.3, -16.1); signed map (-38.0, -26.5). **Vector** length 50.6, 11.3% of its response variance represented; |z| ≥ 3 in 551 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.0 | +2.3 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | 2'-deoxynucleoside 5'-phosphate N-hydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,225,629-43,229,481 (-) |
| Ensembl biotype | protein_coding |
| Also known as | rcl, dJ330M21.3; previously C6orf108 |
| Reactome | 3 pathways, smallest: Purine catabolism; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [O43598](https://www.uniprot.org/uniprotkb/O43598) (5-hydroxymethyl-dUMP N-hydrolase):

> Part of a nucleotide salvage pathway that eliminates epigenetically modified 5-hydroxymethyl-dCMP (hmdCMP) in a two-step process entailing deamination to cytotoxic 5-hydroxymethyl-dUMP (hmdUMP), followed by its hydrolysis into 5-hydroxymethyluracil (hmU) and 2-deoxy-D-ribose 5-phosphate (deoxyribosephosphate). Catalyzes the second step in that pathway, the hydrolysis of the N-glycosidic bond in hmdUMP, degrading this cytotoxic nucleotide to avoid its genomic integration.

**Summary**, from NCBI Gene [10591](https://www.ncbi.nlm.nih.gov/gene/10591):

> This gene was identified on the basis of its stimulation by c-Myc protein. The latter is a transcription factor that participates in the regulation of cell proliferation, differentiation, and apoptosis. The exact function of this gene is not known but studies in rat suggest a role in cellular proliferation and c-Myc-mediated transformation. Two alternative transcripts encoding different proteins have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21218) · Entrez [10591](https://www.ncbi.nlm.nih.gov/gene/10591) · UniProt [O43598](https://www.uniprot.org/uniprotkb/O43598) · Ensembl [ENSG00000112667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112667)

## Data

Gene col 3392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3392); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3392]; `tensor/DDL_lfc|DDL_z.npy` [3392]; `embed/gene_vectors.npy` [3392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3392 or target_col == 3392). Every well: [[DNPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
