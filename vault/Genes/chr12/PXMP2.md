---
symbol: "PXMP2"
type: "gene"
col: 10761
ensembl_id: "ENSG00000176894"
name: "peroxisomal membrane protein 2"
location: "12q24.33"
module: 6
arm: "+"
pooled_cpm: 6.37
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PXMP2

*peroxisomal membrane protein 2* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.36× (z +16.5, q 0e+00, up in 27 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[DT-061 (drug)]] 5 µM: 1.83× (z +3.1, q 0.085, up in 4 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 5.24×, PANC-1 7.09×, KATO III 8.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.576× (z -5.4, q 4e-05, down in 22 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.354×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR76]] (+0.72, fdr 7e-06), [[PKMYT1]] (+0.72, fdr 7e-06), [[E2F1]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM111B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CDC45]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 5.24×, PANC-1 7.09×, KATO III 8.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **5.36×** | +16.5 | 0e+00 | 27/27 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.39×** | +13.1 | 1e-36 | 17/19 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.41×** | +13.0 | 1e-36 | 12/12 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.6 | 3e-06 | 19/32 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.60×** | +4.6 | 5e-04 | 14/31 (HT-29, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +4.2 | 0.003 | 3/15 (SNU-423, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +4.2 | 0.003 | 20/41 (SNU-423, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.57×** | +3.9 | 0.006 | 10/33 (NCI-H1792, A-427, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.8 | 0.009 | 15/40 (AsPC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +3.4 | 0.033 | 10/41 (C-33 A, A-172, …) | two highest doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.39×** | +3.2 | 0.063 | 11/39 (J82, NCI-H2030, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.2 | 0.063 | 8/40 (NCI-H2030, AN3 CA, …) | top dose only |  |
| [[DT-061 (drug)]] 5 µM |  | **1.83×** | +3.1 | 0.085 | 4/31 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.36× | +3.0 | 0.11 | 13/46 (LoVo, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.354×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -5.4 | 4e-05 | 22/38 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.668×** | -3.7 | 0.052 | 15/43 (SK-MEL-2, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -3.6 | 0.052 | 15/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.710× | -3.4 | 0.11 | 16/46 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.730× | -3.1 | 0.23 | 8/43 (Hs 766T, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 8.91 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.49× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 4.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 7.13 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR76]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[E2F1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[RAD51]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CENPM]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[GINS2]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[POLE]] | +0.68 | +0.71 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[HAT1]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NUDT1]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CDC45]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM111B]] | B | FAM111B activity raises PXMP2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without FAM111B | 0.047 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises PXMP2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without TCF19 | 0.069 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC45]] | C | PXMP2's natural level weakens CDC45's drug response | PXMP2's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.26; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.7, -44.2); signed map (-37.3, -45.1). **Vector** length 57.1, 9.01% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.50 to 65); *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.6 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.3 | +13.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | +2.9 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.9 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.0 | +2.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,687,587-132,704,985 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PMP22, MPV17L3 |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Glyoxylate metabolism and glycine degradation; Class I peroxisomal membrane protein import; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR77](https://www.uniprot.org/uniprotkb/Q9NR77) (Peroxisomal membrane protein 2):

> Seems to be involved in pore-forming activity and may contribute to the unspecific permeability of the peroxisomal membrane.

**Summary**, from NCBI Gene [5827](https://www.ncbi.nlm.nih.gov/gene/5827):

> Located in peroxisomal membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9716) · Entrez [5827](https://www.ncbi.nlm.nih.gov/gene/5827) · UniProt [Q9NR77](https://www.uniprot.org/uniprotkb/Q9NR77) · Ensembl [ENSG00000176894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176894)

## Data

Gene col 10761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10761); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10761]; `tensor/DDL_lfc|DDL_z.npy` [10761]; `embed/gene_vectors.npy` [10761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10761 or target_col == 10761). Every well: [[PXMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
