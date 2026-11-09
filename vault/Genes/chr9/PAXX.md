---
symbol: "PAXX"
type: "gene"
col: 7275
ensembl_id: "ENSG00000148362"
name: "PAXX non-homologous end joining factor"
location: "9q34.3"
module: 58
arm: "+"
pooled_cpm: 6.59
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# PAXX

*PAXX non-homologous end joining factor* — 9q34.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.64× (z +10.4, q 8e-23, up in 24 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 9.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (HS-578T 0.0729×).
> Its strongest partners by |cos| (61 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 44 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANTKMT]] (+0.71, fdr 2e-04), [[ATP5F1D]] (+0.70, fdr 1e-04, ⚠ ATP5F1D in the vector space only through flagged drug-doses), [[PUSL1]] (+0.69, fdr 3e-05), [[POLR2I]] (+0.68, fdr 1e-04); moves opposite to [[PAPOLA]] (-0.58, fdr 1e-04), [[UHMK1]] (-0.58, fdr 2e-04), [[EIF4G2]] (-0.57, fdr 0.002, ⚠ not reproduced), [[SETD7]] (-0.55, fdr 5e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 13 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 9.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **4.64×** | +10.4 | 8e-23 | 24/26 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **3.32×** | +7.8 | 1e-12 | 12/13 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.71×** | +6.3 | 7e-08 | 16/19 (LS 180, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **2.15×** | +5.2 | 3e-05 | 23/33 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.93×** | +4.5 | 1e-03 | 25/47 (SW480, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.86×** | +4.2 | 0.002 | 21/46 (SW480, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.78×** | +3.9 | 0.008 | 17/39 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.72×** | +3.7 | 0.016 | 20/46 (SW480, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.74×** | +3.6 | 0.018 | 16/33 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.65×** | +3.4 | 0.036 | 13/41 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.68×** | +3.4 | 0.036 | 16/45 (HEC-1-A, KATO III, …) | rises with dose | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.2 | 0.075 | 12/40 (A-172, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.0 | 0.10 | 11/29 (SHP-77, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (HS-578T 0.0729×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.613× | -3.1 | 0.41 | 10/47 (LS 180, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.11 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0729× (z -8.7) |
| [[LoVo (line)]] | wt | 6.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 38 of them with an alert (⚠; 33 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTKMT]] | +0.71 | +0.30 / +0.68 | both halves | 2e-04 |  |
| [[ATP5F1D]] ⚠ | +0.70 | +0.33 / +0.68 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PUSL1]] | +0.69 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[POLR2I]] | +0.68 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[NME3]] | +0.67 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[SSNA1]] | +0.66 | +0.29 / +0.65 | both halves | 3e-04 |  |
| [[NAA10]] ⚠ | +0.65 | +0.34 / +0.60 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PAFAH1B3]] | +0.65 | +0.25 / +0.58 | both halves | 4e-04 |  |
| [[NUDT8]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[SIGIRR]] | +0.64 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[POLR3K]] | +0.63 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[NTHL1]] | +0.62 | +0.25 / +0.63 | both halves | 4e-04 |  |
| [[TMEM256]] | +0.62 | +0.25 / +0.54 | both halves | 4e-04 |  |
| [[CDKN2D]] | +0.61 | +0.35 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPOLA]] | -0.58 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[UHMK1]] | -0.58 | -0.29 / -0.62 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.57 | -0.13 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[SETD7]] | -0.55 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[PDCD6IP-DT]] | -0.55 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[MKRN5P]] | -0.54 | -0.19 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[MOB1A]] | -0.54 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[BECN1]] | -0.54 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[AP5M1]] | -0.54 | -0.27 / -0.25 | both halves | 4e-04 |  |
| [[SMU1]] | -0.53 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.53 | -0.15 / -0.28 | ⚠ not reproduced | 0.001 |  |
| [[RCN1]] | -0.52 | -0.18 / -0.43 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises PAXX's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without HES6 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-47.4, -15.5); signed map (-31.8, 4.6). **Vector** length 51.9, 9.55% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.1 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +2.7 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +2.7 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +2.2 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | +2.2 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PAXX non-homologous end joining factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,992,422-136,993,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XLS; previously C9orf142 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUH6](https://www.uniprot.org/uniprotkb/Q9BUH6) (Protein PAXX):

> Non-essential DNA repair protein involved in DNA non-homologous end joining (NHEJ); participates in double-strand break (DSB) repair and V(D)J recombination. May act as a scaffold required for accumulation of the Ku heterodimer, composed of XRCC5/Ku80 and XRCC6/Ku70, at double-strand break sites and promote the assembly and/or stability of the NHEJ machinery. Involved in NHEJ by promoting the ligation of blunt-ended DNA ends. Together with NHEJ1/XLF, collaborates with DNA polymerase lambda …

**Summary**, from NCBI Gene [286257](https://www.ncbi.nlm.nih.gov/gene/286257):

> The protein encoded by this gene plays a role in the nonhomologous end joining (NHEJ) pathway of DNA double-strand break repair. The encoded protein may function to stabilize the Ku70/Ku80 heterodimer to facilitate the assembly and maintain the stability of the NHEJ complex. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:27849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27849) · Entrez [286257](https://www.ncbi.nlm.nih.gov/gene/286257) · UniProt [Q9BUH6](https://www.uniprot.org/uniprotkb/Q9BUH6) · Ensembl [ENSG00000148362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148362)

## Data

Gene col 7275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7275); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7275]; `tensor/DDL_lfc|DDL_z.npy` [7275]; `embed/gene_vectors.npy` [7275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7275 or target_col == 7275). Every well: [[PAXX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAXX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
