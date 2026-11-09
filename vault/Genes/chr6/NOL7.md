---
symbol: "NOL7"
type: "gene"
col: 13496
ensembl_id: "ENSG00000225921"
name: "nucleolar protein 7"
location: "6p23"
module: 12
arm: "+"
pooled_cpm: 68.18
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NOL7

*nucleolar protein 7* — 6p23

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.69× (z +4.2, q 0.007, up in 44 of 48 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH10]] (+0.76, fdr 7e-06), [[POLR2I]] (+0.76, fdr 7e-06), [[RBMX2]] (+0.76, fdr 7e-06); moves opposite to [[GPAA1]] (-0.69, fdr 1e-05), [[PRPS2]] (-0.66, fdr 7e-06), [[MOB1A]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.69×** | +4.2 | 0.007 | 44/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.93×** | +4.2 | 0.007 | 37/49 (SNU-423, MIA PaCa-2, …) | two highest doses | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.7 | 0.042 | 39/47 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.55×** | +3.4 | 0.097 | 33/47 (SW 900, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.51× | +3.3 | 0.10 | 33/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.49× | +3.1 | 0.17 | 32/48 (hTERT-HPNE, C-33 A, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.61× | +3.1 | 0.17 | 37/48 (NCI-H23, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.46× | +3.0 | 0.17 | 28/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.654× | -3.4 | 0.23 | 33/48 (HepG2/C3A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.746× | -3.4 | 0.23 | 40/48 (SW 900, RKO, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.688× | -3.0 | 0.48 | 38/48 (HepG2/C3A, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 109 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH10]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 | STRING 833 |
| [[POLR2I]] | +0.76 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[PUS3]] | +0.76 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MRPL21]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[RPP21]] | +0.75 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[CINP]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.74 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.74 | +0.50 / +0.81 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB9]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PSMA7]] | +0.69 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[TRAPPC5]] | +0.68 | +0.37 / +0.72 | both halves | 7e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPAA1]] | -0.69 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.66 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.63 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.63 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.63 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.62 | -0.51 / -0.73 | both halves | 1e-05 |  |
| [[NEMP1]] | -0.62 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[CBX5]] | -0.62 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.62 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[PTBP1]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[HELLS]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TYMS]] | -0.62 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises NOL7's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without MYBL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-38.2, -9.8); signed map (-16.8, -7.6). **Vector** length 79.1, 31.9% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.1 | +4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p23 — chr6:13,615,335-13,632,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOP27, RARG-1, dJ223E5.2; previously C6orf90, PQBP3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMY1](https://www.uniprot.org/uniprotkb/Q9UMY1) (U3 small nucleolar RNA-associated protein NOL7):

> Functions as part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit that coordinates the first two steps of ribosome biogenesis in transcription of the primary transcript pre-RNA and pre-18S processing. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [51406](https://www.ncbi.nlm.nih.gov/gene/51406):

> The protein encoded by this gene localizes to the nucleolus, where it maintains nucleolar structure and cell growth rates. The encoded protein also functions as a tumor suppressor and regulator of angiogenesis. The RB tumor suppressor gene recruits transcription factors to this gene and positively regulates its expression. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:21040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21040) · Entrez [51406](https://www.ncbi.nlm.nih.gov/gene/51406) · UniProt [Q9UMY1](https://www.uniprot.org/uniprotkb/Q9UMY1) · Ensembl [ENSG00000225921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225921)

## Data

Gene col 13496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13496); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13496]; `tensor/DDL_lfc|DDL_z.npy` [13496]; `embed/gene_vectors.npy` [13496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13496 or target_col == 13496). Every well: [[NOL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
