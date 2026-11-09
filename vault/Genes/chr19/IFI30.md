---
symbol: "IFI30"
type: "gene"
col: 13282
ensembl_id: "ENSG00000216490"
name: "IFI30 lysosomal thiol reductase"
location: "19p13.11"
module: 70
arm: "+"
pooled_cpm: 12.94
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# IFI30

*IFI30 lysosomal thiol reductase* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.60× (z +12.1, q 4e-31, up in 39 of 43 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 2.03× (z +8.0, q 2e-13, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.575× (z -4.2, q 0.017, down in 22 of 41 measured lines) ⚠ cell-cycle shift, explains ~39% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (H4 0.0546×, SK-MEL-2 0.0973×; ⚠ cell-cycle shift, explains ~39% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SNU-423 0.0748×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0681×; ⚠ cell-cycle shift, would explain all of this change); [[Erlotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.0835×); [[Rapamycin (drug)]] 0.5 µM in 1 line (C32 0.0583×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB9]] (+0.70, fdr 7e-06), [[LY6E]] (+0.68, fdr 1e-05), [[B2M]] (+0.67, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CNP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **4.60×** | +12.1 | 4e-31 | 39/43 (HCT15, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.53×** | +12.0 | 9e-31 | 41/42 (HCT15, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.51×** | +9.6 | 1e-19 | 16/18 (SHP-77, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **3.25×** | +9.4 | 9e-19 | 26/33 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.11×** | +8.4 | 6e-15 | 33/40 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.03×** | +8.0 | 2e-13 | 37/43 (NCI-H2347, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.55×** | +7.5 | 7e-12 | 32/43 (HCT15, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.20×** | +6.3 | 3e-08 | 30/37 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **2.09×** | +5.4 | 4e-06 | 19/28 (KATO III, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.01×** | +5.4 | 5e-06 | 27/36 (J82, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.86×** | +4.7 | 1e-04 | 23/41 (A498, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +4.7 | 1e-04 | 25/41 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.85×** | +4.7 | 1e-04 | 24/38 (A498, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.78×** | +4.6 | 2e-04 | 23/43 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 23/43 (Hs 766T, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.008 | 16/42 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13282.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (H4 0.0546×, SK-MEL-2 0.0973×; ⚠ cell-cycle shift, explains ~39% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SNU-423 0.0748×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0681×; ⚠ cell-cycle shift, would explain all of this change); [[Erlotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.0835×); [[Rapamycin (drug)]] 0.5 µM in 1 line (C32 0.0583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.575×** | -4.2 | 0.017 | 22/41 (H4, SK-MEL-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.443× | -3.4 | 0.15 | 20/41 (BT-474, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.656× | -3.4 | 0.15 | 17/41 (SW480, HCT15, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.750× | -3.3 | 0.16 | 15/41 (A-172, NCI-H2347, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.486× | -3.0 | 0.30 | 10/43 (SHP-77, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.94 | 2 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 10.6× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0681× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Erlotinib (drug)]] 5 µM 0.0835× (z -8.9) |
| [[HCT15 (line)]] | alt | 12.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 20.7× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.41× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.47× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[SHP-77 (line)]] | alt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[SNU-423 (line)]] | alt | 9.75 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 8.58× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0748× (z -10.8) |
| [[SW480 (line)]] | alt | 8.11 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[A549 (line)]] | wt | 6.03 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C32 (line)]] | wt | 5.71 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0583× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0546× (z -10.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 6.23 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.75× (z +9.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.16× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.03 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +10.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0973× (z -8.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB9]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[LY6E]] | +0.68 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[B2M]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TAP1]] | +0.67 | +0.74 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[UBE2L6]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI6]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 495 |
| [[IFITM3]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 516 |
| [[HLA-B]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PSME1]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[GBP4]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[BST2]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[ISG15]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IFI30's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BST2]] | B | BST2 activity raises IFI30's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without BST2 | 0.073 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNP]] | B | IFI30 activity raises CNP's level | lines that do not express IFI30 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without IFI30 | 0.089 | ⚠ within organs, on part of the lines; also absent: RAP1GAP2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.7, 50.5); signed map (65.6, 28.0). **Vector** length 77.9, 18.7% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.59 to 14); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.57 to 8); *ER-Phagosome pathway* (reactome, mean cos +0.60 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +2.6 | +5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.2 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | IFI30 lysosomal thiol reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,173,162-18,178,117 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFI-30, GILT, IP30, MGC32056, IP-30 |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: Processing of antigen in germinal center B cells; Interferon gamma signaling; MHC class II antigen presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13284](https://www.uniprot.org/uniprotkb/P13284) (Gamma-interferon-inducible lysosomal thiol reductase):

> Lysosomal thiol reductase that catalyzes protein disulfide bonds reduction. Plays an important role in antigen processing and presentation, of namely both major histocompatibility complex (MHC) class I- and class II-restricted antigen by reducing the disulfide bonds of endocytosed proteins and facilitating their unfolding and optimal degradation. Shares with thioredoxin a reduction mechanism in which the N-terminal cysteine thiol group in the CXXC active site motif initiates a nucleophilic …

**Summary**, from NCBI Gene [10437](https://www.ncbi.nlm.nih.gov/gene/10437):

> The protein encoded by this gene is a lysosomal thiol reductase that at low pH can reduce protein disulfide bonds. The enzyme is expressed constitutively in antigen-presenting cells and induced by gamma-interferon in other cell types. This enzyme has an important role in MHC class II-restricted antigen processing. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5398) · Entrez [10437](https://www.ncbi.nlm.nih.gov/gene/10437) · UniProt [P13284](https://www.uniprot.org/uniprotkb/P13284) · Ensembl [ENSG00000216490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000216490)

## Data

Gene col 13282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13282); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13282]; `tensor/DDL_lfc|DDL_z.npy` [13282]; `embed/gene_vectors.npy` [13282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13282 or target_col == 13282). Every well: [[IFI30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
