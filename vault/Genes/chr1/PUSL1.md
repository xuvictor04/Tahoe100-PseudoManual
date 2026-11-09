---
symbol: "PUSL1"
type: "gene"
col: 9885
ensembl_id: "ENSG00000169972"
name: "pseudouridine synthase like 1"
location: "1p36.33"
module: 58
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# PUSL1

*pseudouridine synthase like 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.19× (z +8.3, q 7e-14, up in 37 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Busulfan (drug)]] 5 µM in 1 line (NCI-H460 0.141×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANTKMT]] (+0.75, fdr 3e-05), [[NAA10]] (+0.73, fdr 5e-05, ⚠ NAA10 in the vector space only through flagged drug-doses), [[WRAP73]] (+0.72, fdr 5e-05), [[STUB1]] (+0.71, fdr 3e-05); moves opposite to [[VPS52]] (-0.69, fdr 1e-04), [[CYB5D2]] (-0.67, fdr 1e-04), [[PNISR-AS1]] (-0.66, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.19×** | +8.3 | 7e-14 | 37/42 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.66×** | +7.0 | 8e-10 | 34/46 (SW480, AsPC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.58×** | +6.8 | 3e-09 | 33/45 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.35×** | +5.9 | 7e-07 | 2/6 (A498, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.25×** | +5.8 | 9e-07 | 8/16 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.06×** | +5.2 | 2e-05 | 12/20 (LS 180, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.3 | 0.002 | 7/19 (SHP-77, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.85×** | +4.0 | 0.004 | 3/9 (J82, A498, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.78×** | +3.9 | 0.005 | 11/24 (J82, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.013 | 17/41 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.031 | 12/35 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.35×** | +3.2 | 0.069 | 5/37 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.1 | 0.082 | 5/47 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9885.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Busulfan (drug)]] 5 µM in 1 line (NCI-H460 0.141×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.387× | -3.5 | 0.18 | 15/40 (HT-29, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.714× | -3.4 | 0.18 | 17/34 (C32, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 6.16 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 1 | — | [[Busulfan (drug)]] 5 µM 0.141× (z -8.8) |
| [[A-172 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 13 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTKMT]] | +0.75 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[NAA10]] ⚠ | +0.73 | +0.40 / +0.64 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WRAP73]] | +0.72 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[STUB1]] | +0.71 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.69 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[SSNA1]] | +0.69 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[MRPL41]] ⚠ | +0.69 | +0.47 / +0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC4]] | +0.69 | +0.42 / +0.74 | both halves | 4e-05 |  |
| [[MRPL17]] | +0.69 | +0.36 / +0.61 | both halves | 9e-05 | STRING 791 |
| [[PAXX]] ⚠ | +0.69 | +0.45 / +0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCNQ]] | +0.68 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MRPS34]] | +0.68 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[POLR2I]] | +0.67 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[MRPL55]] | +0.67 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[SLC39A3]] | +0.67 | +0.33 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | -0.69 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CYB5D2]] | -0.67 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.66 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[ACADM]] | -0.65 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[CROCC]] | -0.65 | -0.23 / -0.58 | both halves | 5e-04 |  |
| [[BHLHE40-AS1]] | -0.65 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[DDX39B]] | -0.64 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[KRBA2]] | -0.62 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[PBLD]] | -0.61 | -0.34 / -0.23 | both halves | 5e-04 |  |
| [[DRAIC]] | -0.61 | -0.49 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[AP4S1]] | -0.61 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[PAPOLA]] | -0.61 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[CHD3]] | -0.60 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises PUSL1's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without HES6 | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.4, -15.3); signed map (-31.9, 3.4). **Vector** length 51.4, 7.67% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.1 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.9 | +6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | +1.5 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.0 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -2.4 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -2.2 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine synthase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,308,597-1,311,677 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90811 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0Z8](https://www.uniprot.org/uniprotkb/Q8N0Z8) (tRNA pseudouridine synthase-like 1):

> Pseudouridylate synthase that catalyzes the conversion of uridine to pseudouridine in mitochondrial tRNAs. Acts on position 38/39/40 in the anticodon stem of mitochondrial tRNAs.

**Summary**, from NCBI Gene [126789](https://www.ncbi.nlm.nih.gov/gene/126789):

> Predicted to enable pseudouridine synthase activity. Predicted to be involved in tRNA pseudouridine synthesis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26914) · Entrez [126789](https://www.ncbi.nlm.nih.gov/gene/126789) · UniProt [Q8N0Z8](https://www.uniprot.org/uniprotkb/Q8N0Z8) · Ensembl [ENSG00000169972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169972)

## Data

Gene col 9885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9885); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9885]; `tensor/DDL_lfc|DDL_z.npy` [9885]; `embed/gene_vectors.npy` [9885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9885 or target_col == 9885). Every well: [[PUSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
