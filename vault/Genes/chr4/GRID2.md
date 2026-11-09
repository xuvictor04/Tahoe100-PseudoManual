---
symbol: "GRID2"
type: "gene"
col: 7600
ensembl_id: "ENSG00000152208"
name: "glutamate ionotropic receptor delta type subunit 2"
location: "4q22.1-q22.2"
module: 150
arm: "+"
pooled_cpm: 10.1
n_lines_expressing: 46
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# GRID2

*glutamate ionotropic receptor delta type subunit 2* — 4q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.19× (z +28.2, q 0e+00, up in 31 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (C-33 A 0.0572×, SK-MEL-2 0.245×; ⚠ cell-cycle shift, explains ~48% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (C-33 A 0.0721×, SK-MEL-2 0.174×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.107×, C-33 A 0.185×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.327×); [[TAK-901 (drug)]] 5 µM in 1 line (SK-MEL-2 0.0544×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN5]] (+0.77, fdr 7e-06), [[LINC01122]] (+0.76, fdr 7e-06), [[HPSE2]] (+0.75, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ST8SIA6-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[OXR1-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.19×** | +28.2 | 0e+00 | 31/35 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.79×** | +15.8 | 0e+00 | 33/39 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +11.6 | 8e-29 | 16/23 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +10.8 | 4e-25 | 4/9 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +10.1 | 4e-22 | 24/41 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +8.4 | 5e-15 | 21/32 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +8.3 | 7e-15 | 6/10 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +7.4 | 1e-11 | 18/36 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +6.6 | 2e-09 | 15/36 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.1 | 5e-08 | 12/42 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.7 | 6e-07 | 13/39 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.37×** | +4.4 | 4e-04 | 10/41 (SW48, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.002 | 6/40 (Hs 766T, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.007 | 12/42 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.020 | 17/40 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.042 | 8/34 (SHP-77, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.042 | 4/33 (SW1417, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.042 | 6/43 (NCI-H23, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (C-33 A 0.0572×, SK-MEL-2 0.245×; ⚠ cell-cycle shift, explains ~48% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (C-33 A 0.0721×, SK-MEL-2 0.174×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.107×, C-33 A 0.185×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.327×); [[TAK-901 (drug)]] 5 µM in 1 line (SK-MEL-2 0.0544×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.7 | 0.10 | 12/43 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.716× | -3.4 | 0.18 | 9/34 (H4, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -10.5) |
| [[C-33 A (line)]] | alt | 304 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0572× (z -15.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0721× (z -14.3) |
| [[A498 (line)]] | wt | 2.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 2.90 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.2× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 7.26 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 14.6× (z +10.4) | — |
| [[J82 (line)]] | alt | 3.00 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.99× (z +9.0) | [[Voriconazole (drug)]] 0.05 µM 0.0586× (z -8.8) |
| [[LS 180 (line)]] | wt | 2.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.3× (z +13.5) | — |
| [[A-172 (line)]] | wt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +10.3) | — |
| [[A549 (line)]] | wt | 2.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +9.8) | — |
| [[KATO III (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.57× (z +9.0) | — |
| [[LoVo (line)]] | wt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 6.89 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.02× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.46× (z +13.7) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 2.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +10.5) | — |
| [[A-427 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN5]] | +0.77 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[LINC01122]] | +0.76 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.75 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.75 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.75 | +0.60 / +0.80 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.74 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.73 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[RALYL]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[AGBL4]] | +0.73 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.72 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[CSMD1]] | +0.72 | +0.56 / +0.75 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST8SIA6-AS1]] | B | ST8SIA6-AS1 activity raises GRID2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 2.60× lower at baseline in the lines without ST8SIA6-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[TOP2A]] | B | TOP2A activity lowers GRID2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PI15]] | B | PI15 activity raises GRID2's level | lines that do not express PI15 (36) vs lines expressing it (14) | 3.12× lower at baseline in the lines without PI15 | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC02566, ENSG00000275016, ASCL1 |
| [[HOXD10]] | B | HOXD10 activity raises GRID2's level | lines that do not express HOXD10 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without HOXD10 | 0.079 | ⚠ within organs, on part of the lines; also absent: HOXD11, TMEM52B, PHYHIPL |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OXR1-AS1]] | C | GRID2 activity lowers OXR1-AS1's level | lines that do not express GRID2 (4) vs lines expressing it (46) | 1.81× higher at baseline in the lines without GRID2 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01811, IQCM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.9, 29.1); signed map (33.6, 16.2). **Vector** length 63.1, 9.90% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +28.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor delta type subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1-q22.2 — chr4:92,303,966-93,810,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluD2, GluR-delta-2 |
| Gene groups (HGNC) | Glutamate ionotropic receptor delta type subunits |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [O43424](https://www.uniprot.org/uniprotkb/O43424) (Glutamate receptor ionotropic, delta-2):

> Member of the ionotropic glutamate receptor family, which plays a crucial role in synaptic organization and signal transduction in the central nervous system. Although it shares structural features with ionotropic glutamate receptors, does not bind glutamate as a primary ligand. Promotes synaptogenesis and mediates the D-serine-dependent long term depression signals and AMPA receptor endocytosis of cerebellar parallel fiber-Purkinje cell (PF-PC) synapses through the NRX1B-CBLN1-GRID2 triad …

**Summary**, from NCBI Gene [2895](https://www.ncbi.nlm.nih.gov/gene/2895):

> The protein encoded by this gene is a member of the family of ionotropic glutamate receptors which are the predominant excitatory neurotransmitter receptors in the mammalian brain. The encoded protein is a multi-pass membrane protein that is expressed selectively in cerebellar Purkinje cells. A point mutation in the mouse ortholog, associated with the phenotype named 'lurcher', in the heterozygous state leads to ataxia resulting from selective, cell-autonomous apoptosis of cerebellar Purkinje …

**Accessions** — [HGNC:4576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4576) · Entrez [2895](https://www.ncbi.nlm.nih.gov/gene/2895) · UniProt [O43424](https://www.uniprot.org/uniprotkb/O43424) · Ensembl [ENSG00000152208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152208)

## Data

Gene col 7600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7600); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7600]; `tensor/DDL_lfc|DDL_z.npy` [7600]; `embed/gene_vectors.npy` [7600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7600 or target_col == 7600). Every well: [[GRID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
