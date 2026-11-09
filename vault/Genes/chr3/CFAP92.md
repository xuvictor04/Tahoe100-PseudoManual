---
symbol: "CFAP92"
type: "gene"
col: 3573
ensembl_id: "ENSG00000114656"
name: "cilia and flagella associated protein 92 (putative)"
location: "3q21.3"
module: 75
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# CFAP92

*cilia and flagella associated protein 92 (putative)* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +20.9, q 0e+00, up in 30 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.634× (z -5.9, q 2e-06, down in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 0.169×, SW48 0.223×, KATO III 0.347×, HEC-1-A 0.320×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW48 0.111×, SHP-77 0.104×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW48 0.158×, SNU-1 0.158×); [[Panobinostat (drug)]] 5 µM in 1 line (SW48 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FER1L6]] (+0.68, fdr 1e-05), [[DNAJC9-AS1-1]] (+0.65, fdr 1e-05), [[LINC01811]] (+0.62, fdr 1e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +20.9 | 0e+00 | 30/37 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.6 | 3e-19 | 5/7 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +9.3 | 3e-18 | 26/45 (SW480, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +9.3 | 3e-18 | 3/11 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.3 | 1e-14 | 9/21 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +8.3 | 1e-14 | 24/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.6 | 4e-09 | 11/32 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +5.0 | 4e-05 | 15/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.001 | 15/38 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.34×** | +3.8 | 0.007 | 9/46 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.39×** | +3.8 | 0.009 | 2/22 (NCI-H1573, HT-29) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +3.5 | 0.019 | 6/39 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.031 | 4/44 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.031 | 5/45 (A-172, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.031 | 8/44 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.054 | 0/33 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.1 | 0.054 | 8/45 (PANC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 0.169×, SW48 0.223×, KATO III 0.347×, HEC-1-A 0.320×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW48 0.111×, SHP-77 0.104×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW48 0.158×, SNU-1 0.158×); [[Panobinostat (drug)]] 5 µM in 1 line (SW48 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -5.9 | 2e-06 | 16/45 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -5.0 | 1e-04 | 15/46 (SW48, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.710×** | -3.9 | 0.015 | 12/44 (SW48, SNU-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.785× | -3.2 | 0.22 | 12/45 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 70.7 | 0 | 10 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.107× (z -13.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.4) |
| [[A-427 (line)]] | wt | 9.50 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -10.8) |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.7) |
| [[A498 (line)]] | wt | 2.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 3.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 6.09 | 0 | 1 | — | [[Cilostazol (drug)]] 0.5 µM 0.0647× (z -8.6) |
| [[KATO III (line)]] | alt | 53.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.1) |
| [[SHP-77 (line)]] | alt | 8.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FER1L6]] | +0.68 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[DNAJC9-AS1-1]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[LINC01811]] | +0.62 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[KCNQ1]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ENPP7P4]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[LINC01956]] | +0.58 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[LINC02694]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CASC11]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PPP1R9A-AS1]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PEBP4]] | +0.57 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[ZNF503-AS1]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LRRC4C]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFAP92's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.3, 36.7); signed map (30.7, 11.2). **Vector** length 53.0, 6.37% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +20.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.3 | -3.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 92 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,909,866-129,002,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43738, FAP92; previously KIAA1257 |
| Matched by | ensembl_id |

UniProt [Q9ULG3](https://www.uniprot.org/uniprotkb/Q9ULG3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29231) · Entrez [57501](https://www.ncbi.nlm.nih.gov/gene/57501) · UniProt [Q9ULG3](https://www.uniprot.org/uniprotkb/Q9ULG3) · Ensembl [ENSG00000114656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114656)

## Data

Gene col 3573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3573); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3573]; `tensor/DDL_lfc|DDL_z.npy` [3573]; `embed/gene_vectors.npy` [3573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3573 or target_col == 3573). Every well: [[CFAP92 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP92.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
