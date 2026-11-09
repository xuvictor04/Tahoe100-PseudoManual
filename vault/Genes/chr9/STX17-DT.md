---
symbol: "STX17-DT"
type: "gene"
col: 14921
ensembl_id: "ENSG00000255145"
name: "non-protein coding RNA, associated with MAP kinase pathway and growth arrest"
location: "9q22.33"
module: 26
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# STX17-DT

*non-protein coding RNA, associated with MAP kinase pathway and growth arrest* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.63× (z +25.0, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.715× (z -4.6, q 0.003, down in 15 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.779× (z -3.4, q 0.079, down in 6 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Decitabine (drug)]] 0.05 µM in 1 line (COLO 205 0.0771×); [[Belinostat (drug)]] 0.5 µM in 1 line (A-172 0.110×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A549 0.123×; ⚠ toxic; cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRK1-AS1]] (+0.77, fdr 1e-05), [[PSMD7-DT]] (+0.77, fdr 8e-06), [[KMT2E-AS1]] (+0.76, fdr 1e-05); moves opposite to [[EIF2B3]] (-0.65, fdr 8e-05), [[NUP93]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.63×** | +25.0 | 0e+00 | 42/42 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.52×** | +17.2 | 0e+00 | 35/45 (HT-29, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +15.2 | 0e+00 | 28/40 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +14.3 | 2e-44 | 32/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +13.5 | 2e-39 | 30/42 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +10.8 | 5e-25 | 30/47 (SW480, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +8.1 | 5e-14 | 8/13 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.0 | 1e-13 | 16/32 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +7.8 | 3e-13 | 21/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.8 | 4e-13 | 17/35 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.3 | 1e-11 | 17/47 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.5 | 3e-09 | 18/42 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +6.4 | 5e-09 | 8/20 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +6.3 | 9e-09 | 22/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.34×** | +6.1 | 4e-08 | 14/45 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +5.9 | 1e-07 | 15/44 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +5.3 | 4e-06 | 20/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 13/46 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 5e-04 | 13/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14921.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Decitabine (drug)]] 0.05 µM in 1 line (COLO 205 0.0771×); [[Belinostat (drug)]] 0.5 µM in 1 line (A-172 0.110×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A549 0.123×; ⚠ toxic; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.715×** | -4.6 | 0.003 | 15/46 (NCI-H23, KATO III, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.763×** | -3.7 | 0.062 | 11/47 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.774×** | -3.5 | 0.079 | 11/47 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.779×** | -3.4 | 0.079 | 6/46 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -3.4 | 0.079 | 10/48 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.786× | -3.1 | 0.17 | 7/44 (LOX-IMVI, A-427, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.17 | 14/45 (CHP-212, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.96 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.1) | — |
| [[A-172 (line)]] | wt | 5.78 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +10.6) | [[Belinostat (drug)]] 0.5 µM 0.110× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.25 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 4.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +9.1) | — |
| [[A498 (line)]] | wt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +11.7) | — |
| [[A549 (line)]] | wt | 6.02 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 4.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.31× (z +9.0) | — |
| [[C32 (line)]] | wt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0771× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 5.59 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.2× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 5.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 9.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 7.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +10.0) | — |
| [[RKO (line)]] | wt | 6.38 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 6.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 4.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 4.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +9.9) | — |
| [[A-427 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRK1-AS1]] | +0.77 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.77 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[KMT2E-AS1]] | +0.76 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.75 | +0.71 / +0.56 | both halves | 1e-05 | same gene group |
| [[LRP2BP]] | +0.74 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.73 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.73 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[OOEP]] | +0.72 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[HSPA2-AS1]] | +0.71 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.70 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | +0.70 | +0.70 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | -0.65 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NUP93]] | -0.65 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STX17-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HAND2-AS1]] | B | HAND2-AS1 activity raises STX17-DT's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without HAND2-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.2, 21.4); signed map (28.5, -2.0). **Vector** length 72.8, 12.2% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +25.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +17.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.5 | +2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | +7.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.1 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | non-protein coding RNA, associated with MAP kinase pathway and growth arrest |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q22.33 — chr9:99,397,024-99,906,605 (-) |
| Ensembl biotype | lncRNA |
| Also known as | STX17-AS1; previously STX17-DT |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42408) · Entrez [100996569](https://www.ncbi.nlm.nih.gov/gene/100996569) · Ensembl [ENSG00000255145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255145)

## Data

Gene col 14921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14921); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14921]; `tensor/DDL_lfc|DDL_z.npy` [14921]; `embed/gene_vectors.npy` [14921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14921 or target_col == 14921). Every well: [[STX17-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX17-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
