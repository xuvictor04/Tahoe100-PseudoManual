---
symbol: "CELF6"
type: "gene"
col: 6419
ensembl_id: "ENSG00000140488"
name: "CUGBP Elav-like family member 6"
location: "15q23"
module: 26
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CELF6

*CUGBP Elav-like family member 6* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 11.1× (z +19.8, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.432× (z -3.6, q 0.099, down in 10 of 32 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0479×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.0513×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02646]] (+0.77, fdr 7e-06), [[PTOV1-AS1]] (+0.76, fdr 7e-06), [[CFAP70]] (+0.74, fdr 7e-06); moves opposite to [[SDHAF3]] (-0.63, fdr 4e-05), [[NEDD1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **11.1×** | +19.8 | 0e+00 | 42/42 (HT-29, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +11.0 | 1e-25 | 28/34 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +11.0 | 1e-25 | 24/35 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +9.1 | 1e-17 | 3/4 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +8.0 | 2e-13 | 5/8 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +6.9 | 4e-10 | 12/19 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +6.9 | 4e-10 | 19/33 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.59×** | +5.4 | 5e-06 | 12/44 (LoVo, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +5.2 | 1e-05 | 16/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.2 | 1e-05 | 8/22 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.0 | 2e-05 | 15/35 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 11/43 (NCI-H2030, A549, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.005 | 8/45 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.010 | 11/42 (RPMI-7951, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.56×** | +3.7 | 0.010 | 13/40 (A-427, KATO III, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.018 | 5/39 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.024 | 3/42 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.024 | 11/40 (LoVo, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.049 | 7/42 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.049 | 11/42 (PANC-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vandetanib (drug)]] 0.5 µM |  | **1.42×** | +2.9 | 0.097 | 2/40 (SW480, SNU-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6419.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0479×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.0513×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.432×** | -3.6 | 0.099 | 10/32 (COLO 205, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.649×** | -3.6 | 0.099 | 17/41 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.678× | -3.2 | 0.25 | 13/41 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 5 µM |  | 0.683× | -3.0 | 0.34 | 6/43 (NCI-H460, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.87 | 2 | 0 | [[Auranofin (drug)]] 5 µM 73.5× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 8.43 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.2× (z +9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 10.5× (z +8.5) | — |
| [[KATO III (line)]] | alt | 5.60 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 10.6× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0513× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.69 | 1 | 1 | [[Auranofin (drug)]] 5 µM 11.0× (z +8.9) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0479× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 1.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 22.8× (z +10.5) | — |
| [[C32 (line)]] | wt | 3.61 | 1 | 0 | [[Auranofin (drug)]] 5 µM 40.4× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 1.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 3.33 | 1 | 0 | [[Auranofin (drug)]] 5 µM 105× (z +15.0) | — |
| [[J82 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +8.8) | — |
| [[LoVo (line)]] | wt | 4.75 | 1 | 0 | [[Auranofin (drug)]] 5 µM 43.0× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 11.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.0× (z +11.2) | — |
| [[SW480 (line)]] | alt | 2.87 | 1 | 0 | [[Auranofin (drug)]] 5 µM 21.3× (z +11.9) | — |
| [[A-427 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02646]] | +0.77 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[PTOV1-AS1]] | +0.76 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.74 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[LINC00571]] | +0.74 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[NEB]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[NEK11]] | +0.74 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CDKL3]] | +0.74 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.73 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.73 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.73 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[CATSPERE]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.63 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[NEDD1]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CELF6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.1, 13.0); signed map (22.1, -1.8). **Vector** length 75.0, 12.6% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.3 | +19.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CUGBP Elav-like family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:72,284,727-72,320,157 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BRUNOL6 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J87](https://www.uniprot.org/uniprotkb/Q96J87) (CUGBP Elav-like family member 6):

> RNA-binding protein implicated in the regulation of pre-mRNA alternative splicing. Mediates exon inclusion and/or exclusion in pre-mRNA that are subject to tissue-specific and developmentally regulated alternative splicing. Specifically activates exon 5 inclusion of TNNT2 in a muscle-specific splicing enhancer (MSE)-dependent manner. Promotes also exon exclusion of INSR pre-mRNA.

**Summary**, from NCBI Gene [60677](https://www.ncbi.nlm.nih.gov/gene/60677):

> Members of the CELF/BRUNOL protein family contain two N-terminal RNA recognition motif (RRM) domains, one C-terminal RRM domain, and a divergent segment of 160-230 aa between the second and third RRM domains. Members of this protein family regulate pre-mRNA alternative splicing and may also be involved in mRNA editing, and translation. Multiple alternatively spliced transcript variants encoding different isoforms have been identified in this gene. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:14059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14059) · Entrez [60677](https://www.ncbi.nlm.nih.gov/gene/60677) · UniProt [Q96J87](https://www.uniprot.org/uniprotkb/Q96J87) · Ensembl [ENSG00000140488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140488)

## Data

Gene col 6419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6419); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6419]; `tensor/DDL_lfc|DDL_z.npy` [6419]; `embed/gene_vectors.npy` [6419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6419 or target_col == 6419). Every well: [[CELF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
