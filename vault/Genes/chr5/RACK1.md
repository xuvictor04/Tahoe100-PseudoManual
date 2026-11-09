---
symbol: "RACK1"
type: "gene"
col: 12907
ensembl_id: "ENSG00000204628"
name: "receptor for activated C kinase 1"
location: "5q35.3"
module: 43
arm: "+"
pooled_cpm: 391.53
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RACK1

*receptor for activated C kinase 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +6.7, q 1e-08, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.42×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.39×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.498× (z -8.0, q 1e-12, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (SNU-1 0.203×, SW48 0.298×, RKO 0.340×, CHP-212 0.284×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL7]] (+0.93, fdr 7e-06), [[RPL12]] (+0.91, fdr 7e-06), [[RPLP0]] (+0.91, fdr 7e-06); moves opposite to [[MIS12]] (-0.65, fdr 1e-05), [[FAM111A]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12907.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.42×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.39×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +6.7 | 1e-08 | 49/49 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.6 | 5e-06 | 43/44 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.77×** | +4.6 | 7e-04 | 46/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +4.4 | 0.002 | 41/45 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12907.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (SNU-1 0.203×, SW48 0.298×, RKO 0.340×, CHP-212 0.284×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.498×** | -8.0 | 1e-12 | 46/48 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 652 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.6) |
| [[A-427 (line)]] | wt | 416 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 320 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.9) |
| [[C-33 A (line)]] | alt | 353 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.1) |
| [[CHP-212 (line)]] | wt | 361 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.0) |
| [[COLO 205 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 503 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.9) |
| [[HCT15 (line)]] | alt | 439 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 428 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.7) |
| [[HT-29 (line)]] | alt | 340 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.7) |
| [[LoVo (line)]] | wt | 693 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.2) |
| [[LS 180 (line)]] | wt | 348 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 568 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 335 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 344 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 423 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 617 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.2) |
| [[RKO (line)]] | wt | 455 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.1) |
| [[SNU-1 (line)]] | wt | 383 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.9) |
| [[SW48 (line)]] | wt | 489 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.3) |
| [[SW480 (line)]] | alt | 406 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.7) |
| [[A-172 (line)]] | wt | 279 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 300 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 403 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 523 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 494 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 320 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 427 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 362 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 232 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 486 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 392 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 423 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 491 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 314 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | STRING 999 |
| [[RPL12]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | same gene group; STRING 999 |
| [[RPLP0]] | +0.91 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL11]] | +0.90 | +0.84 / +0.90 | both halves | 7e-06 | STRING 999 |
| [[RPS5]] | +0.90 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL13]] | +0.89 | +0.85 / +0.87 | both halves | 7e-06 | same gene group; STRING 999 |
| [[RPL26]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | STRING 999 |
| [[RPS14]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | STRING 999 |
| [[RPL19]] | +0.88 | +0.80 / +0.89 | both halves | 7e-06 | STRING 999 |
| [[RPL10A]] ⚠ | +0.88 | +0.73 / +0.90 | both halves | 7e-06 | STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL27A]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | same gene group; STRING 999 |
| [[RPS4X]] | +0.86 | +0.87 / +0.89 | both halves | 7e-06 | STRING 999 |
| [[RPS8]] | +0.86 | +0.78 / +0.87 | both halves | 7e-06 | same gene group; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.65 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.898). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.4, -29.3); signed map (-61.1, -5.8). **Vector** length 90.3, 55.6% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.80 to 55); *Peptide chain elongation* (reactome, mean cos +0.80 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.79 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.6 | -0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.4 | +1.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.8 | +0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | receptor for activated C kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:181,236,897-181,248,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Gnb2-rs1, H12.3; previously GNB2L1 |
| Gene groups (HGNC) | WD repeat domain containing; SSU processome; Small nucleolar RNA protein coding host genes |
| Hallmark sets | P53_PATHWAY, MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: TNFR1-mediated ceramide production; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P63244](https://www.uniprot.org/uniprotkb/P63244) (Small ribosomal subunit protein RACK1):

> Scaffolding protein involved in the recruitment, assembly and/or regulation of a variety of signaling molecules. Interacts with a wide variety of proteins and plays a role in many cellular processes. Component of the 40S ribosomal subunit involved in translational repression. Involved in the initiation of the ribosome quality control (RQC), a pathway that takes place when a ribosome has stalled during translation, by promoting ubiquitination of a subset of 40S ribosomal subunits. Binds to and …

**Summary**, from NCBI Gene [10399](https://www.ncbi.nlm.nih.gov/gene/10399):

> Enables several functions, including enzyme binding activity; protein domain specific binding activity; and protein kinase inhibitor activity. Involved in several processes, including positive regulation of protein metabolic process; regulation of signal transduction; and regulation of vesicle-mediated transport. Located in several cellular components, including midbody; perinuclear region of cytoplasm; and phagocytic cup. Part of IRE1-RACK1-PP2A complex. [provided by Alliance of Genome …

**Accessions** — [HGNC:4399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4399) · Entrez [10399](https://www.ncbi.nlm.nih.gov/gene/10399) · UniProt [P63244](https://www.uniprot.org/uniprotkb/P63244) · Ensembl [ENSG00000204628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204628)

## Data

Gene col 12907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12907); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12907]; `tensor/DDL_lfc|DDL_z.npy` [12907]; `embed/gene_vectors.npy` [12907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12907 or target_col == 12907). Every well: [[RACK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RACK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
