---
symbol: "ESR2"
type: "gene"
col: 6366
ensembl_id: "ENSG00000140009"
name: "estrogen receptor 2"
location: "14q23.2-q23.3"
module: 26
arm: "+"
pooled_cpm: 9.55
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ESR2

*estrogen receptor 2* — 14q23.2-q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.29× (z +30.6, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.697× (z -6.6, q 3e-08, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.77, fdr 7e-06), [[DNAH10]] (+0.76, fdr 7e-06), [[DENND6A-AS1]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +30.6 | 0e+00 | 42/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +14.4 | 2e-44 | 28/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +11.2 | 1e-26 | 31/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.2 | 5e-18 | 16/32 (LOX-IMVI, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +8.6 | 1e-15 | 22/44 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +7.7 | 2e-12 | 22/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +7.6 | 3e-12 | 19/45 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +6.6 | 3e-09 | 12/26 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.4 | 9e-09 | 5/16 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.0 | 9e-08 | 15/48 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 2e-06 | 11/45 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +4.6 | 2e-04 | 13/41 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 10/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +3.6 | 0.012 | 11/47 (SW480, A549, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.041 | 11/47 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.046 | 1/47 (SK-MEL-2) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.060 | 6/44 (SW 1271, BT-474, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.060 | 5/43 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.075 | 9/48 (J82, HOP62, …) | rises with dose | position effect removed |
| [[Methylthiouracil (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.091 | 1/47 (COLO 205) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -6.6 | 3e-08 | 17/47 (NCI-H1792, J82, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.753×** | -5.2 | 6e-05 | 18/45 (H4, A549, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -4.9 | 2e-04 | 12/47 (A-427, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.782×** | -4.5 | 0.001 | 15/42 (RPMI-7951, HOP62, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.785×** | -4.4 | 0.001 | 14/48 (NCI-H23, NCI-H2030, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.638×** | -4.3 | 0.002 | 8/41 (C32, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.809×** | -3.9 | 0.009 | 14/46 (A549, RPMI-7951, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.867× | -3.7 | 0.017 | 11/48 (J82, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.828×** | -3.4 | 0.037 | 8/48 (H4, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.044 | 11/46 (RPMI-7951, SW48, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.064 | 3/48 (NCI-H661, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 8.33 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 7.93 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +10.4) | [[Docetaxel (drug)]] 0.05 µM 0.0955× (z -9.4) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 16.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.49× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 7.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +13.9) | — |
| [[SW48 (line)]] | wt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +10.5) | — |
| [[SW480 (line)]] | alt | 6.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +14.7) | — |
| [[A498 (line)]] | wt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.5) | — |
| [[A549 (line)]] | wt | 8.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.104× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +12.3) | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0854× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~90% of this change |
| [[LOX-IMVI (line)]] | wt | 5.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.46× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 5.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 8.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +8.8) | — |
| [[A-172 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.77 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.76 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.75 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[MALINC1]] | +0.74 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.73 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.73 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.73 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.72 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.71 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.71 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NEB]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ANKHD1-DT]] | +0.71 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ESR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01358]] | B | LINC01358 activity raises ESR2's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.37× lower at baseline in the lines without LINC01358 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity raises ESR2's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.31× lower at baseline in the lines without ADAMTS9-AS2 | 0.051 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity weakens ESR2's drug response | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (18) | the lines without ADAMTS9-AS2 respond 1.58× as strongly (z diff -1.09); strongest at Dinaciclib 0.05 µM: 1.71x vs 0.90x (z diff -3.0) | 0.056 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.1, 22.3); signed map (28.7, 0.0). **Vector** length 76.8, 13.1% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +30.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.5 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | estrogen receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2-q23.3 — chr14:64,084,232-64,338,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NR3A2, Erb, ER-beta |
| Gene groups (HGNC) | Estrogen receptors |
| Hallmark sets | PEROXISOME |
| Reactome | 11 pathways, smallest: Nuclear Receptor transcription pathway; Constitutive Signaling by Aberrant PI3K in Cancer; Extra-nuclear estrogen signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92731](https://www.uniprot.org/uniprotkb/Q92731) (Estrogen receptor beta):

> Nuclear hormone receptor. Binds estrogens with an affinity similar to that of ESR1/ER-alpha, and activates expression of reporter genes containing estrogen response elements (ERE) in an estrogen-dependent manner.; [Isoform 2]: Lacks ligand binding ability and has no or only very low ERE binding activity resulting in the loss of ligand-dependent transactivation ability.

**Summary**, from NCBI Gene [2100](https://www.ncbi.nlm.nih.gov/gene/2100):

> This gene encodes a member of the family of estrogen receptors and superfamily of nuclear receptor transcription factors. The gene product contains an N-terminal DNA binding domain and C-terminal ligand binding domain and is localized to the nucleus, cytoplasm, and mitochondria. Upon binding to 17beta-estradiol or related ligands, the encoded protein forms homo- or hetero-dimers that interact with specific DNA sequences to activate transcription. Some isoforms dominantly inhibit the activity of …

**Accessions** — [HGNC:3468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3468) · Entrez [2100](https://www.ncbi.nlm.nih.gov/gene/2100) · UniProt [Q92731](https://www.uniprot.org/uniprotkb/Q92731) · Ensembl [ENSG00000140009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140009)

## Data

Gene col 6366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6366); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6366]; `tensor/DDL_lfc|DDL_z.npy` [6366]; `embed/gene_vectors.npy` [6366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6366 or target_col == 6366). Every well: [[ESR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
