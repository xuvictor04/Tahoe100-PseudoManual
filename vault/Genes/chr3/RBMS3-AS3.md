---
symbol: "RBMS3-AS3"
type: "gene"
col: 14048
ensembl_id: "ENSG00000235904"
name: "RBMS3 antisense RNA 3"
location: "3p24.1"
module: 75
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# RBMS3-AS3

*RBMS3 antisense RNA 3* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 7.05× (z +15.2, q 0e+00, up in 6 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.10× (z +13.5, q 6e-39, up in 24 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.113×; ⚠ cell-cycle shift, explains ~15% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4300HG]] (+0.79, fdr 7e-06), [[PPP1R9A-AS1]] (+0.79, fdr 7e-06), [[EYS]] (+0.78, fdr 7e-06); moves opposite to [[FBXW2]] (-0.65, fdr 4e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.05×** | +15.2 | 0e+00 | 6/6 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.10×** | +13.5 | 6e-39 | 24/35 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +12.9 | 8e-36 | 29/33 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +12.6 | 2e-34 | 14/15 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.0 | 1e-13 | 3/5 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +7.0 | 3e-10 | 18/34 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +5.8 | 7e-07 | 6/16 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.96×** | +5.7 | 1e-06 | 21/42 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +5.2 | 1e-05 | 7/14 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.1 | 2e-05 | 12/28 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.0 | 3e-05 | 12/32 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.91×** | +4.7 | 1e-04 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.64×** | +4.0 | 0.003 | 18/41 (A-172, HEC-1-A, …) | top dose only | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.003 | 11/36 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 9/45 (A-172, HS-578T, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.028 | 5/30 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14048.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.113×; ⚠ cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.858× | -4.7 | 0.001 | 20/47 (SW1417, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.44 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -8.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 2.78 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 2.87 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 3.28 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +8.5) | — |
| [[J82 (line)]] | alt | 4.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 2.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.9× (z +10.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 1.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 16.5× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 4.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +12.2) | — |
| [[A-427 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4300HG]] | +0.79 | +0.84 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.79 | +0.74 / +0.64 | both halves | 7e-06 | same gene group |
| [[EYS]] | +0.78 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[LRRN3]] | +0.78 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.77 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.76 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SFRP4]] | +0.76 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.76 | +0.76 / +0.59 | both halves | 7e-06 | same gene group |
| [[DLEU7]] | +0.75 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[SAMD4A-AS1]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 | same gene group |
| [[CNTNAP5]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.65 | -0.70 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBMS3-AS3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GNAT3]] | B | GNAT3 activity raises RBMS3-AS3's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 1.34× lower at baseline in the lines without GNAT3 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent |
| [[JAM2]] | B | JAM2 activity strengthens RBMS3-AS3's drug response | lines that do not express JAM2 (27) vs lines expressing it (16) | the lines without JAM2 respond 0.55× as strongly (z diff +1.44); strongest at Homoharringtonine 5 µM: 2.11x vs 6.54x (z diff +4.2) | 0.091 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R; target measured in part of the lines; artifact flags |
| [[ANOS2P]] | B | ANOS2P activity raises RBMS3-AS3's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without ANOS2P | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.826). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.6, 27.1); signed map (33.9, 11.6). **Vector** length 53.9, 7.14% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -1.6 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | RBMS3 antisense RNA 3 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p24.1 — chr3:29,054,570-29,290,726 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39989) · Entrez [100873979](https://www.ncbi.nlm.nih.gov/gene/100873979) · Ensembl [ENSG00000235904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235904)

## Data

Gene col 14048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14048); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14048]; `tensor/DDL_lfc|DDL_z.npy` [14048]; `embed/gene_vectors.npy` [14048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14048 or target_col == 14048). Every well: [[RBMS3-AS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMS3-AS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
