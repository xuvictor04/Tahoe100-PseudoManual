---
symbol: "USP38-DT"
type: "gene"
col: 14686
ensembl_id: "ENSG00000250326"
name: "USP38 divergent transcript"
location: "4q31.21"
module: 10
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# USP38-DT

*USP38 divergent transcript* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.79× (z +25.9, q 0e+00, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.635× (z -4.4, q 0.006, down in 12 of 46 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (HOP62 0.0610×; ⚠ cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.86, fdr 7e-06), [[INTS6-AS1]] (+0.85, fdr 7e-06), [[EPM2A-DT]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COP1-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.79×** | +25.9 | 0e+00 | 30/31 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +13.2 | 3e-37 | 22/36 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +9.5 | 5e-19 | 18/29 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +9.4 | 1e-18 | 4/5 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.0 | 2e-17 | 18/46 (A498, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.9 | 2e-13 | 3/4 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +7.8 | 5e-13 | 6/14 (SW 900, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.22×** | +7.6 | 2e-12 | 17/42 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +7.5 | 3e-12 | 17/38 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +6.4 | 8e-09 | 20/41 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +5.9 | 1e-07 | 16/32 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +4.4 | 4e-04 | 12/46 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.3 | 8e-04 | 8/45 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +4.2 | 0.001 | 7/45 (NCI-H2347, A498, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.001 | 13/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 7/44 (HEC-1-A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.006 | 6/33 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.017 | 11/42 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.021 | 7/47 (A498, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14686.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (HOP62 0.0610×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.635×** | -4.4 | 0.006 | 12/46 (HEC-1-A, CHP-212, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.649×** | -4.2 | 0.008 | 18/46 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.38 | 4/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 4.35 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0610× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 1.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +9.5) | — |
| [[SW480 (line)]] | alt | 3.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +10.4) | — |
| [[A-172 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.86 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.85 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[EPM2A-DT]] | +0.84 | +0.89 / +0.59 | both halves | 7e-06 | same gene group |
| [[MAD2L1-DT]] | +0.84 | +0.85 / +0.65 | both halves | 7e-06 | same gene group |
| [[SEPTIN7-DT]] | +0.81 | +0.82 / +0.61 | both halves | 7e-06 | same gene group |
| [[PCNX4-DT]] | +0.80 | +0.82 / +0.63 | both halves | 7e-06 | same gene group |
| [[LINC00240]] | +0.80 | +0.84 / +0.61 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.79 | +0.79 / +0.71 | both halves | 7e-06 | same gene group |
| [[PKN2-AS1]] | +0.79 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[UNC79]] | +0.79 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.78 | +0.79 / +0.56 | both halves | 1e-05 | same gene group |
| [[ATE1OSP]] | +0.78 | +0.80 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COP1-DT]] | B | COP1-DT activity raises USP38-DT's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without COP1-DT | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises USP38-DT's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without IGSF11 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers USP38-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises USP38-DT's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ST8SIA5 | 0.047 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.9, 17.7); signed map (29.0, -8.6). **Vector** length 60.8, 8.88% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +25.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +9.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.6 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | USP38 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q31.21 — chr4:142,933,195-143,184,861 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55554) · Entrez [105377623](https://www.ncbi.nlm.nih.gov/gene/105377623) · Ensembl [ENSG00000250326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250326)

## Data

Gene col 14686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14686); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14686]; `tensor/DDL_lfc|DDL_z.npy` [14686]; `embed/gene_vectors.npy` [14686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14686 or target_col == 14686). Every well: [[USP38-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP38-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
