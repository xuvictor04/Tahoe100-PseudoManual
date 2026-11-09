---
symbol: "MED28-DT"
type: "gene"
col: 14619
ensembl_id: "ENSG00000249502"
name: "MED28 divergent transcript"
location: "4p15.32"
module: 35
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MED28-DT

*MED28 divergent transcript* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.80× (z +21.4, q 0e+00, up in 32 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Flutamide (drug)]] 5 µM in 1 line (LoVo 0.0502×); [[Proglumide (drug)]] 0.05 µM in 1 line (A498 0.0682×); [[Nevirapine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0731×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5-AS1]] (+0.78, fdr 7e-06), [[PAXBP1-AS1]] (+0.78, fdr 7e-06), [[SPATA1]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.80×** | +21.4 | 0e+00 | 32/32 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +10.7 | 2e-24 | 4/10 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +10.3 | 2e-22 | 14/27 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +9.7 | 4e-20 | 20/35 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +8.3 | 1e-14 | 18/34 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.3 | 1e-14 | 14/44 (HOP62, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +7.6 | 2e-12 | 3/5 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.2 | 4e-11 | 1/5 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +6.2 | 4e-08 | 5/13 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +5.7 | 8e-07 | 13/44 (PANC-1, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.9 | 4e-05 | 5/13 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.3 | 9e-04 | 1/38 (C32) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.2 | 0.001 | 1/5 (J82) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 7/43 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.7 | 0.007 | 4/26 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.007 | 6/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 7/42 (RKO, PANC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.013 | 4/29 (NCI-H1573, SW480, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.018 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.018 | 2/38 (RKO, HEC-1-A) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.042 | 4/42 (PANC-1, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.061 | 2/42 (NCI-H23, A-427) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14619.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Flutamide (drug)]] 5 µM in 1 line (LoVo 0.0502×); [[Proglumide (drug)]] 0.05 µM in 1 line (A498 0.0682×); [[Nevirapine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0731×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -4.5 | 0.003 | 16/48 (HCT15, HepG2/C3A, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.755× | -3.1 | 0.58 | 5/44 (NCI-H1792, BT-474, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.42 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +9.8) | [[Nevirapine (drug)]] 0.05 µM 0.0731× (z -8.9) |
| [[A498 (line)]] | wt | 2.08 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0682× (z -9.5) |
| [[HOP62 (line)]] | alt | 2.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +8.6) | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 1 | — | [[Flutamide (drug)]] 5 µM 0.0502× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 2.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 2.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 2.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5-AS1]] | +0.78 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.78 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.78 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.76 | +0.73 / +0.73 | both halves | 7e-06 | same gene group |
| [[LINC01090]] | +0.76 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.75 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.75 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[FAM184B]] | +0.75 | +0.67 / +0.56 | both halves | 1e-05 | ⚠ same locus (14.7 kb, same strand: neighbours can correlate without regulation) |
| [[CIBAR1-DT]] | +0.75 | +0.67 / +0.52 | both halves | 1e-05 | same gene group |
| [[DDX19A-DT]] | +0.74 | +0.66 / +0.60 | both halves | 7e-06 | same gene group |
| [[HRG-AS1]] | +0.73 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CCDC73]] | +0.73 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MED28-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.6, 21.7); signed map (29.6, -1.2). **Vector** length 42.1, 4.12% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +21.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.9 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | MED28 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p15.32 — chr4:17,586,267-17,614,585 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LAP3-AS1, AC006160.1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55567) · Entrez [121232375](https://www.ncbi.nlm.nih.gov/gene/121232375) · Ensembl [ENSG00000249502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249502)

## Data

Gene col 14619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14619); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14619]; `tensor/DDL_lfc|DDL_z.npy` [14619]; `embed/gene_vectors.npy` [14619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14619 or target_col == 14619). Every well: [[MED28-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED28-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
