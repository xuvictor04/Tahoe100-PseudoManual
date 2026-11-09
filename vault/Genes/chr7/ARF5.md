---
symbol: "ARF5"
type: "gene"
col: 40
ensembl_id: "ENSG00000004059"
name: "ARF GTPase 5"
location: "7q32.1"
module: 48
arm: "+"
pooled_cpm: 19.58
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ARF5

*ARF GTPase 5* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.72× (z +10.9, q 7e-25, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 4.34×, HEC-1-A 5.60×, HT-29 5.11×, KATO III 3.72×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (C32 5.28×, HT-29 4.84×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.610× (z -5.8, q 4e-06, down in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.114×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.361×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR2]] (+0.71, fdr 1e-05), [[NPC2]] (+0.67, fdr 1e-05), [[NDUFA2]] (+0.66, fdr 1e-05); moves opposite to [[HNRNPAB]] (-0.60, fdr 2e-05), [[CCT5]] (-0.58, fdr 3e-05), [[SLC19A1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 40.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 4.34×, HEC-1-A 5.60×, HT-29 5.11×, KATO III 3.72×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (C32 5.28×, HT-29 4.84×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +10.9 | 7e-25 | 39/41 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +8.3 | 2e-14 | 29/31 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +6.3 | 6e-08 | 33/37 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.94×** | +5.5 | 5e-06 | 37/44 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.6 | 0.042 | 24/42 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 40.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.114×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.361×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.610×** | -5.8 | 4e-06 | 35/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tadalafil (drug)]] 5 µM |  | 0.681× | -3.1 | 0.64 | 22/48 (NCI-H661, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 40. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 22.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -13.1) |
| [[A498 (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +9.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.4) |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 40), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR2]] | +0.71 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[NPC2]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SVBP]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PPDPF]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ATP5IF1]] | +0.63 | +0.30 / +0.71 | both halves | 2e-04 |  |
| [[MORN2]] | +0.63 | +0.36 / +0.71 | both halves | 1e-04 |  |
| [[ZCRB1]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[GABARAP]] ⚠ | +0.62 | +0.54 / +0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHMP2A]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[CERT1]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PIAS1]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ELF2]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[CCT5]] | -0.58 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SLC19A1]] | -0.57 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[NOLC1]] | -0.56 | -0.40 / -0.64 | both halves | 4e-05 |  |
| [[CTPS1]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[LRP8]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[DDX21]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[DNAH1]] | -0.51 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[NAA15]] | -0.51 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[PUS1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[BICD1]] | -0.50 | -0.52 / -0.43 | both halves | 4e-05 | pathway: Golgi-to-ER retrograde transport |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-8.2, -45.4); signed map (-11.4, 6.6). **Vector** length 43.8, 7.70% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial protein degradation* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.1 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.9 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | +0.5 |
|  | [[Pemetrexed (drug)]] 0.5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:127,588,386-127,591,700 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P84085](https://www.uniprot.org/uniprotkb/P84085) (ADP-ribosylation factor 5):

> GTP-binding protein involved in protein trafficking. Contributes to vesicle budding and uncoating at the Golgi apparatus. Regulates mTORC1 activity at the plasma membrane by promoting its recruitment to membrane ruffles, facilitating activation via the PI3K/Akt signaling pathway. Acts as an early responder to lysosomal damage and participates in lysosomal quality control pathways.; (Microbial infection) Functions as an allosteric activator of the cholera toxin catalytic subunit, an …

**Summary**, from NCBI Gene [381](https://www.ncbi.nlm.nih.gov/gene/381):

> This gene is a member of the human ADP-ribosylation factor (ARF) gene family. These genes encode small guanine nucleotide-binding proteins that stimulate the ADP-ribosyltransferase activity of cholera toxin and play a role in vesicular trafficking and as activators of phospholipase D. The gene products include 6 ARF proteins and 11 ARF-like proteins and constitute 1 family of the RAS superfamily. The ARF proteins are categorized as class I (ARF1, ARF2,and ARF3), class II (ARF4 and ARF5) and …

**Accessions** — [HGNC:658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:658) · Entrez [381](https://www.ncbi.nlm.nih.gov/gene/381) · UniProt [P84085](https://www.uniprot.org/uniprotkb/P84085) · Ensembl [ENSG00000004059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004059)

## Data

Gene col 40: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 40); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 40, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 40]; `tensor/DDL_lfc|DDL_z.npy` [40]; `embed/gene_vectors.npy` [40]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 40 or target_col == 40). Every well: [[ARF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
