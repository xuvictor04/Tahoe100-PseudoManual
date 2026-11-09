---
symbol: "STOML2"
type: "gene"
col: 9102
ensembl_id: "ENSG00000165283"
name: "stomatin like 2"
location: "9p13.3"
module: 7
arm: "+"
pooled_cpm: 26.6
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# STOML2

*stomatin like 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.26× (z +11.0, q 2e-25, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.65× (z +3.8, q 0.013, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.680× (z -4.2, q 0.016, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH3B]] (+0.63, fdr 7e-06), [[VPS25]] (+0.62, fdr 7e-06), [[DDX56]] (+0.60, fdr 1e-05); moves opposite to [[ARHGAP33]] (-0.42, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.26×** | +11.0 | 2e-25 | 44/44 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.46×** | +7.8 | 2e-12 | 31/33 (A498, KATO III, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.50×** | +6.4 | 3e-08 | 29/40 (Hs 766T, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **2.09×** | +5.6 | 4e-06 | 39/46 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +4.3 | 0.002 | 24/48 (A498, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.8 | 0.012 | 32/46 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.013 | 31/48 (NCI-H2030, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.19×** | +3.7 | 0.018 | 36/47 (NCI-H23, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.08×** | +3.4 | 0.042 | 30/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.10 | 21/46 (Hs 766T, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.93× | +3.1 | 0.12 | 25/45 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.680×** | -4.2 | 0.016 | 29/47 (SNU-1, NCI-H661, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 46.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3B]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 | STRING 419 |
| [[VPS25]] | +0.62 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[DDX56]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[NDUFAF4]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NDUFAB1]] | +0.59 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[RBM42]] | +0.57 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RNF7]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[DNLZ]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TMEM70]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[YDJC]] | +0.52 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[PPP1R8]] | +0.51 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[PRR14L]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP33]] | -0.42 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-51.1, 1.5); signed map (-4.2, -19.7). **Vector** length 48.5, 11.4% of its response variance represented; |z| ≥ 3 in 420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -1.2 | +6.4 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | stomatin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,099,776-35,103,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLP-2, HSPC108 |
| Gene groups (HGNC) | Stomatin family |
| Reactome | 6 pathways, smallest: Cellular response to mitochondrial stress; Processing of SMDT1; Mitochondrial calcium ion transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJZ1](https://www.uniprot.org/uniprotkb/Q9UJZ1) (Stomatin-like protein 2, mitochondrial):

> Mitochondrial protein that probably regulates the biogenesis and the activity of mitochondria. Stimulates cardiolipin biosynthesis, binds cardiolipin-enriched membranes where it recruits and stabilizes some proteins including prohibitin and may therefore act in the organization of functional microdomains in mitochondrial membranes. Through regulation of the mitochondrial function may play a role into several biological processes including cell migration, cell proliferation, T-cell activation, …

**Summary**, from NCBI Gene [30968](https://www.ncbi.nlm.nih.gov/gene/30968):

> Enables GTPase binding activity; T cell receptor binding activity; and cardiolipin binding activity. Involved in intracellular calcium ion homeostasis; mitochondrion organization; and protein complex oligomerization. Acts upstream of or within T cell receptor signaling pathway. Located in several cellular components, including immunological synapse; membrane raft; and mitochondrial envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14559) · Entrez [30968](https://www.ncbi.nlm.nih.gov/gene/30968) · UniProt [Q9UJZ1](https://www.uniprot.org/uniprotkb/Q9UJZ1) · Ensembl [ENSG00000165283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165283)

## Data

Gene col 9102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9102); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9102]; `tensor/DDL_lfc|DDL_z.npy` [9102]; `embed/gene_vectors.npy` [9102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9102 or target_col == 9102). Every well: [[STOML2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STOML2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
