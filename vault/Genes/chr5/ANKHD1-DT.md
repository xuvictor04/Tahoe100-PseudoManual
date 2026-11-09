---
symbol: "ANKHD1-DT"
type: "gene"
col: 14625
ensembl_id: "ENSG00000249637"
name: "ANKHD1 divergent transcript"
location: "5q31.3"
module: 23
arm: "+"
pooled_cpm: 4.5
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ANKHD1-DT

*ANKHD1 divergent transcript* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 14.9× (z +34.2, q 0e+00, up in 40 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXA1L-DT]] (+0.80, fdr 1e-05), [[SPEN-AS1]] (+0.80, fdr 7e-06), [[MALINC1]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **14.9×** | +34.2 | 0e+00 | 40/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.71×** | +16.6 | 0e+00 | 38/39 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.20×** | +14.7 | 0e+00 | 36/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.92×** | +12.2 | 3e-32 | 18/23 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.37×** | +12.1 | 1e-31 | 29/35 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.08×** | +11.5 | 8e-29 | 25/34 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.41×** | +11.0 | 4e-26 | 31/37 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.76×** | +11.0 | 4e-26 | 8/12 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +10.7 | 4e-25 | 6/8 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.13×** | +9.3 | 5e-19 | 23/28 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.80×** | +9.2 | 2e-18 | 31/45 (LoVo, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +9.0 | 1e-17 | 37/47 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +8.8 | 5e-17 | 32/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +8.2 | 8e-15 | 40/47 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.1 | 4e-08 | 26/47 (KATO III, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +5.9 | 1e-07 | 24/45 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +5.0 | 2e-05 | 19/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.8 | 4e-05 | 11/46 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +4.5 | 2e-04 | 16/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.792× | -3.0 | 0.91 | 5/48 (SW1417, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.18 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +18.1) | — |
| [[HEC-1-A (line)]] | alt | 6.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +17.4) | — |
| [[HOP62 (line)]] | alt | 2.28 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +13.0) | — |
| [[LoVo (line)]] | wt | 4.86 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +16.8) | — |
| [[PANC-1 (line)]] | alt | 5.66 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.2× (z +22.2) | — |
| [[C-33 A (line)]] | alt | 9.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.52× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 5.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 3.61 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.0× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 5.35 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.98× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.83 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 4.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 3.27 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 8.54 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +16.1) | — |
| [[A-172 (line)]] | wt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.2× (z +12.9) | — |
| [[A498 (line)]] | wt | 1.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 41.1× (z +15.6) | — |
| [[A549 (line)]] | wt | 2.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.9× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 7.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 2.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.0× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 5.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.3× (z +14.4) | — |
| [[C32 (line)]] | wt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 4.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.9× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 4.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 4.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 5.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +16.0) | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.1× (z +12.2) | — |
| [[J82 (line)]] | alt | 6.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +15.0) | — |
| [[KATO III (line)]] | alt | 7.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 3.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.94× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 3.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 9.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.4× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.0× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 3.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.2× (z +11.8) | — |
| [[SW48 (line)]] | wt | 5.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +8.8) | — |
| [[A-427 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXA1L-DT]] | +0.80 | +0.87 / +0.54 | both halves | 1e-05 | same gene group |
| [[SPEN-AS1]] | +0.80 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[MALINC1]] | +0.79 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.78 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.77 | +0.82 / +0.54 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.77 | +0.85 / +0.40 | both halves | 5e-05 |  |
| [[PSMD7-DT]] | +0.77 | +0.81 / +0.56 | both halves | 1e-05 | same gene group |
| [[ITFG2-AS1]] | +0.77 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.77 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.75 | +0.84 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R42]] | +0.75 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.74 | +0.79 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKHD1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises ANKHD1-DT's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without C10orf95-AS1 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (10.0, 22.1); signed map (30.0, -2.4). **Vector** length 61.3, 9.58% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +34.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +16.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +6.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.9 | +8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | +9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.1 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -0.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ANKHD1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q31.3 — chr5:140,370,891-140,401,460 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55564) · Entrez [121232368](https://www.ncbi.nlm.nih.gov/gene/121232368) · Ensembl [ENSG00000249637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249637)

## Data

Gene col 14625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14625); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14625]; `tensor/DDL_lfc|DDL_z.npy` [14625]; `embed/gene_vectors.npy` [14625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14625 or target_col == 14625). Every well: [[ANKHD1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKHD1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
