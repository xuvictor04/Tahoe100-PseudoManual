---
symbol: "ATP5MK"
type: "gene"
col: 10443
ensembl_id: "ENSG00000173915"
name: "ATP synthase membrane subunit k"
location: "10q24.33"
module: 48
arm: "+"
pooled_cpm: 61.21
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5MK

*ATP synthase membrane subunit k* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.87× (z +7.0, q 1e-09, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.588× (z -4.5, q 0.005, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.295×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0768×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD6]] (+0.88, fdr 7e-06), [[ROMO1]] (+0.88, fdr 7e-06), [[ATP5MJ]] (+0.88, fdr 7e-06); moves opposite to [[HNRNPL]] (-0.71, fdr 1e-05), [[SRSF3]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.87×** | +7.0 | 1e-09 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.77×** | +5.8 | 1e-06 | 38/42 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.98×** | +4.1 | 0.008 | 41/47 (COLO 205, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.84×** | +3.6 | 0.040 | 37/47 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.90×** | +3.5 | 0.042 | 33/45 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.5 | 0.042 | 34/47 (MIA PaCa-2, SW 1271, …) | top dose only | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.295×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0768×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.588×** | -4.5 | 0.005 | 38/48 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.562× | -3.4 | 0.18 | 44/48 (RKO, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0768× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.295× (z -17.3) |
| [[A-172 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 26 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | +0.88 | +0.78 / +0.87 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.88 | +0.82 / +0.87 | both halves | 7e-06 | STRING 457 |
| [[ATP5MJ]] | +0.88 | +0.80 / +0.88 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[COX6B1]] | +0.87 | +0.76 / +0.89 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[LAMTOR5]] | +0.86 | +0.75 / +0.87 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.85 | +0.81 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5PD]] | +0.85 | +0.65 / +0.90 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[UBL5]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[NDUFA1]] | +0.84 | +0.80 / +0.89 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 485 |
| [[COX6A1]] | +0.83 | +0.78 / +0.84 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 461 |
| [[UQCRQ]] ⚠ | +0.83 | +0.69 / +0.84 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 898; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | +0.82 | +0.69 / +0.86 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[COX6C]] | +0.81 | +0.67 / +0.85 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 915 |
| [[UBA52]] | +0.81 | +0.72 / +0.80 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | -0.71 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.69 | -0.60 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.892). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.5, -22.3); signed map (-34.3, 9.1). **Vector** length 64.6, 29.4% of its response variance represented; |z| ≥ 3 in 413 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.67 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.71 to 24); *Complex IV assembly* (reactome, mean cos +0.71 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +2.9 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -5.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -4.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.2 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit k |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,389,041-103,396,492 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14697, bA792D24.4, DAPIT, AGP; previously USMG5, ATP5MD |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IX5](https://www.uniprot.org/uniprotkb/Q96IX5) (ATP synthase F(0) complex subunit k, mitochondrial):

> Subunit k, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain (Probable). ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel (By similarity). These two domains are linked by a central stalk rotating inside the F(1) …

**Summary**, from NCBI Gene [84833](https://www.ncbi.nlm.nih.gov/gene/84833):

> Predicted to be involved in proton motive force-driven ATP synthesis. Located in mitochondrion. Part of proton-transporting ATP synthase complex. Implicated in mitochondrial complex V (ATP synthase) deficiency nuclear type 6. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30889) · Entrez [84833](https://www.ncbi.nlm.nih.gov/gene/84833) · UniProt [Q96IX5](https://www.uniprot.org/uniprotkb/Q96IX5) · Ensembl [ENSG00000173915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173915)

## Data

Gene col 10443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10443); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10443]; `tensor/DDL_lfc|DDL_z.npy` [10443]; `embed/gene_vectors.npy` [10443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10443 or target_col == 10443). Every well: [[ATP5MK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
