---
symbol: "CASS4"
type: "gene"
col: 1512
ensembl_id: "ENSG00000087589"
name: "Cas scaffold protein family member 4"
location: "20q13.31"
module: 23
arm: "+"
pooled_cpm: 4.34
n_lines_expressing: 48
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 34
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CASS4

*Cas scaffold protein family member 4* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 13.1× (z +26.5, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.577× (z -4.1, q 0.027, down in 21 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0418×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HCT15 0.0912×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.0698×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAI4]] (+0.83, fdr 7e-06), [[CCDC30]] (+0.83, fdr 7e-06), [[CFAP53]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02641]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **13.1×** | +26.5 | 0e+00 | 36/36 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **12.4×** | +17.6 | 0e+00 | 33/34 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **8.86×** | +15.2 | 0e+00 | 32/35 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.97×** | +14.1 | 3e-43 | 33/38 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **7.09×** | +13.7 | 1e-40 | 17/19 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.16×** | +11.9 | 9e-31 | 37/42 (SW480, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.85×** | +10.7 | 7e-25 | 30/45 (SW1417, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.03×** | +10.1 | 3e-22 | 34/37 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.77×** | +7.4 | 1e-11 | 30/43 (NCI-H2030, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.38×** | +6.3 | 2e-08 | 23/45 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **2.16×** | +5.5 | 1e-06 | 19/45 (SW480, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +5.5 | 1e-06 | 2/10 (BT-474, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.15×** | +5.3 | 5e-06 | 20/41 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.02×** | +5.1 | 2e-05 | 16/41 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +4.9 | 3e-05 | 19/44 (SW480, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +4.5 | 2e-04 | 17/42 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.91×** | +4.5 | 2e-04 | 17/40 (LoVo, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0418×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HCT15 0.0912×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.0698×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -4.1 | 0.027 | 21/43 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -3.7 | 0.071 | 9/46 (HCT15, A-172, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.631× | -3.4 | 0.12 | 12/46 (SK-MEL-2, CHP-212, …) | all doses, flat | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.626× | -3.3 | 0.14 | 6/39 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.647× | -3.2 | 0.14 | 12/45 (SW 1271, SW480, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.77 | 6 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 18.8× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 3.41 | 2 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 30.1× (z +9.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 9.44× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0418× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 2.32 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 13.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 4.33 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0912× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 6.22 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +10.1) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0698× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.97 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.5× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 3.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.7× (z +12.4) | — |
| [[LoVo (line)]] | wt | 3.97 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 4.38 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.79 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 3.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 4.82 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.8× (z +13.2) | — |
| [[A-172 (line)]] | wt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +11.3) | — |
| [[A498 (line)]] | wt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 7.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.19× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.1× (z +10.1) | — |
| [[J82 (line)]] | alt | 2.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.1× (z +9.8) | — |
| [[KATO III (line)]] | alt | 2.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.4× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 2.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.6× (z +10.0) | — |
| [[SW48 (line)]] | wt | 6.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +9.0) | — |
| [[A-427 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.915 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | +0.83 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.83 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.82 | +0.86 / +0.59 | both halves | 7e-06 |  |
| [[TAS2R4]] | +0.82 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.82 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.82 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.81 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[MGAM]] | +0.81 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.81 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SNX31]] | +0.81 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[LSMEM1]] | +0.79 | +0.77 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02641]] | B | LINC02641 activity raises CASS4's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without LINC02641 | 0.012 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[CXCL13]] | B | CXCL13 activity raises CASS4's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without CXCL13 | 0.028 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CASS4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00159]] | C | LINC00159 activity raises CASS4's level | lines that do not express LINC00159 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without LINC00159 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF391, LINC01341, HHAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (10.8, 17.4); signed map (23.1, -0.9). **Vector** length 100, 22.9% of its response variance represented; |z| ≥ 3 in 1,279 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +26.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +17.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +5.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -6.7 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Cas scaffold protein family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:56,412,112-56,460,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEFL, HEPL; previously C20orf32 |
| Gene groups (HGNC) | Cas scaffold protein family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ75](https://www.uniprot.org/uniprotkb/Q9NQ75) (Cas scaffolding protein family member 4):

> Docking protein that plays a role in tyrosine kinase-based signaling related to cell adhesion and cell spreading. Regulates PTK2/FAK1 activity, focal adhesion integrity, and cell spreading.

**Summary**, from NCBI Gene [57091](https://www.ncbi.nlm.nih.gov/gene/57091):

> Enables protein tyrosine kinase binding activity. Involved in several processes, including positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; positive regulation of protein tyrosine kinase activity; and positive regulation of substrate adhesion-dependent cell spreading. Located in cytoplasm and focal adhesion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15878) · Entrez [57091](https://www.ncbi.nlm.nih.gov/gene/57091) · UniProt [Q9NQ75](https://www.uniprot.org/uniprotkb/Q9NQ75) · Ensembl [ENSG00000087589](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087589)

## Data

Gene col 1512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1512); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1512]; `tensor/DDL_lfc|DDL_z.npy` [1512]; `embed/gene_vectors.npy` [1512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1512 or target_col == 1512). Every well: [[CASS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
