---
symbol: "EEF1A1P5"
type: "gene"
col: 12154
ensembl_id: "ENSG00000196205"
name: "eukaryotic translation elongation factor 1 alpha 1 pseudogene 5"
location: "9q34.13"
module: 20
arm: "+"
pooled_cpm: 3.39
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EEF1A1P5

*eukaryotic translation elongation factor 1 alpha 1 pseudogene 5* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.67× (z +8.0, q 7e-13, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.69× (z +4.6, q 6e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.835× (z -5.6, q 1e-05, down in 26 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Darinaparsin (drug)]] 5 µM: 0.743× (z -3.7, q 0.069, down in 12 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0722×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (LoVo 0.0720×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1A1]] (+0.91, fdr 7e-06), [[RPL4]] (+0.84, fdr 7e-06), [[ANKRD30BL]] (+0.77, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.59, fdr 1e-05), [[ISG20L2]] (-0.59, fdr 1e-05), [[MIDN]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYBRD1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EEF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +8.0 | 7e-13 | 6/8 (SNU-423, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +7.8 | 2e-12 | 2/5 (HOP62, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.2 | 1e-07 | 11/20 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +4.6 | 6e-04 | 12/46 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.3 | 0.002 | 7/23 (LOX-IMVI, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.53×** | +3.5 | 0.040 | 7/45 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.43× | +3.0 | 0.19 | 8/39 (NCI-H460, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12154.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0722×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (LoVo 0.0720×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.835× | -5.6 | 1e-05 | 26/48 (SNU-1, PANC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.743×** | -3.7 | 0.069 | 12/44 (LS 180, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.610× | -3.1 | 0.38 | 6/39 (LOX-IMVI, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.70 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0720× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 3.44 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0722× (z -9.1) |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1A1]] | +0.91 | +0.84 / +0.91 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[RPL4]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[ANKRD30BL]] | +0.77 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RPL10]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[RPS18]] | +0.76 | +0.74 / +0.79 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[HNRNPA1L3]] | +0.75 | +0.64 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[EIF4H]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[RPL3]] | +0.72 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[RPS3A]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[DHFR]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[HFM1]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ISG20L2]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[MIDN]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[PRPF38B]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TARS2]] | -0.55 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[RPP14]] | -0.55 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | -0.54 | -0.39 / -0.56 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ADPRS]] | -0.54 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PPP1R35]] ⚠ | -0.54 | -0.48 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF316]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[C1orf35]] | -0.53 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[ZNF557]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYBRD1]] | B | CYBRD1 activity raises EEF1A1P5's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.13× lower at baseline in the lines without CYBRD1 | 0.055 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF2]] | C | EEF1A1P5's natural level weakens EEF2's drug response | EEF1A1P5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.48; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.1, -25.3); signed map (-21.7, -34.2). **Vector** length 44.7, 4.73% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.62 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.62 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.65 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.1 | +0.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.0 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.1 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 alpha 1 pseudogene 5 |
| Locus type | pseudogene |
| Location | 9q34.13 — chr9:133,019,486-133,020,874 (+) |
| Ensembl biotype | processed_pseudogene |
| Also known as | ; previously EEF1AL3 |
| Reactome | 2 pathways, smallest: Eukaryotic Translation Elongation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTE0](https://www.uniprot.org/uniprotkb/Q5VTE0) (Putative elongation factor 1-alpha-like 3):

> This protein promotes the GTP-dependent binding of aminoacyl-tRNA to the A-site of ribosomes during protein biosynthesis.

**Summary**, from NCBI Gene [158078](https://www.ncbi.nlm.nih.gov/gene/158078):

> Predicted to enable GTPase activity and translation elongation factor activity. Predicted to be involved in translational elongation. Located in extracellular exosome; nucleus; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3200) · Entrez [158078](https://www.ncbi.nlm.nih.gov/gene/158078) · UniProt [Q5VTE0](https://www.uniprot.org/uniprotkb/Q5VTE0) · Ensembl [ENSG00000196205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196205)

## Data

Gene col 12154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12154); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12154]; `tensor/DDL_lfc|DDL_z.npy` [12154]; `embed/gene_vectors.npy` [12154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12154 or target_col == 12154). Every well: [[EEF1A1P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1A1P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
