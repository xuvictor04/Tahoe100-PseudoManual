---
symbol: "THSD7B"
type: "gene"
col: 6857
ensembl_id: "ENSG00000144229"
name: "thrombospondin type 1 domain containing 7B"
location: "2q22.1"
module: 150
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# THSD7B

*thrombospondin type 1 domain containing 7B* — 2q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.73× (z +25.4, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.875× (z -4.9, q 5e-04, down in 18 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Baicalin (drug)]] 0.5 µM: 0.671× (z -4.1, q 0.013, down in 9 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNTL6]] (+0.83, fdr 7e-06), [[LRRC4C]] (+0.79, fdr 7e-06), [[LINC01500]] (+0.78, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.73×** | +25.4 | 0e+00 | 29/32 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.34×** | +17.5 | 0e+00 | 25/33 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.94×** | +14.1 | 1e-42 | 7/12 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.47×** | +12.8 | 3e-35 | 29/41 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +12.2 | 4e-32 | 3/6 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +10.6 | 3e-24 | 3/6 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +10.0 | 8e-22 | 26/44 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.36×** | +8.8 | 7e-17 | 4/15 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.22×** | +8.2 | 2e-14 | 19/39 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.0 | 8e-14 | 14/43 (J82, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +7.6 | 1e-12 | 15/32 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.2 | 8e-06 | 9/43 (NCI-H460, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.2 | 1e-05 | 7/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.6 | 1e-04 | 10/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +4.3 | 6e-04 | 11/40 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.029 | 8/36 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.039 | 3/42 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.36×** | +2.9 | 0.092 | 3/28 (RPMI-7951, KATO III, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -4.9 | 5e-04 | 18/46 (RKO, COLO 205, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 0.5 µM |  | **0.671×** | -4.1 | 0.013 | 9/39 (PANC-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **0.707×** | -3.5 | 0.077 | 3/39 (SW 900, RPMI-7951, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 1.60 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.5) | — |
| [[SW480 (line)]] | alt | 1.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.6) | — |
| [[C32 (line)]] | wt | 2.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 1.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +9.8) | — |
| [[J82 (line)]] | alt | 6.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +10.7) | — |
| [[LoVo (line)]] | wt | 2.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.5× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 2.77 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.5× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 2.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 1.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNTL6]] | +0.83 | +0.76 / +0.81 | both halves | 7e-06 | pathway: O-linked glycosylation |
| [[LRRC4C]] | +0.79 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[LINC01500]] | +0.78 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.75 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[EYS]] | +0.75 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ESR1]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.75 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.75 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.75 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers THSD7B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.8, 28.6); signed map (32.6, 14.6). **Vector** length 54.1, 7.16% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +25.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +17.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin type 1 domain containing 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.1 — chr2:136,765,545-137,677,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1679 |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [Q9C0I4](https://www.uniprot.org/uniprotkb/Q9C0I4) carries no function annotation.

**Summary**, from NCBI Gene [80731](https://www.ncbi.nlm.nih.gov/gene/80731):

> Predicted to be involved in actin cytoskeleton organization. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29348) · Entrez [80731](https://www.ncbi.nlm.nih.gov/gene/80731) · UniProt [Q9C0I4](https://www.uniprot.org/uniprotkb/Q9C0I4) · Ensembl [ENSG00000144229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144229)

## Data

Gene col 6857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6857); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6857]; `tensor/DDL_lfc|DDL_z.npy` [6857]; `embed/gene_vectors.npy` [6857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6857 or target_col == 6857). Every well: [[THSD7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THSD7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
