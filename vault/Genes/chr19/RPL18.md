---
symbol: "RPL18"
type: "gene"
col: 722
ensembl_id: "ENSG00000063177"
name: "ribosomal protein L18"
location: "19q13.33"
module: 43
arm: "+"
pooled_cpm: 198.36
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL18

*ribosomal protein L18* — 19q13.33

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +5.5, q 3e-05, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 5 µM in 1 line (SW 1088 0.0703×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35A]] (+0.95, fdr 7e-06), [[RPL36]] (+0.95, fdr 7e-06), [[RPS3]] (+0.95, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPL31]] (+0.94, fdr 7e-06); moves opposite to [[PSME3]] (-0.75, fdr 8e-06), [[PNPO]] (-0.74, fdr 7e-06), [[FGD5-AS1]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.70×** | +5.5 | 3e-05 | 47/49 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.2 | 0.007 | 47/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.93×** | +3.7 | 0.035 | 40/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.89×** | +3.5 | 0.058 | 34/44 (A-172, LoVo, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.84×** | +3.5 | 0.058 | 41/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 5 µM in 1 line (SW 1088 0.0703×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 1088 (line)]] | alt | 131 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0703× (z -9.1) |
| [[A-172 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 279 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 263 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 253 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 176 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 135 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 169 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 282 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 327 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 227 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 301 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 248 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 217 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 270 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 242 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35A]] | +0.95 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: HALLMARK_P53_PATHWAY; STRING 999 |
| [[RPS3]] ⚠ | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.94 | +0.89 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS14]] | +0.93 | +0.79 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.91 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL13]] | +0.91 | +0.81 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS19]] | +0.90 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.90 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 999 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.75 | -0.58 / -0.79 | both halves | 8e-06 |  |
| [[PNPO]] | -0.74 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | -0.72 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.71 | -0.49 / -0.73 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[POGLUT3]] | -0.70 | -0.66 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.918). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-44.8, -26.6); signed map (-59.5, -3.6). **Vector** length 88.1, 57.5% of its response variance represented; |z| ≥ 3 in 348 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.74 to 19); *Translation initiation complex formation* (reactome, mean cos +0.71 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.71 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.1 | +0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.8 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -8.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -8.4 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | -2.8 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,615,328-48,619,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L18, eL18 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | P53_PATHWAY, MYC_TARGETS_V1 |
| Reactome | 39 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07020](https://www.uniprot.org/uniprotkb/Q07020) (Large ribosomal subunit protein eL18):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6141](https://www.ncbi.nlm.nih.gov/gene/6141):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the L18E family of ribosomal proteins that is a component of the 60S subunit. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene dispersed through the genome. Alternatively spliced transcript …

**Accessions** — [HGNC:10310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10310) · Entrez [6141](https://www.ncbi.nlm.nih.gov/gene/6141) · UniProt [Q07020](https://www.uniprot.org/uniprotkb/Q07020) · Ensembl [ENSG00000063177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063177)

## Data

Gene col 722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 722); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 722]; `tensor/DDL_lfc|DDL_z.npy` [722]; `embed/gene_vectors.npy` [722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 722 or target_col == 722). Every well: [[RPL18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
