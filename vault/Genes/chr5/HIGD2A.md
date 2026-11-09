---
symbol: "HIGD2A"
type: "gene"
col: 7058
ensembl_id: "ENSG00000146066"
name: "HIG1 hypoxia inducible domain family member 2A"
location: "5q35.2"
module: 48
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# HIGD2A

*HIG1 hypoxia inducible domain family member 2A* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.44× (z +8.3, q 6e-14, up in 35 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +7.0, q 9e-10, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.402× (z -8.7, q 2e-15, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.250×, HT-29 0.173×, HEC-1-A 0.216×, NCI-H2030 0.279×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSR4]] (+0.73, fdr 7e-06), [[MIR4458HG]] (+0.73, fdr 7e-06), [[ALKBH7]] (+0.72, fdr 7e-06); moves opposite to [[CSRP1]] (-0.69, fdr 7e-06), [[GTF2H3]] (-0.67, fdr 7e-06), [[GTF2A1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +8.3 | 6e-14 | 35/36 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.0 | 9e-10 | 37/45 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +5.7 | 2e-06 | 21/23 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +5.3 | 2e-05 | 36/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.97×** | +4.5 | 6e-04 | 33/46 (LoVo, NCI-H2030, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +4.0 | 0.006 | 20/27 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.78×** | +3.9 | 0.010 | 24/41 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.66×** | +3.3 | 0.081 | 18/39 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.36× | +3.1 | 0.14 | 14/44 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7058.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.250×, HT-29 0.173×, HEC-1-A 0.216×, NCI-H2030 0.279×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.402×** | -8.7 | 2e-15 | 37/47 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.518×** | -4.4 | 0.002 | 32/45 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.618× | -3.3 | 0.22 | 23/47 (COLO 205, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.629× | -3.1 | 0.25 | 20/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.626× | -3.0 | 0.27 | 21/46 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.3) |
| [[HT-29 (line)]] | alt | 9.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.7) |
| [[A-172 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSR4]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.72 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[NENF]] | +0.72 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[COPS9]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.72 | +0.58 / +0.80 | both halves | 7e-06 |  |
| [[UBL5]] | +0.72 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[APOC1]] | +0.71 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.71 | +0.33 / +0.79 | both halves | 1e-04 |  |
| [[OST4]] | +0.71 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[MIF]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[COX7C]] | +0.70 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP1]] | -0.69 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[GTF2H3]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[GTF2A1]] | -0.64 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[ZFP41]] | -0.64 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[DDX1]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[BMS1]] | -0.63 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[GMFB]] | -0.62 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.61 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-44.2, -22.1); signed map (-33.3, 10.5). **Vector** length 60.7, 14.0% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.54 to 24); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.53 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.59 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.9 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | HIG1 hypoxia inducible domain family member 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,388,751-176,389,761 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2198, RCF1B |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW72](https://www.uniprot.org/uniprotkb/Q9BW72) (HIG1 domain family member 2A, mitochondrial):

> Proposed subunit of cytochrome c oxidase (COX, complex IV), which is the terminal component of the mitochondrial respiratory chain that catalyzes the reduction of oxygen to water. May be involved in cytochrome c oxidase activity. May play a role in the assembly of respiratory supercomplexes.

**Summary**, from NCBI Gene [192286](https://www.ncbi.nlm.nih.gov/gene/192286):

> The protein encoded by this gene is a subunit of the cytochrome c oxidase complex (complex IV), which is the terminal enzyme in the mitochondrial respiratory chain. The encoded protein is an inner mitochondrial membrane protein and is a functional ortholog of the yeast respiratory supercomplex factor 1 (Rcf1). In mouse, the orthologous protein enhances cell survival under conditions of hypoxia. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:28311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28311) · Entrez [192286](https://www.ncbi.nlm.nih.gov/gene/192286) · UniProt [Q9BW72](https://www.uniprot.org/uniprotkb/Q9BW72) · Ensembl [ENSG00000146066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146066)

## Data

Gene col 7058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7058); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7058]; `tensor/DDL_lfc|DDL_z.npy` [7058]; `embed/gene_vectors.npy` [7058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7058 or target_col == 7058). Every well: [[HIGD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIGD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
