---
symbol: "DNAI7"
type: "gene"
col: 3980
ensembl_id: "ENSG00000118307"
name: "dynein axonemal intermediate chain 7"
location: "12p12.1"
module: 37
arm: "+"
pooled_cpm: 3.99
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 0
n_dd_up_clean: 37
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DNAI7

*dynein axonemal intermediate chain 7* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.43× (z +21.0, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.0921×, HEC-1-A 0.103×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.108×); [[Epirubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (BT-474 0.0489×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC13]] (+0.64, fdr 7e-06), [[LINC02763]] (+0.61, fdr 7e-06), [[SLC7A9]] (+0.61, fdr 1e-05); moves opposite to [[ANGEL1]] (-0.58, fdr 3e-05), [[KLHL8]] (-0.51, fdr 2e-04), [[BTF3L4]] (-0.50, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXCL13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.43×** | +21.0 | 0e+00 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.03×** | +17.0 | 0e+00 | 42/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +16.9 | 0e+00 | 33/33 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.65×** | +14.8 | 0e+00 | 43/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +12.3 | 8e-33 | 24/38 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +9.3 | 2e-18 | 15/32 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.9 | 3e-13 | 3/6 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +7.7 | 8e-13 | 18/46 (SW 900, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.6 | 2e-12 | 3/10 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.3 | 2e-11 | 7/20 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.0 | 9e-11 | 16/38 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +6.7 | 1e-09 | 17/43 (HEC-1-A, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +6.3 | 1e-08 | 18/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.9 | 2e-07 | 12/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.73×** | +5.5 | 1e-06 | 16/39 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.72×** | +5.4 | 2e-06 | 14/40 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 9e-06 | 10/36 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.9 | 4e-05 | 10/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3980.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.0921×, HEC-1-A 0.103×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.108×); [[Epirubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (BT-474 0.0489×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Aprepitant (drug)]] 0.05 µM |  | 0.741× | -3.2 | 0.46 | 6/43 (HS-578T, CHP-212, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.752× | -3.0 | 0.46 | 8/46 (NCI-H23, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.37 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 26.4× (z +12.4) | — |
| [[SW480 (line)]] | alt | 4.38 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 7.17 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +8.7) | [[Docetaxel (drug)]] 0.05 µM 0.0921× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 2.72 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 18.7× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 5.34 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 0.0489× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 7.09 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.108× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 5.59 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 3.89 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.6× (z +9.4) | — |
| [[LoVo (line)]] | wt | 5.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 7.62 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.110× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.48 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0692× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.86× (z +8.8) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC13]] | +0.64 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.61 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SLC7A9]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[POLN]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CMYA5]] | +0.61 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SLC5A11]] | +0.61 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[FRZB]] | +0.59 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DRC1]] | +0.59 | +0.66 / +0.60 | both halves | 7e-06 | STRING 507 |
| [[TOMM20L-DT]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.58 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PRRT3]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[LDHC]] | +0.58 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL1]] | -0.58 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[KLHL8]] | -0.51 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[BTF3L4]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZFAND4]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[TMEM209]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL13]] | B | CXCL13 activity raises DNAI7's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without CXCL13 | 0.059 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DNAI7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.1, -12.4); signed map (15.1, 6.3). **Vector** length 59.4, 8.51% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +5.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal intermediate chain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:25,108,289-25,195,162 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAS1, FLJ10921, PPP1R54; previously CASC1, CFAP94 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Dyneins, axonemal inner arm I1/f complex subunits; Dynein intermediate chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6TDU7](https://www.uniprot.org/uniprotkb/Q6TDU7) (Dynein axonemal intermediate chain 7):

> Via its association with the multisubunit axonemal dynein complex, is potentially involved in the regulation of cilia function. May also act as a cell cycle regulator.

**Summary**, from NCBI Gene [55259](https://www.ncbi.nlm.nih.gov/gene/55259):

> Predicted to enable beta-tubulin binding activity and microtubule binding activity. Predicted to be located in cilium and microtubule cytoskeleton. Predicted to be part of axonemal dynein complex. Predicted to be active in axoneme and cytoplasmic microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29599) · Entrez [55259](https://www.ncbi.nlm.nih.gov/gene/55259) · UniProt [Q6TDU7](https://www.uniprot.org/uniprotkb/Q6TDU7) · Ensembl [ENSG00000118307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118307)

## Data

Gene col 3980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3980); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3980]; `tensor/DDL_lfc|DDL_z.npy` [3980]; `embed/gene_vectors.npy` [3980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3980 or target_col == 3980). Every well: [[DNAI7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAI7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
