---
symbol: "NDUFA2"
type: "gene"
col: 5218
ensembl_id: "ENSG00000131495"
name: "NADH:ubiquinone oxidoreductase subunit A2"
location: "5q31.3"
module: 48
arm: "+"
pooled_cpm: 20.7
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFA2

*NADH:ubiquinone oxidoreductase subunit A2* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.82× (z +10.3, q 4e-22, up in 46 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (HEC-1-A 4.25×, HOP62 4.11×, A549 4.46×, SW480 3.15×, …).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0825×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBL5]] (+0.83, fdr 7e-06), [[OST4]] (+0.81, fdr 1e-05), [[COX6A1]] (+0.78, fdr 7e-06); moves opposite to [[COA7]] (-0.69, fdr 3e-05), [[PDAP1]] (-0.67, fdr 1e-05), [[GTF2H3]] (-0.67, fdr 9e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (HEC-1-A 4.25×, HOP62 4.11×, A549 4.46×, SW480 3.15×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +10.3 | 4e-22 | 46/46 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.47×** | +8.7 | 6e-16 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.28×** | +8.4 | 1e-14 | 47/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.90×** | +7.5 | 9e-12 | 46/47 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.97×** | +6.7 | 2e-09 | 41/42 (NCI-H460, A-172, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +6.0 | 2e-07 | 39/44 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.35×** | +5.8 | 6e-07 | 31/32 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **2.15×** | +5.4 | 5e-06 | 39/43 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.11×** | +4.9 | 7e-05 | 28/36 (KATO III, A-172, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.93×** | +4.5 | 5e-04 | 31/46 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.007 | 27/48 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.75×** | +3.8 | 0.007 | 30/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.57× | +3.0 | 0.10 | 24/47 (PANC-1, HT-29, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0825×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0825× (z -10.7) |
| [[HOP62 (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +10.2) | — |
| [[J82 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +8.5) | — |
| [[SW480 (line)]] | alt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.3) | — |
| [[A-172 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | +0.83 | +0.58 / +0.86 | both halves | 7e-06 | STRING 495 |
| [[OST4]] | +0.81 | +0.54 / +0.84 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.78 | +0.62 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 782 |
| [[RABAC1]] | +0.78 | +0.43 / +0.81 | both halves | 3e-05 |  |
| [[COX6B1]] | +0.78 | +0.60 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 982 |
| [[COMMD6]] | +0.77 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.77 | +0.58 / +0.74 | both halves | 8e-06 |  |
| [[DDT]] | +0.76 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[UQCRQ]] ⚠ | +0.76 | +0.55 / +0.80 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[SSR4]] | +0.76 | +0.54 / +0.80 | both halves | 1e-05 |  |
| [[LAMTOR2]] | +0.76 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[NDUFB11]] ⚠ | +0.76 | +0.72 / +0.79 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[COX5B]] | +0.76 | +0.40 / +0.82 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 994 |
| [[BBLN]] | +0.75 | +0.52 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA7]] | -0.69 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[PDAP1]] | -0.67 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[GTF2H3]] | -0.67 | -0.36 / -0.73 | both halves | 9e-05 |  |
| [[CCT5]] | -0.66 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.66 | -0.32 / -0.70 | both halves | 1e-04 |  |
| [[SLC35F6]] | -0.66 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.65 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[PSMD11]] | -0.65 | -0.60 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDUFA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ATOX1]] | C | ATOX1's natural level strengthens NDUFA2's drug response | ATOX1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.14; direction not clear | 0.090 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.876). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.6, -21.3); signed map (-33.9, 10.5). **Vector** length 60.7, 16.8% of its response variance represented; |z| ≥ 3 in 613 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.69 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.67 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.70 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.2 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.1 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.0 | +7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -3.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -2.9 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,638,740-140,647,771 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B8 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Complex I biogenesis; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43678](https://www.uniprot.org/uniprotkb/O43678) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4695](https://www.ncbi.nlm.nih.gov/gene/4695):

> The encoded protein is a subunit of the hydrophobic protein fraction of the NADH:ubiquinone oxidoreductase (complex 1), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane, and may be involved in regulating complex I activity or its assembly via assistance in redox processes. Mutations in this gene are associated with Leigh syndrome, an early-onset progressive neurodegenerative disorder. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:7685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7685) · Entrez [4695](https://www.ncbi.nlm.nih.gov/gene/4695) · UniProt [O43678](https://www.uniprot.org/uniprotkb/O43678) · Ensembl [ENSG00000131495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131495)

## Data

Gene col 5218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5218); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5218]; `tensor/DDL_lfc|DDL_z.npy` [5218]; `embed/gene_vectors.npy` [5218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5218 or target_col == 5218). Every well: [[NDUFA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
