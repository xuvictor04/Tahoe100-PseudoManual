---
symbol: "CCDC62"
type: "gene"
col: 5127
ensembl_id: "ENSG00000130783"
name: "coiled-coil domain containing 62"
location: "12q24.31"
module: 37
arm: "+"
pooled_cpm: 11.15
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CCDC62

*coiled-coil domain containing 62* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.58× (z +24.1, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.669× (z -3.9, q 0.064, down in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.235×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0956×; ⚠ toxic; cell-cycle shift, explains ~11% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (HS-578T 0.134×); [[Raltitrexed (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.86, fdr 7e-06), [[MSH4]] (+0.77, fdr 7e-06), [[NUP210L]] (+0.77, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.58×** | +24.1 | 0e+00 | 46/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.32×** | +13.9 | 1e-41 | 40/46 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.86×** | +13.4 | 1e-38 | 46/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +12.1 | 2e-31 | 34/46 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.52×** | +12.0 | 4e-31 | 32/39 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.32×** | +11.4 | 3e-28 | 38/46 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.7 | 2e-20 | 14/20 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +8.7 | 2e-16 | 30/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.5 | 2e-15 | 29/48 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +8.2 | 1e-14 | 16/26 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.1 | 5e-11 | 23/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +6.3 | 1e-08 | 28/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.1 | 5e-08 | 26/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +4.7 | 1e-04 | 12/22 (A549, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 3e-04 | 22/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.003 | 20/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.005 | 11/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.018 | 12/48 (RKO, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.038 | 13/47 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.049 | 12/48 (SW480, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5127.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.235×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0956×; ⚠ toxic; cell-cycle shift, explains ~11% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (HS-578T 0.134×); [[Raltitrexed (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.064 | 19/46 (C-33 A, NCI-H23, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.537× | -3.2 | 0.34 | 15/43 (H4, SW48, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.798× | -3.0 | 0.48 | 8/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.66 | 9 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.10× (z +12.7) | — |
| [[LoVo (line)]] | wt | 9.90 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 31.7× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 12.1 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +13.5) | [[Harringtonine (drug)]] 0.05 µM 0.134× (z -9.3) |
| [[A498 (line)]] | wt | 8.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +13.5) | — |
| [[J82 (line)]] | alt | 5.64 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 5.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.88 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +9.5) | [[Raltitrexed (drug)]] 0.5 µM 0.0725× (z -9.1) |
| [[PANC-1 (line)]] | alt | 8.06 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +13.2) | — |
| [[RKO (line)]] | wt | 22.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +12.4) | — |
| [[SW48 (line)]] | wt | 16.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +8.7) | — |
| [[A-172 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +13.0) | — |
| [[A549 (line)]] | wt | 7.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 5.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.2× (z +15.0) | — |
| [[BT-474 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +10.4) | — |
| [[C32 (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 4.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0956× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[KATO III (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 8.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 7.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.89× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 7.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.97× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 5.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 6.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +10.7) | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.86 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[MSH4]] | +0.77 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[SNX31]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.77 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.75 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[NPHP3-ACAD11]] | +0.75 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[CORIN]] | +0.75 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[WDR49]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[RRH]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC62's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, -16.3); signed map (13.2, 5.9). **Vector** length 106, 27.1% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +24.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.9 | +13.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +13.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +8.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.5 |
|  | [[NG25 (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,774,526-122,827,528 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSP-NY, FLJ40344, CT109, ERAP75 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9F0](https://www.uniprot.org/uniprotkb/Q6P9F0) (Coiled-coil domain-containing protein 62):

> Nuclear receptor coactivator that can enhance preferentially estrogen receptors ESR1 and ESR2 transactivation. Also modulates progesterone/PGR, glucocorticoid/NR3C1 and androgen/AR receptors transactivation, although at lower level; little effect on vitamin D receptor/VDR. Required for normal spermiogenesis. It probably plays a role in acrosome formation (By similarity).

**Summary**, from NCBI Gene [84660](https://www.ncbi.nlm.nih.gov/gene/84660):

> Enables nuclear estrogen receptor binding activity and transcription coactivator activity. Involved in several processes, including cellular response to estradiol stimulus; estrogen receptor signaling pathway; and positive regulation of transcription by RNA polymerase II. Located in acrosomal vesicle and nucleoplasm. Implicated in spermatogenic failure 67. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30723) · Entrez [84660](https://www.ncbi.nlm.nih.gov/gene/84660) · UniProt [Q6P9F0](https://www.uniprot.org/uniprotkb/Q6P9F0) · Ensembl [ENSG00000130783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130783)

## Data

Gene col 5127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5127); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5127]; `tensor/DDL_lfc|DDL_z.npy` [5127]; `embed/gene_vectors.npy` [5127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5127 or target_col == 5127). Every well: [[CCDC62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
