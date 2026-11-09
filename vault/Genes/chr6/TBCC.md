---
symbol: "TBCC"
type: "gene"
col: 4557
ensembl_id: "ENSG00000124659"
name: "tubulin folding cofactor C"
location: "6p21.1"
module: 11
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TBCC

*tubulin folding cofactor C* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +10.7, q 6e-24, up in 36 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (A-172 0.0736×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.112×); [[Busulfan (drug)]] 0.5 µM in 1 line (SHP-77 0.0750×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOPORS]] (+0.81, fdr 7e-06), [[MAD2L1BP]] (+0.76, fdr 7e-06), [[EID2]] (+0.73, fdr 7e-06); moves opposite to [[EIF2S3]] (-0.65, fdr 1e-05), [[CPSF6]] (-0.63, fdr 1e-05), [[MTFR1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +10.7 | 6e-24 | 36/40 (HOP62, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.05×** | +9.7 | 1e-19 | 32/40 (HS-578T, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +8.2 | 4e-14 | 34/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +7.5 | 8e-12 | 22/31 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.17×** | +7.4 | 2e-11 | 39/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +6.7 | 2e-09 | 31/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +6.6 | 3e-09 | 26/40 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +6.2 | 3e-08 | 31/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.8 | 5e-07 | 28/48 (SNU-423, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.74×** | +5.3 | 8e-06 | 24/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.9 | 4e-05 | 20/46 (A498, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.58×** | +4.4 | 6e-04 | 16/32 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 16/37 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.48×** | +3.7 | 0.008 | 8/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.4 | 0.022 | 7/38 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.054 | 10/40 (SW480, BT-474, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (A-172 0.0736×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.112×); [[Busulfan (drug)]] 0.5 µM in 1 line (SHP-77 0.0750×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.685× | -3.5 | 0.20 | 11/34 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.779× | -3.4 | 0.20 | 9/47 (SNU-1, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.725× | -3.1 | 0.39 | 15/30 (KATO III, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.66 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0736× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 7.04 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.133× (z -8.8) |
| [[HT-29 (line)]] | alt | 5.77 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0973× (z -9.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 7.11 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.112× (z -9.3) |
| [[SHP-77 (line)]] | alt | 5.69 | 0 | 1 | — | [[Busulfan (drug)]] 0.5 µM 0.0750× (z -9.3) |
| [[SW1417 (line)]] | alt | 8.80 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.157× (z -8.6) |
| [[A-427 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOPORS]] | +0.81 | +0.75 / +0.88 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.76 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[EID2]] | +0.73 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[LENG1]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.73 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[CPT2]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[KBTBD4]] | +0.72 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SCAND1]] | +0.72 | +0.58 / +0.80 | both halves | 7e-06 |  |
| [[ABT1]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[DPF2]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[USP27X]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S3]] | -0.65 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.63 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[MTFR1]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.62 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.59 | -0.62 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBCC's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.2, 5.2); signed map (2.7, -17.8). **Vector** length 64.2, 10.5% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.4 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tubulin folding cofactor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,744,498-42,746,103 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CFC |
| Reactome | 2 pathways, smallest: Post-chaperonin tubulin folding pathway; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15814](https://www.uniprot.org/uniprotkb/Q15814) (Tubulin-specific chaperone C):

> Tubulin-folding protein; involved in the final step of the tubulin folding pathway.

**Summary**, from NCBI Gene [6903](https://www.ncbi.nlm.nih.gov/gene/6903):

> Cofactor C is one of four proteins (cofactors A, D, E, and C) involved in the pathway leading to correctly folded beta-tubulin from folding intermediates. Cofactors A and D are believed to play a role in capturing and stabilizing beta-tubulin intermediates in a quasi-native confirmation. Cofactor E binds to the cofactor D/beta-tubulin complex; interaction with cofactor C then causes the release of beta-tubulin polypeptides that are committed to the native state. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11580) · Entrez [6903](https://www.ncbi.nlm.nih.gov/gene/6903) · UniProt [Q15814](https://www.uniprot.org/uniprotkb/Q15814) · Ensembl [ENSG00000124659](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124659)

## Data

Gene col 4557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4557); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4557]; `tensor/DDL_lfc|DDL_z.npy` [4557]; `embed/gene_vectors.npy` [4557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4557 or target_col == 4557). Every well: [[TBCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
