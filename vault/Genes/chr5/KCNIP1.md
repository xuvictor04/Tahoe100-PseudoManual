---
symbol: "KCNIP1"
type: "gene"
col: 11243
ensembl_id: "ENSG00000182132"
name: "potassium voltage-gated channel interacting protein 1"
location: "5q35.1"
module: 166
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# KCNIP1

*potassium voltage-gated channel interacting protein 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.77× (z +16.9, q 0e+00, up in 21 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SNU-423 0.0336×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.107×; ⚠ cell-cycle shift, explains ~18% of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SNU-423 0.125×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4300HG]] (+0.76, fdr 7e-06), [[ESR1]] (+0.75, fdr 7e-06), [[LRRC4C]] (+0.75, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CSF1R]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.77×** | +16.9 | 0e+00 | 21/25 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.72×** | +16.7 | 0e+00 | 19/26 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.56×** | +16.3 | 0e+00 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.40×** | +13.3 | 3e-38 | 4/6 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.51×** | +10.4 | 2e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +6.6 | 3e-09 | 12/36 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +6.0 | 1e-07 | 13/29 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.3 | 9e-06 | 1/4 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.2 | 1e-05 | 10/38 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 5/41 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.001 | 10/33 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 9/25 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.012 | 3/40 (HT-29, C-33 A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.053 | 3/12 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.097 | 0/36 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SNU-423 0.0336×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.107×; ⚠ cell-cycle shift, explains ~18% of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SNU-423 0.125×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | 0.671× | -3.4 | 0.37 | 2/27 (NCI-H460, NCI-H2030) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 3 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0336× (z -12.9) |
| [[A-172 (line)]] | wt | 2.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.0× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 2.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 1.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.6× (z +8.5) | — |
| [[A-427 (line)]] | wt | 0.755 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.922 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.823 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.754 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.734 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.939 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.766 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.789 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.671 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.859 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.815 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.832 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.871 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4300HG]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[ESR1]] | +0.75 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[LINC01500]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.73 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[SLC14A2]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DPP6]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 | same gene group; STRING 964 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF1R]] | B | CSF1R activity raises KCNIP1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.36× lower at baseline in the lines without CSF1R | 0.095 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.7, 30.0); signed map (30.4, 15.5). **Vector** length 41.8, 5.27% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +16.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +1.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:170,353,487-170,736,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KCHIP1 |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits; EF-hand domain containing |
| Reactome | 3 pathways, smallest: Phase 1 - inactivation of fast Na+ channels; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZI2](https://www.uniprot.org/uniprotkb/Q9NZI2) (A-type potassium channel modulatory protein KCNIP1):

> Regulatory subunit of Kv4/D (Shal)-type voltage-gated rapidly inactivating A-type potassium channels. Regulates channel density, inactivation kinetics and rate of recovery from inactivation in a calcium-dependent and isoform-specific manner. In vitro, modulates KCND1/Kv4.1 and KCND2/Kv4.2 currents. Increases the presence of KCND2 at the cell surface.

**Summary**, from NCBI Gene [30820](https://www.ncbi.nlm.nih.gov/gene/30820):

> This gene encodes a member of the family of cytosolic voltage-gated potassium (Kv) channel-interacting proteins (KCNIPs), which belong to the neuronal calcium sensor (NCS) family of the calcium binding EF-hand proteins. They associate with Kv4 alpha subunits to form native Kv4 channel complexes. The encoded protein may regulate rapidly inactivating (A-type) currents, and hence neuronal membrane excitability, in response to changes in the concentration of intracellular calcium. Alternative …

**Accessions** — [HGNC:15521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15521) · Entrez [30820](https://www.ncbi.nlm.nih.gov/gene/30820) · UniProt [Q9NZI2](https://www.uniprot.org/uniprotkb/Q9NZI2) · Ensembl [ENSG00000182132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182132)

## Data

Gene col 11243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11243); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11243]; `tensor/DDL_lfc|DDL_z.npy` [11243]; `embed/gene_vectors.npy` [11243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11243 or target_col == 11243). Every well: [[KCNIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
