---
symbol: "POLR3K"
type: "gene"
col: 8467
ensembl_id: "ENSG00000161980"
name: "RNA polymerase III subunit K"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 5.17
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# POLR3K

*RNA polymerase III subunit K* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.57× (z +12.6, q 1e-33, up in 22 of 22 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.94× (z +4.9, q 7e-05, up in 25 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 0.5 µM in 1 line (HT-29 0.147×; ⚠ unreliable plate only); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.278×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAUS7]] (+0.69, fdr 2e-05), [[DCTPP1]] (+0.69, fdr 1e-05), [[MRPL12]] (+0.67, fdr 4e-05); moves opposite to [[RBM3]] (-0.61, fdr 9e-05), [[PCBP2]] (-0.59, fdr 5e-05), [[RNF11]] (-0.59, fdr 1e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **5.57×** | +12.6 | 1e-33 | 22/22 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **4.86×** | +11.6 | 1e-28 | 45/46 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **4.95×** | +11.3 | 3e-27 | 6/7 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **4.25×** | +10.6 | 3e-24 | 45/46 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **3.75×** | +9.7 | 4e-20 | 45/46 (SW480, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.85×** | +7.4 | 1e-11 | 21/27 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.94×** | +7.3 | 2e-11 | 10/11 (SW480, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.12×** | +5.3 | 8e-06 | 28/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.96×** | +4.9 | 5e-05 | 19/40 (A-172, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +4.9 | 7e-05 | 25/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.87×** | +4.6 | 2e-04 | 19/38 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +4.2 | 0.001 | 20/45 (NCI-H460, H4, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.50×** | +4.2 | 0.001 | 15/40 (A549, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.49×** | +4.1 | 0.002 | 21/45 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **1.74×** | +3.9 | 0.004 | 12/29 (NCI-H1573, Hs 766T, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.012 | 14/41 (C32, LoVo, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **2.16×** | +3.0 | 0.084 | 2/26 (A498, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.87×** | +2.9 | 0.089 | 7/37 (PANC-1, HCT15, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.089 | 14/45 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8467.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 0.5 µM in 1 line (HT-29 0.147×; ⚠ unreliable plate only); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.278×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.585× | -3.7 | 0.15 | 15/46 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.638× | -3.0 | 0.53 | 13/47 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.04 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.86 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[PANC-1 (line)]] | alt | 8.11 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[A498 (line)]] | wt | 8.01 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 9.17 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.147× (z -9.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 15 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS7]] | +0.69 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[DCTPP1]] | +0.69 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[MRPL12]] | +0.67 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[TMEM201]] | +0.66 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.65 | +0.31 / +0.64 | both halves | 2e-04 | STRING 689; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[PWP2]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[PAXX]] ⚠ | +0.63 | +0.28 / +0.66 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CISD3]] | +0.62 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[POP5]] | +0.61 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[SLC39A3]] | +0.60 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[PGP]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PUSL1]] | +0.60 | +0.26 / +0.57 | both halves | 3e-04 |  |
| [[HMBS]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MCM10]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM3]] | -0.61 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[PCBP2]] | -0.59 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[RNF11]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[GNAS]] | -0.56 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[CSDE1]] | -0.56 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[PRCP]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LHFPL3]] | -0.53 | -0.25 / -0.29 | both halves | 4e-04 |  |
| [[RAB21]] | -0.53 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[AP2B1]] | -0.53 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[TMEM106B]] | -0.52 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[C8orf44-SGK3]] | -0.51 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[CHD3]] | -0.50 | -0.19 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[OSER1-DT]] | -0.50 | -0.32 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises POLR3K's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without CDC25A | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, -42.7); signed map (-11.2, -53.4). **Vector** length 55.8, 9.29% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.8 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.3 | +10.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.0 | +9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | +3.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +2.0 | +12.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:46,407-53,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPC11, C11 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Y1](https://www.uniprot.org/uniprotkb/Q9Y2Y1) (DNA-directed RNA polymerase III subunit RPC10):

> Core component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs using the four ribonucleoside triphosphates as substrates. Can mediate Pol I proofreading of the nascent RNA transcript. Anchors into the Pol III active site to constantly monitor transcription fidelity, cleaves mis-incorporated 5'-ribonucleotides and restarts the transcription process. Once Pol III reaches the poly(dT) termination signal, can induce Pol III clamp opening and transcription termination (By …

**Summary**, from NCBI Gene [51728](https://www.ncbi.nlm.nih.gov/gene/51728):

> This gene encodes a small essential subunit of RNA polymerase III, the polymerase responsible for synthesizing transfer and small ribosomal RNAs in eukaryotes. The carboxy-terminal domain of this subunit shares a high degree of sequence similarity to the carboxy-terminal domain of an RNA polymerase II elongation factor. This similarity in sequence is supported by functional studies showing that this subunit is required for proper pausing and termination during transcription. Pseudogenes of this …

**Accessions** — [HGNC:14121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14121) · Entrez [51728](https://www.ncbi.nlm.nih.gov/gene/51728) · UniProt [Q9Y2Y1](https://www.uniprot.org/uniprotkb/Q9Y2Y1) · Ensembl [ENSG00000161980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161980)

## Data

Gene col 8467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8467); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8467]; `tensor/DDL_lfc|DDL_z.npy` [8467]; `embed/gene_vectors.npy` [8467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8467 or target_col == 8467). Every well: [[POLR3K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
