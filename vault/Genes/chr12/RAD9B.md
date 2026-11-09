---
symbol: "RAD9B"
type: "gene"
col: 7493
ensembl_id: "ENSG00000151164"
name: "RAD9 checkpoint clamp component B"
location: "12q24.11"
module: 35
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RAD9B

*RAD9 checkpoint clamp component B* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.37× (z +20.5, q 0e+00, up in 25 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.181×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.0984×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.194×; ⚠ cell-cycle shift, explains ~17% of this change); [[Menadione (drug)]] 0.05 µM in 1 line (SW480 0.0896×); [[Orlistat (drug)]] 0.05 µM in 1 line (SW480 0.0939×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK4]] (+0.76, fdr 1e-05), [[NEK8]] (+0.75, fdr 8e-05), [[TMEM202-AS1]] (+0.74, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.37×** | +20.5 | 0e+00 | 25/26 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.4 | 1e-27 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +11.0 | 4e-26 | 16/28 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +10.4 | 4e-23 | 2/3 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +10.4 | 4e-23 | 7/9 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +8.5 | 2e-15 | 11/22 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +7.6 | 3e-12 | 3/8 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +6.9 | 4e-10 | 10/28 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.7 | 2e-09 | 7/43 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.9 | 3e-07 | 11/30 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.0 | 4e-05 | 1/16 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.62×** | +4.8 | 9e-05 | 2/15 (NCI-H2347, NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +4.3 | 9e-04 | 7/39 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 3/39 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +3.8 | 0.007 | 1/3 (HEC-1-A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 3/42 (NCI-H2347, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.009 | 5/43 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.093 | 3/43 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7493.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.181×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.0984×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.194×; ⚠ cell-cycle shift, explains ~17% of this change); [[Menadione (drug)]] 0.05 µM in 1 line (SW480 0.0896×); [[Orlistat (drug)]] 0.05 µM in 1 line (SW480 0.0939×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.704× | -3.5 | 0.16 | 11/38 (PANC-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.706× | -3.4 | 0.16 | 8/43 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.719× | -3.3 | 0.20 | 6/42 (RPMI-7951, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.20 | 13/40 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.546× | -3.1 | 0.20 | 4/38 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.20 | 0 | 3 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0984× (z -9.0) |
| [[PANC-1 (line)]] | alt | 3.88 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.799 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK4]] | +0.76 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[NEK8]] | +0.75 | +0.75 / +0.37 | both halves | 8e-05 |  |
| [[TMEM202-AS1]] | +0.74 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.74 | +0.68 / +0.57 | both halves | 8e-06 |  |
| [[DDX19A-DT]] | +0.74 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZCWPW1]] | +0.74 | +0.74 / +0.31 | both halves | 2e-04 |  |
| [[ATE1OSP]] | +0.73 | +0.73 / +0.40 | both halves | 5e-05 |  |
| [[SEPTIN7-DT]] | +0.72 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[FAM174B]] | +0.72 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[LINC00863]] | +0.72 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[BAAT]] | +0.72 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PJVK]] | +0.72 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAD9B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.9, 20.9); signed map (26.1, -4.9). **Vector** length 45.8, 5.32% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.0 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RAD9 checkpoint clamp component B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,501,655-110,533,556 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40346 |
| Reactome | 21 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; HDR through Single Strand Annealing (SSA) |
| Matched by | ensembl_id |

UniProt [Q6WBX8](https://www.uniprot.org/uniprotkb/Q6WBX8) carries no function annotation.

**Summary**, from NCBI Gene [144715](https://www.ncbi.nlm.nih.gov/gene/144715):

> Predicted to be involved in DNA integrity checkpoint signaling; DNA repair; and cellular response to ionizing radiation. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21700) · Entrez [144715](https://www.ncbi.nlm.nih.gov/gene/144715) · UniProt [Q6WBX8](https://www.uniprot.org/uniprotkb/Q6WBX8) · Ensembl [ENSG00000151164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151164)

## Data

Gene col 7493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7493); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7493]; `tensor/DDL_lfc|DDL_z.npy` [7493]; `embed/gene_vectors.npy` [7493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7493 or target_col == 7493). Every well: [[RAD9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
