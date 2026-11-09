---
symbol: "RAD1"
type: "gene"
col: 3465
ensembl_id: "ENSG00000113456"
name: "RAD1 checkpoint DNA exonuclease"
location: "5p13.2"
module: 6
arm: "+"
pooled_cpm: 22.02
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RAD1

*RAD1 checkpoint DNA exonuclease* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +11.0, q 3e-25, up in 27 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.12×, MIA PaCa-2 2.35×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 2.92×; ⚠ cell-cycle shift, explains ~35% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 4.02×; ⚠ cell-cycle shift, explains ~6% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.175×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Mozavaptan (drug)]] 0.05 µM in 1 line (SW48 0.0713×); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.503×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPN]] (+0.63, fdr 1e-05), [[RAD51]] (+0.61, fdr 3e-05), [[CMC2]] (+0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.12×, MIA PaCa-2 2.35×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 2.92×; ⚠ cell-cycle shift, explains ~35% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 4.02×; ⚠ cell-cycle shift, explains ~6% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +11.0 | 3e-25 | 27/46 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.56×** | +10.5 | 2e-23 | 26/41 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.49×** | +9.4 | 7e-19 | 32/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.50×** | +8.9 | 1e-16 | 22/37 (SW480, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.30×** | +8.7 | 5e-16 | 24/47 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +7.1 | 1e-10 | 23/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.37×** | +7.1 | 1e-10 | 21/33 (AsPC-1, KATO III, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.34×** | +6.9 | 4e-10 | 22/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.34×** | +6.7 | 1e-09 | 17/43 (KATO III, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +5.5 | 2e-06 | 16/48 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.27×** | +5.4 | 4e-06 | 19/46 (LoVo, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.23×** | +4.8 | 7e-05 | 14/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.4 | 6e-04 | 15/48 (A-172, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.19× | +4.2 | 0.001 | 11/48 (NCI-H23, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.18× | +4.0 | 0.003 | 10/47 (MIA PaCa-2, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.175×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Mozavaptan (drug)]] 0.05 µM in 1 line (SW48 0.0713×); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.503×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.866× | -3.4 | 0.21 | 11/48 (A498, A-172, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.767× | -3.3 | 0.21 | 7/48 (NCI-H460, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.865× | -3.2 | 0.21 | 12/47 (SNU-1, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.21 | 10/47 (SNU-423, HS-578T, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.895× | -3.1 | 0.25 | 8/48 (A498, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[A-427 (line)]] | wt | 31.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[AsPC-1 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[LoVo (line)]] | wt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.7) | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0713× (z -10.8) |
| [[A-172 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPN]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[RAD51]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 | pathway: DNA Double-Strand Break Repair; STRING 822 |
| [[CMC2]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[NCAPH2]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RPA2]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 717 |
| [[POLD3]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPJ]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[UBR7]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[RECQL4]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 | STRING 456 |
| [[DSN1]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 | pathway: Cell Cycle Checkpoints |
| [[USP1]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[E2F1]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.7, -47.9); signed map (-39.9, -41.6). **Vector** length 56.8, 7.79% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *CDC6 association with the ORC:origin complex* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +2.2 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +1.6 | +10.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +1.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +1.5 | +7.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.1 | -0.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.1 | +2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.8 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | RAD1 checkpoint DNA exonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:34,905,260-34,918,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRAD1, REC1 |
| Gene groups (HGNC) | Checkpoint clamp complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 21 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; HDR through Single Strand Annealing (SSA) |
| Matched by | ensembl_id |

**Function**, from UniProt [O60671](https://www.uniprot.org/uniprotkb/O60671) (Cell cycle checkpoint protein RAD1):

> Component of the 9-1-1 cell-cycle checkpoint response complex that plays a major role in DNA repair. The 9-1-1 complex is recruited to DNA lesion upon damage by the RAD17-replication factor C (RFC) clamp loader complex. Acts then as a sliding clamp platform on DNA for several proteins involved in long-patch base excision repair (LP-BER). The 9-1-1 complex stimulates DNA polymerase beta (POLB) activity by increasing its affinity for the 3'-OH end of the primer-template and stabilizes POLB to …

**Summary**, from NCBI Gene [5810](https://www.ncbi.nlm.nih.gov/gene/5810):

> This gene encodes a component of a heterotrimeric cell cycle checkpoint complex, known as the 9-1-1 complex, that is activated to stop cell cycle progression in response to DNA damage or incomplete DNA replication. The 9-1-1 complex is recruited by RAD17 to affected sites where it may attract specialized DNA polymerases and other DNA repair effectors. Alternatively spliced transcript variants of this gene have been described. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:9806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9806) · Entrez [5810](https://www.ncbi.nlm.nih.gov/gene/5810) · UniProt [O60671](https://www.uniprot.org/uniprotkb/O60671) · Ensembl [ENSG00000113456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113456)

## Data

Gene col 3465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3465); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3465]; `tensor/DDL_lfc|DDL_z.npy` [3465]; `embed/gene_vectors.npy` [3465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3465 or target_col == 3465). Every well: [[RAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
