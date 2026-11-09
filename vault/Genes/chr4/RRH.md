---
symbol: "RRH"
type: "gene"
col: 11092
ensembl_id: "ENSG00000180245"
name: "retinal pigment epithelium-derived rhodopsin homolog"
location: "4q25"
module: 37
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# RRH

*retinal pigment epithelium-derived rhodopsin homolog* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.17× (z +12.9, q 4e-35, up in 25 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0696×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL9]] (+0.80, fdr 7e-06), [[ISY1-RAB43]] (+0.79, fdr 7e-06), [[FAM209A]] (+0.78, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +12.9 | 4e-35 | 25/29 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.25×** | +11.4 | 1e-27 | 31/41 (SHP-77, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.18×** | +8.8 | 3e-16 | 11/15 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +7.8 | 8e-13 | 22/46 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.51×** | +7.2 | 5e-11 | 22/35 (LoVo, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +6.5 | 1e-08 | 15/34 (LoVo, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.69×** | +5.4 | 6e-06 | 12/36 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.64×** | +5.3 | 7e-06 | 11/26 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +5.0 | 4e-05 | 8/25 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +4.9 | 7e-05 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 9/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.5 | 3e-04 | 8/35 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.72×** | +4.2 | 9e-04 | 11/47 (SW480, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +3.7 | 0.009 | 12/45 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.38×** | +3.6 | 0.014 | 3/38 (A498, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.036 | 12/44 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11092.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.539× | -3.5 | 0.27 | 6/26 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.651× | -3.3 | 0.29 | 13/44 (A549, CHP-212, …) | top dose only | plate-row cell shift |
| [[NG25 (drug)]] 5 µM |  | 0.484× | -3.0 | 0.46 | 3/26 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.66 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0696× (z -10.3) |
| [[A-172 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL9]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[FAM209A]] | +0.78 | +0.71 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GABRR2]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.75 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[NUP210L]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.74 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[KLRA1P]] | +0.74 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.73 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CORIN]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RRH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IMPA1P1]] | B | IMPA1P1 activity raises RRH's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without IMPA1P1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, -17.4); signed map (13.5, 7.6). **Vector** length 66.6, 10.2% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +5.3 |
| fall | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | retinal pigment epithelium-derived rhodopsin homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,827,972-109,849,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | peropsin |
| Gene groups (HGNC) | Opsin receptors |
| Reactome | 5 pathways, smallest: Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [O14718](https://www.uniprot.org/uniprotkb/O14718) (Visual pigment-like receptor peropsin):

> Opsin-family protein localized to the apical microvilli of the retinal pigment epithelium (RPE), where it may participate in retinoid exchange between photoreceptors and RPE or light-dependent retinoid processing. Although it possesses the structural features of a GPCR, no evidence for canonical G protein activation in vivo has been reported.

**Summary**, from NCBI Gene [10692](https://www.ncbi.nlm.nih.gov/gene/10692):

> Opsins are members of the guanine nucleotide-binding protein (G protein)-coupled receptor superfamily. This gene belongs to the seven-exon subfamily of mammalian opsin genes that includes opsin 5 and retinal G protein coupled receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10450) · Entrez [10692](https://www.ncbi.nlm.nih.gov/gene/10692) · UniProt [O14718](https://www.uniprot.org/uniprotkb/O14718) · Ensembl [ENSG00000180245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180245)

## Data

Gene col 11092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11092); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11092]; `tensor/DDL_lfc|DDL_z.npy` [11092]; `embed/gene_vectors.npy` [11092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11092 or target_col == 11092). Every well: [[RRH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
