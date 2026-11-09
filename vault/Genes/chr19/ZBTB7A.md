---
symbol: "ZBTB7A"
type: "gene"
col: 10978
ensembl_id: "ENSG00000178951"
name: "zinc finger and BTB domain containing 7A"
location: "19p13.3"
module: 25
arm: "-"
pooled_cpm: 94.89
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ZBTB7A

*zinc finger and BTB domain containing 7A* — 19p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 2.93×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.398× (z -8.1, q 2e-13, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIDN]] (+0.75, fdr 7e-06), [[IRX5]] (+0.68, fdr 2e-05), [[ZNF503]] (+0.67, fdr 1e-05); moves opposite to [[COPS6]] (-0.69, fdr 7e-06), [[LIN7C]] (-0.68, fdr 1e-05), [[LANCL1]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLCF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 2.93×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.36 | 34/49 (hTERT-HPNE, Panc 03.27, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.40× | +3.0 | 0.36 | 28/48 (LoVo, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -8.1 | 2e-13 | 46/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.413×** | -7.8 | 2e-12 | 46/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.453×** | -7.0 | 5e-10 | 45/48 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.657×** | -5.2 | 2e-05 | 40/48 (A-427, KATO III, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.672×** | -5.0 | 8e-05 | 30/48 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.661×** | -3.4 | 0.067 | 40/48 (SW 1088, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.663×** | -3.3 | 0.067 | 35/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.669×** | -3.3 | 0.076 | 39/48 (SNU-423, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.078 | 35/48 (AsPC-1, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.700×** | -3.1 | 0.096 | 27/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -3.1 | 0.096 | 30/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.709× | -3.0 | 0.11 | 34/48 (HepG2/C3A, COLO 205, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.690× | -3.0 | 0.11 | 40/48 (J82, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 138 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 146 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -15.2) |
| [[HS-578T (line)]] | alt | 76.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.289× (z -9.2) |
| [[KATO III (line)]] | alt | 142 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -12.2) |
| [[LS 180 (line)]] | wt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 90.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -9.8) |
| [[SW480 (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -11.9) |
| [[A-172 (line)]] | wt | 135 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -11.0) |
| [[HOP62 (line)]] | alt | 107 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -10.9) |
| [[RKO (line)]] | wt | 77.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.1) |
| [[SW 900 (line)]] | alt | 113 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -9.6) |
| [[SW1417 (line)]] | alt | 153 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -11.4) |
| [[A-427 (line)]] | wt | 60.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.5) |
| [[BT-474 (line)]] | alt | 73.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -11.2) |
| [[COLO 205 (line)]] | alt | 87.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.3) |
| [[HCT15 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 72.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 78.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.9) |
| [[NCI-H661 (line)]] | alt | 50.2 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0768× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.9) |
| [[SNU-1 (line)]] | wt | 88.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -8.9) |
| [[SW48 (line)]] | wt | 84.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.3) |
| [[A498 (line)]] | wt | 100.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIDN]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[IRX5]] | +0.68 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[ZNF503]] | +0.67 | +0.52 / +0.64 | both halves | 1e-05 | same gene group |
| [[EFNA2]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.65 | +0.54 / +0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00685]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[MSX1]] | +0.64 | +0.32 / +0.74 | both halves | 2e-04 |  |
| [[FOXA2]] | +0.63 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[INAFM1]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[HIC2]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 | same gene group |
| [[RBM38]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[TPRN]] | +0.61 | +0.38 / +0.70 | both halves | 7e-05 |  |
| [[TNRC6C]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS6]] | -0.69 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.68 | -0.49 / -0.76 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.67 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[SCCPDH]] | -0.66 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[UBQLN1]] | -0.66 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[EIF4H]] | -0.66 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[TWF1]] | -0.65 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[NONO]] | -0.64 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[MANEA]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[PPT1]] | -0.63 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[AP2M1]] | -0.63 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SUCLG2]] | -0.62 | -0.53 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | CLCF1 activity raises ZBTB7A's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without CLCF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.772). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.7, -18.6); signed map (-3.7, 8.4). **Vector** length 112, 45.2% of its response variance represented; |z| ≥ 3 in 689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.3 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -8.2 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.0 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -3.1 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,043,303-4,066,899 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBI-1, LRF, DKFZp547O146, pokemon, ZNF857A; previously ZBTB7 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95365](https://www.uniprot.org/uniprotkb/O95365) (Zinc finger and BTB domain-containing protein 7A):

> Transcription factor that represses the transcription of a wide range of genes involved in cell proliferation and differentiation. Directly and specifically binds to the consensus sequence 5'-[GA][CA]GACCCCCCCCC-3' and represses transcription both by regulating the organization of chromatin and through the direct recruitment of transcription factors to gene regulatory regions. Negatively regulates SMAD4 transcriptional activity in the TGF-beta signaling pathway through these two mechanisms. …

**Summary**, from NCBI Gene [51341](https://www.ncbi.nlm.nih.gov/gene/51341):

> Enables several functions, including DNA-binding transcription factor activity; nuclear androgen receptor binding activity; and transcription corepressor binding activity. Involved in several processes, including erythrocyte maturation; negative regulation of signal transduction; and regulation of RNA metabolic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18078) · Entrez [51341](https://www.ncbi.nlm.nih.gov/gene/51341) · UniProt [O95365](https://www.uniprot.org/uniprotkb/O95365) · Ensembl [ENSG00000178951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178951)

## Data

Gene col 10978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10978); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10978]; `tensor/DDL_lfc|DDL_z.npy` [10978]; `embed/gene_vectors.npy` [10978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10978 or target_col == 10978). Every well: [[ZBTB7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
