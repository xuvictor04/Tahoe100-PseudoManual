---
symbol: "TRIM59"
type: "gene"
col: 13088
ensembl_id: "ENSG00000213186"
name: "tripartite motif containing 59"
location: "3q25.33"
module: 39
arm: "+"
pooled_cpm: 21.51
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TRIM59

*tripartite motif containing 59* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.87× (z +27.4, q 0e+00, up in 42 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.195×, HCT15 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (J82 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.203×); [[Flumatinib (mesylate) (drug)]] 5 µM in 1 line (A-427 0.0663×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01934]] (+0.78, fdr 7e-06), [[DPYS]] (+0.71, fdr 7e-06), [[MYH15]] (+0.70, fdr 1e-05); moves opposite to [[PPP1R12B]] (-0.62, fdr 3e-05), [[MPPE1]] (-0.61, fdr 2e-05), [[CCZ1B]] (-0.60, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.87×** | +27.4 | 0e+00 | 42/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +22.2 | 0e+00 | 40/45 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +13.1 | 9e-37 | 39/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +10.7 | 2e-24 | 37/44 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +8.0 | 2e-13 | 12/46 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.75×** | +7.7 | 9e-13 | 28/45 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.7 | 1e-12 | 28/46 (HOP62, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +7.5 | 5e-12 | 28/45 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +6.5 | 7e-09 | 31/46 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.53×** | +6.0 | 1e-07 | 11/27 (SW480, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 3e-06 | 19/44 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.44×** | +4.9 | 4e-05 | 15/34 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +4.5 | 3e-04 | 15/46 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 17/44 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +4.4 | 4e-04 | 15/46 (NCI-H2347, A-172, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.001 | 15/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.004 | 16/46 (Panc 03.27, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.004 | 14/46 (SW1417, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.005 | 19/44 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13088.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.195×, HCT15 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (J82 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.203×); [[Flumatinib (mesylate) (drug)]] 5 µM in 1 line (A-427 0.0663×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.845× | -3.4 | 0.44 | 13/46 (H4, NCI-H23, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.747× | -3.1 | 0.44 | 8/43 (HEC-1-A, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | 0.750× | -3.0 | 0.44 | 5/46 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 14.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +17.3) | — |
| [[HCT15 (line)]] | alt | 25.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[HS-578T (line)]] | alt | 11.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +11.9) | — |
| [[LoVo (line)]] | wt | 11.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +20.6) | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 9.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +15.7) | — |
| [[C32 (line)]] | wt | 6.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 12.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +14.1) | — |
| [[A-172 (line)]] | wt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.5) | — |
| [[A-427 (line)]] | wt | 7.71 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0663× (z -8.7) |
| [[A498 (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 46.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.203× (z -9.1) |
| [[COLO 205 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 8.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.4) | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 66.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +15.4) | — |
| [[SNU-1 (line)]] | wt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SNU-423 (line)]] | alt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.1) | — |
| [[SW480 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | — |
| [[A549 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01934]] | +0.78 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[DPYS]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MYH15]] | +0.70 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[GARIN1B]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[MPP4]] | +0.70 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.69 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[C21orf91-OT1]] | +0.69 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[LINC00486]] | +0.69 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[MMP25]] | +0.69 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[SLC6A13]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[UBE2D3-AS1]] | +0.68 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[LINC01191]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[MPPE1]] | -0.61 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CCZ1B]] | -0.60 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[SHQ1]] | -0.59 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[MYPOP]] | -0.59 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[SLC9A6]] | -0.58 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[PLA2G12A]] | -0.57 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[UNC45A]] | -0.57 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[TSC2]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.57 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[PLD3]] | -0.57 | -0.57 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRIM59's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00334]] | B | LINC00334 activity strengthens TRIM59's drug response | lines that do not express LINC00334 (10) vs lines expressing it (36) | the lines without LINC00334 respond 1.02× as strongly (z diff +0.21); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.16x vs 1.62x (z diff +2.2) | 0.082 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[BTG3-AS1]] | B | BTG3-AS1 activity raises TRIM59's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without BTG3-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -12.1); signed map (19.5, 9.0). **Vector** length 96.3, 21.3% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.1 | +27.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +22.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 59 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33 — chr3:160,432,445-160,485,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSBF1, Mrf1, RNF104; previously TRIM57 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWR1](https://www.uniprot.org/uniprotkb/Q8IWR1) (Tripartite motif-containing protein 59):

> E3 ubiquitin ligase involved in different processes such as development and immune response. Serves as a negative regulator for innate immune signaling pathways by suppressing RLR-induced activation of IRF3/7 and NF-kappa-B via interaction with adapter ECSIT. Regulates autophagy through modulating both the transcription and the ubiquitination of BECN1. On the one hand, regulates the transcription of BECN1 through negatively modulating the NF-kappa-B pathway. On the other hand, regulates …

**Summary**, from NCBI Gene [286827](https://www.ncbi.nlm.nih.gov/gene/286827):

> Predicted to enable ubiquitin protein ligase activity. Acts upstream of or within negative regulation of canonical NF-kappaB signal transduction. Predicted to be located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30834) · Entrez [286827](https://www.ncbi.nlm.nih.gov/gene/286827) · UniProt [Q8IWR1](https://www.uniprot.org/uniprotkb/Q8IWR1) · Ensembl [ENSG00000213186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213186)

## Data

Gene col 13088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13088); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13088]; `tensor/DDL_lfc|DDL_z.npy` [13088]; `embed/gene_vectors.npy` [13088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13088 or target_col == 13088). Every well: [[TRIM59 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM59.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
