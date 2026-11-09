---
symbol: "KCNG3"
type: "gene"
col: 10056
ensembl_id: "ENSG00000171126"
name: "potassium voltage-gated channel modifier subfamily G member 3"
location: "2p21"
module: 102
arm: "+"
pooled_cpm: 4.91
n_lines_expressing: 30
n_dd_up: 49
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# KCNG3

*potassium voltage-gated channel modifier subfamily G member 3* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (23 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.13× (z +25.1, q 0e+00, up in 21 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.222×, SHP-77 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.199×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0586×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0998×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A10]] (+0.64, fdr 4e-05), [[MEGF11]] (+0.60, fdr 3e-05), [[CDH23]] (+0.59, fdr 1e-05); moves opposite to [[DHX16]] (-0.49, fdr 1e-04), [[GTF3C1]] (-0.48, fdr 3e-04), [[PWP1]] (-0.46, fdr 8e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[NTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.13×** | +25.1 | 0e+00 | 21/24 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +13.2 | 2e-37 | 20/28 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.70×** | +11.9 | 1e-30 | 11/17 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.02×** | +8.8 | 2e-16 | 18/28 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.05×** | +8.7 | 6e-16 | 0/6 | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +8.5 | 2e-15 | 1/9 (HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +8.4 | 3e-15 | 13/24 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.00×** | +8.3 | 5e-15 | 7/20 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +7.9 | 2e-13 | 11/25 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.87×** | +7.8 | 3e-13 | 12/28 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.73×** | +6.9 | 4e-10 | 1/15 (LoVo) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.76×** | +6.8 | 6e-10 | 9/24 (A498, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.59×** | +5.8 | 3e-07 | 11/27 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.42×** | +5.8 | 3e-07 | 4/16 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +5.8 | 3e-07 | 10/27 (BT-474, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-06 | 8/28 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.2 | 5e-06 | 8/28 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.77×** | +5.1 | 1e-05 | 3/26 (NCI-H460, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.8 | 6e-05 | 8/24 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | **1.48×** | +4.7 | 7e-05 | 6/26 (BT-474, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 4e-04 | 4/23 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.003 | 5/27 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.022 | 2/24 (MIA PaCa-2, PANC-1) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.2 | 0.026 | 6/24 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.029 | 2/26 (RPMI-7951, A549) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.041 | 2/22 (HEC-1-A, NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10056.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.222×, SHP-77 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.199×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0586×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0998×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.810× | -3.7 | 0.12 | 4/27 (A-427, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.766× | -3.2 | 0.40 | 6/25 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | 0.785× | -3.0 | 0.50 | 7/25 (NCI-H2030, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -11.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 6.43 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +10.2) | — |
| [[A549 (line)]] | wt | 5.10 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +12.3) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0998× (z -8.5) |
| [[A-427 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 5.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0586× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 4.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A10]] | +0.64 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[MEGF11]] | +0.60 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CDH23]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.58 | +0.43 / +0.75 | both halves | 3e-05 |  |
| [[RHBDL3]] | +0.58 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[GRIP2]] | +0.57 | +0.35 / +0.68 | both halves | 1e-04 | pathway: Neuronal System |
| [[MSI1]] | +0.56 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SDK2]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ROR2]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LHX2]] | +0.54 | +0.34 / +0.71 | both halves | 1e-04 |  |
| [[NKAIN1]] | +0.52 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[NETO2]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX16]] | -0.49 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[GTF3C1]] | -0.48 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[PWP1]] | -0.46 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[WDR70]] | -0.45 | -0.25 / -0.27 | both halves | 4e-04 |  |
| [[NELFE]] | -0.44 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[DNAJC16]] | -0.43 | -0.23 / -0.28 | both halves | 5e-04 |  |
| [[IK]] | -0.43 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[TAF6]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[FAM114A2]] | -0.43 | -0.25 / -0.33 | both halves | 4e-04 |  |
| [[TBXT]] ⚠ | -0.42 | -0.31 / -0.41 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[THRAP3]] | -0.42 | -0.40 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNG3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN1]] | B | KCNG3 activity raises NTN1's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.42× lower at baseline in the lines without KCNG3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[WIPF3]] | B | KCNG3 activity raises WIPF3's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without KCNG3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[SH3GL2]] | B | KCNG3 activity raises SH3GL2's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without KCNG3 | 0.081 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[MEGF11]] | B | KCNG3 activity raises MEGF11's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without KCNG3 | 0.082 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[RASGEF1C]] | C | KCNG3 activity raises RASGEF1C's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.75× lower at baseline in the lines without KCNG3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |
| [[RBPMS2]] | C | KCNG3 activity raises RBPMS2's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without KCNG3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |
| [[LHX2]] | C | KCNG3 activity raises LHX2's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 3.07× lower at baseline in the lines without KCNG3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |
| [[PPM1E]] | C | KCNG3 activity raises PPM1E's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.46× lower at baseline in the lines without KCNG3 | 0.063 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.7, 36.4); signed map (28.3, 24.1). **Vector** length 46.4, 8.27% of its response variance represented; |z| ≥ 3 in 611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +25.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.5 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +5.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel modifier subfamily G member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:42,442,017-42,493,982 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv6.3 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAE7](https://www.uniprot.org/uniprotkb/Q8TAE7) (Voltage-gated potassium channel regulatory subunit KCNG3):

> Regulatory subunit of the voltage-gated potassium (Kv) channel which, when coassembled with KCNB1, modulates the kinetics parameters of the heterotetrameric channel namely the inactivation and deactivation rate. Potassium channel subunit that does not form functional channels by itself. Reduces the deactivation rate. Moderately accelerates activation.

**Summary**, from NCBI Gene [170850](https://www.ncbi.nlm.nih.gov/gene/170850):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, subfamily G. This member is a gamma subunit functioning as a modulatory …

**Accessions** — [HGNC:18306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18306) · Entrez [170850](https://www.ncbi.nlm.nih.gov/gene/170850) · UniProt [Q8TAE7](https://www.uniprot.org/uniprotkb/Q8TAE7) · Ensembl [ENSG00000171126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171126)

## Data

Gene col 10056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10056); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10056]; `tensor/DDL_lfc|DDL_z.npy` [10056]; `embed/gene_vectors.npy` [10056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10056 or target_col == 10056). Every well: [[KCNG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
