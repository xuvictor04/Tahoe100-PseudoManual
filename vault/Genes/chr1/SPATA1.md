---
symbol: "SPATA1"
type: "gene"
col: 4337
ensembl_id: "ENSG00000122432"
name: "spermatogenesis associated 1"
location: "1p22.3"
module: 21
arm: "+"
pooled_cpm: 3.94
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPATA1

*spermatogenesis associated 1* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.22× (z +27.1, q 0e+00, up in 38 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (NCI-H2030 0.0825×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H2347 0.0826×); [[Digitoxin (drug)]] 0.05 µM in 1 line (A-172 0.0916×; ⚠ cell-cycle shift, explains ~14% of this change); [[IQ 1 (drug)]] 0.5 µM in 1 line (LoVo 0.0479×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF451-AS1]] (+0.84, fdr 7e-06), [[DENND6A-AS1]] (+0.83, fdr 7e-06), [[LANCL1-AS1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.22×** | +27.1 | 0e+00 | 38/39 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +10.5 | 2e-23 | 7/10 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +9.6 | 2e-19 | 22/33 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +8.7 | 6e-16 | 20/36 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.3 | 1e-14 | 16/22 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +7.1 | 1e-10 | 14/22 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.5 | 6e-09 | 5/8 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +6.0 | 1e-07 | 13/46 (HS-578T, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +5.4 | 4e-06 | 1/7 (CFPAC-1) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +4.9 | 5e-05 | 18/42 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.9 | 0.006 | 9/24 (SNU-423, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.010 | 12/38 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 11/45 (HOP62, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.018 | 9/36 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.3 | 0.031 | 8/37 (RPMI-7951, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4337.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (NCI-H2030 0.0825×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H2347 0.0826×); [[Digitoxin (drug)]] 0.05 µM in 1 line (A-172 0.0916×; ⚠ cell-cycle shift, explains ~14% of this change); [[IQ 1 (drug)]] 0.5 µM in 1 line (LoVo 0.0479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | 0.713× | -3.4 | 0.39 | 7/43 (J82, A549, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.41 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +9.3) | [[Digitoxin (drug)]] 0.05 µM 0.0916× (z -8.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[LoVo (line)]] | wt | 3.29 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +10.5) | [[IQ 1 (drug)]] 0.5 µM 0.0479× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.15 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +10.4) | [[Pemetrexed (drug)]] 5 µM 0.0825× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 3.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +11.4) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0826× (z -9.3) |
| [[A498 (line)]] | wt | 3.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 3.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 2.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.1× (z +9.7) | — |
| [[C32 (line)]] | wt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 4.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.10× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 6.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 5.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 7.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 3.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 4.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.9) | — |
| [[SW480 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +11.1) | — |
| [[A-427 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451-AS1]] | +0.84 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.83 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.82 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.81 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.81 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[PPP1R42]] | +0.80 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[OOEP]] | +0.80 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[PSMD14-DT]] | +0.79 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.79 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.78 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.78 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[MED28-DT]] | +0.78 | +0.64 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPATA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, 23.9); signed map (30.5, -0.2). **Vector** length 57.6, 8.01% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +27.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,506,300-84,567,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SP-2 |
| Matched by | ensembl_id |

UniProt [Q5VX52](https://www.uniprot.org/uniprotkb/Q5VX52) carries no function annotation.

**Summary**, from NCBI Gene [100505741](https://www.ncbi.nlm.nih.gov/gene/100505741):

> Predicted to be located in acrosomal vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14682) · Entrez [100505741](https://www.ncbi.nlm.nih.gov/gene/100505741) · UniProt [Q5VX52](https://www.uniprot.org/uniprotkb/Q5VX52) · Ensembl [ENSG00000122432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122432)

## Data

Gene col 4337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4337); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4337]; `tensor/DDL_lfc|DDL_z.npy` [4337]; `embed/gene_vectors.npy` [4337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4337 or target_col == 4337). Every well: [[SPATA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
