---
symbol: "HEATR4"
type: "gene"
col: 11887
ensembl_id: "ENSG00000187105"
name: "HEAT repeat containing 4"
location: "14q24.3"
module: 35
arm: "+"
pooled_cpm: 3.61
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HEATR4

*HEAT repeat containing 4* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.49× (z +30.7, q 0e+00, up in 30 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (AsPC-1 0.0792×, LoVo 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H2030 0.0509×; ⚠ toxic); [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0514×; ⚠ unreliable plate only); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.146×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX19A-DT]] (+0.75, fdr 7e-06), [[PJVK]] (+0.74, fdr 7e-06), [[RELA-DT]] (+0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.49×** | +30.7 | 0e+00 | 30/31 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.42×** | +20.3 | 0e+00 | 27/29 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.00×** | +14.9 | 0e+00 | 3/4 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.69×** | +14.9 | 0e+00 | 10/13 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.12×** | +12.6 | 1e-34 | 6/6 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +9.7 | 2e-20 | 19/28 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.49×** | +8.8 | 1e-16 | 20/36 (SW480, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.0 | 1e-07 | 14/33 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.8 | 4e-07 | 6/17 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +5.8 | 5e-07 | 8/40 (NCI-H1573, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.6 | 9e-07 | 12/28 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.5 | 2e-06 | 9/41 (SW480, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +5.0 | 2e-05 | 14/39 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 5e-04 | 9/38 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.6 | 0.012 | 4/31 (A-427, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.015 | 6/41 (SW480, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.023 | 4/35 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.042 | 5/39 (NCI-H1573, BT-474, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11887.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (AsPC-1 0.0792×, LoVo 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H2030 0.0509×; ⚠ toxic); [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0514×; ⚠ unreliable plate only); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.146×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (drug)]] 5 µM |  | 0.774× | -3.5 | 0.19 | 10/40 (HCT15, J82, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.510× | -3.4 | 0.19 | 10/24 (HepG2/C3A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Monocrotaline (drug)]] 5 µM |  | 0.719× | -3.1 | 0.42 | 6/32 (SK-MEL-2, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 13.6 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +9.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 3.15 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +13.3) | [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM 0.0514× (z -10.2) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 18.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 2.04 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +11.4) | — |
| [[LoVo (line)]] | wt | 4.63 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.44× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.117× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +11.0) | — |
| [[A549 (line)]] | wt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 8.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0792× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 5.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.35× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 6.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0509× (z -11.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 2.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 1.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 1.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 1.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +8.8) | — |
| [[SW480 (line)]] | alt | 5.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +16.7) | — |
| [[A-172 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19A-DT]] | +0.75 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PJVK]] | +0.74 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[RELA-DT]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[MYO16]] | +0.71 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[LMNB1-DT]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RAD9B]] | +0.71 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[LINC00393]] | +0.71 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TP53TG5]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[SMG1-DT]] | +0.70 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HEATR4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (14.4, 23.0); signed map (30.0, 1.9). **Vector** length 60.5, 9.73% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +30.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +20.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.9 | +1.8 |
|  | [[NG25 (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | HEAT repeat containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,478,484-73,558,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC48595 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q86WZ0](https://www.uniprot.org/uniprotkb/Q86WZ0) carries no function annotation.

**Summary**, from NCBI Gene [399671](https://www.ncbi.nlm.nih.gov/gene/399671):

> Predicted to enable oxidoreductase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16761) · Entrez [399671](https://www.ncbi.nlm.nih.gov/gene/399671) · UniProt [Q86WZ0](https://www.uniprot.org/uniprotkb/Q86WZ0) · Ensembl [ENSG00000187105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187105)

## Data

Gene col 11887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11887); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11887]; `tensor/DDL_lfc|DDL_z.npy` [11887]; `embed/gene_vectors.npy` [11887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11887 or target_col == 11887). Every well: [[HEATR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEATR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
