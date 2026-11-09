---
symbol: "FEM1A"
type: "gene"
col: 6584
ensembl_id: "ENSG00000141965"
name: "fem-1 homolog A"
location: "19p13.3"
module: 7
arm: "+"
pooled_cpm: 8.25
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# FEM1A

*fem-1 homolog A* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +12.3, q 6e-32, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.678× (z -4.8, q 0.001, down in 20 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LS 180 0.0808×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.152×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (BT-474 0.0841×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0836×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM15B]] (+0.78, fdr 7e-06), [[ZNF629]] (+0.77, fdr 7e-06), [[TSSC4]] (+0.76, fdr 7e-06); moves opposite to [[HSPB11]] (-0.65, fdr 2e-05), [[HDAC3]] (-0.64, fdr 2e-05), [[PPP1R2]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PATZ1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +12.3 | 6e-32 | 34/45 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +10.5 | 2e-23 | 30/35 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +7.9 | 4e-13 | 31/43 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +6.6 | 6e-09 | 30/47 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.6 | 6e-09 | 15/23 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +5.8 | 6e-07 | 22/43 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 22/44 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +5.5 | 2e-06 | 21/46 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.4 | 4e-06 | 17/46 (A498, HS-578T, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +5.3 | 5e-06 | 15/36 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +4.5 | 3e-04 | 20/46 (A498, HS-578T, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 9e-04 | 15/48 (HEC-1-A, SW 900, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.1 | 0.002 | 12/47 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 15/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 10/47 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.017 | 14/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.059 | 8/40 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.075 | 4/39 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.075 | 11/45 (SNU-423, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LS 180 0.0808×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.152×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (BT-474 0.0841×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0836×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.678×** | -4.8 | 0.001 | 20/46 (BT-474, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0841× (z -9.4) |
| [[HS-578T (line)]] | alt | 7.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 6.21 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0836× (z -8.9) |
| [[LoVo (line)]] | wt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0808× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 7.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H460 (line)]] | wt | 5.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.2) | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM15B]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.77 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TSSC4]] | +0.76 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.75 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[EXOSC6]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[INTS14]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[YTHDF2]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.72 | +0.78 / +0.57 | both halves | 9e-06 |  |
| [[GTF3C4]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[NIP7]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MRPL50]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | -0.65 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[HDAC3]] | -0.64 | -0.69 / -0.46 | both halves | 2e-05 |  |
| [[PPP1R2]] | -0.63 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[ARL3]] | -0.61 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[SRP54-AS1]] | -0.61 | -0.70 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATZ1]] | C | PATZ1's natural level weakens FEM1A's drug response | PATZ1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.37; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.4, 10.3); signed map (-2.6, -26.4). **Vector** length 68.0, 10.8% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | fem-1 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,791,734-4,801,273 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSK4](https://www.uniprot.org/uniprotkb/Q9BSK4) (Protein fem-1 homolog A):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL2(FEM1A) complex …

**Summary**, from NCBI Gene [55527](https://www.ncbi.nlm.nih.gov/gene/55527):

> Enables EP4 subtype prostaglandin E2 receptor binding activity and ubiquitin-like ligase-substrate adaptor activity. Involved in negative regulation of inflammatory response and ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Located in Golgi apparatus and nucleoplasm. Part of Cul2-RING ubiquitin ligase complex. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16934) · Entrez [55527](https://www.ncbi.nlm.nih.gov/gene/55527) · UniProt [Q9BSK4](https://www.uniprot.org/uniprotkb/Q9BSK4) · Ensembl [ENSG00000141965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141965)

## Data

Gene col 6584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6584); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6584]; `tensor/DDL_lfc|DDL_z.npy` [6584]; `embed/gene_vectors.npy` [6584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6584 or target_col == 6584). Every well: [[FEM1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FEM1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
