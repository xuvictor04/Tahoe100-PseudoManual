---
symbol: "IL18BP"
type: "gene"
col: 6023
ensembl_id: "ENSG00000137496"
name: "interleukin 18 binding protein"
location: "11q13.4"
module: 20
arm: "+"
pooled_cpm: 7.68
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IL18BP

*interleukin 18 binding protein* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +6.2, q 2e-07, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.520× (z -6.0, q 1e-06, down in 26 of 46 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HT-29 0.0420×, LoVo 0.0610×, A549 0.0634×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Hesperidin (drug)]] 0.5 µM in 1 line (SNU-423 0.0543×); [[crizotinib (drug)]] 0.05 µM in 1 line (HS-578T 0.110×); [[Thymol (drug)]] 0.5 µM in 1 line (A-427 0.0816×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNIP2]] (+0.71, fdr 1e-05), [[LY6G5B]] (+0.71, fdr 1e-05), [[SPTLC1]] (+0.69, fdr 2e-05); moves opposite to [[FAM133B]] (-0.64, fdr 2e-05), [[C17orf58]] (-0.62, fdr 3e-05), [[MTLN]] (-0.62, fdr 3e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[HPF1]] (-0.61, fdr 5e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.2 | 2e-07 | 30/43 (SW 900, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.5 | 1e-05 | 7/14 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.2 | 0.004 | 9/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.2 | 0.004 | 10/23 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.009 | 15/45 (SW 900, NCI-H2030, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.026 | 13/47 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.061 | 16/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.075 | 13/39 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 11/43 (A549, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.38× | +3.0 | 0.14 | 8/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6023.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HT-29 0.0420×, LoVo 0.0610×, A549 0.0634×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Hesperidin (drug)]] 0.5 µM in 1 line (SNU-423 0.0543×); [[crizotinib (drug)]] 0.05 µM in 1 line (HS-578T 0.110×); [[Thymol (drug)]] 0.5 µM in 1 line (A-427 0.0816×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.520×** | -6.0 | 1e-06 | 26/46 (A-427, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.645×** | -4.2 | 0.008 | 20/46 (SW480, A-427, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.84 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0634× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Oxaprozin (drug)]] 0.5 µM 0.101× (z -8.8) |
| [[A-427 (line)]] | wt | 6.46 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0816× (z -9.7) |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0827× (z -9.1) |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.110× (z -10.1) |
| [[HT-29 (line)]] | alt | 8.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0420× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.54 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0857× (z -8.9) |
| [[LoVo (line)]] | wt | 6.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0610× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.108× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 4.45 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0978× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 7.85 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0782× (z -8.9) |
| [[SNU-423 (line)]] | alt | 7.19 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0543× (z -11.5) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNIP2]] | +0.71 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.71 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[SPTLC1]] | +0.69 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[AGBL5]] | +0.62 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[MKRN5P]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HCFC1]] | +0.62 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[RPN1]] | +0.61 | +0.30 / +0.68 | both halves | 2e-04 |  |
| [[MC1R]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[EOLA2-DT]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.60 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[GOLGA3]] | +0.59 | +0.37 / +0.72 | both halves | 8e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM133B]] | -0.64 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[C17orf58]] | -0.62 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[MTLN]] ⚠ | -0.62 | -0.44 / -0.61 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HPF1]] | -0.61 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[PET117]] | -0.60 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[MRPL57]] | -0.59 | -0.21 / -0.64 | both halves | 7e-04 |  |
| [[KBTBD6]] | -0.59 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[GTF2H5]] | -0.57 | -0.19 / -0.63 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ATP5PO]] ⚠ | -0.57 | -0.36 / -0.53 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PITPNA-AS1]] | -0.56 | -0.24 / -0.55 | both halves | 4e-04 |  |
| [[RP9]] | -0.55 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[ZNF30]] | -0.55 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[NUDCD2]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ISCA2]] | -0.54 | -0.20 / -0.61 | both halves | 7e-04 |  |
| [[DMAC1]] | -0.53 | -0.27 / -0.61 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IL18BP's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.9, -25.1); signed map (-17.1, -33.1). **Vector** length 63.4, 9.45% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.3 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 18 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:71,998,613-72,007,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL18BPa |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Interleukin-18 signaling; Interleukin-37 signaling; Interleukin-1 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O95998](https://www.uniprot.org/uniprotkb/O95998) (Interleukin-18-binding protein):

> Isoform A binds to IL-18 and inhibits its activity. Functions as an inhibitor of the early TH1 cytokine response.

**Summary**, from NCBI Gene [10068](https://www.ncbi.nlm.nih.gov/gene/10068):

> The protein encoded by this gene functions as an inhibitor of the proinflammatory cytokine, IL18. It binds IL18, prevents the binding of IL18 to its receptor, and thus inhibits IL18-induced IFN-gamma production, resulting in reduced T-helper type 1 immune responses. This protein is constitutively expressed and secreted in mononuclear cells. Elevated level of this protein is detected in the intestinal tissues of patients with Crohn's disease. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:5987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5987) · Entrez [10068](https://www.ncbi.nlm.nih.gov/gene/10068) · UniProt [O95998](https://www.uniprot.org/uniprotkb/O95998) · Ensembl [ENSG00000137496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137496)

## Data

Gene col 6023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6023); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6023]; `tensor/DDL_lfc|DDL_z.npy` [6023]; `embed/gene_vectors.npy` [6023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6023 or target_col == 6023). Every well: [[IL18BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL18BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
