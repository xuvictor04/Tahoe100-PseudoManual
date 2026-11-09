---
symbol: "ALOXE3"
type: "gene"
col: 11004
ensembl_id: "ENSG00000179148"
name: "arachidonate epidermal lipoxygenase 3"
location: "17p13.1"
module: 158
arm: "+"
pooled_cpm: 3.0
n_lines_expressing: 45
n_dd_up: 55
n_dd_down: 0
n_dd_up_clean: 34
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# ALOXE3

*arachidonate epidermal lipoxygenase 3* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 55 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 25.8× (z +43.8, q 0e+00, up in 30 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 0.0955×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD163L1]] (+0.66, fdr 7e-06), [[TRPM2]] (+0.64, fdr 1e-05), [[IL32]] (+0.62, fdr 2e-05); moves opposite to [[NUDT21]] (-0.61, fdr 1e-05), [[MFSD14B]] (-0.59, fdr 1e-05), [[RCN2]] (-0.57, fdr 2e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 55 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **25.8×** | +43.8 | 0e+00 | 30/30 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **15.6×** | +25.1 | 0e+00 | 35/36 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **13.9×** | +25.1 | 0e+00 | 26/26 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +15.5 | 0e+00 | 23/29 (hTERT-HPNE, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.16×** | +13.6 | 5e-40 | 30/37 (SW480, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.98×** | +13.2 | 1e-37 | 31/40 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +11.1 | 8e-27 | 2/6 (PANC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +9.9 | 3e-21 | 23/37 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.72×** | +9.2 | 3e-18 | 0/3 | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +9.1 | 7e-18 | 8/12 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.89×** | +8.8 | 5e-17 | 22/34 (NCI-H23, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.52×** | +8.8 | 5e-17 | 22/35 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.50×** | +8.8 | 9e-17 | 24/41 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.45×** | +7.4 | 4e-12 | 5/10 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.16×** | +7.4 | 7e-12 | 14/38 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.04×** | +6.8 | 3e-10 | 20/37 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +6.3 | 9e-09 | 16/32 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.57×** | +6.1 | 3e-08 | 12/37 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +6.1 | 3e-08 | 14/36 (KATO III, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.0 | 4e-08 | 9/39 (PANC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11004.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 0.0955×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.757× | -3.7 | 0.11 | 9/40 (Hs 766T, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.717× | -3.1 | 0.47 | 6/40 (COLO 205, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.75 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +13.8) | — |
| [[A549 (line)]] | wt | 5.61 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +18.7) | — |
| [[SW480 (line)]] | alt | 4.35 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +18.0) | — |
| [[A-172 (line)]] | wt | 6.43 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.0× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 5.04 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +18.4) | — |
| [[PANC-1 (line)]] | alt | 1.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 6.89 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.0955× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 4.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.1× (z +16.8) | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +20.6) | — |
| [[SW48 (line)]] | wt | 5.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.4× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 1.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 126× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 1.47 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 246× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.3× (z +13.0) | — |
| [[J82 (line)]] | alt | 1.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.1× (z +9.6) | — |
| [[KATO III (line)]] | alt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.3× (z +13.4) | — |
| [[LoVo (line)]] | wt | 1.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.1× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 77.8× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 5.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.2× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 2.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.4× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 2.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.0× (z +11.8) | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.000 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD163L1]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TRPM2]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[IL32]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[NPL]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LETM2]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SBF2-AS1]] | +0.62 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[CFLAR-AS1]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MSANTD3]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[IL6R]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZNF554]] | +0.59 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[DLGAP2]] | +0.59 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[RCN2]] | -0.57 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RNF38]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RANBP9]] | -0.53 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[RPA1]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[TUFM]] | -0.52 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[UBE2G1]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TTLL5]] | -0.52 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[IPO11]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[LRRC28]] | -0.51 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[GLRX5]] | -0.51 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALOXE3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, 4.7); signed map (27.5, 11.5). **Vector** length 68.8, 12.5% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +25.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +43.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +25.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +8.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +4.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.3 | +2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.7 | +7.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | arachidonate epidermal lipoxygenase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,095,900-8,119,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eLOX3, E-LOX |
| Gene groups (HGNC) | Arachidonate lipoxygenases; Hydroperoxy icosatetraenoate dehydratases |
| Reactome | 4 pathways, smallest: Synthesis of 12-eicosatetraenoic acid derivatives; Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYJ1](https://www.uniprot.org/uniprotkb/Q9BYJ1) (Hydroperoxide isomerase ALOXE3):

> Non-heme iron-containing lipoxygenase which is atypical in that it displays a prominent hydroperoxide isomerase activity and a reduced lipoxygenases activity. The hydroperoxide isomerase activity catalyzes the isomerization of hydroperoxides, derived from arachidonic and linoleic acid by ALOX12B, into hepoxilin-type epoxyalcohols and ketones. In presence of oxygen, oxygenates polyunsaturated fatty acids, including arachidonic acid, to produce fatty acid hydroperoxides. In the skin, acts …

**Summary**, from NCBI Gene [59344](https://www.ncbi.nlm.nih.gov/gene/59344):

> This gene is a member of the lipoxygenase family, which are catabolized by arachidonic acid-derived compounds. The encoded enzyme is a hydroperoxide isomerase that synthesizes a unique type of epoxy alcohol (8R-hydroxy-11R,12R-epoxyeicosa-5Z,9E,14Z-trienoic acid) from 12R-hydroperoxyeicosatetraenoic acid (12R-HPETE). This epoxy alcohol can activate the the nuclear receptor peroxisome proliferator-activated receptor alpha (PPARalpha), which is implicated in epidermal differentiation. Loss of …

**Accessions** — [HGNC:13743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13743) · Entrez [59344](https://www.ncbi.nlm.nih.gov/gene/59344) · UniProt [Q9BYJ1](https://www.uniprot.org/uniprotkb/Q9BYJ1) · Ensembl [ENSG00000179148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179148)

## Data

Gene col 11004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11004); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11004]; `tensor/DDL_lfc|DDL_z.npy` [11004]; `embed/gene_vectors.npy` [11004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11004 or target_col == 11004). Every well: [[ALOXE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALOXE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
