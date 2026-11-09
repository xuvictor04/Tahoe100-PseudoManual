---
symbol: "ARFIP2"
type: "gene"
col: 5288
ensembl_id: "ENSG00000132254"
name: "ARF interacting protein 2"
location: "11p15.4"
module: 41
arm: "+"
pooled_cpm: 28.14
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ARFIP2

*ARF interacting protein 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.79× (z +8.7, q 2e-15, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.127×, LS 180 0.324×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.0752×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.225×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPE]] (+0.78, fdr 7e-06), [[POFUT2]] (+0.77, fdr 7e-06), [[GOLGA2]] (+0.70, fdr 7e-06); moves opposite to [[THAP12]] (-0.60, fdr 7e-06), [[HACD3]] (-0.54, fdr 3e-05), [[PPP4R1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +8.7 | 2e-15 | 40/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.3 | 7e-08 | 34/47 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +5.3 | 2e-05 | 27/44 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.25×** | +4.4 | 0.002 | 22/47 (COLO 205, LoVo, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.30×** | +3.8 | 0.013 | 19/42 (SHP-77, BT-474, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +3.8 | 0.013 | 15/37 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.019 | 19/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +3.5 | 0.028 | 18/47 (AsPC-1, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.074 | 18/44 (Hs 766T, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | 1.49× | +3.1 | 0.10 | 8/47 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.10 | 9/48 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.0 | 0.11 | 11/48 (SW1417, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5288.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.127×, LS 180 0.324×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.0752×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.225×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.800× | -3.1 | 0.51 | 18/47 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.51 | 11/48 (LS 180, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.225× (z -10.2) |
| [[COLO 205 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[H4 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0752× (z -15.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | — |
| [[A-172 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPE]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[POFUT2]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LYSMD3]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[COG3]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[SCFD1]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SEC23IP]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[OSBP]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ARF4]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[SPTY2D1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SEC23B]] | +0.64 | +0.72 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP12]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[HACD3]] | -0.54 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[PPP4R1]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[HDAC2]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.9, -37.3); signed map (-51.7, 14.8). **Vector** length 98.0, 23.9% of its response variance represented; |z| ≥ 3 in 660 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.56 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.61 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +6.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.8 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.3 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ARF interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,474,683-6,481,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POR1 |
| Gene groups (HGNC) | AH domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P53365](https://www.uniprot.org/uniprotkb/P53365) (Arfaptin-2):

> Plays a role in constitutive metalloproteinase (MMP) secretion from the trans Golgi network. May have important functions during vesicle biogenesis at certain cargo subdomains, which could be predominantly utilized by secreted MMPs, such as MMP7 and MMP2. Also involved in autophagy by regulating the starvation-dependent trafficking of ATG9A vesicles which deliver the phosphatidylinositol 4-kinase beta (PI4KB) to the autophagosome initiation site. Involved in phagophore growth during mitophagy …

**Summary**, from NCBI Gene [23647](https://www.ncbi.nlm.nih.gov/gene/23647):

> Enables several functions, including GTP-dependent protein binding activity; membrane curvature sensor activity; and phosphatidylinositol-4-phosphate binding activity. Involved in actin cytoskeleton organization; mitophagy; and protein localization to phagophore assembly site. Located in cell cortex; ruffle; and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17160) · Entrez [23647](https://www.ncbi.nlm.nih.gov/gene/23647) · UniProt [P53365](https://www.uniprot.org/uniprotkb/P53365) · Ensembl [ENSG00000132254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132254)

## Data

Gene col 5288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5288); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5288]; `tensor/DDL_lfc|DDL_z.npy` [5288]; `embed/gene_vectors.npy` [5288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5288 or target_col == 5288). Every well: [[ARFIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
