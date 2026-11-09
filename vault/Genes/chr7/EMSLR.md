---
symbol: "EMSLR"
type: "gene"
col: 13849
ensembl_id: "ENSG00000232445"
name: "E2F1 mRNA stabilizing lncRNA"
location: "7q22.1"
module: 33
arm: "+"
pooled_cpm: 6.04
n_lines_expressing: 35
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# EMSLR

*E2F1 mRNA stabilizing lncRNA* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.36× (z +7.9, q 2e-12, up in 16 of 23 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.04× (z +7.3, q 9e-11, up in 20 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.141×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.273×; ⚠ cell-cycle shift, explains ~77% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.100×; ⚠ cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (Hs 766T 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH2]] (+0.74, fdr 7e-06), [[NUFIP1]] (+0.72, fdr 7e-06), [[ZNF485]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00839]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CNNM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +7.9 | 2e-12 | 16/23 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +7.3 | 9e-11 | 20/30 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +7.0 | 4e-10 | 15/30 (NCI-H2347, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.86×** | +6.4 | 2e-08 | 9/20 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.97×** | +6.3 | 4e-08 | 4/8 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +5.6 | 2e-06 | 18/30 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.71×** | +5.5 | 4e-06 | 12/31 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.65×** | +5.1 | 2e-05 | 10/23 (LS 180, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.60×** | +4.8 | 1e-04 | 17/31 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.58×** | +4.2 | 0.002 | 8/24 (NCI-H460, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +4.2 | 0.002 | 11/31 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.0 | 0.003 | 12/27 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.006 | 13/28 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.006 | 11/29 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.024 | 5/29 (HCT15, A549, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +3.2 | 0.041 | 7/28 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.042 | 7/30 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.77×** | +3.1 | 0.067 | 4/28 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.141×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.273×; ⚠ cell-cycle shift, explains ~77% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.100×; ⚠ cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (Hs 766T 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -4.1 | 0.021 | 9/32 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.40 | 9/31 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -11.6) |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 5 µM 0.119× (z -8.6) |
| [[KATO III (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.100× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 5.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH2]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[NUFIP1]] | +0.72 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ZNF485]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[NLE1]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[DCAF4]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.64 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DDX31]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[FXN]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SETD6]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RRS1]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TFAP4]] | +0.61 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00839]] | B | LINC00839 activity lowers EMSLR's level | lines that do not express LINC00839 (24) vs lines expressing it (26) | 1.98× higher at baseline in the lines without LINC00839 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRR16, CCNYL2, PCDH10 |
| [[MTARC1]] | C | MTARC1 activity raises EMSLR's level | lines that do not express MTARC1 (12) vs lines expressing it (38) | 2.25× lower at baseline in the lines without MTARC1 | 0.023 | ⚠ within organs, on part of the lines; also absent: C1orf115, SEPTIN9-DT, MTARC2; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNNM1]] | B | EMSLR activity raises CNNM1's level | lines that do not express EMSLR (15) vs lines expressing it (35) | 2.52× lower at baseline in the lines without EMSLR | 0.091 | ⚠ within organs, on part of the lines; also absent: MLXIPL, GAL, P2RX5 |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.4, -40.6); signed map (-8.1, -50.2). **Vector** length 56.1, 11.9% of its response variance represented; |z| ≥ 3 in 484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.2 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | E2F1 mRNA stabilizing lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q22.1 — chr7:101,308,270-101,314,800 (+) |
| Ensembl biotype | lncRNA |
| Also known as | EMS, BCCE4 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54408) · Entrez [101927746](https://www.ncbi.nlm.nih.gov/gene/101927746) · Ensembl [ENSG00000232445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232445)

## Data

Gene col 13849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13849); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13849]; `tensor/DDL_lfc|DDL_z.npy` [13849]; `embed/gene_vectors.npy` [13849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13849 or target_col == 13849). Every well: [[EMSLR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMSLR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
