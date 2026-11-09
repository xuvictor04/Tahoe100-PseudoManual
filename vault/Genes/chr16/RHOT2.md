---
symbol: "RHOT2"
type: "gene"
col: 6471
ensembl_id: "ENSG00000140983"
name: "ras homolog family member T2"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 12.99
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RHOT2

*ras homolog family member T2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +7.6, q 2e-11, up in 29 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.123×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDC4]] (+0.77, fdr 7e-06), [[TAF1C]] (+0.76, fdr 7e-06), [[ARFRP1]] (+0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +7.6 | 2e-11 | 29/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.81×** | +6.4 | 5e-08 | 19/28 (LoVo, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.2 | 1e-07 | 19/31 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +5.4 | 1e-05 | 31/48 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.56×** | +5.0 | 6e-05 | 23/38 (SW480, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.51×** | +4.7 | 3e-04 | 23/48 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.5 | 5e-04 | 21/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +4.5 | 5e-04 | 25/44 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +4.5 | 5e-04 | 19/43 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.004 | 16/47 (NCI-H460, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.004 | 20/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.41×** | +3.9 | 0.004 | 19/46 (RKO, PANC-1, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.7 | 0.010 | 15/30 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.030 | 16/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +3.3 | 0.033 | 15/48 (SW480, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.033 | 12/47 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.033 | 10/43 (J82, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.060 | 8/46 (Hs 766T, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.063 | 8/44 (RPMI-7951, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.063 | 11/47 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.76×** | +3.0 | 0.072 | 7/43 (RKO, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[BI-78D3 (drug)]] 0.5 µM |  | **1.46×** | +2.9 | 0.092 | 8/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6471.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.123×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.822× | -3.1 | 0.98 | 16/44 (SK-MEL-2, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDC4]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TAF1C]] | +0.76 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ARFRP1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[UCKL1]] | +0.69 | +0.50 / +0.74 | both halves | 1e-05 | **novel candidate** |
| [[FAAP100]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PLA2G4B]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[MUS81]] | +0.67 | +0.57 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[RPS6KB2]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[HGS]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ZNF598]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GPSM1]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PPP1R12C]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.8, -24.7); signed map (-26.7, 1.1). **Vector** length 70.4, 13.6% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.4 | +6.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +3.4 | +3.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.6 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member T2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:668,100-674,174 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIRO-2, MIRO2; previously C16orf39, ARHT2 |
| Gene groups (HGNC) | Miro like atypical Rho GTPases; EF-hand domain containing |
| Hallmark sets | APOPTOSIS, MITOTIC_SPINDLE, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: RHOT2 GTPase cycle; Miro GTPase Cycle; Signaling by Rho GTPases, Miro GTPases and RHOBTB3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXI1](https://www.uniprot.org/uniprotkb/Q8IXI1) (Mitochondrial Rho GTPase 2):

> Atypical mitochondrial nucleoside-triphosphatase (NTPase) involved in mitochondrial trafficking. Probably involved in control of anterograde transport of mitochondria and their subcellular distribution. Can hydrolyze GTP (By similarity). Can hydrolyze ATP and UTP.

**Summary**, from NCBI Gene [89941](https://www.ncbi.nlm.nih.gov/gene/89941):

> This gene encodes a member of the Rho family of GTPases. The encoded protein is localized to the outer mitochondrial membrane and plays a role in mitochondrial trafficking and fusion-fission dynamics. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:21169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21169) · Entrez [89941](https://www.ncbi.nlm.nih.gov/gene/89941) · UniProt [Q8IXI1](https://www.uniprot.org/uniprotkb/Q8IXI1) · Ensembl [ENSG00000140983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140983)

## Data

Gene col 6471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6471); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6471]; `tensor/DDL_lfc|DDL_z.npy` [6471]; `embed/gene_vectors.npy` [6471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6471 or target_col == 6471). Every well: [[RHOT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
