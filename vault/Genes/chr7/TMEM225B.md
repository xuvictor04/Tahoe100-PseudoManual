---
symbol: "TMEM225B"
type: "gene"
col: 14396
ensembl_id: "ENSG00000244219"
name: "transmembrane protein 225B"
location: "7q22.1"
module: 37
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 43
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TMEM225B

*transmembrane protein 225B* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.59× (z +15.7, q 0e+00, up in 24 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.597× (z -4.7, q 0.002, down in 13 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0594×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (A-172 0.0686×); [[Macitentan (drug)]] 5 µM in 1 line (A-172 0.0823×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIWIL2]] (+0.82, fdr 7e-06), [[SNX31]] (+0.80, fdr 7e-06), [[CFAP53]] (+0.76, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[TFAP2E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.59×** | +15.7 | 0e+00 | 24/29 (C32, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +10.3 | 2e-22 | 16/24 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +8.9 | 1e-16 | 11/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +7.1 | 1e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.6 | 2e-06 | 7/20 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.1 | 3e-05 | 7/11 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.22×** | +3.8 | 0.013 | 5/31 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.5 | 0.034 | 2/16 (LoVo, C32) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.043 | 4/36 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.2 | 0.078 | 2/10 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.078 | 1/16 (A-172) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.079 | 1/35 (NCI-H1573) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.1 | 0.079 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.0 | 0.087 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.087 | 2/17 (A549, PANC-1) | inconsistent across doses |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.087 | 4/33 (J82, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14396.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0594×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (A-172 0.0686×); [[Macitentan (drug)]] 5 µM in 1 line (A-172 0.0823×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -4.7 | 0.002 | 13/34 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.649×** | -3.8 | 0.039 | 8/36 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.496× | -3.3 | 0.15 | 4/16 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.705× | -3.2 | 0.17 | 5/36 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.707× | -3.2 | 0.17 | 5/36 (A549, HT-29, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.706× | -3.1 | 0.18 | 7/36 (SW48, SW 900, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.719× | -3.0 | 0.18 | 5/34 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.719× | -3.0 | 0.18 | 3/34 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.41 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0594× (z -10.1) |
| [[C32 (line)]] | wt | 10.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.131× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.4) | — |
| [[A-427 (line)]] | wt | 0.977 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.618 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.230 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIWIL2]] | +0.82 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SNX31]] | +0.80 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[CCNP]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[WDR49]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.67 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[RRH]] | +0.67 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFAP2E]] | B | TMEM225B activity raises TFAP2E's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without TMEM225B | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[TPTE2]] | B | TMEM225B activity raises TPTE2's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without TMEM225B | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[MIR9-1HG]] | B | TMEM225B activity lowers MIR9-1HG's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 1.20× higher at baseline in the lines without TMEM225B | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[C1QTNF7-AS1]] | B | TMEM225B activity raises C1QTNF7-AS1's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without TMEM225B | 0.0997 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, -17.2); signed map (11.7, 5.0). **Vector** length 42.9, 5.32% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +15.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | -1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -4.7 |
|  | [[NG25 (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 225B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,598,267-99,611,045 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P0DP42](https://www.uniprot.org/uniprotkb/P0DP42) carries no function annotation.

**Summary**, from NCBI Gene [100289187](https://www.ncbi.nlm.nih.gov/gene/100289187):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:53075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53075) · Entrez [100289187](https://www.ncbi.nlm.nih.gov/gene/100289187) · UniProt [P0DP42](https://www.uniprot.org/uniprotkb/P0DP42) · Ensembl [ENSG00000244219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244219)

## Data

Gene col 14396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14396); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14396]; `tensor/DDL_lfc|DDL_z.npy` [14396]; `embed/gene_vectors.npy` [14396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14396 or target_col == 14396). Every well: [[TMEM225B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM225B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
