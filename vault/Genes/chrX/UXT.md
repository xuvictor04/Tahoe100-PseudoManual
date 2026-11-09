---
symbol: "UXT"
type: "gene"
col: 4758
ensembl_id: "ENSG00000126756"
name: "ubiquitously expressed prefoldin like chaperone"
location: "Xp11.23"
module: 24
arm: "+"
pooled_cpm: 25.83
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# UXT

*ubiquitously expressed prefoldin like chaperone* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.21× (z +7.5, q 3e-11, up in 36 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 3.91×, PANC-1 3.13×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.661× (z -5.6, q 1e-05, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS39-DT]] (+0.71, fdr 1e-05), [[OMG]] (+0.70, fdr 7e-06), [[HIGD2A]] (+0.70, fdr 1e-05); moves opposite to [[SSX2IP]] (-0.63, fdr 8e-06), [[FAM199X]] (-0.59, fdr 2e-05), [[DNAJC10]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4758.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 3.91×, PANC-1 3.13×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.5 | 3e-11 | 36/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.0 | 8e-10 | 26/33 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +4.6 | 9e-04 | 24/36 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.46×** | +3.6 | 0.044 | 24/46 (NCI-H460, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -5.6 | 1e-05 | 32/47 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -4.9 | 2e-04 | 34/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.637×** | -4.3 | 0.003 | 31/48 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.456×** | -3.9 | 0.013 | 34/48 (CHP-212, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.722× | -3.1 | 0.21 | 17/48 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.710× | -3.0 | 0.21 | 16/47 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.800× | -3.0 | 0.21 | 17/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.1) |
| [[A-172 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 16 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39-DT]] | +0.71 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[OMG]] | +0.70 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[HIGD2A]] | +0.70 | +0.52 / +0.73 | both halves | 1e-05 | STRING 459 |
| [[IGBP1]] | +0.69 | +0.48 / +0.79 | both halves | 2e-05 |  |
| [[ECSIT]] | +0.68 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CEP164P1]] | +0.68 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SMIM27]] | +0.67 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[NDUFB11]] ⚠ | +0.67 | +0.57 / +0.66 | both halves | 1e-05 | STRING 433; ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[NDUFA13]] ⚠ | +0.66 | +0.55 / +0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | +0.65 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[BIRC6-AS2-1]] | +0.65 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[APOC1]] | +0.64 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.63 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[FAM199X]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[DNAJC10]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[LMNB2]] | -0.59 | -0.39 / -0.67 | both halves | 5e-05 |  |
| [[PRELID3B]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ALG10B]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PHF6]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 | STRING 606 |
| [[FH]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[OCRL]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TMEM237]] | -0.55 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[DBN1]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UXT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.6, -22.1); signed map (-6.6, -6.5). **Vector** length 49.2, 10.0% of its response variance represented; |z| ≥ 3 in 440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +2.8 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | +0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitously expressed prefoldin like chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:47,651,796-47,659,180 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ART-27, STAP1, SKP2 |
| Gene groups (HGNC) | Prefoldin subunits; Prefoldin-like complex |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 1 pathways, smallest: Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBK9](https://www.uniprot.org/uniprotkb/Q9UBK9) (Protein UXT):

> Involved in gene transcription regulation. Acts in concert with the corepressor URI1 to regulate androgen receptor AR-mediated transcription. Together with URI1, associates with chromatin to the NKX3-1 promoter region. Negatively regulates the transcriptional activity of the estrogen receptor ESR1 by inducing its translocation into the cytoplasm. May act as nuclear chaperone that facilitates the formation of the NF-kappa-B enhanceosome and thus positively regulates NF-kappa-B transcription …

**Summary**, from NCBI Gene [8409](https://www.ncbi.nlm.nih.gov/gene/8409):

> The protein encoded by this gene functions as a cofactor that modulates androgen receptor-dependent transcription, and also plays a critical role in tumor necrosis factor-induced apoptosis. Expression of this gene may play a role in tumorigenesis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:12641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12641) · Entrez [8409](https://www.ncbi.nlm.nih.gov/gene/8409) · UniProt [Q9UBK9](https://www.uniprot.org/uniprotkb/Q9UBK9) · Ensembl [ENSG00000126756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126756)

## Data

Gene col 4758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4758); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4758]; `tensor/DDL_lfc|DDL_z.npy` [4758]; `embed/gene_vectors.npy` [4758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4758 or target_col == 4758). Every well: [[UXT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UXT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
