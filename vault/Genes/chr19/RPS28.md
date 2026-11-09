---
symbol: "RPS28"
type: "gene"
col: 13930
ensembl_id: "ENSG00000233927"
name: "ribosomal protein S28"
location: "19p13.2"
module: 43
arm: "+"
pooled_cpm: 49.94
n_lines_expressing: 40
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPS28

*ribosomal protein S28* — 19p13.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.41× (z +6.4, q 7e-08, up in 32 of 34 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.319×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL13]] (+0.93, fdr 7e-06), [[RPL31]] (+0.92, fdr 7e-06), [[RPS14]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TOMM7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.41×** | +6.4 | 7e-08 | 32/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +6.3 | 7e-08 | 25/31 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +4.8 | 3e-04 | 24/31 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.85×** | +4.4 | 0.001 | 31/37 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.031 | 22/35 (HT-29, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.319×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.726× | -3.3 | 0.58 | 23/37 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.8) |
| [[A-172 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL13]] | +0.93 | +0.87 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.92 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.92 | +0.86 / +0.87 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPLP2]] | +0.92 | +0.84 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.91 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.91 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS8]] | +0.91 | +0.85 / +0.87 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL26]] | +0.91 | +0.85 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.90 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL35]] ⚠ | +0.90 | +0.79 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.90 | +0.83 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.90 | +0.86 / +0.86 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.89 | +0.80 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOMM7]] | B | RPS28 activity raises TOMM7's level | lines that do not express RPS28 (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without RPS28 | 0.011 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.918). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.0, -27.3); signed map (-60.6, -3.8). **Vector** length 52.2, 14.0% of its response variance represented; |z| ≥ 3 in 283 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.83 to 34); *MYC targets v1* (hallmark, mean cos +0.64 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.66 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.1 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,321,158-8,323,340 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S28, eS28 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62857](https://www.uniprot.org/uniprotkb/P62857) (Small ribosomal subunit protein eS28):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6234](https://www.ncbi.nlm.nih.gov/gene/6234):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S28E family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this …

**Accessions** — [HGNC:10418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10418) · Entrez [6234](https://www.ncbi.nlm.nih.gov/gene/6234) · UniProt [P62857](https://www.uniprot.org/uniprotkb/P62857) · Ensembl [ENSG00000233927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233927)

## Data

Gene col 13930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13930); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13930]; `tensor/DDL_lfc|DDL_z.npy` [13930]; `embed/gene_vectors.npy` [13930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13930 or target_col == 13930). Every well: [[RPS28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
