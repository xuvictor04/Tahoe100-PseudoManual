---
symbol: "OPCML"
type: "gene"
col: 11440
ensembl_id: "ENSG00000183715"
name: "opioid binding protein/cell adhesion molecule like"
location: "11q25"
module: 165
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# OPCML

*opioid binding protein/cell adhesion molecule like* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.04× (z +21.4, q 0e+00, up in 30 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SNU-423 0.0421×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP6]] (+0.78, fdr 7e-06), [[SLC8A1-AS1]] (+0.78, fdr 7e-06), [[MIR4300HG]] (+0.77, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02509]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.04×** | +21.4 | 0e+00 | 30/32 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +12.6 | 5e-34 | 22/35 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +11.3 | 4e-27 | 8/12 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +9.4 | 1e-18 | 4/7 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +9.3 | 2e-18 | 0/4 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.69×** | +9.3 | 2e-18 | 25/41 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.60×** | +9.0 | 3e-17 | 19/38 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.7 | 3e-16 | 25/44 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.7 | 9e-07 | 10/35 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +5.1 | 1e-05 | 13/37 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.0 | 3e-05 | 3/12 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.6 | 2e-04 | 8/28 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.6 | 0.016 | 2/12 (PANC-1, NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.5 | 0.016 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.016 | 3/41 (LoVo, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.047 | 4/34 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.081 | 6/43 (LS 180, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SNU-423 0.0421×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -3.8 | 0.070 | 16/46 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.794× | -3.0 | 0.43 | 14/43 (NCI-H1573, NCI-H23, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 0.05 µM |  | 0.723× | -3.0 | 0.43 | 5/40 (CFPAC-1, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.94× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +10.2) | — |
| [[KATO III (line)]] | alt | 4.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +8.7) | — |
| [[LoVo (line)]] | wt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.60× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0421× (z -10.9) |
| [[A-172 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP6]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.78 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.77 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.76 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.76 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.75 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[USH2A]] | +0.75 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.75 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[RETREG1-AS1]] | +0.75 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[LINC01579]] | +0.74 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.73 | +0.48 / +0.81 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02509]] | B | LINC02509 activity raises OPCML's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.27× lower at baseline in the lines without LINC02509 | 0.041 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.9, 29.9); signed map (31.1, 15.5). **Vector** length 57.8, 8.34% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +21.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | opioid binding protein/cell adhesion molecule like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:132,414,977-133,532,501 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OPCM, OBCAM, IGLON1 |
| Gene groups (HGNC) | I-set domain containing; IgLON cell adhesion molecules |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14982](https://www.uniprot.org/uniprotkb/Q14982) (Opioid-binding protein/cell adhesion molecule):

> Binds opioids in the presence of acidic lipids; probably involved in cell contact.

**Summary**, from NCBI Gene [4978](https://www.ncbi.nlm.nih.gov/gene/4978):

> This gene encodes a member of the IgLON subfamily in the immunoglobulin protein superfamily of proteins. The encoded preprotein is proteolytically processed to generate the mature protein. This protein is localized in the plasma membrane and may have an accessory role in opioid receptor function. This gene has an ortholog in rat and bovine. The opioid binding-cell adhesion molecule encoded by the rat gene binds opioid alkaloids in the presence of acidic lipids, exhibits selectivity for mu …

**Accessions** — [HGNC:8143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8143) · Entrez [4978](https://www.ncbi.nlm.nih.gov/gene/4978) · UniProt [Q14982](https://www.uniprot.org/uniprotkb/Q14982) · Ensembl [ENSG00000183715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183715)

## Data

Gene col 11440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11440); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11440]; `tensor/DDL_lfc|DDL_z.npy` [11440]; `embed/gene_vectors.npy` [11440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11440 or target_col == 11440). Every well: [[OPCML — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPCML.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
