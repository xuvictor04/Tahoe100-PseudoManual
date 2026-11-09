---
symbol: "PITPNA-AS1"
type: "gene"
col: 14088
ensembl_id: "ENSG00000236618"
name: "PITPNA antisense RNA 1"
location: "17p13.3"
module: 24
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PITPNA-AS1

*PITPNA antisense RNA 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +6.8, q 5e-09, up in 1 of 2 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.16× (z +5.4, q 1e-05, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.450× (z -5.7, q 7e-06, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.121×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC5]] (+0.77, fdr 1e-05), [[SMIM26]] (+0.69, fdr 2e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[CLN8-AS1]] (+0.69, fdr 1e-05), [[RP9]] (+0.68, fdr 7e-06); moves opposite to [[HCFC1]] (-0.73, fdr 7e-06), [[CERS2]] (-0.70, fdr 7e-06), [[LY6G5B]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ETFB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.73×** | +6.8 | 5e-09 | 1/2 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.30×** | +5.9 | 1e-06 | 13/20 (A549, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +5.4 | 1e-05 | 29/44 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.05×** | +5.1 | 6e-05 | 12/19 (KATO III, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.82×** | +3.9 | 0.009 | 1/5 (SW480) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.009 | 8/44 (SW480, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.033 | 13/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.38×** | +3.4 | 0.049 | 1/34 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.60×** | +3.3 | 0.063 | 4/33 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.063 | 11/43 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +3.2 | 0.063 | 10/45 (NCI-H460, A498, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.62×** | +3.2 | 0.063 | 6/37 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.54× | +3.0 | 0.11 | 6/46 (PANC-1, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14088.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.450×** | -5.7 | 7e-06 | 23/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -5.2 | 5e-05 | 20/40 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.617× | -3.5 | 0.10 | 12/40 (SNU-423, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.628× | -3.1 | 0.29 | 12/44 (HEC-1-A, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.52 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -8.9) |
| [[A-172 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 10 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC5]] | +0.77 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.69 | +0.48 / +0.73 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CLN8-AS1]] | +0.69 | +0.49 / +0.70 | both halves | 1e-05 | same gene group |
| [[RP9]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.68 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[TIMM17B]] ⚠ | +0.68 | +0.56 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNAPIN]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NFKBIL1]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[GTF2H5]] | +0.67 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[KRT10]] ⚠ | +0.67 | +0.48 / +0.77 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MTLN]] ⚠ | +0.67 | +0.46 / +0.67 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UBE2B]] | +0.67 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ISCA2]] | +0.67 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[AFTPH]] | +0.67 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ZCRB1]] | +0.66 | +0.42 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.73 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[CERS2]] | -0.70 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[LY6G5B]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.67 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[U2AF2]] | -0.67 | -0.33 / -0.69 | both halves | 1e-04 |  |
| [[PSME3]] | -0.66 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[MOB1A]] | -0.66 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[UBQLN4]] | -0.66 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[DHFR]] | -0.66 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[EIF5A]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[SRSF1]] | -0.63 | -0.25 / -0.69 | both halves | 4e-04 |  |
| [[CMPK1]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETFB]] | C | PITPNA-AS1's natural level strengthens ETFB's drug response | PITPNA-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TMEM256]] | C | PITPNA-AS1's natural level strengthens TMEM256's drug response | PITPNA-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.40; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, -16.7); signed map (-13.5, -2.9). **Vector** length 46.1, 6.32% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.5 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PITPNA antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p13.3 — chr17:1,516,877-1,518,101 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44116) · Entrez [100306951](https://www.ncbi.nlm.nih.gov/gene/100306951) · Ensembl [ENSG00000236618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236618)

## Data

Gene col 14088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14088); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14088]; `tensor/DDL_lfc|DDL_z.npy` [14088]; `embed/gene_vectors.npy` [14088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14088 or target_col == 14088). Every well: [[PITPNA-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNA-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
