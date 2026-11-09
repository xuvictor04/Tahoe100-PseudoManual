---
symbol: "FAM177B"
type: "gene"
col: 12410
ensembl_id: "ENSG00000197520"
name: "family with sequence similarity 177 member B"
location: "1q41"
module: 21
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# FAM177B

*family with sequence similarity 177 member B* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.99× (z +16.5, q 0e+00, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.560× (z -5.0, q 4e-04, down in 15 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0790×; ⚠ cell-cycle shift, explains ~42% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.0927×; ⚠ cell-cycle shift, explains ~92% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.135×; ⚠ cell-cycle shift, explains ~16% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.345×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (COLO 205 0.224×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC3A1]] (+0.68, fdr 1e-05), [[PPP1R42]] (+0.67, fdr 1e-05), [[MYLK3]] (+0.65, fdr 1e-05); moves opposite to [[INPP4A]] (-0.57, fdr 4e-05), [[HERC2]] (-0.56, fdr 4e-05), [[MSH5]] (-0.56, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADGRG7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.99×** | +16.5 | 0e+00 | 23/28 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +7.6 | 9e-12 | 13/31 (NCI-H2030, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.1 | 2e-10 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +6.5 | 9e-09 | 5/12 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +6.4 | 2e-08 | 11/42 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.5 | 3e-06 | 5/23 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.5 | 3e-06 | 2/11 (HOP62, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.005 | 12/36 (A-172, HT-29, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.005 | 3/44 (SW480, NCI-H460, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.017 | 7/38 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.6 | 0.020 | 5/45 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.061 | 5/41 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.2 | 0.063 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12410.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0790×; ⚠ cell-cycle shift, explains ~42% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.0927×; ⚠ cell-cycle shift, explains ~92% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.135×; ⚠ cell-cycle shift, explains ~16% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.345×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (COLO 205 0.224×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -5.0 | 4e-04 | 15/36 (COLO 205, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.624×** | -4.0 | 0.015 | 12/40 (COLO 205, NCI-H1792, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.689× | -3.1 | 0.37 | 4/33 (LoVo, COLO 205, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.782× | -3.0 | 0.37 | 7/39 (COLO 205, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 108 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0790× (z -16.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.8) |
| [[A-172 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.892 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC3A1]] | +0.68 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[PPP1R42]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MYLK3]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[STX17-DT]] | +0.64 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[OOEP]] | +0.64 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PLA2G12B]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[RSPH9]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[N4BP2L1]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[HOXA-AS2]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[IL34]] | +0.60 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4A]] | -0.57 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[HERC2]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[MSH5]] | -0.56 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ICMT]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SPATA5]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[EXOC2]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG7]] | B | ADGRG7 activity raises FAM177B's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.29× lower at baseline in the lines without ADGRG7 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[TOP2A]] | B | TOP2A activity lowers FAM177B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, 24.2); signed map (31.3, -0.2). **Vector** length 50.1, 6.67% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -1.5 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 177 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,737,202-222,751,004 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-452F19.2, FLJ43505 |
| Matched by | ensembl_id |

UniProt [A6PVY3](https://www.uniprot.org/uniprotkb/A6PVY3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34395) · Entrez [400823](https://www.ncbi.nlm.nih.gov/gene/400823) · UniProt [A6PVY3](https://www.uniprot.org/uniprotkb/A6PVY3) · Ensembl [ENSG00000197520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197520)

## Data

Gene col 12410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12410); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12410]; `tensor/DDL_lfc|DDL_z.npy` [12410]; `embed/gene_vectors.npy` [12410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12410 or target_col == 12410). Every well: [[FAM177B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM177B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
