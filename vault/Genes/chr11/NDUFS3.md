---
symbol: "NDUFS3"
type: "gene"
col: 13118
ensembl_id: "ENSG00000213619"
name: "NADH:ubiquinone oxidoreductase core subunit S3"
location: "11p11.2"
module: 118
arm: "+"
pooled_cpm: 17.85
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# NDUFS3

*NADH:ubiquinone oxidoreductase core subunit S3* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +6.2, q 1e-07, up in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.775× (z -3.8, q 0.074, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 0.223×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNPY2]] (+0.69, fdr 1e-05), [[NGDN]] (+0.65, fdr 1e-05), [[MED4]] (+0.65, fdr 1e-05); moves opposite to [[DIAPH1]] (-0.61, fdr 1e-05), [[SPAG9]] (-0.56, fdr 1e-05), [[ADAMTSL5]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.2 | 1e-07 | 34/47 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +6.2 | 1e-07 | 31/43 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.62×** | +5.1 | 5e-05 | 25/41 (NCI-H460, LS 180, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.57×** | +4.8 | 2e-04 | 25/43 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.45×** | +3.6 | 0.030 | 17/35 (A549, LoVo, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.037 | 21/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.3 | 0.072 | 18/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +3.2 | 0.088 | 20/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.36× | +3.1 | 0.11 | 13/46 (KATO III, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 0.223×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -3.8 | 0.074 | 22/48 (BT-474, NCI-H2347, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.723× | -3.4 | 0.17 | 20/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[A-427 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNPY2]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[NGDN]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MED4]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[RPRD2]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TMEM101]] | +0.63 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[PPIE]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FBXL15]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[SCNM1]] | +0.62 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[PEX11B]] | +0.62 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[ITGAE]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[RAF1]] | +0.60 | +0.29 / +0.56 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[SPAG9]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | -0.54 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[MYH9]] | -0.53 | -0.27 / -0.62 | both halves | 3e-04 |  |
| [[YWHAZ]] | -0.53 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[CALM2]] | -0.52 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[CORO1C]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SEPTIN10]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ITGB1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 | pathway: RHOG GTPase cycle |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-52.3, 4.4); signed map (-5.5, -3.9). **Vector** length 57.9, 11.0% of its response variance represented; |z| ≥ 3 in 517 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit S3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,565,336-47,584,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-30 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: Complex I biogenesis; RHOG GTPase cycle; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75489](https://www.uniprot.org/uniprotkb/O75489) (NADH dehydrogenase):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity and assembly of complex I.

**Summary**, from NCBI Gene [4722](https://www.ncbi.nlm.nih.gov/gene/4722):

> This gene encodes one of the iron-sulfur protein (IP) components of mitochondrial NADH:ubiquinone oxidoreductase (complex I). Mutations in this gene are associated with Leigh syndrome resulting from mitochondrial complex I deficiency.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:7710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7710) · Entrez [4722](https://www.ncbi.nlm.nih.gov/gene/4722) · UniProt [O75489](https://www.uniprot.org/uniprotkb/O75489) · Ensembl [ENSG00000213619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213619)

## Data

Gene col 13118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13118); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13118]; `tensor/DDL_lfc|DDL_z.npy` [13118]; `embed/gene_vectors.npy` [13118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13118 or target_col == 13118). Every well: [[NDUFS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
