---
symbol: "RPL22L1"
type: "gene"
col: 8721
ensembl_id: "ENSG00000163584"
name: "ribosomal protein L22 like 1"
location: "3q26.2"
module: 54
arm: "+"
pooled_cpm: 37.06
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL22L1

*ribosomal protein L22 like 1* — 3q26.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.45× (z +5.3, q 7e-05, up in 38 of 46 measured lines) ⚠ toxic; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.196×, RKO 0.197×, NCI-H23 0.261×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.230×, C-33 A 0.224×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.0643×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL17]] (+0.70, fdr 1e-05), [[TOMM5]] (+0.69, fdr 7e-06), [[MRPL34]] (+0.68, fdr 3e-05); moves opposite to [[SCRN1]] (-0.67, fdr 2e-05), [[UBE2A]] (-0.66, fdr 4e-05), [[PRKAR1A]] (-0.62, fdr 9e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.45×** | +5.3 | 7e-05 | 38/46 (LoVo, SK-MEL-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +5.1 | 1e-04 | 41/45 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.19×** | +4.8 | 3e-04 | 35/46 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +3.6 | 0.053 | 30/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | 1.69× | +3.2 | 0.14 | 27/45 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8721.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.196×, RKO 0.197×, NCI-H23 0.261×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.230×, C-33 A 0.224×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.0643×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.571× | -3.4 | 0.37 | 33/47 (HT-29, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 92.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 131 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0643× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 19 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL17]] | +0.70 | +0.57 / +0.69 | both halves | 1e-05 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 865 |
| [[TOMM5]] | +0.69 | +0.58 / +0.71 | both halves | 7e-06 | pathway: Protein localization |
| [[MRPL34]] | +0.68 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[RPS26]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 958 |
| [[LSM2]] | +0.66 | +0.30 / +0.72 | both halves | 2e-04 |  |
| [[SNHG15]] | +0.66 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | +0.66 | +0.38 / +0.66 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL14]] | +0.65 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[RPS14]] | +0.65 | +0.48 / +0.63 | both halves | 2e-05 | pathway: Cap-dependent Translation Initiation; STRING 962 |
| [[RSAD1]] | +0.65 | +0.53 / +0.64 | both halves | 1e-05 | STRING 909 |
| [[RPS10]] | +0.64 | +0.49 / +0.60 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 941 |
| [[RPL36]] | +0.64 | +0.38 / +0.64 | both halves | 7e-05 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 976 |
| [[NPM3]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCRN1]] | -0.67 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[UBE2A]] | -0.66 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[PRKAR1A]] | -0.62 | -0.36 / -0.64 | both halves | 9e-05 |  |
| [[EIF4G2]] | -0.61 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[TUG1]] | -0.59 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[STX16]] | -0.58 | -0.25 / -0.64 | both halves | 4e-04 |  |
| [[DVL3]] | -0.57 | -0.19 / -0.66 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZNF436]] | -0.57 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[EXOC7]] | -0.57 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[PEX19]] | -0.56 | -0.29 / -0.62 | both halves | 3e-04 | pathway: Protein localization |
| [[SMU1]] | -0.55 | -0.23 / -0.57 | both halves | 5e-04 |  |
| [[YWHAZ]] | -0.55 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[ATXN1L]] | -0.55 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-42.6, -29.5); signed map (-55.2, -2.8). **Vector** length 81.9, 28.0% of its response variance represented; |z| ≥ 3 in 593 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.53 to 9); *Mitochondrial translation* (reactome, mean cos +0.53 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.6 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L22 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:170,864,875-170,870,208 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

UniProt [Q6P5R6](https://www.uniprot.org/uniprotkb/Q6P5R6) carries no function annotation.

**Summary**, from NCBI Gene [200916](https://www.ncbi.nlm.nih.gov/gene/200916):

> Predicted to enable RNA binding activity. Predicted to be a structural constituent of ribosome. Predicted to be involved in cytoplasmic translation. Predicted to be located in cytoplasm and ribosome. Predicted to be part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27610) · Entrez [200916](https://www.ncbi.nlm.nih.gov/gene/200916) · UniProt [Q6P5R6](https://www.uniprot.org/uniprotkb/Q6P5R6) · Ensembl [ENSG00000163584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163584)

## Data

Gene col 8721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8721); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8721]; `tensor/DDL_lfc|DDL_z.npy` [8721]; `embed/gene_vectors.npy` [8721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8721 or target_col == 8721). Every well: [[RPL22L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL22L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
