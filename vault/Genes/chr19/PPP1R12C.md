---
symbol: "PPP1R12C"
type: "gene"
col: 4625
ensembl_id: "ENSG00000125503"
name: "protein phosphatase 1 regulatory subunit 12C"
location: "19q13.42"
module: 2
arm: "+"
pooled_cpm: 28.52
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PPP1R12C

*protein phosphatase 1 regulatory subunit 12C* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.24× (z +11.6, q 4e-28, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.148×, HCT15 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (AN3 CA 0.0703×); [[Roxadustat (drug)]] 0.05 µM in 1 line (BT-474 0.147×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (AN3 CA 0.0937×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBRSL1]] (+0.74, fdr 7e-06), [[PLXNA3]] (+0.72, fdr 7e-06), [[GDI1]] (+0.69, fdr 7e-06); moves opposite to [[HOXA6]] (-0.54, fdr 6e-05), [[DHRS4-AS1]] (-0.53, fdr 7e-05), [[SCGB2B2]] (-0.51, fdr 6e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +11.6 | 4e-28 | 45/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +10.5 | 2e-23 | 45/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +9.7 | 5e-20 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.9 | 7e-07 | 5/48 (C-33 A, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.8 | 2e-04 | 27/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 9e-04 | 25/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.9 | 0.009 | 23/48 (PANC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.011 | 23/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.017 | 16/48 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.4 | 0.041 | 19/43 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4625.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.148×, HCT15 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (AN3 CA 0.0703×); [[Roxadustat (drug)]] 0.05 µM in 1 line (BT-474 0.147×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (AN3 CA 0.0937×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.3 | 0.52 | 19/47 (RPMI-7951, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0703× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 33.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.5) | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.147× (z -9.9) |
| [[H4 (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.9) | — |
| [[A-172 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBRSL1]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[PLXNA3]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[GDI1]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TNK2]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TCF3]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[R3HDM4]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SIN3B]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ZNF598]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SBF1]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA6]] | -0.54 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[DHRS4-AS1]] | -0.53 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[SCGB2B2]] | -0.51 | -0.21 / -0.46 | both halves | 6e-04 |  |
| [[CHD6]] | -0.50 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[MPLKIP]] | -0.50 | -0.39 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PPP1R12C's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PPP1R12C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ABHD17A]] | C | ABHD17A's natural level weakens PPP1R12C's drug response | ABHD17A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.34; direction not clear | 0.088 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.2, -3.3); signed map (-20.5, 24.6). **Vector** length 88.1, 18.5% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.1 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +9.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 12C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,090,914-55,117,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434D0412, p84, MBS85, p85, AAVS1; previously LENG3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; Myosin phosphatase targeting family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZL4](https://www.uniprot.org/uniprotkb/Q9BZL4) (Protein phosphatase 1 regulatory subunit 12C):

> Regulates myosin phosphatase activity.

**Summary**, from NCBI Gene [54776](https://www.ncbi.nlm.nih.gov/gene/54776):

> The gene encodes a subunit of myosin phosphatase. The encoded protein regulates the catalytic activity of protein phosphatase 1 delta and assembly of the actin cytoskeleton. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:14947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14947) · Entrez [54776](https://www.ncbi.nlm.nih.gov/gene/54776) · UniProt [Q9BZL4](https://www.uniprot.org/uniprotkb/Q9BZL4) · Ensembl [ENSG00000125503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125503)

## Data

Gene col 4625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4625); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4625]; `tensor/DDL_lfc|DDL_z.npy` [4625]; `embed/gene_vectors.npy` [4625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4625 or target_col == 4625). Every well: [[PPP1R12C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R12C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
