---
symbol: "STK26"
type: "gene"
col: 5583
ensembl_id: "ENSG00000134602"
name: "serine/threonine kinase 26"
location: "Xq26.2"
module: 54
arm: "-"
pooled_cpm: 35.96
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# STK26

*serine/threonine kinase 26* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +15.5, q 0e+00, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.726× (z -6.3, q 2e-07, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN11]] (+0.60, fdr 1e-05), [[UBQLN4]] (+0.60, fdr 2e-05), [[NETO2]] (+0.58, fdr 4e-05); moves opposite to [[TIMM29]] (-0.62, fdr 1e-05), [[ACAD10]] (-0.62, fdr 1e-05), [[ESS2]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → cells under [[Pemetrexed (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +15.5 | 0e+00 | 34/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +14.6 | 1e-45 | 29/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +13.7 | 3e-40 | 33/40 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +11.9 | 1e-30 | 29/43 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +9.3 | 1e-18 | 33/43 (PANC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +8.9 | 5e-17 | 27/39 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +7.8 | 7e-13 | 23/43 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.1 | 8e-11 | 21/43 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +7.0 | 2e-10 | 27/43 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.7 | 1e-09 | 24/43 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +6.0 | 1e-07 | 24/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +5.0 | 3e-05 | 20/42 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.26×** | +4.4 | 5e-04 | 21/42 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.3 | 6e-04 | 12/43 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 6e-04 | 19/43 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 14/43 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.094 | 3/43 (NCI-H460, SW1417, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -6.3 | 2e-07 | 25/43 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.728×** | -6.2 | 2e-07 | 26/43 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.756×** | -3.9 | 0.018 | 13/42 (MIA PaCa-2, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.029 | 16/43 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.885× | -3.3 | 0.13 | 10/43 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.850× | -3.2 | 0.14 | 15/42 (A549, SW480, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.18 | 9/43 (A549, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.6 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.9) | — |
| [[SW480 (line)]] | alt | 83.0 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -15.3) |
| [[A498 (line)]] | wt | 22.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 56.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.3) | — |
| [[A549 (line)]] | wt | 17.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 11.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +11.9) | — |
| [[LoVo (line)]] | wt | 30.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 62.7 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.80× (z +8.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.2) | — |
| [[A-427 (line)]] | wt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.9) | — |
| [[J82 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 44.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.3) | — |
| [[A-172 (line)]] | wt | 6.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.60 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[NETO2]] | +0.58 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ADSS2]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[FAM171B]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GALNT7]] | +0.56 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[OXCT1]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[EDEM1]] | +0.56 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[TWF1]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[NCR3LG1]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[FKBP4]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PGRMC1]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM29]] | -0.62 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[ACAD10]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ESS2]] | -0.58 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ENKD1]] | -0.58 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[ATP5MJ]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[C16orf91]] | -0.58 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[MRPL55]] | -0.57 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ATG4B]] | -0.57 | -0.40 / -0.50 | both halves | 5e-05 | STRING 421 |
| [[RPL36AL]] ⚠ | -0.57 | -0.38 / -0.62 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NCBP2AS2]] | -0.57 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[ZER1]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[TECPR1]] | -0.56 | -0.40 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Pemetrexed (drug)]] 5 µM | B | STK26 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express STK26 (5) vs lines expressing it (43) | the lines without STK26: 0.74× the cells of the other lines | 0.027 | ⚠ across organs; maybe low, not absent |
| [[LCMT1]] | B | STK26 activity lowers LCMT1's level | lines that do not express STK26 (5) vs lines expressing it (45) | 1.38× higher at baseline in the lines without STK26 | 0.054 | ⚠ across organs; maybe low, not absent |
| [[MALSU1]] | B | STK26 activity lowers MALSU1's level | lines that do not express STK26 (5) vs lines expressing it (45) | 1.77× higher at baseline in the lines without STK26 | 0.056 | ⚠ across organs; maybe low, not absent |
| [[SEPTIN11]] | B | STK26 activity lowers SEPTIN11's level | lines that do not express STK26 (5) vs lines expressing it (45) | 1.99× higher at baseline in the lines without STK26 | 0.094 | ⚠ across organs; maybe low, not absent |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.5, -14.2); signed map (22.2, -35.6). **Vector** length 101, 24.3% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.9 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +1.6 | +2.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +0.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:132,023,302-132,075,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MST4, MASK |
| Gene groups (HGNC) | STRIPAK complex; STK24/STK25/ST26 kinase family |
| Reactome | 4 pathways, smallest: Apoptotic cleavage of cellular proteins; Apoptotic execution phase; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P289](https://www.uniprot.org/uniprotkb/Q9P289) (Serine/threonine-protein kinase 26):

> Serine/threonine-protein kinase that acts as a mediator of cell growth. Modulates apoptosis. In association with STK24 negatively regulates Golgi reorientation in polarized cell migration upon RHO activation. Phosphorylates ATG4B at 'Ser-383', thereby increasing autophagic flux. Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, …

**Summary**, from NCBI Gene [51765](https://www.ncbi.nlm.nih.gov/gene/51765):

> The product of this gene is a member of the GCK group III family of kinases, which are a subset of the Ste20-like kinases. The encoded protein contains an amino-terminal kinase domain, and a carboxy-terminal regulatory domain that mediates homodimerization. The protein kinase localizes to the Golgi apparatus and is specifically activated by binding to the Golgi matrix protein GM130. It is also cleaved by caspase-3 in vitro, and may function in the apoptotic pathway. Several alternatively …

**Accessions** — [HGNC:18174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18174) · Entrez [51765](https://www.ncbi.nlm.nih.gov/gene/51765) · UniProt [Q9P289](https://www.uniprot.org/uniprotkb/Q9P289) · Ensembl [ENSG00000134602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134602)

## Data

Gene col 5583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5583); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5583]; `tensor/DDL_lfc|DDL_z.npy` [5583]; `embed/gene_vectors.npy` [5583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5583 or target_col == 5583). Every well: [[STK26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
