---
symbol: "UQCRB"
type: "gene"
col: 7982
ensembl_id: "ENSG00000156467"
name: "ubiquinol-cytochrome c reductase binding protein"
location: "8q22.1"
module: 43
arm: "+"
pooled_cpm: 152.35
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# UQCRB

*ubiquinol-cytochrome c reductase binding protein* — 8q22.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.18× (z +7.5, q 4e-11, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 5.90×, MIA PaCa-2 7.65×, NCI-H460 5.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 5.01×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS19]] (+0.92, fdr 7e-06), [[RPL36]] (+0.90, fdr 7e-06), [[RPS12]] (+0.90, fdr 7e-06); moves opposite to [[ZNF460]] (-0.74, fdr 7e-06), [[PSME3]] (-0.71, fdr 7e-06), [[PSMG1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 5.90×, MIA PaCa-2 7.65×, NCI-H460 5.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 5.01×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.18×** | +7.5 | 4e-11 | 49/49 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.28×** | +6.7 | 6e-09 | 43/44 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.8 | 3e-04 | 47/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.40×** | +4.8 | 3e-04 | 42/45 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.98×** | +4.0 | 0.006 | 44/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.75×** | +3.3 | 0.087 | 40/48 (NCI-H460, COLO 205, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.655× | -3.1 | 0.47 | 34/48 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.564× | -3.1 | 0.47 | 47/48 (C-33 A, LoVo, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.569× | -3.0 | 0.47 | 45/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 96.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.90× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 72.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 249 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 168 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 166 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 243 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 25 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS19]] | +0.92 | +0.87 / +0.92 | both halves | 7e-06 |  |
| [[RPL36]] | +0.90 | +0.85 / +0.92 | both halves | 7e-06 |  |
| [[RPS12]] | +0.90 | +0.84 / +0.90 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.90 | +0.82 / +0.92 | both halves | 7e-06 | STRING 447 |
| [[RPLP1]] | +0.89 | +0.83 / +0.90 | both halves | 7e-06 |  |
| [[RPL37A]] ⚠ | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | STRING 481 |
| [[RPS27]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 |  |
| [[RPS27A]] ⚠ | +0.88 | +0.82 / +0.90 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[COX4I1]] ⚠ | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[RPS17]] ⚠ | +0.88 | +0.79 / +0.90 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 |  |
| [[RPL31]] | +0.87 | +0.78 / +0.89 | both halves | 7e-06 | STRING 420 |
| [[COX6B1]] | +0.87 | +0.83 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX7C]] | +0.86 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[RPL23]] | +0.86 | +0.77 / +0.89 | both halves | 7e-06 | STRING 426 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460]] | -0.74 | -0.61 / -0.77 | both halves | 7e-06 |  |
| [[PSME3]] | -0.71 | -0.61 / -0.76 | both halves | 7e-06 |  |
| [[PSMG1]] | -0.69 | -0.61 / -0.70 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.849). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.3, -24.2); signed map (-35.2, 8.6). **Vector** length 73.9, 46.8% of its response variance represented; |z| ≥ 3 in 406 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.72 to 55); *Peptide chain elongation* (reactome, mean cos +0.73 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.72 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.0 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.9 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -6.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.9 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +1.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | -3.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | +0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:96,222,947-96,235,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | QP-C, QCR7, UQCR6; previously UQBP |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P14927](https://www.uniprot.org/uniprotkb/P14927) (Cytochrome b-c1 complex subunit 7):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [7381](https://www.ncbi.nlm.nih.gov/gene/7381):

> This gene encodes a subunit of the ubiquinol-cytochrome c oxidoreductase complex, which consists of one mitochondrial-encoded and 10 nuclear-encoded subunits. The protein encoded by this gene binds ubiquinone and participates in the transfer of electrons when ubiquinone is bound. This protein plays an important role in hypoxia-induced angiogenesis through mitochondrial reactive oxygen species-mediated signaling. Mutations in this gene are associated with mitochondrial complex III deficiency. …

**Accessions** — [HGNC:12582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12582) · Entrez [7381](https://www.ncbi.nlm.nih.gov/gene/7381) · UniProt [P14927](https://www.uniprot.org/uniprotkb/P14927) · Ensembl [ENSG00000156467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156467)

## Data

Gene col 7982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7982); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7982]; `tensor/DDL_lfc|DDL_z.npy` [7982]; `embed/gene_vectors.npy` [7982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7982 or target_col == 7982). Every well: [[UQCRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
