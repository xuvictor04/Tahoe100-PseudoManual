---
symbol: "MRPL51"
type: "gene"
col: 3246
ensembl_id: "ENSG00000111639"
name: "mitochondrial ribosomal protein L51"
location: "12p13.31"
module: 48
arm: "+"
pooled_cpm: 38.32
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# MRPL51

*mitochondrial ribosomal protein L51* — 12p13.31

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.86× (z +7.3, q 2e-10, up in 40 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.127×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.109×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.190×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL36AL]] (+0.79, fdr 7e-06, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[COX17]] (+0.76, fdr 7e-06), [[LAMTOR5]] (+0.74, fdr 1e-05), [[ROMO1]] (+0.73, fdr 1e-05); moves opposite to [[IPO5]] (-0.64, fdr 4e-05), [[UBQLN1]] (-0.58, fdr 1e-05), [[PUS7L]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.86×** | +7.3 | 2e-10 | 40/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.56×** | +6.3 | 1e-07 | 34/38 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.17×** | +5.4 | 1e-05 | 44/46 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.7 | 0.028 | 34/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.63×** | +3.4 | 0.077 | 29/47 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.40×** | +3.3 | 0.079 | 37/48 (RKO, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3246.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.127×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.109×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.190×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.644× | -3.0 | 0.42 | 29/47 (hTERT-HPNE, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -17.2) |
| [[BT-474 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -10.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 19 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36AL]] ⚠ | +0.79 | +0.64 / +0.83 | both halves | 7e-06 | STRING 602; ⚠ in the vector space only through flagged drug-doses |
| [[COX17]] | +0.76 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.74 | +0.49 / +0.79 | both halves | 1e-05 |  |
| [[ROMO1]] | +0.73 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[UQCR10]] ⚠ | +0.73 | +0.61 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.73 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[EMC6]] | +0.72 | +0.57 / +0.77 | both halves | 8e-06 |  |
| [[ATP5MK]] | +0.71 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.71 | +0.57 / +0.74 | both halves | 1e-05 | STRING 480 |
| [[TMEM258]] | +0.70 | +0.54 / +0.75 | both halves | 1e-05 | STRING 463 |
| [[CHCHD1]] | +0.70 | +0.44 / +0.75 | both halves | 3e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 933 |
| [[ATP5ME]] | +0.69 | +0.48 / +0.77 | both halves | 2e-05 | STRING 422 |
| [[C19orf81]] | +0.68 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[SCAND1]] | +0.67 | +0.43 / +0.77 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.64 | -0.41 / -0.70 | both halves | 4e-05 |  |
| [[UBQLN1]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PUS7L]] | -0.57 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[TXNDC5]] | -0.57 | -0.26 / -0.69 | both halves | 3e-04 |  |
| [[LRPPRC]] | -0.56 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[SMG1P3]] | -0.56 | -0.35 / -0.70 | both halves | 1e-04 |  |
| [[TMX3]] | -0.56 | -0.39 / -0.58 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.0, -22.2); signed map (-33.8, 8.8). **Vector** length 57.0, 17.9% of its response variance represented; |z| ≥ 3 in 398 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.59 to 31); *Respiratory electron transport* (reactome, mean cos +0.58 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.60 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +1.9 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.8 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -4.9 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | -2.4 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L51 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,491,886-6,493,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDA09, HSPC241, bMRP64, mL51; previously MRP64 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q4U2R6](https://www.uniprot.org/uniprotkb/Q4U2R6) carries no function annotation.

**Summary**, from NCBI Gene [51258](https://www.ncbi.nlm.nih.gov/gene/51258):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14044) · Entrez [51258](https://www.ncbi.nlm.nih.gov/gene/51258) · UniProt [Q4U2R6](https://www.uniprot.org/uniprotkb/Q4U2R6) · Ensembl [ENSG00000111639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111639)

## Data

Gene col 3246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3246); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3246]; `tensor/DDL_lfc|DDL_z.npy` [3246]; `embed/gene_vectors.npy` [3246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3246 or target_col == 3246). Every well: [[MRPL51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
